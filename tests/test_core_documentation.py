from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_ROOT = ROOT / "modules" / "core"
CORE_MODULES = sorted(path for path in CORE_ROOT.iterdir() if path.is_dir())

REQUIRED_FILES = (
    "README.md",
    "CHANGELOG.md",
    "docs/index.md",
    "docs/confluence-overview.md",
    "docs/scope-and-competency-questions.md",
    "docs/source-analysis.md",
    "docs/concept-model.md",
    "docs/module-boundaries.md",
    "docs/term-catalog.md",
    "docs/shacl-requirements.md",
    "docs/core-shapes.md",
    "docs/diagrams/concept-model.md",
)
DETAIL_DOCUMENTS = REQUIRED_FILES[3:]
METADATA_FIELDS = ("Status", "Version", "Stand", "Geltungsbereich")
README_HEADINGS = (
    "## 1. Kurzbeschreibung",
    "## 2. Verständliches Beispiel",
    "## 3. Modellumfang",
    "## 4. Dokumentation",
    "## 5. Technische Artefakte",
)
INDEX_HEADINGS = (
    "## 1. Überblick",
    "## 2. Einstieg für nichttechnische Leser",
    "## 3. Dokumentationspaket",
    "## 4. Technische Artefakte",
    "## 5. Beispiele und Tests",
    "## 6. Ergänzende Dokumente",
)
CONFLUENCE_HEADINGS = (
    "## 1. Zweck",
    "## 2. Alltagsnahes Beispiel",
    "## 3. Umfang und Abgrenzung",
    "## 4. Modellübersicht",
    "## 5. Zentrale Klassen und Beziehungen",
    "## 6. Validierung in verständlicher Sprache",
    "## 7. Abhängigkeiten",
    "## 8. Version, Status und Artefakte",
    "## 9. Weiterführende Dokumentation",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_module_metadata(module_dir: Path) -> dict:
    return yaml.safe_load(read_text(module_dir / "module.yaml"))


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_core_module_has_complete_documentation_package(module_dir: Path) -> None:
    missing = [relative for relative in REQUIRED_FILES if not (module_dir / relative).is_file()]
    assert not missing, f"Missing documentation files: {missing}"


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_core_module_registers_documentation_artifacts(module_dir: Path) -> None:
    metadata = read_module_metadata(module_dir)
    artifacts = metadata["artifacts"]
    registered = {value for value in artifacts.values() if isinstance(value, str)}

    assert not set(REQUIRED_FILES) - registered
    assert artifacts.get("confluence_overview") == "docs/confluence-overview.md"
    html_documentation = artifacts.get("html_documentation")
    assert isinstance(html_documentation, str)
    assert (module_dir / html_documentation).is_file()


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_core_readme_uses_standard_chapters(module_dir: Path) -> None:
    text = read_text(module_dir / "README.md")
    headings = tuple(line for line in text.splitlines() if line.startswith("## "))
    assert headings == README_HEADINGS
    assert "Dokumentationsstandard" in text


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_core_index_uses_standard_chapters(module_dir: Path) -> None:
    text = read_text(module_dir / "docs" / "index.md")
    headings = tuple(line for line in text.splitlines() if line.startswith("## "))
    assert headings == INDEX_HEADINGS
    assert "[Confluence-Kurzfassung](confluence-overview.md)" in text


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_core_confluence_overview_uses_publication_structure(module_dir: Path) -> None:
    text = read_text(module_dir / "docs" / "confluence-overview.md")
    headings = tuple(line for line in text.splitlines() if line.startswith("## "))

    assert headings == CONFLUENCE_HEADINGS
    assert "Veröffentlichungsquelle für die kompakte Modulseite" in text
    assert re.search(
        r"führt\s+keine neuen fachlichen oder technischen Regeln ein", text
    )
    assert "[Konzeptmodell](concept-model.md)" in text
    assert "[Core-Shape-Referenz](core-shapes.md)" in text or (
        "[Erläuterung zu Core Shapes](core-shapes.md)" in text
    )


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
@pytest.mark.parametrize("relative_path", DETAIL_DOCUMENTS)
def test_core_detail_document_has_metadata_numbering_and_example(
    module_dir: Path, relative_path: str
) -> None:
    text = read_text(module_dir / relative_path)

    for field in METADATA_FIELDS:
        assert re.search(rf"^\*\*{field}(?: der Recherche)?:\*\*", text, re.MULTILINE)

    headings = [line for line in text.splitlines() if line.startswith("## ")]
    assert headings
    assert all(re.match(r"^## \d+\. ", heading) for heading in headings)
    numbers = [int(re.match(r"^## (\d+)\.", heading).group(1)) for heading in headings]
    assert numbers == list(range(1, len(numbers) + 1))
    assert any(re.search(r"beispiel|szenari", heading, re.IGNORECASE) for heading in headings)
