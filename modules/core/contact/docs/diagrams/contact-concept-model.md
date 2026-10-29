# Domain Concept Diagram for Contact

**Status:** Domain model of T-Box and Core Shapes 0.1.0  
**As of:** 27 August 2026

The diagrams show the implemented contact model from five perspectives: core model, private/business contacts, postal address, reference vocabularies, and source mappings.

## 1. Core Model

```mermaid
flowchart LR
    Carrier["Entity holding contact information: conceptually an Agent"]

    subgraph CONTACT["core/contact"]
        direction LR
        Point["ContactPoint: contact information block"]
        Method["ContactMethod: one channel"]
        Usage["ContactUsage: private / business / official"]
        Purpose["ContactPurpose: general / delivery / billing / ..."]
        Channel["ContactChannel: email / phone / website / ..."]
        Platform["ContactPlatform: LinkedIn / Signal / ..."]
    end

    Carrier -->|"hasContactPoint 0..*"| Point
    Point -.->|"isContactPointFor optional"| Carrier
    Point -->|"hasContactMethod 1..*"| Method
    Point -->|"contactUsage 0..1"| Usage
    Point -->|"contactPurpose 0..*"| Purpose
    Method -->|"contactChannel 1"| Channel
    Method -->|"contactPlatform 0..1"| Platform
    Method -->|"contactValue / contactURI / usesAddressAssignment"| Value["Value or reference"]

    classDef carrier fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef vocab fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef value fill:#f1f3f4,stroke:#6b747a,color:#252a2d;

    class Carrier carrier;
    class Point,Method core;
    class Usage,Purpose,Channel,Platform vocab;
    class Value value;
```

## 2. Private and Business Contactability

```mermaid
flowchart TB
    Person["Person: conx-person:Person"]

    subgraph PRIVATE["Private contact point"]
        direction TB
        PrivatePoint["ContactPoint: usage private; purpose general"]
        PrivateEmail["ContactMethod: channel email; value max@example.org"]
        PrivateMobile["ContactMethod: channel mobilePhone; value +49 ..."]
        PrivatePostal["ContactMethod: channel postalAddress; usesAddressAssignment"]
        PrivatePoint --> PrivateEmail
        PrivatePoint --> PrivateMobile
        PrivatePoint --> PrivatePostal
    end

    subgraph BUSINESS["Business contact point"]
        direction TB
        BusinessPoint["ContactPoint: usage business; purpose delivery"]
        BusinessName["contactName: Goods Receiving Gate 4"]
        BusinessEmail["ContactMethod: channel email; value wareneingang@example.org"]
        BusinessPhone["ContactMethod: channel phone; value +49 ..."]
        BusinessPoint --> BusinessName
        BusinessPoint --> BusinessEmail
        BusinessPoint --> BusinessPhone
    end

    Person -->|"hasContactPoint"| PrivatePoint
    Person -->|"hasContactPoint"| BusinessPoint

    classDef person fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef point fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef method fill:#f7faf5,stroke:#71856a,color:#263323;
    classDef label fill:#f1f3f4,stroke:#6b747a,color:#252a2d;

    class Person person;
    class PrivatePoint,BusinessPoint point;
    class PrivateEmail,PrivateMobile,PrivatePostal,BusinessEmail,BusinessPhone method;
    class BusinessName label;
```

## 3. Postal Contact Address

```mermaid
flowchart LR
    Method["ContactMethod: channel postalAddress"]

    subgraph ADDRESS["core/address"]
        direction LR
        Assignment["AddressAssignment: role and delivery instructions"]
        Address["Address: structured address"]
        Role["AddressRole: delivery / billing / residence / ..."]
        Assignment -->|"assignedAddress"| Address
        Assignment -->|"addressRole"| Role
    end

    Method -->|"usesAddressAssignment"| Assignment

    Decision["Decision: postal contact methods reference AddressAssignment to preserve roles and delivery instructions."]
    Decision -.-> Method

    classDef contact fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef address fill:#e9f3f1,stroke:#39706a,color:#17312e;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Method contact;
    class Assignment,Address,Role address;
    class Decision note;
```

## 4. A-Box Vocabularies

```mermaid
flowchart TB
    Method["ContactMethod"]
    Point["ContactPoint"]

    subgraph CHANNEL["contact-channel"]
        direction TB
        Email["email"]
        Phone["phone"]
        Mobile["mobilePhone"]
        Fax["fax"]
        Website["website"]
        Messenger["messenger"]
        Social["socialProfile"]
        Postal["postalAddress"]
    end

    subgraph USAGE["contact-usage"]
        direction TB
        Private["private"]
        Business["business"]
        Official["official"]
    end

    subgraph PURPOSE["contact-purpose"]
        direction TB
        General["general"]
        Delivery["delivery"]
        Billing["billing"]
        Support["support"]
        Sales["sales"]
        Technical["technical"]
        Emergency["emergency"]
    end

    subgraph PLATFORM["contact-platform"]
        direction TB
        Linkedin["linkedin"]
        Instagram["instagram"]
        X["x"]
        Github["github"]
        WhatsApp["whatsapp"]
        Signal["signal"]
        Teams["microsoftTeams"]
    end

    Point -->|"contactUsage"| USAGE
    Point -->|"contactPurpose"| PURPOSE
    Method -->|"contactChannel"| CHANNEL
    Method -->|"contactPlatform"| PLATFORM

    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef vocab fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;

    class Method,Point core;
    class Email,Phone,Mobile,Fax,Website,Messenger,Social,Postal,Private,Business,Official,General,Delivery,Billing,Support,Sales,Technical,Emergency,Linkedin,Instagram,X,Github,WhatsApp,Signal,Teams vocab;
```

## 5. Source Mappings

```mermaid
flowchart LR
    UBLContact["UBL Contact"]
    UBLCommunication["UBL Communication"]
    SchemaCP["schema.org ContactPoint"]
    VCard["vCard RDF"]

    ContactPoint["conx-contact:ContactPoint"]
    ContactMethod["conx-contact:ContactMethod"]
    Vocab["SKOS vocabularies: Channel / Usage / Purpose / Platform"]
    Address["core/address"]

    UBLContact --> ContactPoint
    SchemaCP --> ContactPoint
    UBLCommunication --> ContactMethod
    VCard --> ContactMethod
    VCard --> Vocab
    UBLContact --> Vocab
    SchemaCP --> Vocab
    UBLContact -.-> Address
    VCard -.-> Address

    classDef source fill:#f2edf5,stroke:#70517d,color:#2f2135;
    classDef target fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef address fill:#e9f3f1,stroke:#39706a,color:#17312e;

    class UBLContact,UBLCommunication,SchemaCP,VCard source;
    class ContactPoint,ContactMethod,Vocab target;
    class Address address;
```

## 6. Modeling Decisions

1. `ContactPoint` is a contact information block, rather than a single telephone number field.
2. `ContactMethod` is the smallest independently validatable unit of a specific communication channel.
3. Private, business, and official usage are modeled on the contact point.
4. Delivery, billing, and support are purposes rather than usage contexts.
5. Social profiles are modeled generically and may be classified through platform resources.
6. Postal contact addresses reference `conx-addr:AddressAssignment`.
7. The inverse relationship remains optional.
8. `hasContactPoint` has no restrictive `rdfs:domain`, preventing future entities holding contact information from being unintentionally inferred as Agents.