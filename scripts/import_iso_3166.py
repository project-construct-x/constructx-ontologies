#!/usr/bin/env python3
"""Import current ISO 3166 reference data from EU authority tables."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import DCTERMS, OWL, SKOS, XSD


ENDPOINT = "https://publications.europa.eu/webapi/rdf/sparql"
SOURCE_VERSION = "20260617-0"
DATASET_VERSION = "0.1.0"
RELEASE_DATE = "2026-08-18"

EUVOC = Namespace("http://publications.europa.eu/ontology/euvoc#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
ADDR = Namespace("https://www.construct-x.org/ontology/address#")
COUNTRIES = Namespace("https://www.construct-x.org/vocab/country#")
AREAS = Namespace("https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#")
ID_SCHEME = Namespace("https://www.construct-x.org/vocab/identifier-scheme#")
SCHEMA = Namespace("https://schema.org/")

COUNTRY_SCHEME = URIRef("https://www.construct-x.org/vocab/country")
AREA_SCHEME = URIRef(
    "https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de"
)
ISO_SOURCE = URIRef("https://www.iso.org/iso-3166-country-codes.html")
EU_COUNTRY_DATASET = URIRef("http://publications.europa.eu/resource/dataset/country")
EU_ATU_DATASET = URIRef("http://publications.europa.eu/resource/dataset/atu")

ALPHA_2 = URIRef(f"{EUVOC}ISO_3166_1_ALPHA_2")
ALPHA_3 = URIRef(f"{EUVOC}ISO_3166_1_ALPHA_3")
ISO_NUMERIC = URIRef(f"{EUVOC}ISO_3166_1_NUM")
UNSD_M49 = URIRef(f"{EUVOC}UNSD_M49")
ISO_3166_2 = URIRef(f"{EUVOC}ISO_3166_2")

NETWORK_ALPHA_2 = URIRef(f"{ID_SCHEME}iso-3166-1-alpha-2")
NETWORK_ALPHA_3 = URIRef(f"{ID_SCHEME}iso-3166-1-alpha-3")
NETWORK_NUMERIC = URIRef(f"{ID_SCHEME}iso-3166-1-numeric")
NETWORK_ISO_3166_2 = URIRef(f"{ID_SCHEME}iso-3166-2")

# These entries occur in the EU authority table but are not current ISO 3166-1
# assignments. They are deliberately excluded from this ISO dataset.
NON_CURRENT_ISO_ENTRIES = {"CPT", "CRQ", "FXX", "XKX"}

# The EU graph currently publishes these two ISO numeric values with the M49
# datatype only. Both values are checked explicitly before they are accepted.
NUMERIC_FALLBACKS = {"NPL": "524", "SHN": "654"}

# EU ATU source version 20260617-0 assigns DE-ST to the resource DEU_LD_SN.
# ISO 3166-2 assigns DE-SN to Saxony, so this exact source defect is corrected
# and rejected if the upstream value changes unexpectedly.
SAXONY_SOURCE = "http://publications.europa.eu/resource/authority/atu/DEU_LD_SN"

GERMAN_SUBDIVISIONS = {
    "DE-BB",
    "DE-BE",
    "DE-BW",
    "DE-BY",
    "DE-HB",
    "DE-HE",
    "DE-HH",
    "DE-MV",
    "DE-NI",
    "DE-NW",
    "DE-RP",
    "DE-SH",
    "DE-SL",
    "DE-SN",
    "DE-ST",
    "DE-TH",
}

COUNTRY_CODES_QUERY = f"""
PREFIX euvoc: <http://publications.europa.eu/ontology/euvoc#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?country ?notation (DATATYPE(?notation) AS ?scheme) ?version WHERE {{
  ?country a euvoc:Country ;
    euvoc:status
      <http://publications.europa.eu/resource/authority/concept-status/CURRENT> ;
    skos:notation ?notation ;
    owl:versionInfo ?version .
  FILTER(DATATYPE(?notation) IN (
    <{ALPHA_2}>, <{ALPHA_3}>, <{ISO_NUMERIC}>, <{UNSD_M49}>
  ))
}}
"""

COUNTRY_LABELS_QUERY = """
PREFIX euvoc: <http://publications.europa.eu/ontology/euvoc#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?country ?label ?version WHERE {
  ?country a euvoc:Country ;
    euvoc:status
      <http://publications.europa.eu/resource/authority/concept-status/CURRENT> ;
    skos:prefLabel ?label ;
    owl:versionInfo ?version .
  FILTER(LANG(?label) IN ("de", "en"))
}
"""

GERMAN_AREAS_QUERY = f"""
PREFIX country: <http://publications.europa.eu/resource/authority/country/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX euvoc: <http://publications.europa.eu/ontology/euvoc#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?area ?code ?label ?version WHERE {{
  ?area a euvoc:Atu ;
    euvoc:countryCode country:DEU ;
    dct:type ?type ;
    skos:notation ?code ;
    skos:prefLabel ?label ;
    owl:versionInfo ?version .
  VALUES ?type {{
    <http://publications.europa.eu/resource/authority/atu-type/DEU_LD>
    <http://publications.europa.eu/resource/authority/atu-type/DEU_STS>
  }}
  FILTER(DATATYPE(?code) = <{ISO_3166_2}>)
  FILTER(LANG(?label) IN ("de", "en"))
}}
"""


def fetch_bindings(query: str) -> list[dict[str, dict[str, str]]]:
    query_string = urlencode(
        {"query": query, "format": "application/sparql-results+json"}
    )
    request = Request(
        f"{ENDPOINT}?{query_string}",
        headers={
            "Accept": "application/sparql-results+json",
            "User-Agent": "construct-x-ontologies-iso-import/0.1",
        },
    )
    with urlopen(request, timeout=120) as response:
        payload = json.load(response)
    return payload["results"]["bindings"]


def value(binding: dict[str, dict[str, str]], key: str) -> str:
    return binding[key]["value"]


def load_countries() -> list[dict[str, object]]:
    codes: dict[str, dict[str, str]] = defaultdict(dict)
    labels: dict[str, dict[str, str]] = defaultdict(dict)
    versions: set[str] = set()

    for row in fetch_bindings(COUNTRY_CODES_QUERY):
        country = value(row, "country")
        codes[country][value(row, "scheme")] = value(row, "notation")
        versions.add(value(row, "version"))

    for row in fetch_bindings(COUNTRY_LABELS_QUERY):
        country = value(row, "country")
        label = row["label"]
        language = label.get("xml:lang")
        if language in {"de", "en"}:
            labels[country][language] = label["value"]
        versions.add(value(row, "version"))

    if versions != {SOURCE_VERSION}:
        raise ValueError(f"Unexpected EU country source versions: {sorted(versions)}")

    countries: list[dict[str, object]] = []
    for source, identifiers in codes.items():
        alpha_2 = identifiers.get(str(ALPHA_2))
        alpha_3 = identifiers.get(str(ALPHA_3))
        if not alpha_2 or not alpha_3 or alpha_3 in NON_CURRENT_ISO_ENTRIES:
            continue

        numeric = identifiers.get(str(ISO_NUMERIC))
        if numeric is None:
            numeric = identifiers.get(str(UNSD_M49))
            if numeric != NUMERIC_FALLBACKS.get(alpha_3):
                raise ValueError(
                    f"Unapproved numeric-code fallback for {alpha_3}: {numeric!r}"
                )

        country_labels = labels.get(source, {})
        if set(country_labels) != {"de", "en"}:
            raise ValueError(f"Missing German or English label for {alpha_3}")

        countries.append(
            {
                "source": source,
                "alpha_2": alpha_2,
                "alpha_3": alpha_3,
                "numeric": numeric.zfill(3),
                "labels": country_labels,
            }
        )

    countries.sort(key=lambda item: str(item["alpha_3"]))
    if len(countries) != 249:
        raise ValueError(f"Expected 249 current ISO countries, got {len(countries)}")
    for key in ("alpha_2", "alpha_3", "numeric"):
        if len({item[key] for item in countries}) != 249:
            raise ValueError(f"ISO {key} values are not unique")
    return countries


def load_german_areas() -> list[dict[str, object]]:
    areas: dict[str, dict[str, object]] = {}
    versions: set[str] = set()
    for row in fetch_bindings(GERMAN_AREAS_QUERY):
        source = value(row, "area")
        source_code = value(row, "code")
        if source == SAXONY_SOURCE:
            if source_code != "DE-ST":
                raise ValueError(
                    f"Unexpected Saxony source code; review correction: {source_code}"
                )
            code = "DE-SN"
        else:
            code = source_code
        entry = areas.setdefault(
            code,
            {"source": source, "code": code, "labels": {}},
        )
        label = row["label"]
        language = label.get("xml:lang")
        if language in {"de", "en"}:
            entry["labels"][language] = label["value"]
        versions.add(value(row, "version"))

    if versions != {SOURCE_VERSION}:
        raise ValueError(f"Unexpected EU ATU source versions: {sorted(versions)}")
    if set(areas) != GERMAN_SUBDIVISIONS:
        raise ValueError(
            "Unexpected German ISO 3166-2 coverage: "
            f"missing={sorted(GERMAN_SUBDIVISIONS - set(areas))}, "
            f"extra={sorted(set(areas) - GERMAN_SUBDIVISIONS)}"
        )
    for code, area in areas.items():
        if "de" not in area["labels"]:
            raise ValueError(f"Missing German label for {code}")
    return [areas[code] for code in sorted(areas)]


def bind_prefixes(graph: Graph) -> None:
    for prefix, namespace in (
        ("adms", ADMS),
        ("conx-addr", ADDR),
        ("countries", COUNTRIES),
        ("areas", AREAS),
        ("dcterms", DCTERMS),
        ("id-scheme", ID_SCHEME),
        ("owl", OWL),
        ("rdf", RDF),
        ("rdfs", RDFS),
        ("schema", SCHEMA),
        ("skos", SKOS),
        ("xsd", XSD),
    ):
        graph.bind(prefix, namespace, override=True, replace=True)


def add_creator(graph: Graph, subject: URIRef, suffix: str) -> None:
    creator = BNode(f"creator-{suffix}")
    organization = BNode(f"organization-{suffix}")
    graph.add((subject, DCTERMS.creator, creator))
    graph.add((creator, RDF.type, SCHEMA.Person))
    graph.add((creator, SCHEMA.email, URIRef("mailto:sven.zentgraf@rub.de")))
    graph.add(
        (
            creator,
            SCHEMA.identifier,
            URIRef("https://orcid.org/0000-0001-6058-7614"),
        )
    )
    graph.add((creator, SCHEMA.memberOf, organization))
    graph.add(
        (
            organization,
            SCHEMA.identifier,
            URIRef(
                "https://www.inf.bi.ruhr-uni-bochum.de/iib/lehrstuhl/"
                "mitarbeiter/sven_zentgraf.html.en"
            ),
        )
    )
    graph.add((organization, SCHEMA.name, Literal("Ruhr University Bochum")))
    graph.add((creator, SCHEMA.name, Literal("Sven Zentgraf")))


def add_scheme_metadata(
    graph: Graph,
    scheme: URIRef,
    title_de: str,
    title_en: str,
    description_de: str,
    description_en: str,
    source_dataset: URIRef,
    suffix: str,
) -> None:
    graph.add((scheme, RDF.type, OWL.Ontology))
    graph.add((scheme, RDF.type, SKOS.ConceptScheme))
    graph.add((scheme, DCTERMS.title, Literal(title_de, lang="de")))
    graph.add((scheme, DCTERMS.title, Literal(title_en, lang="en")))
    graph.add((scheme, DCTERMS.description, Literal(description_de, lang="de")))
    graph.add((scheme, DCTERMS.description, Literal(description_en, lang="en")))
    graph.add((scheme, DCTERMS.created, Literal(RELEASE_DATE, datatype=XSD.date)))
    graph.add((scheme, DCTERMS.modified, Literal(RELEASE_DATE, datatype=XSD.date)))
    graph.add(
        (
            scheme,
            DCTERMS.license,
            URIRef("https://creativecommons.org/licenses/by/4.0/"),
        )
    )
    graph.add(
        (
            scheme,
            DCTERMS.publisher,
            URIRef("https://www.construct-x.org/id/organization/ecbe8336-94ab-5c11-8220-94f260963eb2/revision/1"),
        )
    )
    graph.add((scheme, DCTERMS.source, ISO_SOURCE))
    graph.add((scheme, DCTERMS.source, source_dataset))
    graph.add((scheme, SCHEMA.version, Literal(DATASET_VERSION)))
    graph.add((scheme, OWL.versionIRI, URIRef(f"{scheme}/{DATASET_VERSION}")))
    graph.add((scheme, OWL.versionInfo, Literal(DATASET_VERSION)))
    add_creator(graph, scheme, suffix)


def add_identifier(
    graph: Graph,
    subject: URIRef,
    node_key: str,
    identifier_value: str,
    datatype: URIRef,
) -> None:
    identifier = BNode(node_key)
    graph.add((subject, ADMS.identifier, identifier))
    graph.add((identifier, RDF.type, ADMS.Identifier))
    graph.add(
        (identifier, SKOS.notation, Literal(identifier_value, datatype=datatype))
    )
    graph.add(
        (
            identifier,
            ADMS.schemaAgency,
            Literal("International Organization for Standardization (ISO)"),
        )
    )


def build_country_graph(countries: list[dict[str, object]]) -> Graph:
    graph = Graph()
    bind_prefixes(graph)
    add_scheme_metadata(
        graph,
        COUNTRY_SCHEME,
        "L\u00e4nder nach ISO 3166-1",
        "Countries according to ISO 3166-1",
        "Aktuelle L\u00e4nder und Gebiete mit ISO-3166-1-Kennungen.",
        "Current countries and territories with ISO 3166-1 identifiers.",
        EU_COUNTRY_DATASET,
        "countries",
    )

    for item in countries:
        alpha_3 = str(item["alpha_3"])
        subject = COUNTRIES[alpha_3]
        graph.add((subject, RDF.type, ADDR.Country))
        graph.add((subject, RDF.type, SKOS.Concept))
        graph.add((subject, SKOS.inScheme, COUNTRY_SCHEME))
        graph.add((subject, SKOS.topConceptOf, COUNTRY_SCHEME))
        graph.add((COUNTRY_SCHEME, SKOS.hasTopConcept, subject))
        graph.add((subject, DCTERMS.source, URIRef(str(item["source"]))))
        for language, label in sorted(item["labels"].items()):
            graph.add((subject, SKOS.prefLabel, Literal(label, lang=language)))
        add_identifier(
            graph,
            subject,
            f"{alpha_3}-alpha-2",
            str(item["alpha_2"]),
            NETWORK_ALPHA_2,
        )
        add_identifier(
            graph,
            subject,
            f"{alpha_3}-alpha-3",
            alpha_3,
            NETWORK_ALPHA_3,
        )
        add_identifier(
            graph,
            subject,
            f"{alpha_3}-numeric",
            str(item["numeric"]),
            NETWORK_NUMERIC,
        )
    return graph


def build_area_graph(areas: list[dict[str, object]]) -> Graph:
    graph = Graph()
    bind_prefixes(graph)
    add_scheme_metadata(
        graph,
        AREA_SCHEME,
        "Deutsche L\u00e4nder nach ISO 3166-2",
        "German states according to ISO 3166-2",
        "Die 16 L\u00e4nder der Bundesrepublik Deutschland mit ISO-3166-2-Kennung.",
        "The 16 states of the Federal Republic of Germany with ISO 3166-2 codes.",
        EU_ATU_DATASET,
        "de-areas",
    )

    for item in areas:
        code = str(item["code"])
        subject = AREAS[code]
        graph.add((subject, RDF.type, ADDR.AdministrativeArea))
        graph.add((subject, RDF.type, SKOS.Concept))
        graph.add((subject, SKOS.inScheme, AREA_SCHEME))
        graph.add((subject, SKOS.topConceptOf, AREA_SCHEME))
        graph.add((AREA_SCHEME, SKOS.hasTopConcept, subject))
        graph.add((subject, ADDR.broaderAdministrativeTerritory, COUNTRIES.DEU))
        graph.add((subject, DCTERMS.source, URIRef(str(item["source"]))))
        for language, label in sorted(item["labels"].items()):
            graph.add((subject, SKOS.prefLabel, Literal(label, lang=language)))
        add_identifier(
            graph,
            subject,
            f"{code}-iso-3166-2",
            code,
            NETWORK_ISO_3166_2,
        )
    return graph


def write_graph(graph: Graph, destination: Path, header: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    serialized = graph.serialize(format="longturtle")
    destination.write_text(f"# {header}\n\n{serialized}", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root",
    )
    args = parser.parse_args()

    countries = load_countries()
    areas = load_german_areas()
    write_graph(
        build_country_graph(countries),
        args.root
        / "datasets/reference/administrative-territories/iso-3166-1-countries/data/countries.ttl",
        "Generated from ISO identifiers published in the EU country authority table.",
    )
    write_graph(
        build_area_graph(areas),
        args.root
        / "datasets/reference/administrative-territories/iso-3166-2-de/data/administrative-areas.ttl",
        "Generated from ISO identifiers published in the EU ATU authority table.",
    )
    print(f"Imported {len(countries)} countries and {len(areas)} German states.")


if __name__ == "__main__":
    main()


