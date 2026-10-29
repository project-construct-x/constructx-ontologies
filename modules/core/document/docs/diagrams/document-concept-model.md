# Domain Concept Diagram for Document

**Status:** Implemented domain target model 0.1.0  
**As of:** 1 September 2026

The diagrams show the implemented Document Core model from five perspectives: core model, contextual reference, distributions, actor roles, and module boundaries.

## 1. Core Model

```mermaid
flowchart LR
    Context["Domain context: any resource"]

    subgraph DOC["core/document"]
        direction LR
        Ref["DocumentReference: contextual reference"]
        Document["Document: document-like information object"]
        Distribution["DocumentDistribution: file / technical delivery form"]
        Type["DocumentType: controlled type"]
        Status["DocumentStatus: controlled status"]
        Metadata["Metadata: title / language / version / dates / validity"]
    end

    Context -->|"hasDocumentReference 0..*"| Ref
    Ref -->|"referencesDocument 0..1"| Document
    Ref -->|"hasDistribution 0..*"| Distribution
    Document -->|"hasDistribution 0..*"| Distribution
    Document -->|"documentType 0..1"| Type
    Document -->|"documentStatus 0..1"| Status
    Document --> Metadata

    classDef context fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef vocab fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef meta fill:#f1f3f4,stroke:#6b747a,color:#252a2d;

    class Context context;
    class Ref,Document,Distribution core;
    class Type,Status vocab;
    class Metadata meta;
```

## 2. Document Reference in a Domain Context

```mermaid
flowchart TB
    Order["Order 123: domain context"]
    Ref["DocumentReference: reference to a contract annex"]
    Doc["Document: contract annex A"]
    Pdf["DocumentDistribution: contract-annex-a.pdf"]

    Order -->|"hasDocumentReference"| Ref
    Ref -->|"referencesDocument"| Doc
    Ref -->|"hasDistribution"| Pdf
    Doc -->|"hasDistribution"| Pdf

    Note["The requirement for an order to reference particular documents belongs in a profile, rather than the Document Core."]
    Note -.-> Order

    classDef context fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Order context;
    class Ref,Doc,Pdf core;
    class Note note;
```

## 3. Distributions

```mermaid
flowchart LR
    Document["Document: inspection report"]

    subgraph DIST["Technical manifestations"]
        direction TB
        Pdf["DocumentDistribution: PDF; dcat:mediaType application/pdf"]
        Xml["DocumentDistribution: XML; dcat:mediaType application/xml"]
        Html["DocumentDistribution: HTML; dcat:mediaType text/html"]
    end

    Document -->|"hasDistribution"| Pdf
    Document -->|"hasDistribution"| Xml
    Document -->|"hasDistribution"| Html

    Dcat["DCAT-oriented separation: document content and a specific file are distinct."]
    Dcat -.-> DIST

    classDef doc fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef dist fill:#f7faf5,stroke:#71856a,color:#263323;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Document doc;
    class Pdf,Xml,Html dist;
    class Dcat note;
```

## 4. Actor Roles through Participation

```mermaid
flowchart LR
    AgentA["Organization A: Agent"]
    AgentB["Organization B: Agent"]
    PersonX["Person X: Agent"]

    subgraph PART["core/participation"]
        direction TB
        Issuer["Participation: role issuer"]
        Recipient["Participation: role recipient"]
        Author["Participation: role author"]
    end

    Document["Document: invoice or drawing"]

    AgentA --> Issuer
    AgentB --> Recipient
    PersonX --> Author
    Issuer -->|"context"| Document
    Recipient -->|"context"| Document
    Author -->|"context"| Document

    NoProps["No direct Document properties for issuer, sender, receiver, author, or publisher."]
    NoProps -.-> Document

    classDef agent fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef part fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef doc fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class AgentA,AgentB,PersonX agent;
    class Issuer,Recipient,Author part;
    class Document doc;
    class NoProps note;
```

## 5. Module Boundaries

```mermaid
flowchart LR
    DocumentCore["core/document: Document / Reference / Distribution"]
    Participation["core/participation: actor roles"]
    Prov["Provenance profile: generation / derivation / revision"]
    Evidence["Evidence/Credential profile: evidence / credential / proof"]
    Policy["Policy profile: rights / access"]
    Domain["Domain modules: domain-specific mandatory documents"]
    UBL["UBL: comparative source only"]

    Participation -->|"Roles associated with a document"| DocumentCore
    Prov -->|"Generation and derivation"| DocumentCore
    Evidence -->|"Evidence semantics"| DocumentCore
    Policy -->|"Access and rights"| DocumentCore
    Domain -->|"Requires particular references"| DocumentCore
    UBL -.->|"Comparison, no mapping"| DocumentCore

    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef related fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef external fill:#f2edf5,stroke:#70517d,color:#2f2135;

    class DocumentCore core;
    class Participation,Prov,Evidence,Policy,Domain related;
    class UBL external;
```

## 6. Modeling Decisions

1. `Document` is a dedicated Construct-X class.
2. `DocumentReference` is a separate relationship node for contextual document references.
3. `DocumentDistribution` separates specific files from document-like content.
4. Document type and document status are represented through controlled vocabularies.
5. Issuer, sender, recipient, author, and publisher are modeled through `core/participation`.
6. PROV-O is relevant only to generation, derivation, revision, and processing.
7. UBL remains a comparative source and is not introduced as a dependency.
8. Validity is optionally described through `validFrom` and `validUntil`.
9. Distributions directly use `dcat:accessURL`, `dcat:downloadURL`, and `dcat:mediaType`.