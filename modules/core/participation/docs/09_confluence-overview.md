# Construct-X Participation Core Module

**Status:** Approved Confluence summary  
**Version:** 0.2.0  
**As of:** 7 October 2026  
**Scope:** `core/participation`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Participation module describes an agent holding a particular role in a
domain context. The context remains open and may be a contract, document, or
another domain resource.

## 2. Everyday Example

> Anna Miller participates in a construction project as an architect. Anna is
> the participant, "Architect" is the role, and the project is the context.
> The start and end of the assignment may also be recorded.

A second role for Anna in the same context is represented by a second
Participation.

## 3. Scope and Boundaries

The module contains the qualified relationship between agent, role, and
context, a SKOS-based Role class, and optional validity dates. It does not
contain actor master data, the definition of the context, activities,
permissions, memberships, provenance, evidence, or merely planned roles.

## 4. Model Overview

```text
Agent <- participant - Participation - context -> Domain context
                              |
                              +-> role -> Role
                              +-> startDate / endDate
```

A Participation represents exactly one agent-role-context combination. The
context may additionally point to it through `hasParticipation`.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Participation` | Current or historical role assignment |
| `Role` | Controlled description of a role |
| `participant` | References exactly one agent |
| `role` | References exactly one role |
| `context` | References exactly one domain context |
| `hasParticipation` | Optional navigation from context to participation |
| `startDate` / `endDate` | Optional validity interval |

## 6. Validation in Plain Language

Each Participation requires exactly one agent, role, and context. Start and end
dates may occur at most once, and the start must not be after the end. The same
combination must not occur twice in the validated data graph. When
`hasParticipation` is used, the target Participation must explicitly name the
same context.

> "Anna is an architect" is incomplete when the context is missing. The
> construction project makes clear where the role applies.

## 7. Dependencies

`participant` points to `Agent` from `core/agent`. Roles are based on SKOS, and
general starter roles are maintained in a separately versioned vocabulary.
Person, Organization, Document, and domain models can use Participation
without becoming mandatory T-Box imports.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.2.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/participation` |
| Prefix | `conx-part` |

- [Ontology](../ontology/conx-part.ttl)
- [Core Shapes](../shapes/conx-part-core.shacl.ttl)
- [HTML documentation](participation.html)
- [Dated participation example](../tests/valid/dated-participation.ttl)
- [Changelog](../CHANGELOG.md)

## 9. Further Documentation

- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Source Analysis](01_source-analysis.md)
- [Conceptual Model](03_concept-model.md)
- [Module Boundaries](04_module-boundaries.md)
- [Term Catalog](05_term-catalog.md)
- [SHACL Requirements](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Concept Diagram](08_concept-diagram.md)
