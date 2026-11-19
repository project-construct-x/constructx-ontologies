# Identifier Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

## 1. Overview

Identifier provides a shared ADMS/SKOS data contract for domain-specific identifiers.

## 2. Introduction for Nontechnical Readers

> An identifier consists of more than the text “HRB 1234.” It can also specify the responsible register and the identification scheme used.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | German-language publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Scope of the shared contract |
| [Source Analysis](01_source-analysis.md) | Decision to use ADMS and SKOS |
| [Conceptual Model](03_concept-model.md) | Structure of an identifier |
| [Module Boundaries](04_module-boundaries.md) | Separation of structure and domain-specific rules |
| [Term Catalog](05_term-catalog.md) | External terms used |
| [SHACL Requirements](06_shacl-requirements.md) | Three stable rule groups |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- Ontology metadata: `../ontology/conx-id.ttl`
- Core Shapes: `../shapes/conx-id-core.shacl.ttl`
- Architectural decision: [Identifier Model](../../../../docs/architecture/identifier-model.md)

## 5. Examples and Tests

`../tests/valid/` contains minimal identifiers and identifiers with a scheme agency. `../tests/invalid/` illustrates missing or multiple notations.

## 6. Additional Documents

The Identifier Scheme Vocabulary under `datasets/reference/vocabularies/` defines datatypes for specific identification schemes.
