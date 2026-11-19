# Documentation Generation

Repository documentation consists of manually maintained Markdown documents
and generated HTML views of the ontologies. These artifacts follow different
naming rules.

## 1. Manual Core Module Documentation

Every Core module uses a numbered Markdown package under its `docs/` folder:

```text
00_index.md
01_source-analysis.md
02_scope-and-competency-questions.md
03_concept-model.md
04_module-boundaries.md
05_term-catalog.md
06_shacl-requirements.md
07_core-shapes.md
08_concept-diagram.md
09_confluence-overview.md
```

Module-specific supplementary documents continue with `10_`, `11_`, and so
on. The binding structure and content responsibilities are defined in
[`modules/core/DOCUMENTATION.md`](../../modules/core/DOCUMENTATION.md).

All Markdown artifacts are registered with their module-relative paths in the
module's `module.yaml`. Renaming a document therefore requires updating its
metadata entry, links, and documentation tests in the same change.

Profiles and alignments also use `00_index.md` as their documentation entry
point. Their remaining manually maintained documents continue with `01_`,
`02_`, and so on in package-specific reading order. They do not need to create
empty files for every Core-specific topic from `01` through `09`.

## 2. OntoLens HTML Documentation

HTML documentation for RDF/OWL ontologies is generated with OntoLens. The
script `scripts/generate_docs.py` loads OntoLens in this order:

1. from an installed Python package named `ontolens`, if available in the
   project environment;
2. from the local `src` directory configured through `ONTOLENS_SRC`.

No machine-specific default path is used. A local OntoLens checkout is only
included when `ONTOLENS_SRC` is set explicitly.

Run the generator from the repository root:

```bash
uv run python scripts/generate_docs.py
```

Generated ontology HTML remains unnumbered and is written directly to each
ontology module's `docs/` folder, for example:

```text
modules/core/vso/docs/vso.html
modules/core/address/docs/address.html
modules/core/status/docs/status.html
```

The central generated module overview is written to:

```text
docs/generated/module-overview.md
```

The `dist/` directory remains reserved for build artifacts and is not a
location for readable ontology documentation.

## 3. Registered Sources and Targets

The generator reads the Turtle file and HTML target registered in
`module.yaml`. `artifacts.html_documentation` must point to a location below the
module's `docs/` folder.

Examples:

```text
modules/core/vso/ontology/conx-vso.ttl -> modules/core/vso/docs/vso.html
modules/core/address/ontology/conx-addr.ttl -> modules/core/address/docs/address.html
modules/core/status/ontology/conx-status.ttl -> modules/core/status/docs/status.html
```

OntoLens reads the ontology and generates a static review and publication view.
It does not modify domain axioms.
