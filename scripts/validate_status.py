"""Offline validation entry point for the Construct-X Status Core contract.

Shared VSO/ISOProps shape definitions retain their IRIs and constraints, but
their global targets are omitted from the in-memory composition. Status
ConditionAssignmentShape invokes their rules only for hasCondition resources.
No source files or input graphs are modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph, Namespace, OWL, RDF, URIRef, Literal
from rdflib.plugins.parsers.notation3 import RDFSink, SinkParser

ROOT = Path(__file__).resolve().parents[1]
SH = Namespace("http://www.w3.org/ns/shacl#")
VERSION = "0.1.0"
STATUS_ONTOLOGY = "https://www.construct-x.org/ontology/status"
STATUS_SHAPES = "https://www.construct-x.org/shapes/status/core"
SHAPE_DEPENDENCIES = (
    ("modules/core/vso/shapes/conx-vso-core.shacl.ttl",
     "https://www.construct-x.org/shapes/vso/core"),
    ("profiles/construct-x/vso-isoprops/shapes/conx-vso-isoprops.shacl.ttl",
     "https://www.construct-x.org/shapes/vso/isoprops"),
)
ONTOLOGY_DEPENDENCIES = (
    ("modules/core/status/ontology/conx-status.ttl", STATUS_ONTOLOGY),
    ("modules/core/agent/ontology/conx-agent.ttl",
     "https://www.construct-x.org/ontology/agent"),
    ("modules/core/vso/ontology/conx-vso.ttl",
     "https://www.construct-x.org/ontology/vso"),
)
VOCABULARIES = ("status-kind", "status-value", "status-reason")
BUNDLE_FILES = {"shapes": "shapes.ttl", "ontology": "ontology.ttl", "vocabularies": "vocabularies.ttl"}
TARGET_PREDICATES = frozenset((
    SH.targetClass, SH.targetNode, SH.targetSubjectsOf, SH.targetObjectsOf, SH.target,
))


class StatusDependencyError(ValueError):
    """A required local, version-pinned validation dependency is unavailable."""


class _LexicalSink(RDFSink):
    def newLiteral(self, value, datatype, language):
        # Preserve lexical forms for SHACL: RDFLib's default normalization can
        # discard a date's timezone before our calendar-date contract sees it.
        return Literal(value, datatype=datatype, lang=language, normalize=False)


def load_status_data(path: Path) -> Graph:
    """Read local Turtle without normalizing away lexical validation evidence."""
    graph = Graph()
    parser = SinkParser(_LexicalSink(graph), baseURI=path.resolve().as_uri(), turtle=True)
    with path.open("r", encoding="utf-8-sig") as stream:
        parser.loadStream(stream)
    for prefix, namespace in parser._bindings.items():
        graph.bind(prefix, namespace)
    return graph


def load_pinned_graph(root: Path, relative: str, graph_iri: str) -> Graph:
    path = root / relative
    if not path.is_file():
        raise StatusDependencyError(f"Missing status validation dependency: {path}")
    graph = load_status_data(path)
    subject = URIRef(graph_iri)
    if (
        (subject, RDF.type, OWL.Ontology) not in graph
        or set(graph.objects(subject, OWL.versionIRI))
        != {URIRef(f"{graph_iri}/{VERSION}")}
        or set(graph.objects(subject, OWL.versionInfo)) != {Literal(VERSION)}
    ):
        raise StatusDependencyError(
            f"Expected {graph_iri}/{VERSION} metadata in {path}"
        )
    return graph


def copy_graph(source: Graph) -> Graph:
    graph = Graph()
    for prefix, namespace in source.namespaces():
        graph.bind(prefix, namespace)
    for triple in source:
        graph.add(triple)
    return graph


def load_status_shapes(root: Path = ROOT) -> Graph:
    """Return the complete shape bundle, scoped to Status and its conditions."""
    result = load_pinned_graph(
        root, "modules/core/status/shapes/conx-status-core.shacl.ttl", STATUS_SHAPES
    )
    for relative, iri in SHAPE_DEPENDENCIES:
        dependency = load_pinned_graph(root, relative, iri)
        for triple in dependency:
            if triple[1] not in TARGET_PREDICATES:
                result.add(triple)
    return result


def load_status_ontology(root: Path = ROOT) -> Graph:
    result = Graph()
    for relative, iri in ONTOLOGY_DEPENDENCIES:
        result += load_pinned_graph(root, relative, iri)
    return result


def load_status_vocabularies(root: Path = ROOT) -> Graph:
    result = Graph()
    for name in VOCABULARIES:
        result += load_pinned_graph(
            root,
            f"datasets/reference/vocabularies/{name}/{name}.ttl",
            f"https://www.construct-x.org/vocab/{name}",
        )
    return result


def load_status_bundle(directory: Path) -> dict[str, Graph]:
    """Load an exported bundle; missing or altered components are setup errors."""
    try:
        manifest = json.loads((directory / "bundle.json").read_text(encoding="utf-8"))
        if manifest["format"] != 1 or manifest["module"] != "status":
            raise StatusDependencyError("Unsupported Status validation bundle")
        graphs = {}
        for key, filename in BUNDLE_FILES.items():
            path = directory / filename
            if hashlib.sha256(path.read_bytes()).hexdigest() != manifest["sha256"][filename]:
                raise StatusDependencyError(f"Altered Status bundle component: {filename}")
            graphs[key] = load_status_data(path)
        return graphs
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise StatusDependencyError(f"Incomplete or invalid Status bundle: {directory}") from exc


def validate_status(
    data_graph: Graph,
    *,
    root: Path = ROOT,
    include_reference_vocabularies: bool = True,
    additional_ontology: Graph | None = None,
    bundle: Path | None = None,
) -> tuple[bool, Graph, str]:
    """Validate a supplied graph plus local reference data, without inference.

    External terms and their compatibility links can be supplied in data_graph.
    Additional subclass definitions can be supplied in additional_ontology.
    Managed vocabulary metadata rules apply only to the three local namespaces.
    """
    exported = load_status_bundle(bundle) if bundle is not None else None
    data = copy_graph(data_graph)
    if include_reference_vocabularies:
        data += exported["vocabularies"] if exported is not None else load_status_vocabularies(root)
    ontology = exported["ontology"] if exported is not None else load_status_ontology(root)
    if additional_ontology is not None:
        ontology += additional_ontology
    return validate(
        data_graph=data,
        shacl_graph=exported["shapes"] if exported is not None else load_status_shapes(root),
        ont_graph=ontology,
        inference="none",
        advanced=True,
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )


def main() -> int:
    # RDFLib warns when its native datetime cannot represent valid XSD hour 24.
    # The CLI reports actual data errors through SHACL instead. Limit this
    # logging change to the command-line process, leaving library callers alone.
    logging.getLogger("rdflib.term").setLevel(logging.ERROR)
    # Reports contain bilingual diagnostics; keep redirected Windows output
    # consistent with the UTF-8 RDF files and other platforms.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data", type=Path, action="append", required=True,
        help="Turtle data file; repeat for additional local context or external vocabulary data.",
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--bundle", type=Path, help="Use an exported Status validation bundle.")
    parser.add_argument(
        "--no-reference-vocabularies", action="store_true",
        help="Supply all vocabulary data through --data instead of loading bundled vocabularies.",
    )
    args = parser.parse_args()
    bundle = args.bundle
    if bundle is None and (Path(__file__).parent / "bundle.json").is_file():
        bundle = Path(__file__).parent
    data = Graph()
    try:
        for path in args.data:
            data += load_status_data(path)
        conforms, _, report = validate_status(
            data, root=args.root.resolve(),
            include_reference_vocabularies=not args.no_reference_vocabularies,
            bundle=bundle,
        )
    except (StatusDependencyError, OSError) as exc:
        parser.exit(2, f"Status validation setup error: {exc}\n")
    print(report)
    return 0 if conforms else 1


if __name__ == "__main__":
    raise SystemExit(main())
