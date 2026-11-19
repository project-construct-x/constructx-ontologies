from pathlib import Path

import pytest
import yaml
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef

from scripts.validate import validate_repository


ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "profiles/construct-x/vso-isoprops"
PROFILE_FILE = PROFILE_DIR / "profile.yaml"
PROFILE_SHAPES_FILE = PROFILE_DIR / "shapes/conx-vso-isoprops.shacl.ttl"
CORE_SHAPES_FILE = ROOT / "modules/core/vso/shapes/conx-vso-core.shacl.ttl"
ONTOLOGY_FILE = ROOT / "modules/core/vso/ontology/conx-vso.ttl"
VALID_DIR = PROFILE_DIR / "tests/valid"
INVALID_DIR = PROFILE_DIR / "tests/invalid"
EXAMPLES_DIR = PROFILE_DIR / "examples"

PROFILE_SHAPES = Namespace("https://www.construct-x.org/shapes/vso/isoprops#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/vso/isoprops")

EXPECTED_ERROR_IDS = {
    "ISOP-REF-001",
    "ISOP-ID-001",
    "ISOP-ID-002",
    "ISOP-ID-003",
    "ISOP-VERSION-001",
    "ISOP-REVISION-001",
    "ISOP-STATUS-001",
    "ISOP-DATATYPE-001",
    "ISOP-UNIT-001",
    "ISOP-ASSIGN-UNIT-001",
    "ISOP-ASSIGN-UNIT-002",
    "ISOP-VALUE-001",
    "ISOP-VALUE-002",
}


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def load_combined_shapes() -> Graph:
    graph = load_graph(CORE_SHAPES_FILE)
    graph.parse(PROFILE_SHAPES_FILE, format="turtle")
    return graph


def validate_fixture(path: Path) -> tuple[bool, Graph, str]:
    return validate(
        data_graph=load_graph(path),
        shacl_graph=load_combined_shapes(),
        ont_graph=load_graph(ONTOLOGY_FILE),
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
        advanced=True,
    )


def test_isoprops_profile_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_graph(PROFILE_SHAPES_FILE),
        meta_shacl=True,
        advanced=True,
    )

    assert conforms, report


def test_isoprops_profile_shape_graph_has_version_metadata() -> None:
    graph = load_graph(PROFILE_SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/vso/isoprops/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [Literal("0.1.0")]
    assert not list(graph.objects(None, OWL.imports))


def test_profile_metadata_records_isoprops_v22_without_importing_it() -> None:
    metadata = yaml.safe_load(PROFILE_FILE.read_text(encoding="utf-8"))
    dependency = next(item for item in metadata["dependencies"] if item["id"] == "isoprops")

    assert metadata["graph_iri"] == "https://www.construct-x.org/shapes/vso/isoprops"
    assert metadata["version_iri"] == "https://www.construct-x.org/shapes/vso/isoprops/0.1.0"
    assert dependency["ontology_iri"] == "https://w3id.org/isoprops"
    assert dependency["version_iri"] == "https://w3id.org/isoprops"
    assert dependency["version"] == "v2.2"
    assert dependency["relation"] == "referenced-not-imported"


def test_repository_validator_accepts_the_profile_manifest() -> None:
    result = validate_repository(ROOT)

    assert result.ok, result.errors
    assert any(
        "vso-isoprops/profile.yaml" in info.replace("\\", "/")
        for info in result.infos
    )


def test_every_named_profile_constraint_has_bilingual_messages() -> None:
    graph = load_graph(PROFILE_SHAPES_FILE)
    constraint_types = (SH.PropertyShape, SH.SPARQLConstraint)
    constraints = {
        subject
        for constraint_type in constraint_types
        for subject in graph.subjects(RDF.type, constraint_type)
        if isinstance(subject, URIRef) and str(subject).startswith(str(PROFILE_SHAPES))
    }

    assert constraints
    for constraint in constraints:
        languages = {message.language for message in graph.objects(constraint, SH.message)}
        assert languages == {"de", "en"}


@pytest.mark.parametrize(
    "example_name",
    ["measured-property.ttl", "unitless-property.ttl"],
)
def test_public_isoprops_examples_conform(example_name: str) -> None:
    conforms, _, report = validate_fixture(EXAMPLES_DIR / example_name)

    assert conforms, report


def test_all_approved_datatype_mappings_conform() -> None:
    conforms, _, report = validate_fixture(VALID_DIR / "all-datatypes.ttl")

    assert conforms, report


INVALID_FIXTURES = (
    ("malformed-literal.ttl", {"ISOP-VALUE-002"}),
    ("non-isoprops-reference.ttl", {"ISOP-REF-001"}),
    (
        "invalid-definition-metadata.ttl",
        {
            "ISOP-ID-001",
            "ISOP-ID-002",
            "ISOP-VERSION-001",
            "ISOP-REVISION-001",
            "ISOP-STATUS-001",
            "ISOP-DATATYPE-001",
            "ISOP-UNIT-001",
            "ISOP-ASSIGN-UNIT-002",
        },
    ),
    ("mismatched-construct-x-identity.ttl", {"ISOP-ID-003"}),
    ("missing-used-unit.ttl", {"ISOP-ASSIGN-UNIT-001"}),
    ("disallowed-used-unit.ttl", {"ISOP-ASSIGN-UNIT-002"}),
    ("invalid-value-datatypes.ttl", {"ISOP-VALUE-001"}),
)


@pytest.mark.parametrize(("fixture_name", "expected_ids"), INVALID_FIXTURES)
def test_invalid_profile_fixtures_report_expected_contracts(
    fixture_name: str,
    expected_ids: set[str],
) -> None:
    conforms, _, report = validate_fixture(INVALID_DIR / fixture_name)

    assert not conforms, report
    for requirement_id in expected_ids:
        assert requirement_id in report


def test_invalid_fixture_catalog_covers_every_profile_error_code() -> None:
    covered_ids = set().union(*(expected_ids for _, expected_ids in INVALID_FIXTURES))

    assert covered_ids == EXPECTED_ERROR_IDS
