# Agent Integration Model

**Status:** Documentation view of the implemented network version 0.1.0  
**As of:** 27 August 2026

This diagram does not describe any additional OWL axioms. It shows how `conx-agent:Agent` is currently used as a minimal superclass and which domain-specific relationships remain in other modules.

```mermaid
flowchart TB
    subgraph AGENT["core/agent"]
        Agent["Agent: common superclass"]
    end

    subgraph PERSON["core/person"]
        Person["Person: natural person"]
        PersonData["Personal data: name, birth, sex, gender, citizenship, identity evidence"]
        Person --- PersonData
    end

    subgraph ORGANIZATION["core/organization"]
        Org["Organization: organized collective actor"]
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
        LocationAssignment["LocationAssignment"]
        Address["Address"]
        LocationRole["LocationRole"]
        LocationAssignment -->|"assignedAddress"| Address
        LocationAssignment -->|"locationRole"| LocationRole
    end

    Person -->|"rdfs:subClassOf"| Agent
    Org -->|"rdfs:subClassOf"| Agent

    Person -.->|"hasContactPoint"| ContactPoint
    Org -.->|"hasContactPoint"| ContactPoint
    Person -.->|"hasLocationAssignment"| LocationAssignment
    Org -.->|"hasLocationAssignment"| LocationAssignment

    Note["No Agent properties in the MVP; Contact and Address remain unrestricted in domain"]
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
    class LocationAssignment,Address,LocationRole address;
    class Note note;
```

## How to Read the Diagram

1. `Agent` is only the common superclass, not a master data container.
2. `Person` and `Organization` are the currently implemented local specializations of Agent.
3. `hasContactPoint` belongs to `core/contact` and remains without a restrictive `rdfs:domain`.
4. `hasLocationAssignment` belongs to `core/address` and remains without a restrictive `rdfs:domain`.
5. `Membership` and `LegalRepresentation` belong to `core/organization` because they describe organizational relationships.