# Construct-X Organization Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module describes organizations, legal entities, internal organizational
units, memberships, and legal representations.

## 2. Accessible Example

> Example Construction Ltd. is a legal entity. It has an internal department;
> Anna Miller is a member and legally represents the company.

```text
LegalEntity -> OrganizationalUnit
Membership: Person -> Organization
LegalRepresentation: Person -> LegalEntity
```

## 3. Model Scope

The Core contains names, legal form, registration date, activity, hierarchies,
Membership, and LegalRepresentation. Contact, Address, and Identifier are used
from their responsible Core modules.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-org.ttl`
- Core Shapes: `shapes/conx-org-core.shacl.ttl`
- Examples and tests: `tests/valid/` and `tests/invalid/`
- Integrations: Agent, Person, Address, Contact, and Identifier
