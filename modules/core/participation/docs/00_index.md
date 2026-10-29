# Participation Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.2.0  
**As of:** 7 October 2026  
**Scope:** `core/participation`

## 1. Overview

Participation describes an Agent's role in a domain context. Since 0.2.0, the participation can also be reached from the context through `hasParticipation`. The general roles remain separate at version 0.1.0.

## 2. Introduction for Nontechnical Readers

> “Anna is the architect in construction project A” is stored as a separate Participation. This keeps the person, role, and construction project distinct.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | Publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Domain scope |
| [Source Analysis](01_source-analysis.md) | N-ary relationships and role models |
| [Conceptual Model](03_concept-model.md) | Agent, role, and context |
| [Module Boundaries](04_module-boundaries.md) | Distinction from Membership and activities |
| [Term Catalog](05_term-catalog.md) | Classes, properties, and initial roles |
| [SHACL Requirements](06_shacl-requirements.md) | Complete rule catalog |
| [Core Shapes](07_core-shapes.md) | Executable data contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-part.ttl`
- Core Shapes: `../shapes/conx-part-core.shacl.ttl`
- HTML documentation: `participation.html`
- Reference vocabulary: general roles

## 5. Examples and Tests

The test graphs illustrate valid roles, optional periods, and errors caused by a missing Agent, missing role, or duplicate combination.

[Valid context navigation](../tests/valid/context-navigation.ttl) and [invalid context navigation](../tests/invalid/context-navigation.ttl) illustrate the additional reverse direction and its limits.

## 6. Additional Documents

The [Detailed Participation Diagram](diagrams/participation-concept-model.md) provides further integration and temporal examples.