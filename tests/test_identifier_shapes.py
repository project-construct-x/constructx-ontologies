from pathlib import Path

import pytest
import yaml
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/identifier"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-id.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-id-core.shacl.ttl"
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"

CONX_ID_SH = Namespace("https://www.construct-x.org/shapes/identifier/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/identifier")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/identifier/core")


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


def test_identifier_ontology_and_shape_metadata_are_versioned() -> None:
    ontology_graph = load_graph(ONTOLOGY_FILE)
    shapes_graph = load_graph(SHAPES_FILE)

    assert (ONTOLOGY_IRI, RDF.type, OWL.Ontology) in ontology_graph
    assert list(ontology_graph.objects(ONTOLOGY_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/ontology/identifier/0.1.0")
    ]
    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in shapes_graph
    assert list(shapes_graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/identifier/core/0.1.0")
    ]
    assert list(shapes_graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [
        Literal("0.1.0")
    ]


def test_identifier_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(SHAPES_FILE),
        meta_shacl=True,
    )

    assert conforms, report


def test_identifier_module_metadata_registers_the_core_shape_set() -> None:
    metadata = yaml.safe_load((MODULE_DIR / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "identifier"
    assert metadata["type"] == "core"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-id-core.shacl.ttl"
    assert metadata["shape_sets"]["core"]["graph_iri"] == str(SHAPE_GRAPH_IRI)


def test_identifier_contract_defines_the_three_shared_error_ids() -> None:
    graph = load_graph(SHAPES_FILE)
    messages = {str(message) for message in graph.objects(None, SH.message)}

    for error_id in ("ID-001", "ID-002", "ID-003"):
        assert any(f"[{error_id}]" in message for message in messages)


@pytest.mark.parametrize(
    "fixture_name",
    ["minimal-identifier.ttl", "identifier-with-agency.ttl"],
)
def test_valid_identifier_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)
    assert conforms, report


@pytest.mark.parametrize(
    "fixture_name",
    ["missing-notation.ttl", "multiple-notations.ttl", "invalid-schema-agency.ttl"],
)
def test_invalid_identifier_fixtures_fail(fixture_name: str) -> None:
    conforms, _, _ = validate_fixture(INVALID_DIR / fixture_name)
    assert not conforms


def test_shared_identifier_shape_has_no_local_identifier_class() -> None:
    ontology_graph = load_graph(ONTOLOGY_FILE)
    local_classes = {
        subject
        for subject in ontology_graph.subjects(RDF.type, OWL.Class)
        if str(subject).startswith("https://www.construct-x.org/ontology/identifier#")
    }

    assert local_classes == set()
    assert (CONX_ID_SH.ADMSIdentifierShape, RDF.type, SH.NodeShape) in load_graph(
        SHAPES_FILE
    )


def test_consuming_core_shapes_do_not_redeclare_the_shared_contract() -> None:
    consuming_shape_files = (
        ROOT / "modules/core/person/shapes/conx-person-core.shacl.ttl",
        ROOT / "modules/core/organization/shapes/conx-org-core.shacl.ttl",
        ROOT / "modules/core/document/shapes/conx-doc-core.shacl.ttl",
    )

    for shape_file in consuming_shape_files:
        graph = load_graph(shape_file)
        assert (CONX_ID_SH.ADMSIdentifierShape, None, None) not in graph
        assert (None, SH.node, CONX_ID_SH.ADMSIdentifierShape) in graph
