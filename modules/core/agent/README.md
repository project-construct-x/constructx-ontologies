# Construct-X Agent Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module provides `conx-agent:Agent` as the common superclass for persons and
organizations.

## 2. Accessible Example

> A participation can be held by a person or an organization. Both are agents
> and can therefore be referenced through the same relationship.

```text
Participation -> Agent <- Person
                       <- Organization
```

## 3. Model Scope

The Core contains exactly one class and no properties of its own. Concrete
master data remains in Person, Organization, Contact, and Address.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-agent.ttl`
- Core Shapes: not required
- Domain specification: `docs/10_agent-specification.md`
- Tests: repository-wide Agent ontology tests
