from pathlib import Path

import pytest
import yaml
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/vso"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-vso.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-vso-core.shacl.ttl"
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"
EXAMPLES_DIR = MODULE_DIR / "examples"

CONX_VSO = Namespace("https://www.construct-x.org/ontology/vso#")
CONX_VSO_SH = Namespace("https://www.construct-x.org/shapes/vso/core#")
OPM = Namespace("https://w3id.org/opm#")
SCHEMA = Namespace("https://schema.org/")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/vso/core")

EXPECTED_OWL_CARDINALITIES = {
    CONX_VSO.AssignedProperty: {
        (CONX_VSO.hasPropertyReference, OWL.cardinality, 1),
        (CONX_VSO.hasPropertyState, OWL.cardinality, 1),
    },
    CONX_VSO.PropertyState: {
        (SCHEMA.value, OWL.cardinality, 1),
        (CONX_VSO.hasUsedUnit, OWL.maxCardinality, 1),
    },
}

EXPECTED_ERROR_IDS = {
    "VSO-LINK-001",
    "VSO-ASSIGN-001",
    "VSO-ASSIGN-010",
    "VSO-ASSIGN-020",
    "VSO-STATE-010",
    "VSO-STATE-020",
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


def test_vso_owl_contract_matches_approved_cardinalities() -> None:
    graph = load_graph(ONTOLOGY_FILE)

    for class_iri, expected in EXPECTED_OWL_CARDINALITIES.items():
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


def test_vso_keeps_the_approved_opm_alignment() -> None:
    graph = load_graph(ONTOLOGY_FILE)

    assert (CONX_VSO.AssignedProperty, RDFS.subClassOf, OPM.Property) in graph
    assert (CONX_VSO.PropertyState, RDFS.subClassOf, OPM.PropertyState) in graph
    assert (CONX_VSO.hasPropertyState, RDFS.subPropertyOf, OPM.hasPropertyState) in graph
    assert not list(graph.objects(None, OWL.imports))


def test_vso_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(SHAPES_FILE),
        meta_shacl=True,
    )

    assert conforms, report


def test_vso_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/vso/core/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [Literal("0.1.0")]


def test_assignment_owner_is_checked_through_inverse_has_property() -> None:
    graph = load_graph(SHAPES_FILE)
    path = graph.value(CONX_VSO_SH.AssignedPropertyOwnerPropertyShape, SH.path)

    assert path is not None
    assert (path, SH.inversePath, CONX_VSO.hasProperty) in graph
    assert (
        CONX_VSO_SH.AssignedPropertyOwnerPropertyShape,
        SH.minCount,
        Literal(1),
    ) in graph
    assert (
        CONX_VSO_SH.AssignedPropertyOwnerPropertyShape,
        SH.maxCount,
        Literal(1),
    ) in graph


def test_every_named_vso_property_shape_has_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_VSO_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


def test_vso_module_metadata_registers_the_core_shape_set() -> None:
    metadata = yaml.safe_load((MODULE_DIR / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-vso-core.shacl.ttl"
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/vso/core",
        "version_iri": "https://www.construct-x.org/shapes/vso/core/0.1.0",
        "namespace": "https://www.construct-x.org/shapes/vso/core#",
        "version": "0.1.0",
        "artifact": "shapes/conx-vso-core.shacl.ttl",
    }


@pytest.mark.parametrize(
    "fixture_name",
    ["measured-property.ttl", "text-property.ttl", "boolean-property.ttl"],
)
def test_valid_vso_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)

    assert conforms, report


@pytest.mark.parametrize(
    "example_name",
    ["measured-property.ttl", "text-property.ttl"],
)
def test_public_vso_examples_conform(example_name: str) -> None:
    conforms, _, report = validate_fixture(EXAMPLES_DIR / example_name)

    assert conforms, report


INVALID_FIXTURES = (
    ("multiple-owners.ttl", {"VSO-ASSIGN-001"}),
    (
        "invalid-assignment-cardinalities.ttl",
        {"VSO-ASSIGN-010", "VSO-ASSIGN-020"},
    ),
    ("invalid-state-values.ttl", {"VSO-STATE-010", "VSO-STATE-020"}),
    (
        "missing-required-links.ttl",
        {"VSO-ASSIGN-001", "VSO-ASSIGN-020", "VSO-STATE-010"},
    ),
    (
        "invalid-property-link.ttl",
        {"VSO-LINK-001", "VSO-ASSIGN-010", "VSO-ASSIGN-020"},
    ),
)


@pytest.mark.parametrize(("fixture_name", "expected_ids"), INVALID_FIXTURES)
def test_invalid_vso_fixtures_report_expected_contracts(
    fixture_name: str,
    expected_ids: set[str],
) -> None:
    conforms, _, report = validate_fixture(INVALID_DIR / fixture_name)

    assert not conforms, report
    for requirement_id in expected_ids:
        assert requirement_id in report


def test_invalid_fixture_catalog_covers_every_vso_error_code() -> None:
    covered_ids = set().union(*(expected_ids for _, expected_ids in INVALID_FIXTURES))

    assert covered_ids == EXPECTED_ERROR_IDS
