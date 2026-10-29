# Domain-Specific SHACL Requirements of the Address Module

**Status:** Implemented\
**Version:** 0.1.0\
**As of:** 3 September 2026\
**Scope:** Address Core Shapes

## 1. Purpose

The Core Shapes check whether an address assignment is technically complete and an address is structurally described correctly.

## 2. Shape Set

The executable graph is located at `shapes/conx-addr-core.shacl.ttl` and has the stable IRI `https://www.construct-x.org/shapes/address/core`.

## 3. Core Requirements

- An `AddressAssignment` references exactly one `Address`.
- An `AddressAssignment` has at least one `AddressRole`.
- Date and text values must have the specified datatypes.
- Referenced territory resources must be appropriately typed.

## 4. Validation Failure Behavior

A violated core requirement produces a `sh:Violation`. Additional domain-specific mandatory fields belong in stricter profiles.

## 5. Valid Example

> A delivery address assignment has an address and the role “delivery address.” This is valid in the core, even if a domain-specific profile later requires additional mandatory fields.

## 6. Invalid Example

> An assignment without a linked address is invalid because it does not identify which address is to be used.

## 7. Deliberately Excluded Checks

The core does not universally require a postal code, a formatted address, or country-specific syntax.

## 8. Tests

Valid and invalid test graphs are located in `tests/valid` and `tests/invalid`. Further explanations are provided in the Core Shape documentation.