"""Export the complete Status validation package without building other modules."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

if __package__:
    from .validate_status import (
        BUNDLE_FILES, ROOT, load_status_ontology, load_status_shapes, load_status_vocabularies,
    )
else:
    from validate_status import (
        BUNDLE_FILES, ROOT, load_status_ontology, load_status_shapes, load_status_vocabularies,
    )


def build_status_bundle(root: Path, output: Path) -> list[Path]:
    # Resolve all pinned inputs before writing anything. A missing dependency
    # must fail the build, never produce a deceptively incomplete shape graph.
    graphs = {
        "shapes": load_status_shapes(root),
        "ontology": load_status_ontology(root),
        "vocabularies": load_status_vocabularies(root),
    }
    output.mkdir(parents=True, exist_ok=True)
    files = []
    checksums = {}
    for key, graph in graphs.items():
        path = output / BUNDLE_FILES[key]
        graph.serialize(path, format="turtle")
        checksums[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        files.append(path)
    manifest = output / "bundle.json"
    manifest.write_text(json.dumps({
        "format": 1, "module": "status", "version": "0.1.0",
        "sha256": checksums,
    }, indent=2) + "\n", encoding="utf-8")
    runner = output / "validate.py"
    shutil.copy2(Path(__file__).with_name("validate_status.py"), runner)
    readme = output / "README.md"
    readme.write_text("""# Status validation bundle

This package works outside the source repository. Install Python 3.12 or later,
RDFLib and pySHACL, then run:

```console
python validate.py --data /path/to/status-data.ttl
```

Repeat `--data` for additional local context, such as an external vocabulary
or an actor's Core subclass ontology. Use `--no-reference-vocabularies` when
supplying all vocabulary data yourself. No network lookup is performed.
Exit codes: 0 valid, 1 invalid, 2 missing or altered bundle components.

For another SHACL-SPARQL processor, use `shapes.ttl` as the complete shapes
graph. Merge `vocabularies.ttl` into your data graph and supply `ontology.ttl`
as ontology context (or merge it into the data graph). No inference is needed.
Preserve literal lexical forms during loading so malformed values are not
normalized away. The included runner does this for Turtle input.

recordedAt supports XSD end-of-day notation, for example
2026-12-31T24:00:00Z for midnight at the beginning of 1 January 2027.
The supplied spelling is preserved; the complete SHACL graph validates the
calendar date, datatype and allowed zero-valued clock components. recordedAt
and its UTC offset remain optional. The runner reports data errors through
SHACL and suppresses RDFLib's native-conversion warnings for hour 24.

The bundle retains shared VSO/ISOProps constraints while removing their global
targets. They apply only to Status conditions. Do not add the original globally
targeted ISOProps graph unless validating all VSO assignments is intended.
The bundle manifest records SHA-256 hashes of all three RDF components.
""", encoding="utf-8")
    return [*files, manifest, runner, readme]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    paths = build_status_bundle(args.root.resolve(), args.output.resolve())
    print(f"Status validation bundle: {args.output} ({len(paths)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
