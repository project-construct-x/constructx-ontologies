# Conceptual Model of the VSO Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

## 1. Purpose

The conceptual model describes the system-neutral assignment of a property and its value to a resource.

## 2. Model in Plain Language

An `AssignedProperty` is the concrete assignment of a general property definition to exactly one resource.

## 3. Terms

| Term | Meaning |
| --- | --- |
| `AssignedProperty` | Concrete property assignment |
| `PropertyState` | State containing the stored value |
| `hasPropertyReference` | Reference to the property definition |
| `hasUsedUnit` | Optional QUDT unit |

## 4. Relationships

| Source | Relationship | Target | Cardinality |
| --- | --- | --- | --- |
| Resource | `hasProperty` | `AssignedProperty` | |
| `AssignedProperty` | `hasPropertyReference` | Property definition | Exactly one |
| `AssignedProperty` | `hasPropertyState` | `PropertyState` | Exactly one |
| `PropertyState` | `schema:value` | Value | Exactly one |
| `PropertyState` | `hasUsedUnit` | Unit | Optional, at most one |

## 5. Illustrative Example

> Two walls can use the same “Height” definition but each have their own assignment and therefore different values.

## 6. Boundaries

The Core leaves the resource type, property vocabulary, and value datatype unrestricted.

## 7. Decisions

OPM, QUDT, and Schema.org terms are reused. ISOProps rules belong exclusively to the separate profile.