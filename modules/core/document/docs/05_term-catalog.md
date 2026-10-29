# Term Catalog for the Document Core Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`  
**Implementation status:** T-Box, reference vocabularies, and Core Shapes implemented

## 1. Purpose

This catalog describes the local terms of Document T-Box 0.1.0 and the associated reference vocabularies. The stated cardinalities are checked by the Core Shape and are not strict OWL restrictions.

## 2. Namespaces

### Document Ontology

```text
Ontology IRI: https://www.construct-x.org/ontology/document
Version IRI:  https://www.construct-x.org/ontology/document/0.1.0
Namespace:    https://www.construct-x.org/ontology/document#
Prefix:       conx-doc
```

### Document Type Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/document-type
Version IRI:    https://www.construct-x.org/vocab/document-type/0.1.0
Namespace:      https://www.construct-x.org/vocab/document-type#
Prefix:         document-type
```

### Document Status Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/document-status
Version IRI:    https://www.construct-x.org/vocab/document-status/0.1.0
Namespace:      https://www.construct-x.org/vocab/document-status#
Prefix:         document-status
```

## 3. Classes

### 3.1 `conx-doc:Document`

| Item | Specification |
| --- | --- |
| Definition | Document-like information object, independent of a specific file |
| Module | `core/document` |
| Usage | Invoices, contracts, certificates, reports, drawings, and comparable document-like resources |
| Boundary | Not a file, folder, DMS record, or credential model |
| External sources | Dublin Core, Schema.org `DigitalDocument`, FOAF `Document` as alignment sources |

### 3.2 `conx-doc:DocumentReference`

| Item | Specification |
| --- | --- |
| Definition | Contextual reference to a document, external document resource, or distribution |
| Module | `core/document` |
| Usage | Allows reference metadata without directly coupling the domain context to a file |
| Boundary | Not a domain-specific mandatory reference or UBL mapping |
| External sources | UBL `DocumentReference` as a comparative source |

### 3.3 `conx-doc:DocumentDistribution`

| Item | Specification |
| --- | --- |
| Definition | Specific technical delivery form or manifestation of a document |
| Module | `core/document` |
| Usage | PDF file, XML file, download link, or other retrievable representation |
| Boundary | Not a storage, upload, archive, or repository model |
| External sources | DCAT `Distribution` as the primary alignment source |

### 3.4 `conx-doc:DocumentType`

| Item | Specification |
| --- | --- |
| Definition | Controlled type of a document |
| Module | T-Box class in `core/document`, values in the SKOS vocabulary |
| Usage | Cross-domain initial values for profiles and data validation |
| Boundary | Document types are not modeled as local subclasses of `Document` |
| External sources | SKOS, Dublin Core `type`, UBL `DocumentTypeCode` for comparison |

### 3.5 `conx-doc:DocumentStatus`

| Item | Specification |
| --- | --- |
| Definition | Controlled document-related state |
| Module | T-Box class in `core/document`, values in the SKOS vocabulary |
| Usage | Draft, issued, superseded, withdrawn, expired, or archived |
| Boundary | No workflow states such as “under review” or “awaiting approval” |
| External sources | SKOS, ADMS `status`, Schema.org `creativeWorkStatus`, UBL `DocumentStatusCode` for comparison |

## 4. Object Properties

### 4.1 `conx-doc:hasDocumentReference`

| Item | Specification |
| --- | --- |
| Definition | Links any domain context resource to a document reference |
| Domain | No restrictive `rdfs:domain` |
| Range | `conx-doc:DocumentReference` |
| Cardinality | `0..n` |
| Note | Profiles may require mandatory references for particular context classes |

### 4.2 `conx-doc:referencesDocument`

| Item | Specification |
| --- | --- |
| Definition | Links a document reference to a document modeled in the graph |
| Domain | `conx-doc:DocumentReference` |
| Range | `conx-doc:Document` |
| Cardinality | `0..1`, checked in the Core Shape |
| Note | External documents may alternatively be described through URI/distribution references |

### 4.3 `conx-doc:hasDistribution`

| Item | Specification |
| --- | --- |
| Definition | Links a document or document reference to a technical distribution |
| Domain | No restrictive domain or union domain in the open T-Box |
| Range | `conx-doc:DocumentDistribution` |
| Cardinality | `0..n` |
| External source | DCAT `distribution` as an alignment source |

### 4.4 `conx-doc:documentType`

| Item | Specification |
| --- | --- |
| Definition | Assigns a controlled document type to a document or document reference |
| Domain | No restrictive domain; conceptually `Document`/`DocumentReference` |
| Range | `conx-doc:DocumentType` |
| Cardinality | `0..1`, checked in the Core Shape |
| Note | Profiles may impose stricter mandatory requirements |

### 4.5 `conx-doc:documentStatus`

| Item | Specification |
| --- | --- |
| Definition | Assigns a controlled document-related status to a document |
| Domain | Conceptually `conx-doc:Document` |
| Range | `conx-doc:DocumentStatus` |
| Cardinality | `0..1`, checked in the Core Shape |
| Note | Workflow status remains outside the Document Core |

## 5. Datatype Properties and External Properties

General document metadata is defined locally and aligned with external concepts. Technical DCAT properties are used directly.

| Property | Meaning | Range | Alignment or Reuse |
| --- | --- | --- | --- |
| `conx-doc:title` | Display name or domain-specific title | `xsd:string` or `rdf:langString` | `dcterms:title`, `schema:name` |
| `conx-doc:description` | Free-text description | `xsd:string` or `rdf:langString` | `dcterms:description`, `schema:description` |
| `conx-doc:language` | Language of the content | `xsd:string` | `dcterms:language`, `schema:inLanguage` |
| `conx-doc:version` | Document version or edition designation | `xsd:string` | `schema:version` |
| `conx-doc:created` | Creation date or time | `xsd:date` or `xsd:dateTime` | `dcterms:created`, `schema:dateCreated` |
| `conx-doc:issued` | Formal issue date or time in the domain context | `xsd:date` or `xsd:dateTime` | `dcterms:issued` |
| `conx-doc:modified` | Last known modification | `xsd:date` or `xsd:dateTime` | `dcterms:modified`, `schema:dateModified` |
| `conx-doc:validFrom` | Beginning of domain-specific validity | `xsd:date` or `xsd:dateTime` | `schema:validFrom`, `dcterms:valid` |
| `conx-doc:validUntil` | End of domain-specific validity | `xsd:date` or `xsd:dateTime` | `schema:validThrough`, `dcterms:valid` |
| `conx-doc:fileName` | Name of a specific file | `xsd:string` | UBL `FileName` for comparison only |
| `dcat:accessURL` | General access address | IRI | Direct reuse |
| `dcat:downloadURL` | Direct download address | IRI | Direct reuse |
| `dcat:mediaType` | IANA-oriented media type | IRI | Direct reuse |

## 6. MVP Values

### 6.1 Document Types

Reference vocabulary 0.1.0 contains:

```text
document-type:contract
document-type:invoice
document-type:deliveryNote
document-type:certificate
document-type:report
document-type:plan
document-type:evidenceDocument
document-type:other
```

### 6.2 Document Status

Reference vocabulary 0.1.0 contains:

```text
document-status:draft
document-status:issued
document-status:superseded
document-status:withdrawn
document-status:expired
document-status:archived
```

## 7. Not Intended as Local Terms

- `issuer`, `sender`, `receiver`, `author`, or `publisher` as direct Document Core properties,
- `Attachment` as a local core class,
- UBL-specific classes or properties,
- workflow status,
- signature, seal, Credential, or Evidence classes,
- storage, repository, upload, or archive classes.

## 8. Illustrative Example

> An inspection report is described as a `Document`. The PDF file is a `DocumentDistribution`; a reference from a contract is a `DocumentReference`. This prevents every file from becoming a new document.