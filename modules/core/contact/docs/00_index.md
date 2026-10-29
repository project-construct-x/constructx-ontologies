# Contact Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/contact`

## 1. Overview

Contact describes contact points, specific contact methods, usage, and purpose.

## 2. Introduction for Nontechnical Readers

> A contact point may be named “Accounting” and intended for invoice-related communication. Email and telephone are individual methods of this contact point.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | Publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | Assessment of vCard, Schema.org, and UBL |
| [Conceptual Model](03_concept-model.md) | Contact point and contact method |
| [Module Boundaries](04_module-boundaries.md) | Distinction from Address and Agent |
| [Term Catalog](05_term-catalog.md) | Classes, properties, and initial values |
| [SHACL Requirements](06_shacl-requirements.md) | Complete rule catalog |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-contact.ttl`
- Core Shapes: `../shapes/conx-contact-core.shacl.ttl`
- HTML documentation: `contact.html`

## 5. Examples and Tests

Examples for email, websites, messengers, and postal contacts are located in `../tests/valid/`. `../tests/invalid/` illustrates typical structural errors.

## 6. Additional Documents

The [Detailed Contact Concept Diagram](diagrams/contact-concept-model.md) shows additional everyday scenarios and mappings from source models.