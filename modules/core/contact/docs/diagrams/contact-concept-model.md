# Fachliches Kontakt-Konzeptdiagramm

**Status:** Fachliches Modell der T-Box und Core Shapes 0.1.0  
**Stand:** 27. August 2026

Die Diagramme zeigen das umgesetzte Kontaktmodell in fünf Sichten: Kernmodell, private/berufliche Kontakte, postalische Adresse, Referenzvokabulare und Quellenabbildung.

## 1. Kernmodell

```mermaid
flowchart LR
    Carrier["Kontaktträger<br/>fachlich Agent"]

    subgraph CONTACT["core/contact"]
        direction LR
        Point["ContactPoint<br/>Kontaktblock"]
        Method["ContactMethod<br/>ein Kanal"]
        Usage["ContactUsage<br/>private / business / official"]
        Purpose["ContactPurpose<br/>general / delivery / billing / ..."]
        Channel["ContactChannel<br/>email / phone / website / ..."]
        Platform["ContactPlatform<br/>LinkedIn / Signal / ..."]
    end

    Carrier -->|"hasContactPoint 0..*"| Point
    Point -.->|"isContactPointFor optional"| Carrier
    Point -->|"hasContactMethod 1..*"| Method
    Point -->|"contactUsage 0..1"| Usage
    Point -->|"contactPurpose 0..*"| Purpose
    Method -->|"contactChannel 1"| Channel
    Method -->|"contactPlatform 0..1"| Platform
    Method -->|"contactValue / contactURI / usesAddressAssignment"| Value["Wert oder Referenz"]

    classDef carrier fill:#e7f0f7,stroke:#315b7d,color:#172b3a,stroke-width:2px;
    classDef core fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef vocab fill:#fff4d6,stroke:#8c6d1f,color:#392d0e;
    classDef value fill:#f1f3f4,stroke:#6b747a,color:#252a2d;

    class Carrier carrier;
    class Point,Method core;
    class Usage,Purpose,Channel,Platform vocab;
    class Value value;
```

## 2. Private und berufliche Erreichbarkeit

```mermaid
flowchart TB
    Person["Person<br/>conx-person:Person"]

    subgraph PRIVATE["Privater Kontaktpunkt"]
        direction TB
        PrivatePoint["ContactPoint<br/>usage: private<br/>purpose: general"]
        PrivateEmail["ContactMethod<br/>channel: email<br/>value: max@example.org"]
        PrivateMobile["ContactMethod<br/>channel: mobilePhone<br/>value: +49 ..."]
        PrivatePostal["ContactMethod<br/>channel: postalAddress<br/>usesAddressAssignment"]
        PrivatePoint --> PrivateEmail
        PrivatePoint --> PrivateMobile
        PrivatePoint --> PrivatePostal
    end

    subgraph BUSINESS["Beruflicher Kontaktpunkt"]
        direction TB
        BusinessPoint["ContactPoint<br/>usage: business<br/>purpose: delivery"]
        BusinessName["contactName<br/>Wareneingang Tor 4"]
        BusinessEmail["ContactMethod<br/>channel: email<br/>value: wareneingang@example.org"]
        BusinessPhone["ContactMethod<br/>channel: phone<br/>value: +49 ..."]
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

## 3. Postalische Kontaktadresse

```mermaid
flowchart LR
    Method["ContactMethod<br/>channel: postalAddress"]

    subgraph ADDRESS["core/address"]
        direction LR
        Assignment["AddressAssignment<br/>Rolle + Zustellhinweise"]
        Address["Address<br/>strukturierte Anschrift"]
        Role["AddressRole<br/>delivery / billing / residence / ..."]
        Assignment -->|"assignedAddress"| Address
        Assignment -->|"addressRole"| Role
    end

    Method -->|"usesAddressAssignment"| Assignment

    Decision["Entschieden:<br/>postalische Kontaktmethoden<br/>zeigen auf AddressAssignment,<br/>damit Rollen und Zustellhinweise<br/>erhalten bleiben."]
    Decision -.-> Method

    classDef contact fill:#edf6e9,stroke:#466b3c,color:#1d2d19,stroke-width:2px;
    classDef address fill:#e9f3f1,stroke:#39706a,color:#17312e;
    classDef note fill:#f1f3f4,stroke:#6b747a,color:#252a2d,stroke-dasharray:4 3;

    class Method contact;
    class Assignment,Address,Role address;
    class Decision note;
```

## 4. A-Box-Vokabulare

```mermaid
flowchart TB
    Method["ContactMethod"]
    Point["ContactPoint"]

    subgraph CHANNEL["contact-channel"]
        direction LR
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
        direction LR
        Private["private"]
        Business["business"]
        Official["official"]
    end

    subgraph PURPOSE["contact-purpose"]
        direction LR
        General["general"]
        Delivery["delivery"]
        Billing["billing"]
        Support["support"]
        Sales["sales"]
        Technical["technical"]
        Emergency["emergency"]
    end

    subgraph PLATFORM["contact-platform"]
        direction LR
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

## 5. Quellenabbildung

```mermaid
flowchart LR
    UBLContact["UBL Contact"]
    UBLCommunication["UBL Communication"]
    SchemaCP["schema.org ContactPoint"]
    VCard["vCard RDF"]

    ContactPoint["conx-contact:ContactPoint"]
    ContactMethod["conx-contact:ContactMethod"]
    Vocab["SKOS-Vokabulare<br/>Channel / Usage / Purpose / Platform"]
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

## 6. Modellentscheidungen

1. `ContactPoint` ist ein Kontaktblock, kein einzelnes Telefonnummernfeld.
2. `ContactMethod` ist die kleinste validierbare Einheit eines konkreten Kommunikationskanals.
3. Privat, beruflich und offiziell werden am Kontaktpunkt modelliert.
4. Lieferung, Rechnung und Support sind Zwecke und keine Nutzungskontexte.
5. Social Profiles werden generisch modelliert und können über Plattformressourcen typisiert werden.
6. Postalische Kontaktadressen referenzieren `conx-addr:AddressAssignment`.
7. Die inverse Beziehung bleibt optional.
8. `hasContactPoint` besitzt keine harte `rdfs:domain`, damit spätere Kontaktträger nicht unbeabsichtigt als Agent inferiert werden.
