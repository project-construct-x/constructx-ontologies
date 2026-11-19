import shutil

import pytest
from rdflib import BNode, Graph, Namespace, OWL, RDF, URIRef
from rdflib.compare import isomorphic

from scripts.validate_status import (
    ROOT, SH, TARGET_PREDICATES, StatusDependencyError,
    load_status_shapes, load_status_vocabularies, validate_status,
)

MODULE = ROOT / "modules/core/status"
VSO = Namespace("https://www.construct-x.org/ontology/vso#")
EX = Namespace("https://example.org/status/")
SCHEMA = Namespace("https://schema.org/")


def test_unrelated_vso_data_does_not_acquire_isoprops_requirements() -> None:
    graph = Graph().parse(MODULE / "examples/status-with-condition.ttl")
    graph.parse(data="""
      @prefix vso: <https://www.construct-x.org/ontology/vso#> .
      @prefix schema: <https://schema.org/> .
      @prefix ex: <https://example.org/unrelated/> .
      ex:object vso:hasProperty ex:assignment .
      ex:assignment a vso:AssignedProperty ;
        vso:hasPropertyReference ex:definition ;
        vso:hasPropertyState ex:state .
      ex:state a vso:PropertyState ; schema:value "A generic VSO text value" .
    """, format="turtle")
    conforms, _, report = validate_status(graph)
    assert conforms, report


@pytest.mark.parametrize("source", [
    "modules/core/vso/shapes/conx-vso-core.shacl.ttl",
    "profiles/construct-x/vso-isoprops/shapes/conx-vso-isoprops.shacl.ttl",
])
def test_dependency_targets_are_scoped_but_rules_are_reused(source) -> None:
    combined = load_status_shapes()
    vso_source = Graph().parse(ROOT / source)
    expected = Graph()
    for triple in vso_source:
        if triple[1] in TARGET_PREDICATES:
            assert triple not in combined
        else:
            expected.add(triple)
    actual = Graph()
    pending = [s for s in set(vso_source.subjects()) if isinstance(s, URIRef)]
    visited = set()
    while pending:
        subject = pending.pop()
        if subject in visited:
            continue
        visited.add(subject)
        for triple in combined.triples((subject, None, None)):
            actual.add(triple)
            if isinstance(triple[2], BNode):
                pending.append(triple[2])
    assert isomorphic(expected, actual)
    assert list(vso_source.triples((None, SH.targetClass, None)))
    assert list(combined.triples((None, SH.targetObjectsOf, URIRef("https://www.construct-x.org/ontology/status#hasCondition"))))


def test_structured_resource_is_not_a_numeric_measurement() -> None:
    graph = Graph().parse(MODULE / "examples/status-with-condition.ttl")
    graph.set((EX.measuredState, SCHEMA.value, EX.nestedValue))
    conforms, _, report = validate_status(graph)
    assert not conforms, report
    assert "ISOP-VALUE-001" in report


def test_new_measurement_has_a_separate_assignment_and_state() -> None:
    graph = Graph().parse(MODULE / "examples/status-with-condition.ttl")
    graph.parse(data="""
      @prefix s: <https://www.construct-x.org/ontology/status#> .
      @prefix kind: <https://www.construct-x.org/vocab/status-kind#> .
      @prefix value: <https://www.construct-x.org/vocab/status-value#> .
      @prefix vso: <https://www.construct-x.org/ontology/vso#> .
      @prefix schema: <https://schema.org/> .
      @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
      @prefix unit: <http://qudt.org/vocab/unit/> .
      @prefix ex: <https://example.org/status/> .
      ex:delivery s:hasStatus ex:s2 .
      ex:s2 a s:StatusAssignment ; s:hasStatusKind kind:TemperatureInspection ;
        s:hasStatusValue value:Passed ; s:referenceDate "2026-11-10"^^xsd:date ;
        s:referenceTime "11:00:00+01:00"^^xsd:time ; s:previousStatus ex:s1 ;
        s:hasCondition ex:measurement2 .
      ex:goods vso:hasProperty ex:measurement2 .
      ex:measurement2 a vso:AssignedProperty ;
        vso:hasPropertyReference <https://properties.example.org/temperature/revision/1> ;
        vso:hasPropertyState ex:state2 .
      ex:state2 a vso:PropertyState ; schema:value "5.0"^^xsd:decimal ;
        vso:hasUsedUnit unit:DEG_C .
    """, format="turtle")
    graph.set((EX.delivery, URIRef("https://www.construct-x.org/ontology/status#hasCurrentStatus"), EX.s2))
    conforms, _, report = validate_status(graph)
    assert conforms, report
    assert len(list(graph.objects(EX.measuredState, SCHEMA.value))) == 1
    assert str(next(graph.objects(EX.measuredState, SCHEMA.value))) == "8.0"


def test_missing_dependency_is_a_setup_error(tmp_path) -> None:
    with pytest.raises(StatusDependencyError, match="Missing status validation dependency"):
        load_status_shapes(tmp_path)


def test_mismatched_reference_version_is_a_setup_error(tmp_path) -> None:
    relative = "datasets/reference/vocabularies/status-kind"
    shutil.copytree(ROOT / relative, tmp_path / relative)
    path = tmp_path / relative / "status-kind.ttl"
    graph = Graph().parse(path)
    scheme = URIRef("https://www.construct-x.org/vocab/status-kind")
    graph.set((scheme, OWL.versionIRI, URIRef(str(scheme) + "/9.0.0")))
    graph.serialize(path, format="turtle")
    with pytest.raises(StatusDependencyError, match="Expected"):
        load_status_vocabularies(tmp_path)
