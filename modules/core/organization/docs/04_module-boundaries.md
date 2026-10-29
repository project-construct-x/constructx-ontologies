# Module Boundaries of the Organization Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`

## 1. Purpose

The module boundaries separate organizational master data from contacts, addresses, people, process roles, and external evidence.

## 2. Responsibilities

| Topic | Responsible Module |
| --- | --- |
| Organization, Legal Entity, and Organizational Unit | `core/organization` |
| Natural person | `core/person` |
| General actor | `core/agent` |
| Address and address role | `core/address` |
| Contact point and contact method | `core/contact` |
| Cross-domain process role | `core/participation` |
| Identifier structure | `core/identifier` |

## 3. Dependencies

Organization specializes Agent and uses the contracts provided by Person, Address, Contact, and Identifier. External terms are referenced rather than redefined in the Organization ontology.

## 4. Deliberate Exclusions

Locations, bank accounts, credentials, insurance, and domain-specific project roles do not belong in the Organization Core.

## 5. Illustrative Example

> A GmbH has a legal name, a register identifier, a business address, and a billing contact. Only the name, registration date, and organizational structure belong directly to the Organization module.

A `LegalEntity` uses an Identifier from `core/identifier`, an Address through `core/address`, and a ContactPoint through `core/contact`.

## 6. Integration Rule

New relationships are defined where their domain meaning belongs. Organization does not copy properties from other core modules.