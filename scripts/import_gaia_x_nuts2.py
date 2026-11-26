"""Generate the Construct-X NUTS 2 vocabulary from a pinned Gaia-X release."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.request import Request, urlopen

import yaml
from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import DCTERMS, OWL, SKOS, XSD


GAIA_X_RELEASE = "v2.3.0"
GAIA_X_COMMIT = "57131b2cec747de8a08a4115bea198369778aef6"
DATASET_VERSION = "0.2.0"
RELEASE_DATE = "2026-08-20"
SOURCE_URL = (
    "https://gitlab.com/gaia-x/technical-committee/"
    "service-characteristics-working-group/service-characteristics/"
    f"-/raw/{GAIA_X_RELEASE}/linkml/region-codes.yaml"
)
SOURCE_RELEASE = URIRef(
    "https://gitlab.com/gaia-x/technical-committee/"
    "service-characteristics-working-group/service-characteristics/"
    f"-/tree/{GAIA_X_RELEASE}"
)
GAIA_X_ENUM = URIRef("https://w3id.org/gaia-x/development#NUTS2Region")

ADMS = Namespace("http://www.w3.org/ns/adms#")
ADDR = Namespace("https://www.construct-x.org/ontology/address#")
COUNTRIES = Namespace("https://www.construct-x.org/vocab/country#")
ID_SCHEME = Namespace("https://www.construct-x.org/vocab/identifier-scheme#")
NUTS = Namespace("https://www.construct-x.org/vocab/administrative-area/nuts-2#")
SCHEMA = Namespace("https://schema.org/")

SCHEME = URIRef("https://www.construct-x.org/vocab/administrative-area/nuts-2")
COUNTRY_FILE = Path(
    "datasets/reference/administrative-territories/"
    "iso-3166-1-countries/data/countries.ttl"
)
DESTINATION = Path(
    "datasets/reference/administrative-territories/nuts-2/data/nuts-2-regions.ttl"
)
EXPECTED_PREFIXES = {
    "AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL",
    "ES", "FI", "FR", "HR", "HU", "IE", "IT", "LT", "LU",
    "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK",
}


def load_source(path: Path | None) -> dict:
    if path is not None:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    request = Request(SOURCE_URL, headers={"User-Agent": "construct-x-nuts2-import/0.1"})
    with urlopen(request, timeout=120) as response:
        return yaml.safe_load(response.read().decode("utf-8"))


def load_regions(source: dict) -> list[tuple[str, str]]:
    values = source["enums"]["NUTS2Region"]["permissible_values"]
    if len(values) != 271:
        raise ValueError(f"Expected 271 Gaia-X NUTS 2 values, got {len(values)}")
    if {code[:2] for code in values} != EXPECTED_PREFIXES:
        raise ValueError("Unexpected country coverage in Gaia-X NUTS 2 enumeration")

    regions: list[tuple[str, str]] = []
    for code, metadata in values.items():
        if not re.fullmatch(r"[A-Z]{2}[A-Z0-9]{2}", code):
            raise ValueError(f"Unexpected NUTS 2 code: {code}")
        description = metadata.get("description", "")
        marker = "NUTS2 Code for "
        if not description.startswith(marker):
            raise ValueError(f"Unexpected description for {code}: {description!r}")
        regions.append((code, description.removeprefix(marker).strip()))
    return regions


def country_by_alpha2(root: Path) -> dict[str, URIRef]:
    graph = Graph().parse(root / COUNTRY_FILE, format="turtle")
    datatype = ID_SCHEME["iso-3166-1-alpha-2"]
    countries: dict[str, URIRef] = {}
    for country in graph.subjects(RDF.type, ADDR.Country):
        for identifier in graph.objects(country, ADMS.identifier):
            for notation in graph.objects(identifier, SKOS.notation):
                if notation.datatype == datatype:
                    countries[str(notation)] = URIRef(country)
    if len(countries) != 249:
        raise ValueError(f"Expected 249 ISO countries, got {len(countries)}")
    return countries


def add_creator(graph: Graph) -> None:
    creator = BNode("creator-nuts-2")
    organization = BNode("organization-nuts-2")
    graph.add((SCHEME, DCTERMS.creator, creator))
    graph.add((creator, RDF.type, SCHEMA.Person))
    graph.add((creator, SCHEMA.email, URIRef("mailto:sven.zentgraf@rub.de")))
    graph.add(
        (creator, SCHEMA.identifier, URIRef("https://orcid.org/0000-0001-6058-7614"))
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


def build_graph(regions: list[tuple[str, str]], countries: dict[str, URIRef]) -> Graph:
    graph = Graph()
    for prefix, namespace in (
        ("adms", ADMS), ("conx-addr", ADDR), ("countries", COUNTRIES),
        ("dcterms", DCTERMS), ("id-scheme", ID_SCHEME), ("nuts", NUTS),
        ("owl", OWL), ("rdf", RDF), ("rdfs", RDFS), ("schema", SCHEMA),
        ("skos", SKOS), ("xsd", XSD),
    ):
        graph.bind(prefix, namespace, override=True, replace=True)

    graph.add((SCHEME, RDF.type, OWL.Ontology))
    graph.add((SCHEME, RDF.type, SKOS.ConceptScheme))
    graph.add((SCHEME, DCTERMS.created, Literal(RELEASE_DATE, datatype=XSD.date)))
    graph.add((SCHEME, DCTERMS.modified, Literal("2026-11-26", datatype=XSD.date)))
    graph.add((SCHEME, DCTERMS.title, Literal("Construct-X NUTS-2-Regionen", lang="de")))
    graph.add((SCHEME, DCTERMS.title, Literal("Construct-X NUTS 2 regions", lang="en")))
    graph.add(
        (
            SCHEME,
            DCTERMS.description,
            Literal(
                "Versioniertes Referenzvokabular der von Gaia-X v2.3.0 verwendeten "
                "NUTS-2-Codes.",
                lang="de",
            ),
        )
    )
    graph.add(
        (
            SCHEME,
            DCTERMS.description,
            Literal(
                "Versioned reference vocabulary of the NUTS 2 codes used by Gaia-X "
                "v2.3.0.",
                lang="en",
            ),
        )
    )
    graph.add((SCHEME, DCTERMS.license, URIRef("https://www.eclipse.org/legal/epl-2.0/")))
    graph.add((SCHEME, DCTERMS.publisher, URIRef(
        "https://www.construct-x.org/id/organization/"
        "ecbe8336-94ab-5c11-8220-94f260963eb2/revision/1"
    )))
    graph.add((SCHEME, DCTERMS.source, GAIA_X_ENUM))
    graph.add((SCHEME, DCTERMS.source, SOURCE_RELEASE))
    graph.add((SCHEME, DCTERMS.provenance, Literal(f"Gaia-X {GAIA_X_RELEASE}, commit {GAIA_X_COMMIT}")))
    graph.add((SCHEME, SCHEMA.version, Literal(DATASET_VERSION)))
    graph.add((SCHEME, OWL.versionIRI, URIRef(f"{SCHEME}/{DATASET_VERSION}")))
    graph.add((SCHEME, OWL.versionInfo, Literal(DATASET_VERSION)))
    add_creator(graph)

    for code, label in regions:
        region = NUTS[code]
        alpha2 = "GR" if code.startswith("EL") else code[:2]
        country = countries.get(alpha2)
        if country is None:
            raise ValueError(f"No ISO country resource for NUTS 2 code {code}")
        identifier = BNode(f"{code}-nuts-2")

        graph.add((region, RDF.type, ADDR.AdministrativeArea))
        graph.add((region, RDF.type, SKOS.Concept))
        graph.add((region, DCTERMS.source, GAIA_X_ENUM))
        graph.add((region, SKOS.inScheme, SCHEME))
        graph.add((region, SKOS.prefLabel, Literal(label)))
        graph.add((region, SKOS.topConceptOf, SCHEME))
        graph.add((region, ADMS.identifier, identifier))
        graph.add((region, ADDR.hasBroaderAdministrativeTerritory, country))
        graph.add((identifier, RDF.type, ADMS.Identifier))
        graph.add((identifier, SKOS.notation, Literal(code, datatype=ID_SCHEME["nuts-2"])))
        graph.add((identifier, ADMS.schemaAgency, Literal("Eurostat")))
        graph.add((SCHEME, SKOS.hasTopConcept, region))
    return graph


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Local Gaia-X region-codes.yaml")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1],
        help="Repository root",
    )
    args = parser.parse_args()
    regions = load_regions(load_source(args.source))
    graph = build_graph(regions, country_by_alpha2(args.root))
    destination = args.root / DESTINATION
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "# Generated from the Gaia-X v2.3.0 NUTS2Region enumeration.\n\n"
        + graph.serialize(format="longturtle"),
        encoding="utf-8",
    )
    print(f"Imported {len(regions)} Gaia-X-compatible NUTS 2 regions.")


if __name__ == "__main__":
    main()
