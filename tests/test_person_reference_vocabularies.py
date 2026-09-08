from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, SKOS, URIRef


ROOT = Path(__file__).resolve().parents[1]
VOCABULARY_ROOT = ROOT / "datasets/reference/vocabularies"
HUMAN_SEX = Namespace("https://www.construct-x.org/vocab/human-sex#")
GENDER = Namespace("https://www.construct-x.org/vocab/gender#")
HUMAN_SEX_SCHEME = URIRef("https://www.construct-x.org/vocab/human-sex")
GENDER_SCHEME = URIRef("https://www.construct-x.org/vocab/gender")

EXPECTED_HUMAN_SEX_CODES = {
    HUMAN_SEX.notKnown: Literal("0", datatype=HUMAN_SEX["iso-iec-5218"]),
    HUMAN_SEX.male: Literal("1", datatype=HUMAN_SEX["iso-iec-5218"]),
    HUMAN_SEX.female: Literal("2", datatype=HUMAN_SEX["iso-iec-5218"]),
    HUMAN_SEX.notApplicable: Literal("9", datatype=HUMAN_SEX["iso-iec-5218"]),
}
EXPECTED_GENDER_NOTATIONS = {
    GENDER.man: Literal("man"),
    GENDER.woman: Literal("woman"),
    GENDER.nonBinaryOrDiverse: Literal("non-binary-or-diverse"),
    GENDER.notDisclosed: Literal("not-disclosed"),
}


def load_vocabulary(vocabulary_id: str) -> tuple[dict, Graph]:
    directory = VOCABULARY_ROOT / vocabulary_id
    metadata = yaml.safe_load((directory / "dataset.yaml").read_text(encoding="utf-8"))
    graph = Graph().parse(directory / metadata["artifacts"]["data"], format="turtle")
    return metadata, graph


def assert_controlled_vocabulary(
    metadata: dict,
    graph: Graph,
    scheme: URIRef,
    expected_notations: dict[URIRef, Literal],
) -> None:
    assert metadata["type"] == "reference-vocabulary"
    assert metadata["status"] == "draft"
    assert metadata["version"] == "0.1.0"
    assert (scheme, RDF.type, OWL.Ontology) in graph
    assert (scheme, RDF.type, SKOS.ConceptScheme) in graph
    assert list(graph.objects(scheme, OWL.versionIRI)) == [
        URIRef(f"{scheme}/{metadata['version']}")
    ]

    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    assert concepts == set(expected_notations)
    assert set(graph.objects(scheme, SKOS.hasTopConcept)) == concepts

    for concept, notation in expected_notations.items():
        assert (concept, SKOS.inScheme, scheme) in graph
        assert (concept, SKOS.topConceptOf, scheme) in graph
        assert list(graph.objects(concept, SKOS.notation)) == [notation]
        label_languages = {
            label.language for label in graph.objects(concept, SKOS.prefLabel)
        }
        definition_languages = {
            definition.language for definition in graph.objects(concept, SKOS.definition)
        }
        assert label_languages == {"de", "en"}
        assert definition_languages == {"de", "en"}


def test_human_sex_vocabulary_encodes_the_iso_iec_5218_values() -> None:
    metadata, graph = load_vocabulary("human-sex")

    assert_controlled_vocabulary(
        metadata, graph, HUMAN_SEX_SCHEME, EXPECTED_HUMAN_SEX_CODES
    )
    assert (
        HUMAN_SEX_SCHEME,
        URIRef("http://purl.org/dc/terms/source"),
        URIRef("https://www.iso.org/standard/81682.html"),
    ) in graph
    assert (HUMAN_SEX["iso-iec-5218"], RDF.type, RDFS.Datatype) in graph
    assert (
        HUMAN_SEX["iso-iec-5218"], RDFS.isDefinedBy, HUMAN_SEX_SCHEME
    ) in graph


def test_gender_vocabulary_contains_the_approved_initial_values() -> None:
    metadata, graph = load_vocabulary("gender")

    assert_controlled_vocabulary(
        metadata, graph, GENDER_SCHEME, EXPECTED_GENDER_NOTATIONS
    )
    assert Literal("Man", lang="en") in graph.objects(GENDER.man, SKOS.prefLabel)
    assert Literal("Woman", lang="en") in graph.objects(GENDER.woman, SKOS.prefLabel)
    assert Literal("Prefer not to say", lang="en") in graph.objects(
        GENDER.notDisclosed, SKOS.altLabel
    )
    assert any(
        "not a gender identity" in str(note)
        for note in graph.objects(GENDER.notDisclosed, SKOS.scopeNote)
    )


def test_person_reference_vocabularies_do_not_import_external_ontologies() -> None:
    for vocabulary_id, scheme in (
        ("human-sex", HUMAN_SEX_SCHEME),
        ("gender", GENDER_SCHEME),
    ):
        _, graph = load_vocabulary(vocabulary_id)
        assert not list(graph.objects(scheme, OWL.imports))
