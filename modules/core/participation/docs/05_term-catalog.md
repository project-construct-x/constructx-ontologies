# Term Catalog for the Participation MVP

**Status:** Implemented  
**Version:** 0.2.0  
**As of:** 7 October 2026  
**Scope:** `core/participation`  
**Implementation status:** Terms, initial roles, T-Box, and Core Shapes implemented

## 1. Purpose

This catalog translates the confirmed scope and source analysis into specific local terms. It describes classes, properties, cardinalities, definitions, and the implemented initial scope of a minimal role vocabulary.

Cardinalities are implemented in the Core SHACL Profile. They are deliberately not incorporated into the T-Box as strict OWL cardinalities.

Foundations:

- [Source Analysis](01_source-analysis.md)
- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Agent Specification](../../agent/docs/10_agent-specification.md)
- [Domain Conceptual Model](03_concept-model.md)
- [Participation Diagrams](diagrams/participation-concept-model.md)

## 2. Namespaces

### 2.1 Participation Ontology

```text
Ontology IRI: https://www.construct-x.org/ontology/participation
Version IRI:  https://www.construct-x.org/ontology/participation/0.2.0
Namespace:    https://www.construct-x.org/ontology/participation#
Prefix:       conx-part
```

### 2.2 Minimal Role Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/participation-role
Version IRI:    https://www.construct-x.org/vocab/participation-role/0.1.0
Namespace:      https://www.construct-x.org/vocab/participation-role#
Prefix:         part-role
```

The IRIs are established by module and dataset metadata and machine-readable artifacts: T-Box/Core Shapes 0.2.0, role vocabulary 0.1.0.

Reused namespaces:

```text
conx-agent: https://www.construct-x.org/ontology/agent#
skos:       http://www.w3.org/2004/02/skos/core#
xsd:        http://www.w3.org/2001/XMLSchema#
```

## 3. Modeling Rules

1. `Participation` describes a role assignment that currently holds or held historically.
2. A Participation has exactly one Agent, exactly one role, and exactly one domain context.
3. Unqualified involvement without a role is not permitted.
4. Exactly one Participation exists per Agent/role/context combination in domain terms.
5. Roles are modeled as individuals of the local class `Role`.
6. `Role` is a subclass of `skos:Concept`.
7. Construct-X-maintained role values are maintained in separately versioned SKOS Concept Schemes.
8. Context typing remains open; no local `Context` class is introduced.
9. Start and end dates are optional and describe only assignment validity.
10. Activities, events, provenance, evidence, status, power of attorney, and permissions are not modeled by Participation.
11. No role-specific shortcut properties such as `isSellerOf` are introduced.
12. OWL describes classes, meaning, domain, and range. Minimum and maximum cardinalities, date ordering, and uniqueness belong in SHACL.

## 4. Term Overview

### 4.1 Classes

| Local Term | Superclass | MVP |
| --- | --- | --- |
| `conx-part:Participation` | No local superclass | Yes |
| `conx-part:Role` | `skos:Concept` | Yes |

### 4.2 Local Properties

| Property | Domain | Range | Core SHACL |
| --- | --- | --- | --- |
| `conx-part:participant` | `Participation` | `conx-agent:Agent` | Exactly `1` |
| `conx-part:role` | `Participation` | `Role` | Exactly `1` |
| `conx-part:context` | `Participation` | Open typing | Exactly `1` |
| `conx-part:hasParticipation` | Open context | `Participation` | `0..*`, matching explicit `context` back-reference |
| `conx-part:startDate` | `Participation` | `xsd:date` | `0..1` |
| `conx-part:endDate` | `Participation` | `xsd:date` | `0..1` |

`hasParticipation` is the only new inverse property, inverse to `context` rather than `participant`. It is optional; the three core relationships remain explicit. Domain modules may define role-specific subproperties.

## 5. Classes

### 5.1 `conx-part:Participation`

| Item | Specification |
| --- | --- |
| German label | Beteiligung |
| English label | Participation |
| Definition | Assignment that currently holds or held historically, linking exactly one Agent to exactly one role in exactly one domain context |
| Superclass | No local superclass |
| Core requirements | Exactly one `participant`, exactly one `role`, exactly one `context` |
| Optional information | At most one `startDate` and one `endDate` |
| Uniqueness | The combination of `participant`, `role`, and `context` is unique in domain terms |
| Primary sources | W3C N-ary Relations, W3C ORG Membership, ePO AgentInRole, IFC RelAssignsToActor |
| Alignment | No class alignment in the MVP |
| Exclusions | Planned role, activity participation, provenance, authorization, power of attorney, and unqualified involvement |

Conceptual example:

```turtle
ex:participation-1
    a conx-part:Participation ;
    conx-part:participant ex:bauunternehmen-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-4711 ;
    conx-part:startDate "2026-01-15"^^xsd:date .
```

The instance asserts an effective role assignment. It does not assert that the construction company has already performed a specific activity.

### 5.2 `conx-part:Role`

| Item | Specification |
| --- | --- |
| German label | Rolle |
| English label | Role |
| Definition | Function designated by a controlled term that an Agent holds within a Participation in relation to a context |
| Superclass | `skos:Concept` |
| Instances | Role values as individuals, such as Client or Contractor |
| Concept Scheme | No universal requirement; intended for Construct-X-maintained vocabularies |
| Primary sources | W3C ORG `Role`, DCAT `Role`, IFC `IfcActorRole` |
| Alignment | No alignment in the MVP; external class-based role models require later transformation |
| Exclusions | Agent type, profession, permission role, or role class as a local modeling form |

`Role` describes the abstract role value rather than the specific assignment. Only a `Participation` connects the role value to Agent and context.

## 6. Properties

### 6.1 `conx-part:participant`

| Item | Specification |
| --- | --- |
| Definition | Specifies the Agent whose role is described by the Participation |
| Domain | `conx-part:Participation` |
| Range | `conx-agent:Agent` |
| Core SHACL | Exactly one value |
| Inverse | No local inverse property in the MVP |
| Source | W3C ORG `member`, ePO `playedBy`, IFC `RelatingActor` |

A Participation must not group multiple people or organizations. Multiple Agents in the same role and context receive separate Participation instances.

### 6.2 `conx-part:role`

| Item | Specification |
| --- | --- |
| Definition | Specifies the exactly one controlled role of the Agent in the Participation |
| Domain | `conx-part:Participation` |
| Range | `conx-part:Role` |
| Core SHACL | Exactly one value |
| Source | W3C ORG `role`, PROV/DCAT `hadRole`, IFC `ActingRole` |

A Participation without a role value is invalid. If the same Agent holds multiple roles in the same context, a separate Participation is used for each role.

### 6.3 `conx-part:context`

| Item | Specification |
| --- | --- |
| Definition | Specifies the exactly one domain resource in relation to which the role assignment applies |
| Domain | `conx-part:Participation` |
| Range | No domain-specific restrictive local class |
| Core SHACL | Exactly one resource value |
| Source | W3C pattern for n-ary relationships, ePO `contextualisedBy`, SPAR PRO `relatesToEntity` |

Possible context resources include a contract, project, document, delivery note, product, or asset. The Participation module infers no local context type from the use of `context`.

### 6.4 `conx-part:startDate`

| Item | Specification |
| --- | --- |
| Definition | Date from which the role assignment described by the Participation applies or applied |
| Domain | `conx-part:Participation` |
| Range | `xsd:date` |
| Core SHACL | `0..1` |
| Boundary | Not the beginning of an activity or context object |
| Source | W3C ORG `memberDuring`, Schema.org Role `startDate`, SPAR PRO `RoleInTime` |

Absence of a start date means only that the beginning is unspecified. It does not mean that the Participation has always applied.

### 6.5 `conx-part:endDate`

| Item | Specification |
| --- | --- |
| Definition | Date until which the role assignment described by the Participation applies or applied |
| Domain | `conx-part:Participation` |
| Range | `xsd:date` |
| Core SHACL | `0..1` |
| Additional rule | If start and end dates are present, `endDate` must not precede `startDate` |
| Boundary | Not the end of an activity or context object |
| Source | W3C ORG `memberDuring`, Schema.org Role `endDate`, SPAR PRO `RoleInTime` |

Absence of an end date means only that no end is specified. Unlimited or permanent assignment must not be inferred without further information.

### 6.6 `conx-part:hasParticipation`

Links any context to a Participation IRI. No restrictive domain; range Participation; `0..*`. Inverse to `context`.

The value must be a complete Participation; its `context` statement must refer back to the source object. This is not an inverse Agent relationship.

## 7. Minimal Role Vocabulary

The MVP should contain a small, separately versioned SKOS Concept Scheme. It provides an immediately usable starting point and demonstrates role individuals. It is not a closed universal role list.

### 7.1 Approved Initial Values

| IRI Suffix | Notation | German | English | Binding Meaning |
| --- | --- | --- | --- | --- |
| `ClientRole` | `client` | Auftraggeber | Client | Agent on whose behalf or in whose interest the respective context is handled |
| `ContractorRole` | `contractor` | Auftragnehmer | Contractor | Agent contractually obliged within the context to perform agreed services |
| `SupplierRole` | `supplier` | Lieferant | Supplier | Agent providing goods, materials, or equipment within the context |
| `ArchitectRole` | `architect` | Architekt | Architect | Agent performing an architectural planning or design function within the context |
| `EngineerRole` | `engineer` | Ingenieur | Engineer | Agent performing an engineering planning, calculation, or design function within the context |

These five values form the approved, source-based initial scope. `ArchitectRole` and `EngineerRole` designate only a function in the specified context. They classify the Agent as neither a profession nor an organization type. Likewise, `ClientRole`, `ContractorRole`, and `SupplierRole` are not treated as Agent or Organization classes.

Domain-specific roles, such as delivery note roles, are not added preemptively to this minimal vocabulary. Their role sets are derived during development of the respective domain module from its own competency questions and sources. Such roles may be maintained in a separate SKOS Concept Scheme while still being used as `conx-part:Role`.

### 7.2 Maintenance Principles

- Every value is an instance of `conx-part:Role` and `skos:Concept`.
- Every value has German and English preferred labels and definitions.
- Every value has a stable, language-independent `skos:notation`.
- New values are added to the role vocabulary without requiring a Participation T-Box change.
- Removed values are marked deprecated and are not reused with changed meanings.
- Narrower domain role vocabularies may form their own Concept Schemes.
- Similarly named roles are not aligned through `skos:exactMatch` without comparing definitions.

### 7.3 Distinction from LocationRole

The existing LocationRole vocabulary uses the same technical principle: a local role class plus separate SKOS individuals. In content terms, it is not part of the Participation vocabulary. LocationRole describes an address's function within a location assignment; `conx-part:Role` describes an Agent's function in relation to a context.

## 8. Uniqueness and Multiple Roles

### 8.1 Multiple Agents

```turtle
ex:participation-a
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x .

ex:participation-b
    a conx-part:Participation ;
    conx-part:participant ex:organization-b ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x .
```

### 8.2 Multiple Roles of the Same Agent

```turtle
ex:participation-c
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:project-x .

ex:participation-d
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:SupplierRole ;
    conx-part:context ex:project-x .
```

The Agent/role/context combination must not be duplicated by a second Participation. This uniqueness is implemented as a SHACL-SPARQL constraint rather than an `owl:hasKey` axiom.

## 9. Explicitly Excluded Terms

| Term | Rationale |
| --- | --- |
| `AgentRoleAssignment` | `Participation` is confirmed as the central term |
| `AgentInRole` | Unnecessary as a second class alongside `Participation` |
| `Context` / `ParticipationContext` | Context resource typing remains open |
| `ActivityParticipation` | Activities and events belong in a future ontology |
| `ParticipationStatus` | A Participation asserts an assignment that currently holds or held historically |
| `ParticipationEvidence` | Evidence is outside this module |
| `isParticipationOf` | Unnecessary alongside `context` and its optional reverse direction `hasParticipation` |
| `isSellerOf` and comparable properties | Roles remain individuals; no property per role value |
| Local time interval | Simple optional dates suffice for the MVP |
| External alignment axioms | Assessed only for specific needs in separate alignment modules |

## 10. Implemented Core Validation Profile

A `Participation` instance is valid in the implemented core profile if:

1. exactly one `participant` is present and typed as `conx-agent:Agent`,
2. exactly one `role` is present and typed as `conx-part:Role`,
3. exactly one `context` is present as an RDF resource,
4. `startDate` and `endDate` each occur at most once as `xsd:date`,
5. a supplied `endDate` does not precede a supplied `startDate`,
6. no second Participation describes the same Agent/role/context combination.

Whether a domain profile permits only values from a particular role Concept Scheme is decided by that profile. The open core requires only typing as `conx-part:Role`.

## 11. Approval Decision

On 27 August 2026, the following were confirmed for further specification:

1. the property names `participant`, `role`, `context`, `startDate`, and `endDate`,
2. the namespace and prefix `conx-part`,
3. the IRI and prefix `participation-role` and `part-role`,
4. the five initial roles and their definitions in Section 7.1,
5. derivation of further roles from their respective domain modules.

The interaction of these concepts is illustrated in the [Conceptual Model](03_concept-model.md), [Participation Diagrams](diagrams/participation-concept-model.md), and [Module Boundaries](04_module-boundaries.md). The executable validation contract is specified in the [SHACL Requirements](06_shacl-requirements.md) and implemented in the [Core Shapes](07_core-shapes.md).

## 12. Illustrative Example

> `participant` identifies Anna, `role` identifies the Architect role, and `context` identifies the construction project. Only the combination of all three properties forms the complete domain statement.