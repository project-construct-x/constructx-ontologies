from pathlib import Path

import pytest
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/organization"
ONTOLOGY_FILES = (
    ROOT / "modules/core/agent/ontology/conx-agent.ttl",
    ROOT / "modules/core/person/ontology/conx-person.ttl",
    ROOT / "modules/core/address/ontology/conx-addr.ttl",
    ROOT / "modules/core/contact/ontology/conx-contact.ttl",
    MODULE_DIR / "ontology/conx-org.ttl",
)
SHAPES_FILE = MODULE_DIR / "shapes/conx-org-core.shacl.ttl"
INTEGRATION_SHAPE_FILES = (
    ROOT / "modules/core/identifier/shapes/conx-id-core.shacl.ttl",
    ROOT / "modules/core/address/shapes/conx-addr-core.shacl.ttl",
    ROOT / "modules/core/contact/shapes/conx-contact-core.shacl.ttl",
    ROOT / "modules/core/person/shapes/conx-person-core.shacl.ttl",
)
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"
REFERENCE_FILES = (
    ROOT / "datasets/reference/vocabularies/address-roles/address-roles.ttl",
    ROOT / "datasets/reference/vocabularies/contact-channel/contact-channel.ttl",
    ROOT / "datasets/reference/vocabularies/contact-usage/contact-usage.ttl",
    ROOT / "datasets/reference/vocabularies/contact-purpose/contact-purpose.ttl",
    ROOT / "datasets/reference/vocabularies/contact-platform/contact-platform.ttl",
)

CONX_ORG = Namespace("https://www.construct-x.org/ontology/organization#")
CONX_ORG_SH = Namespace("https://www.construct-x.org/shapes/organization/core#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/organization/core")

EXPECTED_ERROR_IDS = {
    "ORG-001",
    "ORG-002",
    "ORG-010",
    "ORG-011",
    "ORG-020",
    "ORG-030",
    "ORG-040",
    "ORG-041",
    "ORG-042",
    "ORG-043",
    "LE-001",
    "LE-002",
    "LE-003",
    "LE-010",
    "LE-020",
    "LE-030",
    "LE-040",
    "LE-050",
    "UNIT-001",
    "UNIT-002",
    "UNIT-003",
    "UNIT-010",
    "UNIT-011",
    "MEM-001",
    "MEM-002",
    "MEM-010",
    "MEM-011",
    "MEM-012",
    "MEM-020",
    "REP-001",
    "REP-002",
    "REP-010",
    "REP-011",
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
    graph = load_graph(SHAPES_FILE)
    for shape_file in INTEGRATION_SHAPE_FILES:
        graph.parse(shape_file, format="turtle")
    return graph


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_data_with_references(path),
        shacl_graph=load_shapes_graph(),
        ont_graph=load_combined_graph(ONTOLOGY_FILES),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def test_organization_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_shapes_graph(),
        meta_shacl=True,
    )

    assert conforms, report


def test_organization_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/organization/core/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [
        Literal("0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.imports)) == [
        URIRef("https://www.construct-x.org/shapes/identifier/core/0.1.0")
    ]


def test_organization_shapes_target_local_properties_but_not_generic_links() -> None:
    graph = load_graph(SHAPES_FILE)
    targets = set(graph.objects(CONX_ORG_SH.OrganizationShape, SH.targetSubjectsOf))

    assert CONX_ORG.name in targets
    assert CONX_ORG.subOrganizationOf in targets
    assert CONX_ORG.hasUnit in targets
    assert ADMS.identifier not in targets


def test_every_named_organization_property_shape_has_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_ORG_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


def test_shape_graph_contains_every_approved_error_code() -> None:
    graph = load_shapes_graph()
    messages = "\n".join(str(message) for message in graph.objects(None, SH.message))

    assert all(error_id in messages for error_id in EXPECTED_ERROR_IDS)


@pytest.mark.parametrize(
    "fixture_name",
    [
        "minimal-organization.ttl",
        "complete-legal-entity.ttl",
        "organizational-unit.ttl",
        "memberships.ttl",
        "legal-representation.ttl",
        "official-homepage.ttl",
    ],
)
def test_valid_organization_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)

    assert conforms, report


INVALID_FIXTURES = (
    (
        "invalid-organization-name-and-type.ttl",
        {"ORG-001", "ORG-002", "ORG-010", "ORG-011", "ORG-020"},
    ),
    (
        "invalid-legal-entity-core.ttl",
        {
            "LE-001",
            "LE-002",
            "LE-003",
            "LE-010",
            "LE-020",
            "LE-040",
            "LE-050",
        },
    ),
    (
        "invalid-registration-and-legal-form.ttl",
        {"LE-020", "LE-030"},
    ),
    (
        "invalid-identifier-and-address.ttl",
        {"ORG-030", "LE-040", "LE-050", "ID-001", "ID-002", "ID-003"},
    ),
    (
        "invalid-organizational-unit.ttl",
        {"UNIT-001", "UNIT-002", "UNIT-003", "UNIT-010", "UNIT-011"},
    ),
    (
        "invalid-hierarchy.ttl",
        {"ORG-040", "ORG-041", "ORG-042", "ORG-043"},
    ),
    (
        "invalid-membership.ttl",
        {"MEM-001", "MEM-002", "MEM-010", "MEM-011", "MEM-012", "MEM-020"},
    ),
    (
        "invalid-legal-representation.ttl",
        {"REP-001", "REP-002", "REP-010", "REP-011"},
    ),
)


@pytest.mark.parametrize(("fixture_name", "expected_ids"), INVALID_FIXTURES)
def test_invalid_organization_fixtures_report_expected_contracts(
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
