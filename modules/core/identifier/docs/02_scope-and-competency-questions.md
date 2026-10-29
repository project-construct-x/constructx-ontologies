# Scope and Competency Questions of the Identifier Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

## 1. Purpose

The module defines a shared minimal contract for domain-specific identifiers.

## 2. Confirmed Scope

- Identifier represented as `adms:Identifier`,
- exactly one identifier value through `skos:notation`,
- optional specification of the issuing agency,
- reusable Core Shape.

## 3. Out of Scope

The module does not determine which identifier a domain object must have. It also defines no parallel Construct-X Identifier class.

## 4. Competency Questions

1. What value does an identifier have?
2. Which identification scheme qualifies the value?
3. Which agency issued the scheme?
4. Can the same contract apply to Person, Organization, and Document?

## 5. Illustrative Example

> An organization has the registration number “HRB 1234.” The organization references a separate Identifier resource containing the value and, optionally, the issuing agency.

The organization references an Identifier containing “HRB 1234” and the issuing agency “Amtsgericht Bochum” (Bochum Local Court).

## 6. Modeling Decisions

ADMS and SKOS are reused directly. Domain modules retain responsibility for mandatory identifiers and permitted identification schemes.

## 7. Acceptance Criteria

The contract is satisfied when every Identifier resource is correctly typed and has exactly one literal notation.