# Domain-Specific SHACL Requirements of the Identifier Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Identifier Core Shapes

## 1. Purpose

The shape provides a single reusable minimal contract for Identifier resources.

## 2. Shape Set

`conx-id-sh:ADMSIdentifierShape` is located in the shape graph `https://www.construct-x.org/shapes/identifier/core`.

## 3. Core Requirements

- Type `adms:Identifier`,
- blank node or IRI,
- exactly one literal `skos:notation`,
- at most one `adms:schemaAgency` as a string.

## 4. Validation Failure Behavior

The stable error codes `ID-001` to `ID-003` distinguish typing, notation, and scheme agency.

## 5. Valid Example

A correctly typed identifier with exactly one notation is valid; the scheme agency may be omitted.

## 6. Invalid Example

> An Identifier resource with two notations is invalid because it is unclear which value represents the identifier.

## 7. Deliberately Excluded Checks

The shape checks neither domain-specific mandatory identifiers nor an allowlist of identification schemes.

## 8. Tests

The test graphs under `tests/valid` and `tests/invalid` cover all three rule groups.