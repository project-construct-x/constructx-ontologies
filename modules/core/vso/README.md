# Construct-X VSO Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The Value Semantics Ontology describes how a property definition and a
concrete value are assigned to a resource.

## 2. Accessible Example

> A wall has the property "Height". Its concrete property assignment carries
> the value 2.80 and references the unit metre.

```text
Wall -> AssignedProperty "Height" -> PropertyState -> 2.80 m
```

## 3. Model Scope

The Core contains property assignment, property reference, state, value, and
an optional unit. Domain value types and ISOProps rules belong in profiles.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-vso.ttl`
- Core Shapes: `shapes/conx-vso-core.shacl.ttl`
- Examples: `examples/measured-property.ttl` and `examples/text-property.ttl`
- Tests: `tests/valid/` and `tests/invalid/`
