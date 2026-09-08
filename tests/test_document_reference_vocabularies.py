from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, OWL, RDF, SKOS, URIRef


ROOT = Path(__file__).resolve().parents[1]
VOCABULARY_ROOT = ROOT / "datasets/reference/vocabularies"
CONX_DOC = Namespace("https://www.construct-x.org/ontology/document#")
DOCUMENT_TYPE = Namespace("https://www.construct-x.org/vocab/document-type#")
DOCUMENT_STATUS = Namespace("https://www.construct-x.org/vocab/document-status#")

VOCABULARIES = {
    "document-type": (
        URIRef("https://www.construct-x.org/vocab/document-type"),
        CONX_DOC.DocumentType,
        {
            DOCUMENT_TYPE.contract: Literal("contract"),
            DOCUMENT_TYPE.invoice: Literal("invoice"),
            DOCUMENT_TYPE.deliveryNote: Literal("delivery-note"),
            DOCUMENT_TYPE.certificate: Literal("certificate"),
            DOCUMENT_TYPE.report: Literal("report"),
            DOCUMENT_TYPE.plan: Literal("plan"),
            DOCUMENT_TYPE.evidenceDocument: Literal("evidence-document"),
            DOCUMENT_TYPE.other: Literal("other"),
        },
    ),
    "document-status": (
        URIRef("https://www.construct-x.org/vocab/document-status"),
        CONX_DOC.DocumentStatus,
        {
            DOCUMENT_STATUS.draft: Literal("draft"),
            DOCUMENT_STATUS.issued: Literal("issued"),
            DOCUMENT_STATUS.superseded: Literal("superseded"),
            DOCUMENT_STATUS.withdrawn: Literal("withdrawn"),
            DOCUMENT_STATUS.expired: Literal("expired"),
            DOCUMENT_STATUS.archived: Literal("archived"),
        },
    ),
}


def load_vocabulary(vocabulary_id: str) -> tuple[dict, Graph]:
    directory = VOCABULARY_ROOT / vocabulary_id
    metadata = yaml.safe_load((directory / "dataset.yaml").read_text(encoding="utf-8"))
    graph = Graph().parse(directory / metadata["artifacts"]["data"], format="turtle")
    return metadata, graph


def test_document_reference_vocabularies_contain_the_approved_values() -> None:
    for vocabulary_id, (scheme, document_class, expected_notations) in VOCABULARIES.items():
        metadata, graph = load_vocabulary(vocabulary_id)

        assert metadata["type"] == "reference-vocabulary"
        assert metadata["status"] == "draft"
        assert metadata["version"] == "0.1.0"
        assert (scheme, RDF.type, OWL.Ontology) in graph
        assert (scheme, RDF.type, SKOS.ConceptScheme) in graph
        assert list(graph.objects(scheme, OWL.versionIRI)) == [
            URIRef(f"{scheme}/0.1.0")
        ]
        assert list(graph.objects(scheme, OWL.versionInfo)) == [Literal("0.1.0")]

        concepts = set(graph.subjects(RDF.type, SKOS.Concept))
        assert concepts == set(expected_notations)
        assert set(graph.objects(scheme, SKOS.hasTopConcept)) == concepts

        for concept, notation in expected_notations.items():
            assert (concept, RDF.type, document_class) in graph
            assert (concept, SKOS.inScheme, scheme) in graph
            assert (concept, SKOS.topConceptOf, scheme) in graph
            assert list(graph.objects(concept, SKOS.notation)) == [notation]
            assert {
                label.language for label in graph.objects(concept, SKOS.prefLabel)
            } == {"de", "en"}
            assert {
                definition.language
                for definition in graph.objects(concept, SKOS.definition)
            } == {"de", "en"}


def test_document_reference_vocabularies_do_not_import_external_ontologies() -> None:
    for vocabulary_id, (scheme, _, _) in VOCABULARIES.items():
        _, graph = load_vocabulary(vocabulary_id)
        assert not list(graph.objects(scheme, OWL.imports))
