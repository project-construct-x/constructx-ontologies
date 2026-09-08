from pathlib import Path

import pytest
import yaml
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/document"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-doc.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-doc-core.shacl.ttl"
IDENTIFIER_SHAPES_FILE = (
    ROOT / "modules/core/identifier/shapes/conx-id-core.shacl.ttl"
)
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"
REFERENCE_FILES = (
    ROOT / "datasets/reference/vocabularies/document-type/document-type.ttl",
    ROOT / "datasets/reference/vocabularies/document-status/document-status.ttl",
)

CONX_DOC = Namespace("https://www.construct-x.org/ontology/document#")
CONX_DOC_SH = Namespace("https://www.construct-x.org/shapes/document/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/document/core")

EXPECTED_ERROR_IDS = {
    "DOC-CTX-001",
    "DOC-CAR-001",
    "DOC-DOC-001",
    "DOC-DOC-002",
    "DOC-DOC-010",
    "DOC-DOC-011",
    "DOC-DOC-012",
    "DOC-DOC-020",
    "DOC-DOC-021",
    "DOC-DOC-030",
    "DOC-DOC-040",
    "DOC-DOC-041",
    "DOC-DOC-042",
    "DOC-DOC-043",
    "DOC-DOC-044",
    "DOC-DOC-045",
    "DOC-DOC-050",
    "DOC-DOC-060",
    "DOC-REF-001",
    "DOC-REF-002",
    "DOC-REF-010",
    "DOC-REF-011",
    "DOC-REF-012",
    "DOC-REF-013",
    "DOC-REF-020",
    "DOC-REF-030",
    "DOC-DIST-001",
    "DOC-DIST-002",
    "DOC-DIST-010",
    "DOC-DIST-011",
    "DOC-DIST-020",
    "DOC-DIST-030",
    "ID-001",
    "ID-002",
    "ID-003",
}


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def load_combined_graph(paths: tuple[Path, ...]) -> Graph:
    graph = Graph()
    for path in paths:
        graph.parse(path, format="turtle")
    return graph


def load_data_with_references(path: Path) -> Graph:
    graph = load_graph(path)
    for reference_file in REFERENCE_FILES:
        graph.parse(reference_file, format="turtle")
    return graph


def load_shapes_graph() -> Graph:
    return load_combined_graph((SHAPES_FILE, IDENTIFIER_SHAPES_FILE))


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_data_with_references(path),
        shacl_graph=load_shapes_graph(),
        ont_graph=load_graph(ONTOLOGY_FILE),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def test_document_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_shapes_graph(),
        meta_shacl=True,
    )

    assert conforms, report


def test_document_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/document/core/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [
        Literal("0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.imports)) == [
        URIRef("https://www.construct-x.org/shapes/identifier/core/0.1.0")
    ]


def test_shared_document_properties_use_the_carrier_shape() -> None:
    graph = load_graph(SHAPES_FILE)
    document_targets = set(graph.objects(CONX_DOC_SH.DocumentShape, SH.targetSubjectsOf))
    carrier_targets = set(
        graph.objects(CONX_DOC_SH.DocumentCarrierShape, SH.targetSubjectsOf)
    )

    assert CONX_DOC.documentStatus in document_targets
    assert CONX_DOC.documentType not in document_targets
    assert CONX_DOC.hasDistribution not in document_targets
    assert carrier_targets == {CONX_DOC.documentType, CONX_DOC.hasDistribution}


def test_every_named_document_property_shape_has_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_DOC_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


def test_shape_graph_contains_every_approved_error_code() -> None:
    graph = load_shapes_graph()
    messages = "\n".join(str(message) for message in graph.objects(None, SH.message))

    assert all(error_id in messages for error_id in EXPECTED_ERROR_IDS)


def test_document_module_metadata_registers_the_core_shape_set() -> None:
    metadata = yaml.safe_load((MODULE_DIR / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-doc-core.shacl.ttl"
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/document/core",
        "version_iri": "https://www.construct-x.org/shapes/document/core/0.1.0",
        "namespace": "https://www.construct-x.org/shapes/document/core#",
        "version": "0.1.0",
        "artifact": "shapes/conx-doc-core.shacl.ttl",
    }


@pytest.mark.parametrize(
    "fixture_name",
    [
        "minimal-document.ttl",
        "complete-document.ttl",
        "multiple-distributions.ttl",
        "document-references.ttl",
        "document-with-participation.ttl",
    ],
)
def test_valid_document_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)

    assert conforms, report


INVALID_FIXTURES = (
    (
        "invalid-document-typing.ttl",
        {
            "DOC-CTX-001",
            "DOC-CAR-001",
            "DOC-DOC-002",
            "DOC-REF-001",
            "DOC-REF-002",
            "DOC-REF-010",
            "DOC-REF-013",
            "DOC-DIST-002",
        },
    ),
    (
        "invalid-document-references.ttl",
        {
            "DOC-DOC-001",
            "DOC-DOC-002",
            "DOC-DOC-020",
            "DOC-REF-010",
            "DOC-REF-011",
            "DOC-REF-012",
            "DOC-REF-013",
            "DOC-REF-020",
            "DOC-DIST-002",
        },
    ),
    (
        "invalid-distributions.ttl",
        {
            "DOC-DOC-050",
            "DOC-DIST-001",
            "DOC-DIST-002",
            "DOC-DIST-010",
            "DOC-DIST-011",
            "DOC-DIST-020",
            "DOC-DIST-030",
        },
    ),
    (
        "invalid-controlled-values.ttl",
        {"DOC-DOC-020", "DOC-DOC-021", "DOC-REF-020"},
    ),
    (
        "invalid-metadata-and-identifiers.ttl",
        {
            "DOC-DOC-010",
            "DOC-DOC-011",
            "DOC-DOC-012",
            "DOC-DOC-030",
            "DOC-DOC-040",
            "DOC-DOC-041",
            "DOC-DOC-042",
            "DOC-DOC-043",
            "DOC-DOC-044",
            "DOC-DOC-045",
            "DOC-DOC-060",
            "DOC-REF-030",
            "ID-001",
            "ID-002",
            "ID-003",
        },
    ),
)


@pytest.mark.parametrize(("fixture_name", "expected_ids"), INVALID_FIXTURES)
def test_invalid_document_fixtures_report_expected_contracts(
    fixture_name: str,
    expected_ids: set[str],
) -> None:
    conforms, _, report = validate_fixture(INVALID_DIR / fixture_name)

    assert not conforms, report
    for requirement_id in expected_ids:
        assert requirement_id in report


def test_invalid_fixture_catalog_covers_every_approved_error_code() -> None:
    covered_ids = set().union(*(expected_ids for _, expected_ids in INVALID_FIXTURES))

    assert covered_ids == EXPECTED_ERROR_IDS


def test_document_and_participation_shapes_validate_together() -> None:
    data_graph = load_data_with_references(VALID_DIR / "document-with-participation.ttl")
    data_graph.parse(
        ROOT / "datasets/reference/vocabularies/participation-role/participation-role.ttl",
        format="turtle",
    )
    shapes_graph = load_combined_graph(
        (
            SHAPES_FILE,
            ROOT / "modules/core/participation/shapes/conx-part-core.shacl.ttl",
        )
    )
    ontology_graph = load_combined_graph(
        (
            ROOT / "modules/core/agent/ontology/conx-agent.ttl",
            ONTOLOGY_FILE,
            ROOT / "modules/core/participation/ontology/conx-part.ttl",
        )
    )

    conforms, _, report = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ontology_graph,
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )

    assert conforms, report
