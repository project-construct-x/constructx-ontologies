import re
import shutil
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup
from pyshacl import validate
from rdflib import Graph
from rdflib.compare import isomorphic
import yaml

from scripts.build import build_repository
from scripts.generate_docs import ontology_html_output_path, render_module_overview
from scripts.validate import validate_repository
from scripts.validate_status import load_status_data, load_status_shapes

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules/core/status"


def test_status_documentation_links_resolve() -> None:
    paths = [MODULE / "README.md", *sorted((MODULE / "docs").glob("*.md"))]
    paths.extend((MODULE / "examples").rglob("*.md"))
    paths.extend(ROOT / f"datasets/reference/vocabularies/{name}/README.md"
                 for name in ("status-kind", "status-value", "status-reason"))
    for path in paths:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            assert (path.parent / relative).exists(), (path, target)


def test_generated_status_html_contains_terms_and_valid_anchors() -> None:
    metadata = yaml.safe_load((MODULE / "module.yaml").read_text(encoding="utf-8"))
    html_path = ontology_html_output_path(MODULE / "module.yaml", metadata)
    assert html_path == MODULE / "docs/status.html"
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    assert soup.title and "Construct-X Status Ontology" in soup.title.get_text()
    for term in ("StatusAssignment", "StatusKind", "StatusValue", "StatusReason",
                 "hasAllowedStatusValue", "hasAllowedStatusReason", "referenceTime",
                 "hasCondition", "previousStatus", "reportedBy"):
        assert soup.find(id=term) is not None, term
    ids = [node["id"] for node in soup.find_all(id=True)]
    assert len(ids) == len(set(ids))
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.startswith("#") and len(href) > 1:
            assert unquote(href[1:]) in ids, href
    assert "modules/core/status/docs/status.html" in render_module_overview(ROOT)


def test_core_only_status_build_includes_dependencies_and_vocabularies(tmp_path: Path) -> None:
    packages = (
        "modules/core/status", "modules/core/agent", "modules/core/vso",
        "profiles/construct-x/vso-isoprops",
        "datasets/reference/vocabularies/status-kind",
        "datasets/reference/vocabularies/status-value",
        "datasets/reference/vocabularies/status-reason",
    )
    for relative in packages:
        shutil.copytree(ROOT / relative, tmp_path / relative)
    validation = validate_repository(tmp_path)
    assert validation.ok, validation.errors
    manifest = build_repository(tmp_path)
    assert all(not item["skipped"] for key in ("modules", "datasets", "profiles")
               for item in manifest[key])
    assert {m["id"] for m in manifest["modules"]} == {"status", "agent", "vso"}
    assert {d["id"] for d in manifest["datasets"]} == {"status-kind", "status-value", "status-reason"}
    included = [file for key in ("modules", "datasets", "profiles")
                for item in manifest[key] for file in item["included_files"]]
    for name in ("conx-status.ttl", "conx-status-core.shacl.ttl", "conx-vso-core.shacl.ttl",
                 "conx-vso-isoprops.shacl.ttl", "status-kind.ttl", "status-value.ttl", "status-reason.ttl"):
        assert any(Path(path).name == name for path in included), name
    assert not any("/domain/" in path for path in included)
    status = next(m for m in manifest["modules"] if m["id"] == "status")
    bundle = tmp_path / status["validation_bundle"]
    assert {p.name for p in bundle.iterdir()} == {
        "shapes.ttl", "ontology.ttl", "vocabularies.ttl", "validate.py", "bundle.json", "README.md"
    }
    published = tmp_path / "dist/modules/core/status/shapes/conx-status-core.shacl.ttl"
    shapes = Graph().parse(published)
    assert isomorphic(shapes, load_status_shapes(tmp_path))
    # Exercise the actual published graph with a generic SHACL processor.
    # No Status loader or source dependency graph participates in validation.
    for fixture, expected in (
        ("examples/minimal-status.ttl", True),
        ("tests/valid/recorded-at-without-offset.ttl", True),
        ("tests/valid/recorded-at-midnight.ttl", True),
        ("tests/valid/recorded-at-midnight-without-offset.ttl", True),
        ("tests/invalid/recorded-at-midnight-invalid-date.ttl", False),
        ("tests/invalid/recorded-at-midnight-nonzero-fraction.ttl", False),
        ("tests/invalid/recorded-at-midnight-invalid-offset.ttl", False),
        ("tests/invalid/recorded-at-space-separator.ttl", False),
        ("tests/invalid/recorded-at-invalid-offset.ttl", False),
        ("examples/status-with-condition.ttl", True),
        ("tests/invalid/condition-missing-unit.ttl", False),
        ("tests/invalid/condition-malformed-literal.ttl", False),
        ("tests/invalid/previous-skips-equal-time.ttl", False),
        ("tests/invalid/current-outdated.ttl", False),
        ("tests/invalid/current-equal-time-predecessor.ttl", False),
        ("tests/invalid/current-ambiguous.ttl", False),
        ("tests/valid/current-equal-time-successor.ttl", True),
        ("tests/valid/current-omitted-ambiguous.ttl", True),
    ):
        data = load_status_data(MODULE / fixture)
        data.parse(bundle / "vocabularies.ttl")
        conforms, _, report = validate(
            data, shacl_graph=shapes, ont_graph=Graph().parse(bundle / "ontology.ttl"),
            inference="none", advanced=True,
        )
        assert conforms == expected, report
