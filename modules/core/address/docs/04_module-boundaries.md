# Module Boundaries of the Address Module

**Status:** Confirmed through domain review and implemented\
**Version:** 0.1.0\
**As of:** 3 September 2026\
**Scope:** `core/address`

## 1. Purpose

This document explains which statements fall within the responsibility of the Address module and when another core module is responsible.

## 2. Responsibilities

| Topic | Responsible Module |
| ----- | ------------------ |
| Street, postal code, locality, and country | `core/address` |
| Email, telephone, and postal contact channel | `core/contact` |
| Person and organization | `core/person`, `core/organization` |
| Coordinates and spatial reference systems | External geospatial/location model |
| Domain-specific identifier structure | `core/identifier` |

## 3. Dependencies

The Address module references SKOS, ADMS, and external address sources, but does not adopt their models in full. Address roles and territory lists are maintained as separate reference data.
## 4. Deliberate Exclusions

The module defines neither a contact point nor an organization nor its own coordinate system. `hasGeographicPosition` serves solely as a link to a model responsible for geographic positions.
## 5. Illustrative Example

> A postal contact method references an address assignment. This keeps email and telephone in the Contact module, while street and locality are maintained in the Address module.

```text
ContactMethod -> AddressAssignment -> Address
```
## 6. Integration Rule

Other modules use `hasAddressAssignment`; they do not duplicate local properties for street, locality, or address role.

