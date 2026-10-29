# Source Analysis for the Person Ontology

**Status:** Consolidated analytical baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 20 August 2026  
**Scope:** `core/person`

## 1. Objective and Method

This analysis evaluates existing person, contact, organization, and identity models as a basis for the Construct-X Person core. It specifically examines:

- domain coverage and concept definitions,
- suitability as a normative core or alignment target,
- boundaries with other Construct-X Core modules,
- identifiers and identity evidence,
- name, birth, sex, gender, and citizenship data,
- contact, address, organization, and project relationships,
- risks arising from overly broad domains, unclear ranges, or sensitive identifiers.

The analysis served as the basis for the local IRIs, references, and axioms of T-Box 0.1.0 and the Person Core Shapes.

## 2. Key Findings

The [SEMIC Core Person Vocabulary 2.1.2](https://semiceu.github.io/Core-Person-Vocabulary/releases/2.1.2/) is the most suitable primary domain reference. It describes real natural persons, distinguishes `sex` from `gender`, supports multiple citizenships, and uses ADMS for identifiers.

[UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-CatalogueRequest-2.5.html) provides important exchange fields from business processes, but its Person aggregate mixes intrinsic data with employment, contact, financial accounts, and document references. In Construct-X, these fields must be distributed across separate modules.

[Schema.org Person](https://schema.org/Person), [FOAF](https://xmlns.com/foaf/spec/), and [vCard RDF](https://www.w3.org/TR/vcard-rdf/) are valuable interoperability sources, but none is sufficiently precise on its own for a quality-assured core model. The [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) supports separating memberships and roles. [W3C Controlled Identifiers](https://www.w3.org/TR/cid/) and the [Verifiable Credentials Data Model 2.1](https://www.w3.org/TR/vc-data-model-2.1/) support the separation of persons, keys, and verifiable identity evidence.

## 3. Sources Evaluated

| Source | Version used | Role in the analysis | Provisional use |
| --- | --- | --- | --- |
| [SEMIC Core Person Vocabulary](https://semiceu.github.io/Core-Person-Vocabulary/releases/2.1.2/) | 2.1.2 | European semantic person model | Primary domain reference and alignment candidate |
| [OASIS UBL](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-CatalogueRequest-2.5.html) | 2.5 CS01 | Business and document exchange | Field analysis and mapping source |
| [Schema.org Person](https://schema.org/Person) | Development version, accessed 2026-08-20 | Broad web interoperability | Alignment and naming source |
| [W3C vCard Ontology](https://www.w3.org/TR/vcard-rdf/) | W3C Interest Group Note, 2014 | Structured names and contacts | Reference for the separate Contact module |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99 | Basic Agent/Person model and web identity | Alignment candidate with limitations |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 2014 | Organization, membership, role, and post | Basis for the Organization module |
| [ADMS](https://semiceu.github.io/ADMS/releases/2.00/) | 2.0 | Structured identifiers | Reuse according to the Construct-X architecture |
| [W3C Controlled Identifiers](https://www.w3.org/TR/cid/) | W3C Recommendation | Keys and verification methods | Basis for an external identity model |
| [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model-2.1/) | 2.1 | Issuer, subject, evidence, status, and validity | Basis for external evidence |
| [ISO/IEC 5218](https://www.iso.org/standard/81682.html) | 2022, Edition 2 | Language-independent codes for human sex in information interchange | Normative basis for the `sex` vocabulary |
| [EU Authority Table Human Sex](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http%3A%2F%2Fpublications.europa.eu%2Fresource%2Fdataset%2Fhuman-sex) | Displayed version 20241211-0 | Existing controlled values for `sex` | Alignment and reuse candidate |
| [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) and [EU Country Authority Table](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/country) | Continuously maintained | Country references | Reuse through the existing Construct-X vocabulary |
| [Data Privacy Vocabulary](https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/) | 2.0 Final Community Group Report | Data protection and processing purposes | Future governance layer, outside the Person T-Box |

The existing Construct-X specifications were also evaluated:

- [Identifier Model](../../../../docs/architecture/identifier-model.md)
- [Namespace Concept](../../../../docs/architecture/construct-x-namespace-konzept.md)
- [Address Roles](../../address/docs/10_address-roles.md)
- [Address Conceptual Model](../../address/docs/03_concept-model.md)
- [ISO 3166-1 Country Dataset](../../../../datasets/reference/administrative-territories/iso-3166-1-countries/README.md)
- [Identifier Scheme Vocabulary](../../../../datasets/reference/vocabularies/identifier-scheme/README.md)

## 4. Analysis of Person and Agent Concepts

### 4.1 SEMIC Core Person

SEMIC defines `Person` as a real natural person, living or deceased. Fictional persons are excluded. The class is a subclass of both `foaf:Person` and `cv:Agent`. This matches the Construct-X objective more closely than the broader Schema.org model.

The source covers names, birth, death, residence, citizenship, identifiers, contact points, `sex`, and `gender`. Some of these areas exceed the Construct-X MVP scope or belong in other modules. SEMIC therefore provides a domain baseline but should not be copied in full.

### 4.2 Schema.org

`schema:Person` also includes fictional persons. The class additionally has a very broad range of properties, including employment, membership, affiliation, qualifications, relationships, ownership, and online profiles. Many ranges allow resources, text, or URLs as alternatives.

This flexibility is useful for web markup but insufficient for a validatable Construct-X module. Particularly useful elements include:

- established names such as `givenName`, `familyName`, and `additionalName`,
- alignments for general interoperability,
- `ContactPoint` as support for a separate contact concept.

### 4.3 FOAF

FOAF provides the established classes `foaf:Agent`, `foaf:Person`, and `foaf:Organization`. It is therefore an alignment target of the implemented `core/agent`.

However, its focus is on social and web-based identities. Properties such as `foaf:mbox`, accounts, and OpenID do not provide a suitable core for Construct-X. In particular, `foaf:mbox` is designed as an inverse-functional property and can make email addresses strong personal identifiers. This is problematic for data minimization and changing contact information.

### 4.4 Assessment

| Question | Decision |
| --- | --- |
| Local `Person` class? | Yes, with a Construct-X namespace and profile |
| Meaning restricted to real natural persons? | Yes, following SEMIC; no fictional persons |
| Shared `Agent` class? | Yes, but in a separate `core/agent` |
| Reuse FOAF directly? | Primarily as an alignment; assess import requirements later |
| Use Schema.org directly as the core? | No; its ranges and scope are too broad |

## 5. Name Model

### 5.1 Comparison

| Concept | SEMIC Core Person | UBL 2.5 | Schema.org | vCard RDF | Construct-X assessment |
| --- | --- | --- | --- | --- | --- |
| Full name | `fullName`, strongly recommended | No equivalent Person field | `name` | `fn` | Include as a mandatory displayable label |
| Given name | `givenName`; all given names may appear in order within one value | `FirstName` | `givenName` | `given-name` | Include as a core term |
| Family name | `familyName` | `FamilyName` | `familyName` | `family-name` | Include as a core term |
| Middle/additional names | No separate core field; can be covered by `givenName` | `MiddleName` | `additionalName` | `additional-name` | Include optionally as `additionalName` |
| Birth name | `birthName` as the complete name at birth | No direct equivalent | No specific core term | No specific core term | Include optionally |
| Title/prefix/suffix | Outside the core of the intended profile | `Title`, `NameSuffix` | `honorificPrefix`, `honorificSuffix` | Corresponding components | Exclude from the MVP |
| Additional family names | Patronymic/matronymic possible | `OtherName`, with a second family name as an example | No precise pattern | Possible through name components | Exclude from the MVP |

### 5.2 Recommendation

The MVP uses five terms: `fullName`, `givenName`, `additionalName`, `familyName`, and `birthName`. `fullName` and `givenName` are mandatory in the Core SHACL profile. `familyName` remains an optional core term so that persons without family names are not excluded. Multiple values should not be unnecessarily prevented at the RDF level because names depend on language and culture.

The order of multiple given names can be preserved in a single literal value. A detailed class for name components or name history is not required for the MVP.

## 6. Birth Details

| Topic | Source coverage | Recommendation |
| --- | --- | --- |
| Birth date | SEMIC permits `xsd:date`, `xsd:gYearMonth`, or `xsd:gYear`; UBL uses `BirthDate`; Schema.org uses `Date` | Include `birthDate` and permit only complete `xsd:date` values in the MVP |
| Birthplace | UBL provides both textual `BirthplaceName` and `BirthplaceLocation`; Schema.org expects `Place`; SEMIC uses a Location resource | Respect the user decision and include `birthPlaceName` as a simple string |
| Death details | SEMIC and Schema.org support date and place | Outside the current MVP |

A textual birthplace value intentionally provides less semantic structure than a place resource but keeps the core small. An additional object relationship can be introduced later without invalidating the MVP value.

## 7. `sex` and `gender`

SEMIC explicitly distinguishes the two terms:

- `sex` refers to biological sex characteristics or their official registration.
- `gender` includes identities, expressions, and social roles and should use controlled values appropriate to the context.

UBL provides `GenderCode` but names different code systems, such as ISO/IEC 5218 or ICAO 9303, depending on the business context. Schema.org permits both `GenderType` and free text for `gender` and does not distinguish a separate `sex` core field. vCard has a combined structured sex/gender entry but does not provide a sufficiently precise target model here.

### Recommendation

1. Model `sex` and `gender` as separate optional object relationships.
2. Values should be SKOS concepts or equivalent controlled resources rather than uncontrolled free text.
3. Use a separately versioned SKOS vocabulary for `sex`, based on ISO/IEC 5218:2022, with codes `0`, `1`, `2`, and `9`.
4. The absence of `sex` means “no statement.” Code `0`, by contrast, explicitly states “not known.”
5. Code `9` means “not applicable” and must not be interpreted as an umbrella value for other gender identities. In the Person context, its use is meaningful only when justified and faithful to the source.
6. An alignment with the EU Authority Table `human-sex` remains subject to a later individual assessment; version 0.1.0 initially uses stable Construct-X IRIs.
7. Use a separately versioned initial Construct-X vocabulary for `gender`, containing `man`, `woman`, `nonBinaryOrDiverse`, and `notDisclosed`.
8. `nonBinaryOrDiverse` is a provisional broad concept that can later be extended with more precise narrower concepts.
9. `notDisclosed` denotes explicit non-disclosure rather than a gender identity; an absent property still means that no statement is present.
10. The EU Authority Table `grammatical-gender` is linguistic and must not be used for persons’ sex or gender data.

## 8. Citizenship and Countries

SEMIC models citizenship as a legal relationship between a person and a jurisdiction. Zero, one, or multiple citizenships are possible. UBL 2.5 provides `CitizenshipCountry` with cardinality `0..n`; the former `NationalityID` is marked as deprecated, while `NationalityCode` still occurs. Schema.org uses `nationality` with `Country` as its range.

Construct-X already has an ISO 3166-1-based country vocabulary with stable IRIs, for example:

```text
https://www.construct-x.org/vocab/country#DEU
```

The country resources have alpha-2, alpha-3, and numeric ADMS identifiers. Citizenship should therefore reference the country resource itself rather than an untyped string code.

### Assessment of Alternatives

| System | Suitability for citizenship | Reason |
| --- | --- | --- |
| ISO 3166-1 | Suitable | Identifies states and dependent territories at country level |
| ISO 3166-2 | Unsuitable as a citizenship value | Identifies administrative subdivisions within states |
| NUTS-2 | Unsuitable | Statistical EU regions, not states or citizenships |

The current typing of countries as `conx-addr:Country` can be reused but reveals a module boundary: `Country` is not exclusively an address concept. Moving it to a geographic core module would be architecturally plausible in the future but is not required for the Person MVP.

Statelessness is not modeled separately in the MVP. It must not be inferred solely from the absence of `citizenship`, since unknown or undisclosed data may also be absent.

## 9. Identifiers

### 9.1 Source Comparison

SEMIC uses `adms:Identifier` and adds, among other elements:

- `skos:notation` for the identifier value,
- `adms:schemaAgency` for the responsible agency,
- `dct:issued` for the issue date,
- `dct:creator` for an issuing Agent,
- a relationship to the identified resource.

UBL 2.5 provides a general Person ID and multiple `NationalID` values. Schema.org permits `PropertyValue`, text, or a URL for `identifier`. vCard provides `hasUID`; FOAF sometimes uses strong web-based identifiers such as mailboxes.

### 9.2 Construct-X Decision

The existing [Construct-X Identifier Model](../../../../docs/architecture/identifier-model.md) is authoritative:

- no parallel local Identifier class,
- `adms:Identifier` as the shared structure,
- `skos:notation` as the value,
- the notation datatype identifies the scheme,
- `adms:schemaAgency` describes the scheme agency,
- schemes are maintained in the central Identifier Scheme vocabulary.

The Person ontology should use this structure and define only the relationship between Person and identifier, unless a generic relationship already exists. Specific national, project-related, or organizational identifier schemes have not yet been selected.

### 9.3 Issuer and Technical Service

The responsible issuing authority and the technical issuance service are not necessarily identical. The target model should therefore be able to distinguish:

- `issuedBy`: the `Agent` responsible in domain or legal terms,
- `issuedThrough`: an optional technical service.

Organizations and services are referenced only. Their internal modeling belongs in separate modules.

## 10. Identity Documents, Credentials, and Public Keys

UBL permits multiple `IdentityDocumentReference` entries for a Person and gives a driving licence as an example. This supports the need for a generic connection but does not provide a sufficient security or trust model.

W3C Controlled Identifiers describes controlled identifier documents, verification methods, public keys, and service endpoints. Successful cryptographic proof demonstrates that someone controls the corresponding private key. It does not automatically prove a name, birth date, or the existence of a natural person.

The W3C Verifiable Credentials Data Model adds the necessary assertion structure:

- `issuer` for the issuing entity,
- `credentialSubject` for the subject of the assertions,
- `evidence` for supporting evidence,
- validity and status, including revocation mechanisms.

### Recommendation

The Person module receives the generic relationship `hasIdentityEvidence`. Permitted targets are external resources, such as identity document or driving licence references, Verifiable Credentials, official register extracts, and other digitally verifiable evidence. Document, credential, and key resources are modeled outside the module. In particular, identity document fields and key material are not attached directly to `Person`.

The following layers remain separate:

| Starting point | Separate layer |
| --- | --- |
| Person IRI | Structured domain identifier |
| Person IRI | Identity document or credential |
| Person IRI | Verification method / public key |

A reliable identity chain requires explicit assertions about the subject, issuer, validity, status, and verification method used.

## 11. Contact Model

### 11.1 Source Coverage

SEMIC `Contact Point` primarily covers contact pages, email, and telephone. Schema.org `ContactPoint` adds, among other elements, `contactType`, service area, available language, and opening hours. Its classification through `contactType` is text-based and therefore offers limited control.

UBL `Contact` contains:

- ID and label,
- functional name,
- position and department,
- telephone, fax, and email,
- notes and additional communication methods.

The UBL documentation notes that a contact name may be functional and need not be a person’s name. This is important for Construct-X: “Site management” or “Billing office” can describe a contact purpose without asserting the existence of a natural person. The evaluated UBL Contact structure is documented, among other places, in [UBL Qualification Application Request 2.5](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-QualificationApplicationRequest-2.5.html).

vCard RDF provides structured email, telephone, and other communication resources. Types such as `Home` and `Work` can express usage contexts. The n-ary property pattern is more suitable than fixed properties such as `privateEmail` or `businessPhone`.

### 11.2 Recommendation

A separate `core/contact` should distinguish at least three levels:

| Level | Relationships and information |
| --- | --- |
| Resource | `hasContactPoint` references a `ContactPoint` |
| `ContactPoint` | `hasContactMethod` references a `ContactMethod`; usage and purpose are described through `ContactUsage` and `ContactPurpose` |
| `ContactMethod` | Describes a `ContactChannel` and its value |

- `ContactPoint` groups the contact options of an entity within a usage context.
- `ContactMethod` describes exactly one channel and its value, URI, or address assignment.
- `ContactUsage` distinguishes, in particular, private, business, and official use.
- `ContactPurpose` separately describes a purpose such as general contact, delivery, billing, support, or emergency.
- `hasContactPoint` has no fixed OWL domain in the open core, allowing the pattern to be used for projects, positions, or other identifiable resources as well as Agents.

The precise modeling of email and telephone values, normalization, multilingualism, and availability times belongs to the implemented Contact module. The Person ontology does not copy these fields.

## 12. Addresses

UBL distinguishes `ResidenceAddress` from other business addresses. The existing Construct-X Address module is already more general: an `AddressAssignment` can connect an identifiable resource to an address and an address role.

Existing roles can be used directly for persons:

- registered address through `RegistrationAddressRole`,
- residential address through `ResidenceAddressRole`,
- correspondence through `PostalAddressRole`.

An organization or site address must not automatically be interpreted as an employee’s address. If a business correspondence address is to appear directly on a Person, it requires an explicit context. This may later be represented by an additional address role or an assignment through a position or organization.

## 13. Organizations, Employment, and Projects

UBL includes fields such as `JobTitle`, `OrganizationDepartment`, and `RoleCode` in its Person aggregate. Schema.org provides `worksFor`, `memberOf`, and `affiliation`. These fields are practical for data exchange but would mix organization and relationship concepts into the Person core.

W3C ORG provides a more suitable target model:

- `org:Organization`,
- `org:memberOf` and `org:hasMember`,
- `org:Membership` for an n-ary relationship,
- `org:Role` and `org:Post`,
- temporal validity of a membership.

Memberships are therefore defined in the Organization module. Employment, positions, and other domain relationships remain outside the Person core. A Person remains a target or participant in these relationships but does not own their semantics.

## 14. UBL Person in Detail

The complete UBL 2.5 Person component was classified against the confirmed scope:

| UBL field | Cardinality | Construct-X mapping |
| --- | --- | --- |
| `ID` | `0..1` | Generic ADMS identifier |
| `FirstName` | `0..1` | `givenName` |
| `FamilyName` | `0..1` | `familyName` |
| `Title` | `0..1` | Outside the MVP |
| `MiddleName` | `0..1` | `additionalName` |
| `OtherName` | `0..1` | Outside the MVP; possible additional family name |
| `NameSuffix` | `0..1` | Outside the MVP |
| `JobTitle` | `0..1` | Organization module |
| `NationalityID` | `0..1` | Deprecated; do not adopt |
| `NationalID` | `0..n` | Structured identifier |
| `NationalityCode` | `0..1` | Replace with a country resource rather than a literal code |
| `GenderCode` | `0..1` | Source input for the separate `sex`/`gender` decision |
| `BirthDate` | `0..1` | `birthDate` |
| `BirthplaceName` | `0..1` | `birthPlaceName` as a string |
| `OrganizationDepartment` | `0..1` | Organization module |
| `RoleCode` | `0..1` | Organization or Project module |
| `BirthplaceLocation` | `0..1` | Outside the MVP |
| `CitizenshipCountry` | `0..n` | Link to ISO 3166-1 country resources |
| `Contact` | `0..1` | Contact module |
| `FinancialAccount` | `0..1` | Explicitly outside the Person core |
| `IdentityDocumentReference` | `0..n` | Generic connection; details in the Identity module |
| `ResidenceAddress` | `0..1` | Address module with `ResidenceAddressRole` |

UBL therefore supports almost all required data groups, but not their intended modular separation.

## 15. Implemented Construct-X Target Profile

The following table documents the target profile derived from the analysis and implemented in version `0.1.0`.

| Term | Kind | Proposed range | MVP profile | Source/rationale |
| --- | --- | --- | --- | --- |
| `Agent` | Class in `core/agent` | - | Common superclass | FOAF, SEMIC, ORG |
| `Person` | Class | `Agent` | Real natural person | SEMIC as the primary definition |
| `fullName` | Datatype property | Language-tagged literal or string | Mandatory | SEMIC `fullName`, vCard `fn` |
| `givenName` | Datatype property | Language-tagged literal or string | Mandatory | SEMIC, UBL, Schema.org, vCard |
| `additionalName` | Datatype property | Language-tagged literal or string | Optional | Schema.org, vCard, UBL `MiddleName` |
| `familyName` | Datatype property | Language-tagged literal or string | Optional core field | SEMIC, UBL, Schema.org, vCard |
| `birthName` | Datatype property | Language-tagged literal or string | Optional | SEMIC |
| `birthDate` | Datatype property | Initially `xsd:date` | Optional, at most one value | SEMIC, UBL, Schema.org |
| `birthPlaceName` | Datatype property | `xsd:string` | Optional, at most one value | UBL and user decision |
| `sex` | Object property | ISO/IEC 5218 concept | Optional, at most one value | SEMIC and ISO/IEC 5218:2022 |
| `gender` | Object property | Concept from the Construct-X Gender vocabulary | Optional, at most one value | SEMIC and confirmed initial vocabulary |
| `citizenship` | Object property | Existing country resource | Optional, multiple values | SEMIC, UBL, ISO 3166-1 |
| Person–identifier relationship | Object property | `adms:Identifier` | Optional, multiple values | ADMS and Construct-X profile |
| `hasIdentityEvidence` | Object property | External evidence resource | Optional, multiple values | UBL, Controlled Identifiers, VC |

Contact and address relationships are intentionally not owned by the Person module. They are applied to Person instances through properties from the responsible modules.

## 16. T-Box and A-Box Boundaries

The implementation separates the following artifact types:

### T-Box

- `Agent` and `Person` classes,
- Person properties and their definitions,
- domain, range, subclass, and alignment axioms,
- where applicable, semantic restrictions that apply independently of an application profile.

### A-Box or Reference Vocabularies

- specific countries such as `country:DEU`,
- controlled values for `sex` and `gender`,
- specific identifier schemes,
- contact and address roles,
- specific persons, identifiers, and evidence in data holder namespaces.

Controlled values should be versioned in separate vocabularies rather than embedded as fixed individuals in the Person T-Box.

## 17. Data Protection and Governance Assessment

Person IRIs and personal identifiers must not be equated with global public discoverability. Decisions about which data are published, exchanged, or access-protected are governance and authorization matters above the ontology layer.

Nevertheless, the following principles apply to the model scope:

- no email address as the default identity key,
- no public keys directly as Person identifiers,
- no unnecessary copying of organization or site data onto persons,
- sensitive evidence only as controlled external resources,
- an explicit distinction between unknown, undisclosed, and absent in domain terms whenever the use case requires it.

The W3C Data Privacy Vocabulary may later describe processing, purposes, legal bases, and technical measures. It does not become part of the Person T-Box.

## 18. Resulting Decisions

The source analysis provides the following sound decisions for the modeling phase:

1. SEMIC Core Person 2.1.2 is the primary domain reference.
2. Construct-X defines its own `Person` class, restricted to real natural persons.
3. `Agent` is implemented as a minimal shared class in a separate core module.
4. The name core consists of `fullName`, `givenName`, `additionalName`, `familyName`, and `birthName`.
5. `fullName` and `givenName` are mandatory in the Core SHACL profile.
6. Birth dates are accepted only as complete `xsd:date` values; birthplace remains a text value.
7. `sex` and `gender` are modeled separately and optionally; `sex` is based on ISO/IEC 5218:2022, and `gender` initially contains four Construct-X concepts.
8. Citizenship references ISO 3166-1-based Construct-X country resources; NUTS-2 is excluded.
9. Identifiers use the existing ADMS profile.
10. `hasIdentityEvidence` generically links persons to external evidence resources.
11. Identity documents, credentials, and public keys are not modeled in detail within the Person ontology.
12. Contact is implemented as a separate assignment model with an unrestricted domain and an outgoing relationship from the entity holding the contact information.
13. Addresses use the existing `AddressAssignment` model.
14. Memberships, employment, and project participation belong to Organization or Project.
15. General assertion provenance and reification remain outside the MVP.

## 19. Open Issues after T-Box Implementation

- finer extensions and long-term governance of the Gender vocabulary,
- direct reuse of or alignment with the EU Authority Table `human-sex`,
- a machine-readable issuer model in addition to `adms:schemaAgency`,
- an initial controlled role vocabulary for the Contact module,
- long-term ownership of the `Country` class,
- precise import, reference, and alignment decisions for each external source.

These issues do not block T-Box 0.1.0. They form a focused decision list for alignments and subsequent modules. The individual local terms are described in the [Term Catalog](05_term-catalog.md), and their implemented validation contracts are described in the [SHACL Requirements Profile](06_shacl-requirements.md).

## 20. Illustrative Mapping Example

> SEMIC provides a broad person model, UBL provides business-related person data, and vCard provides contact patterns. Construct-X adopts only intrinsic personal data from these sources; Contact and Organization remain separate Core modules.
