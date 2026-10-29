# Construct-X Document Core Module

**Status:** Approved Confluence summary  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/document`

This document is the publication source for the concise Confluence module
page. It summarizes the detailed repository documentation and introduces no
new domain or technical rules.

## 1. Purpose

The Document module describes document-like information objects, their use in
a domain context, and their technical provision. It separates the document
itself from a contextual reference and from files or downloads.

## 2. Everyday Example

> A contract references an inspection report. The report is the document, its
> PDF and XML files are two distributions, and the place in the contract that
> points to it is a document reference.

A new file format therefore does not automatically create a new domain
document.

## 3. Scope and Boundaries

The module contains documents, contextual references, technical distributions,
general metadata, controlled document types and statuses, and structured
identifiers. It does not define actor-specific properties, signatures,
credentials, access rights, workflows, provenance, or storage systems.

## 4. Model Overview

```text
Domain context -> DocumentReference -> Document
                        |                 |
                        +-----------------+-> DocumentDistribution
                                                |
                                                +-> PDF, XML, or URL
```

`Document` identifies the content, `DocumentReference` explains the contextual
reference, and `DocumentDistribution` describes its technical availability.

## 5. Key Classes and Relationships

| Term | Plain-language meaning |
| --- | --- |
| `Document` | Document-like information object |
| `DocumentReference` | Contextual reference to a document |
| `DocumentDistribution` | Concrete file or technical provision |
| `DocumentType` | Controlled type such as contract or invoice |
| `DocumentStatus` | Controlled status such as draft or issued |
| `referencesDocument` | Links the reference to the document |
| `hasDistribution` | Links a document or reference to a distribution |

## 6. Validation in Plain Language

Documents, references, and distributions must be typed explicitly. A document
reference needs at least one target: a modeled document, an external reference,
or a distribution. Dates must be valid and consistent, and type and status must
come from the approved vocabularies.

> A document reference without a target is incomplete. A PDF distribution with
> a file name and download IRI may be valid, although the Core does not verify
> whether the file is available or signed.

## 7. Dependencies

The Core Shape imports the versioned contract from `core/identifier`. Document
types and statuses come from separate vocabularies. DCAT properties describe
technical distributions; Dublin Core, Schema.org, FOAF, and SKOS are reference
or alignment sources. Actor roles can be modeled through `core/participation`.

## 8. Version, Status, and Artifacts

| Property | Value |
| --- | --- |
| Repository status | Draft; domain-reviewed and implemented |
| Version | `0.1.0` |
| Ontology IRI | `https://www.construct-x.org/ontology/document` |
| Prefix | `conx-doc` |

- [Ontology](../ontology/conx-doc.ttl)
- [Core Shapes](../shapes/conx-doc-core.shacl.ttl)
- [HTML documentation](document.html)
- [Complete document example](../tests/valid/complete-document.ttl)
- [Changelog](../CHANGELOG.md)

## 9. Further Documentation

- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Source Analysis](01_source-analysis.md)
- [Conceptual Model](03_concept-model.md)
- [Module Boundaries](04_module-boundaries.md)
- [Term Catalog](05_term-catalog.md)
- [SHACL Requirements](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Concept Diagram](08_concept-diagram.md)
