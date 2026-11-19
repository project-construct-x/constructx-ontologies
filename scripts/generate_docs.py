from __future__ import annotations

import importlib.util
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


IGNORED_DIRS = {".git", ".venv", ".uv-cache", "dist", "build", "__pycache__", ".pytest_cache"}


@dataclass(frozen=True)
class GeneratedDocs:
    module_overview: Path
    profile_overview: Path
    ontology_pages: list[Path]
    skipped_modules: list[str]


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def is_ignored(path: Path, root: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.relative_to(root).parts)


def iter_module_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("module.yaml") if not is_ignored(path, root))


def iter_profile_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("profile.yaml") if not is_ignored(path, root))


def read_yaml_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping.")
    return data


def module_has_ontology(module_file: Path, artifacts: dict[str, Any]) -> bool:
    ontology_artifact = artifacts.get("ontology")
    if not ontology_artifact:
        return False
    return (module_file.parent / ontology_artifact).exists()


def ontology_html_output_path(module_file: Path, metadata: dict[str, Any]) -> Path:
    artifacts: dict[str, Any] = metadata.get("artifacts", {})
    configured_path = artifacts.get("html_documentation")
    module_id = str(metadata.get("id"))
    relative_path = Path(configured_path or f"docs/{module_id}.html")

    if relative_path.is_absolute():
        raise ValueError("artifacts.html_documentation must be a module-relative path.")
    if not relative_path.parts or relative_path.parts[0] != "docs":
        raise ValueError("Ontology HTML documentation must be generated inside the module docs/ directory.")

    return module_file.parent / relative_path


def render_module_overview(root: Path) -> str:
    lines = [
        "# Registered Ontology Modules",
        "",
        "This file is generated from `module.yaml` files.",
        "Do not treat it as manually maintained source documentation.",
        "",
        "| ID | Title | Type | Status | Ontology artifact | HTML documentation |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    module_files = iter_module_files(root)
    if not module_files:
        lines.append("| _none_ | _none_ | _none_ | _none_ | _none_ | _none_ |")
        return "\n".join(lines) + "\n"

    for module_file in module_files:
        metadata = read_yaml_file(module_file)
        artifacts: dict[str, Any] = metadata.get("artifacts", {})
        module_id = str(metadata.get("id"))
        html_doc = (
            ontology_html_output_path(module_file, metadata).relative_to(root).as_posix()
            if module_has_ontology(module_file, artifacts)
            else "_not generated_"
        )
        lines.append(
            "| {id} | {title} | {type} | {status} | {ontology} | {html_doc} |".format(
                id=module_id,
                title=metadata.get("title"),
                type=metadata.get("type"),
                status=metadata.get("status"),
                ontology=artifacts.get("ontology"),
                html_doc=html_doc,
            )
        )

    return "\n".join(lines) + "\n"


def render_profile_overview(root: Path) -> str:
    lines = [
        "# Registered Validation Profiles",
        "",
        "This file is generated from `profile.yaml` files.",
        "Do not treat it as manually maintained source documentation.",
        "",
        "| ID | Title | Status | Target module | Shape graph | Shapes | Documentation |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    profile_files = iter_profile_files(root)
    if not profile_files:
        lines.append("| _none_ | _none_ | _none_ | _none_ | _none_ | _none_ | _none_ |")
        return "\n".join(lines) + "\n"

    for profile_file in profile_files:
        metadata = read_yaml_file(profile_file)
        artifacts: dict[str, Any] = metadata.get("artifacts", {})
        profile_dir = profile_file.parent
        shapes = profile_dir / str(artifacts.get("shapes"))
        documentation = profile_dir / str(artifacts.get("documentation"))
        lines.append(
            "| {id} | {title} | {status} | {target} | {graph} | {shapes} | {docs} |".format(
                id=metadata.get("id"),
                title=metadata.get("title"),
                status=metadata.get("status"),
                target=metadata.get("target_module"),
                graph=metadata.get("graph_iri"),
                shapes=shapes.relative_to(root).as_posix(),
                docs=documentation.relative_to(root).as_posix(),
            )
        )

    return "\n".join(lines) + "\n"


def ensure_ontolens_importable() -> bool:
    if importlib.util.find_spec("ontolens") is not None:
        return True

    configured_src = os.environ.get("ONTOLENS_SRC")
    candidates = [Path(configured_src)] if configured_src else []

    for candidate in candidates:
        if candidate.exists() and (candidate / "ontolens" / "__init__.py").exists():
            sys.path.insert(0, str(candidate))
            return importlib.util.find_spec("ontolens") is not None

    return False


def generate_ontology_page(module_file: Path) -> Path | None:
    metadata = read_yaml_file(module_file)
    artifacts: dict[str, Any] = metadata.get("artifacts", {})
    ontology_artifact = artifacts.get("ontology")
    if not ontology_artifact:
        return None

    ontology_path = module_file.parent / ontology_artifact
    if not ontology_path.exists():
        return None

    if not ensure_ontolens_importable():
        raise RuntimeError(
            "OntoLens is not importable. Install ontolens or set ONTOLENS_SRC to the local src directory."
        )

    from ontolens import render as ontolens_render

    output_path = ontology_html_output_path(module_file, metadata)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    original_timestamped_output_path = getattr(ontolens_render, "_timestamped_output_path", None)
    if original_timestamped_output_path is None:
        raise RuntimeError("OntoLens render API changed: missing _timestamped_output_path.")

    try:
        # This repository declares stable module-local documentation paths in module.yaml.
        # OntoLens defaults to timestamped bundles, so the wrapper disables that here.
        ontolens_render._timestamped_output_path = lambda requested_path, generated_at=None: requested_path
        generated_path = ontolens_render.generate(
            ontology_path,
            output_path,
            rdf_format="turtle",
            language="en",
            recommendations=True,
            quality_report=True,
            include_custom_annotations=True,
        )
    finally:
        ontolens_render._timestamped_output_path = original_timestamped_output_path

    if generated_path != output_path:
        raise RuntimeError(f"OntoLens generated {generated_path}, expected {output_path}.")
    return generated_path


def remove_stale_dist_docs(root: Path) -> None:
    stale_docs = root / "dist" / "docs"
    if stale_docs.exists():
        shutil.rmtree(stale_docs)


def generate_docs(root: Path) -> GeneratedDocs:
    remove_stale_dist_docs(root)
    overview_dir = root / "docs" / "generated"
    overview_dir.mkdir(parents=True, exist_ok=True)
    module_overview = overview_dir / "module-overview.md"
    module_overview.write_text(render_module_overview(root), encoding="utf-8")
    profile_overview = overview_dir / "profile-overview.md"
    profile_overview.write_text(render_profile_overview(root), encoding="utf-8")

    ontology_pages: list[Path] = []
    skipped_modules: list[str] = []
    for module_file in iter_module_files(root):
        output_path = generate_ontology_page(module_file)
        if output_path is None:
            skipped_modules.append(str(module_file.parent.relative_to(root)))
        else:
            ontology_pages.append(output_path)

    return GeneratedDocs(
        module_overview=module_overview,
        profile_overview=profile_overview,
        ontology_pages=ontology_pages,
        skipped_modules=skipped_modules,
    )


def main() -> int:
    root = repository_root()
    docs = generate_docs(root)
    print(f"Generated {docs.module_overview.relative_to(root)}.")
    print(f"Generated {docs.profile_overview.relative_to(root)}.")
    for page in docs.ontology_pages:
        print(f"Generated {page.relative_to(root)} with OntoLens.")
    for module in docs.skipped_modules:
        print(f"Skipped ontology HTML for {module}: no ontology artifact available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
