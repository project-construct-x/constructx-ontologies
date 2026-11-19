# Domain-Specific SHACL Requirements for the Participation MVP

**Status:** Implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** Participation Core Shapes

## 1. Purpose

This document specifies the executable data quality requirements for the Participation module. It describes shape targets, constraints, severity levels, stable error codes, and valid and invalid scenarios.

The executable implementation is located at:

```text
modules/core/participation/shapes/conx-part-core.shacl.ttl
```

The T-Box, shape graph, role vocabulary, and test data implement these requirements in version `0.3.0`.

Foundations:

- [Source Analysis](01_source-analysis.md)
- [Scope and Competency Questions](02_scope-and-competency-questions.md)
- [Term Catalog](05_term-catalog.md)
- [Domain Conceptual Model](03_concept-model.md)
- [Module Boundaries](04_module-boundaries.md)
- [Participation Diagrams](diagrams/participation-concept-model.md)

## 2. Shape Set

```text
Shape graph: modules/core/participation/shapes/conx-part-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/participation/core
Version IRI: https://www.construct-x.org/shapes/participation/core/0.3.0
Namespace:   https://www.construct-x.org/shapes/participation/core#
Prefix:      conx-part-sh
Version:     0.3.0
```

These values are established in the shape graph and `module.yaml` for version `0.3.0`.

## 3. Validation Principles

### 3.1 OWL and SHACL

- OWL describes classes, meaning, domain, range, and subclass relationships under the open-world assumption.
- SHACL checks the specific data graph supplied.
- Mandatory fields, maximum cardinalities, date ordering, and uniqueness are implemented in the Core Shape rather than strict OWL cardinalities.
- The shape remains open to additional properties. `sh:closed true` is not intended.
- Validation is performed with the Participation and Agent T-Boxes.
- Role vocabularies are loaded only when used by the respective test or application graph.
- The rules must work without enabled RDFS or OWL inference.

### 3.2 Explicit Typing

Every resource used as a Participation or carrying a local Participation property must be explicitly typed as `conx-part:Participation`.

The value of `hasParticipant` must be typed as `conx-agent:Agent` or a known subclass of `Agent`, such as `conx-person:Person` or `conx-org:Organization`. Typing derived solely from a property domain is insufficient.

Every role value must explicitly be a `conx-part:Role`. Typing solely as `skos:Concept` is insufficient because not every SKOS concept denotes an Agent role.

The context requires no Participation-specific type.

### 3.3 Resource Form

| Resource | Core Requirement | Rationale |
| --- | --- | --- |
| `Participation` | IRI | Separate, referenceable relationship resource with a domain identity |
| `hasParticipant` | IRI | Agents are referenced as domain-identifiable resources |
| `hasRole` | IRI | Roles are stable controlled vocabulary values |
| `hasContext` | IRI or blank node | Context typing remains open and follows the owning domain module |

Literals are excluded from all three core relationships. Blank nodes for Participation, Agent, or role are not permitted in the core profile. A future domain profile may require an IRI for context.

### 3.4 Severity Levels

All core violations defined in this document use `sh:Violation`. The Core Shape produces no warnings for recommendations such as using a particular role Scheme or specifying validity dates.

Future domain profiles may add stricter rules and further severity levels.

### 3.5 Error Messages

Every constraint receives:

- a German `sh:message`,
- an English `sh:message`,
- the stable requirement identifier from this document,
- a specific result path wherever SHACL can determine one.

The identifier appears in square brackets in both messages, for example `[PART-010]`.

## 4. Responsibility Boundaries

| Requirement | Responsible Shape Set | Rule in the Participation Core Shape |
| --- | --- | --- |
| Participation structure | `participation/core` | Validate fully |
| Agent type | `participation/core` with Agent T-Box | Check Agent reference and type |
| Personal and organizational data | `person/core`, `organization/core` | Do not duplicate |
| Role value as `Role` | `participation/core` | Check IRI and explicit type |
| Membership in the minimal role Scheme | Reference dataset or domain profile | Not enforced in the open core |
| Roles for delivery notes and other domain modules | Respective domain profile | Not checked preemptively in the Participation Core |
| Context type and content | Owning domain module | Check resource form only |
| Activity and event participation | Future activity ontology | Not checked |
| Membership | `organization/core` | Not treated as Participation |
| Provenance, evidence, status, and authorization | Other domain or governance profiles | Not checked |

## 5. Approved MVP Requirements

| Topic | Decision |
| --- | --- |
| Participation | Exactly one Agent, exactly one role, and exactly one context |
| Agent | IRI typed as `conx-agent:Agent` or a known subclass |
| Role | IRI explicitly typed as `conx-part:Role` |
| Context | Exactly one IRI or blank node; no local context class |
| Time | `startDate` and `endDate` each optional and occurring at most once as `xsd:date` |
| Date ordering | When both are supplied, `startDate <= endDate` |
| Uniqueness | One Participation per Agent/role/context combination |
| Role Scheme | Not closed in the open core |
| Additional properties | Permitted |
| Inverse relationships | `hasParticipation` optional; valid Participation and identical explicit `hasContext` required |

Start and end dates are not part of the uniqueness key. Different dates therefore do not justify a second Participation with the same Agent/role/context combination.

## 6. Shape Catalog

| Shape IRI | Type | Target or Usage | Purpose |
| --- | --- | --- | --- |
| `conx-part-sh:HasParticipationShape` | Node Shape | Subjects of `hasParticipation` | Valid Participation IRI and matching `hasContext` back-reference |
| `conx-part-sh:ParticipationShape` | Node Shape | Participation class instances and subjects of local Participation properties | Complete role-assignment contract |
| `conx-part-sh:ParticipationIriShape` | Reusable Node Shape | Referenced by `ParticipationShape` | Requires an IRI |
| `conx-part-sh:ExplicitParticipationTypeShape` | Reusable Node Shape | Referenced by `ParticipationShape` | Requires the explicit local type |
| `conx-part-sh:AgentReferenceShape` | Reusable Node Shape | Value of `hasParticipant` | Checks IRI and Agent type |
| `conx-part-sh:RoleReferenceShape` | Reusable Node Shape | Value of `hasRole` | Checks IRI and explicit Role type |
| `conx-part-sh:ContextReferenceShape` | Reusable Node Shape | Value of `hasContext` | Permits IRI or blank node |

The helper shapes have no global targets. They are invoked only by the named Property Shapes or Node Shapes.

## 7. Targets

`conx-part-sh:ParticipationShape` has the following targets:

- `sh:targetClass conx-part:Participation`,
- `sh:targetSubjectsOf conx-part:hasParticipant`,
- `sh:targetSubjectsOf conx-part:hasRole`,
- `sh:targetSubjectsOf conx-part:hasContext`,
- `sh:targetSubjectsOf conx-part:startDate`,
- `sh:targetSubjectsOf conx-part:endDate`.

This also captures untyped resources as soon as they use a local Participation property. A data holder cannot bypass the type requirement by supplying only `hasParticipant`, `hasRole`, and `hasContext`.

Values of `hasParticipant`, `hasRole`, or `hasContext` are not themselves targeted as Participation.

## 8. Node Constraints

| ID | Focus | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-001` | Participation | Resource form | Focus node must be an IRI |
| `PART-002` | Participation | Explicit type | Focus node must explicitly be `conx-part:Participation` |

`PART-002` also applies to every subject of the five existing Participation-specific properties. Subjects of `hasParticipation`, by contrast, are contexts and are not typed as Participation. Additional types on the same node remain permitted.

## 9. Participant Constraints

| ID | Property | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-010` | `hasParticipant` | Minimum cardinality | At least one value |
| `PART-011` | `hasParticipant` | Maximum cardinality | At most one value |
| `PART-012` | `hasParticipant` | Resource form | Value must be an IRI |
| `PART-013` | `hasParticipant` | Agent type | Value must be a `conx-agent:Agent` or an instance of a known subclass |

Together, `PART-010` and `PART-011` require exactly one Agent. An Agent may occur in multiple Participations provided the role or context differs.

The Participation Shape checks no names, identifiers, addresses, or contact information of the Agent.

## 10. Role Constraints

| ID | Property | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-020` | `hasRole` | Minimum cardinality | At least one value |
| `PART-021` | `hasRole` | Maximum cardinality | At most one value |
| `PART-022` | `hasRole` | Resource form | Value must be an IRI |
| `PART-023` | `hasRole` | Role type | Value must explicitly be `conx-part:Role` |

A Participation without a role is invalid. If an Agent has two roles in the same context, two Participations are created.

`PART-023` requires neither `skos:inScheme` nor a value from `participation-role`. Separate domain vocabularies and external role values explicitly typed as `conx-part:Role` therefore remain permitted.

## 11. Context Constraints

| ID | Property | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-030` | `hasContext` | Minimum cardinality | At least one value |
| `PART-031` | `hasContext` | Maximum cardinality | At most one value |
| `PART-032` | `hasContext` | Resource form | Value must be an IRI or blank node |

The core requires no particular context type. In particular, no `conx-part:Context` is introduced or assumed. Literals are unsuitable as contexts because they do not represent domain resources that can be described.

### 11.1 Optional Reverse Direction

| ID | Property | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-060` | `hasParticipation` | Target contract | Complete Participation IRI, including `hasParticipant`, `hasRole`, and `hasContext` |
| `PART-061` | `hasParticipation` / `hasContext` | Context equality | Target Participation must explicitly identify the source object as its `hasContext` |

No `sh:minCount` is imposed: existing data without a forward edge remains valid. The check requires no OWL inference. SHACL does not automatically generate forward edges.

## 12. Temporal Constraints

| ID | Property or Comparison | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-040` | `startDate` | Maximum cardinality | At most one value |
| `PART-041` | `startDate` | Datatype | Every value must be `xsd:date` |
| `PART-042` | `endDate` | Maximum cardinality | At most one value |
| `PART-043` | `endDate` | Datatype | Every value must be `xsd:date` |
| `PART-044` | `startDate`, `endDate` | Ordering | If both values are present, `startDate` must not be later than `endDate` |

`PART-044` should be implemented through a SHACL Core comparison component such as `sh:lessThanOrEquals`. A SPARQL rule is permitted only if the Core component demonstrably fails to work correctly in the validator used.

The following cases remain valid:

| Information | Assessment |
| --- | --- |
| No date | Validity boundaries unspecified |
| Only `startDate` | Beginning specified; end unknown or unspecified |
| Only `endDate` | End specified; beginning unknown or unspecified |
| Both dates equal | Validity relating to or bounded within the same day |
| `startDate` before `endDate` | Ordered validity period |

The shapes do not check whether the Participation currently applies on the validation date.

## 13. Uniqueness Constraint

| ID | Focus | Constraint | SHACL Requirement |
| --- | --- | --- | --- |
| `PART-050` | Participation | Tuple uniqueness | No other Participation may have the same `hasParticipant`, `hasRole`, and `hasContext` |

SHACL Core has no general component for a composite key. `PART-050` is therefore implemented as a local `sh:SPARQLConstraint`.

The query must:

1. compare only complete Agent/role/context combinations,
2. detect another Participation with the same three RDF terms,
3. exclude the focus node itself,
4. produce a deterministic result for each duplicate pair,
5. deliberately exclude dates from the comparison.

Uniqueness applies within the entire data graph supplied to a validation run. The shape cannot detect duplicates that exist only in an unloaded external graph or another dataset. Dataset or data-space profiles must therefore establish which named graphs are validated together for this check.

## 14. Role Vocabulary and Core Openness

The minimal role vocabulary is a separately versioned reference dataset. Its own quality is checked by automated dataset tests rather than a closed value list in the Participation Core Shape.

Every value in the minimal vocabulary must:

1. have an IRI,
2. be a `conx-part:Role` and `skos:Concept`,
3. belong specifically to the Scheme `https://www.construct-x.org/vocab/participation-role`,
4. have exactly one stable `skos:notation`,
5. have one German and one English preferred label,
6. have one German and one English definition.

Version `0.1.0` of the vocabulary contains exactly the five approved initial values. This closed scope is a version-specific statement about the reference dataset rather than a global restriction on all Participations.

Further roles, such as delivery note roles, are defined during development of the respective domain module and may use their own Concept Scheme.

## 15. Valid Core Examples

### 15.1 Minimal Participation

```turtle
ex:agent-a
    a conx-agent:Agent .

ex:contractor-role
    a conx-part:Role .

ex:participation-a
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole ex:contractor-role ;
    conx-part:hasContext ex:contract-x .
```

### 15.2 Participation with Validity Dates

```turtle
ex:participation-b
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-b ;
    conx-part:hasRole part-role:EngineerRole ;
    conx-part:hasContext ex:project-x ;
    conx-part:startDate "2026-01-15"^^xsd:date ;
    conx-part:endDate "2026-12-31"^^xsd:date .
```

The role value from the reference vocabulary must be typed as `conx-part:Role` in the jointly loaded graph.

### 15.3 External Domain Role

```turtle
domain-role:ExampleDocumentRole
    a conx-part:Role, skos:Concept ;
    skos:inScheme domain-role:ExampleRoleScheme .

ex:participation-c
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-c ;
    conx-part:hasRole domain-role:ExampleDocumentRole ;
    conx-part:hasContext ex:document-x .
```

The example remains valid in the open core even though the role does not belong to the minimal `participation-role` Scheme.

### 15.4 Blank Node as Context

```turtle
ex:participation-d
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-d ;
    conx-part:hasRole part-role:SupplierRole ;
    conx-part:hasContext [ ex:localContextCode "A-17" ] .
```

The Core Shape assesses only the context's resource form. A domain profile may require an IRI or a specific context type.

## 16. Invalid Core Examples

### 16.1 Missing Role

```turtle
ex:invalid-a
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasContext ex:contract-x .
```

Expected violation: `PART-020`.

### 16.2 Multiple Agents

```turtle
ex:invalid-b
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a, ex:agent-b ;
    conx-part:hasRole part-role:ContractorRole ;
    conx-part:hasContext ex:contract-x .
```

Expected violation: `PART-011`.

### 16.3 Role without the Local Role Type

```turtle
ex:not-a-role
    a skos:Concept .

ex:invalid-c
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole ex:not-a-role ;
    conx-part:hasContext ex:contract-x .
```

Expected violation: `PART-023`.

### 16.4 Literal as Context

```turtle
ex:invalid-d
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole part-role:ClientRole ;
    conx-part:hasContext "Vertrag X" .
```

Expected violation: `PART-032`.

### 16.5 Reversed Date Order

```turtle
ex:invalid-e
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole part-role:EngineerRole ;
    conx-part:hasContext ex:project-x ;
    conx-part:startDate "2026-12-31"^^xsd:date ;
    conx-part:endDate "2026-01-01"^^xsd:date .
```

Expected violation: `PART-044`.

### 16.6 Duplicate Combination

```turtle
ex:duplicate-a
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole part-role:ContractorRole ;
    conx-part:hasContext ex:contract-x ;
    conx-part:startDate "2026-01-01"^^xsd:date .

ex:duplicate-b
    a conx-part:Participation ;
    conx-part:hasParticipant ex:agent-a ;
    conx-part:hasRole part-role:ContractorRole ;
    conx-part:hasContext ex:contract-x ;
    conx-part:startDate "2026-07-01"^^xsd:date .
```

Expected violation: `PART-050`. Different start dates do not eliminate the duplicate.

## 17. Implemented Test Artifacts

### 17.1 Valid Test Graphs

| File | Scenario |
| --- | --- |
| `tests/valid/minimal-participation.ttl` | Exactly one Agent, one role, and one context |
| `tests/valid/context-navigation.ttl` | Optional `hasParticipation` edge with a matching `hasContext` back-reference |
| `tests/valid/dated-participation.ttl` | Both dates and cases with only one date boundary |
| `tests/valid/multiple-roles-and-contexts.ttl` | Multiple distinct combinations without duplicates |
| `tests/valid/external-role.ttl` | Local Role typing outside the minimal Scheme |
| `tests/valid/blank-node-context.ttl` | Open context as a blank node |
| `tests/valid/agent-subclass.ttl` | Participant as an instance of an Agent subclass |
| `tests/valid/person-and-organization-participants.ttl` | Person and Organization as specific Agent subclasses |

### 17.2 Invalid Test Graphs

| File | Expected Error Codes |
| --- | --- |
| `tests/invalid/missing-required-values.ttl` | `PART-010`, `PART-020`, `PART-030` |
| `tests/invalid/invalid-participant.ttl` | `PART-011`, `PART-012`, `PART-013` |
| `tests/invalid/invalid-role.ttl` | `PART-021`, `PART-022`, `PART-023` |
| `tests/invalid/invalid-context.ttl` | `PART-031`, `PART-032` |
| `tests/invalid/invalid-dates.ttl` | `PART-040`, `PART-041`, `PART-042`, `PART-043`, `PART-044` |
| `tests/invalid/duplicate-participation.ttl` | `PART-050` |
| `tests/invalid/context-navigation.ttl` | `PART-060`, `PART-061` |
| `tests/invalid/untyped-or-blank-participation.ttl` | `PART-001`, `PART-002` |

An invalid graph may contain multiple independent resources. Every documented error code must nevertheless be clearly attributable to an intentionally violated constraint.

## 18. Requirements for Automated Tests

The automated implementation checks:

1. The shape graph passes SHACL metavalidation.
2. All valid test graphs validate without `sh:Violation`.
3. Every invalid test graph produces all documented error codes.
4. Every error code is triggered by at least one test graph.
5. Local shape IRIs and error codes are unique.
6. All named constraints have German and English messages.
7. Validation works with `inference="none"`.
8. Participation and Agent T-Boxes are loaded as the ontology graph.
9. The minimal role vocabulary is loaded for relevant fixtures.
10. A role IRI from another domain remains valid if explicitly typed as `Role`.
11. A resource typed only as `skos:Concept` is rejected as a role.
12. A Person or Organization is accepted as `hasParticipant` through its known Agent subclass.
13. A literal as Agent, role, or context is rejected.
14. A blank node is accepted as context, but not as Participation, Agent, or role.
15. Start date only, end date only, and equal start/end dates remain valid.
16. An end date preceding the start date is rejected.
17. Tuple uniqueness detects duplicates independently of date values.
18. Different roles of the same Agent in the same context remain valid.
19. The same role of the same Agent in different contexts remains valid.
20. The shape remains open to additional properties from other modules.

## 19. Deliberately Excluded Core Validation

The Participation Core Shape does not check:

- whether a context has a particular domain type,
- whether a role belongs to the minimal `participation-role` Scheme,
- whether the role assignment is supported by legal or domain evidence,
- whether the Agent is authorized or qualified to hold the role,
- whether a role is compatible with a particular context type,
- whether the Participation currently applies today,
- whether missing start or end dates are plausible in domain terms,
- whether the context itself exists during the specified period,
- whether an activity was performed or an event attended,
- whether Membership or representation follows from the Participation,
- whether identical Participations exist in unloaded graphs,
- whether provenance, evidence, status, or permissions are present,
- whether role-specific direct relationships were materialized,
- whether external ontologies contain semantically equivalent terms.

These matters belong in domain profiles, other modules, governance rules, or external verification services.

## 20. Implemented Artifacts

1. Participation T-Box and `module.yaml`.
2. Reference vocabulary `participation-role` with `dataset.yaml`.
3. Core Shapes implementing the `PART-*` requirements.
4. Valid and invalid test graphs.
5. Automated ontology, vocabulary, and shape tests.
6. Shape documentation and HTML documentation.
7. Core overviews, structure tests, and build metadata.

## 21. Acceptance Criteria for the Core Shape Implementation

The implementation is complete from a domain perspective because:

1. every `PART-*` requirement is implemented as a traceable constraint,
2. exactly one Agent, one role, and one context are required,
3. Agent and role are explicitly checked against their local types,
4. the context remains open without a local umbrella class,
5. optional date boundaries and their ordering are checked correctly,
6. the composite key works within the validation graph,
7. external role Schemes remain permitted in the core,
8. the minimal role vocabulary is versioned separately from the T-Box,
9. no Agent, context, activity, Membership, or provenance semantics are duplicated,
10. all positive and negative scenarios are checked automatically.

## 22. Domain Approval Decision

Before creating the `.ttl` artifacts, the following were explicitly confirmed on the basis of this document:

1. Participation, Agent, and role value must be IRIs; only context may also be a blank node.
2. A role value must explicitly be `conx-part:Role`; `skos:Concept` alone is insufficient.
3. The Core Shape remains open to roles outside the minimal Participation Scheme.
4. The uniqueness rule applies across the complete jointly validated data graph and ignores start and end dates.
5. All requirements use `sh:Violation`; recommendations are not included as warnings in the Core Shape.