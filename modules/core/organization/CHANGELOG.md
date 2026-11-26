# Changelog

## Core Shapes 0.3.0 - 2026-11-26

- Legal addresses validate `hasAssignedAddress` and `hasLocationRole` on the referenced assignment. The organization T-Box remains at 0.1.0.

## Core shapes 0.2.0 - 2026-11-19

- A legal address requires a `LocationAssignment` with `LegalAddressRole` and one typed `assignedAddress`.

## Unreleased - 2026-09-03

- Added `docs/09_confluence-overview.md` as the sole publication source for the concise Confluence module page.
- Standardized the documentation package and added accessible examples.

## 0.1.0 - 2026-08-27

- Implemented the initial Organization T-Box with `Organization`, `LegalEntity`, `OrganizationalUnit`, `Membership`, and `LegalRepresentation`.
- Modeled names, legal form, registration date, activity, hierarchy, membership, and legal representation.
- Reused the existing Agent, Person, Address, Contact, and Identifier Core contracts.
- Implemented Organization Core Shapes with 36 stable bilingual validation codes.
- Added valid and invalid integration graphs and automated OWL and PySHACL tests.
