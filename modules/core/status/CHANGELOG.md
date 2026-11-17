# Changelog

## 0.1.0 draft corrections — 2026-11-11

- Support recordedAt end-of-day notation (24:00:00) through portable SHACL-SPARQL checks, preserving input spellings, optionality, calendar validity and offset limits; cover rollovers and invalid variants in API, CLI and exported-package tests.
- Validate recordedAt lexical forms as well as the dateTime datatype; keep the field and its UTC offset optional, with source and exported-package regression coverage.
- Added Person and Organization reporter examples with optional Core ontology context, including source, standalone-bundle and actor-contract integration tests.
- Kept hasCurrentStatus optional, but require it to identify the uniquely latest known assignment per object and kind; recordedAt does not affect ordering.
- Added STATUS-064 for superseded selections and STATUS-065 for unresolved equal-time ties, including tests of the exported SHACL package.
- Reject malformed mapped literal values through the shared ISOProps profile.
- Check explicit predecessor order as well as timestamps when detecting skipped statuses.
- Limit referenceTime to microsecond precision; finer values are rejected instead of silently losing ordering information.
- Export a complete offline validation bundle with scoped shapes, ontology context, reference data and a standalone runner.
- Publish the assembled Status Core shape graph in repository builds and test the relocated package independently.
- Added regression cases for malformed values, equal instants, precision limits and missing bundle components.

## 0.1.0 — 2026-11-10

- Introduced StatusAssignment and three SKOS-based status concept classes.
- Required a business reference date and a clock time with explicit UTC offset.
- Added optional current-status navigation and immediate predecessor links.
- Added multiple open reasons and scoped reuse of VSO/ISOProps conditions.
- Published three kinds, six shared values and four reasons in separate vocabularies.
- Added executable SHACL contracts, offline validation, positive and negative tests.
- Added the numbered English documentation package and Confluence publication source.
- Kept the pre-existing question notes and all domain modules unchanged.
