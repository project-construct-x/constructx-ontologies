# Domain-Specific SHACL Requirements of the Address Module

**Status:** Implemented\
**Version:** 0.2.0\
**As of:** 19 November 2026\
**Scope:** Address Core Shapes

## 1. Purpose

The Core Shapes check whether a location assignment is technically complete and an address is structurally described correctly.

## 2. Shape Set

The executable graph is located at `shapes/conx-addr-core.shacl.ttl` and has the stable IRI `https://www.construct-x.org/shapes/address/core`.

## 3. Core Requirements

- A `LocationAssignment` references an `Address`, a geographic reference (IRI or blank node), or both (at most one of each).
- A `LocationAssignment` has at least one `LocationRole`.
- Date and text values must have the specified datatypes.
- Referenced territory resources must be appropriately typed.

## 4. Validation Failure Behavior

A violated core requirement produces a `sh:Violation`. Additional domain-specific mandatory fields belong in stricter profiles.

## 5. Valid Example

> A delivery location assignment has an address and the role “delivery address.” This is valid in the core, even if a domain-specific profile later requires additional mandatory fields.

## 6. Invalid Example

> An assignment with a role but neither an address nor a geolocation fails the inclusive `sh:or` constraint.

## 7. Deliberately Excluded Checks

The core does not universally require a postal code, a formatted address, or country-specific syntax.

## 8. Tests

Valid and invalid test graphs are located in `tests/valid` and `tests/invalid`. Further explanations are provided in the Core Shape documentation.
