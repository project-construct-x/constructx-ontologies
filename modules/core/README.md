# Core Modules

Core modules contain reusable ontologies that apply across domains. They form
shared foundations that can be used by multiple domain modules.

The common structure, required documents, and expectations for accessible
examples are defined in the [documentation standard](DOCUMENTATION.md).

Current Core modules:

- `vso`: Construct-X Value Semantics Ontology
- `address`: Construct-X Address Ontology
- `agent`: minimal common superclass for agents
- `identifier`: shared ADMS/SKOS contract for domain identifiers
- `person`: core data of real natural persons
- `contact`: contact points and communication channels
- `organization`: organizations, legal entities, organizational units, memberships, and legal representations
- `participation`: qualified roles of agents in domain contexts
- `document`: documents, contextual references, technical distributions, document types, and document statuses
- `status`: timestamped status assignments, reusable status vocabularies, optional history, and VSO/ISOProps conditions

Core modules must not import domain modules. External ontologies may only be
used when their imports, versions, and roles are documented transparently.
