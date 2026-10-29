# Construct-X Organization Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Organization module describes organizations, legal entities, internal
organizational units, memberships, and legal representations. It focuses on
organization master data and structure.

## 2. Everyday Example

> Example Construction Ltd. is a legal entity with an internal logistics unit.
> Anna Miller is a member and may legally represent the company. Organization,
> unit, membership, and representation are distinct connected resources.

Anna's personal data is not copied into the membership or representation.

## 3. Scope and Boundaries

The module contains organizations, legal entities, organizational units,
names, legal form, registration data, hierarchies, memberships, and legal
representations. It does not define intrinsic person data, address and contact
structures, general project roles, bank accounts, credentials, insurance, or
project master data.

## 4. Model Overview

```text
Agent
  +-> Organization
        +-> LegalEntity
        +-> OrganizationalUnit

Membership:          Agent -> Organization
LegalRepresentation: Person -> LegalEntity
```

Addresses, contacts, and identifiers are reused from their responsible Core
modules.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Organization` | General organization |
| `LegalEntity` | Legally registered organization |
| `OrganizationalUnit` | Internal unit of an organization |
| `Membership` | Membership of an agent in an organization |
| `LegalRepresentation` | Legal representation by a person |
| `subOrganizationOf` | General organization hierarchy |
| `unitOf` | Assigns a unit to its organization |

## 6. Validation in Plain Language

Every organization requires a name. A legal entity additionally requires a
legal name, exactly one registration date, at least one structured identifier,
and a legal address assignment. Units require their organization, while a
membership or representation requires both participating resources.

> A legal entity without a registration date violates the Core contract. An
> ordinary organization that is not a legal entity does not require one.

## 7. Dependencies

Organization specializes `core/agent` and uses persons from `core/person`.
Identifiers are validated through `core/identifier`; addresses and contacts
come from `core/address` and `core/contact`. W3C ORG, ADMS, SKOS, and
Schema.org are external reference and alignment sources.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/organization` |
| Prefix | `conx-org` |

- [Ontology](../ontology/conx-org.ttl)
- [Core Shapes](../shapes/conx-org-core.shacl.ttl)
- [HTML documentation](organization.html)
- [Complete legal entity example](../tests/valid/complete-legal-entity.ttl)
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
