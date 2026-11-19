"""Current status must be the uniquely latest known assignment, if provided."""
import pytest
from rdflib import BNode, Graph, Literal, Namespace, RDF, XSD

from scripts.validate_status import validate_status

S = Namespace("https://www.construct-x.org/ontology/status#")
K = Namespace("https://www.construct-x.org/vocab/status-kind#")
V = Namespace("https://www.construct-x.org/vocab/status-value#")
EX = Namespace("https://example.org/current-status/")


def add_status(graph, node, *, time="10:00:00Z", date="2026-11-10",
               owner=EX.object, kind=K.TransportStatus, value=V.Shipped, previous=None):
    graph.add((owner, S.hasStatus, node))
    graph.add((node, RDF.type, S.StatusAssignment))
    graph.add((node, S.hasStatusKind, kind))
    graph.add((node, S.hasStatusValue, value))
    graph.add((node, S.referenceDate, Literal(date, datatype=XSD.date, normalize=False)))
    graph.add((node, S.referenceTime, Literal(time, datatype=XSD.time, normalize=False)))
    if previous is not None:
        graph.add((node, S.previousStatus, previous))


def assert_valid(graph):
    conforms, _, report = validate_status(graph)
    assert conforms, report


def assert_invalid(graph, code):
    conforms, _, report = validate_status(graph)
    assert not conforms and code in report, report


@pytest.mark.parametrize("second_time", ["10:00:00Z", "12:00:00Z"])
def test_current_link_is_optional_even_when_latest_is_ambiguous(second_time):
    graph = Graph()
    add_status(graph, EX.a)
    add_status(graph, EX.b, time=second_time)
    before = set(graph)
    assert_valid(graph)
    assert set(graph) == before
    assert not list(graph.triples((None, S.hasCurrentStatus, None)))


@pytest.mark.parametrize("date_a,time_a,date_b,time_b", [
    ("2026-11-10", "09:00:00Z", "2026-11-10", "12:00:00Z"),
    # A's wall-clock time looks later, but B is later in UTC.
    ("2026-11-10", "10:30:00+02:00", "2026-11-10", "09:00:00Z"),
    # A's calendar date looks later, but B is later in UTC.
    ("2026-11-11", "00:30:00+02:00", "2026-11-10", "23:00:00Z"),
    ("2026-11-10", "10:00:00.000001Z", "2026-11-10", "10:00:00.000002Z"),
])
def test_business_instant_determines_latest_without_predecessor_links(date_a, time_a, date_b, time_b):
    graph = Graph()
    add_status(graph, EX.a, date=date_a, time=time_a)
    add_status(graph, EX.b, date=date_b, time=time_b)
    graph.set((EX.object, S.hasCurrentStatus, EX.a))
    assert_invalid(graph, "STATUS-064")
    graph.set((EX.object, S.hasCurrentStatus, EX.b))
    assert_valid(graph)


def test_late_recording_does_not_make_an_older_status_current():
    graph = Graph()
    add_status(graph, EX.shipped, time="09:00:00Z")
    add_status(graph, EX.delivered, time="12:00:00Z", value=V.Delivered)
    graph.add((EX.shipped, S.recordedAt, Literal("2026-11-10T13:00:00Z", datatype=XSD.dateTime)))
    graph.add((EX.delivered, S.recordedAt, Literal("2026-11-10T12:05:00Z", datatype=XSD.dateTime)))
    graph.set((EX.object, S.hasCurrentStatus, EX.shipped))
    assert_invalid(graph, "STATUS-064")
    graph.set((EX.object, S.hasCurrentStatus, EX.delivered))
    assert_valid(graph)


@pytest.mark.parametrize("second_value", [V.Shipped, V.Delivered])
def test_unordered_latest_ties_reject_either_selection_even_with_different_recording_times(second_value):
    graph = Graph()
    add_status(graph, EX.a, time="10:00:00+01:00")
    add_status(graph, EX.b, time="09:00:00Z", value=second_value)
    graph.add((EX.a, S.recordedAt, Literal("2026-11-10T11:00:00Z", datatype=XSD.dateTime)))
    graph.add((EX.b, S.recordedAt, Literal("2026-11-10T12:00:00Z", datatype=XSD.dateTime)))
    for selected in (EX.a, EX.b):
        graph.set((EX.object, S.hasCurrentStatus, selected))
        assert_invalid(graph, "STATUS-065")


def test_equal_time_chain_identifies_the_latest_via_indirect_predecessors():
    graph = Graph()
    add_status(graph, EX.a, time="10:00:00+01:00")
    add_status(graph, EX.b, time="09:00:00Z", previous=EX.a)
    add_status(graph, EX.c, time="11:00:00+02:00", previous=EX.b)
    for selected in (EX.a, EX.b):
        graph.set((EX.object, S.hasCurrentStatus, selected))
        assert_invalid(graph, "STATUS-064")
    graph.set((EX.object, S.hasCurrentStatus, EX.c))
    assert_valid(graph)
    # A disconnected equal-time observation makes even this endpoint ambiguous.
    add_status(graph, EX.d, time="09:00:00Z")
    assert_invalid(graph, "STATUS-065")


def test_shared_predecessor_does_not_resolve_a_latest_tie():
    graph = Graph()
    add_status(graph, EX.a, time="08:00:00Z")
    add_status(graph, EX.b, previous=EX.a)
    add_status(graph, EX.c, previous=EX.a)
    graph.set((EX.object, S.hasCurrentStatus, EX.b))
    assert_invalid(graph, "STATUS-065")


def test_ambiguity_in_older_history_does_not_block_a_unique_latest_status():
    graph = Graph()
    add_status(graph, EX.a)
    add_status(graph, EX.b)
    add_status(graph, EX.c, time="12:00:00Z")
    graph.set((EX.object, S.hasCurrentStatus, EX.c))
    assert_valid(graph)


@pytest.mark.parametrize("owner", [EX.object, BNode("owner")])
def test_other_objects_and_status_kinds_do_not_compete(owner):
    graph = Graph()
    add_status(graph, EX.transport, owner=owner)
    add_status(graph, EX.inspection, owner=owner, time="12:00:00Z", kind=K.TemperatureInspection, value=V.Failed)
    add_status(graph, EX.other_transport, owner=EX.other_object, time="13:00:00Z")
    graph.add((owner, S.hasCurrentStatus, EX.transport))
    graph.add((owner, S.hasCurrentStatus, EX.inspection))
    graph.add((EX.other_object, S.hasCurrentStatus, EX.other_transport))
    assert_valid(graph)


def test_validation_rejects_a_stale_pointer_without_rewriting_it():
    graph = Graph()
    add_status(graph, EX.a)
    graph.set((EX.object, S.hasCurrentStatus, EX.a))
    assert_valid(graph)
    add_status(graph, EX.b, time="12:00:00Z")
    before = set(graph)
    assert_invalid(graph, "STATUS-064")
    assert set(graph) == before
    graph.remove((EX.object, S.hasCurrentStatus, None))
    assert_valid(graph)
