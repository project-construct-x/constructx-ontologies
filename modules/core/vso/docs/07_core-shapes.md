# VSO Core Shapes

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** VSO Core Shapes

## 1. Purpose

The executable shape graph operationalizes the rules defined in the [SHACL Requirements](06_shacl-requirements.md).

## 2. Validated Contracts

Validation checks the owner, property reference, state, value, and optional unit of an assignment.

## 3. Reference Graphs

Targets of `PropertyStateShape` are selected through the `PropertyState` type, `hasPropertyState`, and `hasUsedUnit`. `schema:value` alone is not a VSO marker: a quantity represented as `schema:QuantitativeValue` does not thereby become a property state. The correction dated 6 October 2026 is covered by an integration test.

OPM, QUDT, and Schema.org are referenced. Validation requires no OWL inference.

## 4. Valid Example

`examples/measured-property.ttl` shows a decimal value with a unit; `examples/text-property.ttl` shows a text value without a unit.

## 5. Invalid Example

The focused files under `tests/invalid` illustrate missing links, multiple owners, and invalid state values.

## 6. Tests

Automated PySHACL tests check valid and invalid graphs.

## 7. Intentionally Not Checked

ISOProps rules belong to the separate `vso-isoprops` profile.