# Scope and Competency Questions of the VSO Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

## 1. Purpose

VSO describes how a property with a concrete value is attached to a resource.

## 2. Confirmed Scope

- Property assignment to exactly one resource,
- reference to exactly one property definition,
- exactly one state object with exactly one value,
- optional unit of measurement.

## 3. Outside the Scope

VSO defines neither domain-specific property catalogs nor mandatory datatypes. ISOProps-specific rules belong to a separate profile.

## 4. Competency Questions

1. Which property has been assigned to a resource?
2. What is its current value?
3. Which unit is used?
4. To which resource does the assignment belong?

## 5. Illustrative Example

> A wall has the property “Height”. The stored value is 2.80, and the unit used is metre.

| Resource | Property assignment | State |
| --- | --- | --- |
| Wall | Height | Value: 2.80; unit: metre |

## 6. Modeling Decisions

The property definition and its concrete assignment remain separate. This allows the same definition to be used for many resources.

## 7. Acceptance Criteria

Assignment, reference, state, and value are unambiguously connected; a unit is optional.