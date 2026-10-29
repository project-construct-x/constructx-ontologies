# Domain-Specific SHACL Requirements for the Organization MVP

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Organization Core Shapes

## 1. Purpose

This document specifies the executable quality requirements for organizational data. It describes shape targets, constraints, severity levels, stable error codes, and valid and invalid scenarios.

It documents the implemented shape graph `shapes/conx-org-core.shacl.ttl`.

Foundations:

- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Term Catalog](05_term-catalog.md)
- [Conceptual Model](03_concept-model.md)
- [Source Analysis](01_source-analysis.md)
- [Organization Diagram](diagrams/organization-concept-model.md)

## 2. Implemented Shape Set

```text
Shape graph: modules/core/organization/shapes/conx-org-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/organization/core
Version IRI: https://www.construct-x.org/shapes/organization/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/organization/core#
Prefix:      conx-org-sh
Version:     0.1.0
```

These IRIs are implemented as binding identifiers in the shape graph and module metadata for version `0.1.0`.

## 3. Validation Principles

### 3.1 OWL and SHACL

- OWL describes meaning, subclasses, domain, range, and inverse relationships under the open-world assumption.
- SHACL checks the actual data graph supplied.
- Mandatory fields and maximum cardinalities are enforced exclusively by the Core Shapes as a data contract.
- The shapes remain open to additional properties; `sh:closed true` is not intended.
- SHACL maximum cardinalities do not automatically become OWL cardinality axioms.
- Validation is performed with the Organization, Agent, Person, Address, and Contact T-Boxes and the required reference graphs.

### 3.2 Explicit Typing

Resources using Organization, Legal Entity, Organizational Unit, Membership, or Legal Representation properties must explicitly have the appropriate local type. Domain inference alone does not replace this data requirement.

Subclass conclusions between `LegalEntity`, `OrganizationalUnit`, `Organization`, and `Agent` may follow from the loaded T-Box. A `LegalEntity` therefore need not additionally be typed redundantly as `Organization` and `Agent`.

### 3.3 Resource Form

All five MVP resource types must be referenced through IRIs:

- `Organization`,
- `LegalEntity`,
- `OrganizationalUnit`,
- `Membership`,
- `LegalRepresentation`.

Blank nodes are not permitted for these domain-stable resources in the core profile. ADMS identifiers and existing Address or Contact resources follow their respective shape-set rules and may permit blank nodes.

### 3.4 Severity Levels

All core violations described in this document use `sh:Violation`. The Core Shape produces no warnings for optional recommendations such as legal form, activity, headquarters address, or additional identifiers.

Future application profiles may use `sh:Warning` and `sh:Info` or add stricter `sh:Violation` rules.

### 3.5 Error Messages

Every constraint component receives:

- a German `sh:message`,
- an English `sh:message`,
- a stable requirement identifier,
- a specific result path wherever SHACL can determine one.

## 4. Responsibility Boundaries

| Requirement | Responsible Shape Set | Rule in the Organization Shape |
| --- | --- | --- |
| Organization classes, names, and structure | `organization/core` | Validate fully |
| Legal name, registration date, and legal form | `organization/core` | Validate fully according to MVP rules |
| ADMS identifiers on Organization and Membership | `organization/core` with the existing ADMS pattern | Check the minimal structure through nested validation |
| Specific register, VAT, LEI, EUID, EORI, or GLN schemes | Future domain or jurisdiction profiles | No allowlist check |
| AddressAssignment and address components | `address/core` | Reuse existing shapes |
| At least one legal address for a Legal Entity | `organization/core` plus `address/core` | Require an AddressAssignment with `LegalAddressRole` |
| Contact points and homepage | `contact/core` | Do not duplicate contact payloads in the Organization Shape |
| Personal data | `person/core` | Check only the Person reference of the representation |
| Seller, buyer, and other process roles | Domain/Participation Shapes | Outside Organization Core validation |
| Insurance, qualifications, and compliance | Future external evidence profiles | Outside Organization Core validation |
| Bank accounts and payment data | Future Payment/Finance Shape | Outside Organization Core validation |

## 5. Approved MVP Requirements

The SHACL questions identified in the term catalog are resolved for this requirements document as follows:

| Topic | Decision |
| --- | --- |
| `registrationDate` | Mandatory exactly once as `xsd:date` for every `LegalEntity` |
| ADMS identifier of a `LegalEntity` | At least one structurally valid identifier is mandatory; specific schemes remain open |
| `legalForm` | Optional, at most one value as an IRI and `skos:Concept` |
| Membership role and period | Outside the MVP |
| Inverse hierarchy relationships | Implemented as OWL inverses; SHACL does not require both data directions |
| Legal address | At least one AddressAssignment with `LegalAddressRole` per `LegalEntity` |
| Headquarters address | Optional; no core requirement |
| Legal-form and activity vocabularies | Open `skos:Concept` reference without a closed value list |

The requirement for at least one ADMS identifier establishes only that a structured identifier was supplied. Without a future jurisdiction profile, the Core Shape does not determine whether the identifier suffices as a legally reliable register identifier.

## 6. Shape Catalog

### 6.1 Local Shapes

| Shape IRI | Type | Target or Usage | Purpose |
| --- | --- | --- | --- |
| `conx-org-sh:NonEmptyStringOrLangStringShape` | Reusable Node Shape | Referenced by name Property Shapes | Allows non-empty `xsd:string` or `rdf:langString` values |
| `conx-id-sh:ADMSIdentifierShape` | Reusable Node Shape from `identifier/core` | Values of `adms:identifier` | Checks type, notation, and scheme agency according to the shared minimal contract |
| `conx-org-sh:LegalAddressAssignmentShape` | Reusable Node Shape | Qualified values of `hasAddressAssignment` | Checks AddressAssignment type and `LegalAddressRole` |
| `conx-org-sh:OrganizationShape` | Node Shape | `Organization` and subjects of general Organization properties | Checks IRI, type, name, optional master data, hierarchy, and optional identifiers |
| `conx-org-sh:LegalEntityShape` | Node Shape | `LegalEntity` and subjects of legal properties | Adds legal name, registration date, minimum identifiers, legal form, and legal address |
| `conx-org-sh:OrganizationalUnitShape` | Node Shape | `OrganizationalUnit` and subjects of `unitOf` | Adds at least one parent Organization |
| `conx-org-sh:MembershipShape` | Node Shape | `Membership` and subjects of its properties | Checks exactly one member and one receiving Organization |
| `conx-org-sh:LegalRepresentationShape` | Node Shape | `LegalRepresentation` and subjects of its properties | Checks exactly one Legal Entity and one Person |

### 6.2 Reused Shapes

| Shape | Owner | Usage |
| --- | --- | --- |
| `conx-addr-sh:ResourceWithAddressAssignmentShape` | `address/core` | Checks values of `hasAddressAssignment` |
| `conx-addr-sh:AddressAssignmentShape` | `address/core` | Checks `assignedAddress`, `addressRole`, and other assignment data |
| `conx-addr-sh:AddressShape` | `address/core` | Checks the address itself |
| `conx-contact-sh:ContactCarrierShape` | `contact/core` | Checks values of `hasContactPoint` |
| `conx-contact-sh:ContactPointShape` | `contact/core` | Checks contact point, usage, purpose, and methods |
| `conx-contact-sh:ContactMethodShape` | `contact/core` | Checks contact channel and payload, including website IRI |
| `conx-person-sh:PersonShape` | `person/core` | Checks the referenced Person in a representation where personal data is included in the graph |

The Organization Shape imports the versioned `identifier/core` shape graph and uses its `conx-id-sh:ADMSIdentifierShape`. Domain-specific minimum counts for Organization, Legal Entity, and Membership remain defined in the Organization Shape.

## 7. Targets

### 7.1 `OrganizationShape`

Targets:

- `sh:targetClass conx-org:Organization`,
- `sh:targetSubjectsOf conx-org:name`,
- `sh:targetSubjectsOf conx-org:alternativeName`,
- `sh:targetSubjectsOf conx-org:activity`,
- `sh:targetSubjectsOf conx-org:subOrganizationOf`,
- `sh:targetSubjectsOf conx-org:hasSubOrganization`,
- `sh:targetSubjectsOf conx-org:hasUnit`.

`adms:identifier`, `conx-addr:hasAddressAssignment`, and `conx-contact:hasContactPoint` are generic properties. They must not automatically turn every subject using them into an Organization target. They are checked only within already recognized organizations or covered by their own shape sets.

### 7.2 `LegalEntityShape`

Targets:

- `sh:targetClass conx-org:LegalEntity`,
- `sh:targetSubjectsOf conx-org:legalName`,
- `sh:targetSubjectsOf conx-org:legalForm`,
- `sh:targetSubjectsOf conx-org:registrationDate`,
- `sh:targetObjectsOf conx-org:representedOrganization`.

The shape additionally references the shared Organization contract so that name and general Organization properties are checked even for a resource typed only as `LegalEntity`.

### 7.3 `OrganizationalUnitShape`

Targets:

- `sh:targetClass conx-org:OrganizationalUnit`,
- `sh:targetSubjectsOf conx-org:unitOf`,
- `sh:targetObjectsOf conx-org:hasUnit`.

This shape also references the shared Organization contract.

### 7.4 `MembershipShape`

Targets:

- `sh:targetClass conx-org:Membership`,
- `sh:targetSubjectsOf conx-org:member`,
- `sh:targetSubjectsOf conx-org:membershipOrganization`.

An Agent or Organization does not become a Membership target merely by being the object of a Membership property.

### 7.5 `LegalRepresentationShape`

Targets:

- `sh:targetClass conx-org:LegalRepresentation`,
- `sh:targetSubjectsOf conx-org:representedOrganization`,
- `sh:targetSubjectsOf conx-org:representative`.

## 8. Shared Literal Rules

`name`, `legalName`, and `alternativeName` accept:

- `xsd:string`,
- `rdf:langString`.

Every value must contain at least one non-whitespace character. A rule equivalent to `sh:pattern "\\S"` must be provided.

The following are not permitted:

- empty literals,
- values consisting entirely of whitespace,
- numeric values,
- IRIs or blank nodes as names.

`sh:uniqueLang` is not used in the core. An organization may have multiple names in the same language or in different writing systems.

## 9. `OrganizationShape`

### 9.1 Node Constraints

| ID | Constraint | SHACL Requirement |
| --- | --- | --- |
| `ORG-001` | Referenceable Organization | Focus resource must satisfy `sh:nodeKind sh:IRI` |
| `ORG-002` | Organization type | Focus resource must be a `conx-org:Organization` or a subclass established by the loaded T-Box |

### 9.2 Property Constraints

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `ORG-010` | `conx-org:name` | 1 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `ORG-011` | `conx-org:alternativeName` | 0 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `ORG-020` | `conx-org:activity` | 0 | Unbounded | IRI and instance of `skos:Concept` |
| `ORG-030` | `adms:identifier` | 0 | Unbounded | Blank node or IRI, valid according to `conx-id-sh:ADMSIdentifierShape` |
| `ORG-040` | `conx-org:subOrganizationOf` | 0 | Unbounded | IRI and instance of `conx-org:Organization` |
| `ORG-041` | `conx-org:hasSubOrganization` | 0 | Unbounded | IRI and instance of `conx-org:Organization` |
| `ORG-042` | Direct self-subordination | 0 | 0 | Focus resource must not be its own value of `subOrganizationOf` or `hasSubOrganization` |
| `ORG-043` | `conx-org:hasUnit` | 0 | Unbounded | IRI and instance of `conx-org:OrganizationalUnit` |

### 9.3 Hierarchy Rules

`subOrganizationOf` and `hasSubOrganization` are intended as inverse OWL properties. The Core Shape requires only that supplied values are correctly typed. It does not require both directions to be explicitly present in the data graph.

Direct self-reference is not permitted. A small SPARQL constraint or equivalent SHACL pattern must be provided.

Longer cycles such as A → B → C → A are not checked in the MVP. Whether they are prohibited depends on the subsequently refined meaning of different hierarchy relationships and would require recursive path validation.

`subOrganizationOf` asserts no ownership or control relationship. Such relationships are therefore neither required nor inferred from the hierarchy.

## 10. `LegalEntityShape`

### 10.1 Node Constraints

| ID | Constraint | SHACL Requirement |
| --- | --- | --- |
| `LE-001` | Referenceable Legal Entity | Focus resource must satisfy `sh:nodeKind sh:IRI` |
| `LE-002` | Explicit Legal Entity type | Focus resource must satisfy `sh:class conx-org:LegalEntity` |
| `LE-003` | Organization contract | Focus resource must additionally satisfy the shared Organization contract |

### 10.2 Property Constraints

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | --- | --- | --- |
| `LE-010` | `conx-org:legalName` | 1 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `LE-020` | `conx-org:registrationDate` | 1 | 1 | Lexically valid `xsd:date` |
| `LE-030` | `conx-org:legalForm` | 0 | 1 | IRI and instance of `skos:Concept` |
| `LE-040` | `adms:identifier` | 1 | Unbounded | Blank node or IRI, valid according to `conx-id-sh:ADMSIdentifierShape` |
| `LE-050` | `conx-addr:hasAddressAssignment` | Qualified minimum 1 | Unbounded | At least one AddressAssignment with `roles:LegalAddressRole` |

### 10.3 Registration Date

`registrationDate` accepts only `xsd:date`. The following are not permitted:

- untyped date strings,
- `xsd:gYear` or `xsd:gYearMonth`,
- multiple registration dates,
- a literal with an invalid `xsd:date` lexical form.

A time-dependent rule stating “registration date must not be in the future” is not introduced in the core. It may be added in a stricter profile with a controlled execution time.

`registrationDate` must not be equated with founding or start of activity.

### 10.4 Legal Form

`legalForm` is optional in the MVP. If present, the value must:

1. be an IRI,
2. be typed as `skos:Concept`.

The Core Shape checks neither a closed GLEIF/ISO 20275 value set nor consistency with a jurisdiction. A literal such as `"GmbH"` is nevertheless invalid because it does not identify the legal-form vocabulary used.

### 10.5 Legal Address

At least one value of `conx-addr:hasAddressAssignment` must:

- be a blank node or IRI,
- be typed as `conx-addr:AddressAssignment`,
- have `conx-addr:addressRole roles:LegalAddressRole`.

The implementation uses a qualified minimum cardinality, for example `sh:qualifiedValueShape` with `sh:qualifiedMinCount 1`.

The existing Address Shape additionally checks:

- exactly one `assignedAddress`,
- at least one `addressRole`,
- type and structure of the assigned address.

The Organization Shape does not duplicate these rules. It also does not require a globally inappropriate component list of street, building number, postal code, and locality. Country-specific Address profiles may add such rules later.

One AddressAssignment may simultaneously have legal, registration, and headquarters roles. The Core Shape does not require three separate AddressAssignments.

## 11. ADMS Identifiers

The structural rules and error codes originate from the imported `identifier/core` shape graph. The Organization Shape retains the domain-specific cardinalities for Organization, Legal Entity, and Membership.

### 11.1 Minimal Structure

Every identifier referenced through `adms:identifier` must satisfy:

| ID | Property | Requirement |
| --- | --- | --- |
| `ID-001` | Type | Resource is an `adms:Identifier` |
| `ID-002` | `skos:notation` | Exactly one literal |
| `ID-003` | `adms:schemaAgency` | Optional, at most one `xsd:string` |

The identifier itself may be a blank node or IRI. `skos:notation` must be a literal; its datatype may designate the identification scheme.

### 11.2 Legal Entity Minimum

A `LegalEntity` must have at least one validly structured ADMS identifier. The Core Shape does not yet check:

- whether the notation datatype belongs to an approved list of register schemes,
- whether the identifier matches the jurisdiction,
- whether VAT ID, LEI, EUID, EORI, or GLN suffices as a primary identifier,
- whether the identifier exists in an external register,
- whether name and address match the register entry.

These checks remain reserved for future profiles and external validation services.

### 11.3 Identifiers of Other Resources

`Organization` and `OrganizationalUnit` may optionally have ADMS identifiers. `Membership` may carry a membership number as an ADMS identifier. The same minimal structure applies whenever such identifiers are present.

A membership number belongs to the Membership rather than automatically to the member. Customer, supplier, or tenant numbers belong to their respective business relationships and are outside this shape set.

## 12. `OrganizationalUnitShape`

### 12.1 Node Constraints

| ID | Constraint | SHACL Requirement |
| --- | --- | --- |
| `UNIT-001` | Referenceable Organizational Unit | Focus resource must satisfy `sh:nodeKind sh:IRI` |
| `UNIT-002` | Explicit Unit type | Focus resource must satisfy `sh:class conx-org:OrganizationalUnit` |
| `UNIT-003` | Organization contract | Focus resource must additionally satisfy the shared Organization contract |

### 12.2 Property Constraints

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `UNIT-010` | `conx-org:unitOf` | 1 | Unbounded | IRI and instance of `conx-org:Organization` |
| `UNIT-011` | Direct self-assignment | 0 | 0 | Organizational Unit must not be `unitOf` itself |

`unitOf` and `hasUnit` are implemented as inverse OWL properties. The shape does not require both directions to be supplied explicitly.

Multiple `unitOf` values remain permitted to support matrix organizations. A narrower profile may later require a primary parent organization or exactly one parent organization.

An Organizational Unit requires neither `legalName`, `legalForm`, `registrationDate`, nor a legal address. It may have its own contacts, address assignments, and structured identifiers.

## 13. `MembershipShape`

### 13.1 Node Constraints

| ID | Constraint | SHACL Requirement |
| --- | --- | --- |
| `MEM-001` | Referenceable Membership | Focus resource must satisfy `sh:nodeKind sh:IRI` |
| `MEM-002` | Explicit Membership type | Focus resource must satisfy `sh:class conx-org:Membership` |

### 13.2 Property Constraints

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `MEM-010` | `conx-org:member` | 1 | 1 | IRI and instance of `conx-agent:Agent` |
| `MEM-011` | `conx-org:membershipOrganization` | 1 | 1 | IRI and instance of `conx-org:Organization` |
| `MEM-012` | `adms:identifier` | 0 | Unbounded | Blank node or IRI, valid according to `conx-id-sh:ADMSIdentifierShape` |
| `MEM-020` | Self-membership | 0 | 0 | The same IRI value must not be both member and receiving Organization |

The member may be a person or an organization because both are subclasses of `Agent`. The Membership itself must not be used as a member unless it is additionally typed as an Agent contrary to the model; such multiple typing should be avoided from a domain perspective.

Membership role, status, start, and end are outside version 0.1.0. Shapes must therefore neither require these elements nor report their absence.

The self-membership rule requires a SPARQL constraint or equivalent SHACL pattern comparing `member` and `membershipOrganization` values.

## 14. `LegalRepresentationShape`

### 14.1 Node Constraints

| ID | Constraint | SHACL Requirement |
| --- | --- | --- |
| `REP-001` | Referenceable representation | Focus resource must satisfy `sh:nodeKind sh:IRI` |
| `REP-002` | Explicit representation type | Focus resource must satisfy `sh:class conx-org:LegalRepresentation` |

### 14.2 Property Constraints

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `REP-010` | `conx-org:representedOrganization` | 1 | 1 | IRI and instance of `conx-org:LegalEntity` |
| `REP-011` | `conx-org:representative` | 1 | 1 | IRI and instance of `conx-person:Person` |

The representation resource does not copy personal data. If a representation resource nevertheless uses properties such as `conx-person:birthDate` or `conx-person:fullName`, the Person Shape targets additionally recognize it as a personal-data resource, and it would have to satisfy the Person contract. The Organization Shape itself therefore does not use `sh:closed true`.

The following are not checked:

- representation type,
- sole or joint representation,
- start or end of representation,
- register source,
- power-of-attorney text,
- external evidence.

These concepts are outside the MVP.

## 15. Address and Contact Contracts

### 15.1 Address

Every supplied value of `conx-addr:hasAddressAssignment` is checked by the Address Core Shape. For Legal Entities, the Organization Shape adds only the qualified requirement for a legal address.

The Organization Shape does not itself check:

- street and building number,
- postal code and locality,
- country and administrative unit,
- geographic position,
- `attentionOf`, `careOf`, or department text.

### 15.2 Contact

Every supplied value of `conx-contact:hasContactPoint` is checked by the Contact Core Shape. The Organization Shape requires neither a contact point nor a homepage in the core.

A valid official homepage uses:

```text
contact-usage:official
contact-purpose:general
contact-channel:website
contactURI as an IRI
```

No new `conx-org:homepage` property is provided in either the shape or the T-Box.

## 16. Error Message Catalog

### 16.1 Organization

| ID | German | English |
| --- | --- | --- |
| `ORG-001` | Eine Organisation muss durch eine IRI referenziert werden. | An Organization must be referenced by an IRI. |
| `ORG-002` | Eine Ressource mit Organisationseigenschaften muss als conx-org:Organization oder bestätigte Unterklasse typisiert sein. | A resource using Organization properties must be typed as conx-org:Organization or an established subclass. |
| `ORG-010` | Eine Organisation muss mindestens einen nicht leeren Namen besitzen. | An Organization must have at least one non-empty name. |
| `ORG-011` | Jeder alternative Name muss ein nicht leerer String oder sprachmarkierter String sein. | Every alternative name must be a non-empty string or language-tagged string. |
| `ORG-020` | Jede Tätigkeit muss auf ein referenzierbares SKOS-Konzept verweisen. | Every activity must reference a SKOS concept by IRI. |
| `ORG-030` | Jeder Organisationsidentifikator muss eine gültig strukturierte ADMS-Identifier-Ressource sein. | Every Organization identifier must be a valid structured ADMS Identifier resource. |
| `ORG-040` | Jede übergeordnete Organisation muss durch eine Organization-IRI referenziert werden. | Every parent organization must be referenced by an Organization IRI. |
| `ORG-041` | Jede untergeordnete Organisation muss durch eine Organization-IRI referenziert werden. | Every subordinate organization must be referenced by an Organization IRI. |
| `ORG-042` | Eine Organisation darf nicht unmittelbar sich selbst über- oder untergeordnet sein. | An Organization must not be its own direct parent or subordinate organization. |
| `ORG-043` | Jeder Wert von hasUnit muss auf eine OrganizationalUnit-IRI verweisen. | Every hasUnit value must reference an OrganizationalUnit IRI. |

### 16.2 Legal Entity

| ID | German | English |
| --- | --- | --- |
| `LE-001` | Eine Legal Entity muss durch eine IRI referenziert werden. | A Legal Entity must be referenced by an IRI. |
| `LE-002` | Eine Ressource mit Legal-Entity-Eigenschaften muss explizit als conx-org:LegalEntity typisiert sein. | A resource using Legal Entity properties must be explicitly typed as conx-org:LegalEntity. |
| `LE-003` | Eine Legal Entity muss den allgemeinen Organization-Vertrag erfüllen. | A Legal Entity must conform to the general Organization contract. |
| `LE-010` | Eine Legal Entity muss mindestens einen nicht leeren rechtlichen Namen besitzen. | A Legal Entity must have at least one non-empty legal name. |
| `LE-020` | Eine Legal Entity muss genau ein Registrierungsdatum mit dem Datentyp xsd:date besitzen. | A Legal Entity must have exactly one registration date using datatype xsd:date. |
| `LE-030` | Die Rechtsform darf höchstens einmal vorkommen und muss auf ein SKOS-Konzept verweisen. | The legal form may occur at most once and must reference a SKOS concept. |
| `LE-040` | Eine Legal Entity muss mindestens einen gültig strukturierten ADMS-Identifier besitzen. | A Legal Entity must have at least one valid structured ADMS Identifier. |
| `LE-050` | Eine Legal Entity muss mindestens eine AddressAssignment mit der Rolle LegalAddressRole besitzen. | A Legal Entity must have at least one AddressAssignment with the LegalAddressRole. |

### 16.3 Organizational Unit

| ID | German | English |
| --- | --- | --- |
| `UNIT-001` | Eine Organisationseinheit muss durch eine IRI referenziert werden. | An Organizational Unit must be referenced by an IRI. |
| `UNIT-002` | Eine Ressource mit Unit-Eigenschaften muss explizit als conx-org:OrganizationalUnit typisiert sein. | A resource using Organizational Unit properties must be explicitly typed as conx-org:OrganizationalUnit. |
| `UNIT-003` | Eine Organisationseinheit muss den allgemeinen Organization-Vertrag erfüllen. | An Organizational Unit must conform to the general Organization contract. |
| `UNIT-010` | Eine Organisationseinheit muss mindestens einer Organization über unitOf zugeordnet sein. | An Organizational Unit must be assigned to at least one Organization through unitOf. |
| `UNIT-011` | Eine Organisationseinheit darf nicht unitOf ihrer selbst sein. | An Organizational Unit must not be unitOf itself. |

### 16.4 Membership

| ID | German | English |
| --- | --- | --- |
| `MEM-001` | Eine Membership muss durch eine IRI referenziert werden. | A Membership must be referenced by an IRI. |
| `MEM-002` | Eine Mitgliedschaftsressource muss explizit als conx-org:Membership typisiert sein. | A membership resource must be explicitly typed as conx-org:Membership. |
| `MEM-010` | Eine Membership muss genau einen durch eine Agent-IRI referenzierten Member besitzen. | A Membership must have exactly one member referenced by an Agent IRI. |
| `MEM-011` | Eine Membership muss genau eine aufnehmende Organization besitzen. | A Membership must have exactly one membership Organization. |
| `MEM-012` | Jeder Mitgliedschaftsidentifikator muss eine gültig strukturierte ADMS-Identifier-Ressource sein. | Every Membership identifier must be a valid structured ADMS Identifier resource. |
| `MEM-020` | Eine Organisation darf nicht Mitglied ihrer selbst sein. | An Organization must not be a member of itself. |

### 16.5 Legal Representation

| ID | German | English |
| --- | --- | --- |
| `REP-001` | Eine LegalRepresentation muss durch eine IRI referenziert werden. | A LegalRepresentation must be referenced by an IRI. |
| `REP-002` | Eine Vertretungsressource muss explizit als conx-org:LegalRepresentation typisiert sein. | A representation resource must be explicitly typed as conx-org:LegalRepresentation. |
| `REP-010` | Eine LegalRepresentation muss genau eine Legal Entity als vertretene Organisation referenzieren. | A LegalRepresentation must reference exactly one Legal Entity as the represented organization. |
| `REP-011` | Eine LegalRepresentation muss genau eine Person als rechtliche Vertretung referenzieren. | A LegalRepresentation must reference exactly one Person as its legal representative. |

### 16.6 Shared ADMS Messages

| ID | German | English |
| --- | --- | --- |
| `ID-001` | Eine Identifikatorressource muss als adms:Identifier typisiert sein. | An identifier resource must be typed as adms:Identifier. |
| `ID-002` | Ein Identifikator muss genau eine literale skos:notation besitzen. | An identifier must have exactly one literal skos:notation. |
| `ID-003` | schemaAgency darf höchstens einmal als String angegeben werden. | schemaAgency may be provided at most once as a string. |

## 17. Shared Prefixes for the Example Scenarios

The following prefixes apply to all examples in this document:

```turtle
@prefix conx-agent: <https://www.construct-x.org/ontology/agent#> .
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix conx-org: <https://www.construct-x.org/ontology/organization#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix roles: <https://www.construct-x.org/vocab/address-role#> .
@prefix contact-channel: <https://www.construct-x.org/vocab/contact-channel#> .
@prefix contact-purpose: <https://www.construct-x.org/vocab/contact-purpose#> .
@prefix contact-usage: <https://www.construct-x.org/vocab/contact-usage#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .
@prefix ex-scheme: <https://example.org/id-scheme/> .
```

The example datatypes under `ex-scheme:` are placeholders for Organization identification schemes that have not yet been established. They must not be interpreted as already published Construct-X schemes.

## 18. Valid Scenarios

### V-01: Minimal General Organization

```turtle
ex:bauverband
    a conx-org:Organization ;
    conx-org:name "Bauverband Beispielregion"@de .
```

Expected result: valid. A general Organization requires neither legal form, registration date, identifier, nor address.

### V-02: Complete Legal Entity

```turtle
ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date ;
    adms:identifier ex:bau-gmbh-register-id ;
    conx-addr:hasAddressAssignment ex:bau-gmbh-legal-address .

ex:bau-gmbh-register-id
    a adms:Identifier ;
    skos:notation "HRB 12345"^^ex-scheme:local-register-number ;
    adms:schemaAgency "Zuständige Registerstelle" .

ex:bau-gmbh-legal-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:bau-gmbh-address ;
    conx-addr:addressRole roles:LegalAddressRole,
                          roles:RegistrationAddressRole .

ex:bau-gmbh-address
    a conx-addr:Address ;
    conx-addr:streetName "Beispielstraße" ;
    conx-addr:houseNumber "12" ;
    conx-addr:postalCode "44787" ;
    conx-addr:localityName "Bochum" .
```

Expected result: valid. The same AddressAssignment satisfies both the legal and registration address roles.

### V-03: Legal Entity with Optional Legal Form and Activity

```turtle
ex:planung-ag
    a conx-org:LegalEntity ;
    conx-org:name "Planung AG" ;
    conx-org:legalName "Planung Beispiel Aktiengesellschaft"@de ;
    conx-org:registrationDate "2020-02-03"^^xsd:date ;
    conx-org:legalForm ex:legal-form-ag ;
    conx-org:activity ex:nace-activity ;
    adms:identifier ex:planung-ag-id ;
    conx-addr:hasAddressAssignment ex:planung-ag-legal-address .

ex:legal-form-ag a skos:Concept .
ex:nace-activity a skos:Concept .

ex:planung-ag-id
    a adms:Identifier ;
    skos:notation "REG-9876"^^ex-scheme:local-register-number .

ex:planung-ag-legal-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:planung-ag-address ;
    conx-addr:addressRole roles:LegalAddressRole .

ex:planung-ag-address a conx-addr:Address .
```

Expected result: valid. The Core Shape checks SKOS types, but not whether the concepts originate from ISO 20275 or NACE.

### V-04: Organizational Unit with Matrix Assignment

```turtle
ex:central-procurement
    a conx-org:OrganizationalUnit ;
    conx-org:name "Zentraler Einkauf"@de ;
    conx-org:unitOf ex:bau-gmbh,
                    ex:planung-ag .
```

Expected result: valid, provided both target resources are typed as Organization or a subclass and are available in the validation graph. Multiple `unitOf` values are permitted in the core.

### V-05: Membership of an Organization

```turtle
ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband ;
    adms:identifier ex:membership-number-4711 .

ex:membership-number-4711
    a adms:Identifier ;
    skos:notation "4711"^^ex-scheme:association-membership-number ;
    adms:schemaAgency "Bauverband Beispielregion" .
```

Expected result: valid. The membership number belongs to the Membership.

### V-06: Membership of a Person

```turtle
ex:person-123 a conx-person:Person ;
    conx-person:fullName "Maria Beispiel" ;
    conx-person:givenName "Maria" .

ex:person-membership
    a conx-org:Membership ;
    conx-org:member ex:person-123 ;
    conx-org:membershipOrganization ex:bauverband .
```

Expected result: valid. `Person` is a subclass of `Agent` through the loaded T-Box.

### V-07: Legal Representation

```turtle
ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

Expected result: valid. The representation references the Person and contains no copied personal data.

### V-08: Official Homepage through Contact

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

Expected result: valid in the combined Organization, Contact, and Address validation run. The Organization Shape requires no dedicated homepage property.

### V-09: Hierarchy in One Data Direction

```turtle
ex:regional-office
    a conx-org:Organization ;
    conx-org:name "Regionalorganisation West"@de ;
    conx-org:subOrganizationOf ex:bauverband .
```

Expected result: valid. `ex:bauverband conx-org:hasSubOrganization ex:regional-office` need not additionally be stored explicitly.

## 19. Invalid Scenarios

### I-01: Organization as a Blank Node

```turtle
[] a conx-org:Organization ;
   conx-org:name "Nicht stabil referenzierbar" .
```

Expected violation: `ORG-001`.

### I-02: Organization Property without Organization Type or Name

```turtle
ex:untyped-resource
    conx-org:alternativeName "Beispiel" .
```

Expected violations: `ORG-002`, `ORG-010`.

### I-03: Invalid Names and Activity

```turtle
ex:invalid-name-org
    a conx-org:Organization ;
    conx-org:name "   ", 42 ;
    conx-org:alternativeName "" ;
    conx-org:activity "Bauwirtschaft" .
```

Expected violations: `ORG-010`, `ORG-011`, `ORG-020`. An activity must reference a SKOS concept through an IRI.

### I-04: Incomplete Legal Entity

```turtle
ex:incomplete-company
    a conx-org:LegalEntity ;
    conx-org:name "Unvollständig" .
```

Expected violations: `LE-010`, `LE-020`, `LE-040`, `LE-050`.

### I-05: Incorrect and Multiple Registration Dates

```turtle
ex:invalid-date-company
    a conx-org:LegalEntity ;
    conx-org:name "Datum Fehler" ;
    conx-org:legalName "Datum Fehler GmbH" ;
    conx-org:registrationDate "2020"^^xsd:gYear,
                              "2020-01-02"^^xsd:date .
```

Expected violation: `LE-020`; this isolated example additionally lacks an identifier and legal address (`LE-040`, `LE-050`).

### I-06: Legal Form as a Literal and with Multiple Values

```turtle
ex:invalid-legal-form-company
    a conx-org:LegalEntity ;
    conx-org:legalForm "GmbH",
                       ex:legal-form-gmbh .

ex:legal-form-gmbh a skos:Concept .
```

Expected violation: `LE-030`; additional violations of mandatory Legal Entity requirements may occur in this isolated example.

### I-07: Identifier without Type or Notation

```turtle
ex:invalid-identifier-company
    a conx-org:LegalEntity ;
    conx-org:name "Kennungsfehler" ;
    conx-org:legalName "Kennungsfehler GmbH" ;
    conx-org:registrationDate "2021-05-06"^^xsd:date ;
    adms:identifier ex:broken-identifier .

ex:broken-identifier
    adms:schemaAgency "Registerstelle" .
```

Expected violations: `ORG-030` or `LE-040`, `ID-001`, `ID-002`; the legal address is also missing (`LE-050`).

### I-08: Address without the Legal Address Role

```turtle
ex:no-legal-address-company
    a conx-org:LegalEntity ;
    conx-org:name "Adressfehler" ;
    conx-org:legalName "Adressfehler GmbH" ;
    conx-org:registrationDate "2019-03-04"^^xsd:date ;
    adms:identifier ex:valid-company-id ;
    conx-addr:hasAddressAssignment ex:postal-only-assignment .

ex:valid-company-id
    a adms:Identifier ;
    skos:notation "REG-1"^^ex-scheme:local-register-number .

ex:postal-only-assignment
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:postal-address ;
    conx-addr:addressRole roles:PostalAddressRole .

ex:postal-address a conx-addr:Address .
```

Expected violation: `LE-050`. The existing postal address does not replace the legal address role.

### I-09: Organizational Unit without a Parent Organization

```turtle
ex:orphan-unit
    a conx-org:OrganizationalUnit ;
    conx-org:name "Verwaiste Einheit" .
```

Expected violation: `UNIT-010`.

### I-10: Organizational Unit References Itself

```turtle
ex:self-unit
    a conx-org:OrganizationalUnit ;
    conx-org:name "Selbstbezug" ;
    conx-org:unitOf ex:self-unit .
```

Expected violation: `UNIT-011`.

### I-11: Invalid Organizational Hierarchy

```turtle
ex:self-parent
    a conx-org:Organization ;
    conx-org:name "Selbsthierarchie" ;
    conx-org:subOrganizationOf ex:self-parent .

ex:wrong-parent
    a conx-org:Organization ;
    conx-org:name "Falsche Oberorganisation" ;
    conx-org:subOrganizationOf ex:not-an-organization .

ex:wrong-child
    a conx-org:Organization ;
    conx-org:name "Falsche Unterorganisation" ;
    conx-org:hasSubOrganization ex:not-an-organization .

ex:wrong-unit-target
    a conx-org:Organization ;
    conx-org:name "Falsches Unit-Ziel" ;
    conx-org:hasUnit ex:not-a-unit .

ex:not-an-organization a skos:Concept .

ex:not-a-unit a conx-org:Organization ;
    conx-org:name "Keine Organisationseinheit" .
```

Expected violations: `ORG-040`, `ORG-041`, `ORG-042`, `ORG-043`.

### I-12: Membership without Unambiguous Endpoints

```turtle
ex:invalid-membership
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh,
                    ex:planung-ag .
```

Expected violations: `MEM-010`, `MEM-011`.

### I-13: Self-Membership

```turtle
ex:self-membership
    a conx-org:Membership ;
    conx-org:member ex:bauverband ;
    conx-org:membershipOrganization ex:bauverband .
```

Expected violation: `MEM-020`.

### I-14: Representation Does Not Reference a Person

```turtle
ex:invalid-representation
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:bauverband .
```

Expected violation: `REP-011`, because `ex:bauverband` is an Organization rather than a Person.

### I-15: Representation with Multiple People

```turtle
ex:ambiguous-representation
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123,
                            ex:person-456 .
```

Expected violation: `REP-011`. Multiple representatives require multiple representation resources; joint representation rules are outside the MVP.

### I-16: Website as an Organization Property or Literal Payload

```turtle
ex:bau-gmbh
    conx-org:homepage "https://example.org/" ;
    conx-contact:hasContactPoint ex:broken-contact .

ex:broken-contact
    a conx-contact:ContactPoint ;
    conx-contact:hasContactMethod ex:broken-website .

ex:broken-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactValue "https://example.org/" .
```

Expected result: the open Organization Shape does not validate `conx-org:homepage` as a known core property, and it has no defined Construct-X semantics. The Contact Shape reports `CON-CM-020` for the website's literal payload. This scenario deliberately documents that open shapes do not prohibit unknown properties.

## 20. Implemented Test Catalog

### 20.1 Valid Test Graphs

| File | Content |
| --- | --- |
| `tests/valid/minimal-organization.ttl` | General Organization with only a name |
| `tests/valid/complete-legal-entity.ttl` | Legal name, registration date, identifier, legal address, optional legal form and activity |
| `tests/valid/organizational-unit.ttl` | Unit with one and multiple `unitOf` assignments |
| `tests/valid/memberships.ttl` | Person and Organization memberships with optional membership number |
| `tests/valid/legal-representation.ttl` | Representation resource between Legal Entity and Person |
| `tests/valid/official-homepage.ttl` | Organization with an official website through Contact |

### 20.2 Invalid Test Graphs

| File | Expected Error Codes |
| --- | --- |
| `tests/invalid/invalid-organization-name-and-type.ttl` | `ORG-001`, `ORG-002`, `ORG-010`, `ORG-011`, `ORG-020` |
| `tests/invalid/invalid-legal-entity-core.ttl` | `LE-001`, `LE-002`, `LE-003`, `LE-010`, `LE-020`, `LE-040`, `LE-050` |
| `tests/invalid/invalid-registration-and-legal-form.ttl` | `LE-020`, `LE-030` |
| `tests/invalid/invalid-identifier-and-address.ttl` | `ORG-030`, `LE-040`, `LE-050`, `ID-001`, `ID-002`, `ID-003` |
| `tests/invalid/invalid-organizational-unit.ttl` | `UNIT-001`, `UNIT-002`, `UNIT-003`, `UNIT-010`, `UNIT-011` |
| `tests/invalid/invalid-hierarchy.ttl` | `ORG-040`, `ORG-041`, `ORG-042`, `ORG-043` |
| `tests/invalid/invalid-membership.ttl` | `MEM-001`, `MEM-002`, `MEM-010`, `MEM-011`, `MEM-012`, `MEM-020` |
| `tests/invalid/invalid-legal-representation.ttl` | `REP-001`, `REP-002`, `REP-010`, `REP-011` |

## 21. Requirements for Automated Tests

The automated tests check at least:

1. Every valid test graph validates without `sh:Violation`.
2. Every invalid test graph produces all error codes documented for it.
3. Every local shape IRI and error code is unique.
4. All shape messages are available in German and English.
5. Organization, Agent, Person, Address, and Contact T-Boxes are included in the combined validation run.
6. Address and Contact Core Shapes are loaded together whenever the test graph uses corresponding properties.
7. A Legal Entity passes only with a name, legal name, exactly one registration date, at least one ADMS identifier, and at least one legal address.
8. An Organization without legal specialization remains valid without a registration date, identifier, or address.
9. An Organizational Unit passes only with a name and at least one `unitOf`.
10. Membership and LegalRepresentation each enforce exactly one value per endpoint property.
11. Blank nodes for the five local MVP classes are rejected.
12. Direct self-hierarchy, self-assignment of a unit, and self-membership are rejected.
13. Both inverse hierarchy directions are not required as input.
14. The Organization Shape remains open and does not prohibit external properties.
15. No rule requires `EconomicActor`, local `FormalOrganization`, `Post`, a Credential class, or `homepage`.
16. Every documented error code is triggered by at least one invalid test graph.

## 22. Deliberately Excluded Core Checks

- Closed list of legally permitted register and tax identification schemes,
- live checks against BRIS, VIES, GLEIF, EORI, or national registers,
- comparison of legal name, legal form, and address with register data,
- completeness of an address under national law,
- requirement for a separate headquarters address,
- closed ISO 20275 or NACE value set,
- future or historical registration date,
- ownership and control relationships,
- longer organizational hierarchy cycles,
- role, status, and period of a Membership,
- type, period, and joint representation rules of a LegalRepresentation,
- evidence of membership, insurance, or qualifications,
- SME, tax, creditworthiness, and sanctions status,
- bank accounts and payment data,
- process roles such as Buyer, Seller, or Carrier,
- access control or data protection rules,
- general provenance and statement history.

## 23. Implementation Status

The `.shacl.ttl` implementation reflects the following confirmed points:

1. The shape catalog with five domain-specific Node Shapes is confirmed.
2. `registrationDate` remains a mandatory single value.
3. The structural identifier minimum is confirmed despite the open list of schemes.
4. At least one legal address is confirmed as a Legal Entity Core requirement.
5. `legalForm` remains optional.
6. Membership and representation are sufficient without role, period, or credential.
7. IRIs are mandatory for Membership and LegalRepresentation.
8. The documented error codes and test scenarios are accepted as the implementation contract.

The T-Box, shape graph, valid and invalid test graphs, and automated tests are implemented for version `0.1.0`. HTML documentation and network metadata will be updated in the subsequent documentation step.