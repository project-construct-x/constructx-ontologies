# Construct-X Participation Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026

## 1. Summary

The module describes a currently or historically valid role held by an agent
in a domain context.

## 2. Accessible Example

> Anna Miller participates in a construction project as an architect.
> Participation connects Anna, the "Architect" role, and the project.

```text
Participation -> Person
              -> Role: Architect
              -> Domain context
```

## 3. Model Scope

Each Participation has exactly one agent, role, and context. Start and end
dates are optional. Activities, permissions, and Membership remain outside the
module. `hasParticipation` optionally exposes participations from the context.
The properties still belong to the Participation instance, not to the
referenced resource.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-part.ttl`
- Core Shapes: `shapes/conx-part-core.shacl.ttl`
- Examples and tests: `tests/valid/` and `tests/invalid/`
- Reference vocabulary: general Participation roles
