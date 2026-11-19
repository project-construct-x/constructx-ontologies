# Domain Conceptual Model of the Participation Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** `core/participation`  
**Implementation status:** Implemented as T-Box, role vocabulary, and Core Shapes

## 1. Purpose

The conceptual model combines source analysis, confirmed scope, and term catalog into a consistent domain model. It describes a qualified relationship between Agent, role, and context without duplicating the semantics of these resources.

Visual perspectives are provided in the [Participation Diagrams](diagrams/participation-concept-model.md). Classes, properties, and cardinalities are documented in the [Term Catalog](05_term-catalog.md).

## 2. Model Core

The MVP has two local classes:

```text
Participation
Role
```

The domain core is:

| Resource | Property | Requirement |
| --- | --- | --- |
| `Participation` | `hasParticipant` | Exactly one Agent |
| `Participation` | `hasRole` | Exactly one Role |
| `Participation` | `hasContext` | Exactly one domain resource |
| `Participation` | `startDate` | Optionally one `xsd:date` |
| `Participation` | `endDate` | Optionally one `xsd:date` |

`Participation` is the specific assignment. `Role` is the controlled role value. Agent and context are referenced from their responsible modules.

## 3. Meaning of Participation

A `Participation` describes a role assignment that currently holds or held historically. It is neither a plan nor an assertion that an activity was performed.

Example:

> Organization A is the Contractor in Contract X.

This statement contains three distinct elements:

1. `Organization A` is the Agent.
2. `Contractor` is the role.
3. `Contract X` is the context.

The Participation links these elements. It does not turn the Agent into a subclass `Contractor` or the contract into a Participation-specific context class.

## 4. Qualified Relationship

A direct property such as `isContractorOf` could link Agent and context, but loses the role as an independently maintainable value and cannot carry information about the relationship's validity.

The qualified pattern therefore objectifies the relationship:

| Resource | Property | Target |
| --- | --- | --- |
| Participation P | `hasParticipant` | Agent A |
| Participation P | `hasContext` | Context X |
| Participation P | `hasRole` | Role R |

The Participation is not RDF reification of a triple. It is a separate domain relationship resource following the W3C pattern for n-ary relationships.

## 5. Agent

`hasParticipant` references exactly one `conx-agent:Agent`. This allows people and organizations to use the same Participation pattern.

| Class | Superclass |
| --- | --- |
| `conx-person:Person` | `conx-agent:Agent` |
| `conx-org:Organization` | `conx-agent:Agent` |

The model does not close the Agent hierarchy to these two types. A future additional Agent type may use Participation without changing the Participation T-Box.

Multiple Agents are not grouped in one Participation. If multiple Agents act jointly, either each Agent has its own Participation or an existing Organization or consortium is referenced as the collective Agent.

## 6. Role

### 6.1 Role Value and Assignment

The local class `Role` is a subclass of `skos:Concept`. Its instances are controlled role values:

- `ClientRole`
- `ContractorRole`
- `SupplierRole`
- `ArchitectRole`
- `EngineerRole`

Roles are individuals rather than subclasses of Agent or Participation. A role is assigned to an Agent and context only through its use in a Participation.

### 6.2 Multiple Roles

An Agent may have multiple roles in the same context. Each role receives a separate Participation:

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| P1 | Organization A | `ContractorRole` | Project X |
| P2 | Organization A | `SupplierRole` | Project X |

Every combination therefore remains individually referenceable. A Participation with two roles would become ambiguous if start and end dates or other domain rules differed by role.

### 6.3 Role Vocabularies

The Participation T-Box defines no closed role list. A minimal Construct-X vocabulary illustrates use and provides an immediately usable initial set. Further domain vocabularies may contain contract, delivery, document, or lifecycle roles.

Construct-X-maintained role vocabularies use SKOS Concept Schemes. The general T-Box does not, however, require Scheme membership, allowing external role values to be used after explicit typing.

## 7. Context

### 7.1 Open Resource Reference

The context is the resource in relation to which the role applies. Depending on the domain module, this may be:

- a contract,
- a project,
- a document,
- a delivery note,
- a product or asset,
- another domain-defined resource.

These resources have no necessary common local superclass. The Participation module therefore introduces no `Context` class and imposes no domain-specific restrictive range on `hasContext`.

### 7.2 Exactly One Context

A Participation has exactly one context. If the same role applies to two contracts, two Participation instances are created:

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| P1 | Organization A | `ContractorRole` | Contract X |
| P2 | Organization A | `ContractorRole` | Contract Y |

Multiple contexts in one instance would leave it unclear whether the role assignment and its validity dates apply identically to each context.

Domain profiles may restrict the open context. For example, a document profile may allow only `Document` as context without changing the general Participation T-Box.

## 8. Uniqueness

Exactly one Participation exists per Agent/role/context combination in domain terms:

```text
(hasParticipant, hasRole, hasContext) -> one Participation
```

This rule prevents duplicate relationship resources for the same statement. It is checked against the data graph using SHACL. No `owl:hasKey` is provided because a violation should be reported as a data quality error rather than logically merged through `owl:sameAs`.

Multiple separate validity periods for the same combination cannot be modeled in the MVP. Such a requirement would fundamentally change either the uniqueness rule or the temporal model and therefore requires a separate future modeling decision.

## 9. Temporal Validity

`startDate` and `endDate` are optional date values on the Participation:

| Information | Meaning |
| --- | --- |
| No date | The assignment currently holds or held historically; temporal boundaries are unspecified |
| Only `startDate` | The beginning of validity is specified, but the end is not |
| Only `endDate` | The end of validity is specified, but the beginning is not |
| Both dates | Validity is bounded by beginning and end |

If both values are present, `endDate` must not precede `startDate`. The dates designate neither the beginning nor the end of an activity and do not change the lifetime of the context object.

The MVP uses simple `xsd:date` values. A local interval class or OWL-Time import is unnecessary.

## 10. Boundary with Activities

Participation describes roles rather than activity participation:

| Model | Statement |
| --- | --- |
| Participation | Organization A is the Contractor in Project X |
| Future activity ontology | Organization A performs Activity Y |

The first statement does not prove the second. A role may exist without a specific activity having begun or ended. A future activity ontology may reference Agent, Participation, or Role, but owns its own event and execution semantics.

## 11. Boundary with Membership

`core/organization:Membership` and `Participation` remain separate:

| Membership | Participation |
| --- | --- |
| Affiliation with an Organization | Role in relation to any context |
| Context is an Organization | Context type remains open |
| No role value required in the current MVP | Exactly one Role required |
| May have its own identifier, such as a membership number | No Participation-specific identifier provided |

Membership is therefore not modeled as a subclass of Participation. The Participation module does not change existing organizational semantics.

## 12. Navigation from Context and Domain Specialization

The model introduces no properties such as `isClientOf`, `isContractorOf`, or `isSupplierOf`. The complete statement remains the Participation with its `hasParticipant`, `hasRole`, and `hasContext`.

Since 0.2.0, `hasParticipation` additionally connects context to Participation. Only this general property is `owl:inverseOf hasContext`; its source type remains open. It is optional and not functional.

Domain modules may define descriptive subproperties such as `conx-dn:hasBuyerParticipation`. They must check the appropriate role and identical context. The role remains explicit on the Participation. This is not a direct shortcut from context to Agent.

For offline validation, `hasContext` remains explicitly required. The forward edge alone does not replace a complete Participation. Existing instances without a forward edge remain valid. OWL inference may derive general inverse relationships; it does not automatically generate role-specific edges.

## 13. Origin, Evidence, and Status

The presence of a Participation asserts an assignment that currently holds or held historically. The module therefore has no status values for planned, proposed, or revoked relationships.

Origin, evidence, provenance, power of attorney, and authorization are neither modeled in the MVP nor earmarked as future extensions of this module. Other models may reference Participation resources without introducing their semantics into the Participation core.

## 14. Overall Conceptual Example

The example uses Participation 0.3.0 and the unchanged role vocabulary 0.1.0:

```turtle
@prefix conx-part: <https://www.construct-x.org/ontology/participation#> .
@prefix part-role: <https://www.construct-x.org/vocab/participation-role#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .

ex:contract-4711 conx-part:hasParticipation ex:contractor-participation,
    ex:supplier-participation .

ex:contractor-participation
    a conx-part:Participation ;
    conx-part:hasParticipant ex:bauunternehmen-a ;
    conx-part:hasRole part-role:ContractorRole ;
    conx-part:hasContext ex:contract-4711 ;
    conx-part:startDate "2026-01-15"^^xsd:date ;
    conx-part:endDate "2026-12-31"^^xsd:date .

ex:supplier-participation
    a conx-part:Participation ;
    conx-part:hasParticipant ex:bauunternehmen-a ;
    conx-part:hasRole part-role:SupplierRole ;
    conx-part:hasContext ex:contract-4711 .
```

The same company holds two different roles in the same contract. Two Participation instances are therefore used.

## 15. Modeling Decisions

1. `Participation` is the sole local class for the specific role assignment.
2. A Participation represents exactly one combination of Agent, role, and context.
3. `hasParticipant`, `hasRole`, and `hasContext` are each required exactly once in the core profile.
4. Roles are maintained as individuals of the local SKOS-based class `Role`.
5. Context typing remains open and is restricted through domain profiles.
6. Start and end dates are optional `xsd:date` values describing validity.
7. Activities and events are outside the model.
8. Membership remains an independent organizational concept.
9. There are no role-specific shortcut properties in the core and no external alignment axioms. Domain modules may specialize `hasParticipation` by role.
10. Origin, evidence, status, provenance, power of attorney, and authorization are excluded.
11. A minimal role vocabulary with the approved roles `ClientRole`, `ContractorRole`, `SupplierRole`, `ArchitectRole`, and `EngineerRole` is provided separately from the T-Box.
12. Cardinality, date ordering, and uniqueness are implemented in SHACL rather than strict OWL cardinalities.
13. Further roles are derived during development of the responsible domain module rather than incorporated into the core preemptively.