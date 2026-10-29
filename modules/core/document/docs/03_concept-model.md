# Domain Conceptual Model of the Document Core Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`  
**Implementation status:** T-Box, reference vocabularies, and Core Shapes implemented

## 1. Purpose

The conceptual model describes the implemented document-related core of the Construct-X ontology network. It combines the source analysis, confirmed scope decisions, and term catalog into a consistent domain model.

The complete Mermaid diagrams are provided in the [Domain Concept Diagram for Document](diagrams/document-concept-model.md). Classes and properties are documented in the [Term Catalog](05_term-catalog.md). Module boundaries are described in [module-boundaries.md](04_module-boundaries.md).

## 2. Model Core

The MVP defines five local core concepts:

```text
Document
DocumentReference
DocumentDistribution
DocumentType
DocumentStatus
```

These concepts represent three distinct levels:

1. document-like content,
2. contextual reference to a document,
3. technical delivery as a file, download, or comparable distribution.

Actor roles, signatures, credentials, evidence, rights, workflows, archiving, and storage are not defined in the Document Core.

## 3. Basic Model

| Resource | Property or Information | Target |
| --- | --- | --- |
| Domain context | Contextual reference | `DocumentReference` |
| `DocumentReference` | `referencesDocument` | `Document` |
| `DocumentReference` | `hasDistribution` | `DocumentDistribution` |
| `Document` | `documentType` | Controlled document type |
| `Document` | `documentStatus` | Controlled document status |
| `Document` | Identifiers | Identifier resources |
| `Document` | Metadata | General descriptive information |
| `Document` | `hasDistribution` | `DocumentDistribution` |

A domain resource does not necessarily reference a file directly. It references a document reference. The document reference may point to a document modeled in the graph, an external document resource, or a specific distribution.

## 4. Classes

### 4.1 `Document`

`Document` is a dedicated Construct-X class for a document-like information object. The concept is independent of a specific file.

A document may be:

- an invoice,
- a contract,
- a certificate,
- a report,
- a plan or drawing,
- an evidence document.

A document is not automatically:

- a PDF file,
- a download link,
- a DMS record,
- a Credential,
- an Evidence resource,
- a signed artifact,
- a workflow object.

External concepts such as `schema:DigitalDocument`, `foaf:Document`, or Dublin Core resource concepts may serve as future alignment targets. They do not replace the local Construct-X core concept.

### 4.2 `DocumentReference`

`DocumentReference` is a separate resource for a contextual reference to a document.

It is required when the reference itself may carry domain-specific information, for example:

- which context references the document,
- which type of document is expected,
- which version or language is referenced,
- whether the reference points to a modeled document or only an external resource,
- which distribution is used in the context.

A direct property from the domain context to a file is insufficient for this purpose.

### 4.3 `DocumentDistribution`

`DocumentDistribution` describes a specific technical manifestation or delivery form of a document. The concept follows the DCAT approach.

Examples:

- a PDF file,
- an XML file,
- an HTML view,
- a download link,
- a retrievable external file.

Multiple distributions may represent the same document. For example, an inspection report may have PDF, XML, and HTML distributions.

A distribution is not a storage, upload, archive, or repository model.

### 4.4 `DocumentType`

`DocumentType` is a controlled document type. Document types are represented as reference vocabulary values rather than local subclasses of `Document`.

This keeps the core stable: a `Document` references `document-type:invoice` through `documentType`, rather than introducing `InvoiceDocument rdfs:subClassOf Document`.

Domain-specific profiles may later define stricter rules for particular document types.

### 4.5 `DocumentStatus`

`DocumentStatus` is a controlled document-related state.

Status describes neither the document type nor the process step.

| Document Type | Document Status |
| --- | --- |
| Certificate | Expired |

Workflow states such as “under review,” “awaiting approval,” or “assigned to the legal department” do not belong in the Document Core.

## 5. Document, Reference, and Distribution

The three concepts must not be conflated.

| Question | Model Concept |
| --- | --- |
| What is the document-like content? | `Document` |
| Why or where is it referenced? | `DocumentReference` |
| Which specific file or technical delivery form exists? | `DocumentDistribution` |

Example:

| Resource | Property | Target or Value |
| --- | --- | --- |
| Order 123 | `hasDocumentReference` | Contract annex reference |
| Contract annex reference | `referencesDocument` | Contract annex A |
| Contract annex reference | `hasDistribution` | `vertragsanlage-a.pdf` |
| Contract annex A | `documentType` | `contract` |
| Contract annex A | `documentStatus` | `issued` |

This separation allows a document to be known without a file, to have multiple files, or to be referenced only externally.

## 6. Metadata

The Document Core should provide general metadata. These elements are not universally mandatory in the open core.

| Metadata | Meaning |
| --- | --- |
| Title | Display name or domain-specific document title |
| Description | Free-text description |
| Language | Language of the document content |
| Version | Document version or edition designation |
| Created | Generation date or time |
| Issued | Formal issue date in the domain context |
| Modified | Last known modification |
| Valid from | Beginning of domain-specific validity |
| Valid until | End of domain-specific validity |

General metadata is maintained as local `conx-doc` properties and linked through `rdfs:seeAlso` to appropriate Dublin Core and Schema.org concepts. Technical distributions directly use `dcat:accessURL`, `dcat:downloadURL`, and `dcat:mediaType`.

## 7. Identifiers

Document identifiers follow the existing Construct-X ADMS/SKOS pattern.

A `Document` references an `adms:Identifier` through `adms:identifier`. The identifier is described using `skos:notation` and `adms:schemaAgency`.

The resource IRI and domain-specific identifiers remain separate. The Document Core introduces no dedicated number properties such as `documentNumber`, `invoiceNumber`, `contractNumber`, `uuidValue`, or `archiveId`.

## 8. Actor Roles

Actor roles associated with a document are modeled through `core/participation`.

An Agent plays a role in the context of a `Document` or `DocumentReference`.

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

The Document Core therefore introduces no direct properties for issuer, sender, recipient, author, or publisher. Profiles may later specify that particular roles are mandatory for particular document types.

## 9. Provenance

Provenance describes the generation, derivation, revision, or processing of a document.

Examples:

- A PDF was generated from dataset Y.
- Document version 3 replaces document version 2.
- An inspection report was generated by activity X.

These semantics do not belong in the Document Core. PROV-O remains a future alignment or profile source for this purpose.

## 10. UBL as a Comparative Source

UBL shows that document references and technical attachments may carry their own metadata in business processes. This observation supports the separation of `DocumentReference` and `DocumentDistribution`.

However, the following applies to the MVP:

- no UBL import,
- no UBL copies,
- no UBL mapping as a deliverable,
- no mandatory UBL structure in the Document Core.

## 11. Outside the Document Core

The following topics do not belong in the Document Core:

- invoice, delivery note, contract, certificate, or report classes,
- direct actor properties such as issuer, sender, recipient, author, or publisher,
- signature, seal, timestamp, and trust-list models,
- Verifiable Credentials and Data Integrity proofs,
- Evidence/Requirement semantics,
- workflow status, approval processes, and task management,
- access control, permissions, and policy evaluation,
- archiving, file plans, retention, and records management,
- full text, OCR, pages, sections, and annotations,
- storage-specific, upload-specific, repository-specific, or DMS-specific concepts,
- UBL dependencies or UBL mappings.

## 12. Modeling Decisions

| Topic | Decision |
| --- | --- |
| Local document concept | Dedicated class `Document` |
| References | Dedicated class `DocumentReference` |
| Files | DCAT-oriented class `DocumentDistribution` |
| Document types | Controlled MVP vocabulary |
| Document status | Controlled MVP vocabulary |
| Identifiers | Reuse of the ADMS/SKOS pattern |
| Actor roles | Modeled through `core/participation` |
| Provenance | Outside the core; future PROV-O alignment or profile |
| UBL | Comparative source only |

## 13. Finalized Detailed Decisions

| Topic | Decision |
| --- | --- |
| External properties | Local `conx-doc` metadata properties with alignment; direct use of technical DCAT properties |
| Validity | Optional `validFrom` and `validUntil` values |
| Type vocabulary | `contract`, `invoice`, `deliveryNote`, `certificate`, `report`, `plan`, `evidenceDocument`, `other` |
| Status vocabulary | `draft`, `issued`, `superseded`, `withdrawn`, `expired`, `archived` |
| Distribution | `dcat:accessURL`, `dcat:downloadURL`, and `dcat:mediaType`; local `fileName` |
| DocumentReference | At least one target in the Core Shape: document, external resource, or distribution |

## 14. Implementation Status

`module.yaml`, `ontology/conx-doc.ttl`, the reference vocabularies, `shapes/conx-doc-core.shacl.ttl`, examples, and tests implement the confirmed [SHACL Requirements](06_shacl-requirements.md).

## 15. Illustrative Example

> An inspection report is a Document. Its PDF file is a distribution. If a contract references the report, a DocumentReference is used rather than creating a second copy of the document.