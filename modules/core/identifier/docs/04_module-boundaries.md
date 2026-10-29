# Module Boundaries of the Identifier Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

## 1. Purpose

The boundary separates the general identifier structure from domain-specific rules.

## 2. Responsibilities

Identifier owns the type, notation, and optional scheme agency. Person, Organization, and Document determine independently whether identifiers are permitted or mandatory and how many may occur.

## 3. Dependencies

The module uses ADMS and SKOS. Consuming Core Shapes import the versioned Identifier shape graph.

## 4. Deliberate Exclusions

Credential content, cryptographic verification, trust status, and the stable IRI of a resource do not belong to the Identifier contract.

## 5. Illustrative Example

> The Identifier contract can check that “P-4711” is stored correctly. Whether every person requires a personnel number is determined by a Person or application profile.

## 6. Integration Rule

Core modules reference `conx-id-sh:ADMSIdentifierShape` rather than duplicating the notation and scheme agency rules.