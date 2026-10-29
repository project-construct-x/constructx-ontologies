# Construct-X Person Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module describes intrinsic core data of real natural persons.

## 2. Accessible Example

> Anna Miller is described as a person with her name and date of birth. Her
> telephone number belongs to a contact point, her company affiliation to a
> Membership, and her personnel number to an Identifier resource.

```text
Person -> ContactPoint
       -> Membership
       -> Identifier
```

## 3. Model Scope

The Core contains names, birth information, `sex`, `gender`, nationality,
identifiers, and an open link to identity evidence.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-person.ttl`
- Core Shapes: `shapes/conx-person-core.shacl.ttl`
- Examples and tests: `tests/valid/` and `tests/invalid/`
- Reference vocabularies: `human-sex` and `gender`
