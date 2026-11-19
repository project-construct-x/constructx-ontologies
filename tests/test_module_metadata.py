from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VSO_MODULE_FILE = ROOT / "modules/core/vso/module.yaml"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_vso_module_yaml_can_be_read() -> None:
    metadata = load_yaml(VSO_MODULE_FILE)
    assert metadata["id"] == "vso"
    assert metadata["type"] == "core"
    assert metadata["ontology_iri"] == "https://www.construct-x.org/ontology/vso"
    assert metadata["version_iri"] == "https://www.construct-x.org/ontology/vso/0.1.0"
    assert metadata["namespace"] == "https://www.construct-x.org/ontology/vso#"
    assert metadata["preferred_namespace_prefix"] == "conx-vso"
    assert metadata["artifacts"]["ontology"] == "ontology/conx-vso.ttl"
    assert metadata["artifacts"]["html_documentation"] == "docs/vso.html"






def test_address_module_yaml_can_be_read() -> None:
    metadata = load_yaml(ROOT / "modules/core/address/module.yaml")
    assert metadata["id"] == "address"
    assert metadata["type"] == "core"
    assert metadata["status"] == "draft"
    assert metadata["version"] == "0.2.0"
    assert metadata["ontology_iri"] == "https://www.construct-x.org/ontology/address"
    assert metadata["version_iri"] == "https://www.construct-x.org/ontology/address/0.2.0"
    assert metadata["namespace"] == "https://www.construct-x.org/ontology/address#"
    assert metadata["preferred_namespace_prefix"] == "conx-addr"
    assert metadata["artifacts"]["ontology"] == "ontology/conx-addr.ttl"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-addr-core.shacl.ttl"
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/address/core",
        "version_iri": "https://www.construct-x.org/shapes/address/core/0.2.0",
        "namespace": "https://www.construct-x.org/shapes/address/core#",
        "version": "0.2.0",
        "artifact": "shapes/conx-addr-core.shacl.ttl",
    }
    assert metadata["artifacts"]["html_documentation"] == "docs/address.html"
    for key in ("concept_model", "confluence_overview"):
        assert (ROOT / "modules/core/address" / metadata["artifacts"][key]).is_file()
