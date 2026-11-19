from pathlib import Path

from scripts.build import build_repository


def test_build_includes_declared_reference_vocabulary(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "datasets/reference/vocabularies/address-roles"
    dataset_dir.mkdir(parents=True)
    (dataset_dir / "address-roles.ttl").write_text(
        "<https://example.org/role> <https://example.org/name> \"Role\" .\n",
        encoding="utf-8",
    )
    (dataset_dir / "dataset.yaml").write_text(
        "\n".join(
            [
                "id: address-roles",
                "status: draft",
                "version: 0.1.0",
                "artifacts:",
                "  data: address-roles.ttl",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = build_repository(tmp_path)

    assert manifest["modules"] == []
    assert manifest["datasets"] == [
        {
            "id": "address-roles",
            "dataset_path": "datasets/reference/vocabularies/address-roles",
            "status": "draft",
            "version": "0.1.0",
            "vocabulary_iri": None,
            "version_iri": None,
            "namespace": None,
            "included_files": [
                "dist/datasets/reference/vocabularies/address-roles/dataset.yaml",
                "dist/datasets/reference/vocabularies/address-roles/address-roles.ttl",
            ],
            "skipped": False,
            "reason": None,
        }
    ]
    assert (
        tmp_path / "dist/datasets/reference/vocabularies/address-roles/address-roles.ttl"
    ).is_file()
    assert (
        tmp_path / "dist/datasets/reference/vocabularies/address-roles/dataset.yaml"
    ).is_file()


def test_build_preserves_nested_dataset_artifact_path(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "datasets/reference/administrative-territories/countries"
    data_dir = dataset_dir / "data"
    data_dir.mkdir(parents=True)
    (data_dir / "countries.ttl").write_text(
        "<https://example.org/country> <https://example.org/name> \"Country\" .\n",
        encoding="utf-8",
    )
    (dataset_dir / "dataset.yaml").write_text(
        "\n".join(
            [
                "id: countries",
                "status: draft",
                "version: 0.1.0",
                "artifacts:",
                "  data: data/countries.ttl",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = build_repository(tmp_path)

    assert manifest["datasets"][0]["included_files"] == [
        "dist/datasets/reference/administrative-territories/countries/dataset.yaml",
        "dist/datasets/reference/administrative-territories/countries/data/countries.ttl",
    ]
    assert (
        tmp_path
        / "dist/datasets/reference/administrative-territories/countries/data/countries.ttl"
    ).is_file()


def test_build_includes_declared_module_shapes(tmp_path: Path) -> None:
    module_dir = tmp_path / "modules/core/address"
    ontology_dir = module_dir / "ontology"
    shapes_dir = module_dir / "shapes"
    ontology_dir.mkdir(parents=True)
    shapes_dir.mkdir()
    (ontology_dir / "address.ttl").write_text(
        "<https://example.org/address> a <http://www.w3.org/2002/07/owl#Ontology> .\n",
        encoding="utf-8",
    )
    (shapes_dir / "address-core.ttl").write_text(
        "<https://example.org/AddressShape> a <http://www.w3.org/ns/shacl#NodeShape> .\n",
        encoding="utf-8",
    )
    (module_dir / "module.yaml").write_text(
        "\n".join(
            [
                "id: address",
                "status: draft",
                "artifacts:",
                "  ontology: ontology/address.ttl",
                "  core_shapes: shapes/address-core.ttl",
                "  strict_shapes: null",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = build_repository(tmp_path)

    assert manifest["modules"][0]["included_files"] == [
        "dist/modules/core/address/address.ttl",
        "dist/modules/core/address/shapes/address-core.ttl",
    ]
    assert (tmp_path / "dist/modules/core/address/shapes/address-core.ttl").is_file()




def test_build_includes_profile_metadata_shapes_and_examples(tmp_path: Path) -> None:
    profile_dir = tmp_path / "profiles/construction-x/vso-isoprops"
    shapes_dir = profile_dir / "shapes"
    examples_dir = profile_dir / "examples"
    shapes_dir.mkdir(parents=True)
    examples_dir.mkdir()
    (shapes_dir / "profile.ttl").write_text(
        "<https://example.org/shapes> a <http://www.w3.org/2002/07/owl#Ontology> .\n",
        encoding="utf-8",
    )
    (examples_dir / "valid.ttl").write_text(
        "<https://example.org/subject> <https://example.org/value> \"valid\" .\n",
        encoding="utf-8",
    )
    (profile_dir / "profile.yaml").write_text(
        "\n".join(
            [
                "id: vso-isoprops",
                "status: draft",
                "version: 0.1.0",
                "target_module: vso",
                "shape_set: isoprops",
                "graph_iri: https://example.org/shapes",
                "version_iri: https://example.org/shapes/0.1.0",
                "namespace: https://example.org/shapes#",
                "artifacts:",
                "  shapes: shapes/profile.ttl",
                "  examples:",
                "    - examples/valid.ttl",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = build_repository(tmp_path)

    assert manifest["profiles"][0]["included_files"] == [
        "dist/profiles/construction-x/vso-isoprops/profile.yaml",
        "dist/profiles/construction-x/vso-isoprops/shapes/profile.ttl",
        "dist/profiles/construction-x/vso-isoprops/examples/valid.ttl",
    ]
    assert (
        tmp_path
        / "dist/profiles/construction-x/vso-isoprops/shapes/profile.ttl"
    ).is_file()
