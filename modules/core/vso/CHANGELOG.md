# Changelog

## Unreleased

- 2026-10-06: PropertyStateShape now selects only VSO states and VSO links,
  rather than arbitrary resources with `schema:value`. Quantities can therefore
  be validated alongside property states.

- Added `docs/09_confluence-overview.md` as the sole publication source for the concise Confluence module page.
- Migrated the documentation package to the shared Core structure and added accessible examples.
- Added and integrated the VSO 0.1.0 ontology.
- Confirmed the OPM subclass and subproperty alignments.
- Retained `schema:value` as the single value predicate.
- Changed every assignment to exactly one property state.
- Changed the used-unit cardinality from exactly one to optional, at most one.
- Added versioned VSO Core Shapes with stable validation codes.
- Added valid examples, focused invalid fixtures and automated tests.
- Reserved ISOProps-specific constraints for a separate profile or alignment.
