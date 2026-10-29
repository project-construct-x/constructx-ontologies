# Term Catalog for the Person MVP

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

## 1. Purpose

This catalog translates the confirmed scope and source analysis into concrete terms. For each term, it describes its name, definition, module ownership, domain, range, cardinality, requirement level, source, alignment, example, and data protection relevance.

The specifications form the domain basis of the implemented T-Box and Core Shapes. The specific shape rules are defined in the [SHACL Requirements Profile](06_shacl-requirements.md) and implemented in machine-readable form in `shapes/conx-person-core.shacl.ttl`.

## 2. Namespaces

### Person Ontology

```text
Ontology IRI: https://www.construct-x.org/ontology/person
Version IRI:  https://www.construct-x.org/ontology/person/0.1.0
Namespace:    https://www.construct-x.org/ontology/person#
Prefix:       conx-person
```

### Agent Ontology

```text
Ontology IRI: https://www.construct-x.org/ontology/agent
Version IRI:  https://www.construct-x.org/ontology/agent/0.1.0
Namespace:    https://www.construct-x.org/ontology/agent#
Prefix:       conx-agent
```

### Human Sex Reference Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/human-sex
Version IRI:    https://www.construct-x.org/vocab/human-sex/0.1.0
Namespace:      https://www.construct-x.org/vocab/human-sex#
Prefix:         human-sex
```

### Gender Reference Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/gender
Version IRI:    https://www.construct-x.org/vocab/gender/0.1.0
Namespace:      https://www.construct-x.org/vocab/gender#
Prefix:         gender
```

Version `0.1.0` is specified in the module and vocabulary metadata.

## 3. Modeling Rules

- OWL describes meaning, inheritance, domain, and range as openly as possible.
- The Core SHACL profile describes mandatory fields, maximum cardinalities, and permitted value sets.
- An absent optional value is neither a negative assertion nor a substitute code.
- Names in multiple languages or writing systems may have multiple literal values.
- Controlled value sets are maintained as separately versioned A-Box vocabularies.
- Person instances receive IRIs in the respective data holder’s namespace rather than the Construct-X ontology namespace.

## 4. Classes

### 4.1 `conx-agent:Agent`

| Item | Specification |
| --- | --- |
| Definition | Actor that can act, bear responsibility, or serve as an issuer or participant in a domain context |
| Module | `modules/core/agent` |
| Superclass | No local superclass in the MVP |
| Subclasses | Initially `conx-person:Person`; later `conx-org:Organization` |
| Requirement level | Abstract shared type; no mandatory attributes |
| Source | FOAF Agent, SEMIC Agent, W3C ORG |
| Alignment | `rdfs:subClassOf foaf:Agent` recommended; no unverified equivalence |
| Data protection | No directly personal values; concrete subclasses may represent personal data |

Example:

```turtle
ex:person-123 a conx-person:Person, conx-agent:Agent .
```

The detailed specification is provided in the [Agent Specification](../../agent/docs/10_agent-specification.md).

### 4.2 `conx-person:Person`

| Item | Specification |
| --- | --- |
| Definition | Real natural person, living or deceased |
| Module | `modules/core/person` |
| Superclass | `conx-agent:Agent` |
| Exclusions | Fictional persons, organizations, software services, and roles |
| Requirement level | Instances use the Person Core Shape |
| Source | SEMIC Core Person as the primary source |
| Alignment | `rdfs:subClassOf foaf:Person`; assess alignment with `schema:Person`, but equivalence is not recommended because of its broader scope |
| Data protection | The instance represents personal data; access and publication are governed outside the T-Box |

Example:

```turtle
ex:person-123 a conx-person:Person .
```

## 5. Name Terms

### 5.1 `conx-person:fullName`

| Item | Specification |
| --- | --- |
| Definition | Complete, directly displayable name of a Person in a desired written form |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | No OWL maximum; Core SHACL minimum `1` |
| Requirement level | Mandatory |
| Source | SEMIC `fullName`, vCard `fn`, Schema.org `name` |
| Alignment | SEMIC `fullName`; assess `rdfs:subPropertyOf schema:name` |
| Data protection | Directly identifying; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:fullName "Dr. Maria Anna Beispiel"@de .
```

### 5.2 `conx-person:givenName`

| Item | Specification |
| --- | --- |
| Definition | Primary given name or sequence of names recorded as a Person’s primary given names |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | No OWL maximum; Core SHACL minimum `1` |
| Requirement level | Mandatory |
| Source | SEMIC `givenName`, UBL `FirstName`, Schema.org, and vCard |
| Alignment | `schema:givenName`, vCard `given-name`, SEMIC `givenName` |
| Data protection | Directly identifying; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:givenName "Maria" .
```

### 5.3 `conx-person:familyName`

| Item | Specification |
| --- | --- |
| Definition | Family name or surname of a Person |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | `0..n` |
| Requirement level | Optional core field; recommended if available |
| Source | SEMIC `familyName`, UBL `FamilyName`, Schema.org, and vCard |
| Alignment | `schema:familyName`, vCard `family-name`, SEMIC `familyName` |
| Data protection | Directly identifying; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:familyName "Beispiel" .
```

The optional cardinality accommodates persons without family names. A specific application profile may make the field mandatory when required by its legal or process context.

### 5.4 `conx-person:additionalName`

| Item | Specification |
| --- | --- |
| Definition | Additional given name, middle name, or additional given-name component |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | `0..n` |
| Requirement level | Optional |
| Source | Schema.org `additionalName`, vCard `additional-name`, UBL `MiddleName` |
| Alignment | `schema:additionalName`; document UBL mapping |
| Data protection | Directly identifying; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:additionalName "Anna" .
```

### 5.5 `conx-person:birthName`

| Item | Specification |
| --- | --- |
| Definition | Complete name recorded for a Person at birth |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | `0..n` |
| Requirement level | Optional |
| Source | SEMIC `birthName` |
| Alignment | SEMIC `birthName`; no forced Schema.org alignment |
| Data protection | Directly identifying and historical; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:birthName "Maria Anna Altname" .
```

The term does not replace a general name history and contains no period.

## 6. Birth Details

### 6.1 `conx-person:birthDate`

| Item | Specification |
| --- | --- |
| Definition | Complete calendar date of a Person’s birth |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | Exclusively `xsd:date` |
| Cardinality | `0..1` |
| Requirement level | Optional, but part of the MVP |
| Source | SEMIC `dateOfBirth`, UBL `BirthDate`, Schema.org `birthDate` |
| Alignment | `schema:birthDate`; SEMIC alignment with a narrower local datatype |
| Data protection | Strongly identifying; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:birthDate "1985-04-23"^^xsd:date .
```

`xsd:gYear` and `xsd:gYearMonth` are not permitted in the MVP.

### 6.2 `conx-person:birthPlaceName`

| Item | Specification |
| --- | --- |
| Definition | Textual name of a Person’s birthplace |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` or `rdf:langString` |
| Cardinality | `0..1` |
| Requirement level | Optional |
| Source | UBL `BirthplaceName` |
| Alignment | UBL mapping; no direct alignment with object-valued place properties |
| Data protection | Strongly identifying in combination with name and date; high protection requirements |

Example:

```turtle
ex:person-123 conx-person:birthPlaceName "Bochum"@de .
```

## 7. Sex and Gender Information

### 7.1 `conx-person:sex`

| Item | Specification |
| --- | --- |
| Definition | Classification of human sex recorded for information interchange according to ISO/IEC 5218:2022 |
| Module | Property in `core/person`; values in a separate reference vocabulary |
| Domain | `conx-person:Person` |
| Range | `skos:Concept` from `https://www.construct-x.org/vocab/human-sex` |
| Cardinality | `0..1` |
| Requirement level | Optional |
| Source | ISO/IEC 5218:2022, SEMIC `sex`, EU Authority Table `human-sex` |
| Alignment | SEMIC `sex`; assess value alignment with the EU table before implementation |
| Data protection | Sensitive personal attribute; very high protection requirements |

Example:

```turtle
ex:person-123 conx-person:sex human-sex:female .
```

### 7.2 `conx-person:gender`

| Item | Specification |
| --- | --- |
| Definition | Gender identity, expression, or social or legal classification in the applicable context |
| Module | Property in `core/person`; values in a separate reference vocabulary |
| Domain | `conx-person:Person` |
| Range | `skos:Concept` from `https://www.construct-x.org/vocab/gender` |
| Cardinality | `0..1` |
| Requirement level | Optional |
| Source | SEMIC `gender`; Schema.org as a broad alignment source |
| Alignment | Align external values only after individual assessment |
| Data protection | Sensitive personal attribute; very high protection requirements |

Example:

```turtle
ex:person-123 conx-person:gender gender:woman .
```

## 8. `human-sex` Reference Vocabulary

| Local term | ISO/IEC 5218 code | German label | English label | Use |
| --- | --- | --- | --- | --- |
| `human-sex:notKnown` | `0` | Nicht bekannt | Not known | Value was explicitly supplied as unknown |
| `human-sex:male` | `1` | Männlich | Male | Classification value for data exchange |
| `human-sex:female` | `2` | Weiblich | Female | Classification value for data exchange |
| `human-sex:notApplicable` | `9` | Nicht anwendbar | Not applicable | Use only faithfully to the source; do not use as an additional gender category |

Implemented RDF pattern:

- a separate `skos:ConceptScheme`,
- one `skos:Concept` per code,
- numeric code as `skos:notation` using an unambiguously named ISO/IEC 5218 datatype,
- German and English `skos:prefLabel` values,
- `skos:exactMatch` or `skos:closeMatch` to EU resources only after individual assessment,
- versioning independent of the Person T-Box.

Code `0` and the absence of `conx-person:sex` have different meanings:

| Representation | Meaning |
| --- | --- |
| No property | No statement in the dataset |
| Code `0` | Explicitly supplied value “not known” |

## 9. Gender Reference Vocabulary

| Local term | German label | English label | Semantics |
| --- | --- | --- | --- |
| `gender:man` | Mann | Man | The Person identifies as a man |
| `gender:woman` | Frau | Woman | The Person identifies as a woman |
| `gender:nonBinaryOrDiverse` | Nicht-binär oder divers | Non-binary or gender-diverse | Provisional, extensible umbrella concept beyond the binary values |
| `gender:notDisclosed` | Keine Angabe | Not disclosed | The Person has explicitly chosen not to disclose gender information |

`gender:notDisclosed` is not a gender identity. Nevertheless, the first profile permits the value as a response to the same property so that explicit non-disclosure can be distinguished from a missing statement:

| Representation | Meaning |
| --- | --- |
| No property | No statement is present in the dataset |
| `gender:notDisclosed` | The Person does not wish to disclose the information |

`gender:nonBinaryOrDiverse` is intentionally a broad initial concept. More precise identities can later be added as separate concepts and classified through `skos:broader gender:nonBinaryOrDiverse`. “Other” is not used as a preferred label because it does not denote a meaningful domain identity; it may be documented as an input value in source mappings.

## 10. Citizenship

### 10.1 `conx-person:citizenship`

| Item | Specification |
| --- | --- |
| Definition | Legal affiliation of a Person with a state |
| Module | Property in `core/person`; values in the existing country reference dataset |
| Domain | `conx-person:Person` |
| Range | `conx-addr:Country` from the ISO 3166-1 country vocabulary |
| Cardinality | `0..n` |
| Requirement level | Optional |
| Source | SEMIC `citizenship`, UBL `CitizenshipCountry`, Schema.org `nationality` |
| Alignment | Assess SEMIC and Schema.org |
| Data protection | Personal and potentially sensitive depending on context; high protection requirements |

Example:

```turtle
ex:person-123
    conx-person:citizenship <https://www.construct-x.org/vocab/country#DEU> .
```

Statelessness is not modeled in the MVP. It must not be inferred from the absence of the property.

## 11. Identifiers

### 11.1 Reuse of `adms:identifier`

| Item | Specification |
| --- | --- |
| Definition | Links a Person to a structured domain identifier |
| Module | External ADMS term according to the Construct-X Identifier Model; no local replacement property |
| Domain | Applied to `conx-person:Person` in the local shape |
| Range | `adms:Identifier` |
| Cardinality | `0..n` |
| Requirement level | Optional |
| Source | ADMS 2.0 and Construct-X Identifier Model |
| Alignment | Direct reuse |
| Data protection | Often strongly or uniquely identifying; very high protection requirements |

Example:

```turtle
ex:person-123 adms:identifier [
    a adms:Identifier ;
    skos:notation "P-4711"^^id-scheme:project-person-id ;
    adms:schemaAgency "Beispielorganisation"
] .
```

Specific identifier schemes will be created after internal project clarification.

## 12. Identity Evidence

### 12.1 `conx-person:hasIdentityEvidence`

| Item | Specification |
| --- | --- |
| Definition | Links a Person to an external resource that supports or enables verification of assertions about their identity |
| Module | `core/person` |
| Domain | `conx-person:Person` |
| Range | Referenceable external resource with an IRI; future Identity modules may define narrower subclasses |
| Cardinality | `0..n` |
| Requirement level | Optional |
| Source | UBL `IdentityDocumentReference`, W3C Controlled Identifiers, and VC Data Model |
| Alignment | No premature equivalence alignment; possible subproperties in the Identity module |
| Data protection | Evidence may contain particularly sensitive data or access paths; very high protection requirements |

Example:

```turtle
ex:person-123 conx-person:hasIdentityEvidence ex:credential-789 .

ex:credential-789 a ex:VerifiableCredential .
```

Possible target resources:

- identity document reference,
- driving licence reference,
- Verifiable Credential,
- official register extract,
- other digitally verifiable evidence.

The property asserts only an evidence relationship. It does not automatically assert validity, trustworthiness, or cryptographic verification. These semantics belong to the target resource model.

## 13. Terms from Other Modules

The following required relationships are not defined in the Person module:

| Need | Responsible term or module | Rationale |
| --- | --- | --- |
| Contact point and contact methods | Existing `core/contact` with outgoing `hasContactPoint`, `ContactPoint`, and `ContactMethod` | Reusable for projects, positions, and other resources because there is no restrictive Agent domain |
| Registered, residential, and postal address | Existing `core/address` with `AddressAssignment` | Address semantics already exist |
| Membership and employment | Existing `core/organization` | Role, organization, and period form a separate relationship |
| Project participation | Responsible Project module | Project role and period belong to the project context |
| Evidence details | Future Identity or Credential module | Validity, issuer, status, revocation, and keys are separate concepts |
| `issuedBy` and `issuedThrough` | Identifier/identity architecture | Must not be restricted to Person identifiers |

## 14. Implemented Core SHACL Profile

| Property | Minimum | Maximum | Additional rule |
| --- | ---: | ---: | --- |
| `fullName` | 1 | Unbounded | `xsd:string` or `rdf:langString`; non-empty |
| `givenName` | 1 | Unbounded | `xsd:string` or `rdf:langString`; non-empty |
| `familyName` | 0 | Unbounded | Non-empty literal |
| `additionalName` | 0 | Unbounded | Non-empty literal |
| `birthName` | 0 | Unbounded | Non-empty literal |
| `birthDate` | 0 | 1 | Exclusively `xsd:date` |
| `birthPlaceName` | 0 | 1 | Non-empty literal |
| `sex` | 0 | 1 | Value from the approved `human-sex` scheme |
| `gender` | 0 | 1 | Value from the approved Gender scheme |
| `citizenship` | 0 | Unbounded | Value from the approved country vocabulary |
| `adms:identifier` | 0 | Unbounded | Each value is an `adms:Identifier` resource with exactly one `skos:notation`; `adms:schemaAgency` is optional |
| `hasIdentityEvidence` | 0 | Unbounded | IRI; stricter rules in the target module |

The maximum values are SHACL decisions and should not automatically be adopted as OWL cardinalities.

## 15. Compact Target Profile Example

```turtle
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix human-sex: <https://www.construct-x.org/vocab/human-sex#> .
@prefix gender: <https://www.construct-x.org/vocab/gender#> .
@prefix country: <https://www.construct-x.org/vocab/country#> .
@prefix ex: <https://example.org/id/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:person-123 a conx-person:Person ;
    conx-person:fullName "Maria Anna Beispiel" ;
    conx-person:givenName "Maria" ;
    conx-person:additionalName "Anna" ;
    conx-person:familyName "Beispiel" ;
    conx-person:birthDate "1985-04-23"^^xsd:date ;
    conx-person:birthPlaceName "Bochum" ;
    conx-person:sex human-sex:female ;
    conx-person:gender gender:woman ;
    conx-person:citizenship country:DEU ;
    conx-person:hasIdentityEvidence ex:credential-789 .
```

The example illustrates the target profile; instance data and SHACL test cases are not yet part of this T-Box release.

The complete domain interaction is shown in the [Person Diagram](diagrams/person-concept-model.md).

## 16. Terms Not Yet Finalized

| Topic | Reason for deferral |
| --- | --- |
| Extension of the Gender value vocabulary | More precise non-binary or gender-diverse concepts and governance will be added later |
| `issuedBy` and `issuedThrough` | Ownership between the generic Identifier and Identity models remains open |
| Contact terms and contact roles | Specified in the separate Contact module |
| Organization and project relationships | Owned by the respective modules |
| Statelessness status | Explicitly deferred for the MVP |