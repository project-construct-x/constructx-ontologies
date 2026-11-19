"""Recording time is optional, but supplied dateTime literals must be valid."""
import subprocess
import sys

import pytest
from rdflib import Literal, Namespace, URIRef, XSD

from scripts.validate_status import ROOT, load_status_data, validate_status

MODULE = ROOT / "modules/core/status"
S = Namespace("https://www.construct-x.org/ontology/status#")


@pytest.mark.parametrize("lexical", [
    None,
    "2026-11-11T10:00:00",
    "2026-11-11T10:00:00Z",
    "2026-11-11T10:00:00+01:00",
    "2026-11-11T10:00:00-05:30",
    "2026-11-11T10:00:00+14:00",
    "2026-11-11T10:00:00-14:00",
    "2024-02-29T10:00:00Z",
    # recordedAt does not participate in ordering or inherit the six-digit limit.
    "2026-11-11T10:00:00.1234567Z",
])
def test_recorded_at_accepts_absence_and_valid_optional_offsets(lexical):
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    assert not list(data.objects(statement, S.recordedAt))
    if lexical is not None:
        data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
    before = set(data)
    conforms, _, report = validate_status(data)
    assert conforms, report
    assert set(data) == before


@pytest.mark.parametrize("lexical", [
    "2026-11-11 10:00:00Z",
    "2026-11-11t10:00:00Z",
    "2026-11-11",
    "20261111T100000Z",
    "2026-11-11T10:00Z",
    "2026-11-11T10:00:00,5Z",
    "2026-11-11T10:00:00+15:00",
    "2026-11-11T10:00:00-15:00",
    "2026-11-11T10:00:00+14:01",
    "2026-11-11T10:00:00-14:01",
    "2026-11-11T10:00:00+01:60",
    "2026-11-11T10:00:00+0100",
    "2026-11-11T10:00:00Zjunk",
    "2026-02-29T10:00:00Z",
    "2026-11-11T24:01:00Z",
    "2026-11-11T10:60:00Z",
    "2026-11-11T10:00:60Z",
])
def test_recorded_at_rejects_malformed_typed_literals(lexical):
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
    conforms, _, report = validate_status(data)
    assert not conforms and "STATUS-032" in report, report


def test_recorded_at_still_allows_at_most_one_timestamp():
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    for lexical in ("2026-11-11T10:00:00Z", "2026-11-11T11:00:00Z"):
        data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
    conforms, _, report = validate_status(data)
    assert not conforms and "STATUS-032" in report, report


@pytest.mark.parametrize("end_of_day,next_midnight", [
    ("2026-11-11T24:00:00", "2026-11-12T00:00:00"),
    ("2026-11-11T24:00:00Z", "2026-11-12T00:00:00Z"),
    ("2026-11-11T24:00:00+01:00", "2026-11-12T00:00:00+01:00"),
    ("2026-11-11T24:00:00-05:30", "2026-11-12T00:00:00-05:30"),
    ("2026-11-11T24:00:00+14:00", "2026-11-12T00:00:00+14:00"),
    ("2026-11-11T24:00:00-14:00", "2026-11-12T00:00:00-14:00"),
    ("2026-11-30T24:00:00Z", "2026-12-01T00:00:00Z"),
    ("2026-12-31T24:00:00Z", "2027-01-01T00:00:00Z"),
    ("2024-02-28T24:00:00Z", "2024-02-29T00:00:00Z"),
    ("2024-02-29T24:00:00Z", "2024-03-01T00:00:00Z"),
    ("2026-02-28T24:00:00Z", "2026-03-01T00:00:00Z"),
    ("2000-02-29T24:00:00Z", "2000-03-01T00:00:00Z"),
    ("2026-11-11T24:00:00.0Z", "2026-11-12T00:00:00Z"),
    ("2026-11-11T24:00:00.000000000+01:00", "2026-11-12T00:00:00+01:00"),
])
def test_recorded_at_accepts_both_midnight_spellings_without_rewriting(end_of_day, next_midnight):
    for lexical in (end_of_day, next_midnight):
        data = load_status_data(MODULE / "examples/minimal-status.ttl")
        statement = next(data.subjects(S.referenceDate, None))
        data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
        before = set(data)
        conforms, _, report = validate_status(data)
        assert conforms, report
        assert set(data) == before
        assert str(next(data.objects(statement, S.recordedAt))) == lexical


@pytest.mark.parametrize("lexical", [
    "2026-11-11T24:01:00Z",
    "2026-11-11T24:00:01Z",
    "2026-11-11T24:00:00.1Z",
    "2026-11-11T24:00:00.000000001Z",
    "2026-11-11T24:00:00+15:00",
    "2026-11-11T24:00:00-14:01",
    "2026-11-11T24:00:00+01:60",
    "2026-02-29T24:00:00Z",
    "1900-02-29T24:00:00Z",
    "2100-02-29T24:00:00Z",
    "2026-04-31T24:00:00Z",
    "2026-13-01T24:00:00Z",
    "2026-11-11 24:00:00Z",
])
def test_recorded_at_midnight_does_not_bypass_calendar_clock_or_offset_checks(lexical):
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
    conforms, _, report = validate_status(data)
    assert not conforms and "STATUS-032" in report, report


@pytest.mark.parametrize("value", [
    Literal("2026-11-11T24:00:00Z"),
    Literal("2026-11-11T24:00:00Z", lang="en"),
    Literal("2026-11-11T24:00:00Z", datatype=XSD.date, normalize=False),
    URIRef("https://example.org/2026-11-11T24:00:00Z"),
])
def test_recorded_at_midnight_still_requires_a_datetime_literal(value):
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    data.add((statement, S.recordedAt, value))
    conforms, _, report = validate_status(data)
    assert not conforms and "STATUS-032" in report, report


def test_equivalent_midnight_spellings_do_not_collapse_the_maximum_count():
    data = load_status_data(MODULE / "examples/minimal-status.ttl")
    statement = next(data.subjects(S.referenceDate, None))
    for lexical in ("2026-11-11T24:00:00Z", "2026-11-12T00:00:00Z"):
        data.add((statement, S.recordedAt, Literal(lexical, datatype=XSD.dateTime, normalize=False)))
    conforms, report_graph, report = validate_status(data)
    assert not conforms and "STATUS-032" in report, report
    sh = Namespace("http://www.w3.org/ns/shacl#")
    assert sh.MaxCountConstraintComponent in set(report_graph.objects(None, sh.sourceConstraintComponent))


@pytest.mark.parametrize("fixture,expected", [
    ("valid/recorded-at-midnight.ttl", 0),
    ("valid/recorded-at-midnight-without-offset.ttl", 0),
    ("invalid/recorded-at-midnight-invalid-date.ttl", 1),
    ("invalid/recorded-at-midnight-nonzero-fraction.ttl", 1),
    ("invalid/recorded-at-midnight-invalid-offset.ttl", 1),
])
def test_midnight_cli_uses_shacl_diagnostics_without_conversion_tracebacks(fixture, expected, tmp_path):
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/validate_status.py"),
         "--data", str(MODULE / "tests" / fixture)],
        cwd=tmp_path, capture_output=True, text=True, encoding="utf-8",
    )
    assert result.returncode == expected, result.stdout + result.stderr
    assert ("Conforms: True" if expected == 0 else "STATUS-032") in result.stdout
    assert "Failed to convert Literal" not in result.stderr
    assert "Traceback" not in result.stderr
