# Concept Diagram of the Address Module

**Status:** Implemented Documentation View\
**Version:** 0.2.0\
**As of:** 19 November 2026\
**Scope:** `core/address`

## 1. Core Model

```mermaid
flowchart LR
    Resource[Any resource] -->|hasLocationAssignment| Assignment[LocationAssignment]
    Assignment -->|assignedAddress 0..1| Address[Address]
    Assignment -->|locationRole 1..n| Role[LocationRole]
    Assignment -->|hasGeoReference 0..1| Position[External geographic reference]
    Address -->|hasCountry| Country
    Address -->|hasAdministrativeArea| AdministrativeArea
    Country -.->|subclass of| AdministrativeTerritory
    AdministrativeArea -.->|subclass of| AdministrativeTerritory
```

## 2. Illustrative Example

> Each assignment includes an address, a geolocation, or both. Two gates may share a street address and use separate assignments to identify their respective access points.

## 3. Further Details

The complete domain model is provided in the conceptual model.
