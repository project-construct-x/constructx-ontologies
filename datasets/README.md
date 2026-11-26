# Core Reference Datasets

Reference data is maintained separately from ontology T-Boxes and SHACL shapes.
This distribution includes the vocabularies and administrative datasets used
or documented by the Core modules.

- [Construct-X ISO 3166-1 Countries](reference/administrative-territories/iso-3166-1-countries/README.md) — 0.1.0
- [Construct-X German States according to ISO 3166-2](reference/administrative-territories/iso-3166-2-de/README.md) — 0.2.0
- [Construct-X NUTS 2 Regions](reference/administrative-territories/nuts-2/README.md) — 0.2.0
- [Construct-X Address Roles](reference/vocabularies/address-roles/README.md) — 0.3.0
- [Construct-X Contact Channels](reference/vocabularies/contact-channel/README.md) — 0.1.1
- [Construct-X Contact Platforms](reference/vocabularies/contact-platform/README.md) — 0.1.0
- [Construct-X Contact Purposes](reference/vocabularies/contact-purpose/README.md) — 0.1.0
- [Construct-X Contact Usage](reference/vocabularies/contact-usage/README.md) — 0.1.0
- [Construct-X Document Statuses](reference/vocabularies/document-status/README.md) — 0.1.0
- [Construct-X Document Types](reference/vocabularies/document-type/README.md) — 0.1.0
- [Construct-X Gender](reference/vocabularies/gender/README.md) — 0.1.0
- [Construct-X Human Sex](reference/vocabularies/human-sex/README.md) — 0.1.0
- [Construct-X Identifier Scheme Datatypes](reference/vocabularies/identifier-scheme/README.md) — 0.2.0
- [Construct-X Participation Roles](reference/vocabularies/participation-role/README.md) — 0.1.0
- [Construct-X Status kinds](reference/vocabularies/status-kind/README.md) — 0.1.0
- [Construct-X Status reasons](reference/vocabularies/status-reason/README.md) — 0.1.0
- [Construct-X Status values](reference/vocabularies/status-value/README.md) — 0.1.0

For example, Address can reference the country concept for Germany; its
identifier uses an ISO 3166 datatype from the shared identifier-scheme
vocabulary. NUTS 2 is an optional administrative reference vocabulary described
by Address, not a mandatory field on every address. Status uses separate
vocabularies for status kind, value and reason.

Each dataset records its version, source and license in `dataset.yaml`.
Intentional multilingual labels and source data are preserved.
