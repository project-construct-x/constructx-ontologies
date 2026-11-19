# Domain SHACL Requirements for the Person MVP

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Person Core Shapes

## 1. Purpose

This document defines the executable quality requirements for Person data. It describes shape targets, constraints, severity levels, error messages, and valid and invalid scenarios. It forms the domain basis of the implemented Core Shapes.

The executable shape graph is located at `shapes/conx-person-core.shacl.ttl`. Contact requirements are covered by the separate, implemented `core/contact` and are not duplicated in the Person shape.

## 2. Shape Set

```text
Shape graph: modules/core/person/shapes/conx-person-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/person/core
Version IRI: https://www.construct-x.org/shapes/person/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/person/core#
Prefix:      conx-person-sh
Version:     0.1.0
```

The IRIs and version are specified in `module.yaml` and the shape graph.

## 3. Validation Principles

### 3.1 Relationship between OWL and SHACL

- OWL describes semantics under the open-world assumption.
- SHACL checks the specific data graph supplied.
- Mandatory fields and maximum values are checked in the Core Shape as closed data requirements.
- The shapes remain open to additional properties; `sh:closed true` is not intended.
- SHACL maximum values are not automatically adopted as OWL cardinalities.

### 3.2 Severity Levels

All Core violations defined in this document use `sh:Violation`. Recommendations such as providing a family name produce neither errors nor warnings in the Core.

Application profiles may later add rules using `sh:Warning` or `sh:Info`.

### 3.3 Error Messages

Each domain constraint component receives at least:

- a German `sh:message`,
- an English `sh:message`,
- a stable requirement identifier from this document,
- a precise result path, where SHACL can determine one.

### 3.4 Reference Data

Validation must be performed together with the approved reference graphs:

- Construct-X `human-sex` vocabulary,
- Construct-X Gender vocabulary,
- Construct-X ISO 3166-1 country vocabulary.

The small `sex` and Gender value sets may additionally be included as closed `sh:in` lists in the Person shape. The 249 countries are not copied into the shape; they are checked through type and `skos:inScheme`.

## 4. Responsibility Boundaries of the Shape Sets

| Requirement | Responsible shape set | Rule in the Person shape |
| --- | --- | --- |
| Intrinsic personal data | `person/core` | Validate completely |
| Relationship to ADMS identifiers | `person/core` + `identifier/core` | Check the domain assignment locally and the shared ADMS structure centrally |
| Additional identifier rules | Future domain profiles | Do not enforce concrete schemes or issuer semantics in the Person MVP |
| Relationship to identity evidence | `person/core` | Check referenceability |
| Document or credential content | Future Identity shape | Do not check in the Person shape |
| Contact assignment | `contact/core` | Person may use the property; the Contact shape validates the assignment |
| Address | Existing `address/core` | Reuse existing Address Shapes |
| Membership and project participation | Future domain shape sets | Do not check in the Person shape |

## 5. Shape Catalog

### 5.1 Implemented Shapes of the Person Module

| Shape IRI | Type | Target or use | Purpose |
| --- | --- | --- | --- |
| `conx-person-sh:StringOrLangStringShape` | Reusable Node Shape | Referenced by Property Shapes | Permits `xsd:string` or `rdf:langString` |
| `conx-person-sh:NonEmptyStringOrLangStringShape` | Reusable Node Shape | Referenced by name and place values | Permits String/LangString containing at least one non-whitespace character |
| `conx-person-sh:PersonShape` | Node Shape | `conx-person:Person` and subjects of Person properties | Groups all Person constraints |
| `conx-person-sh:HumanSexConceptShape` | Node Shape | Objects of `conx-person:sex` | Checks IRI and the four permitted ISO/IEC 5218 concepts |
| `conx-person-sh:GenderConceptShape` | Node Shape | Objects of `conx-person:gender` | Checks IRI and the four approved Gender values |
| `conx-person-sh:CitizenshipCountryShape` | Node Shape | Objects of `conx-person:citizenship` | Checks the Country class and Country Concept Scheme |
| `conx-person-sh:IdentityEvidenceReferenceShape` | Node Shape | Objects of `conx-person:hasIdentityEvidence` | Checks an external IRI without validating evidence details |

### 5.2 Reused Shapes from Other Core Modules

| Shape IRI | Owner | Purpose |
| --- | --- | --- |
| `conx-contact-sh:ContactCarrierShape` | `contact/core` | Checks `hasContactPoint` values without a restrictive Agent domain |
| `conx-contact-sh:ContactPointShape` | `contact/core` | Checks the contact block, usage, purpose, and contact methods |
| `conx-contact-sh:ContactMethodShape` | `contact/core` | Checks the contact channel and channel-specific payload |
| Existing Address Shapes | `address/core` | Check location assignment, address, and address roles |
| `conx-id-sh:ADMSIdentifierShape` | `identifier/core` | Checks identifier type, notation, and optional scheme agency |

## 6. Targets of `PersonShape`

The implemented `PersonShape` combines the following targets:

1. `sh:targetClass conx-person:Person`,
2. `sh:targetSubjectsOf` for each property of the Person core.

The second target group detects resources that use, for example, `birthDate` or `gender` without being typed as `conx-person:Person`. The shape then requires an explicit Person type. RDFS domain inference alone is insufficient for the data quality check.

The following properties trigger the target:

- `fullName`,
- `givenName`,
- `familyName`,
- `additionalName`,
- `birthName`,
- `birthDate`,
- `birthPlaceName`,
- `sex`,
- `gender`,
- `citizenship`,
- `hasIdentityEvidence`.

`adms:identifier` is a generic property and must not automatically make every subject a Person target. It is checked only within resources already identified as persons.

## 7. Node Constraints for Persons

| ID | Constraint | SHACL requirement |
| --- | --- | --- |
| `PER-001` | Referenceable Person | The focus resource must satisfy `sh:nodeKind sh:IRI` |
| `PER-002` | Explicit Person type | The focus resource must satisfy `sh:class conx-person:Person` |

Persons are therefore not supplied as blank nodes. The stable IRI remains independent of domain identifiers, identity documents, or public keys.

## 8. Property Constraints of `PersonShape`

| ID | Property | Minimum | Maximum | Value requirement |
| --- | --- | ---: | ---: | --- |
| `PER-010` | `fullName` | 1 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `PER-011` | `givenName` | 1 | Unbounded | Non-empty `xsd:string` or `rdf:langString` |
| `PER-012` | `familyName` | 0 | Unbounded | If present: non-empty String/LangString |
| `PER-013` | `additionalName` | 0 | Unbounded | If present: non-empty String/LangString |
| `PER-014` | `birthName` | 0 | Unbounded | If present: non-empty String/LangString |
| `PER-020` | `birthDate` | 0 | 1 | Exclusively lexically valid `xsd:date` |
| `PER-021` | `birthPlaceName` | 0 | 1 | Non-empty String/LangString |
| `PER-030` | `sex` | 0 | 1 | IRI from the closed Human Sex value set |
| `PER-031` | `gender` | 0 | 1 | IRI from the closed initial Gender value set |
| `PER-040` | `citizenship` | 0 | Unbounded | IRI, instance of `conx-addr:Country`, in the Country Concept Scheme |
| `PER-050` | `adms:identifier` | 0 | Unbounded | Blank node or IRI, instance of `adms:Identifier`, exactly one literal `skos:notation`, optionally at most one `adms:schemaAgency` string |
| `PER-060` | `hasIdentityEvidence` | 0 | Unbounded | External IRI; no class restriction in the Person core |

## 9. Literal Rules

### 9.1 Names and Birthplace

Permitted:

- plain literals with datatype `xsd:string`,
- language-tagged literals with datatype `rdf:langString`.

Not permitted:

- empty values,
- values consisting only of whitespace,
- numeric or other unrelated datatypes.

The non-empty check should use a rule equivalent to `sh:pattern "\\S"`. `sh:uniqueLang` is not used because multiple names in the same language or different writing systems may be permitted.

### 9.2 Birth Date

`birthDate` accepts only `xsd:date`. The following are not permitted:

- `xsd:gYear`,
- `xsd:gYearMonth`,
- untyped date strings,
- multiple birth dates.

The Core does not include a “birth date must not be in the future” check. Such a rule would be time-dependent and may be added in a stricter application profile.

## 10. Controlled Values

### 10.1 `sex`

The permitted `sh:in` list contains exactly:

```text
human-sex:notKnown
human-sex:male
human-sex:female
human-sex:notApplicable
```

Additionally, `sh:nodeKind sh:IRI` and `sh:maxCount 1` apply.

The absence of the property means that no statement is present in the dataset. `human-sex:notKnown`, by contrast, explicitly states that the value is unknown.

`human-sex:notApplicable` must not be used as a substitute for gender diversity. SHACL cannot determine the domain rationale for its use; this remains a governance requirement.

### 10.2 `gender`

The permitted `sh:in` list initially contains exactly:

```text
gender:man
gender:woman
gender:nonBinaryOrDiverse
gender:notDisclosed
```

Additionally, `sh:nodeKind sh:IRI` and `sh:maxCount 1` apply.

Semantic notes:

- `man` and `woman` are gender identities; the English labels are intentionally `Man` and `Woman`, rather than `Male` and `Female`.
- `nonBinaryOrDiverse` is an extensible umbrella concept. More precise concepts may be added in later vocabulary versions.
- `notDisclosed` is not an identity; it represents explicit non-disclosure.
- An absent `gender` property means only that no statement is present in the dataset.

Extending the closed list requires a new version of the shape set. This prevents an older profile from silently accepting unknown new Gender values.

### 10.3 Citizenship

Every `citizenship` value must:

1. be an IRI,
2. be typed as `conx-addr:Country`,
3. have `skos:inScheme <https://www.construct-x.org/vocab/country>`.

A literal such as `"DE"`, an ISO 3166-2 subdivision, or a NUTS-2 region is not permitted. Multiple citizenships are allowed. Citizenship is not mandatory.

## 11. Identifier Requirements

For each `adms:identifier` value, the Person shape checks at least:

- resource kind `sh:BlankNodeOrIRI`,
- class `adms:Identifier`,
- exactly one literal `skos:notation`,
- optionally at most one `adms:schemaAgency` as `xsd:string`.

The domain property `adms:identifier` remains in the Person shape. Its values are validated using the shared `conx-id-sh:ADMSIdentifierShape` from `identifier/core`:

| ID | Property | Requirement |
| --- | --- | --- |
| `ID-001` | Resource type | `adms:Identifier` |
| `ID-002` | `skos:notation` | Exactly one literal |
| `ID-003` | `adms:schemaAgency` | Optional, at most one `xsd:string` |

The notation datatype may identify a Construct-X identifier scheme but is not checked against a closed approval list. Specific Person identifier schemes can therefore be added in domain profiles.

`issuedBy` and `issuedThrough` are not required because their final property ownership in the Identifier or Identity model has not been established. `adms:schemaAgency` remains an optional textual entry and is not interpreted as a complete issuer model.

## 12. Identity Evidence Requirements

`hasIdentityEvidence` has:

- `sh:minCount 0`,
- no maximum,
- `sh:nodeKind sh:IRI`.

The Person shape intentionally requires no shared class for the target resource. Permitted external models may provide identity document references, driving licence references, Verifiable Credentials, register extracts, or other digitally verifiable evidence.

The Person shape does not check:

- issuer and trust status,
- issue and expiry dates,
- credential subject,
- evidence chain,
- revocation and status,
- cryptographic keys and proofs.

These rules belong to the respective Document, Credential, or Identity shape.

## 13. Contact Shape Contract

The following requirements are not implemented in the Person shape; they are described in the separate `contact/core` shape set. The current requirements document is located at `modules/core/contact/docs/06_shacl-requirements.md`.

### 13.1 `ContactCarrierShape`

- Target: subjects of `conx-contact:hasContactPoint`.
- No `sh:class conx-agent:Agent` requirement in the open Core Shape.
- Each value must be a blank node or IRI and a `conx-contact:ContactPoint`.
- The shape makes no assertion about whether the subject is a Person, organization, project, position, or another resource.

### 13.2 `ContactPointShape`

| ID | Property | Minimum | Maximum | Value requirement |
| --- | --- | ---: | ---: | --- |
| `CON-CP-010` | `hasContactMethod` | 1 | Unbounded | Resource of type `ContactMethod` |
| `CON-CP-020` | `contactUsage` | 0 | 1 | IRI from the approved Contact Usage scheme |
| `CON-CP-021` | `contactPurpose` | 0 | Unbounded | IRI from the approved Contact Purpose scheme |

`contactUsage` describes the private, business, or official usage context. Separately, `contactPurpose` describes the domain function, such as general contact, delivery, billing, support, or emergency. `contact-usage:private` is not an access or confidentiality rule.

### 13.3 `ContactMethodShape`

The minimal shape requires:

- blank node or IRI,
- explicit type `conx-contact:ContactMethod`,
- exactly one approved `contactChannel`,
- exactly one payload matching the channel: `contactValue`, `contactURI`, or `usesLocationAssignment`.

Postal contact methods reference `conx-addr:LocationAssignment` exclusively through `usesLocationAssignment`. A direct reference to `conx-addr:Address` is not intended in the Contact MVP.

## 14. Error Message Catalog

### 14.1 Person-Related Messages

| ID | German | English |
| --- | --- | --- |
| `PER-001` | Eine Person muss durch eine IRI referenziert werden. | A Person must be referenced by an IRI. |
| `PER-002` | Eine Ressource mit Personeneigenschaften muss explizit als conx-person:Person typisiert sein. | A resource using Person properties must be explicitly typed as conx-person:Person. |
| `PER-010` | Eine Person muss mindestens einen nicht leeren vollständigen Namen besitzen. | A Person must have at least one non-empty full name. |
| `PER-011` | Eine Person muss mindestens einen nicht leeren Vornamen besitzen. | A Person must have at least one non-empty given name. |
| `PER-012` | Jeder Familienname muss ein nicht leerer String oder sprachmarkierter String sein. | Every family name must be a non-empty string or language-tagged string. |
| `PER-013` | Jeder zusätzliche Name muss ein nicht leerer String oder sprachmarkierter String sein. | Every additional name must be a non-empty string or language-tagged string. |
| `PER-014` | Jeder Geburtsname muss ein nicht leerer String oder sprachmarkierter String sein. | Every birth name must be a non-empty string or language-tagged string. |
| `PER-020` | Eine Person darf höchstens ein vollständiges Geburtsdatum mit dem Datentyp xsd:date besitzen. | A Person may have at most one complete birth date using datatype xsd:date. |
| `PER-021` | Der Geburtsortname muss ein nicht leerer String oder sprachmarkierter String sein und darf höchstens einmal vorkommen. | The birth place name must be a non-empty string or language-tagged string and may occur at most once. |
| `PER-030` | sex darf höchstens einmal vorkommen und muss auf einen freigegebenen ISO/IEC-5218-Wert verweisen. | sex may occur at most once and must reference an approved ISO/IEC 5218 value. |
| `PER-031` | gender darf höchstens einmal vorkommen und muss auf einen freigegebenen Genderwert verweisen. | gender may occur at most once and must reference an approved gender value. |
| `PER-040` | Jede Staatsangehörigkeit muss auf ein Land des freigegebenen Construct-X-Ländervokabulars verweisen. | Every citizenship value must reference a country from the approved Construct-X country vocabulary. |
| `PER-050` | Jeder Personenidentifikator muss eine ADMS-Identifier-Ressource mit genau einer literalen Notation sein. | Every Person identifier must be an ADMS Identifier resource with exactly one literal notation. |
| `PER-060` | Jeder Identitätsnachweis muss durch eine externe IRI referenziert werden. | Every identity evidence resource must be referenced by an external IRI. |

### 14.2 Identifier Messages

| ID | German | English |
| --- | --- | --- |
| `ID-001` | Eine Identifikatorressource muss als adms:Identifier typisiert sein. | An identifier resource must be typed as adms:Identifier. |
| `ID-002` | Ein Identifikator muss genau eine skos:notation besitzen. | An identifier must have exactly one skos:notation. |
| `ID-003` | schemaAgency darf höchstens einmal als String angegeben werden. | schemaAgency may be provided at most once as a string. |

### 14.3 Contact Messages

| ID | German | English |
| --- | --- | --- |
| `CON-CAR-001` | Jeder Wert von hasContactPoint muss eine ContactPoint-Ressource sein. | Every hasContactPoint value must be a ContactPoint resource. |
| `CON-CP-010` | Ein ContactPoint muss mindestens eine ContactMethod besitzen. | A ContactPoint must have at least one ContactMethod. |
| `CON-CP-020` | contactUsage darf höchstens einmal vorkommen und muss auf einen freigegebenen Usage-Wert verweisen. | contactUsage may occur at most once and must reference an approved usage value. |
| `CON-CP-021` | Jeder contactPurpose-Wert muss auf einen freigegebenen Purpose-Wert verweisen. | Every contactPurpose value must reference an approved purpose value. |
| `CON-CM-010` | Eine ContactMethod muss genau einen freigegebenen Kontaktkanal besitzen. | A ContactMethod must have exactly one approved contact channel. |
| `CON-CM-020` | Eine ContactMethod muss genau einen zum Kanal passenden Payload besitzen. | A ContactMethod must have exactly one payload matching its channel. |
| `CON-CM-032` | Eine postalische Kontaktmethode muss genau eine conx-addr:LocationAssignment referenzieren. | A postal contact method must reference exactly one conx-addr:LocationAssignment. |

## 15. Valid Scenarios

### V-01: Minimal Valid Person

```turtle
ex:person-1 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" .
```

Expected result: valid. All optional properties may be absent.

### V-02: Complete Person with Controlled Values

```turtle
ex:person-2 a conx-person:Person ;
    conx-person:fullName "Maria Anna Beispiel"@de ;
    conx-person:givenName "Maria" ;
    conx-person:additionalName "Anna" ;
    conx-person:familyName "Beispiel" ;
    conx-person:birthDate "1985-04-23"^^xsd:date ;
    conx-person:birthPlaceName "Bochum"@de ;
    conx-person:sex human-sex:female ;
    conx-person:gender gender:woman ;
    conx-person:citizenship country:DEU ;
    conx-person:hasIdentityEvidence ex:credential-789 .
```

Expected result: valid if the referenced vocabularies are loaded into the validation graph.

### V-03: Explicit Non-Disclosure of Gender

```turtle
ex:person-3 a conx-person:Person ;
    conx-person:fullName "Alex Beispiel" ;
    conx-person:givenName "Alex" ;
    conx-person:gender gender:notDisclosed .
```

Expected result: valid. The Person has explicitly chosen not to disclose gender information.

### V-04: Private Contact Point

```turtle
ex:person-4 a conx-person:Person ;
    conx-person:fullName "Sam Beispiel" ;
    conx-person:givenName "Sam" ;
    conx-contact:hasContactPoint ex:person-4-private-contact .

ex:person-4-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:email-1 .

ex:email-1
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "sam@example.org" .
```

Expected result: valid for Person and Contact once the Contact Core Shape and channel model are implemented.

### V-05: Multiple Citizenships and Identifiers

```turtle
ex:person-5 a conx-person:Person ;
    conx-person:fullName "Robin Beispiel" ;
    conx-person:givenName "Robin" ;
    conx-person:citizenship country:DEU,
                                country:FRA ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "P-4711"^^id-scheme:project-person-id ;
        adms:schemaAgency "Beispielorganisation"
    ] .
```

Expected result: valid if the identifier scheme used is approved.

## 16. Invalid Scenarios

### I-01: Missing `fullName`

```turtle
ex:invalid-1 a conx-person:Person ;
    conx-person:givenName "Kim" .
```

Expected violation: `PER-010`.

### I-02: Missing `givenName`

```turtle
ex:invalid-2 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" .
```

Expected violation: `PER-011`.

### I-03: Empty Name

```turtle
ex:invalid-3 a conx-person:Person ;
    conx-person:fullName "   " ;
    conx-person:givenName "Kim" .
```

Expected violation: `PER-010`.

### I-04: Incomplete Birth Date

```turtle
ex:invalid-4 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:birthDate "1985"^^xsd:gYear .
```

Expected violation: `PER-020`.

### I-05: Multiple Birth Dates

```turtle
ex:invalid-5 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:birthDate "1985-04-23"^^xsd:date,
                          "1985-04-24"^^xsd:date .
```

Expected violation: `PER-020`.

### I-06: `sex` as a Literal

```turtle
ex:invalid-6 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:sex "female" .
```

Expected violation: `PER-030`.

### I-07: Unknown Gender Value

```turtle
ex:invalid-7 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:gender ex:unsupported-gender-value .
```

Expected violation: `PER-031`.

### I-08: Multiple Gender Values

```turtle
ex:invalid-8 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:gender gender:nonBinaryOrDiverse,
                       gender:notDisclosed .
```

Expected violation: `PER-031`.

### I-09: Country Code as a Literal

```turtle
ex:invalid-9 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:citizenship "DE" .
```

Expected violation: `PER-040`.

### I-10: Region Instead of a State

```turtle
ex:invalid-10 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:citizenship ex:nuts-region-DEA1 .
```

Expected violation: `PER-040`.

### I-11: Identifier as a Literal

```turtle
ex:invalid-11 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    adms:identifier "P-4711" .
```

Expected violation: `PER-050`.

### I-12: Identity Evidence as a Literal

```turtle
ex:invalid-12 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:hasIdentityEvidence "Personalausweis" .
```

Expected violation: `PER-060`.

### I-13: Contact Point without a Contact Method

```turtle
ex:person-13 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-contact:hasContactPoint ex:invalid-contact-point .

ex:invalid-contact-point
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private .
```

Expected violation in the Contact shape: `CON-CP-010`.

### I-14: Two Contact Usage Values

```turtle
ex:invalid-contact-point-2
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private,
                              contact-usage:business ;
    conx-contact:hasContactMethod ex:email-2 .
```

Expected violation in the Contact shape: `CON-CP-020`.

### I-15: Person Property without a Person Type

```turtle
ex:invalid-15
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" .
```

Expected violation: `PER-002`.

## 17. Intentionally Not Validated

The Core Shape does not check:

- whether `fullName` can be assembled from given, additional, and family names,
- whether a Person has a family name,
- whether the birth date is in the past,
- whether `sex` and `gender` supposedly correspond,
- whether citizenship is supported by domain or legal evidence,
- whether a Person is stateless,
- whether identity evidence is trustworthy, valid, or revoked,
- whether private contact details may be published,
- whether a contact point is actually reachable,
- whether additional properties from other Construct-X modules are used.

These matters are intentionally left open, belong in stricter application profiles, or fall within other domain modules.

## 18. Test Artifacts

The implementation contains at least the following files:

```text
modules/core/person/tests/valid/minimal-person.ttl
modules/core/person/tests/valid/complete-person.ttl
modules/core/person/tests/valid/gender-not-disclosed.ttl
modules/core/person/tests/invalid/missing-required-names.ttl
modules/core/person/tests/invalid/invalid-name-values.ttl
modules/core/person/tests/invalid/invalid-birth-values.ttl
modules/core/person/tests/invalid/invalid-controlled-values.ttl
modules/core/person/tests/invalid/invalid-identifier-and-evidence.ttl
```

Once the Contact module has been created, contact cases belong in its own test directories.

Automated tests verify:

1. all valid files conform,
2. each invalid file produces at least the expected requirement identifier,
3. German and English messages are present,
4. every agreed maximum or minimum cardinality is implemented in the shape,
5. reference vocabularies are loaded into the validation environment,
6. the shapes work without RDFS or OWL inference wherever explicit types are required.

## 19. Implementation Sequence

1. Create versioned Gender and Human Sex reference vocabularies. Completed.
2. Implement the `core/agent` and `core/person` T-Boxes. Completed.
3. Derive Person Core Shapes from this document, including the minimal ADMS constraints. Completed.
4. Create valid and invalid test graphs. Completed.
5. Integrate reference graphs into build and validation. Completed.
6. Specify the Contact module separately and implement its shapes.
7. Generate HTML documentation and update network metadata. Completed.

## 20. Acceptance Criteria for the Core Shape Implementation

The implementation is complete from a domain perspective when:

1. each `PER-*` requirement is implemented in exactly one traceable constraint,
2. the four Sex and four Gender values are validated as closed sets,
3. countries are checked through the existing reference graph,
4. identifiers are not accepted as literals,
5. external identity evidence must be referenced by IRIs,
6. additional properties from other modules remain permitted,
7. all described positive and negative scenarios are checked automatically,
8. no Contact, Credential, or Organization semantics are duplicated in the Person shape.