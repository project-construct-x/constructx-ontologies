# VSO ISOProps Profile Requirements

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `profile/vso-isoprops`

## 1. Composition

The profile is additive. Data must be validated against both the VSO Core Shapes and this profile Shape graph.

## 2. Reference and Identity

| ID | Requirement |
| --- | --- |
| `ISOP-REF-001` | Every VSO assignment references exactly one IRI explicitly typed as `isoprops:Property`. |
| `ISOP-ID-001` | Every referenced ISOProps property has exactly one RFC-4122-style GUID string. |
| `ISOP-ID-002` | A Construct-X managed property IRI identifies an exact `/revision/{revision}` resource. |
| `ISOP-ID-003` | GUID and revision encoded in a Construct-X IRI match the ISOProps metadata. |

External ISOProps IRIs are allowed. The Construct-X path rules apply only to IRIs below `https://www.construct-x.org/id/property/`.

## 3. Version and Status

| ID | Requirement |
| --- | --- |
| `ISOP-VERSION-001` | Exactly one positive integer `isoprops:versionNumber` is present. |
| `ISOP-REVISION-001` | Exactly one positive integer `isoprops:revisionNumber` is present. |
| `ISOP-STATUS-001` | Exactly one status with value `active` or `inactive` is present. |

Inactive exact revisions remain valid references for historical and reproducible data.

## 4. Datatype Mapping

| ISOProps token | Accepted RDF value |
| --- | --- |
| `BOOLEAN` | `xsd:boolean` |
| `INTEGER` | `xsd:integer` and its derived integer datatypes |
| `RATIONAL` | Any XSD numeric datatype |
| `REAL` | Any XSD numeric datatype |
| `COMPLEX` | Any RDF literal |
| `STRING` | `xsd:string` or `rdf:langString` |
| `DATETIME` | `xsd:dateTime` |

| ID | Requirement |
| --- | --- |
| `ISOP-DATATYPE-001` | Every referenced definition declares exactly one approved ISOProps datatype token. |
| `ISOP-VALUE-001` | The VSO `schema:value` matches the conservative RDF mapping of that token. |
| `ISOP-VALUE-002` | Values of mapped datatypes must have valid lexical forms and satisfy their datatype's value bounds. |

For example, `"warm"^^xsd:decimal`, `"1e2"^^xsd:decimal` and
`"128"^^xsd:byte` are invalid. A datatype IRI alone does not prove that its
value is valid. `"8.0"^^xsd:decimal` and `"127"^^xsd:byte` remain valid.
The check uses [SHACL datatype constraints](https://www.w3.org/TR/shacl/#DatatypeConstraintComponent)
and explicit numeric lexical patterns based on [XSD datatypes](https://www.w3.org/TR/xmlschema11-2/).

Mapped standard types are checked even when used for COMPLEX. Other COMPLEX
literal datatypes remain opaque; this profile does not validate their
application-specific internal structure. Parsers must preserve lexical forms
so invalid input is not normalized away before validation.

## 5. Unit Contract

| ID | Requirement |
| --- | --- |
| `ISOP-UNIT-001` | Every referenced definition declares at least one IRI-valued `qudt:Unit`. |
| `ISOP-ASSIGN-UNIT-001` | Every VSO state in this profile declares exactly one used unit. |
| `ISOP-ASSIGN-UNIT-002` | The used unit is one of the units allowed by the referenced ISOProps definition. |

ISOProps uses `http://qudt.org/vocab/unit/UNITLESS` for properties without a physical unit. The VSO Core continues to allow a missing unit; the ISOProps profile deliberately tightens that rule.
