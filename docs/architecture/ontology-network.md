<a id="ontologienetzwerk"></a>

# Core Ontology Network

This distribution contains the cross-domain Core ontologies of Construct-X.
Ontology axioms, SHACL shapes, instance examples and reference data remain
separate so they can be maintained and validated independently.

<a id="aufbau"></a>

## Structure

- `modules/core/` contains the ten Core modules listed in the [module index](../README.md).
- `datasets/reference/` contains their controlled vocabularies and administrative reference data.
- `profiles/construct-x/vso-isoprops/` contains the validation dependency used by Status conditions.
- `network/` records external references and validation dependencies.

<a id="aktuelle-module"></a>

## Current Modules

Address, Agent, Contact, Document, Identifier, Organization, Participation,
Person, Status and VSO are included. Their versions and registered artifacts
are listed in the [generated overview](../generated/module-overview.md).

For example, Person and Organization specialize Agent. Participation connects
an Agent to a role in a context. A Status can identify that Agent as its reporter
and use a VSO property assignment as a condition.

<a id="aktuelle-profile"></a>

## Supporting Validation Profile

The [VSO/ISOProps profile](../../profiles/construct-x/vso-isoprops/docs/00_index.md)
checks property definitions, literal datatypes and allowed units. The Status
validator composes these rules with the Status and VSO shapes, scoped to Status
conditions. It does not impose global ISOProps rules on unrelated assignments.

<a id="oeffentliche-iris"></a>

## Public IRIs

Public ontology IRIs follow `https://www.construct-x.org/ontology/{module}`.
Repository categories are not part of these IRIs. See the
[namespace concept](construct-x-namespace-konzept.md) for the full rules.

<a id="repository-dokumentation-und-confluence"></a>

## Repository Documentation and Confluence

Versioned technical decisions are maintained in the repository. German
Confluence overviews introduce each Core module using the same chapter
structure and accessible examples; they link to the detailed documentation.
