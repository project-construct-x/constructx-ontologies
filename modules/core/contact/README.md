# Construct-X Contact Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.2.0  
**As of:** 19 November 2026

## 1. Summary

The module describes contact points and concrete contact methods for persons,
organizations, and other contactable resources.

## 2. Accessible Example

> A company's accounting department can be reached by email and telephone for
> invoice questions. The contact point describes purpose and usage; the two
> contact methods contain the concrete values.

```text
Company -> ContactPoint "Accounting" -> Email
                                      -> Telephone
```

## 3. Model Scope

The Core separates `ContactPoint`, `ContactMethod`, channel, usage, purpose,
and platform. Postal contacts reference a LocationAssignment.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-contact.ttl`
- Core Shapes: `shapes/conx-contact-core.shacl.ttl`
- Examples and tests: `tests/valid/` and `tests/invalid/`
- Reference vocabularies: channel, usage, purpose, and platform
