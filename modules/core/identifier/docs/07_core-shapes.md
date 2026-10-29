# Identifier Core Shapes

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Identifier Core Shapes

## 1. Purpose

The shape graph `https://www.construct-x.org/shapes/identifier/core` provides the reusable `conx-id-sh:ADMSIdentifierShape`.

## 2. Validated Contract

The shape requires an `adms:Identifier` resource with exactly one literal `skos:notation`. `adms:schemaAgency` remains optional and is limited to at most one `xsd:string`.

## 3. Reuse

Consuming core modules import the versioned shape graph and integrate `conx-id-sh:ADMSIdentifierShape` through their local `adms:identifier` Property Shapes. This keeps domain-specific cardinalities local while defining the structure of an identifier only once.

## 4. Illustrative Example

> The identifier “HRB 1234” is valid if it is represented as an `adms:Identifier` with exactly one `skos:notation`. Whether an organization must have such a registration identifier is determined by the Organization Shape.

## 5. Tests

Valid and invalid examples are located in `tests/valid` and `tests/invalid`.

## 6. Deliberately Excluded Checks

The Core Shape enforces neither a specific identification scheme nor a mandatory identifier for a particular domain class.