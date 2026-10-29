# Term Catalog of the VSO Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

## 1. Purpose

The catalog provides a compact explanation of the public VSO terms.

## 2. Namespace

`https://www.construct-x.org/ontology/vso#` with the prefix `conx-vso`.

## 3. Classes

| Class | Meaning |
| --- | --- |
| `AssignedProperty` | Concrete assignment of a property definition |
| `PropertyState` | State carrying the concrete value |

## 4. Properties

| Property | Meaning |
| --- | --- |
| `hasProperty` | Connects a resource to an assignment |
| `hasPropertyReference` | References the property definition |
| `hasPropertyState` | Connects an assignment to a state |
| `hasUsedUnit` | Optionally references a QUDT unit |
| `schema:value` | Contains the concrete value |

## 5. Controlled Values

Units come from QUDT. VSO has no unit vocabulary of its own.

## 6. Illustrative Example

An assignment references “Height”; its state contains `2.80` and references the QUDT unit metre.

## 7. Exclusions

Domain-specific property definitions and ISOProps metadata are not local VSO terms.