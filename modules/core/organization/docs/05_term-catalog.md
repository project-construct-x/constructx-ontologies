# Term Catalog for the Organization MVP

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/organization`  
**Implementation status:** T-Box and Core Shapes 0.1.0 implemented

## 1. Purpose

This catalog translates the confirmed scope and source analysis into specific terms. It describes local classes and properties and the reuse of existing Construct-X modules and external vocabularies.

Cardinalities marked “Core SHACL” are described in the [SHACL Requirements Document](06_shacl-requirements.md) and implemented in the executable Core Shape. They are deliberately not modeled as strict OWL cardinalities.

Foundations:

- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Source Analysis](01_source-analysis.md)
- [Agent Specification](../../agent/docs/10_agent-specification.md)
- [Identifier Model](../../../../docs/architecture/identifier-model.md)
- [Address Roles](../../address/docs/10_address-roles.md)
- [Contact Term Catalog](../../contact/docs/05_term-catalog.md)

## 2. Namespace

```text
Ontology IRI: https://www.construct-x.org/ontology/organization
Version IRI:  https://www.construct-x.org/ontology/organization/0.1.0
Namespace:    https://www.construct-x.org/ontology/organization#
Prefix:       conx-org
```

The IRIs are established by the module metadata and T-Box 0.1.0.

Reused namespaces:

```text
conx-agent:   https://www.construct-x.org/ontology/agent#
conx-person:  https://www.construct-x.org/ontology/person#
conx-addr:    https://www.construct-x.org/ontology/address#
conx-contact: https://www.construct-x.org/ontology/contact#
adms:         http://www.w3.org/ns/adms#
skos:         http://www.w3.org/2004/02/skos/core#
```

## 3. Modeling Rules

1. `Organization` is a subclass of `conx-agent:Agent`.
2. `LegalEntity` and `OrganizationalUnit` specialize `Organization`.
3. The MVP contains no local classes `EconomicActor`, `Enterprise`, `FormalOrganization`, or `Post`.
4. Sole traders and freelancers remain `conx-person:Person` and act through contextual Agent roles.
5. Membership and legal representation are modeled as separate relationship resources.
6. OWL describes meaning, domain, range, subclasses, and inverse relationships as openly as possible.
7. SHACL handles minimum and maximum cardinalities, datatypes, and closed profile rules.
8. Domain-specific identifiers exclusively use `adms:Identifier`; no local Identifier class is introduced.
9. Address and Contact are connected through the existing assignment properties with unrestricted domains.
10. Jurisdiction-specific identifier, legal-form, and register rules are outside version 0.1.0.
11. Organization, unit, membership, and representation instances receive IRIs in their data holder's namespace.

## 4. Term Overview

### 4.1 Classes

| Local Term | Superclass | MVP |
| --- | --- | --- |
| `conx-org:Organization` | `conx-agent:Agent` | Yes |
| `conx-org:LegalEntity` | `conx-org:Organization` | Yes |
| `conx-org:OrganizationalUnit` | `conx-org:Organization` | Yes |
| `conx-org:Membership` | No local superclass | Yes |
| `conx-org:LegalRepresentation` | No local superclass | Yes |

### 4.2 Local Properties

| Property | Domain | Range | Core SHACL 0.1.0 |
| --- | --- | --- | --- |
| `conx-org:name` | `Organization` | `xsd:string` or `rdf:langString` | `1..n` |
| `conx-org:legalName` | `LegalEntity` | `xsd:string` or `rdf:langString` | `1..n` |
| `conx-org:alternativeName` | `Organization` | `xsd:string` or `rdf:langString` | `0..n` |
| `conx-org:legalForm` | `LegalEntity` | `skos:Concept` | `0..1` |
| `conx-org:registrationDate` | `LegalEntity` | `xsd:date` | `1` |
| `conx-org:activity` | `Organization` | `skos:Concept` | `0..n` |
| `conx-org:subOrganizationOf` | `Organization` | `Organization` | `0..n` |
| `conx-org:hasSubOrganization` | `Organization` | `Organization` | `0..n` |
| `conx-org:unitOf` | `OrganizationalUnit` | `Organization` | `1..n` |
| `conx-org:hasUnit` | `Organization` | `OrganizationalUnit` | `0..n` |
| `conx-org:member` | `Membership` | `conx-agent:Agent` | `1` |
| `conx-org:membershipOrganization` | `Membership` | `Organization` | `1` |
| `conx-org:representedOrganization` | `LegalRepresentation` | `LegalEntity` | `1` |
| `conx-org:representative` | `LegalRepresentation` | `conx-person:Person` | `1` |

### 4.3 Reused Properties

| Property | Usage |
| --- | --- |
| `adms:identifier` | Identifiers of an Organization, Legal Entity, Organizational Unit, or Membership |
| `conx-addr:hasAddressAssignment` | Legal, registered, headquarters, or postal address assignment |
| `conx-contact:hasContactPoint` | General, official, and functional contact points, including the homepage |

## 5. Classes

### 5.1 `conx-org:Organization`

| Item | Specification |
| --- | --- |
| Definition | Organized collective actor with a common purpose or a persistently recognizable structure |
| Superclass | `conx-agent:Agent` |
| MVP subclasses | `conx-org:LegalEntity`, `conx-org:OrganizationalUnit` |
| Core requirement | At least one `conx-org:name` |
| Exclusions | Mere location, project, individual person, and contextual business role |
| Primary source | W3C Organization Ontology |
| Alignment | `rdfs:subClassOf org:Organization` as a conservative candidate; no equivalence without individual assessment |
| Instantiation | Company, public authority, association, consortium, or organizational grouping, provided the local scope is satisfied |

Example:

```turtle
ex:bauverband
    a conx-org:Organization ;
    conx-org:name "Bauverband Beispielregion"@de .
```

`Organization` asserts neither separate legal personality nor a particular legal form or economic activity.

### 5.2 `conx-org:LegalEntity`

| Item | Specification |
| --- | --- |
| Definition | Organization with its own legal identity, treated as a bearer of rights and obligations in the relevant jurisdiction |
| Superclass | `conx-org:Organization` |
| Core requirements | `name`, `legalName`, `registrationDate`; at least one structured ADMS identifier is checked by the Core Shape |
| Primary sources | SEMIC Core Business Vocabulary, Gaia-X LegalPerson, GLEIF |
| Alignment | Assess alignment with SEMIC `LegalEntity`, W3C `org:FormalOrganization`, and Gaia-X `LegalPerson`; no blanket equivalence |
| Exclusions | Departments, mere locations, and self-employed persons without a separately modeled legal organization |

Example:

```turtle
ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date .
```

The local class is deliberately organization-specific. It must therefore not be equated without assessment with an external concept that also includes self-employed natural persons.

### 5.3 `conx-org:OrganizationalUnit`

| Item | Specification |
| --- | --- |
| Definition | Organizational part of one or more parent organizations with its own function or responsibility, but without separate legal personality arising from that fact |
| Superclass | `conx-org:Organization` |
| Core requirements | `name` and at least one `unitOf` |
| Primary source | W3C Organization Ontology `org:OrganizationalUnit` |
| Alignment | `rdfs:subClassOf org:OrganizationalUnit` as a candidate |
| Examples | Department, division, branch without separate legal personality, functional plant organization |
| Exclusions | Physical location without organizational function and subsidiary with separate legal personality |

An organizational unit may have its own address, contact points, and identifiers. This does not automatically make it a `LegalEntity`.

### 5.4 `conx-org:Membership`

| Item | Specification |
| --- | --- |
| Definition | Separate relationship through which an Agent is a member of an Organization |
| Superclass | No local superclass |
| Core requirements | Exactly one `member` and exactly one `membershipOrganization` |
| Primary source | W3C Organization Ontology `org:Membership` |
| Alignment | Assess alignment with `org:Membership`, `org:member`, and `org:organization` |
| Possible identifier | Membership number as `adms:identifier` of the Membership |
| Examples | Person in an association, company in a guild, company affiliated with a statutory accident insurance institution |

Example:

```turtle
ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband .
```

Role, status, and validity period are not introduced as mandatory concepts in the MVP. The relationship resource allows these extensions later.

### 5.5 `conx-org:LegalRepresentation`

| Item | Specification |
| --- | --- |
| Definition | Relationship through which a Person legally represents a Legal Entity |
| Superclass | No local superclass |
| Core requirements | Exactly one `representedOrganization` and exactly one `representative` |
| Primary sources | SEMIC Power of Attorney, Schema.org `legalRepresentative`, UBL, and BRIS requirements |
| Alignment | No direct class equivalent confirmed; assess property mappings later |
| Data protection boundary | No copies of the person's names, title, date of birth, or place of birth |

Example:

```turtle
ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

The separate resource allows future information on representation type, period, or joint representation without burdening the MVP with these details.

## 6. Name and Registration Properties

### 6.1 `conx-org:name`

| Item | Specification |
| --- | --- |
| Definition | Generally usable designation of an Organization |
| Domain | `conx-org:Organization` |
| Range | `xsd:string` or `rdf:langString` |
| Core SHACL | At least one non-empty value |
| Requirement | Mandatory for every Organization, including subclasses |
| Sources | W3C ORG, Schema.org `name`, Gaia-X `name`, UBL `PartyName` |
| Alignment | Assess `rdfs:subPropertyOf schema:name`; do not impose equivalence |

### 6.2 `conx-org:legalName`

| Item | Specification |
| --- | --- |
| Definition | Legally or officially registered name of a Legal Entity |
| Domain | `conx-org:LegalEntity` |
| Range | `xsd:string` or `rdf:langString` |
| Core SHACL | At least one non-empty value |
| Requirement | Mandatory for `LegalEntity` |
| Sources | SEMIC `legalName`, Schema.org `legalName`, UBL `RegistrationName` |
| Alignment | SEMIC and Schema.org as candidates |

The value may be identical to `name`, but is not automatically derived from it. An organization may use a shorter name than its registered name.

### 6.3 `conx-org:alternativeName`

| Item | Specification |
| --- | --- |
| Definition | Other common designation, abbreviation, or trading name of an Organization |
| Domain | `conx-org:Organization` |
| Range | `xsd:string` or `rdf:langString` |
| Core SHACL | `0..n`, non-empty |
| Requirement | Optional |
| Sources | SEMIC `alternativeName`, Schema.org `alternateName`, UBL `TradePartyName` |

A general name history and temporal validity of individual names are outside the MVP.

### 6.4 `conx-org:legalForm`

| Item | Specification |
| --- | --- |
| Definition | Classification of a Legal Entity's legal form in the relevant jurisdiction |
| Domain | `conx-org:LegalEntity` |
| Range | `skos:Concept` |
| Core SHACL | `0..1` |
| Requirement | Optional in the MVP; future profiles may require a value |
| Sources | SEMIC `legalFormType`, GLEIF/ISO 20275, Schema.org |
| Value set | Not yet closed; ISO 20275/GLEIF is the preferred candidate |

Free text may occur in external sources, but is not the preferred normative range.

### 6.5 `conx-org:registrationDate`

| Item | Specification |
| --- | --- |
| Definition | Calendar date on which a Legal Entity was registered in the authoritative register |
| Domain | `conx-org:LegalEntity` |
| Range | Exclusively `xsd:date` |
| Core SHACL | Exactly one value |
| Requirement | Mandatory for `LegalEntity` in the implemented MVP profile |
| Sources | SEMIC `registrationDate`; register and GLEIF data |

`registrationDate` is not automatically the founding date or actual start of business activity. `foundingDate` and `activityStartDate` are not introduced in the MVP.

### 6.6 `conx-org:activity`

| Item | Specification |
| --- | --- |
| Definition | Activity area of an Organization expressed through a controlled classification |
| Domain | `conx-org:Organization` |
| Range | `skos:Concept` |
| Core SHACL | `0..n` |
| Requirement | Optional |
| Sources | SEMIC `legalEntityActivity`, NACE, Schema.org |
| Value set | Open in the MVP; NACE Rev. 2.1 is the preferred European source |

Distinguishing primary and secondary activities is outside version 0.1.0.

## 7. Structural Properties

### 7.1 `conx-org:subOrganizationOf`

| Item | Specification |
| --- | --- |
| Definition | Places an Organization under a parent Organization in a general organizational hierarchy |
| Domain | `conx-org:Organization` |
| Range | `conx-org:Organization` |
| Core SHACL | `0..n`; value must not be identical to the subject |
| Inverse property | `conx-org:hasSubOrganization` |
| Source | W3C ORG, Schema.org, Gaia-X |
| Alignment | Assess `org:subOrganizationOf`, `schema:parentOrganization` |

The relationship asserts no corporate ownership or control percentage.

### 7.2 `conx-org:hasSubOrganization`

| Item | Specification |
| --- | --- |
| Definition | Links an Organization to an organizationally subordinate Organization |
| Domain | `conx-org:Organization` |
| Range | `conx-org:Organization` |
| Core SHACL | `0..n` |
| Inverse property | `conx-org:subOrganizationOf` |
| Source | W3C ORG, Schema.org, Gaia-X |

Data storage may choose a preferred direction; OWL can infer the inverse relationship. The SHACL profile should not require both directions as explicit input.

### 7.3 `conx-org:unitOf`

| Item | Specification |
| --- | --- |
| Definition | Assigns an Organizational Unit to a parent Organization |
| Domain | `conx-org:OrganizationalUnit` |
| Range | `conx-org:Organization` |
| Core SHACL | At least one value; no global maximum |
| Inverse property | `conx-org:hasUnit` |
| Source | W3C ORG `unitOf` |

Multiple values remain possible for matrix organizations. A future narrower profile may require exactly one primary assignment.

### 7.4 `conx-org:hasUnit`

| Item | Specification |
| --- | --- |
| Definition | Links an Organization to a contained Organizational Unit |
| Domain | `conx-org:Organization` |
| Range | `conx-org:OrganizationalUnit` |
| Core SHACL | `0..n` |
| Inverse property | `conx-org:unitOf` |
| Source | W3C ORG `hasUnit` |

## 8. Membership Properties

### 8.1 `conx-org:member`

| Item | Specification |
| --- | --- |
| Definition | Specifies the Agent that is the subject of a Membership |
| Domain | `conx-org:Membership` |
| Range | `conx-agent:Agent` |
| Core SHACL | Exactly one value, explicitly typed as Agent or an established subclass |
| Source | W3C ORG `member` |

The range permits people and organizations. A Membership itself is not an Agent.

### 8.2 `conx-org:membershipOrganization`

| Item | Specification |
| --- | --- |
| Definition | Specifies the Organization in which the Membership exists |
| Domain | `conx-org:Membership` |
| Range | `conx-org:Organization` |
| Core SHACL | Exactly one value |
| Source | W3C ORG `organization` |
| Alignment | Assess `org:organization`; the local name avoids the ambiguity of a highly generic property name |

Direct shortcuts such as `hasMember` and `memberOf` are not introduced as a second mandatory data direction in the MVP. They may later be considered as derivable convenience properties.

## 9. Representation Properties

### 9.1 `conx-org:representedOrganization`

| Item | Specification |
| --- | --- |
| Definition | Specifies the Legal Entity to which a legal representation relationship refers |
| Domain | `conx-org:LegalRepresentation` |
| Range | `conx-org:LegalEntity` |
| Core SHACL | Exactly one value |
| Source | SEMIC, Schema.org, UBL, and register requirements |

### 9.2 `conx-org:representative`

| Item | Specification |
| --- | --- |
| Definition | Specifies the Person legally representing a Legal Entity |
| Domain | `conx-org:LegalRepresentation` |
| Range | `conx-person:Person` |
| Core SHACL | Exactly one value, explicitly typed as Person |
| Data protection | Only the Person resource is referenced; personal data is not duplicated in the representation |

The MVP provides no direct shortcut property from Legal Entity to Person. This keeps the representation relationship extensible with type, period, and representation rules.

## 10. Reused Integration Terms

### 10.1 `adms:identifier`

Organizations, Legal Entities, Organizational Units, and Memberships may have ADMS identifiers. The general pattern is:

```turtle
ex:bau-gmbh
    adms:identifier [
        a adms:Identifier ;
        skos:notation "HRB 12345"^^ex-scheme:local-register-number ;
        adms:schemaAgency "Responsible registration authority"
    ] .
```

The datatype in this example is not yet an approved Construct-X value. The list of Organization identification schemes will be established in a later phase. The MVP must not treat VAT ID, LEI, EUID, EORI, or GLN as jointly mandatory identifiers.

A membership number belongs to the `Membership`, rather than automatically to the member:

```turtle
ex:membership-4711
    adms:identifier [
        a adms:Identifier ;
        skos:notation "4711"^^ex-scheme:association-membership-number ;
        adms:schemaAgency "Bauverband Beispielregion"
    ] .
```

### 10.2 `conx-addr:hasAddressAssignment`

Organizations and Organizational Units use the existing AddressAssignment pattern. For Legal Entities, the roles `LegalAddressRole`, `HeadquartersAddressRole`, `RegistrationAddressRole`, and `PostalAddressRole` are particularly relevant.

No properties such as `street`, `houseNumber`, `postalCode`, or `city` are introduced in the `conx-org` namespace.

### 10.3 `conx-contact:hasContactPoint`

Organizations and Organizational Units use the existing Contact ontology. The official homepage is modeled through the existing website contact channel:

```turtle
ex:bau-gmbh
    conx-contact:hasContactPoint ex:bau-gmbh-official-contact .

ex:bau-gmbh-official-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:official ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:bau-gmbh-website .

ex:bau-gmbh-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactURI <https://example.org/> .
```

No local `homepage` property is introduced.

## 11. Explicitly Deferred Terms

| Term | Rationale |
| --- | --- |
| `EconomicActor` | Not a class directly adopted from an evaluated core ontology; economic activity is expressed through roles |
| `Enterprise` | Legally and statistically context-dependent concept, particularly for SME assessments |
| `EconomicOperator` | Market or process role, not an intrinsic organization class |
| `FormalOrganization` | The external W3C ORG concept suffices as a future alignment target |
| `Post` / position | No confirmed need for permanent or vacant positions |
| `BusinessProfile` | Required only for multiple separate business identities of the same person |
| `hasLegalRepresentative` | Direct shortcut would bypass the extensible representation resource |
| `hasMember` / `memberOf` | Direct shortcuts are derivable from Membership and unnecessary as a second data direction in the MVP |
| `foundingDate` | Not identical to registration date and currently unnecessary |
| `activityStartDate` | Too ambiguous from a domain perspective and currently unnecessary |
| `homepage` | Already representable through `core/contact` |
| `FinancialAccount` | Belongs in a future payment or financial model |
| Credential class | No dedicated Credential module approved for the MVP |

## 12. Validation Profiles

### 12.1 Organization Core

- Explicit type `conx-org:Organization` or an established subclass,
- at least one non-empty `name` value,
- resource values for hierarchy, ADMS identifiers, AddressAssignments, and ContactPoints,
- no universal requirement for register identifier, legal form, or address.

### 12.2 Legal Entity Core

- All Organization Core rules,
- at least one non-empty `legalName` value,
- exactly one `registrationDate` as `xsd:date`,
- at least one structurally valid ADMS identifier,
- `legalForm` at most once and as a `skos:Concept`,
- requirements for a legal-address assignment checked against the existing Address Shapes in the SHACL requirements document.

### 12.3 Organizational Unit Core

- All Organization Core rules,
- at least one `unitOf` relationship to an Organization,
- no requirement for a separate legal form, legal name, or registration date.

### 12.4 Relationship Core

- `Membership`: exactly one `member` and one `membershipOrganization`,
- `LegalRepresentation`: exactly one `representedOrganization` and one `representative` Person,
- no embedded names or dates of birth in the representation.

## 13. Decisions for the SHACL Requirements

The previously open acceptance points are resolved in the [SHACL Requirements Document](06_shacl-requirements.md) as follows:

1. `registrationDate` is mandatory exactly once as `xsd:date` for every `LegalEntity`.
2. Every `LegalEntity` requires at least one structured ADMS identifier; specific identification schemes remain open in the core.
3. `legalForm` remains optional and is limited to at most one SKOS concept.
4. Membership role and validity period are not yet part of the MVP.
5. Hierarchy relationship pairs are implemented as OWL inverses; SHACL does not require both directions to be supplied explicitly.
6. Every `LegalEntity` requires at least one AddressAssignment with `LegalAddressRole`.

The interaction of these concepts is illustrated in the [Organization Diagram](diagrams/organization-concept-model.md).

## 14. Illustrative Example

> `legalName` denotes the legal name of a Legal Entity. A short brand name may additionally appear as `name` or `alternativeName`, but does not replace the legal name.
