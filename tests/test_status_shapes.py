from pathlib import Path
import re
import subprocess
import sys

import pytest
from pyshacl import validate
from rdflib import Graph, Namespace, RDF, URIRef
from scripts.validate_status import ROOT, load_status_data, load_status_shapes, validate_status

MODULE = ROOT / "modules/core/status"
SH = Namespace("http://www.w3.org/ns/shacl#")
S = Namespace("https://www.construct-x.org/ontology/status#")

INVALID_CASES = {
    "current-outdated.ttl": ["STATUS-064"],
    "current-equal-time-predecessor.ttl": ["STATUS-064"],
    "current-ambiguous.ttl": ["STATUS-065"],
    "condition-malformed-literal.ttl": ["ISOP-VALUE-002"],
    "previous-skips-equal-time.ttl": ["STATUS-054"],
    "excessive-time-precision.ttl": ["STATUS-031"],
    "missing-required-values.ttl": [
        "STATUS-020",
        "STATUS-021",
        "STATUS-030",
        "STATUS-031"
    ],
    "multiple-required-values.ttl": [
        "STATUS-020",
        "STATUS-021",
        "STATUS-030",
        "STATUS-031"
    ],
    "missing-owner.ttl": [
        "STATUS-010"
    ],
    "multiple-owners.ttl": [
        "STATUS-010"
    ],
    "untyped-status.ttl": [
        "STATUS-001"
    ],
    "blank-status.ttl": [
        "STATUS-001"
    ],
    "missing-offset.ttl": [
        "STATUS-031"
    ],
    "invalid-date.ttl": [
        "STATUS-030"
    ],
    "invalid-offset.ttl": [
        "STATUS-031"
    ],
    "date-with-offset.ttl": [
        "STATUS-030"
    ],
    "disallowed-value.ttl": [
        "STATUS-022"
    ],
    "unknown-kind.ttl": [
        "STATUS-020"
    ],
    "invalid-reason.ttl": [
        "STATUS-023"
    ],
    "invalid-text.ttl": [
        "STATUS-033",
        "STATUS-034"
    ],
    "invalid-reporter.ttl": [
        "STATUS-040"
    ],
    "invalid-recorded-at.ttl": [
        "STATUS-032"
    ],
    "recorded-at-space-separator.ttl": ["STATUS-032"],
    "recorded-at-invalid-offset.ttl": ["STATUS-032"],
    "recorded-at-midnight-invalid-date.ttl": ["STATUS-032"],
    "recorded-at-midnight-nonzero-fraction.ttl": ["STATUS-032"],
    "recorded-at-midnight-invalid-offset.ttl": ["STATUS-032"],
    "current-not-in-history.ttl": [
        "STATUS-062"
    ],
    "two-current-statuses.ttl": [
        "STATUS-063"
    ],
    "previous-wrong-owner.ttl": [
        "STATUS-051"
    ],
    "previous-wrong-kind.ttl": [
        "STATUS-051"
    ],
    "self-cycle.ttl": [
        "STATUS-052"
    ],
    "history-cycle.ttl": [
        "STATUS-052"
    ],
    "previous-in-future.ttl": [
        "STATUS-053"
    ],
    "previous-skips-status.ttl": [
        "STATUS-054"
    ],
    "multiple-previous.ttl": [
        "STATUS-050"
    ],
    "condition-missing-unit.ttl": [
        "ISOP-ASSIGN-UNIT-001"
    ],
    "condition-disallowed-unit.ttl": [
        "ISOP-ASSIGN-UNIT-002"
    ],
    "condition-wrong-datatype.ttl": [
        "ISOP-VALUE-001"
    ],
    "condition-multiple-values.ttl": [
        "VSO-STATE-010"
    ],
    "condition-missing-owner.ttl": [
        "VSO-ASSIGN-001"
    ],
    "condition-multiple-owners.ttl": [
        "VSO-ASSIGN-001"
    ],
    "condition-invalid-definition.ttl": [
        "ISOP-REVISION-001"
    ]
}


def error_ids(report: Graph) -> set[str]:
    return {
        match
        for message in report.objects(None, SH.resultMessage)
        for match in re.findall(r"\[([A-Z0-9-]+)\]", str(message))
    }


@pytest.mark.parametrize("path", sorted((MODULE / "tests/valid").glob("*.ttl")), ids=lambda p: p.name)
def test_valid_status_fixtures(path: Path) -> None:
    conforms, _, report = validate_status(load_status_data(path))
    assert conforms, report


@pytest.mark.parametrize("path", sorted((MODULE / "examples").glob("*.ttl")), ids=lambda p: p.name)
def test_public_examples(path: Path) -> None:
    conforms, _, report = validate_status(load_status_data(path))
    assert conforms, report


@pytest.mark.parametrize(("name", "expected"), INVALID_CASES.items())
def test_invalid_status_fixtures(name: str, expected: list[str]) -> None:
    conforms, report_graph, report = validate_status(
        load_status_data(MODULE / "tests/invalid" / name)
    )
    assert not conforms, report
    assert set(expected) <= error_ids(report_graph), report


def test_complete_shape_bundle_is_valid_shacl() -> None:
    conforms, _, report = validate(
        Graph(), shacl_graph=load_status_shapes(), meta_shacl=True, advanced=True
    )
    assert conforms, report


def test_every_new_named_constraint_has_bilingual_diagnostics() -> None:
    graph = Graph().parse(MODULE / "shapes/conx-status-core.shacl.ttl")
    for shape_type in (SH.PropertyShape, SH.SPARQLConstraint):
        for shape in graph.subjects(RDF.type, shape_type):
            assert {m.language for m in graph.objects(shape, SH.message)} == {"en", "de"}
            assert all(re.search(r"\[STATUS-[A-Z0-9-]+\]", str(m)) for m in graph.objects(shape, SH.message))


def test_references_cannot_bypass_assignment_validation() -> None:
    data = Graph().parse(data="""
      @prefix s: <https://www.construct-x.org/ontology/status#> .
      <https://example.org/resource> s:hasCurrentStatus <https://example.org/missing> .
    """, format="turtle")
    conforms, report, _ = validate_status(data)
    assert not conforms
    assert {"STATUS-001", "STATUS-010", "STATUS-020", "STATUS-030", "STATUS-062"} <= error_ids(report)


def test_validation_does_not_mutate_input() -> None:
    data = Graph().parse(MODULE / "examples/minimal-status.ttl")
    original = set(data)
    assert validate_status(data)[0]
    assert set(data) == original


def test_fractional_seconds_and_maximum_offset_are_supported() -> None:
    from rdflib import Literal, XSD
    data = Graph().parse(MODULE / "examples/minimal-status.ttl")
    assignment = next(data.subjects(RDF.type, S.StatusAssignment))
    data.set((assignment, S.referenceTime, Literal("10:00:00.125+14:00", datatype=XSD.time)))
    conforms, _, report = validate_status(data)
    assert conforms, report


def test_cli_validates_public_example_offline() -> None:
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/validate_status.py"),
         "--data", str(MODULE / "examples/status-with-condition.ttl")],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Conforms: True" in result.stdout
