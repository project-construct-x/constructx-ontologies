from pathlib import Path

import pytest
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/address"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-addr.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-addr-core.shacl.ttl"
VALID_FILE = MODULE_DIR / "tests/valid/complete-address.ttl"
INVALID_DIR = MODULE_DIR / "tests/invalid"

CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
CONX_ADDR_SH = Namespace("https://www.construct-x.org/shapes/address/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")

OWL_CARDINALITIES = {
    CONX_ADDR.Address: {
        (CONX_ADDR.hasCountry, OWL.maxCardinality, 1),
        (CONX_ADDR.houseNumber, OWL.maxCardinality, 1),
        (CONX_ADDR.postOfficeBoxNumber, OWL.maxCardinality, 1),
        (CONX_ADDR.postalCode, OWL.maxCardinality, 1),
    },
    CONX_ADDR.AddressAssignment: {
        (CONX_ADDR.assignedAddress, OWL.cardinality, 1),
        (CONX_ADDR.addressRole, OWL.minCardinality, 1),
        (CONX_ADDR.careOf, OWL.maxCardinality, 1),
    },
    CONX_ADDR.AdministrativeArea: {
        (
            CONX_ADDR.broaderAdministrativeTerritory,
            OWL.maxCardinality,
            1,
        ),
    },
}

SHACL_CARDINALITIES = {
    CONX_ADDR_SH.AssignedAddressPropertyShape: {
        (SH.minCount, 1),
        (SH.maxCount, 1),
    },
    CONX_ADDR_SH.AddressRolePropertyShape: {(SH.minCount, 1)},
    CONX_ADDR_SH.HasCountryPropertyShape: {(SH.maxCount, 1)},
    CONX_ADDR_SH.HouseNumberPropertyShape: {(SH.maxCount, 1)},
    CONX_ADDR_SH.PostOfficeBoxNumberPropertyShape: {(SH.maxCount, 1)},
    CONX_ADDR_SH.PostalCodePropertyShape: {(SH.maxCount, 1)},
    CONX_ADDR_SH.CareOfPropertyShape: {(SH.maxCount, 1)},
    CONX_ADDR_SH.BroaderAdministrativeTerritoryPropertyShape: {
        (SH.maxCount, 1)
    },
}


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_graph(path),
        shacl_graph=load_graph(SHAPES_FILE),
        ont_graph=load_graph(ONTOLOGY_FILE),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def test_owl_restrictions_express_every_general_cardinality() -> None:
    graph = load_graph(ONTOLOGY_FILE)

    for class_iri, expected in OWL_CARDINALITIES.items():
        actual = set()
        for restriction in graph.objects(class_iri, RDFS.subClassOf):
            if (restriction, RDF.type, OWL.Restriction) not in graph:
                continue
            property_iri = graph.value(restriction, OWL.onProperty)
            for predicate in (OWL.cardinality, OWL.minCardinality, OWL.maxCardinality):
                count = graph.value(restriction, predicate)
                if count is not None:
                    actual.add((property_iri, predicate, int(count)))
        assert actual == expected


def test_shacl_shapes_mirror_all_owl_cardinalities() -> None:
    graph = load_graph(SHAPES_FILE)

    for shape, constraints in SHACL_CARDINALITIES.items():
        assert (shape, RDF.type, SH.PropertyShape) in graph
        for predicate, count in constraints:
            assert (shape, predicate, Literal(count)) in graph


def test_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(SHAPES_FILE),
        meta_shacl=True,
    )

    assert conforms, report


def test_complete_address_conforms_to_core_shapes() -> None:
    conforms, _, report = validate_fixture(VALID_FILE)

    assert conforms, report


@pytest.mark.parametrize(
    ("fixture_name", "expected_paths"),
    [
        (
            "assignment-missing-required-values.ttl",
            {CONX_ADDR.assignedAddress, CONX_ADDR.addressRole},
        ),
        (
            "invalid-core-values.ttl",
            {
                CONX_ADDR.assignedAddress,
                CONX_ADDR.addressRole,
                CONX_ADDR.careOf,
                CONX_ADDR.hasCountry,
                CONX_ADDR.hasAdministrativeArea,
                CONX_ADDR.hasGeographicPosition,
                CONX_ADDR.streetName,
                CONX_ADDR.houseNumber,
                CONX_ADDR.postalCode,
                CONX_ADDR.broaderAdministrativeTerritory,
            },
        ),
    ],
)
def test_invalid_address_fixtures_report_expected_paths(
    fixture_name: str, expected_paths: set[URIRef]
) -> None:
    conforms, report_graph, report = validate_fixture(INVALID_DIR / fixture_name)
    result_paths = set(report_graph.objects(None, SH.resultPath))

    assert not conforms, report
    assert expected_paths.issubset(result_paths)
