# Source Analysis for the Document Core Module

**Status:** Consolidated analysis baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 27 August 2026  
**Scope:** `core/document`  
**Subject:** Documents, document references, distributions, document metadata, and boundaries with evidence and signatures

## 1. Purpose and Method

This analysis evaluates existing ontologies, vocabularies, exchange formats, and legal/trust models as the domain foundation for the implemented Construct-X module `core/document`.

The analysis focuses on:

- general document and information object concepts,
- document references in business and administrative processes,
- attachments, external files, distributions, and formats,
- title, date, language, version, status, and document type,
- identifiers and structured identification,
- authorship, publishers, issuers, and recipients,
- evidence, credentials, signatures, and trust information,
- access rights and terms of use,
- boundaries with `core/agent`, `core/participation`, `core/contact`, `core/organization`, `core/person`, `core/address`, `core/vso`, and future profiles.

This file deliberately provides only foundational research. It does not define a Construct-X T-Box, SHACL rules, or final local IRIs.

Existing domain drafts were not evaluated as modeling templates. They may provide requirements later, but they are not the source of the Document Core structure.

## 2. Source Hierarchy

| Source Type | Relevance to Construct-X | Examples |
| --- | --- | --- |
| General metadata and web vocabularies | Foundation for stable basic concepts | Dublin Core Terms, Schema.org, FOAF |
| Linked Data standards for distribution, versioning, and provenance | Foundation for boundaries and alignment | DCAT 3, PROV-O, ADMS, SKOS |
| Business and administrative exchange formats | Comparative sources for recurring document reference and attachment structures | OASIS UBL 2.5, SEMIC CCCEV/CPSV-AP |
| Trust, signature, and credential standards | Sources for boundaries with evidence and signature models | W3C VC, W3C Data Integrity, DID Core, eIDAS, ETSI ESI |
| Technical registries for file formats | Foundation for media types | IANA Media Types |
| Rights and policy models | Candidates for later profiles, rather than the initial Document Core | ODRL |

A class or property is not adopted solely because it appears in a source. The deciding factors are whether it is stable across domains, can be assigned a clear modular boundary, and is reusable in the Construct-X core.

## 3. Summary of Findings

The most robust foundation for the Document Core is a combination of:

1. [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) for general metadata such as title, description, date, language, identifier, relation, source, version, and validity.
2. [Schema.org CreativeWork, DigitalDocument, and MediaObject](https://schema.org/DigitalDocument) as a broad source for web interoperability involving digital documents, media objects, encodings, URLs, licenses, and publication dates.
3. [OASIS UBL 2.5](https://docs.oasis-open.org/ubl/) as a comparative source for `DocumentReference`, `Attachment`, `ExternalReference`, issue date/time, version, UUID, document type, and referenced documents in business transactions. UBL is not planned as a dependency; no UBL mapping is currently intended.
4. [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) for separating abstract content from specific distributions, download URLs, media types, packaging, and compression.
5. [PROV-O](https://www.w3.org/TR/prov-o/) for origin, derivation, generation, and responsibility, primarily as an alignment or future provenance layer.
6. [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) and [SKOS](https://www.w3.org/TR/skos-reference/) for structured identifiers and controlled vocabularies.

The initial Document Core should therefore not be built as a document management system. A suitable core describes only:

- a document-like information object,
- a contextual document reference,
- an attached or externally referenced file,
- general metadata,
- structured identifiers using the existing ADMS/SKOS pattern,
- clear extension points for signatures, rights, evidence, versioning, and provenance.

Signatures, credentials, access rights, approval processes, archiving, file plans, and domain-specific document types should not be incorporated into the initial Document Core.

## 4. Sources Evaluated

| Source | Version Used | Role in the Analysis | Provisional Use |
| --- | --- | --- | --- |
| [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | DCMI Recommendation, current specification accessed 2026-08-27 | General resource metadata | Primary source for title, description, date, identifier, language, relation, source, version, and validity |
| [Schema.org DigitalDocument](https://schema.org/DigitalDocument), [CreativeWork](https://schema.org/CreativeWork), [MediaObject](https://schema.org/MediaObject) | Development version, accessed 2026-08-27 | Web interoperability | Source for alignment and naming; not adopted as a strict core model |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99, accessed 2026-08-27 | Simple document concept in the Web of Data context | Possible alignment with `foaf:Document`, but too narrow from a domain perspective |
| [OASIS UBL 2.5](https://docs.oasis-open.org/ubl/) | OASIS Standard according to the announcement of 26/27 August 2026; detailed reports additionally checked against CS01/CSD reports | Business documents, document references, attachments | Comparative source; no dependency or currently planned mapping |
| [UBL AttachedDocument Summary Report](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-AttachedDocument-2.5.html) | CS01 report, accessed 2026-08-27 | Detailed structure for `Attachment`, `DocumentReference`, and `ExternalReference` | Comparative field analysis, not a binding specification |
| [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | W3C Recommendation, 22 August 2024 | Catalogs, resources, distributions, download URLs, media types | Reference for specific files and technical distributions |
| [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) | SEMIC Recommendation, 2024-02-01 | Identifiers, assets, version navigation, status | Reuse according to the existing Construct-X identifier model |
| [SKOS Reference](https://www.w3.org/TR/skos-reference/) | W3C Recommendation, 2009 | Controlled concepts and notations | Foundation for document types, status values, and identification schemes |
| [PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation, 2013 | Provenance, derivation, generation, responsibility | Not copied into the core; used later as a provenance and alignment source |
| [SEMIC CCCEV](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/core-criterion-and-core-evidence-vocabulary) | Version 2.2.0, 2026 release | Evidence, criteria, and requirements | Important boundary: Evidence is not simply Document |
| [CPSV-AP 3.2.0](https://semiceu.github.io/CPSV-AP/releases/3.2.0/) | SEMIC Recommendation, 2024 | Public services, evidence, related documentation | Source of requirements for evidence and related documentation |
| [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model/) | W3C Recommendation, 15 May 2025 | Credentials, issuer, subject, validity, status, evidence | Boundary with verifiable evidence; not copied as the Document Core |
| [W3C Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) | W3C Recommendation, 15 May 2025 | Cryptographic proofs for VCs and similar documents | Future signature/proof layer, outside the core |
| [W3C DID Core](https://www.w3.org/TR/did-core/) | W3C Recommendation, 2022 | Controlled identifier documents and verification methods | Relevant only to identity and signature binding |
| [eIDAS Regulation 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) and amendments | EU legal framework | Electronic signatures, seals, timestamps, electronic documents, delivery services | Legal and trust context, outside the T-Box core |
| [ETSI ESI](https://www.etsi.org/technical-groups/esi/) | Continuously maintained standards | Technical standards for signatures, seals, and trust services | Future signature/trust profiles |
| [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) | W3C Recommendation, 2018 | Permissions, prohibitions, and duties for assets | Future rights/policy layer |
| [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | W3C Recommendation, 2017 | Annotations, body, target, SpecificResource, selector | Future references to document parts and comments |
| [IANA Media Types](https://www.iana.org/assignments/media-types) | Registry as of 2026-08-24 | Canonical media types | Preferred source for `mediaType` values |
| [OWL-Time](https://www.w3.org/TR/owl-time/) | W3C Candidate Recommendation Draft, 2022 | Intervals, instants, validity periods | Used only if a full temporal model becomes necessary |

The following internal project documents are relevant to the subsequent modeling phase:

- [Identifier Model](../../../../docs/architecture/identifier-model.md)
- [Namespace Concept](../../../../docs/architecture/construct-x-namespace-konzept.md)
- [Dependency Rules](../../../../docs/architecture/dependency-rules.md)
- [Versioning Rules](../../../../docs/architecture/versioning.md)
- [Agent Specification](../../agent/docs/10_agent-specification.md)
- [Participation Module](../../participation/docs/00_index.md)

## 5. Basic Concepts: Document, Work, File, Reference

### 5.1 Document as an Information Object

A core document should not be confused with a specific file. Many sources distinguish directly or indirectly between:

- intellectual or domain-specific content,
- a specific digital or physical manifestation,
- a reference to this content,
- a file or distribution carrying this content.

Dublin Core deliberately remains general and describes resources through metadata. Schema.org distinguishes `CreativeWork`, `DigitalDocument`, and `MediaObject`. DCAT separates `Resource` or `Dataset` from `Distribution`. ADMS separates `Asset` and `AssetDistribution`.

For Construct-X, this means:

- `Document` is implemented as a dedicated Construct-X class.
- A file, download, or embedded binary is not automatically identical to the domain-level document.
- A `DocumentReference` describes the context in which a resource references a document.
- A specific file or technical delivery form is conceived as a distribution following the DCAT approach, rather than a simple attachment literal.

### 5.2 Document Reference as a Separate Relationship Node

UBL strongly supports the observation that document references in business processes are more than simple links. `DocumentReference` has fields for ID, UUID, IssueDate, IssueTime, DocumentType, DocumentTypeCode, DocumentDescription, VersionID, LanguageID, LocaleCode, ValidityPeriod, IssuerParty, Attachment, and XPath.

This supports a separate reference resource when more than a URI needs to be expressed within a context. A simple direct link property is insufficient once reference type, referenced document date, language, version, validity, or attachment must be kept together.

### 5.3 Attachment and ExternalReference

UBL `Attachment` may contain an embedded document or an external reference. `ExternalReference` includes URI, FileName, FormatCode, EncodingCode, CharacterSetCode, MimeCode, HashAlgorithmMethod, DocumentHash, ExpiryDate, and ExpiryTime.

DCAT treats technical files as distributions with `accessURL`, `downloadURL`, `mediaType`, `format`, `compressFormat`, `packageFormat`, `byteSize`, and other technical access information.

For Construct-X, this means:

- A specific file or technical manifestation should be modeled following the DCAT approach.
- An external file requires at least a URI or distribution extension point.
- Media types should align with IANA.

## 6. Metadata Analysis

### 6.1 Title and Description

Dublin Core `title` and `description` are the natural choices for general metadata. Schema.org uses `name`, `headline`, `abstract`, and `description`, but is considerably broader and more web-oriented.

Implemented decision:

- Titles and descriptions should allow language-tagged literals.
- A domain-specific mandatory title belongs in profiles rather than the general T-Box.
- Where an external vocabulary is directly sufficient, alignment or even direct reuse should be considered instead of requiring local copies.

### 6.2 Date, Issue Time, and Validity

Dublin Core provides `date`, `created`, `issued`, `modified`, `valid`, and further specializations. UBL separates `IssueDate`, `IssueTime`, and `ValidityPeriod`. Schema.org separates `dateCreated`, `dateModified`, `datePublished`, and `expires`. VC uses `validFrom` and `validUntil`.

For Construct-X, the initial decision should not be that “a general documentDate is always sufficient.” At least the following distinct statements exist:

| Statement | Meaning | Likely Source |
| --- | --- | --- |
| Creation date | When the document was generated | DCT, Schema.org, PROV |
| Issue date | When it was formally issued in its domain context | UBL, DCT `issued`, VC `validFrom` |
| Modification date | When the content was last changed | DCT, Schema.org |
| Publication date | When it was published | Schema.org, DCT |
| Validity | Period during which the document or evidence is valid | DCT `valid`, UBL `ValidityPeriod`, VC |
| Expiry/availability | When a link or content ceases to be reliable | UBL `ExpiryDate`, Schema.org `expires` |

Recommendation:

- The important date concepts are implemented as optional elements in the Document Core: created, issued, modified, and valid.
- Local date properties are aligned transparently with DCT or Schema.org.
- Validity boundaries use `xsd:date` or `xsd:dateTime`, rather than arbitrary plain strings.
- Issue date/time may be important for many business documents, but its domain meaning must be distinguished from DCT `issued`.

### 6.3 Language and Locale

Dublin Core `language`, Schema.org `inLanguage`, and UBL `LanguageID`/`LocaleCode` demonstrate the same need. Language is central to documents, particularly multilingual documents and parallel versions.

Recommendation:

- Language should be supported in the core.
- The choice between BCP 47 language codes and a controlled language vocabulary should be made in profiles.
- Locale and language must not be conflated: language describes the content, while locale describes a regional language or presentation variant.

### 6.4 Document Type and Status

Dublin Core `type`, Schema.org `creativeWorkStatus`, ADMS `status`, UBL `DocumentTypeCode`, and `DocumentStatusCode` demonstrate that type and status are recurring requirements.

However, the following distinctions matter:

- “Invoice,” “delivery note,” “contract,” and “inspection report” are domain-specific document types, rather than automatically being core classes.
- Status values such as `draft`, `issued`, `cancelled`, `obsolete`, `superseded`, `accepted`, or `rejected` often depend on workflows or domains.
- ADMS `status` describes status within a particular workflow context and should not generally be interpreted as a universal legal status.

Recommendation:

- A small document type vocabulary is implemented for the MVP.
- Document types are treated as controlled concepts, rather than fixed subclasses of the Document Core.
- A small document status vocabulary is implemented for the MVP.
- Status describes the state of a document, for example draft, issued, superseded, withdrawn, or expired.
- Workflow states such as “under review,” “awaiting approval,” or “assigned to the legal department” should not be included in the Document Core.
- No domain-specific allowlist should be included in the core.

### 6.5 Version, Revision, Derivation, and Replacement

Dublin Core provides `hasVersion`, `isVersionOf`, `replaces`, `isReplacedBy`, and `source`. ADMS provides `prev`, `next`, `last`, and `versionNotes`. DCAT 3 adds versioning relationships. PROV-O models derivation and revisions through `wasDerivedFrom` and qualified relationships.

For Construct-X, the following points matter:

- Document versions are not the same as ontology versions.
- A file in another format is not necessarily a new domain-level version.
- A corrected or replacement version should not be inferred solely from its filename.
- An exact version may be crucial for documents used as evidence.

Recommendation:

- A simple version indicator can initially be provided as metadata.
- Structural versioning relationships should preferably reuse existing DCT, ADMS, DCAT, or PROV relationships.
- Before introducing local versioning logic, it must be clarified whether document versioning differs from versioning other resources in the network.

## 7. Identifiers and Numbers

Dublin Core `identifier`, ADMS `Identifier`, SKOS `notation`, and UBL `ID`/`UUID` show that documents frequently have multiple identifiers:

- domain-specific document number,
- UUID,
- external register or archive identifier,
- DOI, URN, ISBN, or similar publication identifier,
- internal system ID.

The existing Construct-X identifier model is authoritative here:

A resource references an `adms:Identifier` through `adms:identifier`. The identifier contains:

- `skos:notation "value"^^identificationScheme`,
- `adms:schemaAgency "Issuer of the identification scheme"`.

Recommendation:

1. Do not introduce local properties such as `invoiceNumber`, `documentNumber`, `uuidValue`, `doi`, or `archiveId` in the Document Core.
2. Model document identifiers through ADMS.
3. Maintain identification schemes in a reference vocabulary if they are reused across Construct-X.
4. Do not introduce technical integrity verification through the Document Core identifier model.

## 8. Actors: Creator, Issuer, Publisher, Sender, Receiver

The sources use many actor concepts:

- Dublin Core: `creator`, `contributor`, `publisher`, `rightsHolder`.
- Schema.org: `author`, `creator`, `editor`, `publisher`, `provider`, `accountablePerson`, `copyrightHolder`.
- UBL: `IssuerParty`, `SenderParty`, `ReceiverParty`.
- VC: `issuer`, `holder`, `verifier`, `credentialSubject`.
- PROV-O: `wasAttributedTo`, `wasGeneratedBy`, `wasAssociatedWith`.

These concepts are not interchangeable. An author is not automatically the issuer, sender, publisher, legally responsible party, or technical uploader.

For Construct-X, this means:

- Actor roles associated with documents should most likely be modeled through `core/participation`.
- The Document Core should not introduce separate person or organization properties for every possible actor type.
- A future profile may require a particular document type to have exactly one issuer or sender.
- Provenance roles should be compared with PROV-O when the focus is generation, derivation, or processing.

Decision for the next modeling phase:

- Issuer, sender, recipient, author, and publisher are not introduced as dedicated direct Document Core properties.
- These roles are modeled through the Participation pattern: an Agent plays a controlled role in the context of a document or document reference.
- PROV-O remains responsible for actual provenance cases, namely generation, derivation, revision, or processing.

Examples:

| Context | Participation |
| --- | --- |
| Invoice 4711 | Organization A as `issuer`; Organization B as `recipient` |
| Structural drawing version 3 | Person X as `author`; Organization Y as `publisher`; Organization Z as `recipient` |
| Building permit | Authority A as `issuer`; Applicant B as `recipient` |

For a PDF file generated from dataset Y, a PROV-O profile can describe:

- the document `wasGeneratedBy` export run X,
- the document `wasDerivedFrom` dataset Y.

## 9. Evidence, Credentials, and Supporting Documentation

SEMIC CCCEV describes Evidence as proof that a Requirement is satisfied. CPSV-AP uses Evidence in the context of public services and distinguishes Evidence from related documentation.

W3C Verifiable Credentials models verifiable claims with an issuer, credential subject, validity, status, schema, and optional evidence. W3C Data Integrity describes cryptographic proofs for these and similar documents.

The following distinctions are important for the module boundary:

- Not every document is Evidence.
- Not every Evidence resource is a document; it may also be a dataset, register entry, artifact, or structured response.
- A credential is not simply an attachment, but a structure of claims that can be signed and verified.
- Identity evidence requires a subject, issuer, validity, status, and trust decision.

Recommendation:

- The Document Core may reference documents used as evidence.
- The semantics of “demonstrates compliance with Requirement X” belong in an Evidence/Requirement profile or a future specialized module, rather than the general Document Core.
- `core/person` and `core/organization` should reference external evidence resources rather than duplicate evidence as document fields.

## 10. Signatures, Seals, and Integrity Evidence

eIDAS regulates electronic signatures, electronic seals, electronic timestamps, electronic documents, electronic delivery services, and website certificates, among other matters. ETSI ESI provides corresponding technical standards and profiles.

W3C Data Integrity describes proofs for verifiable data. DID Core describes verification methods and controlled identifier documents.

The central distinctions for Construct-X are:

- A digital signature demonstrates control over a key and integrity with respect to the signed content.
- A qualified seal or qualified signature has jurisdiction-specific significance and requires trust-list/certificate context.
- A simple link to a signed PDF file is not a complete signature model.

Recommendation:

- Do not include signature, seal, timestamp, or trust-list details in the initial Document Core.
- Introduce a neutral extension point for signature/proof resources only once the specific trust scope has been clarified.

## 11. Rights, Licenses, and Access

Dublin Core and Schema.org provide simple license and rights information. ODRL is a considerably more powerful model for machine-readable policies involving permissions, prohibitions, duties, assets, parties, and constraints.

For Construct-X:

- A license URI may be general metadata.
- Access control, confidentiality, redistribution rights, and terms of use are policy matters, rather than merely document metadata.
- ODRL is a suitable candidate for future profiles, but too extensive for the initial Document Core.

Recommendation:

- Do not introduce a dedicated rights/policy ontology within the Document Core.
- Include license information only if it is required across domains in the MVP.
- Do not attach access rights to documents as simple Boolean values.

## 12. References to Document Parts, XPath, Annotations, and Excerpts

UBL `DocumentReference` provides `XPath` to identify a location within a referenced document. The Web Annotation Data Model models bodies, targets, SpecificResources, selectors, and states. These allow comments or references to specific document regions to be described.

For Construct-X:

- A document excerpt is not the same as a document.
- An XPath, page range, byte range, or fragment identifier depends on the format.
- Annotations may be independent resources with a motivation, body, and target.

Recommendation:

- Do not introduce detailed excerpt or annotation modeling in the initial Document Core.
- Annotation properties in domain modules may suffice for simple source or mapping paths.
- If required by the domain, use Web Annotation as an alignment source later.

## 13. File Formats and Media Types

IANA is the authoritative source for media types. DCAT recommends `dcat:mediaType` when the type is defined by IANA, and `dcterms:format` for more general format information.

Recommendation:

1. Do not treat media types as arbitrary, uncontrolled semantics.
2. If only a single value is required, a literal containing an IANA value may suffice for the MVP.

## 14. Provisional Module Boundaries

| Area | Belongs in `core/document` | Does Not Belong in `core/document` |
| --- | --- | --- |
| Document core | General document or document-like information object | Invoice, delivery note, contract, or certificate semantics |
| Reference | Contextual document reference | Domain-specific mandatory references |
| Distribution | Specific file or technical delivery form | Complete storage, DMS, or archive model |
| Metadata | Title, description, language, and creation/issue/modification/validity information as candidates | Workflow status without profile context |
| Identifier | Reuse of ADMS/SKOS | Local number properties for each document type |
| Actors | Reference to the Agent/Participation pattern | Dedicated properties for every actor role concept |
| Evidence | A document may serve as or be referenced as an evidence resource | Evidence/Requirement/Credential semantics |
| Signature | Possible extension point | eIDAS/ETSI/Data Integrity model within the core |
| Rights | Possible license reference | ODRL policy or access control within the core |
| Formats | Media type/distribution integration | Dedicated list of all file formats |

## 15. Core Terms as the Implemented Analysis Outcome

The following list shows how the research findings were implemented in version `0.1.0`.

### 15.1 Implemented Classes

| Term | Meaning | Rationale |
| --- | --- | --- |
| `Document` | Dedicated Construct-X class for a document-like information object | DCT, Schema.org, FOAF, and UBL serve only as alignment and comparative sources |
| `DocumentReference` | Context resource referencing a document or external document resource | UBL shows that references can carry their own metadata |
| `DocumentDistribution` | Specific file, download, or technical delivery form of a document | DCAT-oriented separation of document content and technical distribution |
| `DocumentType` | Controlled document type | Small MVP vocabulary implemented |
| `DocumentStatus` | Controlled state of a document | Small MVP vocabulary implemented |

Optional future additions:

- domain-specific document type extensions,
- domain-specific status extensions,
- provenance, signature, credential, or rights profiles.

### 15.2 Implemented Relationships

| Term | Meaning | Notes |
| --- | --- | --- |
| `hasDocumentReference` | Links any context resource to a document reference | Should have no restrictive RDFS domain |
| `referencesDocument` | Links a document reference to a described document | Only when the target is modeled in the graph |
| `hasDistribution` | Links a document or document reference to a specific distribution | DCAT-oriented separation |
| `dcterms:references`, `dcat:accessURL`, `dcat:downloadURL` | Reference an external document resource or technical access point | Direct reuse of established properties |
| `documentType` | References a controlled document type | SKOS concept rather than class |
| `documentStatus` | References a controlled status value | The core provides a small value set; profiles may extend it |

### 15.3 Implemented Metadata

| Candidate | Meaning | Source |
| --- | --- | --- |
| Title | Display name or domain-specific document title | DCT `title`, Schema.org `name` |
| Description | Free-text description | DCT `description`, UBL `DocumentDescription` |
| Language | Language of the content | DCT `language`, Schema.org `inLanguage`, UBL `LanguageID` |
| Issue date | Formal issuance in the domain context | DCT `issued`, UBL `IssueDate` |
| Issue time | Time of formal issuance | UBL `IssueTime` |
| Modification date | Last known modification | DCT `modified`, Schema.org `dateModified` |
| Version | Document version or edition designation | UBL `VersionID`, DCAT/ADMS/DCT |
| Validity | Period during which the document or evidence is valid | DCT `valid`, UBL `ValidityPeriod`, VC |
| Filename | Name of a specific file | UBL `FileName` |
| Media type | Technical format | IANA, DCAT, Schema.org |

## 16. Excluded from the Initial Document Core

Despite their presence in the sources, the following topics should not be included directly in the initial core:

- signature and seal classes,
- electronic timestamps,
- trust-list and certificate validation,
- credential, evidence, and requirement models,
- archiving, file plans, retention, and records management,
- access control, role-based rights, and policy evaluation,
- invoice, delivery note, contract, certificate, and report classes,
- workflow status and approvals,
- full-text content, OCR, extraction, and page/section models,
- file storage locations, uploads, repository-specific or DMS-specific concepts,
- format-specific structures such as PDF pages, XML XPath, or IFC references.

## 17. Implications for Profiles and Validation

Mandatory fields should not be hidden in the general T-Box. Several layers are more appropriate for the document domain:

1. **Document Core:** very general structure and datatype consistency.
2. **Document Reference Core Shapes:** check that a document reference points to at least a described document or an external resource.
3. **Distribution Shapes:** check that file, URI, and format information is consistent.
4. **Document Type Profiles:** invoices, delivery notes, contracts, certificates, inspection reports, etc. define their own mandatory information.
5. **Participation Profiles:** issuer, sender, recipient, author, publisher, and similar roles may become mandatory depending on the document type.
6. **Trust/Evidence Profiles:** signature, credential, evidence status, and external verification.

The general ontology should therefore avoid asserting domain-specific cardinalities such as “every document has exactly one issuer” or “every document has exactly one file.”

## 18. Consolidated and Implemented Decisions

The following points form the basis of the implemented T-Box and Core Shapes:

1. The Document Core requires a dedicated, narrow core rather than a large document management model.
2. Document, document reference, and distribution are modeled separately.
3. A document reference is a separate resource because it can carry contextual metadata.
4. Domain-specific document types do not belong in the core as classes.
5. Document types and status values are implemented as small controlled MVP vocabularies and may be profiled later.
6. Identifiers follow the shared ADMS/SKOS contract from `core/identifier`.
7. Actor roles such as issuer, sender, recipient, author, publisher, or rights holder must not be conflated.
8. Actor relationships are modeled through `core/participation`; PROV-O is relevant to generation, derivation, revision, and processing.
9. Distributions provide connections for URI, filename, and media type, but no storage model.
10. IANA is the preferred source for media types.
11. Validity, expiry, and availability are distinct statements.
12. Evidence and Credential must not be equated with Document.
13. Signatures, seals, and eIDAS/ETSI trust do not belong in the initial Document Core.
14. Rights and access control do not belong in the initial Document Core; ODRL remains a future profile or alignment topic.
15. References to document parts and annotations remain outside the MVP.

## 19. Implemented Modeling Decisions

The T-Box and Core Shapes implement the following domain guidelines:

1. Construct-X introduces its own class `Document`. External classes such as `schema:DigitalDocument` or `foaf:Document` are alignment targets, rather than the local core concept.
2. Files and technical delivery forms are separated as distributions following the DCAT approach. `Attachment` remains only a UBL comparison term.
3. The most important date concepts are implemented as optional elements: created, issued, modified, and valid.
4. A small document type vocabulary is implemented for the MVP.
5. A small document status vocabulary is implemented for the MVP. This refers to document-related states such as draft, issued, superseded, withdrawn, or expired, rather than workflow states.
6. Issuer, sender, recipient, author, and publisher are modeled through `core/participation`.
7. PROV-O is used only for actual provenance cases: generation, derivation, revision, or processing of a document.
8. UBL is used only as a comparative source. Neither a dependency nor a UBL mapping is currently planned.

## 20. Overall Assessment

A robust `core/document` component should not emerge from a long list of possible document attributes. Instead, the sources reveal several clearly separated layers:

| Layer | Content |
| --- | --- |
| Domain context | Context in which a document is referenced |
| Document reference | Contextual reference |
| Reference target | Document or external resource |
| Technical representation | Distribution/file |
| Descriptive information | Metadata, identifiers, type, status, language, version |

Additional, separate layers build on this:

- participating actors and roles,
- provenance and derivation,
- evidence and credentials,
- signatures and trust services,
- rights and access policies,
- domain-specific document types and profiles.

The most important architectural decision for the next phase is therefore:

> Document Core describes document-like resources and references, but not the domain-specific meaning, legal evidential value, signature validity, or process role of a document.

This keeps the module small enough for the core while allowing integration with future profiles.

## 21. Illustrative Mapping Example

> DCAT provides the pattern for technical distributions, DCTERMS provides general metadata, and UBL provides domain-specific reference scenarios. Construct-X combines these contributions without copying any source model in full.****
