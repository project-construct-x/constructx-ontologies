# Construct-X Identifier Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Identifier module provides a shared data contract for domain identifiers.
Person, Organization, and Document can use the same ADMS/SKOS pattern without
redefining identifier-value rules.

## 2. Everyday Example

> The commercial register number "HRB 1234" belongs to an organization. Its
> value and issuing agency are stored together as an Identifier resource.

The organization's web IRI and its register number remain distinct: the IRI
identifies the RDF resource, while the Identifier represents a domain key.

## 3. Scope and Boundaries

The module contains the reusable `adms:Identifier` contract, exactly one
`skos:notation`, and an optional `adms:schemaAgency`. It does not introduce a
parallel Construct-X Identifier class, prescribe identifier schemes, or decide
which identifiers a domain module requires.

## 4. Model Overview

```text
Domain resource -> adms:identifier -> adms:Identifier
                                         |
                                         +-> skos:notation
                                         +-> adms:schemaAgency (optional)
```

The identifier is a resource so that value and provenance can be described
together.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `adms:Identifier` | Reusable identifier resource |
| `adms:identifier` | Links a domain resource to its identifier |
| `skos:notation` | Carries the identifier value |
| `adms:schemaAgency` | Optionally identifies the issuing agency or scheme |

## 6. Validation in Plain Language

Every identifier resource requires exactly one non-empty `skos:notation`.
`adms:schemaAgency` is optional but may occur at most once and must reference a
resource.

> An Identifier without a notation is invalid. An Identifier with one notation
> and no schema agency is valid when the consuming module does not require one.

## 7. Dependencies

The contract reuses ADMS and SKOS directly. Person, Organization, and Document
import the versioned Identifier Shape when validating structured identifiers.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/identifier` |
| Shape prefix | `conx-id-sh` |

- [Ontology metadata](../ontology/conx-id.ttl)
- [Core Shapes](../shapes/conx-id-core.shacl.ttl)
- [HTML documentation](identifier.html)
- [Minimal identifier example](../tests/valid/minimal-identifier.ttl)
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
