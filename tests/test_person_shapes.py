from pathlib import Path

import pytest
import yaml
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/person"
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-person.ttl"
SHAPES_FILE = MODULE_DIR / "shapes/conx-person-core.shacl.ttl"
IDENTIFIER_SHAPES_FILE = (
    ROOT / "modules/core/identifier/shapes/conx-id-core.shacl.ttl"
)
VALID_DIR = MODULE_DIR / "tests/valid"
INVALID_DIR = MODULE_DIR / "tests/invalid"
REFERENCE_FILES = (
    ROOT / "datasets/reference/vocabularies/human-sex/human-sex.ttl",
    ROOT / "datasets/reference/vocabularies/gender/gender.ttl",
    ROOT
    / "datasets/reference/administrative-territories/iso-3166-1-countries/data/countries.ttl",
)

CONX_PERSON = Namespace("https://www.construct-x.org/ontology/person#")
CONX_PERSON_SH = Namespace("https://www.construct-x.org/shapes/person/core#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SHAPE_GRAPH_IRI = URIRef("https://www.construct-x.org/shapes/person/core")


def load_graph(path: Path) -> Graph:
    return Graph().parse(path, format="turtle")


def load_data_with_references(path: Path) -> Graph:
    graph = load_graph(path)
    for reference_file in REFERENCE_FILES:
        graph.parse(reference_file, format="turtle")
    return graph


def load_shapes_graph() -> Graph:
    graph = load_graph(SHAPES_FILE)
    graph.parse(IDENTIFIER_SHAPES_FILE, format="turtle")
    return graph


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


def test_person_core_shapes_are_valid_shacl() -> None:
    conforms, _, report = validate(
        data_graph=Graph(),
        shacl_graph=load_shapes_graph(),
        meta_shacl=True,
    )

    assert conforms, report


def test_person_shape_graph_has_consistent_version_metadata() -> None:
    graph = load_graph(SHAPES_FILE)

    assert (SHAPE_GRAPH_IRI, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/shapes/person/core/0.1.0")
    ]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.versionInfo)) == [Literal("0.1.0")]
    assert list(graph.objects(SHAPE_GRAPH_IRI, OWL.imports)) == [
        URIRef("https://www.construct-x.org/shapes/identifier/core/0.1.0")
    ]


def test_person_shape_targets_person_properties_but_not_generic_identifiers() -> None:
    graph = load_graph(SHAPES_FILE)
    targets = set(graph.objects(CONX_PERSON_SH.PersonShape, SH.targetSubjectsOf))

    assert CONX_PERSON.fullName in targets
    assert CONX_PERSON.hasIdentityEvidence in targets
    assert ADMS.identifier not in targets


def test_every_named_person_property_shape_has_bilingual_messages() -> None:
    graph = load_graph(SHAPES_FILE)
    property_shapes = {
        shape
        for shape in graph.subjects(RDF.type, SH.PropertyShape)
        if isinstance(shape, URIRef) and str(shape).startswith(str(CONX_PERSON_SH))
    }

    assert property_shapes
    for shape in property_shapes:
        languages = {message.language for message in graph.objects(shape, SH.message)}
        assert languages == {"de", "en"}


def test_person_module_metadata_registers_the_core_shape_set() -> None:
    metadata = yaml.safe_load((MODULE_DIR / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-person-core.shacl.ttl"
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/person/core",
        "version_iri": "https://www.construct-x.org/shapes/person/core/0.1.0",
        "namespace": "https://www.construct-x.org/shapes/person/core#",
        "version": "0.1.0",
        "artifact": "shapes/conx-person-core.shacl.ttl",
    }


@pytest.mark.parametrize(
    "fixture_name",
    [
        "minimal-person.ttl",
        "complete-person.ttl",
        "gender-not-disclosed.ttl",
    ],
)
def test_valid_person_fixtures_conform(fixture_name: str) -> None:
    conforms, _, report = validate_fixture(VALID_DIR / fixture_name)

    assert conforms, report


@pytest.mark.parametrize(
    ("fixture_name", "expected_paths", "expected_ids"),
    [
        (
            "missing-required-names.ttl",
            {CONX_PERSON.fullName, CONX_PERSON.givenName},
            {"PER-001", "PER-002", "PER-010", "PER-011"},
        ),
        (
            "invalid-name-values.ttl",
            {
                CONX_PERSON.fullName,
                CONX_PERSON.familyName,
                CONX_PERSON.additionalName,
                CONX_PERSON.birthName,
                CONX_PERSON.birthPlaceName,
            },
            {"PER-010", "PER-012", "PER-013", "PER-014", "PER-021"},
        ),
        (
            "invalid-birth-values.ttl",
            {CONX_PERSON.birthDate},
            {"PER-020"},
        ),
        (
            "invalid-controlled-values.ttl",
            {CONX_PERSON.sex, CONX_PERSON.gender, CONX_PERSON.citizenship},
            {"PER-030", "PER-031", "PER-040"},
        ),
        (
            "invalid-identifier-and-evidence.ttl",
            {
                ADMS.identifier,
                SKOS.notation,
                ADMS.schemaAgency,
                CONX_PERSON.hasIdentityEvidence,
            },
            {"PER-050", "ID-001", "ID-002", "ID-003", "PER-060"},
        ),
    ],
)
def test_invalid_person_fixtures_report_expected_contracts(
    fixture_name: str,
    expected_paths: set[URIRef],
    expected_ids: set[str],
) -> None:
    conforms, report_graph, report = validate_fixture(INVALID_DIR / fixture_name)
    result_paths = set(report_graph.objects(None, SH.resultPath))

    assert not conforms, report
    assert expected_paths.issubset(result_paths)
    for requirement_id in expected_ids:
        assert requirement_id in report
