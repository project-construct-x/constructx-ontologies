# Changelog

## 0.3.0 - 2026-11-19

- Rename `participant`, `role`, and `context` to `hasParticipant`, `hasRole`, and `hasContext`. Migrate these predicates in RDF data and queries. `hasParticipation` is now the inverse of `hasContext`.

## 0.2.0 - 2026-10-07

- Added the optional context-side `hasParticipation` property as `owl:inverseOf context`; no role-specific Core properties were introduced.
- Added PART-060 and PART-061 to check valid Participation IRIs and matching explicit context back-references.
- Kept the Participation contract backward compatible; existing data without outgoing links remains valid.
- Updated the concept, documentation package, Turtle example, and Mermaid diagrams; the role vocabulary remains at 0.1.0.

## Unreleased - 2026-09-03

- Added `docs/09_confluence-overview.md` as the sole publication source for the concise Confluence module page.
- Standardized the documentation package and added accessible examples.

## 0.1.0 - 2026-08-27

- Added the initial Participation T-Box for qualified agent-role assignments.
- Defined agent, role, and open domain context as the three core relationships.
- Added optional start and end dates for the assignment's validity.
- Implemented the minimal role vocabulary and Core SHACL profile separately from the T-Box.
- Added positive and negative SHACL cases, including concrete Person and Organization participants.
