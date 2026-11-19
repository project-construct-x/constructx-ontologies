from pathlib import Path

import yaml

from documentation_checks import broken_local_links


ROOT = Path(__file__).resolve().parents[1]


def test_repository_contains_only_core_ontology_modules() -> None:
    module_root = ROOT / "modules"

    assert {path.name for path in module_root.iterdir() if path.is_dir()} == {"core"}
    assert {
        path.parent.relative_to(ROOT).as_posix()
        for path in (ROOT / "profiles").rglob("profile.yaml")
    } == {"profiles/construct-x/vso-isoprops"}

    for metadata_file in (module_root / "core").glob("*/module.yaml"):
        metadata = yaml.safe_load(metadata_file.read_text(encoding="utf-8"))
        assert metadata["type"] == "core"


def test_domain_reference_vocabularies_are_not_part_of_core_distribution() -> None:
    dataset_ids = {
        yaml.safe_load(path.read_text(encoding="utf-8-sig"))["id"]
        for path in (ROOT / "datasets").rglob("dataset.yaml")
    }
    assert not {"delivery-role", "delivery-feature"} & dataset_ids
    assert {"status-kind", "status-value", "status-reason", "nuts-2"} <= dataset_ids


def test_dependency_registry_contains_no_excluded_repository_paths() -> None:
    lock_file = ROOT / "network/imports.lock.yaml"
    dependencies = yaml.safe_load(lock_file.read_text(encoding="utf-8"))["dependencies"]
    excluded_prefixes = ("modules/domain", "modules/alignments")

    for dependency in dependencies.values():
        assert all(
            not path.startswith(excluded_prefixes)
            for path in dependency.get("used_by", [])
        )
        assert all((ROOT / path).exists() for path in dependency.get("used_by", []))
        if dependency.get("resolution"):
            assert (ROOT / dependency["resolution"]).is_file()


def test_repository_and_supporting_documentation_links_resolve() -> None:
    files = set(ROOT.glob("*.md"))
    for directory in ("docs", "datasets", "network", "profiles"):
        files.update((ROOT / directory).rglob("*.md"))
    assert not broken_local_links(files)
