# Construct-X Identifier Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module provides the shared ADMS/SKOS contract for domain identifiers
without introducing a parallel Construct-X Identifier class.

## 2. Accessible Example

> The commercial register number "HRB 1234" is stored as a dedicated
> identifier resource. This allows the value, identifier scheme, and issuing
> agency to be described together.

```text
Organization -> Identifier -> HRB 1234
```

## 3. Model Scope

Each identifier is an `adms:Identifier` with exactly one `skos:notation`.
`adms:schemaAgency` is optional. Domain modules decide which identifiers they
require.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology metadata: `ontology/conx-id.ttl`
- Core Shapes: `shapes/conx-id-core.shacl.ttl`
- Valid examples: `tests/valid/`
- Invalid examples: `tests/invalid/`
