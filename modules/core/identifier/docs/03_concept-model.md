# Conceptual Model of the Identifier Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/identifier`

## 1. Purpose

The model describes the shared structure of a domain-specific identifier.

## 2. Model in Plain Language

A domain resource references an Identifier. The Identifier carries exactly one identifier value and may name the responsible scheme agency.

## 3. Terms

| Term | Meaning |
| --- | --- |
| `adms:Identifier` | Separate identifier resource |
| `adms:identifier` | Relationship from the domain object to the identifier |
| `skos:notation` | Actual identifier value |
| `adms:schemaAgency` | Optional issuing agency |

## 4. Relationships

Domain modules define which resources use `adms:identifier`. The Identifier module then checks the structure of the target value.

## 5. Illustrative Example

```turtle
ex:firma adms:identifier ex:register-id .
ex:register-id
    a adms:Identifier ;
    skos:notation "HRB 1234" ;
    adms:schemaAgency "Amtsgericht Bochum" .
```

## 6. Boundaries

A resource IRI, a domain-specific identifier, and identity evidence are distinct concepts.

## 7. Decisions

No local identifier concepts are introduced. The contract remains small and applicable across domains.