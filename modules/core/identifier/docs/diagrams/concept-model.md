# Konzeptdiagramm des Identifier-Moduls

**Status:** Implementierte Dokumentationssicht  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Kernmodell

```mermaid
flowchart LR
    Resource[Fachressource] -->|adms:identifier| Identifier[adms:Identifier]
    Identifier -->|skos:notation, genau 1| Value[Kennungswert]
    Identifier -.->|schemaAgency, optional| Agency[Herausgebende Stelle]
```

## 2. Lesebeispiel

> Die Organisation verweist auf eine Kennungsressource. Dort stehen die
> eigentliche Registernummer und optional das verantwortliche Register.

## 3. Vertiefung

Details stehen im [Konzeptmodell](../concept-model.md).
