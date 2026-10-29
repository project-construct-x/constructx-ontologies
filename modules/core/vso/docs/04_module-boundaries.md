# Module Boundaries of the VSO Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/vso`

## 1. Purpose

The boundaries keep the VSO Core independent of specific domains and property standards.

## 2. Responsibilities

VSO owns the structure of property assignments. Domain modules determine which resources may carry which properties.

## 3. Dependencies

OPM provides the basic classes, QUDT provides units, and Schema.org provides the value property. These ontologies are referenced rather than imported.

## 4. Deliberate Exclusions

ISOProps identifiers, domain-specific ranges, and mandatory unit requirements are not VSO Core rules.

## 5. Illustrative Example

> VSO can express that a door has a width of 1.01 metres. A Door or Construction profile determines whether doors must have a width.

## 6. Integration Rule

Specific standards impose stricter requirements on VSO through profiles without changing the open Core contract.