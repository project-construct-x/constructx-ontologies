from pathlib import Path

from rdflib import Graph, Namespace, OWL, RDF, RDFS, SKOS, URIRef
import yaml

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules/core/status"
S = Namespace("https://www.construct-x.org/ontology/status#")


def ontology() -> Graph:
    return Graph().parse(MODULE / "ontology/conx-status.ttl", format="turtle")


def test_status_public_contract_has_expected_terms_and_no_deferred_classes() -> None:
    graph = ontology()
    assert set(graph.subjects(RDF.type, OWL.Class)) == {
        S.StatusAssignment, S.StatusKind, S.StatusValue, S.StatusReason,
    }
    assert set(graph.subjects(RDF.type, OWL.ObjectProperty)) == {
        S.hasStatus, S.hasCurrentStatus, S.hasStatusKind, S.hasStatusValue,
        S.hasStatusReason, S.hasAllowedStatusValue, S.hasAllowedStatusReason,
        S.previousStatus, S.reportedBy, S.hasCondition,
    }
    assert set(graph.subjects(RDF.type, OWL.DatatypeProperty)) == {
        S.referenceDate, S.referenceTime, S.recordedAt, S.description, S.reasonText,
    }
    for cls in (S.StatusKind, S.StatusValue, S.StatusReason):
        assert (cls, RDFS.subClassOf, SKOS.Concept) in graph


def test_history_and_current_status_have_distinct_semantics() -> None:
    graph = ontology()
    assert (S.hasCurrentStatus, RDFS.subPropertyOf, S.hasStatus) in graph
    assert (S.hasCurrentStatus, RDF.type, OWL.FunctionalProperty) not in graph
    assert (S.previousStatus, RDF.type, OWL.TransitiveProperty) not in graph
    assert not list(graph.objects(S.hasStatus, RDFS.domain))
    assert not list(graph.objects(S.hasCurrentStatus, RDFS.domain))


def test_module_metadata_matches_ontology_and_shape_versions() -> None:
    metadata = yaml.safe_load((MODULE / "module.yaml").read_text(encoding="utf-8"))
    graph = ontology()
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.1.0"
    assert (URIRef(metadata["ontology_iri"]), OWL.versionIRI, URIRef(metadata["version_iri"])) in graph
    assert metadata["shape_sets"]["core"]["artifact"] == metadata["artifacts"]["core_shapes"]
    for field, relative in metadata["artifacts"].items():
        if isinstance(relative, str):
            assert (MODULE / relative).is_file(), (field, relative)


def test_status_is_domain_independent_and_has_no_fixed_vocabulary_enumeration() -> None:
    graph = ontology()
    assert not list(graph.triples((None, OWL.imports, None)))
    assert not list(graph.triples((None, OWL.oneOf, None)))
    assert not any("/ontology/delivery" in str(term) for triple in graph for term in triple)
    metadata = yaml.safe_load((MODULE / "module.yaml").read_text(encoding="utf-8"))
    assert {d["id"] for d in metadata["dependencies"]}.isdisjoint({"delivery", "project"})


def test_local_terms_have_bilingual_labels_and_comments() -> None:
    graph = ontology()
    for category in (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty):
        for term in graph.subjects(RDF.type, category):
            assert {v.language for v in graph.objects(term, RDFS.label)} == {"de", "en"}
            assert {v.language for v in graph.objects(term, RDFS.comment)} == {"de", "en"}
