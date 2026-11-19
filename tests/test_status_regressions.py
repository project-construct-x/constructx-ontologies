"""Behavioral regressions found in the Status Core review."""
import pytest
from rdflib import Literal, Namespace, URIRef, XSD

from scripts.validate_status import ROOT, load_status_data, validate_status

MODULE = ROOT / "modules/core/status"
S = Namespace("https://www.construct-x.org/ontology/status#")
EX = Namespace("https://example.org/status/")
ISO = Namespace("https://w3id.org/isoprops#")
SCHEMA = Namespace("https://schema.org/")
DEFINITION = URIRef("https://properties.example.org/temperature/revision/1")


@pytest.mark.parametrize("declared,datatype,lexical,expected", [
    ("REAL", XSD.decimal, "warm", False),
    ("REAL", XSD.decimal, "1e2", False),
    ("REAL", XSD.decimal, "NaN", False),
    ("REAL", XSD.double, "warm", False),
    ("REAL", XSD.float, "warm", False),
    ("INTEGER", XSD.integer, "1.5", False),
    ("INTEGER", XSD.integer, "1_000", False),
    ("INTEGER", XSD.byte, "128", False),
    ("INTEGER", XSD.unsignedByte, "-1", False),
    ("INTEGER", XSD.positiveInteger, "0", False),
    ("BOOLEAN", XSD.boolean, "yes", False),
    ("DATETIME", XSD.dateTime, "2026-02-30T10:00:00Z", False),
    ("DATETIME", XSD.dateTime, "2026-11-11 10:00:00Z", False),
    ("DATETIME", XSD.dateTime, "2026-11-11T10:00:00+14:01", False),
    ("COMPLEX", XSD.decimal, "warm", False),
    ("REAL", XSD.decimal, "8.0", True),
    ("REAL", XSD.decimal, "+.5", True),
    ("REAL", XSD.double, "1.2e3", True),
    ("REAL", XSD.float, "1.2E-3", True),
    ("INTEGER", XSD.byte, "127", True),
    ("INTEGER", XSD.byte, "-128", True),
    ("INTEGER", XSD.unsignedLong, "18446744073709551615", True),
    ("BOOLEAN", XSD.boolean, "1", True),
    ("BOOLEAN", XSD.boolean, "false", True),
    ("DATETIME", XSD.dateTime, "2026-11-11T10:00:00Z", True),
    ("DATETIME", XSD.dateTime, "2026-11-11T10:00:00", True),
    ("COMPLEX", URIRef("https://example.org/complex-number"), "3+4i", True),
])
def test_condition_checks_literal_content_and_preserves_valid_types(
    declared, datatype, lexical, expected
) -> None:
    graph = load_status_data(MODULE / "examples/status-with-condition.ttl")
    graph.set((DEFINITION, ISO.dataType, Literal(declared)))
    graph.set((EX.measuredState, SCHEMA.value, Literal(lexical, datatype=datatype, normalize=False)))
    conforms, _, report = validate_status(graph)
    assert conforms == expected, report
    if not expected:
        assert "ISOP-VALUE-002" in report


@pytest.mark.parametrize("same_instant", ["08:00:00+01:00", "07:00:00Z"])
def test_explicit_equal_time_order_must_not_be_skipped(same_instant) -> None:
    graph = load_status_data(MODULE / "examples/status-history.ttl")
    graph.set((EX.s2, S.referenceTime, Literal(same_instant, datatype=XSD.time, normalize=False)))
    graph.set((EX.s3, S.previousStatus, EX.s1))
    conforms, _, report = validate_status(graph)
    assert not conforms and "STATUS-054" in report
    graph.set((EX.s3, S.previousStatus, EX.s2))
    conforms, _, report = validate_status(graph)
    assert conforms, report


def test_tied_observations_without_an_explicit_order_remain_valid() -> None:
    graph = load_status_data(MODULE / "examples/status-history.ttl")
    graph.set((EX.s2, S.referenceTime, Literal("08:00:00+01:00", datatype=XSD.time)))
    graph.remove((EX.s2, S.previousStatus, None))
    graph.set((EX.s3, S.previousStatus, EX.s1))
    assert validate_status(graph)[0]


def test_microsecond_order_is_preserved_and_submicroseconds_are_rejected() -> None:
    graph = load_status_data(MODULE / "examples/status-history.ttl")
    graph.set((EX.s1, S.referenceTime, Literal("08:00:00.000002Z", datatype=XSD.time, normalize=False)))
    graph.set((EX.s2, S.referenceTime, Literal("08:00:00.000001Z", datatype=XSD.time, normalize=False)))
    conforms, _, report = validate_status(graph)
    assert not conforms and "STATUS-053" in report
    graph.set((EX.s2, S.referenceTime, Literal("08:00:00.000003Z", datatype=XSD.time, normalize=False)))
    assert validate_status(graph)[0]
    graph.set((EX.s1, S.referenceTime, Literal("08:00:00.0000002Z", datatype=XSD.time, normalize=False)))
    conforms, _, report = validate_status(graph)
    assert not conforms and "STATUS-031" in report
