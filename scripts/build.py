from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


IGNORED_DIRS = {".git", ".venv", ".uv-cache", "dist", "build", "__pycache__", ".pytest_cache"}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def is_ignored(path: Path, root: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.relative_to(root).parts)


def iter_module_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("module.yaml") if not is_ignored(path, root))


def iter_dataset_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("dataset.yaml") if not is_ignored(path, root))


def iter_profile_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("profile.yaml") if not is_ignored(path, root))


def read_yaml_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping.")
    return data


def build_repository(root: Path) -> dict[str, Any]:
    dist_dir = root / "dist"
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()

    manifest: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "modules": [],
        "datasets": [],
        "profiles": [],
    }

    for module_file in iter_module_files(root):
        metadata = read_yaml_file(module_file)
        module_id = metadata.get("id")
        artifacts = metadata.get("artifacts", {})
        ontology_artifact = artifacts.get("ontology")
        module_dir = module_file.parent

        module_entry: dict[str, Any] = {
            "id": module_id,
            "module_path": module_dir.relative_to(root).as_posix(),
            "status": metadata.get("status"),
            "version": metadata.get("version"),
            "ontology_iri": metadata.get("ontology_iri"),
            "version_iri": metadata.get("version_iri"),
            "namespace": metadata.get("namespace"),
            "shape_sets": metadata.get("shape_sets", {}),
            "included_files": [],
            "skipped": False,
            "reason": None,
        }

        if not ontology_artifact:
            module_entry["skipped"] = True
            module_entry["reason"] = "No ontology artifact configured."
            manifest["modules"].append(module_entry)
            continue

        ontology_path = module_dir / ontology_artifact
        if not ontology_path.exists():
            module_entry["skipped"] = True
            module_entry["reason"] = "Ontology file is not available."
            manifest["modules"].append(module_entry)
            continue

        shape_artifacts = [
            (artifact_name, artifacts.get(artifact_name))
            for artifact_name in ("core_shapes", "strict_shapes")
            if artifacts.get(artifact_name)
        ]
        mapping_artifacts = artifacts.get("mapping_artifacts", [])
        missing_shapes = [
            artifact_name
            for artifact_name, artifact_path in shape_artifacts
            if not (module_dir / artifact_path).exists()
        ]
        if missing_shapes:
            module_entry["skipped"] = True
            module_entry["reason"] = (
                "Declared shape file is not available: " + ", ".join(missing_shapes)
            )
            manifest["modules"].append(module_entry)
            continue
        missing_mappings = [
            mapping_artifact
            for mapping_artifact in mapping_artifacts
            if not (module_dir / mapping_artifact).exists()
        ]
        if missing_mappings:
            module_entry["skipped"] = True
            module_entry["reason"] = (
                "Declared mapping file is not available: "
                + ", ".join(missing_mappings)
            )
            manifest["modules"].append(module_entry)
            continue

        target_dir = dist_dir / module_dir.relative_to(root)
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / ontology_path.name
        shutil.copy2(ontology_path, target_file)
        module_entry["included_files"].append(target_file.relative_to(root).as_posix())
        for _, shape_artifact in shape_artifacts:
            shape_path = module_dir / shape_artifact
            target_shape = target_dir / shape_artifact
            target_shape.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(shape_path, target_shape)
            module_entry["included_files"].append(
                target_shape.relative_to(root).as_posix()
            )
        for mapping_artifact in mapping_artifacts:
            mapping_path = module_dir / mapping_artifact
            target_mapping = target_dir / mapping_artifact
            target_mapping.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(mapping_path, target_mapping)
            module_entry["included_files"].append(
                target_mapping.relative_to(root).as_posix()
            )
        manifest["modules"].append(module_entry)

    for dataset_file in iter_dataset_files(root):
        metadata = read_yaml_file(dataset_file)
        dataset_id = metadata.get("id")
        artifacts = metadata.get("artifacts", {})
        data_artifact = artifacts.get("data")
        dataset_dir = dataset_file.parent

        dataset_entry: dict[str, Any] = {
            "id": dataset_id,
            "dataset_path": dataset_dir.relative_to(root).as_posix(),
            "status": metadata.get("status"),
            "version": metadata.get("version"),
            "vocabulary_iri": metadata.get("vocabulary_iri"),
            "version_iri": metadata.get("version_iri"),
            "namespace": metadata.get("namespace"),
            "included_files": [],
            "skipped": False,
            "reason": None,
        }

        if not data_artifact:
            dataset_entry["skipped"] = True
            dataset_entry["reason"] = "No data artifact configured."
            manifest["datasets"].append(dataset_entry)
            continue

        data_path = dataset_dir / data_artifact
        if not data_path.exists():
            dataset_entry["skipped"] = True
            dataset_entry["reason"] = "Dataset file is not available."
            manifest["datasets"].append(dataset_entry)
            continue

        target_dir = dist_dir / dataset_dir.relative_to(root)
        target_dir.mkdir(parents=True, exist_ok=True)
        target_metadata = target_dir / dataset_file.name
        target_data = target_dir / data_artifact
        target_data.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dataset_file, target_metadata)
        shutil.copy2(data_path, target_data)
        dataset_entry["included_files"].extend(
            [
                target_metadata.relative_to(root).as_posix(),
                target_data.relative_to(root).as_posix(),
            ]
        )
        manifest["datasets"].append(dataset_entry)

    for profile_file in iter_profile_files(root):
        metadata = read_yaml_file(profile_file)
        profile_id = metadata.get("id")
        artifacts = metadata.get("artifacts", {})
        shapes_artifact = artifacts.get("shapes")
        examples = artifacts.get("examples", [])
        profile_dir = profile_file.parent

        profile_entry: dict[str, Any] = {
            "id": profile_id,
            "profile_path": profile_dir.relative_to(root).as_posix(),
            "status": metadata.get("status"),
            "version": metadata.get("version"),
            "target_module": metadata.get("target_module"),
            "shape_set": metadata.get("shape_set"),
            "graph_iri": metadata.get("graph_iri"),
            "version_iri": metadata.get("version_iri"),
            "namespace": metadata.get("namespace"),
            "included_files": [],
            "skipped": False,
            "reason": None,
        }

        if not shapes_artifact:
            profile_entry["skipped"] = True
            profile_entry["reason"] = "No profile shapes artifact configured."
            manifest["profiles"].append(profile_entry)
            continue

        shapes_path = profile_dir / shapes_artifact
        missing_examples = [
            example for example in examples if not (profile_dir / example).is_file()
        ]
        if not shapes_path.is_file():
            profile_entry["skipped"] = True
            profile_entry["reason"] = "Profile shapes file is not available."
            manifest["profiles"].append(profile_entry)
            continue
        if missing_examples:
            profile_entry["skipped"] = True
            profile_entry["reason"] = (
                "Declared profile example is not available: "
                + ", ".join(missing_examples)
            )
            manifest["profiles"].append(profile_entry)
            continue

        target_dir = dist_dir / profile_dir.relative_to(root)
        target_metadata = target_dir / profile_file.name
        target_shapes = target_dir / shapes_artifact
        target_shapes.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(profile_file, target_metadata)
        shutil.copy2(shapes_path, target_shapes)
        profile_entry["included_files"].extend(
            [
                target_metadata.relative_to(root).as_posix(),
                target_shapes.relative_to(root).as_posix(),
            ]
        )
        for example in examples:
            example_path = profile_dir / example
            target_example = target_dir / example
            target_example.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(example_path, target_example)
            profile_entry["included_files"].append(
                target_example.relative_to(root).as_posix()
            )
        manifest["profiles"].append(profile_entry)

    manifest_path = dist_dir / "build-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    root = repository_root()
    manifest = build_repository(root)
    module_count = len(manifest["modules"])
    dataset_count = len(manifest["datasets"])
    profile_count = len(manifest["profiles"])
    entries = [*manifest["modules"], *manifest["datasets"], *manifest["profiles"]]
    included_count = sum(len(entry["included_files"]) for entry in entries)
    skipped_count = sum(1 for entry in entries if entry["skipped"])

    print(f"Build manifest created for {module_count} module(s).")
    print(f"Build manifest created for {dataset_count} dataset(s).")
    print(f"Build manifest created for {profile_count} profile(s).")
    print(f"Included files: {included_count}.")
    print(f"Skipped entries: {skipped_count}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

