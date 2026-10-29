# Construct-X Person Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Person module describes intrinsic core data of natural persons. It keeps
personal characteristics separate from contact methods, addresses,
organization relationships, and domain roles.

## 2. Everyday Example

> Anna Miller is described as a person with her name and date of birth. Her
> telephone number belongs to a ContactPoint, her company affiliation to a
> Membership, and her personnel number to an Identifier resource.

A telephone number can change without restructuring the person core or a
membership.

## 3. Scope and Boundaries

The module contains full name and name parts, birth information, `sex`,
`gender`, citizenship, structured identifiers, and an open link to identity
evidence. It does not contain email, telephone, address parts, memberships,
employment, project roles, credential internals, or a location model.

## 4. Model Overview

```text
Agent
  +-> Person
        +-> name and birth information
        +-> sex / gender
        +-> citizenship -> Country
        +-> adms:identifier -> Identifier
        +-> hasIdentityEvidence -> external evidence resource
```

Contact, Address, and Organization may reference a Person but remain separate
modules.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Person` | Real natural person and subclass of `Agent` |
| `fullName` | Complete display name |
| `givenName` / `familyName` | Given and family names |
| `birthDate` / `birthPlaceName` | Birth date and textual birth place |
| `sex` | Classification used for data exchange |
| `gender` | Gender identity or corresponding classification |
| `citizenship` | Legal affiliation with a country |
| `hasIdentityEvidence` | Open link to an evidence resource |

## 6. Validation in Plain Language

Each Person requires at least one full name and one given name. Text values
must not be empty. A birth date must be a complete calendar date; `sex` and
`gender` use their approved vocabularies. Citizenship points to country
resources, and identifiers follow the shared Identifier contract.

> A birth value of "1985" is invalid because a complete date is expected. The
> birth date may be omitted when the use case does not require it.

## 7. Dependencies

`Person` specializes `Agent` from `core/agent`. Identifiers are validated by
the imported Shape from `core/identifier`. Citizenship uses country reference
data, while `sex` and `gender` have separately versioned vocabularies. FOAF and
SEMIC are external reference and alignment sources.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/person` |
| Prefix | `conx-person` |

- [Ontology](../ontology/conx-person.ttl)
- [Core Shapes](../shapes/conx-person-core.shacl.ttl)
- [HTML documentation](person.html)
- [Complete person example](../tests/valid/complete-person.ttl)
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
