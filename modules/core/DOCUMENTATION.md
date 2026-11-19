# Documentation Standard for Core Modules

**Status:** Binding working convention  
**Version:** 2.1<br>
**As of:** 17 November 2026<br>
**Scope:** `modules/core/*`

## 1. Purpose

Every Core module uses the same documentation structure, regardless of its
technical or domain complexity. Subject-matter experts must be able to locate
precise rules quickly, while readers without RDF, OWL, or SHACL experience must
be able to understand the model through plain-language examples.

## 2. Required Documentation Package

Each Core module contains this documentation package:

```text
README.md
CHANGELOG.md
docs/00_index.md
docs/01_source-analysis.md
docs/02_scope-and-competency-questions.md
docs/03_concept-model.md
docs/04_module-boundaries.md
docs/05_term-catalog.md
docs/06_shacl-requirements.md
docs/07_core-shapes.md
docs/08_concept-diagram.md
docs/09_confluence-overview.md
```

If a topic is not applicable, the corresponding file remains present and
explains why. This applies, for example, to a module without its own Core Shape.

## 3. File Naming and Ordering

The two-digit prefix defines the reading order and is part of the file name.
The index always starts with `00_`; the common package ends with `09_`.

Module-specific supplementary documents continue with `10_`, `11_`, and so
on. Their order and purpose must be listed in `docs/00_index.md` and registered
in `module.yaml`.

Supporting files in subdirectories, generated HTML documentation, `README.md`,
and `CHANGELOG.md` are exempt from the numeric prefix. Examples include
`docs/diagrams/organization-concept-model.md` and `docs/organization.html`.

## 4. Document Header

Normative and currently maintained documents begin below the title with:

```text
**Status:** Implemented or confirmed
**Version:** 0.1.0
**As of:** 29 October 2026
**Scope:** `core/<module>`
```

Source analyses may additionally state a research cutoff date. Historical
working documents must be explicitly marked as supplementary and non-normative.

Confluence overviews use German metadata labels and values: `Status`, `Version`,
`Stand`, and `Geltungsbereich`. Module names, versions, and technical paths remain
unchanged.

## 5. Responsibilities of Each Document

| Document | Responsibility |
| --- | --- |
| `README.md` | Brief repository-level introduction |
| `docs/00_index.md` | Central navigation and current module status |
| `docs/01_source-analysis.md` | Sources, alternatives, and reasons for the selected approach |
| `docs/02_scope-and-competency-questions.md` | Scope, exclusions, and answerable questions |
| `docs/03_concept-model.md` | Domain model explained in accessible language |
| `docs/04_module-boundaries.md` | Responsibilities and dependencies |
| `docs/05_term-catalog.md` | Classes, properties, and controlled values |
| `docs/06_shacl-requirements.md` | Domain validation requirements |
| `docs/07_core-shapes.md` | Concise reference for the executable Shape Graph |
| `docs/08_concept-diagram.md` | Visual overview with a reading example |
| `docs/09_confluence-overview.md` | Publication source for the concise Confluence module page |

## 6. Accessible Examples

Each domain document contains at least one concrete situation or small data
example. An example starts with the domain statement and only then introduces
technical details.

Example:

> An organization has a billing address. The address contains the street and
> city; the role "billing address" belongs to the address assignment.

```text
Organization -> AddressAssignment -> Address
                       |
                       +-> Role: Billing address
```

Turtle examples should remain short and use only terms explained in the
surrounding text.

## 7. Language and Terminology

- Prose and headings in the detailed repository documentation, module indexes,
  READMEs, and changelogs are written in English.
- Every `docs/09_confluence-overview.md` is written in German, including its
  title, metadata labels, headings, explanations, and link labels. German is
  the agreed Confluence publication language for all Core modules. The module
  index identifies this document as the German publication source.
- Bilingual tables are retained where they document actual German and English
  vocabulary labels or validation messages. Their headings and surrounding
  explanations are in English. Ordinary explanatory prose is not duplicated
  in both languages.
- Language-tagged example values, quoted source labels, and proper names may
  retain their original language. Generic explanatory sample values use
  English in the detailed documentation.
- Classes, properties, prefixes, and public IRIs remain unchanged.
- The repository uses the term "Construct-X Core module".
- Chapters use consecutive numbering.
- File names use lowercase kebab case after the numeric prefix.

## 8. Maintenance

All documents are registered in `module.yaml` and linked from
`docs/00_index.md`. Changes to a T-Box or Core Shape are reflected in the
concept model, term catalog, SHACL documentation, and changelog at the same
time. Relative links must resolve within the repository.

## 9. Confluence Publication

The file `docs/09_confluence-overview.md` is the only publication source for
the concise Confluence page of a Core module. It summarizes the detailed
repository documents without introducing additional rules. The ontology and
Shape Graphs remain the normative machine-readable artifacts.

Each Confluence summary uses exactly these German chapter headings:

1. Zweck
2. Alltagsbeispiel
3. Umfang und Abgrenzung
4. Modellübersicht
5. Zentrale Klassen und Beziehungen
6. Validierung in Alltagssprache
7. Abhängigkeiten
8. Version, Status und Artefakte
9. Weiterführende Dokumentation

A change starts in the responsible detailed document and is then reflected in
the summary. The Confluence page is published from
`docs/09_confluence-overview.md` and is not maintained independently.
