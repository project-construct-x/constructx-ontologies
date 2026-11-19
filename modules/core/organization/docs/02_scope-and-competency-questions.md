# Scope and Competency Questions of the Organization Ontology

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`  
**Implementation status:** T-Box and Core Shapes 0.1.0 implemented

## 1. Purpose

The Organization ontology describes organizations, legally registered organizations, internal organizational units, memberships, and legal representation. It provides organizational master data without duplicating person, address, contact, payment, process-role, or evidence models.

This document defines the domain scope and competency questions of the MVP. The associated [Term Catalog](05_term-catalog.md) documents the implemented classes and properties. The domain rationale is provided in the [Source Analysis](01_source-analysis.md).

## 2. Confirmed Scope

| Area | MVP Decision |
| --- | --- |
| General organization | `Organization` as an organized collective actor and subclass of `conx-agent:Agent` |
| Legally registered organization | `LegalEntity` as a subclass of `Organization` |
| Organizational unit | `OrganizationalUnit` for departments, divisions, and comparable units within an organization |
| Economic actor | No local class `EconomicActor`, `Enterprise`, or `EconomicOperator` in the Organization core |
| Sole traders and freelancers | Remain natural persons and may act economically through contextual Agent roles |
| Formal organization | No local class `FormalOrganization`; assess external W3C ORG alignment later |
| Names | General name, legal name, and alternative name |
| Legal form | Optional reference to a controlled legal-form concept; specific value set not yet closed |
| Registration | `registrationDate` for registration of a `LegalEntity` |
| Activity | Optional reference to a controlled activity classification; NACE is the preferred European source, but is not fixed as the MVP value set |
| Identifiers | Reuse of ADMS; no local Identifier class or universal mandatory list of specific schemes |
| Hierarchy | General parent/subordinate relationship and specific affiliation of an `OrganizationalUnit` |
| Membership | Separate relationship resource between an `Agent` and an `Organization` |
| Post / `Post` | Outside the MVP; introduced only when permanent positions that may also be vacant are required |
| Legal representation | Separate relationship resource from `LegalEntity` to `Person` in the Organization module |
| Address | Reuse of `core/address` and its `LocationAssignment` pattern |
| Contact and homepage | Reuse of `core/contact`; homepage as an official general website contact |
| Process roles | Seller, buyer, shipper, recipient, carrier, and similar roles remain contextual Agent roles outside the Organization core |
| Evidence | No dedicated Credential module in the MVP; external evidence is not modeled in detail |
| Jurisdictions | No national or European allowlists or verification profiles in the MVP |

## 3. Domain Target Model

| Class | Superclass |
| --- | --- |
| `Person` | `Agent` |
| `Organization` | `Agent` |
| `LegalEntity` | `Organization` |
| `OrganizationalUnit` | `Organization` |

| Resource | Property | Target |
| --- | --- | --- |
| `Membership` | `member` | `Agent` |
| `Membership` | `membershipOrganization` | `Organization` |
| `LegalRepresentation` | `representedOrganization` | `LegalEntity` |
| `LegalRepresentation` | `representative` | `Person` |
| `Organization` | `hasLocationAssignment` | `LocationAssignment`, which references an `Address` |
| `Organization` | `hasContactPoint` | `ContactPoint`, which references a `ContactMethod` |

This representation shows domain-level connections. The core modules and external terms used are documented in `module.yaml` as resolved references without `owl:imports`; the shapes are loaded together for integration checks.

## 4. Competency Questions

### OCQ-01: How is an organization referenced unambiguously?

Every organization receives a stable IRI in its data holder's namespace. The resource IRI must be distinguished from domain-specific identifiers. An organization may have zero or more `adms:Identifier` resources.

The model must support:

- the same organization with multiple identifiers,
- identifiers from different schemes and jurisdictions,
- the responsible scheme agency,
- identifiers of an organizational unit or membership,
- separation of global, register-related, and contextually assigned identifiers.

### OCQ-02: What distinguishes `Organization`, `LegalEntity`, and `OrganizationalUnit`?

`Organization` is the general concept for a structured collective actor. Within the local scope, `LegalEntity` denotes an organization with its own legal identity. `OrganizationalUnit` denotes an organizational part that is meaningful only in relation to at least one parent organization.

A subsidiary with its own legal personality is a `LegalEntity`. A procurement department is an `OrganizationalUnit`. A corporate group or consortium may be an `Organization` without automatically being a `LegalEntity`.

### OCQ-03: How are sole traders and freelancers handled?

A self-employed natural person remains a `conx-person:Person`. Economic activity alone does not cause the person to be typed as an `Organization` or local `LegalEntity`.

Within a delivery, contract, or procurement context, the person may act as a seller, contractor, or economic operator through an Agent role assignment. Business identifiers, contacts, and location assignments may be linked to the person without creating a second artificial organization.

A future `BusinessProfile` resource should be considered only if several separate business activities, trading names, or public business identities of the same person must be distinguished. It is outside version 0.1.0.

### OCQ-04: How are organization names distinguished?

The MVP distinguishes:

- `name` as a generally usable designation of an organization,
- `legalName` as the official or legally maintained name of a `LegalEntity`,
- `alternativeName` for trading names, abbreviations, and other common designations.

`name` is mandatory for every organization. `legalName` is additionally mandatory for every `LegalEntity`. Multilingual names may be provided multiple times; future shapes may restrict each language to at most one preferred value of the same kind if this requirement is confirmed.

### OCQ-05: How is legal form represented?

Legal form is modeled as a reference to a controlled concept rather than solely as a free-text string. GLEIF/ISO 20275 is the preferred international source. Since the MVP defines no jurisdiction profiles, the specific value set is not yet closed.

Legal form belongs only to `LegalEntity`. It is not required in the general Organization Core and remains optional in the Legal Entity Core Shape.

### OCQ-06: Which identifiers belong to an organization?

All identifiers use the existing ADMS pattern. An organization or relationship resource references an `adms:Identifier` through `adms:identifier`; the identifier carries `skos:notation` and, optionally, `adms:schemaAgency`.

A fixed global list of VAT ID, LEI, EUID, EORI, and GLN would be incorrect. These schemes have different scopes:

- national register identifier or EUID for legal registration,
- VAT ID for VAT contexts,
- LEI for LEI-registered entities,
- EORI for customs operations,
- GLN for GS1-identified legal entities, functions, or locations,
- DID for technical control, rather than sole proof of legal identity.

Version 0.1.0 therefore checks the ADMS structure but not a jurisdiction-dependent allowlist. Business-partner-specific customer, supplier, tenant, or location numbers belong to the respective relationship or process resource rather than generally to the organization.

### OCQ-07: How are organizational units and locations separated?

The decision follows two independent questions:

1. Does the resource have organizational responsibility, management, or function?
2. Does the resource describe a physical place with an address or coordinates?

A department is only an `OrganizationalUnit`. A construction site is primarily a location or project site. A plant or depot may consist of two linked resources: an organizational unit and a location.

A branch without separate legal personality is typically an `OrganizationalUnit` with a location and possibly its own register identifier. A subsidiary with separate legal personality, by contrast, is a `LegalEntity`, even if it occupies the same location.

### OCQ-08: How are organizational hierarchies represented?

`subOrganizationOf` and its inverse `hasSubOrganization` are implemented for general relationships between organizations. They express organizational subordination, but not automatically ownership, corporate control, or consolidated accounting relationships.

For an `OrganizationalUnit`, the more specific `unitOf` relationship and its inverse `hasUnit` are used. In the core profile, each `OrganizationalUnit` must be assigned to at least one parent `Organization`. Multiple assignments are not categorically prohibited in the domain model, so matrix organizations remain possible.

### OCQ-09: How is membership modeled?

Membership is a separate relationship between an `Agent` and an `Organization`:

| Resource | Property | Target |
| --- | --- | --- |
| `Membership` | `member` | `Agent` |
| `Membership` | `membershipOrganization` | `Organization` |

The `member` may be a person or an organization. This also supports membership in an association, guild, or statutory accident insurance institution. A membership number is modeled as an `adms:Identifier` of the `Membership` because it identifies the specific membership within the receiving organization's system.

Membership role, status, and period are plausible extensions, but will only be assessed as binding requirements when defining SHACL and subsequent development stages.

### OCQ-10: What is a post, and why is it outside the MVP?

A post in the sense of W3C ORG `Post` is a permanent position within an organization, such as “Head of Procurement.” Its holder may change, or it may temporarily be vacant. It therefore differs from membership, a role value, a job title, or legal representation.

The current Construct-X use case requires neither independently referenceable vacant positions nor complete organizational charts. `Post` and local post properties are therefore deferred to a later development stage.

### OCQ-11: How is legal representation modeled?

Legal representation is modeled in the Organization module as a separate relationship resource:

| Resource | Property | Target |
| --- | --- | --- |
| `LegalRepresentation` | `representedOrganization` | `LegalEntity` |
| `LegalRepresentation` | `representative` | `Person` |

The representation resource contains no copies of title, given name, family name, date of birth, or place of birth. These remain exclusively on the referenced person. Representation type, validity, sole/joint representation, and evidence may be added later without changing the basic pattern.

A simple direct property `hasLegalRepresentative` is not required as a second parallel data direction in the MVP because it would bypass the relationship resource and omit future metadata.

### OCQ-12: How are organization addresses represented?

The organization uses `conx-addr:hasLocationAssignment`. Address components remain entirely within `core/address`. Relevant address roles include:

- `roles:LegalAddressRole`,
- `roles:HeadquartersAddressRole`,
- `roles:RegistrationAddressRole`,
- `roles:PostalAddressRole`.

The same address may have multiple roles through one assignment. A Legal Entity self-description may later require at least one legal address without expressing this cardinality as an OWL truth for every organization.

### OCQ-13: How are contact information and homepages represented?

The organization references existing contact points through `conx-contact:hasContactPoint`. An official homepage is modeled without introducing a new Organization property:

| Resource | Property | Value or Target |
| --- | --- | --- |
| `Organization` | `hasContactPoint` | `ContactPoint` |
| `ContactPoint` | `contactUsage` | `official` |
| `ContactPoint` | `contactPurpose` | `general` |
| `ContactPoint` | `hasContactMethod` | `ContactMethod` |
| `ContactMethod` | `contactChannel` | `website` |
| `ContactMethod` | `contactURI` | Official web IRI |

Role-specific delivery, billing, support, or sales contacts may use additional contact points. Contact values are not copied into the organization.

### OCQ-14: How are sellers, buyers, and other business roles represented?

Seller, buyer, shipper, recipient, carrier, manufacturer, and customer are not subclasses of `Organization`. They are connected to the relevant delivery note, contract, item, project, or other context through an Agent role assignment.

The same organization can therefore hold several roles in the same transaction. A natural person may also act as an economic actor without being typed as an organization.

### OCQ-15: Which date and activity concepts belong in the MVP?

`registrationDate` describes the registration date of a `LegalEntity`. It replaces the ambiguous concept “start of activity.” `foundingDate` and `activityStartDate` are not introduced in the MVP.

An economic activity may optionally reference a controlled concept. NACE Rev. 2.1 is the preferred reference for European data, but does not become a closed MVP value set without an approved jurisdiction profile.

### OCQ-16: How are insurance, qualifications, and compliance handled?

Insurance, professional qualifications, SME status, tax status, creditworthiness, and sanctions checks are not permanent intrinsic organization properties. The Organization module introduces neither simple Booleans nor a dedicated Credential module for them.

Such statements may later be referenced as external, dated evidence or assessment resources. The specific model will be established only upon a confirmed cross-module use case.

### OCQ-17: What does the SHACL requirements document specify?

The [SHACL Requirements Document](06_shacl-requirements.md) specifies in particular:

- minimum and maximum cardinalities for name and legal name,
- mandatory status and datatype of `registrationDate`,
- minimum information for a `LegalEntity`,
- structure and permitted values of an organizational hierarchy,
- minimum information for `Membership` and `LegalRepresentation`,
- requirements for ADMS identifiers without a jurisdiction-specific allowlist,
- reuse of existing Address and Contact Shapes,
- valid and invalid scenarios for every class and relationship.

## 5. Module Boundaries

| Module | Responsibility in the Integrated Model |
| --- | --- |
| `core/agent` | Common superclass of Person and Organization |
| `core/organization` | Organization, Legal Entity, Organizational Unit, hierarchy, membership, and legal representation |
| `core/person` | Natural person; target of the representation relationship and possible member |
| `core/address` | Address, LocationAssignment, and address roles |
| `core/contact` | Contact point, contact method, usage, purpose, and homepage |
| Domain/Participation model | Seller, buyer, delivery, project, and contract roles |
| External evidence systems | Insurance, qualifications, compliance, register comparison, and other evidence |

## 6. Explicitly Outside the Organization Core

- Natural person data,
- a class `EconomicActor`, `Enterprise`, or local `EconomicOperator`,
- local `FormalOrganization` and `Post`,
- staffing plans and complete organizational charts,
- locations, geometries, and address components,
- email, telephone, website, and other contact values,
- buyer, seller, manufacturer, transport, and project roles,
- bank accounts, IBAN, BIC, and account holder,
- ownership, shareholding, and control percentages,
- beneficial owners,
- power-of-attorney texts and detailed representation rules,
- insurance, qualification, and compliance evidence,
- credit ratings and credit scores,
- national register and validation services,
- general provenance and histories of individual statements.

These exclusions do not prevent links to external resources. They establish that the Organization module is not responsible for their semantics.

## 7. Nonblocking Follow-Up Decisions

| Topic | Treatment |
| --- | --- |
| Legal-form vocabulary | ISO 20275/GLEIF as the preferred source; specific adoption after analyzing licensing, IRIs, and update process |
| Activity vocabulary | NACE Rev. 2.1 preferred; no closed MVP value set yet |
| Register identifiers | Specific national and European schemes only in later profiles |
| Membership role and period | Outside the core MVP; extension upon a confirmed use case |
| Representation type and validity | Relationship resource may be extended in a later development stage |
| Location module | Organization core references locations only once a responsible local location class is established |
| External alignments | Machine-readable alignment with W3C ORG, SEMIC, Gaia-X, and Schema.org only after checking IRIs and imports |

## 8. Acceptance of the SHACL Contract

The domain-specific SHACL contract is implemented because:

1. the five MVP classes and their responsibilities are confirmed,
2. the specified properties and cardinalities from the term catalog are confirmed,
3. separation of organizational units and locations is accepted,
4. reuse of ADMS, Address, and Contact is confirmed,
5. deferred jurisdiction, credential, and post topics are not treated as MVP requirements.

The visual target model is documented in the [Organization Diagram](diagrams/organization-concept-model.md). The complete shape catalog, constraints, error messages, and example scenarios are provided in the [SHACL Requirements Document](06_shacl-requirements.md).

## 9. Illustrative Example

> Beispiel Bau GmbH is a Legal Entity. Its planning department is an OrganizationalUnit. Anna Müller is described separately as a member through Membership and as a legal representative through LegalRepresentation.