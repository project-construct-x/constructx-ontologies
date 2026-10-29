# Domain Specification of the Agent Core

**Status:** Implemented specification of T-Box 0.1.0  
**As of:** 27 August 2026

## 1. Purpose

`core/agent` provides a minimal common superclass for actors in the Construct-X ontology network. The module prevents general relationships from being anchored in either the Person or Organization module and thereby becoming biased towards one domain.

The Agent core is an integration point, rather than a standalone master data model. Personal and organizational data remain in their respective modules.

## 2. Decision

Construct-X introduces the local class `conx-agent:Agent` in a separate core module.

| Subclass | Superclass |
| --- | --- |
| `conx-person:Person` | `conx-agent:Agent` |
| `conx-org:Organization` | `conx-agent:Agent` |

The class is not defined as `conx-person:Agent`. Otherwise, the Organization module would have to depend on the Person ontology, even though organizations are not people.

## 3. Public IRIs

```text
Ontology IRI: https://www.construct-x.org/ontology/agent
Version IRI:  https://www.construct-x.org/ontology/agent/0.1.0
Namespace:    https://www.construct-x.org/ontology/agent#
Prefix:       conx-agent
```

Version `0.1.0` is the current draft of the minimal Agent core.

## 4. Class `conx-agent:Agent`

| Item                 | Specification                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Label                | Agent / Akteur                                                                                                    |
| Definition           | Entity that can act, bear responsibility, or be referenced as an issuer or participant in a domain context        |
| Module               | `modules/core/agent`                                                                                              |
| Superclass           | No local superclass in the MVP                                                                                    |
| Local subclasses     | `conx-person:Person`, `conx-org:Organization`                                                                     |
| Mandatory attributes | None                                                                                                              |
| Instantiation        | Direct instances are technically possible but should only be used when no more specific local agent type is known |
| Primary sources      | FOAF, SEMIC Core Vocabularies, W3C Organization Ontology                                                          |
| External alignment   | `rdfs:subClassOf foaf:Agent` implemented                                                                          |

### Definitions

German definition, translated:

> An entity that can act, bear responsibility, or be referenced as a participant in a domain context.

English:

> An entity that can act, bear responsibility, or be referenced as a participant in a domain context.

The definition deliberately remains broader than “natural or legal person.” This allows other clearly defined actor types to be added later without asserting them in the MVP.

## 5. MVP Scope

In version `0.1.0`, the Agent core contains exactly:

- the class `conx-agent:Agent`,
- German and English labels and definitions,
- module and ontology metadata,
- a conservative alignment with `foaf:Agent`.

Initially, the Agent core contains no properties of its own. This keeps it stable and prevents domain-specific relationships without clear ownership from accumulating in the base module.

## 6. Explicitly Outside the Agent Core

- Names and dates of birth,
- `sex`, `gender`, and citizenship,
- organization names and organizational structure,
- contact point values and contact roles,
- addresses and address roles,
- memberships, employment, and posts,
- project participations,
- identifier structure,
- credentials, keys, and identity documents,
- generic permission or authorization models,
- software agents as an already established subclass.

A future `SoftwareAgent` is possible, but only after a Construct-X use case has been confirmed. Technical services are not automatically classified as agents.

## 7. Why No Agent Properties in the MVP?

A property with the domain `Agent` automatically applies to people and organizations. This is appropriate only if the relationship truly applies to all relevant agent types and falls within the domain responsibility of the Agent module.

More suitable owners exist for the relationships discussed so far:

| Relationship | Owner | Use of `Agent` |
| --- | --- | --- |
| Contact assignment | `core/contact` | `hasContactPoint` remains unrestricted in domain and can be used for agents |
| Membership | `core/organization` | `member` uses `conx-agent:Agent` as its range |
| Legal representation | `core/organization` | The represented resource is a Legal Entity; the representing resource is a Person |
| Project participation | Project module | The participant may be an Agent |
| `issuedBy` | Identifier/identity model | The issuer may be an Agent |
| `hasIdentityEvidence` | `core/person` | The domain remains Person, rather than every Agent |
| Address | `core/address` | `hasAddressAssignment` remains unrestricted in domain and can be used for agents |

## 8. Alignment Strategy

### 8.1 FOAF

FOAF is the natural choice for a broad alignment target:

```turtle
conx-agent:Agent rdfs:subClassOf foaf:Agent .
```

`rdfs:subClassOf` is preferable to `owl:equivalentClass`. FOAF describes an agent very broadly as something that can act. Construct-X should control its local scope and may therefore remain narrower.

### 8.2 SEMIC

SEMIC supports the pattern of a common Agent superclass for Person and Organization. Before establishing a machine-readable alignment, the canonical IRI, version, and import implications of the specific SEMIC artifact used must be checked.

### 8.3 Schema.org

A direct alignment with `schema:Thing` provides no domain-specific benefit. `schema:Person` is assessed in relation to the Person concept, and `schema:Organization` in relation to the Organization concept.

### 8.4 W3C ORG

W3C ORG uses `foaf:Agent` for members and other actors. The local FOAF alignment enables compatible specialization in the Organization module without copying ORG into the Agent core.

## 9. Dependency Direction

| Module | Dependency on `core/agent` |
| --- | --- |
| `core/person` | Imports/references |
| `core/organization` | Imports/references |
| `domain/project` | Optionally references |

Person and Organization reference the Agent core as their common superclass. `core/agent` itself must not depend on `person`, `contact`, `organization`, or `project`. This keeps the dependencies free of cycles.

## 10. Competency Questions

### ACQ-01: Can a natural person be used as a general actor?

Yes. `conx-person:Person` is a subclass of `conx-agent:Agent`.

### ACQ-02: Can an organization use the same contact mechanism as a person?

Yes. People and organizations can use the same property `conx-contact:hasContactPoint`, whose domain remains unrestricted. The Contact module owns this property and validates the contact point structure. The Agent module defines no contact property of its own.

### ACQ-03: Can the issuing body of an identifier or piece of evidence be modeled?

Yes. An `issuedBy` relationship defined in the identifier or identity architecture can use `conx-agent:Agent` as its range.

### ACQ-04: Do names, contact information, or addresses belong directly to the Agent?

No. Natural persons and organizations have different naming semantics. Contact values are assigned through the Contact module. Addresses are assigned through the Address module. Both patterns remain unrestricted in domain so that projects, sites, or future resources can also use them.

### ACQ-05: Must every Agent be classified as a Person or Organization?

No. The T-Box does not enforce an exhaustive class partition. Application profiles may require more specific types.

## 11. Implemented OWL and SHACL Scope

### OWL

The T-Box contains:

- an ontology resource with a versioned metadata structure,
- `conx-agent:Agent` as an `owl:Class`,
- labels and definitions in German and English,
- a conservative FOAF alignment.

No OWL cardinalities or disjointness axioms are required.

### SHACL

Without Agent properties, a standalone Core Shape for `Agent` initially provides no validation benefit. Validation rules are defined for specific subclasses or relationships:

- a Person Shape for personal data,
- a Contact Shape for contact assignments,
- Organization Shapes for organizational data, memberships, and legal representation.

The Agent module therefore has no dedicated shape artifact in version `0.1.0`.

## 12. Conceptual Example

```turtle
@prefix conx-agent: <https://www.construct-x.org/ontology/agent#> .
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix ex: <https://example.org/id/> .

ex:person-123 a conx-person:Person .

# Follows semantically from the implemented subclass relationship:
# ex:person-123 a conx-agent:Agent .
```

The example illustrates the inference resulting from the implemented T-Box.

## 13. Current Integration Status

The Agent module is now integrated into the implemented core modules:

| Module | Agent Reference | Owner of Domain-Specific Details |
| --- | --- | --- |
| `core/person` | `conx-person:Person rdfs:subClassOf conx-agent:Agent` | Personal names, dates of birth, sex, gender, citizenship, and identity evidence |
| `core/organization` | `conx-org:Organization rdfs:subClassOf conx-agent:Agent` | Organization classes, membership, and legal representation |
| `core/contact` | Agents can use `conx-contact:hasContactPoint` | Contact point, contact method, usage context, and purpose |
| `core/address` | Agents can use `conx-addr:hasAddressAssignment` | AddressAssignment, Address, and AddressRole |

The corresponding overview is provided in the [Integration Diagram](diagrams/agent-integration-model.md).

## 14. Fulfilled Acceptance Criteria

1. The definition and scope of `Agent` are confirmed.
2. The public IRIs are specified in the module metadata and the T-Box.
3. `rdfs:subClassOf foaf:Agent` has been assessed against equivalence and mapping-only alternatives.
4. The need to import FOAF has been technically reviewed.
5. Version `0.1.0` without an Agent Shape is confirmed to comply with the module conventions.
6. The Person model uses `conx-agent:Agent` as its direct superclass.
7. The Organization model uses `conx-agent:Agent` as its direct superclass.
8. Contact and address assignments remain in their respective domain modules and are not moved into the Agent core.

## 15. Follow-Up Tasks

`core/agent`, `core/person`, `core/contact`, `core/address`, and `core/organization` are aligned at the domain level as core modules. No dedicated shape is currently required for the Agent core. The next useful work concerns documentation and visualization support: OntoLens should make reused external properties and external domain/range nodes more visible.