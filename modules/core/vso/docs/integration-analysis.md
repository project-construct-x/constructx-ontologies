# CX-VSO Integration Analysis

Source file: `modules/core/vso/ontology/conx-vso.ttl`

## Parsed Metadata

- Triple count: 73
- Ontology IRI: `https://www.construct-x.org/ontology/vso`
- Version IRI: `https://www.construct-x.org/ontology/vso/0.1.0`
- Version info: `0.1.0`
- Preferred namespace prefix: `conx-vso`
- Preferred namespace URI: `https://www.construct-x.org/ontology/vso#`
- Created: `2026-08-06`
- License: `https://creativecommons.org/licenses/by/4.0/`
- Publisher: `https://www.construct-x.org/id/organization/ecbe8336-94ab-5c11-8220-94f260963eb2/revision/1`

## Namespace Alignment

Previous technical identifiers found before this task:

- Ontology IRI: `https://www.construct-x.org/ontology/value-semantics`
- Namespace: `https://www.construct-x.org/ontology/value-semantics#`
- Version IRI: `https://www.construct-x.org/ontology/value-semantics/0.1.0`
- Repository path: `modules/core/value-semantics/ontology/conx-vso.ttl`

Applied namespace concept:

- Ontology IRI: `https://www.construct-x.org/ontology/vso`
- Namespace: `https://www.construct-x.org/ontology/vso#`
- Version IRI: `https://www.construct-x.org/ontology/vso/0.1.0`
- Repository path: `modules/core/vso/ontology/conx-vso.ttl`

The prefix `conx-vso` already matched the convention and was retained.

## Imports And External References

The ontology declares no `owl:imports`.

Referenced external terms:

- `opm:Property`
- `opm:PropertyState`
- `opm:hasPropertyState`
- `qudt:Unit`
- `schema:value`

Because no `owl:imports` are present, external ontology IRIs and tested versions remain `null` in `network/imports.lock.yaml`. The referenced namespaces are documented as `referenced-not-imported`.

## T-Box And A-Box Assessment

T-Box content found:

- OWL ontology header
- 2 OWL classes:
  - `conx-vso:AssignedProperty`
  - `conx-vso:PropertyState`
- 4 OWL object properties:
  - `conx-vso:hasProperty`
  - `conx-vso:hasPropertyReference`
  - `conx-vso:hasPropertyState`
  - `conx-vso:hasUsedUnit`
- 4 blank-node OWL restrictions
- Domain, range, subclass and subproperty axioms

Current cardinalities:

- exactly one `conx-vso:hasPropertyReference` per `AssignedProperty`,
- exactly one `conx-vso:hasPropertyState` per `AssignedProperty`,
- exactly one `schema:value` per `PropertyState`,
- at most one optional `conx-vso:hasUsedUnit` per `PropertyState`.

A-Box content found:

- No `owl:NamedIndividual` declarations
- No instance data for domain objects was identified

Metadata IRIs such as license and publisher are ontology metadata references, not domain A-Box examples.

## Follow-Up

The approved Core semantics are implemented in `shapes/conx-vso-core.shacl.ttl`, public examples and automated tests. ISOProps-specific constraints remain a separate future profile or alignment.

Before the first stable public release, confirm that `https://www.construct-x.org` is the permanent canonical Authority.


