# Construct-X Status Core Module

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Summary

The Construct-X Core module for timestamped status assignments, reusable status
vocabularies, optional history navigation and VSO/ISOProps conditions.
It follows the [Core documentation standard](../DOCUMENTATION.md).

## 2. Accessible Example

A delivery can be **Shipped** while its temperature inspection has **Failed**.
These are two independent status kinds. Each statement has its own date and
time with UTC offset. A temperature measurement can explain the inspection.

```text
Delivery -> Status assignment -> Transport status / Shipped
         -> Status assignment -> Temperature inspection / Failed
                                  -> VSO assignment -> Temperature / 8.0 °C
```

See the [minimal example](examples/minimal-status.ttl) and
[complete measurement example](examples/status-with-condition.ttl).
The [current status example](examples/current-status-selection.ttl) explains
why a late-recorded shipping report does not replace a newer delivery status.
The [reporting actor examples](examples/reporting-actors/README.md) show a
Person and an Organization using reportedBy, with the required Core context
and runnable validation commands.

## 3. Model Scope

Four classes: StatusAssignment, StatusKind, StatusValue and StatusReason.
Date, time, kind and value are mandatory; actor, recording time, reasons,
conditions and history navigation are optional. Reasons remain open.
When hasCurrentStatus is provided, it must identify the uniquely latest known
statement for that object and kind, using business time and explicit
predecessor order for equal instants. Recording time does not decide this.
Corrections, numeric intervals, workflow transitions and Document migration
are outside this release. No domain ontology is imported.

## 4. Documentation

Start with the [module index](docs/00_index.md), then the
[conceptual model](docs/03_concept-model.md) and
[Confluence overview](docs/09_confluence-overview.md).

## 5. Technical Artifacts

- [Manifest](module.yaml), [ontology](ontology/conx-status.ttl),
  [Core shapes](shapes/conx-status-core.shacl.ttl), [HTML catalog](docs/status.html).
- [Validation entry point](../../../scripts/validate_status.py), using locally
  pinned reference graphs and existing VSO/ISOProps rules.
- [Changelog](CHANGELOG.md); initial version 0.1.0 (draft).
- [Bundle exporter](../../../scripts/status_bundle.py): complete offline
  validation package; see [Core Shapes](docs/07_core-shapes.md) for usage.

From the repository root:

```console
python scripts/validate_status.py --data modules/core/status/examples/status-with-condition.ttl
```
