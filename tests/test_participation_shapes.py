from pathlib import Path

import pytest
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/participation"
ONTOLOGY_FILES = (
    ROOT / "modules/core/agent/ontology/conx-agent.ttl",
    ROOT / "modules/core/person/ontology/conx-person.ttl",
    ROOT / "modules/core/organization/ontology/conx-org.ttl",
    MODULE_DIR / "ontology/conx-part.ttl",
)
SHAPES_FILE = MODULE_DIR / "shapes/conx-part-core.shacl.ttl"
ROLE_VOCABULARY_FILE = (
    ROOT
    / "datasets/reference/vocabularies/participation-role/participation-role.ttl"
)
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"

CONX_PART = Namespace("https://www.construct-x.org/ontology/participation#")
CONX_PART_SH = Namespace("https://www.construct-x.org/shapes/participation/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/participation/core")
EXPECTED_ERROR_IDS = {
    "PART-001",
    "PART-002",
    "PART-010",
    "PART-011",
    "PART-012",
    "PART-013",
    "PART-020",
    "PART-021",
    "PART-022",
    "PART-023",
    "PART-030",
    "PART-031",
    "PART-032",
    "PART-040",
    "PART-041",
    "PART-042",
    "PART-043",
    "PART-044",
    "PART-050",
}


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def load_combined_graph(paths: tuple[Path, ...]) -> Graph:
    graph = Graph()
    for path in paths:
        graph.parse(path, format="turtle")
    return graph


def load_data_with_roles(path: Path) -> Graph:
    graph = load_graph(path)
    graph.parse(ROLE_VOCABULARY_FILE, format="turtle")
    return graph


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_data_with_roles(path),
        shacl_graph=load_graph(SHAPES_FILE),
        ont_graph=load_combined_graph(ONTOLOGY_FILES),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def report_error_ids(report_graph: Graph) -> set[str]:
    return {
        error_id
        for message in report_graph.objects(None, SH.resultMessage)
        for error_id in EXPECTED_ERROR_IDS
        if f"[{error_id}]" in str(message)
    }


def test_participation_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(SHAPES_FILE),
        meta_shacl=True,
    )
    assert conforms, report


def test_participation_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/participation/core/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [
        Literal("0.1.0")
    ]


def test_participation_shape_targets_every_local_property() -> None:
    graph = load_graph(SHAPES_FILE)
    targets = set(graph.objects(CONX_PART_SH.ParticipationShape, SH.targetSubjectsOf))

    assert targets == {
        CONX_PART.participant,
        CONX_PART.role,
        CONX_PART.context,
        CONX_PART.startDate,
        CONX_PART.endDate,
    }


def test_named_participation_property_shapes_have_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_PART_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


def test_every_approved_error_id_occurs_in_the_shape_graph() -> None:
    graph = load_graph(SHAPES_FILE)
    messages = {str(message) for message in graph.objects(None, SH.message)}
    found = {
        error_id
        for error_id in EXPECTED_ERROR_IDS
        if any(f"[{error_id}]" in message for message in messages)
    }
    assert found == EXPECTED_ERROR_IDS


@pytest.mark.parametrize(
    "fixture_name",
    [
        "minimal-participation.ttl",
        "dated-participation.ttl",
        "multiple-roles-and-contexts.ttl",
        "external-role.ttl",
        "blank-node-context.ttl",
        "agent-subclass.ttl",
        "person-and-organization-participants.ttl",
    ],
)
def test_valid_participation_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)
    assert conforms, report


@pytest.mark.parametrize(
    ("fixture_name", "expected_ids"),
    [
        ("missing-required-values.ttl", {"PART-010", "PART-020", "PART-030"}),
        ("invalid-participant.ttl", {"PART-011", "PART-012", "PART-013"}),
        ("invalid-role.ttl", {"PART-021", "PART-022", "PART-023"}),
        ("invalid-context.ttl", {"PART-031", "PART-032"}),
        (
            "invalid-dates.ttl",
            {"PART-040", "PART-041", "PART-042", "PART-043", "PART-044"},
        ),
        ("duplicate-participation.ttl", {"PART-050"}),
        ("untyped-or-blank-participation.ttl", {"PART-001", "PART-002"}),
    ],
)
def test_invalid_participation_fixtures_report_expected_contracts(
    fixture_name: str, expected_ids: set[str]
) -> None:
    conforms, report_graph, report = validate_fixture(INVALID_DIR / fixture_name)

    assert not conforms, report
    assert expected_ids <= report_error_ids(report_graph), report
