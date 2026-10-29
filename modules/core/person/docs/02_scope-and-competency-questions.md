# Scope and Competency Questions of the Person Ontology

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

## 1. Purpose

The Person ontology describes natural persons and their directly personal core data. It aims to make persons uniquely referenceable in Construct-X without itself fully modeling organizational structures, projects, addresses, qualifications, or digital identity evidence.

This document defines the domain scope and competency questions. Classes, properties, IRIs, cardinalities, and imports are to be understood as proposals until the subsequent modeling phase.

## 2. Confirmed Scope

| Area | MVP decision |
| --- | --- |
| Subject | Real natural persons; no fictional characters or organizations |
| Referencing | Each Person is referenced by an IRI controlled by the respective data holder |
| Names | `fullName` and `givenName` are mandatory; `familyName`, `additionalName`, and `birthName` are optional in the core |
| Birth | Complete birth date as `xsd:date`; birthplace as a simple text value |
| Sex and gender | `sex` and `gender` as two separate optional entries; `sex` according to ISO/IEC 5218:2022 and four initial Gender values |
| Citizenship | Links to existing ISO 3166-1 country resources; multiple values are possible |
| Identifiers | Generic structured identifiers according to the Construct-X ADMS profile |
| Identity evidence | Generic links to externally modeled documents, credentials, or verification methods |
| Contact | Assignment through a separate reusable Contact module |
| Address | Assignment through the existing Address module and its `AddressAssignment` pattern |
| Organization and Project | Relationships are modeled in the respective responsible modules |
| Agent | Minimal shared superclass in a separate `core/agent` module |

## 3. Domain Target Model

`Person` is a subclass of `Agent` and contains names, birth details, `sex`/`gender`, citizenships, identifiers, and references to external identity evidence.

| Starting resource | Domain connection | Target | Responsible module |
| --- | --- | --- | --- |
| Person | `hasContactPoint` | Contact point with contact methods | Contact module |
| Person | Address assignment | Address | Address module |
| Person | Membership | Organization | `core/organization` |
| Person | Participation | Project | Project module |

These connections represent domain relationships and do not automatically imply OWL imports. The responsible modules and dependency rules are defined in [module-boundaries.md](04_module-boundaries.md).

## 4. Competency Questions

### CQ-01: How Is a Natural Person Uniquely Referenced?

A Person receives a stable IRI in the data holder’s namespace. The IRI is the resource’s technical RDF identity. Identity document numbers, personnel numbers, register identifiers, credentials, or public keys are additional identification or evidence resources and do not replace the Person IRI.

The model must be able to represent:

- a Person with multiple identifiers,
- the respective identifier scheme,
- the issuing authority or scheme agency,
- a reference to external identity evidence,
- evidence whose holder or subject is the Person.

### CQ-02: How Are Names and Name Changes Represented?

The MVP includes:

- mandatory given name (`givenName`),
- family name (`familyName`) as an optional core field,
- optional additional given names or middle names (`additionalName`),
- full name (`fullName`) as a mandatory, directly displayable label,
- optional birth name (`birthName`).

`familyName` remains optional so that persons without family names are not excluded from the model. `additionalName` is preferred over the culturally narrower term `middleName`, but can be mapped to `schema:additionalName` and UBL `MiddleName`. General tracking of arbitrary name changes is outside the MVP. The birth name covers only the explicitly requested initial case.

### CQ-03: How Are `sex` and `gender` Distinguished?

Both entries are optional and are not treated as synonyms:

- `sex` describes biological sex or a sex classification recorded in official contexts.
- `gender` describes gender identity, expression, or a social or legal classification in the applicable context.

Both entries reference controlled concepts. A separately versioned reference vocabulary based on [ISO/IEC 5218:2022](https://www.iso.org/standard/81682.html) is used for `sex`:

| Code | Meaning | Modeling note |
| --- | --- | --- |
| `0` | Not known | Explicit assertion that the value is not known to the creator |
| `1` | Male | Classification value for data exchange |
| `2` | Female | Classification value for data exchange |
| `9` | Not applicable | Not a value for additional gender identities; use for natural persons only with a justified source context |

Complete absence of the property means “no statement present” and is not equivalent to code `0`. ISO/IEC 5218 explicitly describes human sex for information interchange, rather than gender identities.

A separate Construct-X reference vocabulary with four initial values is used for `gender`:

- `gender:man` for Man,
- `gender:woman` for Woman,
- `gender:nonBinaryOrDiverse` as a provisional, extensible umbrella concept for non-binary or gender-diverse identities,
- `gender:notDisclosed` for an explicit choice not to disclose.

`gender:notDisclosed` is not an identity and differs from complete absence of the property. The EU table `grammatical-gender` must not be used for persons.

### CQ-04: How Are Birth Date and Birthplace Described?

Birth date is part of the MVP. Only complete date values using `xsd:date` are supported. Partial entries such as a year or year/month are outside the MVP.

Birthplace is intentionally modeled as a simple text value. A link to a place resource is not required in the MVP.

### CQ-05: How Is Citizenship Represented?

A Person can be linked to zero, one, or multiple country resources from the existing Construct-X country vocabulary. This vocabulary is based on ISO 3166-1.

NUTS-2 and ISO 3166-2 are unsuitable for this purpose: they classify regions or administrative subdivisions rather than citizenships. Statelessness is not modeled separately in the MVP. The absence of `citizenship` therefore remains merely the absence of a statement and must not automatically be interpreted as statelessness.

### CQ-06: How Are Identifiers and Their Issuers Described?

Identifiers follow the existing ADMS profile:

- `adms:Identifier` represents the identifier resource,
- `skos:notation` contains the value,
- the notation datatype identifies the identifier scheme,
- `adms:schemaAgency` may contain the name of the responsible scheme agency.

For a machine-readable relationship to the responsible issuing authority, an additional relationship such as `issuedBy` to an `Agent` should be provided. A technical issuance service can, where necessary, be described separately through `issuedThrough`. Specific identifier schemes will be defined after internal project clarification.

### CQ-07: How Are Identity Documents, Credentials, and Public Keys Connected?

The Person ontology receives the generic relationship `hasIdentityEvidence`. Its target is an external resource, for example an identity document reference, a driving licence reference, a Verifiable Credential, an official register extract, or other digitally verifiable evidence.

Detailed models for document numbers, validity, status, revocation, cryptographic keys, and verification procedures do not belong in the Person module. A public key initially establishes only control over a verification method. A reliable connection to a natural person requires evidence issued by a trusted issuer.

### CQ-08: How Are Private and Business Contact Details Distinguished?

Contact information is assigned through a separate Contact module. The described resource references a contact point through `hasContactPoint`; this contact point groups concrete `ContactMethod` resources such as email, telephone, website, or postal address assignment. `hasContactPoint` has no fixed OWL domain in the open core and therefore remains usable for organizations, projects, or positions.

Private, business, or official use is modeled through `contactUsage` on the contact point. A separate `contactPurpose` can express purposes such as general contact, delivery, billing, support, or emergency. Telephone numbers and email addresses are therefore not treated as fixed Person properties. Functional contacts such as “Site management” or “Billing office” remain possible without being mistaken for personal names. The usage value `private` is not an access rule; authorization remains outside the contact model.

### CQ-09: Which Addresses May Be Assigned to a Person?

The existing Address module is reused. The following roles are particularly relevant to persons:

- `RegistrationAddressRole` for a registered address,
- `ResidenceAddressRole` for a residential address,
- `PostalAddressRole` for a correspondence address.

A company or site address primarily belongs to the organization or site. It should not be copied directly onto a Person solely because of employment. A direct business correspondence address may later be represented through an explicit address role if a well-founded use case exists.

### CQ-10: How Is a Person Connected to Organizations or Projects?

Memberships, employment, and project participation are not intrinsic Person properties. They are modeled in the responsible domain modules:

- Organization module: membership, employment, role, post, and inverse relationships,
- Project module: participation, project role, and validity period.

Simple shortcut properties such as `isMemberOf` and `hasMember` may additionally be defined there. Relationships involving a role and a period require a separate membership or participation resource. This is a domain-specific n-ary relationship pattern rather than general RDF reification.

### CQ-11: How Are the Source, Validity, and Version of Personal Assertions Described?

A general provenance and history layer for individual assertions is outside the MVP. This does not prevent external identifier, document, or credential resources from having their own domain-required information about issuance, expiry, status, or revocation.

### CQ-12: Which Validation Questions Does the Core SHACL Profile Answer?

The implemented Core profile checks:

- that `fullName` and `givenName` each occur at least once,
- that birth dates are complete `xsd:date` values,
- that `sex` and `gender` each have at most one value,
- that `sex` uses only values from the approved ISO/IEC 5218 vocabulary,
- that `gender` uses only one of the four approved initial values,
- whether citizenship values come exclusively from the approved country vocabulary,
- the minimum information required for an identifier and an identity evidence reference.

## 5. Explicitly Outside the Person Core

- organization data, employment relationships, memberships, posts, and roles
- project participation and project roles
- complete address and contact models
- qualifications, certificates, and professional competencies
- detailed models for identity documents and Verifiable Credentials
- public keys, authentication, accounts, and authorization
- bank and payment data
- biometric and health data
- family, household, and social relationships
- powers of attorney and legal representation
- interests, preferences, and social network profiles
- general provenance, assertion history, and RDF reification

These exclusions do not prevent later links to corresponding resources. They only establish that the Person module does not own their semantics.

## 6. Non-Blocking Follow-Up Decisions

| Topic | Follow-up decision | Impact |
| --- | --- | --- |
| Gender extension | Finer subdivision of `nonBinaryOrDiverse` and long-term governance | Reference vocabulary |
| Identity evidence | Detailed model after selection of a security and trust model | External identity or credential profile |

## 7. Implemented Acceptance Criteria

The ontology and its Core Shapes were implemented after:

1. the module boundaries and the role of `core/agent` were confirmed,
2. the local terms and their ownership were defined,
3. follow-up decisions were classified as non-blocking,
4. external vocabularies were documented as referenced or aligned,
5. the Core SHACL profile was agreed.

The domain term catalog is documented in [term-catalog.md](05_term-catalog.md). The shared Agent superclass is described in the [Agent Specification](../../agent/docs/10_agent-specification.md). The executable data requirements are specified at domain level in the [SHACL Requirements](06_shacl-requirements.md).

## 8. Implementation Status

`core/agent`, `core/person`, the reference vocabularies, and the Core SHACL profile are implemented, tested, documented, and registered in the network metadata.

## 9. Illustrative Example

> Anna Müller can be described by her full name and birth date. An absent gender entry means only that no statement is present in the dataset; it is not automatically interpreted as `notDisclosed`.