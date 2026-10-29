# Construct-X Contact Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/contact`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Contact module describes how persons, organizations, and other resources
can be reached. It separates a contact point and its purpose from concrete
methods such as email, telephone, or website.

## 2. Everyday Example

> A company's accounting department can be reached by email and telephone for
> invoice questions. "Accounting" is the contact point; the email address and
> telephone number are two methods attached to it.

Usage and purpose are described separately from the contact value itself.

## 3. Scope and Boundaries

The module contains contact points, contact methods, channels, usage contexts,
purposes, and optional platform, language, and availability information. It
does not define names, organization structures, address parts, consent, or
technical reachability checks.

## 4. Model Overview

```text
Contactable resource -> ContactPoint "Accounting"
                              |       |
                              |       +-> Purpose: Invoice
                              +-> ContactMethod -> Channel: Email
                              +-> ContactMethod -> Channel: Telephone
```

A postal contact method references an existing `AddressAssignment` instead of
copying address data.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `ContactPoint` | Contact point for a particular usage context |
| `ContactMethod` | Individual communication method |
| `ContactChannel` | Channel such as email or telephone |
| `ContactUsage` | Usage such as private or business |
| `ContactPurpose` | Purpose such as invoice or support |
| `hasContactMethod` | Groups methods at a contact point |
| `contactValue` | Contains an email address or telephone number |
| `usesAddressAssignment` | Reuses an existing postal address assignment |

## 6. Validation in Plain Language

Each contact point requires at least one method. Every method has exactly one
approved channel and must provide the matching payload: text for email and
telephone, an IRI for websites, or an address assignment for postal contact.

> A website channel carrying a telephone number as plain text is invalid. A
> website method with a web IRI satisfies the Core contract, although the Core
> does not test whether the site is reachable.

## 7. Dependencies

Postal contact methods reference `core/address`. Channel, usage, purpose, and
platform come from separately versioned Construct-X vocabularies. Schema.org
and vCard are used as external reference and alignment sources.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/contact` |
| Prefix | `conx-contact` |

- [Ontology](../ontology/conx-contact.ttl)
- [Core Shapes](../shapes/conx-contact-core.shacl.ttl)
- [HTML documentation](contact.html)
- [Valid contact example](../tests/valid/business-delivery-contact.ttl)
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
