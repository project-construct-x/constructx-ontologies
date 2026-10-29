# Domain Conceptual Model of the Organization Ontology

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`  
**Implementation status:** T-Box and Core Shapes 0.1.0 implemented

## 1. Purpose

The conceptual model describes the organization-related core of the Construct-X ontology network. It combines the source analysis, confirmed scope decisions, and term catalog into a consistent model.

The complete diagrams are provided in the [Domain Organization Diagram](diagrams/organization-concept-model.md). Class and property details are documented in the [Term Catalog](05_term-catalog.md).

## 2. Model Core

The MVP contains five local classes:

```text
Organization
LegalEntity
OrganizationalUnit
Membership
LegalRepresentation
```

The classes represent three distinct aspects:

1. organizational identity and internal structure,
2. membership of an Agent in an Organization,
3. legal representation of a Legal Entity by a Person.

Person, Address, ContactPoint, Identifier, and process role are not redefined.

## 3. Class Hierarchy

| Class | Superclass |
| --- | --- |
| `conx-person:Person` | `conx-agent:Agent` |
| `conx-org:Organization` | `conx-agent:Agent` |
| `conx-org:LegalEntity` | `conx-org:Organization` |
| `conx-org:OrganizationalUnit` | `conx-org:Organization` |

`Organization` is the only direct local organization subclass of `Agent`. `LegalEntity` and `OrganizationalUnit` specialize `Organization`.

### 3.1 `Organization`

An organization is an organized collective actor with a common purpose or a persistently recognizable structure. The concept covers more than legally registered companies, including associations, consortia, and organizational groupings.

An organization is not automatically:

- a legal person or registered legal entity,
- economically active,
- the owner of another organization,
- a physical location,
- a seller, buyer, or other process participant.

### 3.2 `LegalEntity`

Within the local Construct-X scope, a `LegalEntity` is an organization with its own legal identity. In addition to its general name, it has a legal name and a registration date.

The local concept is narrower than external models that also treat self-employed natural persons as Legal Entities. A future subclass or mapping relationship is therefore plausible, but an `owl:equivalentClass` assertion is not justified in advance.

### 3.3 `OrganizationalUnit`

An `OrganizationalUnit` is an organizational part of a parent organization. It has its own function or responsibility, but this alone does not give it separate legal personality.

In the implemented core profile, each organizational unit requires at least one `unitOf` relationship. Multiple relationships remain possible for matrix organizations.

## 4. No General `EconomicActor`

Version 0.1.0 introduces no class `EconomicActor`, `Enterprise`, or local `EconomicOperator`.

Depending on the legal and process context, the EU concepts “enterprise” and “economic operator” also encompass natural persons, public bodies, and temporary groups. This makes them unsuitable as fixed organization subclasses.

A self-employed person therefore remains:

```text
conx-person:Person
```

In a business context, the person may act as a seller, contractor, or other economic participant through the same Agent role assignment used for an organization.

## 5. Names and Registration

### 5.1 Name Levels

| Property | Meaning | Target Class |
| --- | --- | --- |
| `name` | Generally usable organizational designation | `Organization` |
| `legalName` | Name maintained legally or in an official register | `LegalEntity` |
| `alternativeName` | Trading name, abbreviation, or other common designation | `Organization` |

Every organization requires at least one `name`. Every Legal Entity additionally requires at least one `legalName`. Both values may be identical.

Multilingual values remain possible. A complete name history with validity periods is outside the MVP.

### 5.2 Registration

`registrationDate` refers exclusively to the registration date of a `LegalEntity`. It is not equivalent to:

- founding date,
- start of economic activity,
- start of a specific membership,
- date on which an identifier was issued.

The term catalog specifies exactly one complete `xsd:date`. The [SHACL Requirements Document](06_shacl-requirements.md) confirms this requirement and covers it through valid and invalid scenarios.

### 5.3 Legal Form and Activity

`legalForm` and `activity` reference controlled concepts. The MVP does not yet establish closed value sets:

- ISO 20275/GLEIF is the preferred candidate for legal forms,
- NACE Rev. 2.1 is the preferred European candidate for activities.

A closed global list could not be justified without a jurisdiction profile. Both properties therefore remain optional in the general MVP.

## 6. Identifiers

The model exclusively uses the existing ADMS profile.

`Organization`, `LegalEntity`, `OrganizationalUnit`, and `Membership` may reference an `adms:Identifier` through `adms:identifier`. The identifier carries `skos:notation` and, optionally, `adms:schemaAgency`.

The stable resource IRI and domain-specific identifiers remain separate.

### 6.1 Identifier Categories

| Category | Examples | Modeling Note |
| --- | --- | --- |
| Legal registration | National register identifier, EUID | Future jurisdiction-specific selection |
| Tax | VAT ID, W-IdNr., national tax number | Not available for every organization |
| Financial market | LEI | Additional reliable identifier, but not universally available |
| Customs | EORI | Only for relevant parties involved in customs operations |
| Supply chain | GLN | Consider the type of resource identified |
| Technical | DID | Control of an identifier, not automatically legal identity |
| Membership | Association or guild membership number | Identifier of the `Membership` |

Version 0.1.0 does not place these schemes in a global allowlist. The implemented Core Shape checks the ADMS structure, but does not replace a national register service.

## 7. Organizational Hierarchy

The model distinguishes two relationships.

### 7.1 General Suborganization

An `Organization` references a parent `Organization` through `subOrganizationOf`.

The inverse relationship is `hasSubOrganization`. It may be used for organizational groupings, umbrella organizations, or other forms of subordination.

The relationship does not automatically mean:

- corporate ownership,
- majority control,
- inclusion in consolidated accounts,
- identical legal responsibility.

### 7.2 Organizational Unit

An `OrganizationalUnit` references a parent `Organization` through `unitOf`.

The inverse relationship is `hasUnit`. It is more specific than the general suborganization relationship and expresses that the unit is defined within the parent organization.

Both relationship pairs are intended to be modeled as inverses in OWL. The Core SHACL Profile nevertheless does not require both directions to be stored explicitly.

## 8. Organizational Unit and Location

Organization and place are modeled as independent dimensions.

| Subject | Organization Type | Location Resource |
| --- | --- | --- |
| Procurement department | `OrganizationalUnit` | Only if a separate physical place is required |
| Branch without separate legal personality | `OrganizationalUnit` | Typically yes |
| Subsidiary | `LegalEntity` | Optionally its own registered office or multiple locations |
| Plant | Often `OrganizationalUnit` | Physical plant location represented separately |
| Depot | Only if it has its own organizational function | Physical depot location represented separately |
| Construction site | Not an Organization merely because it is a place | Project or construction site location |
| Corporate group | `Organization`, if required as a separate grouping | No single mandatory location |

A resource is not used simultaneously as an organizational unit and a physical place. This allows the same unit to have multiple locations and the same location to have multiple organizational users without conflating identities.

The specific relationship to a future location class remains deferred. Addresses can already be linked to an organization or organizational unit through `conx-addr:hasAddressAssignment`.

## 9. Membership

A membership links an Agent to an Organization:

| Resource | Property | Target |
| --- | --- | --- |
| `Membership` | `member` | `Agent` |
| `Membership` | `membershipOrganization` | `Organization` |

The member may be:

- a `Person`,
- an `Organization`,
- a `LegalEntity`,
- an `OrganizationalUnit`, where permitted by the domain.

The receiving resource is always an `Organization`. Memberships in associations, guilds, or statutory accident insurance institutions can therefore use the same pattern.

A membership number is maintained as an ADMS identifier of the `Membership`. It is not interpreted as a global identifier of the member.

### 9.1 Distinction from a Post

Membership states that an Agent belongs to an Organization. A post in the sense of W3C ORG `Post`, by contrast, is a permanent position that can exist while vacant.

Since the MVP requires neither vacant positions nor complete organizational charts, it contains no `Post` class. A role value on a future Membership does not automatically require a post either.

## 10. Legal Representation

Legal representation is modeled as a separate relationship resource:

| Resource | Property | Target |
| --- | --- | --- |
| `LegalRepresentation` | `representedOrganization` | `LegalEntity` |
| `LegalRepresentation` | `representative` | `Person` |

The resource prevents duplication of personal data. In the MVP, it contains only the two required relationships.

Future extensions may add:

- representation type,
- sole or joint representation,
- validity period,
- register reference,
- external evidence resource.

These extensions are outside version 0.1.0. A direct parallel property `hasLegalRepresentative` is not initially introduced.

## 11. Address and Contact

### 11.1 Address Assignment

An organization uses the existing pattern:

| Resource | Property | Target |
| --- | --- | --- |
| `Organization` | `conx-addr:hasAddressAssignment` | `AddressAssignment` |
| `AddressAssignment` | `assignedAddress` | `Address` |
| `AddressAssignment` | `addressRole` | `AddressRole` |

The following are particularly relevant for Legal Entities:

- `LegalAddressRole`,
- `HeadquartersAddressRole`,
- `RegistrationAddressRole`,
- `PostalAddressRole`.

Street, building number, postal code, and locality are not duplicated in `core/organization`.

### 11.2 Contact and Homepage

An organization uses the existing Contact model:

| Resource | Property | Target |
| --- | --- | --- |
| `Organization` | `conx-contact:hasContactPoint` | `ContactPoint` |
| `ContactPoint` | `hasContactMethod` | `ContactMethod` |

An official homepage uses a contact point and method with:

```text
contactUsage   = contact-usage:official
contactPurpose = contact-purpose:general
contactChannel = contact-channel:website
contactURI     = official web IRI
```

No local `homepage` property is therefore required. Delivery, billing, or support contacts may be separate contact points of the same organization.

## 12. Process Roles

Business roles are modeled outside the Organization core:

| Resource | Property | Target |
| --- | --- | --- |
| `AgentRoleAssignment` | `assignedAgent` | Person or Organization |
| `AgentRoleAssignment` | `role` | Controlled role value |
| `AgentRoleAssignment` | `context` | Delivery note, consignment, contract, item, or project |

Examples of role values include seller, buyer, shipper, recipient, carrier, manufacturer, and customer.

This pattern also handles self-employed persons: they may act as sellers or contractors without being classified as organizations.

## 13. External Evidence and Assessments

The MVP introduces no dedicated Credential module. Insurance, qualifications, SME status, tax status, creditworthiness, and sanctions checks remain outside the Organization core.

In particular, the model does not assert flat Booleans such as:

- `isCompliantWithRussiaSanctions`,
- `isNotInDifficulty`,
- `isSME`,
- `isInputTaxDeductible`.

Such statements require a time, legal basis, issuer, assessed subject, and possibly validity. A future external evidence resource may be linked once a specific use case exists.

## 14. Overall Conceptual Example

```turtle
@prefix conx-org: <https://www.construct-x.org/ontology/organization#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .

ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date ;
    adms:identifier ex:bau-gmbh-register-id ;
    conx-addr:hasAddressAssignment ex:bau-gmbh-legal-address ;
    conx-contact:hasContactPoint ex:bau-gmbh-official-contact .

ex:einkauf
    a conx-org:OrganizationalUnit ;
    conx-org:name "Einkauf"@de ;
    conx-org:unitOf ex:bau-gmbh .

ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband ;
    adms:identifier ex:membership-number-4711 .

ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

The referenced Identifier, Address, Contact, and Person resources are described by their responsible models and are not duplicated here.

## 15. Implemented Model Invariants

1. Every `Organization` has at least one name.
2. Every `LegalEntity` is an `Organization` and additionally has a legal name and registration date.
3. Every `OrganizationalUnit` is an `Organization` and has at least one `unitOf` relationship.
4. Every `Membership` links exactly one Agent to exactly one Organization.
5. Every `LegalRepresentation` links exactly one Legal Entity to exactly one Person.
6. Personal data is not duplicated in an organization or representation resource.
7. Addresses and contacts are connected exclusively through their existing assignment patterns.
8. A homepage is modeled as a website contact.
9. Identifiers use ADMS; membership numbers belong to Membership.
10. Process roles are not Organization subclasses.
11. Organizational units and physical locations remain separate resources.
12. The MVP contains no `EconomicActor`, local `FormalOrganization`, `Post`, or Credential class.

## 16. Implementation Status

The complete domain-specific [SHACL Requirements Document](06_shacl-requirements.md) is derived from this model. The T-Box, shape graph, and valid and invalid test graphs are implemented for version `0.1.0`. Next steps are generated HTML documentation, network metadata, and subsequently independent alignments or stricter domain-specific profiles.