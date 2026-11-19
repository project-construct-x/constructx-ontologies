import shutil
import subprocess
import sys

import pytest
from rdflib import Graph

from scripts.status_bundle import build_status_bundle
from scripts.validate_status import ROOT, StatusDependencyError, load_status_data, validate_status

MODULE = ROOT / "modules/core/status"


@pytest.fixture(scope="module")
def exported_bundle(tmp_path_factory):
    directory = tmp_path_factory.mktemp("status-export")
    build_status_bundle(ROOT, directory)
    return directory


@pytest.mark.parametrize("fixture,expected,message", [
    ("examples/minimal-status.ttl", 0, "Conforms: True"),
    ("tests/valid/recorded-at-without-offset.ttl", 0, "Conforms: True"),
    ("tests/valid/recorded-at-midnight.ttl", 0, "Conforms: True"),
    ("tests/valid/recorded-at-midnight-without-offset.ttl", 0, "Conforms: True"),
    ("tests/invalid/recorded-at-midnight-invalid-date.ttl", 1, "STATUS-032"),
    ("tests/invalid/recorded-at-midnight-nonzero-fraction.ttl", 1, "STATUS-032"),
    ("tests/invalid/recorded-at-midnight-invalid-offset.ttl", 1, "STATUS-032"),
    ("tests/invalid/recorded-at-space-separator.ttl", 1, "STATUS-032"),
    ("tests/invalid/recorded-at-invalid-offset.ttl", 1, "STATUS-032"),
    ("examples/status-with-condition.ttl", 0, "Conforms: True"),
    ("tests/invalid/condition-missing-unit.ttl", 1, "ISOP-ASSIGN-UNIT-001"),
    ("tests/invalid/condition-malformed-literal.ttl", 1, "ISOP-VALUE-002"),
    ("tests/invalid/previous-skips-equal-time.ttl", 1, "STATUS-054"),
    ("tests/invalid/excessive-time-precision.ttl", 1, "STATUS-031"),
    ("tests/invalid/date-with-offset.ttl", 1, "STATUS-030"),
    ("tests/invalid/current-outdated.ttl", 1, "STATUS-064"),
    ("tests/invalid/current-equal-time-predecessor.ttl", 1, "STATUS-064"),
    ("tests/invalid/current-ambiguous.ttl", 1, "STATUS-065"),
    ("tests/valid/current-equal-time-successor.ttl", 0, "Conforms: True"),
    ("tests/valid/current-omitted-ambiguous.ttl", 0, "Conforms: True"),
])
def test_relocated_bundle_runs_without_source_checkout(exported_bundle, tmp_path, fixture, expected, message):
    standalone = tmp_path / "package"
    shutil.copytree(exported_bundle, standalone)
    data = tmp_path / "data.ttl"
    shutil.copy2(MODULE / fixture, data)
    result = subprocess.run(
        [sys.executable, "-B", str(standalone / "validate.py"), "--data", str(data)],
        cwd=tmp_path, capture_output=True, text=True, encoding="utf-8",
    )
    assert result.returncode == expected, result.stdout + result.stderr
    assert message in result.stdout
    assert "Failed to convert Literal" not in result.stderr
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize("mutation", ["missing", "altered"])
def test_incomplete_bundle_is_a_setup_error(exported_bundle, tmp_path, mutation):
    standalone = tmp_path / "package"
    shutil.copytree(exported_bundle, standalone)
    shapes = standalone / "shapes.ttl"
    if mutation == "missing":
        shapes.unlink()
    else:
        shapes.write_text("# missing dependency constraints\n", encoding="utf-8")
    with pytest.raises(StatusDependencyError):
        validate_status(Graph(), bundle=standalone)
    result = subprocess.run(
        [sys.executable, "-B", str(standalone / "validate.py"), "--data",
         str(MODULE / "examples/minimal-status.ttl")],
        cwd=tmp_path, capture_output=True, text=True, encoding="utf-8",
    )
    assert result.returncode == 2
    assert "setup error" in result.stderr


def test_export_does_not_apply_isoprops_to_unrelated_vso(exported_bundle):
    data = load_status_data(MODULE / "examples/status-with-condition.ttl")
    data.parse(data='''
      @prefix v: <https://www.construct-x.org/ontology/vso#> .
      @prefix schema: <https://schema.org/> .
      <urn:object> v:hasProperty <urn:assignment> .
      <urn:assignment> a v:AssignedProperty ; v:hasPropertyReference <urn:definition> ;
        v:hasPropertyState <urn:state> .
      <urn:state> a v:PropertyState ; schema:value "Generic VSO value" .
    ''', format="turtle")
    conforms, _, report = validate_status(data, bundle=exported_bundle)
    assert conforms, report


def test_missing_export_dependency_fails_before_writing(tmp_path):
    output = tmp_path / "output"
    with pytest.raises(StatusDependencyError):
        build_status_bundle(tmp_path, output)
    assert not output.exists()
