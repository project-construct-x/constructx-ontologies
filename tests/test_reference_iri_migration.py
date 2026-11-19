from pathlib import Path

from rdflib import Graph, URIRef


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_IRI_PREFIXES = (
    "https://www.construct-x.org/id/country/",
    "https://www.construct-x.org/id/administrative-area/",
    "https://www.construct-x.org/id/organization/construct-x",
)
REQUIRED_IRIS = {
    "https://www.construct-x.org/vocab/address-role#PostalAddressRole",
    "https://www.construct-x.org/vocab/country#DEU",
    "https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#DE-NW",
    "https://www.construct-x.org/vocab/identifier-scheme#iso-3166-1-alpha-2",
    "https://www.construct-x.org/vocab/identifier-scheme#nuts-2",
    "https://www.construct-x.org/vocab/administrative-area/nuts-2#DEA5",
    "https://www.construct-x.org/id/organization/ecbe8336-94ab-5c11-8220-94f260963eb2/revision/1",
}


def iter_turtle_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.ttl")
        if not any(part in {".git", ".venv", ".uv-cache", "build", "dist"} for part in path.parts)
    )


def construct_x_iris() -> set[str]:
    iris: set[str] = set()
    for path in iter_turtle_files():
        graph = Graph().parse(path, format="turtle")
        for triple in graph:
            for node in triple:
                if isinstance(node, URIRef) and str(node).startswith("https://www.construct-x.org/"):
                    iris.add(str(node))
    return iris


def test_reference_vocabularies_use_hash_namespaces_for_terms() -> None:
    iris = construct_x_iris()

    assert REQUIRED_IRIS.issubset(iris)
    assert not {
        iri
        for iri in iris
        for forbidden_prefix in FORBIDDEN_IRI_PREFIXES
        if iri.startswith(forbidden_prefix)
    }

    versioned_vocabularies = {
        "https://www.construct-x.org/vocab/address-role": "0.3.0",
        "https://www.construct-x.org/vocab/country": "0.1.0",
        "https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de": "0.1.0",
        "https://www.construct-x.org/vocab/identifier-scheme": "0.2.0",
        "https://www.construct-x.org/vocab/administrative-area/nuts-2": "0.1.0",
    }
    for stable_iri, version in versioned_vocabularies.items():
        slash_iris = {iri for iri in iris if iri.startswith(f"{stable_iri}/")}
        assert slash_iris == {f"{stable_iri}/{version}"}


def test_persistent_id_resources_use_revision_bound_iris() -> None:
    iris = construct_x_iris()
    id_iris = {iri for iri in iris if iri.startswith("https://www.construct-x.org/id/")}

    assert id_iris
    assert all("/revision/" in iri for iri in id_iris)
