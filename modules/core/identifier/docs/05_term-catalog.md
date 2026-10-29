# Term Catalog of the Identifier Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

## 1. Purpose

The catalog documents the directly reused terms.

## 2. Namespaces

The shape namespace is `https://www.construct-x.org/shapes/identifier/core#`. The domain concepts originate from ADMS and SKOS.

## 3. Classes

The module uses `adms:Identifier` and defines no local class.

## 4. Properties

| Property | Meaning |
| --- | --- |
| `adms:identifier` | Links a resource to an identifier |
| `skos:notation` | Contains the identifier value |
| `adms:schemaAgency` | Optionally names the issuing agency |

## 5. Controlled Values

Identification schemes may be designated through datatype IRIs from the separate Identifier Scheme Vocabulary.

## 6. Illustrative Example

`"DE"^^id-scheme:iso-3166-1-alpha-2` explicitly denotes an alpha-2 country code, rather than merely the text “DE.”

## 7. Exclusions

The module owns no local domain-specific identifier types and no list of permitted identifiers for each domain class.