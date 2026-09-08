# Fachliches Document-Konzeptdiagramm

**Status:** Umgesetztes fachliches Zielbild 0.1.0  
**Stand:** 1. September 2026

Die Diagramme zeigen das umgesetzte Document-Core-Modell in fünf Sichten:
Kernmodell, Kontextreferenz, Distributionen, Akteursrollen und
Modulabgrenzung.

## 1. Kernmodell

```mermaid
flowchart LR
    Context["Fachlicher Kontext<br/>beliebige Ressource"]

    subgraph DOC["core/document"]
        direction LR
        Ref["DocumentReference<br/>kontextbezogene Referenz"]
        Document["Document<br/>dokumentartiges Informationsobjekt"]
        Distribution["DocumentDistribution<br/>Datei / Bereitstellung"]
        Type["DocumentType<br/>kontrollierter Typ"]
        Status["DocumentStatus<br/>kontrollierter Status"]
        Metadata["Metadaten<br/>Titel / Sprache / Version / Daten / Gültigkeit"]
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

## 2. Dokumentreferenz im fachlichen Kontext

```mermaid
flowchart TB
    Order["Bestellung 123<br/>fachlicher Kontext"]
    Ref["DocumentReference<br/>Referenz auf Vertragsanlage"]
    Doc["Document<br/>Vertragsanlage A"]
    Pdf["DocumentDistribution<br/>contract-annex-a.pdf"]

    Order -->|"hasDocumentReference"| Ref
    Ref -->|"referencesDocument"| Doc
    Ref -->|"hasDistribution"| Pdf
    Doc -->|"hasDistribution"| Pdf

    Note["Die Pflicht, dass eine Bestellung<br/>bestimmte Dokumente referenziert,<br/>gehört in ein Profil,<br/>nicht in den Document Core."]
    Note -.-> Order

    classDef context fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Order context;
    class Ref,Doc,Pdf core;
    class Note note;
```

## 3. Distributionen

```mermaid
flowchart LR
    Document["Document<br/>Prüfbericht"]

    subgraph DIST["technische Ausprägungen"]
        direction TB
        Pdf["DocumentDistribution<br/>PDF<br/>dcat:mediaType application/pdf"]
        Xml["DocumentDistribution<br/>XML<br/>dcat:mediaType application/xml"]
        Html["DocumentDistribution<br/>HTML<br/>dcat:mediaType text/html"]
    end

    Document -->|"hasDistribution"| Pdf
    Document -->|"hasDistribution"| Xml
    Document -->|"hasDistribution"| Html

    Dcat["DCAT-nahe Trennung:<br/>Dokumentinhalt und konkrete Datei<br/>sind nicht dasselbe."]
    Dcat -.-> DIST

    classDef doc fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef dist fill:#f7faf5,stroke:#71856a,color:#263323;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Document doc;
    class Pdf,Xml,Html dist;
    class Dcat note;
```

## 4. Akteursrollen über Participation

```mermaid
flowchart LR
    AgentA["Organisation A<br/>Agent"]
    AgentB["Organisation B<br/>Agent"]
    PersonX["Person X<br/>Agent"]

    subgraph PART["core/participation"]
        direction TB
        Issuer["Participation<br/>role: issuer"]
        Recipient["Participation<br/>role: recipient"]
        Author["Participation<br/>role: author"]
    end

    Document["Document<br/>Rechnung oder Plan"]

    AgentA --> Issuer
    AgentB --> Recipient
    PersonX --> Author
    Issuer -->|"context"| Document
    Recipient -->|"context"| Document
    Author -->|"context"| Document

    NoProps["Keine direkten Document-Properties<br/>für issuer, sender,<br/>receiver, author oder publisher."]
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

## 5. Modulabgrenzung

```mermaid
flowchart TB
    DocumentCore["core/document<br/>Document / Reference / Distribution"]
    Participation["core/participation<br/>Agentenrollen"]
    Prov["Provenienzprofil<br/>Erzeugung / Ableitung / Revision"]
    Evidence["Evidence-/Credential-Profil<br/>Nachweis / Credential / Proof"]
    Policy["Policy-Profil<br/>Rechte / Zugriff"]
    Domain["Domain-Module<br/>fachliche Pflichtdokumente"]
    UBL["UBL<br/>nur Vergleichsquelle"]

    Participation -->|"Rollen am Dokument"| DocumentCore
    Prov -->|"Entstehung und Ableitung"| DocumentCore
    Evidence -->|"Nachweissemantik"| DocumentCore
    Policy -->|"Zugriffs- und Rechtefragen"| DocumentCore
    Domain -->|"verpflichtet bestimmte Referenzen"| DocumentCore
    UBL -.->|"Vergleich, kein Mapping"| DocumentCore

    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef related fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef external fill:#f2edf5,stroke:#70517d,color:#2f2135;

    class DocumentCore core;
    class Participation,Prov,Evidence,Policy,Domain related;
    class UBL external;
```

## 6. Modellentscheidungen

1. `Document` ist eine eigene Construct-X-Klasse.
2. `DocumentReference` ist ein eigener Beziehungsknoten für kontextbezogene
   Dokumentverweise.
3. `DocumentDistribution` trennt konkrete Dateien vom dokumentartigen Inhalt.
4. Dokumenttyp und Dokumentstatus werden kontrollierte Vokabulare.
5. Aussteller, Sender, Empfänger, Autor und Publisher werden über
   `core/participation` modelliert.
6. PROV-O ist nur für Entstehung, Ableitung, Revision und Verarbeitung
   relevant.
7. UBL bleibt Vergleichsquelle und wird nicht als Abhängigkeit eingeführt.
8. Gültigkeit wird optional über `validFrom` und `validUntil` beschrieben.
9. Distributionen verwenden `dcat:accessURL`, `dcat:downloadURL` und
   `dcat:mediaType` direkt.
