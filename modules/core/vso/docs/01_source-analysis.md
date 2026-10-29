# Source Analysis of the VSO Module

**Status:** Consolidated analytical baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 1 September 2026  
**Scope:** `core/vso`

## 1. Objective and Method

The analysis examined a system-neutral pattern for property assignments, values, and units.

## 2. Sources Evaluated

| Source | Contribution |
| --- | --- |
| OPM | Property and PropertyState |
| QUDT | Reusable units of measurement |
| Schema.org | Generic `schema:value` property |
| ISOProps | Separate interoperability profile |

## 3. Assessment

OPM provides a suitable basic structure. QUDT and Schema.org cover units and values without requiring VSO to introduce parallel terms.

## 4. Result

VSO adds unambiguous connections between a resource, an assignment, a property reference, and a state. External ontologies are referenced rather than imported.

## 5. Illustrative Example

> “2.80” alone is not meaningful. Combined with the property definition “Height” and the unit “Metre”, it becomes an understandable property of a wall.

Technical details of the existing implementation are provided in the [Integration Analysis](10_integration-analysis.md).
