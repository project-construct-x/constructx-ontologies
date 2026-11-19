# Module Boundaries of the Participation Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** `core/participation`

## 1. Purpose

This document assigns Participation concepts to the responsible Construct-X modules. It prevents a general contextual role assignment from simultaneously modeling Agent master data, context semantics, activities, memberships, evidence, or permissions.

The Participation module describes only the statement:

> An Agent holds exactly one role in relation to exactly one context.

The statement may optionally be supplemented by the beginning and end of its validity.

## 2. Guiding Principles

1. `Participation` owns the qualified relationship between Agent, role, and context.
2. Agent, role value, and context retain their domain identities outside the Participation.
3. Roles are modeled as individuals of a local SKOS-based class `Role`.
4. Context typing remains open and is described by its domain module.
5. A Participation asserts an assignment that currently holds or held historically, not a plan or possibility.
6. Participation does not describe participation in activities or events.
7. Relationships with independent domain semantics remain in their original modules.
8. Further roles are derived only during development of the responsible domain module.

## 3. Ownership by Module

| Module or Artifact | Owns | Explicitly Does Not Own |
| --- | --- | --- |
| `core/participation` | `Participation`, `Role`, `hasParticipant`, `hasRole`, `hasContext`, `startDate`, `endDate` | Agent master data, context classes, activities, membership, provenance, permissions |
| `core/agent` | Common class `Agent` | Specific roles and role assignments |
| `core/person` | People and intrinsic personal data | General contextual Agent roles |
| `core/organization` | Organizations, Organizational Units, `Membership`, legal representation | General process, contract, or document roles |
| `core/document` | Documents and document semantics | General Agent role assignments |
| Future activity ontology | Activities, events, and actual participation in them | General resource-related role assignment |
| Domain modules | Their own context types, domain requirements, and domain-specific role vocabularies | Generic Participation pattern |
| `participation-role` | Five general initial roles as reference data | T-Box terms and domain-module-specific role lists |

## 4. Model Core and Relationship Direction

Participation is a separate domain relationship resource:

| Resource | Property | Target |
| --- | --- | --- |
| `Participation` | `hasParticipant` | Agent |
| `Participation` | `hasContext` | Context |
| `Participation` | `hasRole` | Role |

The properties point from the Participation to its three components. Since 0.2.0, `hasParticipation` provides the optional reverse direction from context to Participation instance. `owl:inverseOf hasContext` describes the semantics; the offline SHACL contract still requires an explicit matching `hasContext` back-reference. This creates neither a second role nor a second actor. `isParticipationOf` is not additionally introduced. Domain modules may define role-specific subproperties pointing to Participation, but must not attach contacts or numbers to the property itself.

Role-specific properties such as `isContractorOf`, `hasSeller`, or `hasArchitect` are also not defined in the core. They would require a T-Box change for every new role value and move the role back into a property rather than a controlled value.

## 5. Boundary with Agent

`hasParticipant` references exactly one `conx-agent:Agent`. The Participation module defines neither new Agent types nor a closed selection of Person and Organization.

The following existing types can therefore be used today:

```text
conx-person:Person       rdfs:subClassOf conx-agent:Agent
conx-org:Organization    rdfs:subClassOf conx-agent:Agent
```

Future Agent subclasses are automatically compatible without extending the Participation T-Box. The Agent's names, identifiers, addresses, and contact information remain in their respective modules.

## 6. Context Boundary

The context is the exactly one resource in relation to which the role applies. The Participation module deliberately defines neither `Context` nor a closed superclass for context resources.

Possible contexts include:

- a contract,
- a project,
- a document,
- a product or asset,
- a tender,
- another domain-identified resource.

The module defining the context resource also owns its properties, lifecycle, and validation rules. Use as `hasContext` does not imply new typing of the resource.

A domain profile may restrict context for its use case. For example, a document profile may require a particular document type without transferring this restriction to the general Participation Core Shape.

## 7. Role Class and Role Vocabularies

The Participation T-Box defines only the general class `Role` as a subclass of `skos:Concept`. Specific roles are reference data rather than subclasses of Agent or Participation.

The minimal `participation-role` vocabulary contains only:

- `ClientRole`,
- `ContractorRole`,
- `SupplierRole`,
- `ArchitectRole`,
- `EngineerRole`.

These roles illustrate the general model core. In particular, `ArchitectRole` and `EngineerRole` designate functions within their respective contexts rather than professions or Agent types.

Domain-specific roles are derived from the sources and competency questions of each domain module during its development. Delivery note roles are therefore established only during development of the Delivery Note module. They may belong to a separate SKOS Concept Scheme and become usable with Participation through explicit typing as `conx-part:Role`.

The open core profile does not require membership in the minimal `participation-role` Scheme. A domain profile may, by contrast, require its own approved role Scheme.

## 8. Boundary with Membership

`conx-org:Membership` remains a separate organizational relationship. A Membership asserts that an Agent is a member of an Organization. A Participation more generally asserts that an Agent holds a role in relation to a domain context.

| Concept | Components |
| --- | --- |
| Membership | Agent + Organization |
| Participation | Agent + Role + open context |

Membership is neither made a subclass of Participation nor replaced by Participation in the MVP. Future alignment is possible only if both models are genuinely compatible in cardinalities, temporal information, and role implications.

## 9. Boundary with Activities and Events

A Participation does not state that the Agent performed an activity or attended an event.

> Organization A holds ContractorRole in Contract X.

This statement proves no specific construction work. A future activity ontology may model activities, events, performers, and times while referencing existing Agents or Participations. The corresponding execution semantics will not subsequently be added to Participation.

## 10. Boundary with Documents and Other Domain Modules

A Document may be the context of a Participation. The Document module nevertheless owns document type, version, content, status, and other document semantics.

A domain module may:

- use its resources as contexts,
- provide its own role vocabulary,
- require particular roles and context types,
- formulate additional domain constraints on Participations.

It may reuse the generic model without redefining `Participation`, `hasParticipant`, `hasRole`, or `hasContext`.

## 11. Temporal Validity

`startDate` and `endDate` describe only the validity of the role assignment. They do not describe:

- beginning or end of the context object,
- duration of an activity,
- creation or modification time of the RDF statement,
- publication or processing status.

Missing dates mean only that the respective boundary is unspecified. They imply neither unlimited nor perpetual validity.

## 12. Uniqueness and Identity

Exactly one Participation exists per Agent/role/context combination in domain terms:

```text
(hasParticipant, hasRole, hasContext) -> one Participation
```

Start and end dates do not belong to the uniqueness key. Two Participations with the same Agent, role value, and context therefore remain duplicates even if they have different dates. This consequence is part of the confirmed modeling decision.

The rule is not modeled as `owl:hasKey`. It belongs in the Core SHACL Profile and applies within the data graph validated together in a given run.

## 13. Excluded Semantics

The Participation module neither currently owns nor plans to add:

- planned, requested, or possible roles,
- Participation status,
- origin and provenance of the statement,
- evidence and supporting records,
- powers of attorney and permissions,
- contractual or remuneration terms,
- responsibility for specific activities,
- access control and data protection rules.

Other modules may reference a Participation. This does not make their semantics part of the Participation core.

## 14. T-Box, A-Box, and Shape Separation

### 14.1 Participation T-Box

- `Participation`
- `Role`
- `hasParticipant`
- `hasRole`
- `hasContext`
- `startDate`
- `endDate`

### 14.2 Reference Data

- Minimal Concept Scheme `participation-role`,
- five approved general role individuals,
- future separately versioned role Schemes of domain modules.

### 14.3 Core Shapes

- Minimum and maximum cardinalities,
- resource forms and type requirements,
- date datatype and ordering,
- uniqueness of Agent, role, and context.

The T-Box contains neither a closed role enumeration nor strict OWL cardinalities for these data quality rules.

## 15. Dependency and Alignment Strategy

| Source or Module | MVP Classification |
| --- | --- |
| `core/agent` | Referenced because `hasParticipant` points to `conx-agent:Agent` |
| SKOS | Reused for `Role` and role vocabularies |
| `participation-role` | Separately versioned reference dataset, not embedded in the T-Box |
| Person, Organization, Document, and domain modules | No mandatory imports; used together in data and profiles |
| W3C ORG, PROV-O, DCAT, ePO, IFC, Schema.org, and PRO | Analysis sources and future alignment candidates; no equivalence assertions in the MVP |

Merely referencing external terms does not automatically create an `owl:imports` entry. Actual imports or alignment axioms are introduced only after separate domain review.

## 16. Implementation Status of Module Boundaries

The described module boundaries are implemented in version `0.3.0`:

1. The T-Box references `core/agent` and SKOS without adopting external domain semantics.
2. The minimal role vocabulary is provided separately from the T-Box.
3. The Core SHACL Profile implements approved cardinalities and date rules.
4. Positive and negative test data cover the SHACL contract.
5. Person and Organization are tested as specific Agent subclasses in integration tests.
6. Module and shape documentation and network views are generated.

Further modules may use `Participation` and establish their own domain context types and role vocabularies without extending the core T-Box.

## 17. Illustrative Example

> Participation describes “Anna is the architect in the construction project.” Membership, by contrast, describes “Anna is a member of the architectural practice.” Although both statements involve roles, they belong in different modules.