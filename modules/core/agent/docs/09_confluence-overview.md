# Construct-X Agent Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Agent module provides a common superclass for actors. Persons and
organizations can therefore participate in general relationships through the
same type without losing their distinct meaning.

## 2. Everyday Example

> Anna Miller and Example Construction Ltd. can both participate in a
> contract. Anna is a person and the company is an organization, but both can
> be referenced as agents in the shared relationship.

Names and register data remain in the responsible Person and Organization
modules.

## 3. Scope and Boundaries

The module contains only the common `Agent` class and the semantic basis for
relationships that accept persons and organizations. It deliberately defines
no properties, master data, or general mandatory fields.

## 4. Model Overview

```text
                 Agent
                /     \
          Person       Organization

Participation -> participant -> Agent
```

`Agent` is the shared connection point. Concrete information remains on
`Person` or `Organization`.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Agent` | Entity that can act, bear responsibility, or participate |
| `Person` | Natural person from `core/person` |
| `Organization` | Organization from `core/organization` |

The Agent module defines no relationships itself. For example, `participant`
belongs to Participation but points to an `Agent`.

## 6. Validation in Plain Language

The Agent module intentionally has no Core Shape. A single superclass has no
meaningful mandatory fields; concrete modules validate their own data
contracts.

> Person validates the required person name, while Organization validates the
> required organization name. An Agent Shape would duplicate these rules.

## 7. Dependencies

`Agent` is conservatively aligned with `foaf:Agent` and `cv:Agent`. Person and
Organization specialize the local class, and Participation uses it as the
range for participants.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/agent` |
| Prefix | `conx-agent` |
| Core Shape | Not required |

- [Ontology](../ontology/conx-agent.ttl)
- [HTML documentation](agent.html)
- [Changelog](../CHANGELOG.md)

## 9. Further Documentation

- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Source Analysis](01_source-analysis.md)
- [Conceptual Model](03_concept-model.md)
- [Module Boundaries](04_module-boundaries.md)
- [Term Catalog](05_term-catalog.md)
- [SHACL Requirements](06_shacl-requirements.md)
- [Core Shapes Explanation](07_core-shapes.md)
- [Concept Diagram](08_concept-diagram.md)
- [Agent Specification](10_agent-specification.md)
