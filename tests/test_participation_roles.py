from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, OWL, RDF, SKOS, URIRef


ROOT = Path(__file__).resolve().parents[1]
VOCABULARY_DIR = ROOT / "datasets/reference/vocabularies/participation-role"
METADATA_FILE = VOCABULARY_DIR / "dataset.yaml"
CONX_PART = Namespace("https://www.construct-x.org/ontology/participation#")
PART_ROLE = Namespace("https://www.construct-x.org/vocab/participation-role#")
SCHEME = URIRef("https://www.construct-x.org/vocab/participation-role")
EXPECTED_NOTATIONS = {
    PART_ROLE.ClientRole: Literal("client"),
    PART_ROLE.ContractorRole: Literal("contractor"),
    PART_ROLE.SupplierRole: Literal("supplier"),
    PART_ROLE.ArchitectRole: Literal("architect"),
    PART_ROLE.EngineerRole: Literal("engineer"),
}


def load_vocabulary() -> tuple[dict, Graph]:
    metadata = yaml.safe_load(METADATA_FILE.read_text(encoding="utf-8"))
    graph = Graph().parse(
        VOCABULARY_DIR / metadata["artifacts"]["data"], format="turtle"
    )
    return metadata, graph


def test_participation_role_vocabulary_contains_exactly_the_approved_values() -> None:
    metadata, graph = load_vocabulary()

    assert metadata["id"] == "participation-role"
    assert metadata["type"] == "reference-vocabulary"
    assert metadata["status"] == "draft"
    assert metadata["version"] == "0.1.0"
    assert (SCHEME, RDF.type, OWL.Ontology) in graph
    assert (SCHEME, RDF.type, SKOS.ConceptScheme) in graph
    assert list(graph.objects(SCHEME, OWL.versionIRI)) == [
        URIRef("https://www.construct-x.org/vocab/participation-role/0.1.0")
    ]
    assert list(graph.objects(SCHEME, OWL.versionInfo)) == [Literal("0.1.0")]

    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    assert concepts == set(EXPECTED_NOTATIONS)
    assert set(graph.objects(SCHEME, SKOS.hasTopConcept)) == concepts

    for concept, notation in EXPECTED_NOTATIONS.items():
        assert (concept, RDF.type, CONX_PART.Role) in graph
        assert (concept, SKOS.inScheme, SCHEME) in graph
        assert (concept, SKOS.topConceptOf, SCHEME) in graph
        assert list(graph.objects(concept, SKOS.notation)) == [notation]
        assert {label.language for label in graph.objects(concept, SKOS.prefLabel)} == {
            "de",
            "en",
        }
        assert {
            definition.language for definition in graph.objects(concept, SKOS.definition)
        } == {"de", "en"}


def test_participation_role_vocabulary_does_not_import_other_ontologies() -> None:
    _, graph = load_vocabulary()
    assert not list(graph.objects(SCHEME, OWL.imports))
