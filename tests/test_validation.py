from pathlib import Path

import pytest
from rdflib import Graph

from scripts.validate import (
    validate_dataset_yaml,
    validate_module_yaml,
    validate_repository,
)


ROOT = Path(__file__).resolve().parents[1]


def test_valid_turtle_string_can_be_parsed() -> None:
    graph = Graph()
    graph.parse(
        data="""
            @prefix ex: <https://example.invalid/> .
            ex:subject ex:predicate "value" .
        """,
        format="turtle",
    )
    assert len(graph) == 1


def test_invalid_turtle_string_is_detected() -> None:
    graph = Graph()
    with pytest.raises(Exception):
        graph.parse(data="@prefix ex: <https://example.invalid/> . ex:s ex:p", format="turtle")


def test_missing_ontology_is_error_for_future_module_status() -> None:
    module_file = ROOT / "tests/fixtures/draft-missing/draft-missing.yaml"

    result = validate_module_yaml(module_file, ROOT / "tests/fixtures")

    assert not result.ok
    assert any("ontology file is required" in error for error in result.errors)


def test_validation_succeeds_with_provided_ontology_files() -> None:
    result = validate_repository(ROOT)
    assert result.ok
    assert any("modules" in info and "conx-vso.ttl" in info for info in result.infos)
    assert any("modules" in info and "conx-addr.ttl" in info and "parsed" in info for info in result.infos)


def test_reference_vocabulary_without_version_iri_is_rejected(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "vocabulary"
    dataset_dir.mkdir()
    (dataset_dir / "vocabulary.ttl").write_text(
        "<https://www.construct-x.org/vocab/example> "
        "a <http://www.w3.org/2002/07/owl#Ontology> .\n",
        encoding="utf-8",
    )
    metadata_file = dataset_dir / "dataset.yaml"
    metadata_file.write_text(
        "\n".join(
            [
                "id: example",
                "title: Example",
                "type: reference-vocabulary",
                "status: draft",
                "version: 0.1.0",
                "vocabulary_iri: https://www.construct-x.org/vocab/example",
                "namespace: https://www.construct-x.org/vocab/example#",
                "dependencies: []",
                "artifacts:",
                "  data: vocabulary.ttl",
            ]
        ),
        encoding="utf-8",
    )

    result = validate_dataset_yaml(metadata_file, tmp_path)

    assert not result.ok
    assert any("version_iri" in error for error in result.errors)
