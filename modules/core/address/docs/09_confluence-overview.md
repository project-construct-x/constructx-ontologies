# Construct-X Address Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/address`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Address module describes structured addresses and their assignment to
persons, organizations, or other resources. An address is stored independently
of its purpose; delivery, billing, or business use is recorded on the
assignment.

## 2. Everyday Example

> A construction company uses the same address for deliveries and invoices.
> The address is created once. Two roles on the assignment explain how it may
> be used.

This avoids contradictory copies of the same street, house number, and postal
code.

## 3. Scope and Boundaries

The module contains structured address parts, address assignments, assignment
roles, countries, administrative territories, and an open link to a geographic
position. It does not define contact channels, a coordinate reference system,
person or organization master data, or country-specific postal rules.

## 4. Model Overview

```text
Resource -> AddressAssignment -> Address
                 |
                 +-> AddressRole

Address -> Country
        -> AdministrativeArea
        -> external geographic position
```

`AddressAssignment` answers "for whom and for what purpose?"; `Address`
answers "what is the address?".

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Address` | Structured address |
| `AddressAssignment` | Assignment of an address to a resource |
| `AddressRole` | Purpose of the assignment, such as delivery address |
| `Country` | Country from the reference dataset |
| `AdministrativeArea` | Administrative territory within a country |
| `assignedAddress` | Links the assignment to the address |
| `addressRole` | States one or more purposes |
| `hasGeographicPosition` | Optionally links to an external geographic model |

## 6. Validation in Plain Language

An address assignment is complete only when it references exactly one address
and has at least one role. Single-value fields must not be supplied with
conflicting values, and linked roles and territories must be resources.

> A delivery-address assignment without an address is invalid. Whether a
> delivery address must contain a postal code is decided by a domain profile,
> not by the open Core.

## 7. Dependencies

The module has no mandatory dependency on another Construct-X Core module.
Address roles and ISO and NUTS territories are versioned separately as
reference data. Contact, Person, and Organization can reuse the Address model
without copying its terms.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/address` |
| Prefix | `conx-addr` |

- [Ontology](../ontology/conx-addr.ttl)
- [Core Shapes](../shapes/conx-addr-core.shacl.ttl)
- [HTML documentation](address.html)
- [Complete data example](../examples/rub-address.ttl)
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
