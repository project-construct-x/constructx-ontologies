# Concept Diagram of the Participation Module

**Status:** Implemented Documentation View  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** `core/participation`

## 1. Core Model

```mermaid
flowchart LR
    Participation[Participation] -->|hasParticipant| Agent[Agent]
    Participation -->|hasRole| Role[Role]
    Participation -->|hasContext| Context[Domain resource]
    Context -->|"hasParticipation 0..*"| Participation
    Participation -.->|"startDate / endDate"| Period[Temporal validity]
```

## 2. Illustrative Example

> A Person is involved as the Architect in a construction project. Participation links Person, role, and construction project without conflating these concepts.

## 3. Further Details

Additional views are provided in the [Detailed Participation Diagram](diagrams/participation-concept-model.md).
