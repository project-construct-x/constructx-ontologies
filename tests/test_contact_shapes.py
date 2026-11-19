from pathlib import Path

import pytest
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/contact"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-contact.ttl"
ADDRESS_ONTOLOGY_FILE = ROOT / "modules/core/address/ontology/conx-addr.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-contact-core.shacl.ttl"
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"
REFERENCE_FILES = (
    ROOT / "datasets/reference/vocabularies/contact-channel/contact-channel.ttl",
    ROOT / "datasets/reference/vocabularies/contact-usage/contact-usage.ttl",
    ROOT / "datasets/reference/vocabularies/contact-purpose/contact-purpose.ttl",
    ROOT / "datasets/reference/vocabularies/contact-platform/contact-platform.ttl",
    ROOT / "datasets/reference/vocabularies/address-roles/address-roles.ttl",
)

CONX_CONTACT = Namespace("https://www.construct-x.org/ontology/contact#")
CONX_CONTACT_SH = Namespace("https://www.construct-x.org/shapes/contact/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/contact/core")


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def load_data_with_references(path: Path) -> Graph:
    graph = load_graph(path)
    for reference_file in REFERENCE_FILES:
        graph.parse(reference_file, format="turtle")
    return graph


def load_ontology_graph() -> Graph:
    graph = load_graph(ONTOLOGY_FILE)
    graph.parse(ADDRESS_ONTOLOGY_FILE, format="turtle")
    return graph


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_data_with_references(path),
        shacl_graph=load_graph(SHAPES_FILE),
        ont_graph=load_ontology_graph(),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def test_contact_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(SHAPES_FILE),
        meta_shacl=True,
    )

    assert conforms, report


def test_contact_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/contact/core/0.2.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [
        Literal("0.2.0")
    ]


def test_contact_shape_targets_contact_terms() -> None:
    graph = load_graph(SHAPES_FILE)

    point_targets = set(graph.objects(CONX_CONTACT_SH.ContactPointShape, SH.targetSubjectsOf))
    method_targets = set(graph.objects(CONX_CONTACT_SH.ContactMethodShape, SH.targetSubjectsOf))

    assert CONX_CONTACT.hasContactMethod in point_targets
    assert CONX_CONTACT.contactUsage in point_targets
    assert CONX_CONTACT.contactPlatform in method_targets
    assert CONX_CONTACT.usesLocationAssignment in method_targets


def test_every_named_contact_property_shape_has_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_CONTACT_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


@pytest.mark.parametrize(
    "fixture_name",
    [
        "minimal-email-contact.ttl",
        "business-delivery-contact.ttl",
        "website-and-social-contact.ttl",
        "messenger-contact.ttl",
    ],
)
def test_valid_contact_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)

    assert conforms, report


@pytest.mark.parametrize(
    ("fixture_name", "expected_ids"),
    [
        ("contact-point-missing-method.ttl", {"CON-CP-010"}),
        ("contact-method-invalid-channel.ttl", {"CON-CM-010", "CON-CM-020"}),
        (
            "contact-method-invalid-payload.ttl",
            {"CON-CM-020", "CON-CM-030", "CON-CM-031"},
        ),
        ("postal-contact-invalid-address-reference.ttl", {"CON-CM-020", "CON-CM-032"}),
        ("invalid-usage-and-purpose.ttl", {"CON-CP-020", "CON-CP-021"}),
        (
            "invalid-text-values.ttl",
            {
                "CON-CP-030",
                "CON-CP-031",
                "CON-CP-032",
                "CON-CP-033",
                "CON-CP-034",
                "CON-CM-033",
            },
        ),
    ],
)
def test_invalid_contact_fixtures_report_expected_contracts(
    fixture_name: str,
    expected_ids: set[str],
) -> None:
    conforms, _, report = validate_fixture(INVALID_DIR / fixture_name)

    assert not conforms, report
    for requirement_id in expected_ids:
        assert requirement_id in report

def test_postal_contact_requires_an_address_even_when_geolocation_exists() -> None:
    addr = Namespace("https://www.construct-x.org/ontology/address#")
    graph = load_data_with_references(VALID_DIR / "business-delivery-contact.ttl")
    assignment, = graph.subjects(addr.assignedAddress, None)
    graph.remove((assignment, addr.assignedAddress, None))
    position = URIRef("https://example.org/gate")
    graph.add((assignment, addr.hasGeoReference, position))
    conforms, _, report = validate(graph, shacl_graph=load_graph(SHAPES_FILE), ont_graph=load_ontology_graph())
    assert not conforms
    assert "CON-CM-032" in report
