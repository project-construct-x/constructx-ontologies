import pytest
from rdflib import Graph, Literal, Namespace, RDF, SKOS, URIRef
from scripts.validate_status import ROOT, load_status_vocabularies, validate_status

S = Namespace("https://www.construct-x.org/ontology/status#")
K = Namespace("https://www.construct-x.org/vocab/status-kind#")
V = Namespace("https://www.construct-x.org/vocab/status-value#")
R = Namespace("https://www.construct-x.org/vocab/status-reason#")


def test_approved_initial_vocabularies_and_compatibility() -> None:
    graph = load_status_vocabularies()
    assert set(graph.subjects(RDF.type, S.StatusKind)) == {K.TransportStatus, K.TemperatureInspection, K.QuantityInspection}
    assert set(graph.subjects(RDF.type, S.StatusValue)) == {V.InProgress, V.Shipped, V.Delivered, V.NotChecked, V.Passed, V.Failed}
    assert set(graph.subjects(RDF.type, S.StatusReason)) == {R.VehicleBreakdown, R.AccessBlocked, R.TemperatureExceeded, R.QuantityMismatch}
    assert set(graph.objects(K.TransportStatus, S.hasAllowedStatusValue)) == {V.InProgress, V.Shipped, V.Delivered}
    for kind in (K.TemperatureInspection, K.QuantityInspection):
        assert set(graph.objects(kind, S.hasAllowedStatusValue)) == {V.NotChecked, V.Passed, V.Failed}
    assert set(graph.objects(K.TransportStatus, S.hasAllowedStatusReason)) == {R.VehicleBreakdown, R.AccessBlocked}
    assert set(graph.objects(K.TemperatureInspection, S.hasAllowedStatusReason)) == {R.TemperatureExceeded}
    assert set(graph.objects(K.QuantityInspection, S.hasAllowedStatusReason)) == {R.QuantityMismatch}
    for term in graph.subjects(RDF.type, SKOS.Concept):
        assert {v.language for v in graph.objects(term, SKOS.prefLabel)} == {"de", "en"}
        assert {v.language for v in graph.objects(term, SKOS.definition)} == {"de", "en"}
    conforms, _, report = validate_status(graph, include_reference_vocabularies=False)
    assert conforms, report


@pytest.mark.parametrize("predicate", [SKOS.prefLabel, SKOS.definition, SKOS.notation, SKOS.inScheme])
def test_managed_terms_require_publication_metadata(predicate) -> None:
    graph = load_status_vocabularies()
    graph.remove((V.Failed, predicate, None))
    conforms, _, report = validate_status(graph, include_reference_vocabularies=False)
    assert not conforms, report


@pytest.mark.parametrize("mutation", ["duplicate-label", "duplicate-code", "two-codes", "wrong-code-type", "plain-label", "same-alternative-label"])
def test_invalid_managed_metadata_is_rejected(mutation: str) -> None:
    graph = load_status_vocabularies()
    if mutation == "duplicate-label":
        graph.add((V.Failed, SKOS.prefLabel, Literal("Another label", lang="en")))
    elif mutation == "duplicate-code":
        graph.set((V.Failed, SKOS.notation, Literal("passed")))
    elif mutation == "two-codes":
        graph.add((V.Failed, SKOS.notation, Literal("another-code")))
    elif mutation == "wrong-code-type":
        graph.set((V.Failed, SKOS.notation, Literal(42)))
    elif mutation == "plain-label":
        graph.add((V.Failed, SKOS.prefLabel, Literal("No language")))
    else:
        graph.add((V.Failed, SKOS.altLabel, Literal("Failed", lang="en")))
    conforms, _, report = validate_status(graph, include_reference_vocabularies=False)
    assert not conforms, report


def test_multiple_scheme_memberships_and_optional_metadata_are_allowed() -> None:
    graph = load_status_vocabularies()
    scheme = URIRef("https://example.org/vocab/quality")
    graph.add((scheme, RDF.type, SKOS.ConceptScheme))
    graph.add((V.Failed, SKOS.inScheme, scheme))
    graph.add((V.Failed, SKOS.altLabel, Literal("Rejected by inspection", lang="en")))
    graph.add((V.Failed, SKOS.scopeNote, Literal("Does not imply a transport state.", lang="en")))
    conforms, _, report = validate_status(graph, include_reference_vocabularies=False)
    assert conforms, report


def test_an_unused_kind_need_not_have_allowed_values() -> None:
    graph = load_status_vocabularies()
    graph.remove((K.TransportStatus, S.hasAllowedStatusValue, None))
    conforms, _, report = validate_status(graph, include_reference_vocabularies=False)
    assert conforms, report


def test_external_terms_do_not_inherit_our_publication_metadata_requirements() -> None:
    data = Graph().parse(ROOT / "modules/core/status/tests/valid/external-vocabulary.ttl")
    conforms, _, report = validate_status(data, include_reference_vocabularies=False)
    assert conforms, report
