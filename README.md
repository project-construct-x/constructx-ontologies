# Construct-X Core Ontologies

This repository provides the reusable Core ontologies of Construct-X, their
documentation, examples, SHACL validation rules and reference data.

**Status:** Draft. Each module is versioned independently.

## Core Modules

| Module | Version | Purpose |
| --- | --- | --- |
| [Address](modules/core/address/README.md) | 0.2.0 | Structured addresses and location assignments with an address, a geographic reference, or both |
| [Agent](modules/core/agent/README.md) | 0.1.0 | Shared superclass for actors |
| [Contact](modules/core/contact/README.md) | 0.2.0 | Contact points and communication methods |
| [Document](modules/core/document/README.md) | 0.1.0 | Documents, references and technical distributions |
| [Identifier](modules/core/identifier/README.md) | 0.1.0 | Shared ADMS/SKOS identifier contract |
| [Organization](modules/core/organization/README.md) | 0.1.0 | Organizations, units, memberships and representation |
| [Participation](modules/core/participation/README.md) | 0.2.0 | Roles of agents in business contexts |
| [Person](modules/core/person/README.md) | 0.1.0 | Core data of natural persons |
| [Status](modules/core/status/README.md) | 0.1.0 | Timestamped status assignments, history and optional conditions |
| [VSO](modules/core/vso/README.md) | 0.1.0 | Property assignments, values and units |

Domain ontologies and optional alignments are outside this distribution.
The VSO/ISOProps validation profile is included because the Status validation
contract uses its rules for property-based conditions. It is a supporting
validation dependency, not an additional ontology module.

For example, an organization can have an Address, participate in a context in
a defined role, and report a Status. A condition on that status can refer to a
measured VSO property whose datatype and unit are checked against ISOProps.

## Repository Structure

```text
modules/core/       Core ontologies, shapes, documentation, examples and fixtures
datasets/reference/ Controlled vocabularies and administrative reference data
profiles/construct-x/vso-isoprops/  Supporting validation profile
docs/               Architecture, development guides and module navigation
network/            External references and validation dependencies
scripts/            Manual validation, build, import and documentation tools
tests/              Core and supporting-dependency checks
```

## Getting Started

Install Python 3.12 or later and [uv](https://docs.astral.sh/uv/), then run:

```bash
git clone https://github.com/project-construct-x/constructx-ontologies.git
cd constructx-ontologies
uv sync --locked
uv run python scripts/validate.py
uv run pytest
```

The GitHub Actions **Validate** workflow runs only when started manually through
**Actions → Validate → Run workflow**. Pushes and pull requests do not start it.
Documentation checks cover declared files, local links and technical consistency;
they do not enforce exact chapter titles, prose, language or chapter numbering.

To validate a Status example with all required local dependencies:

```bash
uv run python scripts/validate_status.py --data modules/core/status/examples/minimal-status.ttl
```

To build the distribution or export the standalone Status validation bundle:

```bash
uv run python scripts/build.py
uv run python scripts/status_bundle.py --output build/status-bundle
```

The general build recreates `dist/`. The Status bundle can be used independently
of this checkout; its README describes validation outside the repository.

## Documentation

Start at the [documentation index](docs/README.md). Each Core module uses
`docs/00_index.md` for navigation and `docs/09_confluence-overview.md` for its
German Confluence overview. Other maintained documentation is in English;
intentional bilingual labels and original source material are retained.

The [documentation standard](modules/core/DOCUMENTATION.md) describes the shared
structure. [Documentation generation](docs/development/documentation-generation.md)
explains the optional OntoLens HTML generator and its separate installation.

## Licenses

Code is licensed under Apache License 2.0; see [LICENSE](LICENSE).
Ontologies, documentation and other non-code content are licensed under
CC BY 4.0; see [LICENSE_non-code](LICENSE_non-code). Third-party source and
license exceptions are recorded in local metadata and [NOTICE.md](NOTICE.md).
