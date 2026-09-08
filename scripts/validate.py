from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import OWL


IGNORED_DIRS = {".git", ".venv", ".uv-cache", "dist", "build", "__pycache__", ".pytest_cache"}
REQUIRED_MODULE_FIELDS = {
    "id",
    "title",
    "type",
    "status",
    "version",
    "ontology_iri",
    "version_iri",
    "namespace",
    "dependencies",
    "maintainers",
    "artifacts",
}
REQUIRED_ARTIFACT_FIELDS = {"ontology", "core_shapes", "strict_shapes", "documentation"}
REQUIRED_DATASET_FIELDS = {
    "id",
    "title",
    "type",
    "status",
    "version",
    "vocabulary_iri",
    "version_iri",
    "namespace",
    "dependencies",
    "artifacts",
}
REQUIRED_PROFILE_FIELDS = {
    "id",
    "title",
    "type",
    "status",
    "version",
    "target_module",
    "shape_set",
    "graph_iri",
    "version_iri",
    "namespace",
    "dependencies",
    "maintainers",
    "artifacts",
}
REQUIRED_PROFILE_ARTIFACT_FIELDS = {"shapes", "documentation", "examples"}
FUTURE_ONTOLOGY_STATUSES = {"draft", "candidate", "released"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
ONTOLOGY_IRI_RE = re.compile(
    r"^https://www\.construct-x\.org/ontology/[a-z][a-z0-9-]*$"
)
ALIGNMENT_IRI_RE = re.compile(
    r"^https://www\.construct-x\.org/alignment/[a-z][a-z0-9-]*$"
)
SHAPE_GRAPH_IRI_RE = re.compile(
    r"^https://www\.construct-x\.org/shapes/[a-z][a-z0-9-]*/[a-z][a-z0-9-]*$"
)
VOCABULARY_IRI_RE = re.compile(
    r"^https://www\.construct-x\.org/vocab/[a-z0-9-]+(?:/[a-z0-9-]+)*$"
)


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    infos: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def is_ignored(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts
    return any(part in IGNORED_DIRS for part in relative_parts)


def iter_files(root: Path, pattern: str) -> list[Path]:
    return sorted(path for path in root.rglob(pattern) if not is_ignored(path, root))


def parse_turtle_files(root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])
    turtle_files = iter_files(root, "*.ttl")

    if not turtle_files:
        result.infos.append("No Turtle files found. This is valid for the current scaffold.")
        return result

    for turtle_file in turtle_files:
        graph = Graph()
        try:
            graph.parse(turtle_file, format="turtle")
        except Exception as exc:  # rdflib raises parser-specific exceptions
            result.errors.append(f"{turtle_file.relative_to(root)}: Turtle parse error: {exc}")
        else:
            result.infos.append(
                f"{turtle_file.relative_to(root)}: parsed {len(graph)} triples."
            )

    return result


def read_yaml_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("YAML document must be a mapping.")
    return data


def validate_graph_version(
    graph: Graph,
    graph_iri: str,
    version_iri: str,
    version: str,
    label: str,
) -> list[str]:
    errors: list[str] = []
    subject = URIRef(graph_iri)
    expected_version_iri = URIRef(version_iri)

    if (subject, RDF.type, OWL.Ontology) not in graph:
        errors.append(f"{label}: stable graph IRI must be typed owl:Ontology: {graph_iri}")
    if list(graph.objects(subject, OWL.versionIRI)) != [expected_version_iri]:
        errors.append(
            f"{label}: owl:versionIRI must be exactly {version_iri}"
        )
    if list(graph.objects(subject, OWL.versionInfo)) != [Literal(version)]:
        errors.append(f"{label}: owl:versionInfo must be exactly {version}")

    return errors


def validate_module_yaml(path: Path, root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])

    try:
        metadata = read_yaml_file(path)
    except Exception as exc:
        result.errors.append(f"{path.relative_to(root)}: YAML read error: {exc}")
        return result

    missing_fields = sorted(REQUIRED_MODULE_FIELDS - set(metadata))
    if missing_fields:
        result.errors.append(
            f"{path.relative_to(root)}: missing required fields: {', '.join(missing_fields)}"
        )
        return result

    artifacts = metadata.get("artifacts")
    if not isinstance(artifacts, dict):
        result.errors.append(f"{path.relative_to(root)}: artifacts must be a mapping.")
        return result

    missing_artifacts = sorted(REQUIRED_ARTIFACT_FIELDS - set(artifacts))
    if missing_artifacts:
        result.errors.append(
            f"{path.relative_to(root)}: missing artifact fields: {', '.join(missing_artifacts)}"
        )

    ontology_artifact = artifacts.get("ontology")
    status = metadata.get("status")
    if not isinstance(ontology_artifact, str) or not ontology_artifact:
        result.errors.append(f"{path.relative_to(root)}: artifacts.ontology must be a path.")
        return result

    ontology_path = path.parent / ontology_artifact
    if not ontology_path.exists():
        if status == "awaiting-ontology":
            result.infos.append(
                f"{path.relative_to(root)}: ontology file is pending: "
                f"{ontology_path.relative_to(root)}"
            )
        elif status in FUTURE_ONTOLOGY_STATUSES:
            result.errors.append(
                f"{path.relative_to(root)}: ontology file is required for status "
                f"{status!r}: {ontology_path.relative_to(root)}"
            )
        else:
            result.warnings.append(
                f"{path.relative_to(root)}: unknown status {status!r}; "
                f"ontology file missing: {ontology_path.relative_to(root)}"
            )

    version = str(metadata.get("version"))
    ontology_iri = metadata.get("ontology_iri")
    version_iri = metadata.get("version_iri")
    namespace = metadata.get("namespace")
    label = str(path.relative_to(root))
    if not SEMVER_RE.fullmatch(version):
        result.errors.append(f"{label}: version must use SemVer: {version}")
    iri_pattern = ALIGNMENT_IRI_RE if metadata.get("type") == "alignment" else ONTOLOGY_IRI_RE
    if not isinstance(ontology_iri, str) or not iri_pattern.fullmatch(ontology_iri):
        result.errors.append(f"{label}: invalid ontology_iri: {ontology_iri}")
    elif version_iri != f"{ontology_iri}/{version}":
        result.errors.append(
            f"{label}: version_iri must be {ontology_iri}/{version}"
        )
    if isinstance(ontology_iri, str) and namespace != f"{ontology_iri}#":
        result.errors.append(f"{label}: namespace must be {ontology_iri}#")

    if ontology_path.is_file() and isinstance(ontology_iri, str) and isinstance(version_iri, str):
        ontology_graph = Graph().parse(ontology_path, format="turtle")
        result.errors.extend(
            validate_graph_version(
                ontology_graph, ontology_iri, version_iri, version, label
            )
        )

    for shape_name in ("core_shapes", "strict_shapes"):
        shape_artifact = artifacts.get(shape_name)
        if shape_artifact is None:
            continue
        if not isinstance(shape_artifact, str) or not shape_artifact:
            result.errors.append(
                f"{path.relative_to(root)}: artifacts.{shape_name} must be a path or null."
            )
            continue
        shape_path = path.parent / shape_artifact
        if not shape_path.is_file():
            result.errors.append(
                f"{path.relative_to(root)}: declared {shape_name} file is missing: "
                f"{shape_path.relative_to(root)}"
            )
            continue

        shape_set_name = shape_name.removesuffix("_shapes")
        shape_sets = metadata.get("shape_sets")
        if not isinstance(shape_sets, dict) or not isinstance(
            shape_sets.get(shape_set_name), dict
        ):
            result.errors.append(
                f"{label}: missing shape_sets.{shape_set_name} metadata"
            )
            continue

        shape_metadata = shape_sets[shape_set_name]
        shape_graph_iri = shape_metadata.get("graph_iri")
        shape_version = str(shape_metadata.get("version"))
        shape_version_iri = shape_metadata.get("version_iri")
        shape_namespace = shape_metadata.get("namespace")
        shape_label = f"{label}: shape_sets.{shape_set_name}"

        if shape_metadata.get("artifact") != shape_artifact:
            result.errors.append(
                f"{shape_label}.artifact must match artifacts.{shape_name}"
            )
        if not SEMVER_RE.fullmatch(shape_version):
            result.errors.append(
                f"{shape_label}.version must use SemVer: {shape_version}"
            )
        if not isinstance(shape_graph_iri, str) or not SHAPE_GRAPH_IRI_RE.fullmatch(
            shape_graph_iri
        ):
            result.errors.append(
                f"{shape_label}.graph_iri must follow /shapes/{{module}}/{{shape-set}}"
            )
            continue
        expected_shape_graph_iri = (
            f"https://www.construct-x.org/shapes/{metadata['id']}/{shape_set_name}"
        )
        if shape_graph_iri != expected_shape_graph_iri:
            result.errors.append(
                f"{shape_label}.graph_iri must be {expected_shape_graph_iri}"
            )
        if shape_version_iri != f"{shape_graph_iri}/{shape_version}":
            result.errors.append(
                f"{shape_label}.version_iri must be "
                f"{shape_graph_iri}/{shape_version}"
            )
        if shape_namespace != f"{shape_graph_iri}#":
            result.errors.append(
                f"{shape_label}.namespace must be {shape_graph_iri}#"
            )
        if isinstance(shape_version_iri, str):
            shape_graph = Graph().parse(shape_path, format="turtle")
            result.errors.extend(
                validate_graph_version(
                    shape_graph,
                    shape_graph_iri,
                    shape_version_iri,
                    shape_version,
                    shape_label,
                )
            )

    mapping_artifacts = artifacts.get("mapping_artifacts", [])
    if not isinstance(mapping_artifacts, list) or not all(
        isinstance(artifact, str) and artifact for artifact in mapping_artifacts
    ):
        result.errors.append(
            f"{label}: artifacts.mapping_artifacts must be a list of paths"
        )
    else:
        for mapping_artifact in mapping_artifacts:
            mapping_path = path.parent / mapping_artifact
            if not mapping_path.is_file():
                result.errors.append(
                    f"{label}: declared mapping artifact is missing: "
                    f"{mapping_path.relative_to(root)}"
                )

    result.infos.append(f"{path.relative_to(root)}: module metadata loaded.")
    return result


def validate_module_files(root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])
    module_files = iter_files(root, "module.yaml")

    if not module_files:
        result.warnings.append("No module.yaml files found.")
        return result

    for module_file in module_files:
        module_result = validate_module_yaml(module_file, root)
        result.errors.extend(module_result.errors)
        result.warnings.extend(module_result.warnings)
        result.infos.extend(module_result.infos)

    return result


def validate_dataset_yaml(path: Path, root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])
    label = str(path.relative_to(root))

    try:
        metadata = read_yaml_file(path)
    except Exception as exc:
        result.errors.append(f"{label}: YAML read error: {exc}")
        return result

    missing_fields = sorted(REQUIRED_DATASET_FIELDS - set(metadata))
    if missing_fields:
        result.errors.append(
            f"{label}: missing required fields: {', '.join(missing_fields)}"
        )
        return result

    version = str(metadata["version"])
    vocabulary_iri = metadata["vocabulary_iri"]
    version_iri = metadata["version_iri"]
    namespace = metadata["namespace"]

    if metadata["type"] != "reference-vocabulary":
        result.errors.append(f"{label}: type must be reference-vocabulary")
    if not SEMVER_RE.fullmatch(version):
        result.errors.append(f"{label}: version must use SemVer: {version}")
    if not isinstance(vocabulary_iri, str) or not VOCABULARY_IRI_RE.fullmatch(
        vocabulary_iri
    ):
        result.errors.append(f"{label}: invalid vocabulary_iri: {vocabulary_iri}")
        return result
    if version_iri != f"{vocabulary_iri}/{version}":
        result.errors.append(
            f"{label}: version_iri must be {vocabulary_iri}/{version}"
        )
    if namespace != f"{vocabulary_iri}#":
        result.errors.append(f"{label}: namespace must be {vocabulary_iri}#")

    artifacts = metadata.get("artifacts")
    if not isinstance(artifacts, dict) or not isinstance(artifacts.get("data"), str):
        result.errors.append(f"{label}: artifacts.data must be a path")
        return result
    data_path = path.parent / artifacts["data"]
    if not data_path.is_file():
        result.errors.append(
            f"{label}: declared data file is missing: {data_path.relative_to(root)}"
        )
        return result

    graph = Graph().parse(data_path, format="turtle")
    result.errors.extend(
        validate_graph_version(graph, vocabulary_iri, version_iri, version, label)
    )

    dependencies = metadata.get("dependencies")
    if not isinstance(dependencies, list):
        result.errors.append(f"{label}: dependencies must be a list")
    else:
        for dependency in dependencies:
            if not isinstance(dependency, dict) or "version" not in dependency:
                continue
            stable_iri = dependency.get("ontology_iri") or dependency.get(
                "vocabulary_iri"
            )
            if stable_iri and dependency.get("version_iri") != (
                f"{stable_iri}/{dependency['version']}"
            ):
                result.errors.append(
                    f"{label}: internal dependency {dependency.get('id')} must use "
                    "a matching version_iri"
                )

    result.infos.append(f"{label}: dataset metadata and graph version loaded.")
    return result


def validate_dataset_files(root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])
    dataset_files = iter_files(root, "dataset.yaml")

    for dataset_file in dataset_files:
        dataset_result = validate_dataset_yaml(dataset_file, root)
        result.errors.extend(dataset_result.errors)
        result.warnings.extend(dataset_result.warnings)
        result.infos.extend(dataset_result.infos)

    return result


def validate_profile_yaml(path: Path, root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])
    label = str(path.relative_to(root))

    try:
        metadata = read_yaml_file(path)
    except Exception as exc:
        result.errors.append(f"{label}: YAML read error: {exc}")
        return result

    missing_fields = sorted(REQUIRED_PROFILE_FIELDS - set(metadata))
    if missing_fields:
        result.errors.append(
            f"{label}: missing required fields: {', '.join(missing_fields)}"
        )
        return result

    if metadata["type"] != "profile":
        result.errors.append(f"{label}: type must be profile")

    version = str(metadata["version"])
    target_module = metadata["target_module"]
    shape_set = metadata["shape_set"]
    graph_iri = metadata["graph_iri"]
    version_iri = metadata["version_iri"]
    namespace = metadata["namespace"]

    if not SEMVER_RE.fullmatch(version):
        result.errors.append(f"{label}: version must use SemVer: {version}")
    if not isinstance(target_module, str) or not re.fullmatch(
        r"[a-z][a-z0-9-]*", target_module
    ):
        result.errors.append(f"{label}: invalid target_module: {target_module}")
    if not isinstance(shape_set, str) or not re.fullmatch(
        r"[a-z][a-z0-9-]*", shape_set
    ):
        result.errors.append(f"{label}: invalid shape_set: {shape_set}")

    expected_graph_iri = (
        f"https://www.construct-x.org/shapes/{target_module}/{shape_set}"
    )
    if graph_iri != expected_graph_iri:
        result.errors.append(f"{label}: graph_iri must be {expected_graph_iri}")
    if version_iri != f"{graph_iri}/{version}":
        result.errors.append(f"{label}: version_iri must be {graph_iri}/{version}")
    if namespace != f"{graph_iri}#":
        result.errors.append(f"{label}: namespace must be {graph_iri}#")

    artifacts = metadata.get("artifacts")
    if not isinstance(artifacts, dict):
        result.errors.append(f"{label}: artifacts must be a mapping")
        return result

    missing_artifacts = sorted(REQUIRED_PROFILE_ARTIFACT_FIELDS - set(artifacts))
    if missing_artifacts:
        result.errors.append(
            f"{label}: missing artifact fields: {', '.join(missing_artifacts)}"
        )
        return result

    shapes_artifact = artifacts.get("shapes")
    if not isinstance(shapes_artifact, str) or not shapes_artifact:
        result.errors.append(f"{label}: artifacts.shapes must be a path")
    else:
        shapes_path = path.parent / shapes_artifact
        if not shapes_path.is_file():
            result.errors.append(
                f"{label}: declared shapes file is missing: "
                f"{shapes_path.relative_to(root)}"
            )
        else:
            shapes_graph = Graph().parse(shapes_path, format="turtle")
            result.errors.extend(
                validate_graph_version(
                    shapes_graph,
                    graph_iri,
                    version_iri,
                    version,
                    label,
                )
            )
            if list(shapes_graph.objects(None, OWL.imports)):
                result.errors.append(
                    f"{label}: profile shapes must not declare owl:imports"
                )

    documentation_artifact = artifacts.get("documentation")
    if not isinstance(documentation_artifact, str) or not (
        path.parent / documentation_artifact
    ).is_file():
        result.errors.append(
            f"{label}: artifacts.documentation must reference an existing file"
        )

    examples = artifacts.get("examples")
    if not isinstance(examples, list) or not all(
        isinstance(example, str) and example for example in examples
    ):
        result.errors.append(f"{label}: artifacts.examples must be a list of paths")
    else:
        for example in examples:
            example_path = path.parent / example
            if not example_path.is_file():
                result.errors.append(
                    f"{label}: declared example is missing: "
                    f"{example_path.relative_to(root)}"
                )

    if not isinstance(metadata.get("dependencies"), list):
        result.errors.append(f"{label}: dependencies must be a list")

    result.infos.append(f"{label}: profile metadata loaded.")
    return result


def validate_profile_files(root: Path) -> ValidationResult:
    result = ValidationResult(errors=[], warnings=[], infos=[])

    for profile_file in iter_files(root, "profile.yaml"):
        profile_result = validate_profile_yaml(profile_file, root)
        result.errors.extend(profile_result.errors)
        result.warnings.extend(profile_result.warnings)
        result.infos.extend(profile_result.infos)

    return result


def combine_results(*results: ValidationResult) -> ValidationResult:
    combined = ValidationResult(errors=[], warnings=[], infos=[])
    for result in results:
        combined.errors.extend(result.errors)
        combined.warnings.extend(result.warnings)
        combined.infos.extend(result.infos)
    return combined


def print_result(result: ValidationResult) -> None:
    for info in result.infos:
        print(f"INFO: {info}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)


def validate_repository(root: Path) -> ValidationResult:
    return combine_results(
        parse_turtle_files(root),
        validate_module_files(root),
        validate_dataset_files(root),
        validate_profile_files(root),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the ontology repository scaffold.")
    parser.add_argument(
        "--root",
        type=Path,
        default=repository_root(),
        help="Repository root. Defaults to the parent directory of scripts/.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    result = validate_repository(root)
    print_result(result)

    if result.ok:
        print("Validation successful.")
        return 0

    print("Validation failed.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

