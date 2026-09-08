# Changelog

## Unreleased

- Core-only-Publikationspaket auf ISO-3166-Referenzdaten begrenzt und das abgelöste ausführliche Confluence-Bestandsdokument entfernt.
- Kompakte `docs/confluence-overview.md` als alleinige Veröffentlichungsquelle der Confluence-Modulseite ergänzt.
- Dokumentationspaket nach dem gemeinsamen Core-Standard vereinheitlicht und um verständliche Beispiele ergänzt.
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
