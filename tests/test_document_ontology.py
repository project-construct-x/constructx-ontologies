from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/document"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-doc.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/document")
CONX_DOC = Namespace("https://www.construct-x.org/ontology/document#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_DOC))
    }


def test_document_tbox_contains_exactly_the_approved_terms() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == {
        CONX_DOC.Document,
        CONX_DOC.DocumentReference,
        CONX_DOC.DocumentDistribution,
        CONX_DOC.DocumentType,
        CONX_DOC.DocumentStatus,
    }
    assert local_terms_of_type(graph, OWL.ObjectProperty) == {
        CONX_DOC.hasDocumentReference,
        CONX_DOC.referencesDocument,
        CONX_DOC.hasDistribution,
        CONX_DOC.documentType,
        CONX_DOC.documentStatus,
    }
    assert local_terms_of_type(graph, OWL.DatatypeProperty) == {
        CONX_DOC.title,
        CONX_DOC.description,
        CONX_DOC.language,
        CONX_DOC.version,
        CONX_DOC.created,
        CONX_DOC.issued,
        CONX_DOC.modified,
        CONX_DOC.validFrom,
        CONX_DOC.validUntil,
        CONX_DOC.fileName,
    }
    assert not local_terms_of_type(graph, OWL.NamedIndividual)


def test_document_class_and_object_property_contracts_match_the_model() -> None:
    graph = load_graph()

    assert (CONX_DOC.DocumentType, RDFS.subClassOf, SKOS.Concept) in graph
    assert (CONX_DOC.DocumentStatus, RDFS.subClassOf, SKOS.Concept) in graph
    assert not list(graph.objects(CONX_DOC.Document, RDFS.subClassOf))
    assert not list(graph.objects(CONX_DOC.DocumentDistribution, RDFS.subClassOf))

    assert not list(graph.objects(CONX_DOC.hasDocumentReference, RDFS.domain))
    assert list(graph.objects(CONX_DOC.hasDocumentReference, RDFS.range)) == [
        CONX_DOC.DocumentReference
    ]
    assert list(graph.objects(CONX_DOC.referencesDocument, RDFS.domain)) == [
        CONX_DOC.DocumentReference
    ]
    assert list(graph.objects(CONX_DOC.referencesDocument, RDFS.range)) == [
        CONX_DOC.Document
    ]
    assert not list(graph.objects(CONX_DOC.hasDistribution, RDFS.domain))
    assert list(graph.objects(CONX_DOC.hasDistribution, RDFS.range)) == [
        CONX_DOC.DocumentDistribution
    ]
    assert not list(graph.objects(CONX_DOC.documentType, RDFS.domain))
    assert list(graph.objects(CONX_DOC.documentType, RDFS.range)) == [
        CONX_DOC.DocumentType
    ]
    assert list(graph.objects(CONX_DOC.documentStatus, RDFS.domain)) == [
        CONX_DOC.Document
    ]
    assert list(graph.objects(CONX_DOC.documentStatus, RDFS.range)) == [
        CONX_DOC.DocumentStatus
    ]


def test_document_datatype_properties_keep_the_approved_boundaries() -> None:
    graph = load_graph()

    assert list(graph.objects(CONX_DOC.fileName, RDFS.domain)) == [
        CONX_DOC.DocumentDistribution
    ]
    assert list(graph.objects(CONX_DOC.fileName, RDFS.range)) == [XSD.string]
    for property_iri in (
        CONX_DOC.title,
        CONX_DOC.description,
        CONX_DOC.language,
        CONX_DOC.version,
        CONX_DOC.created,
        CONX_DOC.issued,
        CONX_DOC.modified,
        CONX_DOC.validFrom,
        CONX_DOC.validUntil,
    ):
        assert not list(graph.objects(property_iri, RDFS.domain))
        assert list(graph.objects(property_iri, RDFS.range))


def test_document_tbox_keeps_validation_and_excluded_terms_outside_owl() -> None:
    graph = load_graph()

    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))
    assert not set(graph.subjects(RDF.type, OWL.Restriction))
    assert not set(graph.subjects(OWL.inverseOf, None))
    assert ADMS.identifier not in local_terms_of_type(graph, OWL.ObjectProperty)
    assert DCAT.accessURL not in local_terms_of_type(graph, OWL.ObjectProperty)


def test_document_module_metadata_matches_the_implementation() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "document"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.1.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.1.0"
    assert metadata["namespace"] == str(CONX_DOC)
    assert metadata["preferred_namespace_prefix"] == "conx-doc"
    assert metadata["artifacts"]["ontology"] == "ontology/conx-doc.ttl"
    assert metadata["artifacts"]["core_shapes"] == (
        "shapes/conx-doc-core.shacl.ttl"
    )
    assert metadata["artifacts"]["strict_shapes"] is None
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/document/core",
        "version_iri": "https://www.construct-x.org/shapes/document/core/0.1.0",
        "namespace": "https://www.construct-x.org/shapes/document/core#",
        "version": "0.1.0",
        "artifact": "shapes/conx-doc-core.shacl.ttl",
    }

    dependencies = {dependency["id"]: dependency for dependency in metadata["dependencies"]}
    assert set(dependencies) == {
        "document-type",
        "document-status",
        "identifier",
        "adms",
        "dcat",
        "dcterms",
        "foaf",
        "schema-org",
        "skos",
    }
    assert dependencies["identifier"]["relation"] == "shape-imported"
    assert all(
        dependency["relation"] == "referenced-not-imported"
        for dependency_id, dependency in dependencies.items()
        if dependency_id != "identifier"
    )
