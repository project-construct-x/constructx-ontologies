# Participation Domain Diagrams

**Status:** Conceptual diagrams of the implemented version 0.3.0  
**Version:** 0.3.0  
**Scope:** `core/participation`  
**As of:** 19 November 2026

The Mermaid diagrams show the confirmed Participation model from six perspectives: the core model, separate combinations, unrestricted context, temporal validity, role vocabulary, and module boundaries.

## 1. Core Model

```mermaid
flowchart LR
    subgraph AGENT_CORE["core/agent"]
        direction TB
        Agent["Agent: person or organization"]
    end

    subgraph PARTICIPATION_CORE["core/participation"]
        direction TB
        Participation["Participation: qualified role assignment"]
        Role["Role: local SKOS class"]
        Start["startDate 0..1: xsd:date"]
        End["endDate 0..1: xsd:date"]

        Participation -->|"hasRole exactly 1"| Role
        Participation --> Start
        Participation --> End
    end

    Context["Domain context: type remains unrestricted"]

    Participation -->|"hasParticipant exactly 1"| Agent
    Participation -->|"hasContext exactly 1"| Context
    Context -->|"hasParticipation 0..*"| Participation

    Meaning["An instance asserts an assignment that currently holds or held historically."]
    Meaning -.-> Participation

    classDef agent fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef role fill:#fff4d6,stroke:#8c6d1f,color:#392d0e,stroke-width:2px;
    classDef context fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef date fill:#e9f3f1,stroke:#39706a,color:#17312e;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Agent agent;
    class Participation participation;
    class Role role;
    class Context context;
    class Start,End date;
    class Meaning note;
```

### Reading Guidelines

1. Each Participation has exactly one Agent.
2. Each Participation has exactly one role value.
3. Each Participation has exactly one context.
4. Start and end dates are optional and describe validity only.
5. The context is not restricted by a local class.

## 2. One Instance per Combination

```mermaid
flowchart TB
    AgentA["Organization A"]
    AgentB["Organization B"]
    Project["Project X: shared context"]

    P1["Participation P1"]
    P2["Participation P2"]
    P3["Participation P3"]

    Contractor["ContractorRole: contractor"]
    Supplier["SupplierRole: supplier"]

    P1 -->|"hasParticipant"| AgentA
    P1 -->|"hasRole"| Contractor
    P1 -->|"hasContext"| Project

    P2 -->|"hasParticipant"| AgentA
    P2 -->|"hasRole"| Supplier
    P2 -->|"hasContext"| Project

    P3 -->|"hasParticipant"| AgentB
    P3 -->|"hasRole"| Contractor
    P3 -->|"hasContext"| Project

    Unique["Domain key for each instance: hasParticipant + hasRole + hasContext"]
    Unique -.-> P1
    Unique -.-> P2
    Unique -.-> P3

    classDef agent fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef role fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef context fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class AgentA,AgentB agent;
    class P1,P2,P3 participation;
    class Contractor,Supplier role;
    class Project context;
    class Unique note;
```

### Meaning of the Diagram

- Organization A has two roles in the same project and therefore two Participations.
- Organization A and Organization B have the same role in the same project and therefore each have their own Participation.
- No Participation combines multiple Agents or roles.

## 3. Unrestricted Domain Context

```mermaid
flowchart LR
    Participation["Participation"]

    subgraph CONTEXTS["Possible context resources from the responsible modules"]
        direction TB
        Contract["Contract"]
        Project["Project"]
        Document["Document"]
        Delivery["Delivery note"]
        Product["Product or asset"]
        Other["Other domain resource"]
    end

    Participation -->|"hasContext exactly 1"| Contract
    Participation -.->|"alternatively"| Project
    Participation -.->|"alternatively"| Document
    Participation -.->|"alternatively"| Delivery
    Participation -.->|"alternatively"| Product
    Participation -.->|"alternatively"| Other

    NoClass["No local Context class. The applicable domain profile may restrict permitted context types."]
    NoClass -.-> Participation

    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef context fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Participation participation;
    class Contract,Project,Document,Delivery,Product,Other context;
    class NoClass note;
```

The dashed edges indicate alternatives. An individual Participation always uses exactly one of these context resources.

## 4. Optional Temporal Validity

```mermaid
flowchart LR
    UnknownStart["Start not specified"]
    Start["startDate: 2026-01-15"]
    Participation["Participation: validity of the role assignment"]
    End["endDate: 2026-12-31"]
    UnknownEnd["End not specified"]

    UnknownStart -.-> Start
    Start --> Participation
    Participation --> End
    End -.-> UnknownEnd

    Rule["If both dates are present: endDate must not precede startDate."]
    Rule -.-> Participation

    NotActivity["The dates do not delimit an activity or the duration of the context."]
    NotActivity -.-> Participation

    classDef date fill:#e9f3f1,stroke:#39706a,color:#17312e,stroke-width:2px;
    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef optional fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;
    classDef note fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;

    class Start,End date;
    class Participation participation;
    class UnknownStart,UnknownEnd optional;
    class Rule,NotActivity note;
```

### Permitted Date Combinations

| Start date | End date | Meaning |
| --- | --- | --- |
| Absent | Absent | Temporal boundaries are not specified |
| Present | Absent | The start is specified, but the end is not |
| Absent | Present | The end is specified, but the start is not |
| Present | Present | Validity is bounded at both ends |

## 5. Roles as SKOS Individuals

```mermaid
flowchart TB
    SkosConcept["skos:Concept"]
    RoleClass["conx-part:Role"]
    Scheme["Participation Role Concept Scheme: separate reference vocabulary"]

    Client["ClientRole: client"]
    Contractor["ContractorRole: contractor"]
    Supplier["SupplierRole: supplier"]
    Architect["ArchitectRole: architect"]
    Engineer["EngineerRole: engineer"]

    RoleClass -->|"rdfs:subClassOf"| SkosConcept
    Scheme -->|"skos:hasTopConcept"| Client
    Scheme -->|"skos:hasTopConcept"| Contractor
    Scheme -->|"skos:hasTopConcept"| Supplier
    Scheme -->|"skos:hasTopConcept"| Architect
    Scheme -->|"skos:hasTopConcept"| Engineer

    Client -->|"rdf:type"| RoleClass
    Contractor -->|"rdf:type"| RoleClass
    Supplier -->|"rdf:type"| RoleClass
    Architect -->|"rdf:type"| RoleClass
    Engineer -->|"rdf:type"| RoleClass

    Note["Roles are individuals. New roles extend the vocabulary, not the Participation T-Box."]
    Note -.-> Scheme

    classDef classNode fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef scheme fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef role fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class SkosConcept,RoleClass classNode;
    class Scheme scheme;
    class Client,Contractor,Supplier,Architect,Engineer role;
    class Note note;
```

The five roles shown are the proposal from the term catalog. The diagram does not yet assert that a dataset has been implemented.

## 6. Module Boundaries

```mermaid
flowchart TB
    Agent["core/agent: Agent identity"]
    Participation["core/participation: role of an Agent in a context"]
    Membership["core/organization: Membership"]
    Activity["Future activity ontology: execution and event participation"]
    ContextModule["Responsible domain module: semantics of the context resource"]
    RoleVocab["Role vocabulary: concrete role individuals"]

    Participation -->|"hasParticipant"| Agent
    Participation -->|"hasContext"| ContextModule
    Participation -->|"hasRole"| RoleVocab

    Membership -.->|"remains separate"| Participation
    Activity -.->|"no activity inference"| Participation

    Excluded["Outside the Participation module: status, evidence, provenance, power of attorney, authorization, role-specific shortcut properties"]
    Excluded -.-> Participation

    classDef external fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef separate fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef vocab fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef excluded fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Agent,ContextModule external;
    class Participation participation;
    class Membership,Activity separate;
    class RoleVocab vocab;
    class Excluded excluded;
```

## 7. Modeling Decisions

1. Participation is a qualified role assignment rather than participation in an activity.
2. Each Participation has exactly one Agent, one role, and one context.
3. The combination of these three values is unique within the domain.
4. Roles are individuals of a local, SKOS-based class.
5. Context types are defined by domain profiles rather than the Core.
6. Start and end dates are optional boundaries of assignment validity.
7. Membership and Participation remain independent.
8. The Core contains no role-specific shortcut properties, status values, or evidence values.
9. `hasParticipation` is the optional reverse relationship from the context; the three core relationships on Participation remain explicitly present.