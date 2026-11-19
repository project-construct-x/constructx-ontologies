# Construct-X Status values

## 1. Purpose

This versioned SKOS vocabulary supplies initial status values for the
[Status Core module](../../../../modules/core/status/docs/00_index.md).
It contains individuals of `conx-status:StatusValue`, not additional ontology classes.

## 2. Terms

| Term | Code | English label | German label |
| --- | --- | --- | --- |
| `InProgress` | `in-progress` | In progress | In Bearbeitung |
| `Shipped` | `shipped` | Shipped | Versendet |
| `Delivered` | `delivered` | Delivered | Geliefert |
| `NotChecked` | `not-checked` | Not checked | Nicht geprüft |
| `Passed` | `passed` | Passed | Bestanden |
| `Failed` | `failed` | Failed | Nicht bestanden |

## 3. Example and compatibility

A delivery can have transport status Shipped and temperature inspection Failed
at the same time. The kind declares its allowed values explicitly.
Reasons remain open: a typed reason may be used without a kind-to-reason link.


## 4. Publication contract

Our terms have one nonempty code, at least one preferred label and definition,
and at least one scheme membership. Preferred labels are unique per language.
This release supplies English and German labels and definitions. Alternative
labels and scope notes are optional. Codes are unique within a scheme.
These publication requirements do not impose our metadata policy on external concepts.

## 5. Version and validation

Version: **0.1.0**, status: **draft**. Stable graph: `https://www.construct-x.org/vocab/status-value`.
Release graph: `https://www.construct-x.org/vocab/status-value/0.1.0`. Term IRIs retain their identity across
compatible releases. See [dataset.yaml](dataset.yaml) and [CHANGELOG.md](CHANGELOG.md).
Validate with the Status Core shapes and the pinned reference graphs;
see the module's [validation guide](../../../../modules/core/status/docs/07_core-shapes.md).
