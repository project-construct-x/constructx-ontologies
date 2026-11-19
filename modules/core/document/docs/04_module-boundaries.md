# Module Boundaries of the Document Core Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`

## 1. Purpose

This document assigns document concepts to the responsible Construct-X modules. The Document Core module describes document-like resources, document references, and technical distributions without taking over actor roles, provenance, evidence, credentials, signatures, rights, or workflows.

## 2. Guiding Principles

1. `Document` describes a document-like information object.
2. `DocumentDistribution` describes a specific technical manifestation or delivery form.
3. `DocumentReference` describes a contextual reference.
4. Domain-specific document types and document statuses are controlled reference values, rather than a class hierarchy.
5. Actor roles associated with a document are handled through `core/participation`.
6. Generation, derivation, and revision belong in a provenance profile.
7. UBL is a comparative source, rather than a dependency or planned mapping.

## 3. Responsibilities by Module

| Module | Owns | Explicitly Does Not Own |
| --- | --- | --- |
| `core/document` | `Document`, `DocumentReference`, `DocumentDistribution`, document type, document status, general document metadata | Actor roles, signatures, credentials, evidence, workflow, rights, storage |
| `core/agent` | General actor concept | Document metadata and document references |
| `core/participation` | An Agent plays a role in a context | Document content, file or distribution semantics |
| `core/person` | Intrinsic personal data | Author, issuer, or recipient properties on a document |
| `core/organization` | Organizational master data and structure | Publisher, sender, or issuer properties on a document |
| `core/contact` | Contactability | Document delivery, document content, or document status |
| `core/address` | Addresses and location assignments | Documents, files, or distributions |
| Future provenance profile | Generation, derivation, revision, processing | General document master data |
| Future Evidence/Credential profile | Evidence semantics, credential verifiability, revocation | General document core |
| Future rights/policy profile | Access, license terms, redistribution rules | Document core and technical distribution |
| Domain modules | Mandatory documents and domain-specific document roles for each process | General Document Core concept |

## 4. Boundary with `core/participation`

Actor roles associated with a document are not introduced as dedicated properties in the Document Core.

A Document provides the context for a Participation. An Agent plays a role such as `issuer`, `recipient`, `author`, or `publisher`.

Examples:

| Context | Actor | Role |
| --- | --- | --- |
| Invoice 4711 | Organization A | `issuer` |
| Invoice 4711 | Organization B | `recipient` |
| Structural drawing version 3 | Person X | `author` |
| Structural drawing version 3 | Organization Y | `publisher` |

This prevents properties such as `documentIssuer`, `documentSender`, `documentReceiver`, `documentAuthor`, and `documentPublisher` from entering the core.

## 5. Boundary with Provenance

Provenance describes how a document originated, what it was derived from, or which activity generated it.

| Resource | Property | Target |
| --- | --- | --- |
| Document version 3 | `wasDerivedFrom` | Document version 2 |
| Document version 3 | `wasGeneratedBy` | Export run X |

Such statements are not the same as document metadata or actor roles. The Document Core may be aligned with PROV-O later, but does not copy provenance semantics into the core.

## 6. Boundary with Evidence and Credentials

A document may be used as evidence. This does not mean that every document is an Evidence or Credential resource.

| Layer | Example |
| --- | --- |
| Document | PDF of a certificate |
| Evidence profile | This document demonstrates compliance with Requirement X |
| Credential profile | This credential was issued by Issuer Y for Subject Z |

Requirement satisfaction, credential status, revocation, cryptographic proofs, and verification methods do not belong in `core/document`.

## 7. Boundary with Signatures and Trust

The Document Core does not model electronic signatures, seals, timestamps, trust lists, or eIDAS/ETSI verification logic.

A signed PDF file may be described as a distribution of a document. Signature validity and legal evidential value belong in a future Trust or Evidence profile.

## 8. Boundary with Rights and Access

The Document Core provides no access control. A file may exist without the model describing who may read, redistribute, delete, or license it.

License or rights information may be considered later as simple metadata or within a policy profile. ODRL remains a possible alignment source for this purpose.

## 9. Boundary with UBL

UBL remains a comparative source for the Document Core module. In particular, `DocumentReference`, `Attachment`, and `ExternalReference` illustrate which domain-specific information may arise in business processes.

The following applies to the MVP:

- no `owl:imports` of UBL,
- no local UBL copies,
- no UBL mapping as a deliverable,
- no mandatory UBL structure in the core.

## 10. T-Box and A-Box Separation

### T-Box Terms

- `Document`
- `DocumentReference`
- `DocumentDistribution`
- `DocumentType`
- `DocumentStatus`
- `hasDocumentReference`
- `referencesDocument`
- `hasDistribution`
- `documentType`
- `documentStatus`
- Local metadata properties for title, description, language, version, date information, and filename
- Direct use of `dcterms:references`, `dcat:accessURL`, `dcat:downloadURL`, and `dcat:mediaType`

### A-Box or Reference Vocabularies

- `document-type`: controlled document types,
- `document-status`: controlled document statuses.

Specific documents, document numbers, files, URLs, and role relationships are instance data maintained by data holders.

## 11. Import and Alignment Strategy

| Source | Classification |
| --- | --- |
| Dublin Core Terms | Alignment for local general metadata; `dcterms:references` for external reference targets |
| DCAT 3 | Direct reuse of `accessURL`, `downloadURL`, and `mediaType`; alignment for distributions |
| ADMS/SKOS | Existing pattern for identifiers and controlled values |
| Schema.org | Alignment source for web interoperability |
| FOAF | Simple alignment with `foaf:Document`, rather than adoption as the core model |
| PROV-O | Future provenance profile or alignment |
| UBL | Comparative source, not a dependency |

All external namespaces used are documented as `referenced-not-imported` in `module.yaml`. The T-Box declares no `owl:imports`.

## 12. Illustrative Example

> The Document module can record that an inspection report exists and is available as a PDF. Who signed it, whether the signature is valid, and who may read it remain the responsibility of signature, trust, and access models.