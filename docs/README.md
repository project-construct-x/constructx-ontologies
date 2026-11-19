# Construct-X Core Documentation

## Module Documentation

Use the documentation index for detailed explanations, rules and examples.
The German Confluence overview gives a short introduction for readers without
RDF or SHACL experience.

| Module | Detailed documentation | Confluence |
| --- | --- | --- |
| Address | [Documentation](../modules/core/address/docs/00_index.md) | [German overview](../modules/core/address/docs/09_confluence-overview.md) |
| Agent | [Documentation](../modules/core/agent/docs/00_index.md) | [German overview](../modules/core/agent/docs/09_confluence-overview.md) |
| Contact | [Documentation](../modules/core/contact/docs/00_index.md) | [German overview](../modules/core/contact/docs/09_confluence-overview.md) |
| Document | [Documentation](../modules/core/document/docs/00_index.md) | [German overview](../modules/core/document/docs/09_confluence-overview.md) |
| Identifier | [Documentation](../modules/core/identifier/docs/00_index.md) | [German overview](../modules/core/identifier/docs/09_confluence-overview.md) |
| Organization | [Documentation](../modules/core/organization/docs/00_index.md) | [German overview](../modules/core/organization/docs/09_confluence-overview.md) |
| Participation | [Documentation](../modules/core/participation/docs/00_index.md) | [German overview](../modules/core/participation/docs/09_confluence-overview.md) |
| Person | [Documentation](../modules/core/person/docs/00_index.md) | [German overview](../modules/core/person/docs/09_confluence-overview.md) |
| Status | [Documentation](../modules/core/status/docs/00_index.md) | [German overview](../modules/core/status/docs/09_confluence-overview.md) |
| VSO | [Documentation](../modules/core/vso/docs/00_index.md) | [German overview](../modules/core/vso/docs/09_confluence-overview.md) |

For example, start with Address to understand a postal address, then follow
Organization to see how that address is assigned to a company. Participation
explains the company's role in a context; Status explains changes over time.

The [Core documentation standard](../modules/core/DOCUMENTATION.md) defines the
shared numbered structure. HTML reference pages remain unnumbered.

## Architecture

- [Namespace and IRI concept](architecture/construct-x-namespace-konzept.md)
- [Core network](architecture/ontology-network.md)
- [Dependency rules](architecture/dependency-rules.md)
- [Identifier model](architecture/identifier-model.md)
- [Versioning](architecture/versioning.md)

## Supporting Data and Validation

- [Reference datasets](../datasets/README.md)
- [VSO/ISOProps validation profile](../profiles/construct-x/vso-isoprops/docs/00_index.md)
- [Dependency registry](../network/README.md)
- [Generated module overview](generated/module-overview.md)
- [Generated profile overview](generated/profile-overview.md)

## Development

- [Contributing](../CONTRIBUTING.md)
- [Contribution guide](development/contribution-guide.md)
- [Naming conventions](development/naming-conventions.md)
- [Documentation generation](development/documentation-generation.md)
- [Release process](development/release-process.md)

## Authority of the Artifacts

Markdown documentation explains the model. The registered Turtle ontologies
and SHACL shapes are its normative machine-readable artifacts.
