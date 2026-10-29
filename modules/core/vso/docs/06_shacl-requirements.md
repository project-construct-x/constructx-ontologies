# Domain SHACL Requirements of the VSO Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** VSO Core Shapes

## 1. Purpose

The Core Shapes validate the system-neutral contract for property assignments.

## 2. Shape Set

The graph is located at `shapes/conx-vso-core.shacl.ttl` and has the IRI `https://www.construct-x.org/shapes/vso/core`.

## 3. Core Requirements

| ID | Requirement |
| --- | --- |
| `VSO-LINK-001` | `hasProperty` references a valid assignment |
| `VSO-ASSIGN-001` | Each assignment belongs to exactly one resource |
| `VSO-ASSIGN-010` | Exactly one property reference as an IRI |
| `VSO-ASSIGN-020` | Exactly one PropertyState |
| `VSO-STATE-010` | Exactly one `schema:value` |
| `VSO-STATE-020` | At most one QUDT unit as an IRI |

## 4. Error Behavior

Each violation produces the stable code of the corresponding rule.

## 5. Valid Example

> A wall has exactly one height assignment with one state and the value 2.80 metres.

## 6. Invalid Example

> A property assignment with two states is invalid because the Core expects exactly one current state node.

## 7. Intentionally Not Checked

The resource class, property vocabulary, value datatype, and whether a unit is mandatory remain unrestricted.

## 8. Tests

The test graphs under `tests/valid` and `tests/invalid` cover all stable error codes.