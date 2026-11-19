# Address Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/address`

## 1. Overview

Address describes structured addresses, their assignment to resources, and the role of each assignment.

## 2. Introduction for Nontechnical Readers

> An address answers “Where?”. An AddressAssignment additionally answers “For whom?” and “For what purpose?”, such as use as a delivery address.

The easiest starting point is the [Conceptual Model](03_concept-model.md), followed by the [Concept Diagram](08_concept-diagram.md).

## 3. Documentation Package

| Document | Content |
| -------- | ------- |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope and answerable questions |
| [Source Analysis](01_source-analysis.md) | Comparison of external address models |
| [Conceptual Model](03_concept-model.md) | Classes, relationships, and decisions |
| [Module Boundaries](04_module-boundaries.md) | Distinction from Contact, Agent, and Geo |
| [Term Catalog](05_term-catalog.md) | Concise reference of terms |
| [SHACL Requirements](06_shacl-requirements.md) | Domain-specific validation rules |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |
| [Confluence Summary](09_confluence-overview.md) | German-language publication source for the concise module page |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-addr.ttl`
- Core Shapes: `../shapes/conx-addr-core.shacl.ttl`
- HTML documentation: `address.html`

## 5. Examples and Tests

The example `../examples/rub-address.ttl` shows a complete address. Positive and negative validation examples are located in `../tests/`.

## 6. Additional Documents

- [Address Roles](10_address-roles.md)
- [Administrative Territories](11_administrative-territories.md)
