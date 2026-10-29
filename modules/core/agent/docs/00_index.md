# Agent Core Module Documentation

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Overview

Agent provides the common superclass for people and organizations.

## 2. Introduction for Nontechnical Readers

> Here, “Agent” simply means “actor.” If a relationship can apply to both people and organizations, it may reference Agent.

The easiest starting point is the [Conceptual Model](03_concept-model.md).

## 3. Documentation Package

| Document | Content |
| --- | --- |
| [Confluence Summary](09_confluence-overview.md) | Publication source for the concise module page |
| [Scope and Competency Questions](02_scope-and-competency-questions.md) | Minimal scope and benefits |
| [Source Analysis](01_source-analysis.md) | Selection of the agent concept |
| [Conceptual Model](03_concept-model.md) | Person and Organization as subclasses of Agent |
| [Module Boundaries](04_module-boundaries.md) | Core without properties and its dependencies |
| [Term Catalog](05_term-catalog.md) | Reference for the single local class |
| [SHACL Requirements](06_shacl-requirements.md) | Rationale for not defining a dedicated shape |
| [Core Shapes](07_core-shapes.md) | Status of the validation contract |
| [Concept Diagram](08_concept-diagram.md) | Visual summary |

## 4. Technical Artifacts

- T-Box: `../ontology/conx-agent.ttl`
- Core Shapes: Not required
- HTML documentation: `agent.html`

## 5. Examples and Tests

The [Concept Diagram](08_concept-diagram.md) shows Person and Organization as specific agent types. Ontology tests verify the subclass relationship.

## 6. Additional Documents

- [Detailed Agent Specification](10_agent-specification.md)
- [Integration Diagram](diagrams/agent-integration-model.md)