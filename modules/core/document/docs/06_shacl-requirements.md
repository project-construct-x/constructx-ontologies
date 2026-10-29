# Domain-Specific SHACL Requirements for the Document Core Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Document Core Shapes  
**Implementation status:** Core shape graph and automated test cases available

## 1. Purpose

This document describes the binding data quality requirements of the Document Core module. The executable implementation is located at `modules/core/document/shapes/conx-doc-core.shacl.ttl`.

## 2. Shape Set

```text
Shape graph: modules/core/document/shapes/conx-doc-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/document/core
Version IRI: https://www.construct-x.org/shapes/document/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/document/core#
Prefix:      conx-doc-sh
Version:     0.1.0
```

## 3. Validation Principles

- OWL describes the open semantics of the concepts; SHACL checks concrete data submissions against the core profile.
- Mandatory fields and maximum cardinalities are not encoded as strict OWL cardinalities in the open T-Box.
- Additional properties remain permitted; the shape set does not use `sh:closed true`.
- All core violations use `sh:Violation`.
- Every named Property Shape has a German and an English message with a stable requirement identifier.
- Validation requires no RDFS or OWL inference.

## 4. Responsibility Boundaries

| Requirement | Responsible Shape Set | Rule in the Document Core Shape |
| --- | --- | --- |
| Documents, references, and distributions | `document/core` | Check typing and core structure |
| Document types and document statuses | `document/core` plus reference vocabularies | Check values against approved value sets |
| Identifiers | ADMS/SKOS contract in `document/core` | Reuse the existing identifier structure |
| Actor roles | `participation/core` or profile | No direct role properties in the Document Core |
| Provenance | Provenance profile | Outside the Document Core Shape |
| Evidence, credentials, and signatures | Trust/Evidence profiles | Outside the Document Core Shape |
| Rights and access | Policy profile | Outside the Document Core Shape |
| UBL structures | No current mapping | Comparative source only; no validation dependency |

## 5. Shape Catalog

| Shape IRI | Type | Target or Usage | Purpose |
| --- | --- | --- | --- |
| `conx-doc-sh:DocumentContextShape` | Node Shape | Subjects of `hasDocumentReference` | Checks contextual reference values |
| `conx-doc-sh:DocumentCarrierShape` | Node Shape | Subjects of `documentType` or `hasDistribution` | Requires type `Document` or `DocumentReference` |
| `conx-doc-sh:DocumentShape` | Node Shape | Document targets | Checks document core and metadata |
| `conx-doc-sh:DocumentReferenceShape` | Node Shape | Reference targets | Checks document references and reference targets |
| `conx-doc-sh:DocumentDistributionShape` | Node Shape | Distribution targets | Checks technical distributions |
| `conx-doc-sh:DocumentTypeConceptShape` | Node Shape | Values of `documentType` | Checks approved document types |
| `conx-doc-sh:DocumentStatusConceptShape` | Node Shape | Values of `documentStatus` | Checks approved document statuses |
| `conx-id-sh:ADMSIdentifierShape` | Node Shape from `identifier/core` | Values of `adms:identifier` | Checks the shared ADMS/SKOS identifier contract |
| `conx-doc-sh:StringOrLangStringShape` | Reusable Node Shape | Text values | Allows `xsd:string` or `rdf:langString` |
| `conx-doc-sh:NonEmptyStringOrLangStringShape` | Reusable Node Shape | Domain-specific text | Requires non-empty text values |
| `conx-doc-sh:NonEmptyStringShape` | Reusable Node Shape | Technical text values | Requires non-empty `xsd:string` values |
| `conx-doc-sh:DateOrDateTimeShape` | Reusable Node Shape | Date values | Allows `xsd:date` or `xsd:dateTime` |

## 6. Targets

### 6.1 Context and Shared Properties

`DocumentContextShape` uses `sh:targetSubjectsOf conx-doc:hasDocumentReference`. Every value must be an explicitly typed `DocumentReference` resource (`DOC-CTX-001`).

`DocumentCarrierShape` uses `sh:targetSubjectsOf conx-doc:documentType` and `sh:targetSubjectsOf conx-doc:hasDistribution`. The subject must be explicitly typed as `Document` or `DocumentReference` (`DOC-CAR-001`). This checks shared properties without retyping references as documents.

### 6.2 Documents

`DocumentShape` uses:

- `sh:targetClass conx-doc:Document`,
- `sh:targetObjectsOf conx-doc:referencesDocument`,
- `sh:targetSubjectsOf conx-doc:documentStatus`.

### 6.3 Document References

`DocumentReferenceShape` uses:

- `sh:targetClass conx-doc:DocumentReference`,
- `sh:targetObjectsOf conx-doc:hasDocumentReference`,
- `sh:targetSubjectsOf conx-doc:referencesDocument`.

### 6.4 Distributions

`DocumentDistributionShape` uses:

- `sh:targetClass conx-doc:DocumentDistribution`,
- `sh:targetObjectsOf conx-doc:hasDistribution`,
- `sh:targetSubjectsOf conx-doc:fileName`.

External DCAT properties are deliberately not global targets. They are checked only on resources already recognized as `DocumentDistribution`.

## 7. Node Constraints

| ID | Focus | Requirement |
| --- | --- | --- |
| `DOC-CTX-001` | Context resource | `hasDocumentReference` references a typed `DocumentReference` |
| `DOC-CAR-001` | Document carrier | The subject of shared properties is a `Document` or `DocumentReference` |
| `DOC-DOC-001` | `Document` | Focus value is an IRI or blank node |
| `DOC-DOC-002` | `Document` | Explicit type `conx-doc:Document` |
| `DOC-REF-001` | `DocumentReference` | Focus value is an IRI or blank node |
| `DOC-REF-002` | `DocumentReference` | Explicit type `conx-doc:DocumentReference` |
| `DOC-DIST-001` | `DocumentDistribution` | Focus value is an IRI or blank node |
| `DOC-DIST-002` | `DocumentDistribution` | Explicit type `conx-doc:DocumentDistribution` |

## 8. Property Constraints for `Document`

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `DOC-DOC-010` | `title` | 0 | Unbounded | Non-empty string or language-tagged literal |
| `DOC-DOC-011` | `description` | 0 | Unbounded | Non-empty string or language-tagged literal |
| `DOC-DOC-012` | `language` | 0 | Unbounded | Non-empty `xsd:string` |
| `DOC-DOC-020` | `documentType` | 0 | 1 | IRI from the approved document type vocabulary |
| `DOC-DOC-021` | `documentStatus` | 0 | 1 | IRI from the approved document status vocabulary |
| `DOC-DOC-030` | `version` | 0 | 1 | Non-empty `xsd:string` |
| `DOC-DOC-040` | `created` | 0 | 1 | `xsd:date` or `xsd:dateTime` |
| `DOC-DOC-041` | `issued` | 0 | 1 | `xsd:date` or `xsd:dateTime` |
| `DOC-DOC-042` | `modified` | 0 | 1 | `xsd:date` or `xsd:dateTime` |
| `DOC-DOC-043` | `validFrom` | 0 | 1 | `xsd:date` or `xsd:dateTime` |
| `DOC-DOC-044` | `validUntil` | 0 | 1 | `xsd:date` or `xsd:dateTime` |
| `DOC-DOC-045` | Validity ordering | - | - | `validFrom` is not later than `validUntil` |
| `DOC-DOC-050` | `hasDistribution` | 0 | Unbounded | Typed `DocumentDistribution` resource |
| `DOC-DOC-060` | `adms:identifier` | 0 | Unbounded | Validly structured ADMS identifier resource |

For unambiguous comparison, `validFrom` and `validUntil` should use the same datatype.

## 9. Property Constraints for `DocumentReference`

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | --- | --- | --- |
| `DOC-REF-010` | `referencesDocument` | 0 | 1 | Explicitly typed `Document` resource |
| `DOC-REF-011` | `dcterms:references` | 0 | 1 | IRI of an external document resource |
| `DOC-REF-012` | `hasDistribution` | 0 | Unbounded | Typed `DocumentDistribution` resource |
| `DOC-REF-013` | Reference target | 1 alternative | - | Document, external IRI, or distribution |
| `DOC-REF-020` | `documentType` | 0 | 1 | IRI from the approved document type vocabulary |
| `DOC-REF-030` | `adms:identifier` | 0 | Unbounded | Validly structured ADMS identifier resource |

## 10. Property Constraints for `DocumentDistribution`

| ID | Property | Minimum | Maximum | Value Requirement |
| --- | --- | ---: | ---: | --- |
| `DOC-DIST-010` | `dcat:accessURL` | 0 | Unbounded | IRI |
| `DOC-DIST-011` | `dcat:downloadURL` | 0 | Unbounded | IRI |
| `DOC-DIST-020` | `fileName` | 0 | 1 | Non-empty `xsd:string` |
| `DOC-DIST-030` | `dcat:mediaType` | 0 | 1 | IANA-oriented IRI |

A distribution may exist as a technical placeholder without an access URL. The Core Shape does not enforce a storage or archive model.

## 11. Identifier Constraints

The error codes in this section are provided by the imported `identifier/core` shape graph. The Document Shape defines only which document and reference resources use `adms:identifier`.

| ID | Requirement |
| --- | --- |
| `ID-001` | Identifier resource is explicitly typed as `adms:Identifier` |
| `ID-002` | Exactly one literal `skos:notation` |
| `ID-003` | At most one `adms:schemaAgency` as `xsd:string` |

## 12. Controlled Values

The Document Type vocabulary contains `contract`, `invoice`, `deliveryNote`, `certificate`, `report`, `plan`, `evidenceDocument`, and `other`.

The Document Status vocabulary contains `draft`, `issued`, `superseded`, `withdrawn`, `expired`, and `archived`.

The shapes check the IRI, `skos:Concept`, the local class type, and a closed `sh:in` list. Vocabulary extensions therefore require deliberate versioning of both the reference vocabulary and the shape set.

## 13. Test Cases

Valid test graphs:

- `minimal-document.ttl`,
- `complete-document.ttl`,
- `multiple-distributions.ttl`,
- `document-references.ttl`,
- `document-with-participation.ttl`.

Invalid test graphs:

- `invalid-document-typing.ttl`,
- `invalid-document-references.ttl`,
- `invalid-distributions.ttl`,
- `invalid-controlled-values.ttl`,
- `invalid-metadata-and-identifiers.ttl`.

The automated suite checks all valid and invalid graphs, SHACL-SHACL conformance, shape metadata, bilingual messages, and coverage of all approved requirement identifiers.

## 14. Outside Validation by the Document Core Shape

- UBL conformance or UBL mappings,
- digital signature validity and credential status,
- Evidence or Requirement satisfaction,
- direct issuer, author, publisher, sender, or recipient roles,
- rights, access, confidentiality, and workflow status,
- URL reachability or file existence,
- DMS, archive, storage, and retention rules,
- mandatory domain-specific metadata for individual document types.

These requirements belong in specialized modules or profiles.

## 15. Illustrative Example

> A document with a title and type, together with a PDF distribution, is valid in the core. If the distribution references neither a download nor an access address, the shape reports a structural error.