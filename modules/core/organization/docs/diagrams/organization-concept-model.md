# Domain Organization Diagram

**Status:** Domain model of implemented version 0.1.0  
**As of:** 27 August 2026  
**Implementation status:** T-Box and Core Shapes 0.1.0 implemented

The model is presented from four perspectives, keeping the class hierarchy, master data, organizational parts, and process roles separately readable.

## 1. Classes and Relationships

```mermaid
flowchart TB
    subgraph AGENTS["Existing Agent types"]
        direction LR
        Agent["Agent: common superclass"]
        Person["Person: natural person"]
        Person -->|"rdfs:subClassOf"| Agent
    end

    subgraph ORGANIZATION["core/organization - MVP 0.1.0"]
        direction TB
        Org["Organization: organized collective actor"]
        Legal["LegalEntity: separate legal identity"]
        Unit["OrganizationalUnit: internal organizational unit"]

        Membership["Membership: membership relationship"]
        Representation["LegalRepresentation: legal representation relationship"]

        Legal -->|"rdfs:subClassOf"| Org
        Unit -->|"rdfs:subClassOf"| Org

        Membership -->|"member 1"| Agent
        Membership -->|"membershipOrganization 1"| Org
        Representation -->|"representedOrganization 1"| Legal
        Representation -->|"representative 1"| Person
    end

    Org -->|"rdfs:subClassOf"| Agent

    Deferred["Outside the MVP: EconomicActor / Enterprise; FormalOrganization / Post; Credential class"]
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

### How to Read the Diagram

1. `Organization` is the common local organization class.
2. `LegalEntity` and `OrganizationalUnit` are distinct specializations.
3. Membership and representation are resources rather than direct text attributes.
4. A Person may be a member or legal representative without becoming an Organization instance.

## 2. Organizational Master Data and Connections Between Modules

```mermaid
flowchart LR
    subgraph CORE["Organization core"]
        direction TB
        Legal["LegalEntity"]
        Names["Names: name 1..*; legalName 1..*; alternativeName 0..*"]
        Registration["Registration: registrationDate 1; legalForm 0..1; activity 0..*"]

        Legal --- Names
        Legal --- Registration
    end

    subgraph IDENTIFIERS["ADMS"]
        direction TB
        Identifier["adms:Identifier"]
        Notation["skos:notation 1: typed identification scheme"]
        Agency["adms:schemaAgency 0..1"]
        Identifier --> Notation
        Identifier --> Agency
    end

    subgraph ADDRESS["core/address"]
        direction TB
        LocationAssignment["LocationAssignment"]
        Address["Address"]
        LocationRole["LocationRole: Legal / Headquarters / Registration / Postal"]
        LocationAssignment -->|"assignedAddress 1"| Address
        LocationAssignment -->|"locationRole 1..*"| LocationRole
    end

    subgraph CONTACT["core/contact"]
        direction TB
        ContactPoint["ContactPoint: usage official; purpose general"]
        Website["ContactMethod: channel website; contactURI web IRI"]
        ContactPoint -->|"hasContactMethod"| Website
    end

    Legal -->|"adms:identifier 1..*"| Identifier
    Legal -->|"hasLocationAssignment 0..*"| LocationAssignment
    Legal -->|"hasContactPoint 0..*"| ContactPoint

    Note["No local properties for street, postal code, email, or homepage"]
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
    class LocationAssignment,Address,LocationRole address;
    class ContactPoint,Website contact;
    class Note note;
```

### Homepage Example

| Resource | Property | Value or Target |
| --- | --- | --- |
| `LegalEntity` | `hasContactPoint` | `ContactPoint` |
| `ContactPoint` | `contactUsage` | `official` |
| `ContactPoint` | `contactPurpose` | `general` |
| `ContactPoint` | `hasContactMethod` | `ContactMethod` |
| `ContactMethod` | `contactChannel` | `website` |
| `ContactMethod` | `contactURI` | `https://example.org/` |

The homepage is therefore represented entirely within the existing Contact model.

## 3. Organizational Unit, Location, or Legal Entity

```mermaid
flowchart TB
    Subject["Subject to be modeled"]

    LegalQuestion{"Separate legal identity and legal personality?"}
    FunctionQuestion{"Own organizational function or responsibility?"}
    PlaceQuestion{"Physical place with an address, coordinates, or access point?"}

    Legal["LegalEntity: for example, a subsidiary GmbH"]
    Unit["OrganizationalUnit: for example, procurement or a branch"]
    Place["Location resource: for example, a plant, depot, or construction site"]
    Combined["Link separate resources: for example, plant organization and plant location"]
    General["Organization: for example, a grouping or consortium without confirmed separate legal personality"]

    Subject --> LegalQuestion
    LegalQuestion -->|"yes"| Legal
    LegalQuestion -->|"no"| FunctionQuestion
    FunctionQuestion -->|"yes"| Unit
    FunctionQuestion -->|"no"| PlaceQuestion
    PlaceQuestion -->|"yes"| Place
    PlaceQuestion -->|"no, but a collective actor"| General

    Unit -.->|"additional physical place"| Combined
    Place -.->|"additional organizational function"| Combined

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

### Typical Classification

| Subject | Result |
| --- | --- |
| Subsidiary | `LegalEntity` |
| Department | `OrganizationalUnit` |
| Branch without separate legal personality | `OrganizationalUnit` plus location |
| Plant or depot | Location; additionally an Organizational Unit if it has its own function |
| Construction site | Location or project site |
| Corporate group or organizational grouping | `Organization`, not automatically `LegalEntity` |

## 4. Membership, Representation, and Process Role

```mermaid
flowchart TB
    Person["Person"]
    MemberOrg["Organization or LegalEntity as a member"]
    HostOrg["Organization: association / guild / statutory accident insurance institution"]
    Legal["LegalEntity: represented organization"]

    MembershipPerson["Membership"]
    MembershipOrg["Membership"]
    Representation["LegalRepresentation"]

    MembershipPerson -->|"member"| Person
    MembershipPerson -->|"membershipOrganization"| HostOrg
    MembershipOrg -->|"member"| MemberOrg
    MembershipOrg -->|"membershipOrganization"| HostOrg
    Representation -->|"representative"| Person
    Representation -->|"representedOrganization"| Legal

    subgraph PROCESS["Outside core/organization"]
        direction LR
        Context["Business context: delivery note / contract / project"]
        Assignment["AgentRoleAssignment"]
        Role["Role value: seller / buyer / carrier / ..."]
        Context --> Assignment
        Assignment --> Role
    end

    Assignment -->|"assignedAgent"| Person
    Assignment -->|"assignedAgent"| MemberOrg

    NoEconomicActor["No EconomicActor class: people and organizations may hold the same process roles"]
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

### Boundaries

- `Membership` describes membership in an Organization.
- `LegalRepresentation` describes legal representation of a Legal Entity.
- `AgentRoleAssignment` describes a function within a specific transaction or process.
- `Post` would describe a permanent position and is outside the MVP.

## 5. Modeling Decisions

1. `Organization` is a subclass of the existing `Agent`.
2. `LegalEntity` and `OrganizationalUnit` are not synonyms.
3. An Organizational Unit is not automatically a location; the two are linked as separate resources where required.
4. A subsidiary with its own legal identity is a `LegalEntity`, rather than merely an `OrganizationalUnit`.
5. Sole traders and freelancers remain people.
6. Economic activity is expressed through process roles; there is no local `EconomicActor` class.
7. Membership and legal representation are separate relationship resources.
8. Representation data references a Person without duplicating personal properties.
9. Membership numbers identify the Membership rather than generally identifying the member.
10. Addresses, contacts, and identifiers use existing modules and vocabularies.
11. A homepage is an official general website contact method.
12. `FormalOrganization`, `Post`, a Credential class, and jurisdiction profiles remain outside the MVP.