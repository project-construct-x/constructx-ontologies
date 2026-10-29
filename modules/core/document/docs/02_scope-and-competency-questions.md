# Scope and Competency Questions of the Document Core Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`  
**Implementation status:** T-Box, reference vocabularies, and Core Shapes implemented

## 1. Purpose

The Document Core module describes document-like resources, document references, and technical distributions. It makes documents unambiguously referenceable in Construct-X without duplicating a document management, archive, signature, credential, rights, or workflow model.

This document defines the domain scope and competency questions of the MVP. Classes, properties, IRIs, and cardinalities are implemented in the T-Box and Core Shapes. External terms used are documented as `referenced-not-imported`.

The domain rationale is provided in the [Source Analysis](01_source-analysis.md).

## 2. Confirmed Scope

| Area | MVP Decision |
| --- | --- |
| Document core | Dedicated Construct-X class `Document` for document-like information objects |
| External alignments | Schema.org, FOAF, and Dublin Core are alignment targets, rather than the local core concept |
| Document reference | Dedicated resource `DocumentReference` when a context resource references a document |
| File/technical delivery form | DCAT-oriented separation through `DocumentDistribution`; `Attachment` remains only a UBL comparison term |
| Metadata | Title, description, language, version, and central date information are optional |
| Date information | Created, issued, modified, and valid are optional core elements |
| Document type | Small controlled MVP vocabulary `DocumentType` |
| Document status | Small controlled MVP vocabulary `DocumentStatus` |
| Identifiers | Reuse of `core/identifier` and its ADMS/SKOS contract |
| Actor roles | Issuer, sender, recipient, author, publisher, and similar roles modeled through `core/participation` |
| Provenance | PROV-O used only for actual generation, derivation, revision, or processing |
| UBL | Comparative source only; no dependency or currently planned mapping |
| Signatures and credentials | Outside the Document Core; future Trust/Evidence profiles are possible |
| Rights and access | No policy or access control in the Document Core |

## 3. Domain Target Model

| Element | Structure or Responsibility |
| --- | --- |
| Domain context | References a `DocumentReference` |
| `DocumentReference` | `referencesDocument` links to `Document`; `hasDistribution` links to `DocumentDistribution`; may carry reference metadata |
| `Document` | Title, description, language, identifiers, document type, document status, date information, and distributions |
| `DocumentDistribution` | URI or download/access information, filename, and media type |
| Actor roles associated with a document | `core/participation` |
| Generation, derivation, revision | Future PROV-O alignment or provenance profile |

This representation shows domain-level connections. External vocabularies are documented in `module.yaml` as references without `owl:imports`.

## 4. Competency Questions

### DCQ-01: How is a document referenced unambiguously?

A document receives a stable IRI in the namespace of its data holder. This IRI is the document's technical RDF identity. Domain-specific document numbers, register identifiers, UUIDs, or external archive numbers are additional identifiers and do not replace the document IRI.

The model must support:

- a document with a stable IRI,
- a document with multiple identifiers,
- the respective identification scheme,
- the responsible scheme agency,
- separation between the resource IRI and the domain-specific identifier.

### DCQ-02: What distinguishes `Document`, `DocumentReference`, and `DocumentDistribution`?

`Document` describes the document-like information object. An invoice, contract, certificate, or drawing may be a document in the domain sense without referring to a specific file.

`DocumentReference` describes a contextual reference to a document. It is needed when another resource references a document and the reference may carry its own information, such as reference type, context, language, version, or validity.

`DocumentDistribution` describes the specific technical manifestation or delivery form, such as a PDF file, download link, or another retrievable file.

The model must support:

- a document without a known file,
- a document with multiple distributions,
- a context resource with one or more document references,
- a document reference pointing to a locally modeled document or an external document resource.

### DCQ-03: How does a domain context resource reference a document?

A domain resource should not necessarily point directly to a file. It references a `DocumentReference`. The reference may then point to a modeled `Document`, an external resource, or a distribution.

Example:

| Resource | Property | Target |
| --- | --- | --- |
| Order 123 | `hasDocumentReference` | Reference to contract annex A |
| Reference to contract annex A | `referencesDocument` | Contract annex A |
| Reference to contract annex A | `hasDistribution` | PDF file of the contract annex |

This allows future profiles to specify which document references are mandatory in particular domain contexts without introducing those requirements into the Document Core itself.

### DCQ-04: Which general metadata belongs in the Document Core?

The Document Core should provide general metadata that is useful across documents:

- title,
- description,
- language,
- version,
- creation date,
- issue date,
- modification date,
- validity.

These elements are not universally mandatory in the open core. A future profile determines whether a particular document type requires a title, version, or issue date.

### DCQ-05: How are document types modeled?

Document types are implemented as controlled concepts rather than subclasses of the Document Core. This keeps the core small and extensible.

The separate MVP reference vocabulary contains the following initial values:

- contract,
- invoice,
- delivery note,
- certificate,
- report,
- plan or drawing,
- evidence document,
- other document.

### DCQ-06: How are document statuses modeled?

Document status describes the state of a document, rather than its type or process step.

Examples:

| Document Type | Document Status |
| --- | --- |
| Invoice | Issued |
| Contract | Draft |
| Certificate | Expired |

The separate MVP reference vocabulary contains the following document-related status values:

- draft,
- issued or released,
- superseded,
- revoked or withdrawn,
- expired,
- archived.

Workflow states such as “under review,” “awaiting approval,” or “assigned to the legal department” do not belong in the Document Core.

### DCQ-07: How are date concepts distinguished?

The Document Core should support several optional date concepts because a single general document date would be too ambiguous from a domain perspective.

| Date | Meaning |
| --- | --- |
| Created | When the document was generated |
| Issued | When the document was formally issued in its domain context |
| Modified | When the content was last changed |
| Valid from | Beginning of domain-specific validity |
| Valid until | End of domain-specific validity |

Validity is not the same as publication, link expiry, or archiving. The MVP uses two optional values, `validFrom` and `validUntil`; both may be expressed as `xsd:date` or `xsd:dateTime`.

### DCQ-08: How are files and technical delivery forms described?

A file or technical delivery form is modeled as a `DocumentDistribution`. It is not identical to the document itself.

The model must support:

- a distribution with a URI,
- a distribution with a filename,
- a distribution with a media type,
- multiple distributions for the same document, such as PDF and XML,
- a distribution used through a document reference.

Media types should align with IANA. A storage, upload, repository, or archive model does not belong in the Document Core.

### DCQ-09: How are issuer, sender, recipient, author, and publisher modeled?

These actor roles are not introduced as dedicated direct properties in the Document Core. They are modeled through `core/participation`: an Agent plays a controlled role in the context of a document or document reference.

Invoice example:

| Context | Actor | Role |
| --- | --- | --- |
| Invoice 4711 | Organization A | `issuer` |
| Invoice 4711 | Organization B | `recipient` |

Construction drawing example:

| Context | Actor | Role |
| --- | --- | --- |
| Structural drawing version 3 | Person X | `author` |
| Structural drawing version 3 | Organization Y | `publisher` |
| Structural drawing version 3 | Organization Z | `recipient` |

Permit decision example:

| Context | Actor | Role |
| --- | --- | --- |
| Building permit | Authority A | `issuer` |
| Building permit | Applicant B | `recipient` |

A future profile may specify that a particular document type must have exactly one issuer or at least one recipient. These cardinalities do not belong in the general Document Core.

### DCQ-10: When is PROV-O relevant?

PROV-O is relevant when describing the generation, derivation, revision, or processing of a document.

Examples:

- A PDF file was generated from dataset Y.
- Document version 3 replaces document version 2.
- An inspection report was generated by activity X.

These statements describe provenance. They are not the same as domain-specific actor roles associated with a document. Author, issuer, sender, and recipient are handled through `core/participation`; generation, derivation, and revision may be aligned with PROV-O later.

### DCQ-11: How are Evidence, Credentials, and signatures distinguished?

A document may be used as evidence, but this does not make the Document Core module an Evidence or Credential model.

The model may represent that a document exists and is referenced. The semantics of “demonstrates compliance with Requirement X,” “is a Verifiable Credential,” “was cryptographically signed,” or “has qualified legal validity” belong in future profiles or specialized modules.

### DCQ-12: How are rights, licenses, and access handled?

A simple license or rights URI may be considered as general metadata later. Access control, role-based rights, confidentiality, consent, redistribution rules, and policy evaluation are outside the Document Core.

ODRL remains a possible future alignment source for rights and policy profiles.

### DCQ-13: Which validation questions does the Core SHACL Profile address?

The implemented Core SHACL Profile checks:

- that `Document`, `DocumentReference`, and `DocumentDistribution` are correctly typed,
- that document types use only values from the approved document type vocabulary,
- that document statuses use only values from the approved document status vocabulary,
- that date values use appropriate datatypes,
- that distributions use a valid IRI when a URI is provided,
- that media types are used consistently as technical format information,
- that identifiers follow the existing ADMS/SKOS pattern,
- that no direct Document Core properties are required for issuer, author, publisher, sender, or recipient.

## 5. Explicitly Outside the Document Core

- Invoice, delivery note, contract, certificate, or report classes,
- UBL dependencies and UBL mappings,
- signature, seal, timestamp, and trust-list models,
- Verifiable Credentials and Data Integrity proofs,
- Evidence/Requirement semantics,
- workflow status, approval processes, and task management,
- access control, permissions, data protection, and policy evaluation,
- archiving, file plans, retention, and records management,
- full text, OCR, pages, sections, and annotations,
- storage-specific, upload-specific, repository-specific, or DMS-specific concepts,
- domain-specific mandatory documents and allowlists.

These exclusions do not prevent future links to corresponding resources. They only establish that their semantics are not owned by the Document Core.

## 6. Resolved Modeling Decisions

| Topic | Decision | Rationale |
| --- | --- | --- |
| Local document concept | Dedicated class `Document` | Construct-X requires a stable core concept and can align external concepts |
| File vs. document | Separation through `DocumentDistribution` | A file is only a manifestation or delivery form of a document |
| UBL | Comparative source only | No current mapping or planned dependency |
| Document type | Small MVP vocabulary | Profiles need a shared starting point without proliferating classes |
| Document status | Small MVP vocabulary | Document state is a recurring domain requirement; workflow status remains outside |
| Actor roles | Through `core/participation` | Prevents direct properties for every possible role |
| Provenance | Future PROV-O alignment or profile | Generation and derivation have different semantics from document metadata |

## 7. Finalized Modeling Decisions

| Topic | Decision |
| --- | --- |
| External terms | Local metadata properties with alignment; direct reuse of DCAT access properties |
| Date model | Optional `validFrom` and `validUntil` values |
| Type vocabulary | Eight approved MVP values in a separate SKOS vocabulary |
| Status vocabulary | Six approved MVP values in a separate SKOS vocabulary |
| Distribution | Local `DocumentDistribution`, directly using `dcat:accessURL`, `dcat:downloadURL`, and `dcat:mediaType` |
| Document reference | At least one target required by the Core Shape |

## 8. Acceptance Criteria for the Shape Phase

The shape phase is complete because:

1. the T-Box and reference vocabularies have been syntactically validated,
2. the agreed classes and properties are fully implemented,
3. the reference vocabularies are available with separate versioning,
4. the SHACL requirements match the implemented T-Box,
5. valid and invalid RDF test graphs are checked automatically,
6. all approved error codes are covered by negative test cases,
7. the generated HTML documentation and repository-wide tests include the module.

## 9. Planned Follow-Up Tasks

Mandatory domain-specific metadata for individual document types, stricter role rules, and further integration requirements will be developed in dedicated profiles as needed.

## 10. Illustrative Example

> A delivery note may reference a contract. The Document Core describes the contract, reference, and file, but requires no delivery-note-specific mandatory role.