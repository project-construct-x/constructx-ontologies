# Fachliche Participation-Diagramme

**Status:** Konzeptdiagramme der implementierten Version 0.1.0  
**Stand:** 27. August 2026

Die Mermaid-Diagramme zeigen das bestätigte Participation-Modell in sechs
Sichten: Kernmodell, getrennte Kombinationen, offener Kontext, zeitliche
Gültigkeit, Rollen-Vokabular und Modulgrenzen.

## 1. Kernmodell

```mermaid
flowchart LR
    subgraph AGENT_CORE["core/agent"]
        direction TB
        Agent["Agent<br/>Person oder Organisation"]
    end

    subgraph PARTICIPATION_CORE["core/participation"]
        direction TB
        Participation["Participation<br/>qualifizierte Rollenzuordnung"]
        Role["Role<br/>lokale SKOS-Klasse"]
        Start["startDate 0..1<br/>xsd:date"]
        End["endDate 0..1<br/>xsd:date"]

        Participation -->|"role genau 1"| Role
        Participation --> Start
        Participation --> End
    end

    Context["Fachlicher Kontext<br/>Typ bleibt offen"]

    Participation -->|"participant genau 1"| Agent
    Participation -->|"context genau 1"| Context

    Meaning["Eine Instanz behauptet eine<br/>tatsächlich geltende oder<br/>historisch gegoltene Zuordnung."]
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

### Leseregeln

1. Jede Participation besitzt genau einen Agenten.
2. Jede Participation besitzt genau einen Rollenwert.
3. Jede Participation besitzt genau einen Kontext.
4. Start- und Enddatum sind optional und beschreiben nur die Gültigkeit.
5. Der Kontext wird nicht durch eine lokale Klasse eingeschränkt.

## 2. Eine Instanz pro Kombination

```mermaid
flowchart TB
    AgentA["Organisation A"]
    AgentB["Organisation B"]
    Project["Projekt X<br/>gemeinsamer Kontext"]

    P1["Participation P1"]
    P2["Participation P2"]
    P3["Participation P3"]

    Contractor["ContractorRole<br/>Auftragnehmer"]
    Supplier["SupplierRole<br/>Lieferant"]

    P1 -->|"participant"| AgentA
    P1 -->|"role"| Contractor
    P1 -->|"context"| Project

    P2 -->|"participant"| AgentA
    P2 -->|"role"| Supplier
    P2 -->|"context"| Project

    P3 -->|"participant"| AgentB
    P3 -->|"role"| Contractor
    P3 -->|"context"| Project

    Unique["Fachlicher Schlüssel je Instanz:<br/>participant + role + context"]
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

### Aussage des Diagramms

- Organisation A besitzt zwei Rollen im selben Projekt und deshalb zwei
  Participations.
- Organisation A und Organisation B besitzen dieselbe Rolle im selben Projekt
  und deshalb jeweils eine eigene Participation.
- Keine Participation bündelt mehrere Agenten oder Rollen.

## 3. Offener fachlicher Kontext

```mermaid
flowchart LR
    Participation["Participation"]

    subgraph CONTEXTS["Mögliche Kontextressourcen aus zuständigen Modulen"]
        direction TB
        Contract["Vertrag"]
        Project["Projekt"]
        Document["Dokument"]
        Delivery["Lieferschein"]
        Product["Produkt oder Asset"]
        Other["Weitere fachliche Ressource"]
    end

    Participation -->|"context genau 1"| Contract
    Participation -.->|"alternativ"| Project
    Participation -.->|"alternativ"| Document
    Participation -.->|"alternativ"| Delivery
    Participation -.->|"alternativ"| Product
    Participation -.->|"alternativ"| Other

    NoClass["Keine lokale Klasse Context.<br/>Das jeweilige Fachprofil darf<br/>zulässige Kontexttypen begrenzen."]
    NoClass -.-> Participation

    classDef participation fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef context fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Participation participation;
    class Contract,Project,Document,Delivery,Product,Other context;
    class NoClass note;
```

Die gestrichelten Kanten zeigen Alternativen. Eine einzelne Participation
verwendet immer genau eine dieser Kontextressourcen.

## 4. Optionale zeitliche Gültigkeit

```mermaid
flowchart LR
    UnknownStart["Beginn nicht angegeben"]
    Start["startDate<br/>2026-01-15"]
    Participation["Participation<br/>Gültigkeit der Rollenzuordnung"]
    End["endDate<br/>2026-12-31"]
    UnknownEnd["Ende nicht angegeben"]

    UnknownStart -.-> Start
    Start --> Participation
    Participation --> End
    End -.-> UnknownEnd

    Rule["Wenn beide Daten vorhanden sind:<br/>endDate darf nicht vor startDate liegen."]
    Rule -.-> Participation

    NotActivity["Die Daten begrenzen keine Aktivität<br/>und nicht die Laufzeit des Kontexts."]
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

### Erlaubte Datumsvarianten

| Startdatum | Enddatum | Bedeutung |
| --- | --- | --- |
| fehlt | fehlt | Zeitliche Grenzen sind nicht angegeben |
| vorhanden | fehlt | Beginn ist angegeben, Ende nicht |
| fehlt | vorhanden | Ende ist angegeben, Beginn nicht |
| vorhanden | vorhanden | Gültigkeit ist beidseitig begrenzt |

## 5. Rollen als SKOS-Individuen

```mermaid
flowchart TB
    SkosConcept["skos:Concept"]
    RoleClass["conx-part:Role"]
    Scheme["Participation Role Concept Scheme<br/>separates Referenzvokabular"]

    Client["ClientRole<br/>Auftraggeber"]
    Contractor["ContractorRole<br/>Auftragnehmer"]
    Supplier["SupplierRole<br/>Lieferant"]
    Architect["ArchitectRole<br/>Architekt"]
    Engineer["EngineerRole<br/>Ingenieur"]

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

    Note["Rollen sind Individuen.<br/>Neue Rollen erweitern das Vokabular,<br/>nicht die Participation-T-Box."]
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

Die dargestellten fünf Rollen sind der Vorschlag des Begriffskatalogs. Das
Diagramm behauptet noch keinen implementierten Datensatz.

## 6. Modulgrenzen

```mermaid
flowchart TB
    Agent["core/agent<br/>Agentenidentität"]
    Participation["core/participation<br/>Rolle eines Agenten im Kontext"]
    Membership["core/organization<br/>Membership"]
    Activity["Spätere Aktivitätsontologie<br/>Ausführung und Ereignisteilnahme"]
    ContextModule["Zuständiges Fachmodul<br/>Semantik der Kontextressource"]
    RoleVocab["Rollen-Vokabular<br/>konkrete Rollenindividuen"]

    Participation -->|"participant"| Agent
    Participation -->|"context"| ContextModule
    Participation -->|"role"| RoleVocab

    Membership -.->|"bleibt getrennt"| Participation
    Activity -.->|"keine Aktivitätsinferenz"| Participation

    Excluded["Nicht im Participation-Modul:<br/>Status / Nachweis / Provenienz<br/>Vollmacht / Berechtigung<br/>rollenspezifische Kurzproperties"]
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

## 7. Modellentscheidungen

1. Participation ist eine qualifizierte Rollenzuordnung und keine
   Aktivitätsteilnahme.
2. Agent, Rolle und Kontext kommen pro Participation jeweils genau einmal vor.
3. Die Kombination aus diesen drei Werten ist fachlich eindeutig.
4. Rollen sind Individuen einer lokalen, SKOS-basierten Klasse.
5. Kontexttypen werden von Fachprofilen und nicht vom Core festgelegt.
6. Start- und Enddatum sind optionale Grenzen der Zuordnungsgültigkeit.
7. Membership und Participation bleiben unabhängig.
8. Es gibt keine rollenspezifischen Kurzproperties, Status- oder Nachweiswerte.
