from pathlib import Path

import pytest

from documentation_checks import (
    broken_local_links,
    documentation_files,
    module_artifacts,
)


ROOT = Path(__file__).resolve().parents[1]
CORE_MODULES = sorted(path.parent for path in (ROOT / "modules/core").glob("*/module.yaml"))


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_registered_documentation_exists(module_dir: Path) -> None:
    index = module_artifacts(module_dir).get("documentation")
    assert isinstance(index, str) and index
    assert (module_dir / index).is_file()
    for path in documentation_files(module_dir):
        assert path.is_file(), path
        assert path.stat().st_size, f"Empty documentation file: {path}"


@pytest.mark.parametrize("module_dir", CORE_MODULES, ids=lambda path: path.name)
def test_documentation_links_resolve(module_dir: Path) -> None:
    assert not (errors := broken_local_links(sorted(module_dir.rglob("*.md")))), errors
