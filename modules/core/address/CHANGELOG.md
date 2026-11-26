# Changelog

## 0.3.0 - 2026-11-26

- Migrate predicates on existing triples: `assignedAddress` to `hasAssignedAddress`, `locationRole` to `hasLocationRole`, and `broaderAdministrativeTerritory` to `hasBroaderAdministrativeTerritory`. Keep subjects and objects unchanged. This also applies to administrative-area reference data.
- Move `departmentName`, `attentionOf` and `careOf` to the optional `https://www.construct-x.org/ontology/delivery-instructions#` namespace; keep subjects, literal values and language tags. Only the extension defines and validates these delivery hints.
- `hasGeoReference` remains open-range. Address-only, geographic-reference-only and combined assignments remain valid.

## 0.2.0 - 2026-11-19

- Replaced `AddressAssignment`, `hasAddressAssignment`, `AddressRole` and `addressRole` with `LocationAssignment`, `hasLocationAssignment`, `LocationRole` and `locationRole`. Existing role individuals retain their IRIs.
- Replace each `Address → hasGeographicPosition → position` edge with `LocationAssignment → hasGeoReference → position`; the geographic reference can use any external model. For a shared address, identify the intended assignment before moving the point.
- OWL and Core SHACL require at least one role and an address or a geolocation (or both), with at most one of each payload.

## Unreleased

- Added `docs/09_confluence-overview.md` as the sole publication source for the concise Confluence module page.
- Standardized the documentation package and added accessible examples.
- Aligned Address Shapes and all related reference vocabularies with the network-wide Shape-Set, SemVer graph and hash-namespace conventions.
- Added the versioned Identifier Scheme Datatype vocabulary used by the ISO reference datasets.
- Replaced the ontology creator organization with structured creator metadata for Sven Zentgraf, including email, ORCID and affiliation.
- Added and documented the separate Address Roles SKOS reference vocabulary in `datasets/reference/vocabularies/address-roles`.
- Added ISO 3166-1 country and German ISO 3166-2 state reference datasets with ADMS identifiers.
- Added administrative-territory documentation and an executable Bochum address example.
- Added Address Core SHACL Shapes for general cardinality, class, node-kind and datatype validation.
- Mirrored all general maximum cardinalities as OWL restrictions in the Address T-Box.
- Added valid and invalid SHACL fixtures and automated OWL/SHACL parity tests.
- Added a complete beginner-friendly and technically detailed Confluence documentation page.

## 0.1.0 - 2026-08-13

- Added the initial Address Ontology T-Box with six classes, seven object properties and seventeen datatype properties.
- Added structured address components for streets, buildings, internal delivery points, localities, postal codes, post office boxes and plot identifiers.
- Added contextual address assignments with one address and one or more externally maintained address roles.
- Added referenceable countries and administrative areas without embedding reference-data individuals in the T-Box.
- Added `hasGeographicPosition` as an open extension point without defining coordinates or an external range.
- Excluded formatted postal addresses and unstructured address lines from the authoritative model.
