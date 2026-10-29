# Construct-X Document Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module separates a domain document, its contextual reference, and its
technical provision as a file.

## 2. Accessible Example

> A contract references an inspection report. The report is the document; its
> PDF and XML files are two distributions of the same document.

```text
Contract -> DocumentReference -> Document -> PDF
                                        +-> XML
```

## 3. Model Scope

The Core contains `Document`, `DocumentReference`, `DocumentDistribution`,
metadata, status, type, validity, and identifiers. Agent roles are modeled
through Participation.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-doc.ttl`
- Core Shapes: `shapes/conx-doc-core.shacl.ttl`
- Examples and tests: `tests/valid/` and `tests/invalid/`
- Reference vocabularies: document type and document status
