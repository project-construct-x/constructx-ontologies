# Construct-X VSO Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Value Semantics Ontology describes how a property definition and a
concrete value are assigned to a resource through a domain-independent pattern.

## 2. Everyday Example

> A wall has the property "Height". The concrete assignment references the
> Height definition, contains the value 2.80, and uses the unit metre.

VSO describes how value and unit are connected. A domain profile decides
whether every wall must have a height.

## 3. Scope and Boundaries

The module contains the assignment of a property to a resource, the reference
to a property definition, a state with exactly one value, and an optional QUDT
unit. It does not contain property definitions, ISOProps identifiers and
metadata, domain-specific value ranges, or requirements for particular object
types.

## 4. Model Overview

```text
Resource -> AssignedProperty -> Property definition
                    |
                    +-> PropertyState
                           +-> schema:value
                           +-> hasUsedUnit -> optional QUDT unit
```

The assignment resource keeps the relationship extensible and separates the
general definition from a concrete value.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `AssignedProperty` | Concrete assignment of a property definition |
| `PropertyState` | State that carries the concrete value |
| `hasProperty` | Links a resource to its assignment |
| `hasPropertyReference` | Points to the property definition |
| `hasPropertyState` | Links assignment and value state |
| `schema:value` | Carries the concrete value |
| `hasUsedUnit` | Optionally points to a QUDT unit |

## 6. Validation in Plain Language

Each assignment belongs to exactly one resource, references exactly one
property definition, and has exactly one state. The state contains exactly one
value and at most one unit.

> A height assignment with two current states is invalid because the current
> value is ambiguous. A textual property without a unit can be fully valid.

## 7. Dependencies

OPM provides the basic property concepts, QUDT the units, and Schema.org the
value property. These ontologies are referenced rather than imported in full.
The separate `vso-isoprops` profile can add ISOProps rules without changing the
open VSO Core.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/vso` |
| Prefix | `conx-vso` |

- [Ontology](../ontology/conx-vso.ttl)
- [Core Shapes](../shapes/conx-vso-core.shacl.ttl)
- [HTML documentation](vso.html)
- [Measured property example](../examples/measured-property.ttl)
- [Text property example](../examples/text-property.ttl)
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
- [Integration Analysis](10_integration-analysis.md)
- [Review Report](11_review-report.md)
