"""Documentation integrity checks without editorial or language requirements."""

from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote, urlsplit

import markdown
import yaml
from bs4 import BeautifulSoup


def module_artifacts(module: Path) -> dict:
    return yaml.safe_load(
        (module / "module.yaml").read_text(encoding="utf-8-sig")
    )["artifacts"]


def documentation_files(module: Path) -> set[Path]:
    files = set()
    for value in module_artifacts(module).values():
        for relative in value if isinstance(value, list) else [value]:
            if isinstance(relative, str) and Path(relative).suffix in {".md", ".html", ".pdf"}:
                files.add(module / relative)
    return files


@lru_cache
def rendered_document(path: Path) -> BeautifulSoup:
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix == ".md":
        text = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    return BeautifulSoup(text, "html.parser")


def broken_local_links(files) -> list[tuple[Path, str, str]]:
    errors = []
    for file in files:
        for link in rendered_document(file).select("a[href]"):
            target = urlsplit(link["href"])
            if target.scheme or target.netloc:
                continue
            path = (file.parent / unquote(target.path)).resolve() if target.path else file
            if not path.exists():
                errors.append((file, link["href"], "missing file"))
            elif target.fragment and path.suffix in {".md", ".html"}:
                if rendered_document(path).find(id=unquote(target.fragment)) is None:
                    errors.append((file, link["href"], "missing anchor"))
    return errors
