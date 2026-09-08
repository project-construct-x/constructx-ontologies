# Fachliches Organisationsdiagramm

**Status:** Fachliches Modell der implementierten Version 0.1.0  
**Stand:** 27. August 2026  
**Umsetzungsstand:** T-Box und Core Shapes 0.1.0 implementiert

Die Darstellung ist in vier Sichten gegliedert. Dadurch bleiben
Klassenhierarchie, Stammdaten, Organisationsteile und Prozessrollen getrennt
lesbar.

## 1. Klassen und Beziehungen

```mermaid
flowchart TB
    subgraph AGENTS["Bestehende Agententypen"]
        direction LR
        Agent["Agent<br/>gemeinsame Oberklasse"]
        Person["Person<br/>natürliche Person"]
        Person -->|"rdfs:subClassOf"| Agent
    end

    subgraph ORGANIZATION["core/organization - MVP 0.1.0"]
        direction TB
        Org["Organization<br/>organisierter kollektiver Akteur"]
        Legal["LegalEntity<br/>eigene rechtliche Identität"]
        Unit["OrganizationalUnit<br/>interne organisatorische Einheit"]

        Membership["Membership<br/>Mitgliedschaftsbeziehung"]
        Representation["LegalRepresentation<br/>rechtliche Vertretungsbeziehung"]

        Legal -->|"rdfs:subClassOf"| Org
        Unit -->|"rdfs:subClassOf"| Org

        Membership -->|"member 1"| Agent
        Membership -->|"membershipOrganization 1"| Org
        Representation -->|"representedOrganization 1"| Legal
        Representation -->|"representative 1"| Person
    end

    Org -->|"rdfs:subClassOf"| Agent

    Deferred["Nicht im MVP<br/>EconomicActor / Enterprise<br/>FormalOrganization / Post<br/>Credential-Klasse"]
    Deferred -.-> Org

    classDef agent fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef organization fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef legal fill:#fff4d6,stroke:#8c6d1f,color:#392d0e,stroke-width:2px;
    classDef unit fill:#e9f3f1,stroke:#39706a,color:#17312e,stroke-width:2px;
    classDef relation fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef deferred fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Agent,Person agent;
    class Org organization;
    class Legal legal;
    class Unit unit;
    class Membership,Representation relation;
    class Deferred deferred;
```

### Leseregeln

1. `Organization` ist die gemeinsame lokale Organisationsklasse.
2. `LegalEntity` und `OrganizationalUnit` sind unterschiedliche Spezialisierungen.
3. Mitgliedschaft und Vertretung sind Ressourcen, keine direkten Textattribute.
4. Eine Person kann Mitglied oder rechtliche Vertretung sein, ohne
   Organisationsinstanz zu werden.

## 2. Organisationsstammdaten und Modulübergänge

```mermaid
flowchart LR
    subgraph CORE["Organisationskern"]
        direction TB
        Legal["LegalEntity"]
        Names["Namen<br/>name 1..*<br/>legalName 1..*<br/>alternativeName 0..*"]
        Registration["Registrierung<br/>registrationDate 1<br/>legalForm 0..1<br/>activity 0..*"]

        Legal --- Names
        Legal --- Registration
    end

    subgraph IDENTIFIERS["ADMS"]
        direction TB
        Identifier["adms:Identifier"]
        Notation["skos:notation 1<br/>typisiertes Kennungsschema"]
        Agency["adms:schemaAgency 0..1"]
        Identifier --> Notation
        Identifier --> Agency
    end

    subgraph ADDRESS["core/address"]
        direction TB
        AddressAssignment["AddressAssignment"]
        Address["Address"]
        AddressRole["AddressRole<br/>Legal / Headquarters<br/>Registration / Postal"]
        AddressAssignment -->|"assignedAddress 1"| Address
        AddressAssignment -->|"addressRole 1..*"| AddressRole
    end

    subgraph CONTACT["core/contact"]
        direction TB
        ContactPoint["ContactPoint<br/>usage: official<br/>purpose: general"]
        Website["ContactMethod<br/>channel: website<br/>contactURI: Web-IRI"]
        ContactPoint -->|"hasContactMethod"| Website
    end

    Legal -->|"adms:identifier 1..*"| Identifier
    Legal -->|"hasAddressAssignment 0..*"| AddressAssignment
    Legal -->|"hasContactPoint 0..*"| ContactPoint

    Note["Keine lokalen Properties für<br/>Straße, PLZ, E-Mail oder Homepage"]
    Note -.-> Legal

    classDef core fill:#fff4d6,stroke:#8c6d1f,color:#392d0e,stroke-width:2px;
    classDef detail fill:#fffaf0,stroke:#9b8550,color:#3a321f;
    classDef identifier fill:#f9e9e8,stroke:#99534d,color:#3d211f;
    classDef address fill:#e9f3f1,stroke:#39706a,color:#17312e;
    classDef contact fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Legal core;
    class Names,Registration detail;
    class Identifier,Notation,Agency identifier;
    class AddressAssignment,Address,AddressRole address;
    class ContactPoint,Website contact;
    class Note note;
```

### Homepage-Beispiel

```text
LegalEntity
  -> hasContactPoint
       -> contactUsage: official
       -> contactPurpose: general
       -> hasContactMethod
            -> contactChannel: website
            -> contactURI: https://example.org/
```

Die Homepage ist damit vollständig im bestehenden Kontaktmodell abgebildet.

## 3. Organisationseinheit, Standort oder Legal Entity

```mermaid
flowchart TB
    Subject["Zu modellierender Gegenstand"]

    LegalQuestion{"Eigene rechtliche Identität<br/>und eigenes Rechtssubjekt?"}
    FunctionQuestion{"Eigene organisatorische<br/>Funktion oder Zuständigkeit?"}
    PlaceQuestion{"Physischer Ort mit Adresse,<br/>Koordinaten oder Zugang?"}

    Legal["LegalEntity<br/>z. B. Tochter-GmbH"]
    Unit["OrganizationalUnit<br/>z. B. Einkauf oder Niederlassung"]
    Place["Standortressource<br/>z. B. Werk, Depot, Baustelle"]
    Combined["Getrennte Ressourcen verknüpfen<br/>z. B. Werksorganisation + Werksstandort"]
    General["Organization<br/>z. B. Verbund oder ARGE<br/>ohne bestätigte eigene Rechtspersönlichkeit"]

    Subject --> LegalQuestion
    LegalQuestion -->|"ja"| Legal
    LegalQuestion -->|"nein"| FunctionQuestion
    FunctionQuestion -->|"ja"| Unit
    FunctionQuestion -->|"nein"| PlaceQuestion
    PlaceQuestion -->|"ja"| Place
    PlaceQuestion -->|"nein, aber kollektiver Akteur"| General

    Unit -.->|"zusätzlicher physischer Ort"| Combined
    Place -.->|"zusätzliche organisatorische Funktion"| Combined

    classDef question fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef legal fill:#fff4d6,stroke:#8c6d1f,color:#392d0e,stroke-width:2px;
    classDef unit fill:#e9f3f1,stroke:#39706a,color:#17312e,stroke-width:2px;
    classDef place fill:#f9e9e8,stroke:#99534d,color:#3d211f,stroke-width:2px;
    classDef combined fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef general fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;

    class Subject,LegalQuestion,FunctionQuestion,PlaceQuestion question;
    class Legal legal;
    class Unit unit;
    class Place place;
    class Combined combined;
    class General general;
```

### Typische Zuordnung

| Gegenstand | Ergebnis |
| --- | --- |
| Tochtergesellschaft | `LegalEntity` |
| Abteilung | `OrganizationalUnit` |
| Niederlassung ohne eigene Rechtspersönlichkeit | `OrganizationalUnit` plus Standort |
| Werk oder Depot | Standort; zusätzlich Organisationseinheit bei eigener Funktion |
| Baustelle | Standort beziehungsweise Projektort |
| Konzern oder Organisationsverbund | `Organization`, nicht automatisch `LegalEntity` |

## 4. Mitgliedschaft, Vertretung und Prozessrolle

```mermaid
flowchart TB
    Person["Person"]
    MemberOrg["Organization oder LegalEntity<br/>als Mitglied"]
    HostOrg["Organization<br/>Verband / Innung / Berufsgenossenschaft"]
    Legal["LegalEntity<br/>vertretene Organisation"]

    MembershipPerson["Membership"]
    MembershipOrg["Membership"]
    Representation["LegalRepresentation"]

    MembershipPerson -->|"member"| Person
    MembershipPerson -->|"membershipOrganization"| HostOrg
    MembershipOrg -->|"member"| MemberOrg
    MembershipOrg -->|"membershipOrganization"| HostOrg
    Representation -->|"representative"| Person
    Representation -->|"representedOrganization"| Legal

    subgraph PROCESS["Außerhalb core/organization"]
        direction LR
        Context["Geschäftskontext<br/>Lieferschein / Vertrag / Projekt"]
        Assignment["AgentRoleAssignment"]
        Role["Rollenwert<br/>seller / buyer / carrier / ..."]
        Context --> Assignment
        Assignment --> Role
    end

    Assignment -->|"assignedAgent"| Person
    Assignment -->|"assignedAgent"| MemberOrg

    NoEconomicActor["Keine Klasse EconomicActor<br/>Person und Organisation können<br/>dieselben Prozessrollen übernehmen"]
    NoEconomicActor -.-> Assignment

    classDef person fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef organization fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef legal fill:#fff4d6,stroke:#8c6d1f,color:#392d0e,stroke-width:2px;
    classDef relation fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef process fill:#f9e9e8,stroke:#99534d,color:#3d211f;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Person person;
    class MemberOrg,HostOrg organization;
    class Legal legal;
    class MembershipPerson,MembershipOrg,Representation relation;
    class Context,Assignment,Role process;
    class NoEconomicActor note;
```

### Abgrenzung

- `Membership` beschreibt Zugehörigkeit zu einer Organisation.
- `LegalRepresentation` beschreibt rechtliche Vertretung einer Legal Entity.
- `AgentRoleAssignment` beschreibt eine Funktion in einem konkreten Vorgang.
- `Post` würde eine dauerhaft eingerichtete Stelle beschreiben und ist nicht im
  MVP enthalten.

## 5. Modellentscheidungen

1. `Organization` ist Unterklasse des vorhandenen `Agent`.
2. `LegalEntity` und `OrganizationalUnit` sind keine Synonyme.
3. Eine Organisationseinheit ist nicht automatisch ein Standort; beide werden
   bei Bedarf als getrennte Ressourcen verknüpft.
4. Eine Tochtergesellschaft mit eigener rechtlicher Identität ist
   `LegalEntity`, keine bloße `OrganizationalUnit`.
5. Einzelunternehmen und Freiberufler bleiben Personen.
6. Wirtschaftliches Handeln wird über Prozessrollen ausgedrückt; es gibt keine
   lokale Klasse `EconomicActor`.
7. Mitgliedschaft und rechtliche Vertretung sind eigenständige
   Beziehungsressourcen.
8. Vertretungsdaten referenzieren eine Person und duplizieren keine
   Personeneigenschaften.
9. Mitgliedsnummern identifizieren die Membership, nicht pauschal das Mitglied.
10. Adressen, Kontakte und Identifier verwenden bestehende Module und
    Vokabulare.
11. Eine Homepage ist eine offizielle allgemeine Website-Kontaktmethode.
12. `FormalOrganization`, `Post`, Credential-Klasse und Jurisdiktionsprofile
    bleiben außerhalb des MVP.
