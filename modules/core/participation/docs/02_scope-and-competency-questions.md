# Scope and Competency Questions of the Participation Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** `core/participation`

## 1. Purpose

The Participation module describes an Agent's contextual role assignment that currently holds or held historically. It answers which Agent has or had which role in which domain context.

The module describes no activities or events and does not assert that the Agent performed a particular action. The Agent's master data and the semantics of the context remain in their responsible modules.

## 2. Confirmed Scope

| Area | MVP Decision |
| --- | --- |
| Central class | `Participation`, with the German label Beteiligung |
| Meaning | Qualified role assignment that currently holds or held historically; no planning, possibility, or activity participation |
| Agent | Exactly one `core/agent:Agent` per Participation |
| Role | Exactly one value of the local class `Role`; no unqualified Participation |
| Context | Exactly one domain resource; no local umbrella type for contexts |
| Navigation from context | `hasParticipation` optionally provides the reverse direction of `hasContext`; domain modules may define role-specific subproperties |
| Uniqueness | Exactly one Participation per Agent/role/context combination in domain terms |
| Time | Start and end dates are optional and describe only assignment validity |
| Role class | Local `Role` as a subclass of `skos:Concept` |
| Role values | Individuals only, not role classes |
| Concept Schemes | No universal requirement; Construct-X-maintained role vocabularies use SKOS Concept Schemes |
| Initial vocabulary | A minimal, separately maintained role vocabulary is included in the MVP |
| Membership | Remains an independent concept of `core/organization` |
| Alignments | No external equivalence assertions or alignment axioms in the MVP |
| Shortcut relationships | No role-specific direct properties in the core |
| Origin, evidence, and status | Outside the module and not planned as future Participation extensions |

## 3. Domain Target Model

The following representation uses the property names and public IRIs established in the term catalog.

| Resource | Property | Requirement |
| --- | --- | --- |
| `Participation` | `hasParticipant` | Exactly one Agent |
| `Participation` | `hasRole` | Exactly one Role |
| `Participation` | `hasContext` | Exactly one domain resource |
| `Participation` | `startDate` | Optional, at most one date |
| `Participation` | `endDate` | Optional, at most one date |

A `Participation` is always qualified. A statement such as “Agent A is somehow involved in context X” is insufficient for a valid Participation.

## 4. Modeling Principles

### 4.1 Agent, Role, and Context Remain Separate

The Agent remains the same Person or Organization regardless of its roles. A role is not modeled as a subclass of the Agent.

| Agent | Participation | Role | Context |
| --- | --- | --- | --- |
| Organization A | Participation 1 | Contractor | Project X |
| Organization A | Participation 2 | Supplier | Contract Y |

Organization A therefore becomes neither a class `ContractorOrganization` nor a second Organization instance.

### 4.2 One Participation Represents Exactly One Combination

An instance links exactly one Agent, exactly one role, and exactly one context. Multiple Agents, roles, or contexts are not grouped in one Participation.

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| Participation 1 | Agent A | Contractor | Project X |
| Participation 2 | Agent B | Contractor | Project X |
| Participation 3 | Agent A | Supplier | Project X |

This pattern avoids ambiguity and allows every assignment to be referenced and validated individually.

### 4.3 Roles Are Individuals

The local class `Role` classifies all role values suitable for Participation:

```turtle
Role rdfs:subClassOf skos:Concept .
role:example-role rdf:type Role .
```

Specific role values are maintained as individuals in separate vocabularies. Role classes following the ePO pattern are excluded from the local core model.

### 4.4 Context Remains Open in Domain Terms

A context may, for example, be a contract, document, project, delivery note, product, or another domain resource. These resources currently have no necessary common core superclass.

The Participation module therefore introduces no class `Context` or `ParticipationContext`. Each domain profile may restrict the context types it permits.

### 4.5 Dates Describe Validity

Start and end dates are optional. When present, they specify from when or until when the role assignment applies.

Example:

```text
Person A + Project Manager + Project X
  startDate = 2026-01-01
  endDate   = 2026-06-30
```

These dates do not describe activity duration. A Participation may have only one start and one end date. If both are present, the end date must not precede the start date.

## 5. Competency Questions

### PCQ-01: Which Agent has which role in a context?

A `Participation` links exactly one existing Agent to exactly one role and exactly one context.

Conceptual example:

```text
Participation P1
  participant = Organization A
  role        = Contractor
  context     = Project X
```

The Participation asserts that this assignment currently holds or held during the specified period.

### PCQ-02: Can a Person or Organization have multiple roles in the same context?

Yes. A separate Participation is used for each role.

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| P1 | Organization A | Contractor | Project X |
| P2 | Organization A | Supplier | Project X |

This makes it unambiguous which additional information belongs to which role.

### PCQ-03: Can multiple Agents have the same role in the same context?

Yes. Each Agent receives a separate Participation.

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| P1 | Organization A | Designer | Project X |
| P2 | Organization B | Designer | Project X |

Alternatively, a consortium acting jointly and itself modeled as an Organization may be referenced as one Agent.

### PCQ-04: Is involvement without a known role permitted?

No. The module describes only qualified involvement. A Participation without a role does not specify the Agent's function in the context and is invalid in the core profile.

A generic fallback value such as `unknown` or `unspecified` is not provided in the MVP. If no role value is available, no Participation is created.

### PCQ-05: Can one Participation group multiple contexts?

No. If an Agent and role apply to multiple contexts, a separate Participation is used for each context.

| Participation | Agent | Role | Context |
| --- | --- | --- | --- |
| P1 | Organization A | Contractor | Contract X |
| P2 | Organization A | Contractor | Contract Y |

This avoids ambiguous combinations of multiple roles and contexts.

### PCQ-06: Can the same combination occur multiple times?

Exactly one Participation exists per Agent/role/context combination in domain terms.

```text
Agent A + Contractor + Project X = exactly one Participation
```

Optional start and end dates belong to this assignment. Multiple separate validity periods for the same combination are not supported in the MVP. A future need for interrupted or recurring assignments would require a new domain decision.

### PCQ-07: How is temporal validity described?

A Participation may optionally have a start date, an end date, or both:

- Start date only: the assignment applies from this date; no end is specified.
- End date only: the assignment applied until this date; no beginning is specified.
- Start and end dates: the assignment applies within the specified period.
- No date: the assignment exists without its temporal boundaries being expressed.

The specific property names and datatype are established in the term catalog. The MVP uses a simple complete calendar date as `xsd:date`.

### PCQ-08: How are roles defined and maintained?

`Role` is a local subclass of `skos:Concept`. Specific roles are individuals. Construct-X-maintained role lists are provided as versioned SKOS Concept Schemes outside the Participation T-Box.

The T-Box does not require Scheme membership for every role value. External values explicitly classified as the local `Role` may therefore also be used in domain profiles.

### PCQ-09: Which role vocabulary is included in the MVP?

The MVP includes a small, separately versioned role vocabulary. It should contain several specific roles so that data examples, shapes, and queries can realistically demonstrate the Participation pattern.

The specific initial roles are established in the term catalog. The Participation module itself defines no universal role list and does not indiscriminately mix construction, contract, delivery, and document roles in its T-Box.

`LocationRole` follows a comparable pattern for controlled role values, but is not a Participation role vocabulary: it classifies an address's function within a location assignment rather than an Agent's role.

### PCQ-10: Is organizational membership a Participation?

Not in the MVP. `core/organization:Membership` describes an Agent's affiliation with an Organization and currently requires no role value. A `Participation`, by contrast, always requires exactly one role.

The concepts therefore remain independent. The Participation module does not change existing Membership.

### PCQ-11: Does a Participation assert execution of an activity?

No. For example, holding the role `Contractor` in a project does not assert that specific construction work has already been performed.

Activities, events, and their actual participants will be described in another ontology later.

### PCQ-12: Are role-specific shortcut relationships generated?

No. The combination:

```text
Organization A + Seller + Contract X
```

does not generate an additional core property statement such as `Organization A isSellerOf Contract X`. The role remains an individual on the Participation, and the qualified relationship is the sole authoritative representation.

The optional navigation `Context hasParticipation Participation` and its domain-specific subproperties instead point to the existing Participation rather than directly to the Agent. Role and context remain explicit there.

### PCQ-13: How are origin, evidence, or status described?

They are not described in the Participation module. An existing Participation asserts an assignment that currently holds or held historically. Status values such as planned, proposed, or revoked do not fit this meaning.

Provenance, evidence, permissions, and powers of attorney are independent domain topics and are not earmarked as future extensions of this module.

## 6. Explicitly Outside the Participation Core

- Activities, events, and process flows,
- actual execution of individual actions,
- planned, proposed, or possible role assignments,
- unqualified involvement without a role,
- personal, organizational, contact, and address master data,
- organizational memberships, posts, and employment models,
- legal representation, power of attorney, and signing authority,
- technical roles, user accounts, and access permissions,
- RACI matrices and detailed responsibility models,
- origin, evidence, status, and provenance of a role assignment,
- contract, project, document, and delivery semantics,
- dedicated time intervals or a general temporal ontology,
- role-specific direct shortcut properties,
- external alignment axioms with ORG, PROV-O, DCAT, ePO, IFC, Schema.org, or PRO.

## 7. Module Boundaries

| Module or Artifact | Responsibility in the Integrated Model |
| --- | --- |
| `core/agent` | Provides the common class for the exactly one participating Agent |
| `core/person` | Describes personal master data; a Person may be a participant |
| `core/organization` | Describes Organizations and Membership; an Organization may be a participant or context |
| `core/document` | Provides document semantics; a Document may be a role assignment's context |
| Domain modules | Define permitted context types and use appropriate role vocabularies |
| Role vocabulary | Provides specific role individuals separately from the Participation T-Box |
| Future activity ontology | Describes activities, events, and actual activity participation |

## 8. Core Validation Requirements

The implemented Core SHACL Profile checks:

- exactly one Agent per `Participation`,
- exactly one role value per `Participation`,
- exactly one context per `Participation`,
- explicit typing of the Agent as `core/agent:Agent`,
- explicit typing of the role value as the local `Role`,
- at most one start and one end date,
- complete date values using the specified datatype,
- an end date that does not precede the start date,
- domain-level uniqueness of the Agent/role/context combination,
- use of the approved values of the minimal role vocabulary where the corresponding closed profile applies.

The T-Box itself should not carry mandatory fields or uniqueness rules as OWL cardinalities. These requirements are implemented in the Core SHACL Profile.

## 9. Acceptance Criteria for Modeling Approval

The [Implemented Term Catalog](05_term-catalog.md) and [Domain Conceptual Model](03_concept-model.md) could be created because:

1. the meaning and name of the central class are confirmed,
2. Agent, role, and context each occur exactly once,
3. unqualified involvement is excluded,
4. roles are modeled as individuals of a local `Role`,
5. context typing remains open,
6. temporal validity is implemented optionally through start and end dates,
7. Membership, activities, provenance, and permissions are distinguished,
8. external alignments and direct role properties are outside the MVP,
9. a minimal role vocabulary is established as a separate MVP artifact.

The public terms, property names, date datatypes, and initial role vocabulary are confirmed. Further roles are derived only from the sources and competency questions of the responsible domain module. The [Module Boundaries](04_module-boundaries.md), [SHACL Requirements Document](06_shacl-requirements.md), T-Box, role vocabulary 0.1.0, and [Core Shapes](07_core-shapes.md) 0.3.0 are implemented.

## 10. Illustrative Example

> An Organization may be both Supplier and Contractor in the same context. Two Participation resources with different roles are used rather than combining both meanings in an ambiguous statement.