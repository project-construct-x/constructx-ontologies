import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAMESPACE_DOC = ROOT / "docs/architecture/construct-x-namespace-konzept.md"


def test_namespace_concept_documents_public_iri_patterns() -> None:
    text = NAMESPACE_DOC.read_text(encoding="utf-8-sig")
    # Placeholder names and surrounding prose may be translated or reworded.
    normalized = re.sub(r"\{[^{}\s]+\}", "{}", text)
    for pattern in (
        "https://www.construct-x.org/vocab/{}/{}",
        "https://www.construct-x.org/vocab/{}#{}",
        "https://www.construct-x.org/id/{}/{}",
        "https://www.construct-x.org/id/{}/{}/revision/{}",
        "https://www.construct-x.org/shapes/{}/{}",
        "https://www.construct-x.org/shapes/{}/{}/{}",
        "https://www.construct-x.org/shapes/{}/{}#{}",
    ):
        assert pattern in normalized, pattern
