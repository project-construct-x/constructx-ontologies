from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAMESPACE_DOC = ROOT / "docs/architecture/construct-x-namespace-konzept.md"


def test_namespace_concept_documents_vocab_and_reference_object_versioning() -> None:
    text = NAMESPACE_DOC.read_text(encoding="utf-8")

    assert "https://www.construct-x.org/vocab/{vokabular}/{semver}" in text
    assert "https://www.construct-x.org/vocab/{vokabular}#{localName}" in text
    assert "https://www.construct-x.org/id/{typ}/{guid}" in text
    assert "https://www.construct-x.org/id/{typ}/{guid}/revision/{revision}" in text
    assert "Referenzobjekte werden individuell versioniert und verwenden ausdruecklich kein SemVer" in text
    assert "Die SemVer-Version eines veroeffentlichten Graphen und die Revision" in text


def test_namespace_concept_uses_guid_placeholder_for_reference_objects() -> None:
    text = NAMESPACE_DOC.read_text(encoding="utf-8")

    assert "/id/{typ}/{id}" not in text
    assert "Dokumentstand: 2026-08-18" in text


def test_namespace_concept_documents_versioned_shape_sets() -> None:
    text = NAMESPACE_DOC.read_text(encoding="utf-8")

    assert "https://www.construct-x.org/shapes/{modul}/{shape-set}" in text
    assert "https://www.construct-x.org/shapes/{modul}/{shape-set}/{semver}" in text
    assert "https://www.construct-x.org/shapes/{modul}/{shape-set}#{localName}" in text
