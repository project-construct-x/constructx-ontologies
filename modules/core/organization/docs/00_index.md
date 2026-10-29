# Organization Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`

## 1. Overview

Organization describes organizations, legal entities, internal units, memberships, and legal representation relationships.

## 2. Introduction for Nontechnical Readers

> A GmbH is a Legal Entity. A department is an OrganizationalUnit. Membership and representation are described as separate relationships.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | Publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | Standards and register models |
| [Conceptual Model](03_concept-model.md) | Organization types and relationships |
| [Module Boundaries](04_module-boundaries.md) | Responsibilities of other core modules |
| [Term Catalog](05_term-catalog.md) | Classes and properties |
| [SHACL Requirements](06_shacl-requirements.md) | Complete rule catalog |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-org.ttl`
- Core Shapes: `../shapes/conx-org-core.shacl.ttl`
- HTML documentation: `organization.html`

## 5. Examples and Tests

Valid graphs illustrate Legal Entity, Organizational Unit, Membership, and LegalRepresentation. Invalid graphs illustrate violations of mandatory relationships.

## 6. Additional Documents

The [Detailed Organization Diagram](diagrams/organization-concept-model.md) shows master data, connections between modules, and process roles.