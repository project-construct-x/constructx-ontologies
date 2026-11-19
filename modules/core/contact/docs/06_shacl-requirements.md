# Domain-Specific SHACL Requirements for the Contact Module

**Status:** Implemented  
**Version:** 0.2.0  
**As of:** 19 November 2026  
**Scope:** Contact Core Shapes

## 1. Purpose

This document specifies the data quality requirements for the Contact module. It describes shape targets, constraints, severity levels, error messages, and valid and invalid scenarios. The executable shape graph is implemented in `modules/core/contact/shapes/conx-contact-core.shacl.ttl`.

## 2. Implemented Shape Set

```text
Shape graph: modules/core/contact/shapes/conx-contact-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/contact/core
Version IRI: https://www.construct-x.org/shapes/contact/core/0.2.0
Namespace:   https://www.construct-x.org/shapes/contact/core#
Prefix:      conx-contact-sh
Version:     0.2.0
```

## 3. Validation Principles

### 3.1 OWL and SHACL

- OWL describes the open semantics of the concepts.
- SHACL checks the specific data graph supplied.
- Mandatory fields, maximum cardinalities, and channel-specific value forms are checked in the Core Shape.
- The shapes remain open to additional properties; `sh:closed true` is not intended.
- SHACL maximum cardinalities are not automatically adopted as OWL cardinalities.

### 3.2 Severity Levels

All core violations use `sh:Violation`. Recommendations such as specifying `contactPlatform` for social profiles or `availableLanguage` for support contacts produce no warning in the core.

Application profiles may later add stricter rules using `sh:Warning` or `sh:Info`.

### 3.3 Error Messages

Each constraint component receives at least:

- a German `sh:message`,
- an English `sh:message`,
- a stable requirement identifier,
- a traceable result path.

### 3.4 Reference Data

Validation must be performed together with the approved contact vocabularies:

- Construct-X `contact-channel`,
- Construct-X `contact-usage`,
- Construct-X `contact-purpose`,
- Construct-X `contact-platform`,
- Construct-X Address Ontology or Address core data when `postalAddress` is used.

The small sets of initial values can be included as closed `sh:in` lists in the first shape set. Alternatively, type and `skos:inScheme` can be checked against loaded reference graphs. For version `0.1.0`, a closed initial set is preferable from a domain perspective so that new values are versioned deliberately.

## 4. Responsibility Boundaries

| Requirement | Responsible Shape Set | Rule in the Contact Shape |
| --- | --- | --- |
| Entity holding contact information references a contact point | `contact/core` | Check values of `hasContactPoint` |
| Contact point and contact methods | `contact/core` | Validate fully |
| Contact channel, usage, and purpose | `contact/core` plus reference vocabularies | Check values against approved vocabularies |
| Postal contact address | `contact/core` plus `address/core` | `usesLocationAssignment` requires `conx-addr:LocationAssignment`; the Address Shape checks address details |
| Personal data | `person/core` | Do not check in the Contact Shape |
| Organizational structure | `organization/core` | Do not check in the Contact Shape |
| Delivery note requirements | `domain/delivery-note` | Do not enforce in the Contact core |
| Access, consent, and confidentiality | Governance or data protection profile | Do not check in the Contact core |

## 5. Shape Catalog

| Shape IRI | Type | Target or Usage | Purpose |
| --- | --- | --- | --- |
| `conx-contact-sh:NonEmptyStringOrLangStringShape` | Reusable Node Shape | Referenced by text values | Allows non-empty `xsd:string` and `rdf:langString` values |
| `conx-contact-sh:NonEmptyStringShape` | Reusable Node Shape | Referenced by technical values | Allows non-empty `xsd:string` values |
| `conx-contact-sh:ContactCarrierShape` | Node Shape | Subjects of `conx-contact:hasContactPoint` | Checks values of `hasContactPoint` without imposing Agent typing on the subject |
| `conx-contact-sh:ContactPointShape` | Node Shape | `conx-contact:ContactPoint` and objects of `hasContactPoint` | Checks the contact information block, usage, purpose, and methods |
| `conx-contact-sh:ContactMethodShape` | Node Shape | `conx-contact:ContactMethod` and objects of `hasContactMethod` | Checks the channel and channel-specific payload |
| `conx-contact-sh:ContactChannelConceptShape` | Node Shape | Values of `contactChannel` | Checks approved channel values |
| `conx-contact-sh:ContactUsageConceptShape` | Node Shape | Values of `contactUsage` | Checks approved usage values |
| `conx-contact-sh:ContactPurposeConceptShape` | Node Shape | Values of `contactPurpose` | Checks approved purpose values |
| `conx-contact-sh:ContactPlatformConceptShape` | Node Shape | Values of `contactPlatform` | Checks approved platform values |
| `conx-contact-sh:PostalLocationAssignmentReferenceShape` | Node Shape | Values of `usesLocationAssignment` | Checks the reference to `conx-addr:LocationAssignment` |

## 6. Targets

### 6.1 `ContactCarrierShape`

Target:

- `sh:targetSubjectsOf conx-contact:hasContactPoint`.

The shape does not require an explicit type of `conx-agent:Agent`. Although the intended domain-level direction remains from `Agent` to `ContactPoint`, mandatory typing in the Core Shape would prevent future entities such as projects, construction sites, or services from holding contact information.

### 6.2 `ContactPointShape`

Targets:

- `sh:targetClass conx-contact:ContactPoint`,
- `sh:targetObjectsOf conx-contact:hasContactPoint`,
- `sh:targetSubjectsOf conx-contact:hasContactMethod`,
- `sh:targetSubjectsOf conx-contact:contactUsage`,
- `sh:targetSubjectsOf conx-contact:contactPurpose`,
- `sh:targetSubjectsOf conx-contact:contactName`,
- `sh:targetSubjectsOf conx-contact:departmentName`,
- `sh:targetSubjectsOf conx-contact:functionTitle`,
- `sh:targetSubjectsOf conx-contact:availableLanguage`,
- `sh:targetSubjectsOf conx-contact:availabilityNote`,
- `sh:targetSubjectsOf conx-contact:isContactPointFor`.

Resources used as contact points must therefore be explicitly typed as `conx-contact:ContactPoint`.

### 6.3 `ContactMethodShape`

Targets:

- `sh:targetClass conx-contact:ContactMethod`,
- `sh:targetObjectsOf conx-contact:hasContactMethod`,
- `sh:targetSubjectsOf conx-contact:contactChannel`,
- `sh:targetSubjectsOf conx-contact:contactValue`,
- `sh:targetSubjectsOf conx-contact:contactURI`,
- `sh:targetSubjectsOf conx-contact:usesLocationAssignment`,
- `sh:targetSubjectsOf conx-contact:contactPlatform`.

Resources carrying channel values must therefore be explicitly typed as `conx-contact:ContactMethod`.

## 7. Node Constraints

| ID | Focus | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `CON-CAR-001` | Entity holding contact information | Values of `hasContactPoint` | Each value must be a blank node or IRI and a `conx-contact:ContactPoint` |
| `CON-CP-001` | `ContactPoint` | Resource form | Contact points must be blank nodes or IRIs |
| `CON-CP-002` | `ContactPoint` | Explicit type | Contact points must explicitly be `conx-contact:ContactPoint` |
| `CON-CM-001` | `ContactMethod` | Resource form | Contact methods must be blank nodes or IRIs |
| `CON-CM-002` | `ContactMethod` | Explicit type | Contact methods must explicitly be `conx-contact:ContactMethod` |

Contact points and contact methods may be modeled as blank nodes in the core. IRIs are recommended for reusable contacts or contacts maintained separately, but are not mandatory.

## 8. Property Constraints for `ContactPoint`

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `CON-CP-010` | `hasContactMethod` | 1 | Unbounded | Blank node or IRI, explicitly typed as `conx-contact:ContactMethod` |
| `CON-CP-020` | `contactUsage` | 0 | 1 | IRI from `contact-usage` |
| `CON-CP-021` | `contactPurpose` | 0 | Unbounded | IRI from `contact-purpose` |
| `CON-CP-030` | `contactName` | 0 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `CON-CP-031` | `departmentName` | 0 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `CON-CP-032` | `functionTitle` | 0 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `CON-CP-033` | `availableLanguage` | 0 | Unbounded | Non-empty language code as `xsd:string`; BCP 47 is recommended |
| `CON-CP-034` | `availabilityNote` | 0 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `CON-CP-040` | `isContactPointFor` | 0 | Unbounded | Blank node or IRI; maintaining the inverse is not mandatory |

`contactUsage` describes the usage context. `contactPurpose` describes the domain-specific function. They must not be combined into an ambiguous `contactType` property.

## 9. Property Constraints for `ContactMethod`

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | --- | --- | --- |
| `CON-CM-010` | `contactChannel` | 1 | 1 | IRI from `contact-channel` |
| `CON-CM-020` | Payload | 1 | 1 | Exactly one permitted value form according to the channel |
| `CON-CM-030` | `contactValue` | Channel-dependent | Channel-dependent | Non-empty `xsd:string` |
| `CON-CM-031` | `contactURI` | Channel-dependent | Channel-dependent | IRI |
| `CON-CM-032` | `usesLocationAssignment` | Channel-dependent | Channel-dependent | IRI or blank node of type `conx-addr:LocationAssignment` |
| `CON-CM-033` | `contactPlatform` | 0 | 1 | IRI from `contact-platform` |

Here, payload means the specific contact value. Exactly one payload type is permitted per method:

- `contactValue`,
- `contactURI`,
- `usesLocationAssignment`.

A method must not simultaneously carry a telephone number, a URL, and a location assignment.

## 10. Channel-Specific Payload Rules

| Channel | Required Payload | Not Permitted in the Core | Note |
| --- | --- | --- | --- |
| `contact-channel:email` | Exactly one `contactValue` as a non-empty string | `contactURI`, `usesLocationAssignment` | Strict email syntax reserved for a later profile |
| `contact-channel:phone` | Exactly one `contactValue` as a non-empty string | `contactURI`, `usesLocationAssignment` | Do not enforce international formatting in the core |
| `contact-channel:mobilePhone` | Exactly one `contactValue` as a non-empty string | `contactURI`, `usesLocationAssignment` | Dedicated mobile telephone channel |
| `contact-channel:fax` | Exactly one `contactValue` as a non-empty string | `contactURI`, `usesLocationAssignment` | UBL `Telefax`, Schema.org `faxNumber` |
| `contact-channel:website` | Exactly one `contactURI` | `contactValue`, `usesLocationAssignment` | IRI rather than a free-text string |
| `contact-channel:socialProfile` | Exactly one `contactURI` | `contactValue`, `usesLocationAssignment` | Optional platform value from `contact-platform` |
| `contact-channel:messenger` | Exactly one `contactValue` or exactly one `contactURI` | `usesLocationAssignment` | Handle or URI depending on the platform |
| `contact-channel:postalAddress` | Exactly one `usesLocationAssignment` | `contactValue`, `contactURI` | References `conx-addr:LocationAssignment` |

Syntax validation for email and telephone numbers deliberately remains pragmatic. An overly strict regular expression in the core would reject legitimate international or source-specific values. Stricter profiles may require E.164, `mailto:`, or organization-specific rules.

## 11. Controlled Values

### 11.1 `contact-channel`

The permitted initial set is:

```text
contact-channel:email
contact-channel:phone
contact-channel:mobilePhone
contact-channel:fax
contact-channel:website
contact-channel:messenger
contact-channel:socialProfile
contact-channel:postalAddress
```

### 11.2 `contact-usage`

The permitted initial set is:

```text
contact-usage:private
contact-usage:business
contact-usage:official
```

`contact-usage:private` is not an access restriction. It denotes only the domain-specific usage context.

### 11.3 `contact-purpose`

The permitted initial set is:

```text
contact-purpose:general
contact-purpose:delivery
contact-purpose:billing
contact-purpose:support
contact-purpose:sales
contact-purpose:technical
contact-purpose:emergency
```

### 11.4 `contact-platform`

The platform vocabulary is part of the MVP. The initial set is:

```text
contact-platform:linkedin
contact-platform:instagram
contact-platform:x
contact-platform:facebook
contact-platform:github
contact-platform:whatsapp
contact-platform:signal
contact-platform:microsoftTeams
```

The shape checks any platform values provided against this approved initial set.

## 12. Postal Contact Addresses

Postal contact methods exclusively use `usesLocationAssignment` to reference a `conx-addr:LocationAssignment` from a `ContactMethod`.

A direct reference to `conx-addr:Address` is not permitted in the Contact MVP. The reason is that `LocationAssignment` carries the domain-specific use of the address, such as delivery address, invoice address, registered address, department, “for the attention of,” and c/o. These details must not be lost when describing postal contactability.

The Contact Shape checks only:

- exactly one `usesLocationAssignment` for channel `postalAddress`,
- the value is a blank node or IRI,
- the value is a `conx-addr:LocationAssignment` with exactly one `assignedAddress` of type `Address`.

The Address Core Shape checks the internal address structure, `assignedAddress`, `locationRole`, and address components.

## 13. Error Message Catalog

### 13.1 Entities Holding Contact Information

| ID | German | English |
| --- | --- | --- |
| `CON-CAR-001` | Jeder Wert von hasContactPoint muss eine ContactPoint-Ressource sein. | Every hasContactPoint value must be a ContactPoint resource. |

### 13.2 Contact Points

| ID | German | English |
| --- | --- | --- |
| `CON-CP-001` | Ein ContactPoint muss eine Ressource sein und darf kein Literal sein. | A ContactPoint must be a resource and must not be a literal. |
| `CON-CP-002` | Eine als Kontaktpunkt verwendete Ressource muss explizit als conx-contact:ContactPoint typisiert sein. | A resource used as contact point must be explicitly typed as conx-contact:ContactPoint. |
| `CON-CP-010` | Ein ContactPoint muss mindestens eine ContactMethod besitzen. | A ContactPoint must have at least one ContactMethod. |
| `CON-CP-020` | contactUsage darf höchstens einmal vorkommen und muss auf einen freigegebenen Usage-Wert verweisen. | contactUsage may occur at most once and must reference an approved usage value. |
| `CON-CP-021` | Jeder contactPurpose-Wert muss auf einen freigegebenen Purpose-Wert verweisen. | Every contactPurpose value must reference an approved purpose value. |
| `CON-CP-030` | contactName muss ein nicht leerer String oder sprachmarkierter String sein. | contactName must be a non-empty string or language-tagged string. |
| `CON-CP-031` | departmentName muss ein nicht leerer String oder sprachmarkierter String sein. | departmentName must be a non-empty string or language-tagged string. |
| `CON-CP-032` | functionTitle muss ein nicht leerer String oder sprachmarkierter String sein. | functionTitle must be a non-empty string or language-tagged string. |
| `CON-CP-033` | availableLanguage muss als nicht leerer Sprachcode angegeben werden. | availableLanguage must be provided as a non-empty language code. |
| `CON-CP-034` | availabilityNote muss ein nicht leerer String oder sprachmarkierter String sein. | availabilityNote must be a non-empty string or language-tagged string. |
| `CON-CP-040` | isContactPointFor darf nur auf Ressourcen zeigen. | isContactPointFor may only reference resources. |

### 13.3 Contact Methods

| ID | German | English |
| --- | --- | --- |
| `CON-CM-001` | Eine ContactMethod muss eine Ressource sein und darf kein Literal sein. | A ContactMethod must be a resource and must not be a literal. |
| `CON-CM-002` | Eine als Kontaktmethode verwendete Ressource muss explizit als conx-contact:ContactMethod typisiert sein. | A resource used as contact method must be explicitly typed as conx-contact:ContactMethod. |
| `CON-CM-010` | Eine ContactMethod muss genau einen freigegebenen Kontaktkanal besitzen. | A ContactMethod must have exactly one approved contact channel. |
| `CON-CM-020` | Eine ContactMethod muss genau einen zum Kanal passenden Payload besitzen. | A ContactMethod must have exactly one payload matching its channel. |
| `CON-CM-030` | contactValue muss als nicht leerer String angegeben werden, wenn der Kanal einen Literalwert verlangt. | contactValue must be provided as a non-empty string when the channel requires a literal value. |
| `CON-CM-031` | contactURI muss eine IRI sein, wenn der Kanal eine URI verlangt. | contactURI must be an IRI when the channel requires a URI. |
| `CON-CM-032` | Eine postalische Kontaktmethode muss genau eine conx-addr:LocationAssignment referenzieren. | A postal contact method must reference exactly one conx-addr:LocationAssignment. |
| `CON-CM-033` | contactPlatform darf höchstens einmal vorkommen und muss auf eine freigegebene Plattform verweisen. | contactPlatform may occur at most once and must reference an approved platform. |

## 14. Valid Scenarios

### V-01: Private Contact Point with Email and Mobile Telephone

```turtle
ex:person-1
    conx-contact:hasContactPoint ex:person-1-private-contact .

ex:person-1-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-1-private-email,
                                  ex:person-1-private-mobile .

ex:person-1-private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .

ex:person-1-private-mobile
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:mobilePhone ;
    conx-contact:contactValue "+49 171 1234567" .
```

Expected result: valid.

### V-02: Business Delivery Contact with a Postal Location Assignment

```turtle
ex:company-1
    conx-contact:hasContactPoint ex:company-1-delivery-contact .

ex:company-1-delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:delivery ;
    conx-contact:contactName "Wareneingang Tor 4"@de ;
    conx-contact:hasContactMethod ex:company-1-delivery-email,
                                  ex:company-1-delivery-postal .

ex:company-1-delivery-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "wareneingang@example.org" .

ex:company-1-delivery-postal
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesLocationAssignment ex:company-1-delivery-address-assignment .

ex:company-1-delivery-address-assignment
    a conx-addr:LocationAssignment ;
    conx-addr:locationRole roles:DeliveryAddressRole ;
    conx-addr:assignedAddress ex:address-1 .

ex:address-1
    a conx-addr:Address .
```

Expected result: valid if the Address Core Shape accepts the location assignment.

### V-03: Official Website Contact

```turtle
ex:agent-1
    conx-contact:hasContactPoint ex:agent-1-official-contact .

ex:agent-1-official-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:official ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:agent-1-website .

ex:agent-1-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactURI <https://example.org/contact> .
```

Expected result: valid.

### V-04: Social Profile with a Platform

```turtle
ex:person-2
    conx-contact:hasContactPoint ex:person-2-business-contact .

ex:person-2-business-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-2-linkedin .

ex:person-2-linkedin
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin ;
    conx-contact:contactURI <https://www.linkedin.com/in/example> .
```

Expected result: valid.

### V-05: Messenger with a Handle

```turtle
ex:support-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactPurpose contact-purpose:support ;
    conx-contact:hasContactMethod ex:support-chat .

ex:support-chat
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:messenger ;
    conx-contact:contactValue "@support-desk" .
```

Expected result: valid.

## 15. Invalid Scenarios

### I-01: Contact Point as a Literal

```turtle
ex:person-1
    conx-contact:hasContactPoint "max@example.org" .
```

Expected violation: `CON-CAR-001`.

### I-02: Contact Point without a Method

```turtle
ex:contact-1
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private .
```

Expected violation: `CON-CP-010`.

### I-03: Contact Method without a Channel

```turtle
ex:method-1
    a conx-contact:ContactMethod ;
    conx-contact:contactValue "max@example.org" .
```

Expected violation: `CON-CM-010`.

### I-04: Contact Method with Multiple Channels

```turtle
ex:method-2
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email,
                                contact-channel:phone ;
    conx-contact:contactValue "max@example.org" .
```

Expected violation: `CON-CM-010`.

### I-05: Unknown Channel

```turtle
ex:method-3
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel ex:unsupported-channel ;
    conx-contact:contactValue "max@example.org" .
```

Expected violation: `CON-CM-010`.

### I-06: Website as a Literal Instead of an IRI

```turtle
ex:method-4
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactValue "https://example.org/contact" .
```

Expected violation: `CON-CM-020` or `CON-CM-031`.

### I-07: Email with a URI Payload

```turtle
ex:method-5
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactURI <mailto:max@example.org> .
```

Expected violation: `CON-CM-020` or `CON-CM-030`.

### I-08: Postal Method with a Direct Address Reference

```turtle
ex:method-6
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesAddress ex:address-1 .
```

Expected violation: `CON-CM-020` or `CON-CM-032`. The property `usesAddress` is not part of the MVP.

### I-09: Postal Method with a Free-Text Address

```turtle
ex:method-7
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:contactValue "Musterstrasse 1, 12345 Berlin" .
```

Expected violation: `CON-CM-020` or `CON-CM-032`.

### I-10: Multiple Usage Values

```turtle
ex:contact-2
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private,
                              contact-usage:business ;
    conx-contact:hasContactMethod ex:method-8 .
```

Expected violation: `CON-CP-020`.

### I-11: Unknown Purpose Value

```turtle
ex:contact-3
    a conx-contact:ContactPoint ;
    conx-contact:contactPurpose ex:dispatch ;
    conx-contact:hasContactMethod ex:method-9 .
```

Expected violation: `CON-CP-021`.

### I-12: Empty Functional Contact Name

```turtle
ex:contact-4
    a conx-contact:ContactPoint ;
    conx-contact:contactName "   " ;
    conx-contact:hasContactMethod ex:method-10 .
```

Expected violation: `CON-CP-030`.

### I-13: Multiple Platforms Specified

```turtle
ex:method-11
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin,
                                 contact-platform:instagram ;
    conx-contact:contactURI <https://example.org/profile> .
```

Expected violation: `CON-CM-033`.

## 16. Deliberately Excluded Checks

The Contact Core Shape does not check:

- whether a telephone number can actually be reached,
- whether an email address exists,
- whether a social profile URL actually belongs to the specified platform,
- whether private contact information may be published,
- whether a contact point is currently staffed,
- whether a contact point represents a person, department, or role,
- whether `contactName` is a personal name or a functional designation,
- whether an organization must have a delivery contact,
- whether the contact point actually supports `availableLanguage`.

These matters belong in stricter process profiles, governance rules, or operational systems.

## 17. Test Artifacts

The implementation includes the following test graphs:

```text
modules/core/contact/tests/valid/minimal-email-contact.ttl
modules/core/contact/tests/valid/business-delivery-contact.ttl
modules/core/contact/tests/valid/website-and-social-contact.ttl
modules/core/contact/tests/valid/messenger-contact.ttl
modules/core/contact/tests/invalid/contact-point-missing-method.ttl
modules/core/contact/tests/invalid/contact-method-invalid-channel.ttl
modules/core/contact/tests/invalid/contact-method-invalid-payload.ttl
modules/core/contact/tests/invalid/postal-contact-invalid-address-reference.ttl
modules/core/contact/tests/invalid/invalid-usage-and-purpose.ttl
modules/core/contact/tests/invalid/invalid-text-values.ttl
```

Automated tests verify that:

1. all valid files conform,
2. every invalid file produces at least the expected requirement identifier,
3. German and English messages are present,
4. channel-specific payload rules work without OWL inference,
5. contact vocabularies and Address core data are loaded into the validation environment,
6. additional properties from other modules remain permitted.

## 18. Implemented Artifacts

1. Reference vocabularies `contact-channel`, `contact-usage`, `contact-purpose`, and `contact-platform`.
2. `core/contact` T-Box.
3. Core Shapes specified in this document.
4. Valid and invalid test graphs.
5. Automated tests for the ontology, reference vocabularies, and shapes.
6. HTML documentation and module metadata.

## 19. Acceptance Criteria for the Core Shape Implementation

The implementation is complete from a domain perspective when:

1. every `CON-*` requirement is implemented as a traceable constraint,
2. `ContactPoint` requires at least one `ContactMethod`,
3. every `ContactMethod` has exactly one approved channel,
4. the payload rules apply for each channel,
5. postal contact methods exclusively use `usesLocationAssignment`,
6. Usage, Purpose, Channel, and Platform are validated against approved vocabularies,
7. the inverse relationship remains optional,
8. no address, person, or organization semantics are duplicated in the Contact Shape.

## 20. Illustrative Example

> A business billing contact has an email method. The shape checks that the method, channel, and email value are consistent. It does not check whether the mailbox can actually be reached.
