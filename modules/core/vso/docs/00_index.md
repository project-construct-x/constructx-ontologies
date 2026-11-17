# VSO Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

## 1. Overview

VSO connects resources to concrete property assignments, states, values, and optional units.

## 2. Introduction for Nontechnical Readers

> A wall does not simply have the value “2.80”. Only the combination of the property “Height”, the value 2.80, and the unit metre is unambiguous.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | German-language publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | OPM, QUDT, and Schema.org |
| [Conceptual Model](03_concept-model.md) | Assignment, state, value, and unit |
| [Module Boundaries](04_module-boundaries.md) | Boundaries with domain and ISOProps profiles |
| [Term Catalog](05_term-catalog.md) | Classes and properties |
| [SHACL Requirements](06_shacl-requirements.md) | Stable VSO rules |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Conceptual Diagram](08_concept-diagram.md) | Visual overview |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-vso.ttl`
- Core Shapes: `../shapes/conx-vso-core.shacl.ttl`
- HTML documentation: `vso.html`

## 5. Examples and Tests

`../examples/measured-property.ttl` shows a measured value with a unit; `../examples/text-property.ttl` shows a text value without a unit. Invalid cases are located under `../tests/invalid/`.

## 6. Additional Documents

- [Integration Analysis](10_integration-analysis.md)
- [Review Report](11_review-report.md)
