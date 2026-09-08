from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_repository_contains_only_core_ontology_modules() -> None:
    module_root = ROOT / "modules"

    assert {path.name for path in module_root.iterdir() if path.is_dir()} == {"core"}
    assert not (ROOT / "profiles").exists()

    for metadata_file in (module_root / "core").glob("*/module.yaml"):
        metadata = yaml.safe_load(metadata_file.read_text(encoding="utf-8"))
        assert metadata["type"] == "core"


def test_optional_nuts_dataset_is_not_part_of_core_release() -> None:
    assert not (
        ROOT / "datasets/reference/administrative-territories/nuts-2"
    ).exists()


def test_dependency_registry_contains_no_excluded_repository_paths() -> None:
    lock_file = ROOT / "network/imports.lock.yaml"
    dependencies = yaml.safe_load(lock_file.read_text(encoding="utf-8"))["dependencies"]
    excluded_prefixes = ("modules/domain", "modules/alignments", "profiles/")

    for dependency in dependencies.values():
        assert all(
            not path.startswith(excluded_prefixes)
            for path in dependency.get("used_by", [])
        )
