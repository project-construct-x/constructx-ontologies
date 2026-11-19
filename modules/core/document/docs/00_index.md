# Document Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`

## 1. Overview

Document separates domain-level documents, contextual references, and technical file distributions.

## 2. Introduction for Nontechnical Readers

> An inspection report is the document. The PDF file is a distribution. A contract can reference the report specifically through a DocumentReference.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | German-language publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | Standards and modeling alternatives |
| [Conceptual Model](03_concept-model.md) | Document, reference, and distribution |
| [Module Boundaries](04_module-boundaries.md) | Distinction from Participation, Evidence, and rights |
| [Term Catalog](05_term-catalog.md) | Classes, properties, and vocabularies |
| [SHACL Requirements](06_shacl-requirements.md) | Domain-specific rule catalog |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-doc.ttl`
- Core Shapes: `../shapes/conx-doc-core.shacl.ttl`
- HTML documentation: `document.html`
- Reference vocabularies: document type and document status

## 5. Examples and Tests

Valid examples show complete documents and references. Invalid graphs in `../tests/invalid/` illustrate errors in metadata, identifiers, and distributions.

## 6. Additional Documents

The [Detailed Document Diagram](diagrams/document-concept-model.md) provides additional views of references, distributions, and Participation.
