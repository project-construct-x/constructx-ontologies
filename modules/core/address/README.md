# Construct-X Address Core Module

**Status:** Draft, domain-reviewed, and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026

## 1. Summary

The module describes structured addresses and their contextual assignment to
persons, organizations, or other resources.

## 2. Accessible Example

> An organization can use the same address as both a delivery address and a
> billing address. The address is stored once; its roles belong to the address
> assignment.

```text
Organization -> AddressAssignment -> Address
                     +-> Delivery address
                     +-> Billing address
```

## 3. Model Scope

The Core contains `Address`, `AddressAssignment`, `AddressRole`, and
administrative territories. Contact channels and coordinate models remain in
their responsible modules.

## 4. Documentation

The central entry point is the [documentation index](docs/00_index.md). The
[documentation standard](../DOCUMENTATION.md) defines the common structure for
all Core modules.

## 5. Technical Artifacts

- Ontology: `ontology/conx-addr.ttl`
- Core Shapes: `shapes/conx-addr-core.shacl.ttl`
- Examples: `examples/`
- Tests: `tests/valid/` and `tests/invalid/`
- Reference data: address roles and ISO and NUTS territories under `datasets/reference/`
