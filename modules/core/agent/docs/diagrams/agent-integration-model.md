# Agent-Integrationsmodell

**Status:** Dokumentationssicht auf den implementierten Netzwerkstand 0.1.0  
**Stand:** 27. August 2026

Dieses Diagramm beschreibt keine zusätzlichen OWL-Axiome. Es zeigt, wie
`conx-agent:Agent` aktuell als minimale Oberklasse verwendet wird und welche
fachlichen Beziehungen in anderen Modulen bleiben.

```mermaid
flowchart TB
    subgraph AGENT["core/agent"]
        Agent["Agent<br/>gemeinsame Oberklasse"]
    end

    subgraph PERSON["core/person"]
        Person["Person<br/>natürliche Person"]
        PersonData["Personendaten<br/>Name, Geburt, Sex, Gender,<br/>Staatsangehörigkeit, Identitätsnachweis"]
        Person --- PersonData
    end

    subgraph ORGANIZATION["core/organization"]
        Org["Organization<br/>organisierter kollektiver Akteur"]
        Legal["LegalEntity"]
        Unit["OrganizationalUnit"]
        Membership["Membership"]
        Representation["LegalRepresentation"]

        Legal -->|"rdfs:subClassOf"| Org
        Unit -->|"rdfs:subClassOf"| Org
        Membership -->|"member"| Agent
        Membership -->|"membershipOrganization"| Org
        Representation -->|"representative"| Person
        Representation -->|"representedOrganization"| Legal
    end

    subgraph CONTACT["core/contact"]
        ContactPoint["ContactPoint"]
        ContactMethod["ContactMethod"]
        ContactPoint -->|"hasContactMethod"| ContactMethod
    end

    subgraph ADDRESS["core/address"]
        AddressAssignment["AddressAssignment"]
        Address["Address"]
        AddressRole["AddressRole"]
        AddressAssignment -->|"assignedAddress"| Address
        AddressAssignment -->|"addressRole"| AddressRole
    end

    Person -->|"rdfs:subClassOf"| Agent
    Org -->|"rdfs:subClassOf"| Agent

    Person -.->|"hasContactPoint"| ContactPoint
    Org -.->|"hasContactPoint"| ContactPoint
    Person -.->|"hasAddressAssignment"| AddressAssignment
    Org -.->|"hasAddressAssignment"| AddressAssignment

    Note["Keine Agent-Properties im MVP<br/>Contact und Address bleiben domänenoffen"]
    Note -.-> Agent

    classDef agent fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef person fill:#f9e9e8,stroke:#99534d,color:#3d211f,stroke-width:2px;
    classDef org fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef contact fill:#f2edf5,stroke:#70517d,color:#2f2135,stroke-width:2px;
    classDef address fill:#e9f3f1,stroke:#39706a,color:#17312e,stroke-width:2px;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Agent agent;
    class Person,PersonData person;
    class Org,Legal,Unit,Membership,Representation org;
    class ContactPoint,ContactMethod contact;
    class AddressAssignment,Address,AddressRole address;
    class Note note;
```

## Leseregeln

1. `Agent` ist nur die gemeinsame Oberklasse, kein Stammdatencontainer.
2. `Person` und `Organization` sind die derzeit implementierten lokalen
   Agent-Spezialisierungen.
3. `hasContactPoint` gehört zu `core/contact` und bleibt ohne harte
   `rdfs:domain`.
4. `hasAddressAssignment` gehört zu `core/address` und bleibt ohne harte
   `rdfs:domain`.
5. `Membership` und `LegalRepresentation` gehören zu `core/organization`, weil
   sie Organisationsbeziehungen beschreiben.
