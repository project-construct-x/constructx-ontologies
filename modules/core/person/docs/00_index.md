# Person Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

## 1. Overview

Person describes the intrinsic core data of real natural persons.

## 2. Introduction for Nontechnical Readers

> A name and birth date describe a Person directly. Telephone numbers, company affiliations, and identifiers are linked information with their own data contracts.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Overview](09_confluence-overview.md) | German-language publication source for the compact module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | Person standards and modeling decisions |
| [Conceptual Model](03_concept-model.md) | Person core and connections to other modules |
| [Module Boundaries](04_module-boundaries.md) | Boundaries with Organization, Contact, and Address |
| [Term Catalog](05_term-catalog.md) | Classes, properties, and vocabularies |
| [SHACL Requirements](06_shacl-requirements.md) | Complete rule catalog |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Conceptual Diagram](08_concept-diagram.md) | Visual overview |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-person.ttl`
- Core Shapes: `../shapes/conx-person-core.shacl.ttl`
- HTML documentation: `person.html`
- Reference vocabularies: `human-sex` and `gender`

## 5. Examples and Tests

Valid graphs show minimal and complete Person instances. Invalid graphs illustrate errors involving names, datatypes, controlled values, and identifiers.

## 6. Additional Documents

The [Detailed Person Diagram](diagrams/person-concept-model.md) shows contact details and connections to other modules.
