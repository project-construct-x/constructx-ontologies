from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import OWL, SKOS


ROOT = Path(__file__).resolve().parents[1]
COUNTRY_DIR = (
    ROOT
    / "datasets/reference/administrative-territories/iso-3166-1-countries"
)
AREA_DIR = ROOT / "datasets/reference/administrative-territories/iso-3166-2-de"
COUNTRY_FILE = COUNTRY_DIR / "data/countries.ttl"
AREA_FILE = AREA_DIR / "data/administrative-areas.ttl"
EXAMPLE_FILE = ROOT / "modules/core/address/examples/rub-address.ttl"

ADMS = Namespace("http://www.w3.org/ns/adms#")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
COUNTRIES = Namespace("https://www.construct-x.org/vocab/country#")
AREAS = Namespace("https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#")
ID_SCHEME = Namespace("https://www.construct-x.org/vocab/identifier-scheme#")
ROLES = Namespace("https://www.construct-x.org/vocab/address-role#")
EX = Namespace("https://example.org/id/")

COUNTRY_SCHEME = URIRef("https://www.construct-x.org/vocab/country")
AREA_SCHEME = URIRef(
    "https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de"
)
SOURCE_VERSION = "20260617-0"

COUNTRY_IDENTIFIER_TYPES = {
    ID_SCHEME["iso-3166-1-alpha-2"],
    ID_SCHEME["iso-3166-1-alpha-3"],
    ID_SCHEME["iso-3166-1-numeric"],
}
EXPECTED_GERMAN_AREAS = {
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


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def identifier_values(graph: Graph, subject: URIRef) -> dict[URIRef, str]:
    identifiers: dict[URIRef, str] = {}
    nodes = list(graph.objects(subject, ADMS.identifier))
    for node in nodes:
        assert (node, RDF.type, ADMS.Identifier) in graph
        notations = list(graph.objects(node, SKOS.notation))
        assert len(notations) == 1
        notation = notations[0]
        assert notation.datatype is not None
        assert list(graph.objects(node, ADMS.schemaAgency)) == [
            Literal("International Organization for Standardization (ISO)")
        ]
        assert notation.datatype not in identifiers
        identifiers[notation.datatype] = str(notation)
    return identifiers


def test_dataset_metadata_records_scope_source_and_dependencies() -> None:
    with (COUNTRY_DIR / "dataset.yaml").open(encoding="utf-8") as handle:
        countries = yaml.safe_load(handle)
    with (AREA_DIR / "dataset.yaml").open(encoding="utf-8") as handle:
        areas = yaml.safe_load(handle)

    assert countries["id"] == "iso-3166-1-countries"
    assert countries["version"] == "0.1.0"
    assert countries["version_iri"] == f"{COUNTRY_SCHEME}/0.1.0"
    assert countries["source"]["extraction_version"] == SOURCE_VERSION
    assert {dependency["id"] for dependency in countries["dependencies"]} == {
        "address",
        "adms",
        "identifier-scheme",
    }

    assert areas["id"] == "iso-3166-2-de"
    assert areas["version"] == "0.1.0"
    assert areas["version_iri"] == f"{AREA_SCHEME}/0.1.0"
    assert areas["source"]["extraction_version"] == SOURCE_VERSION
    assert {dependency["id"] for dependency in areas["dependencies"]} == {
        "address",
        "adms",
        "iso-3166-1-countries",
        "identifier-scheme",
    }


def test_country_dataset_contains_exactly_249_current_iso_entries() -> None:
    graph = load_graph(COUNTRY_FILE)
    countries = set(graph.subjects(RDF.type, CONX_ADDR.Country))

    assert len(countries) == 249
    assert (COUNTRY_SCHEME, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(COUNTRY_SCHEME, OWL.versionIRI)) == [
        URIRef(f"{COUNTRY_SCHEME}/0.1.0")
    ]
    assert all(str(country).startswith(str(COUNTRIES)) for country in countries)
    assert set(graph.objects(COUNTRY_SCHEME, SKOS.hasTopConcept)) == countries
    assert not {
        COUNTRIES.CPT,
        COUNTRIES.CRQ,
        COUNTRIES.FXX,
        COUNTRIES.XKX,
    }.intersection(countries)

    values_by_type = {datatype: set() for datatype in COUNTRY_IDENTIFIER_TYPES}
    for country in countries:
        assert (country, RDF.type, SKOS.Concept) in graph
        assert (country, SKOS.inScheme, COUNTRY_SCHEME) in graph
        assert (country, SKOS.topConceptOf, COUNTRY_SCHEME) in graph
        assert {label.language for label in graph.objects(country, SKOS.prefLabel)} == {
            "de",
            "en",
        }

        identifiers = identifier_values(graph, country)
        assert set(identifiers) == COUNTRY_IDENTIFIER_TYPES
        for datatype, identifier in identifiers.items():
            values_by_type[datatype].add(identifier)

    assert all(len(values) == 249 for values in values_by_type.values())
    assert all(
        len(value) == 2 and value.isupper()
        for value in values_by_type[ID_SCHEME["iso-3166-1-alpha-2"]]
    )
    assert all(
        len(value) == 3 and value.isupper()
        for value in values_by_type[ID_SCHEME["iso-3166-1-alpha-3"]]
    )
    assert all(
        len(value) == 3 and value.isdigit()
        for value in values_by_type[ID_SCHEME["iso-3166-1-numeric"]]
    )


def test_country_identifiers_cover_germany_and_guard_numeric_fallbacks() -> None:
    graph = load_graph(COUNTRY_FILE)

    assert identifier_values(graph, COUNTRIES.DEU) == {
        ID_SCHEME["iso-3166-1-alpha-2"]: "DE",
        ID_SCHEME["iso-3166-1-alpha-3"]: "DEU",
        ID_SCHEME["iso-3166-1-numeric"]: "276",
    }
    assert identifier_values(graph, COUNTRIES.NPL)[
        ID_SCHEME["iso-3166-1-numeric"]
    ] == "524"
    assert identifier_values(graph, COUNTRIES.SHN)[
        ID_SCHEME["iso-3166-1-numeric"]
    ] == "654"


def test_german_area_dataset_contains_only_the_16_states() -> None:
    graph = load_graph(AREA_FILE)
    areas = set(graph.subjects(RDF.type, CONX_ADDR.AdministrativeArea))

    assert areas == {AREAS[code] for code in EXPECTED_GERMAN_AREAS}
    assert (AREA_SCHEME, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(AREA_SCHEME, OWL.versionIRI)) == [
        URIRef(f"{AREA_SCHEME}/0.1.0")
    ]
    assert set(graph.objects(AREA_SCHEME, SKOS.hasTopConcept)) == areas

    for code in EXPECTED_GERMAN_AREAS:
        area = AREAS[code]
        assert (area, RDF.type, SKOS.Concept) in graph
        assert (area, SKOS.inScheme, AREA_SCHEME) in graph
        assert (
            area,
            CONX_ADDR.broaderAdministrativeTerritory,
            COUNTRIES.DEU,
        ) in graph
        assert any(label.language == "de" for label in graph.objects(area, SKOS.prefLabel))
        assert identifier_values(graph, area) == {
            ID_SCHEME["iso-3166-2"]: code
        }

    assert not any(
        str(label) == "Bochum"
        for subject in areas
        for label in graph.objects(subject, SKOS.prefLabel)
    )


def test_saxony_source_record_is_published_with_the_correct_iso_code() -> None:
    graph = load_graph(AREA_FILE)
    saxony_source = URIRef(
        "http://publications.europa.eu/resource/authority/atu/DEU_LD_SN"
    )

    assert (
        AREAS["DE-SN"],
        URIRef("http://purl.org/dc/terms/source"),
        saxony_source,
    ) in graph
    assert identifier_values(graph, AREAS["DE-SN"])[ID_SCHEME["iso-3166-2"]] == "DE-SN"
    assert identifier_values(graph, AREAS["DE-ST"])[ID_SCHEME["iso-3166-2"]] == "DE-ST"


def test_address_example_uses_references_but_keeps_city_as_literal() -> None:
    graph = load_graph(EXAMPLE_FILE)

    assert (EX.rub, CONX_ADDR.hasAddressAssignment, EX["rub-postal-address-assignment"]) in graph
    assert (
        EX["rub-postal-address-assignment"],
        CONX_ADDR.addressRole,
        ROLES.PostalAddressRole,
    ) in graph
    assert (EX["rub-address"], CONX_ADDR.hasCountry, COUNTRIES.DEU) in graph
    assert (
        EX["rub-address"],
        CONX_ADDR.hasAdministrativeArea,
        AREAS["DE-NW"],
    ) in graph
    assert (
        EX["rub-address"],
        CONX_ADDR.localityName,
        Literal("Bochum", lang="de"),
    ) in graph

