from pathlib import Path

import yaml
from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL


ROOT = Path(__file__).resolve().parents[1]
DATASET_FILES = (
    ROOT / "datasets/reference/vocabularies/address-roles/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/identifier-scheme/dataset.yaml",
    ROOT
    / "datasets/reference/administrative-territories/iso-3166-1-countries/dataset.yaml",
    ROOT
    / "datasets/reference/administrative-territories/iso-3166-2-de/dataset.yaml",
    ROOT / "datasets/reference/administrative-territories/nuts-2/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/human-sex/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/gender/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/contact-channel/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/contact-usage/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/contact-purpose/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/contact-platform/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/participation-role/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/document-type/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/document-status/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/status-kind/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/status-value/dataset.yaml",
    ROOT / "datasets/reference/vocabularies/status-reason/dataset.yaml",
)
ID_SCHEME = "https://www.construct-x.org/vocab/identifier-scheme#"


def test_every_reference_vocabulary_has_consistent_graph_version_metadata() -> None:
    for metadata_file in DATASET_FILES:
        metadata = yaml.safe_load(metadata_file.read_text(encoding="utf-8"))
        stable_iri = metadata["vocabulary_iri"]
        version = metadata["version"]
        version_iri = metadata["version_iri"]
        namespace = metadata["namespace"]
        graph = Graph().parse(
            metadata_file.parent / metadata["artifacts"]["data"], format="turtle"
        )
        subject = URIRef(stable_iri)

        assert version_iri == f"{stable_iri}/{version}"
        assert namespace == f"{stable_iri}#"
        assert (subject, RDF.type, OWL.Ontology) in graph
        assert list(graph.objects(subject, OWL.versionIRI)) == [URIRef(version_iri)]
        assert list(graph.objects(subject, OWL.versionInfo)) == [Literal(version)]


def test_identifier_scheme_terms_are_stable_declared_rdf_datatypes() -> None:
    metadata_file = DATASET_FILES[1]
    metadata = yaml.safe_load(metadata_file.read_text(encoding="utf-8"))
    graph = Graph().parse(
        metadata_file.parent / metadata["artifacts"]["data"], format="turtle"
    )
    expected_terms = {
        URIRef(f"{ID_SCHEME}iso-3166-1-alpha-2"),
        URIRef(f"{ID_SCHEME}iso-3166-1-alpha-3"),
        URIRef(f"{ID_SCHEME}iso-3166-1-numeric"),
        URIRef(f"{ID_SCHEME}iso-3166-2"),
        URIRef(f"{ID_SCHEME}nuts-2"),
    }

    assert set(graph.subjects(RDF.type, RDFS.Datatype)) == expected_terms
    assert all(
        (term, RDFS.isDefinedBy, URIRef(metadata["vocabulary_iri"])) in graph
        for term in expected_terms
    )
