# Source Analysis for the Participation Module

**Status:** Consolidated analysis baseline  
**Version:** 0.2.0  
**As of:** 7 October 2026  
**Research cutoff date:** 27 August 2026  
**Scope:** `core/participation`  
**Implementation status:** T-Box and Core Shapes 0.2.0; role vocabulary unchanged at 0.1.0

## 1. Purpose and Method

This analysis examines existing ontologies, standards, and ontology design patterns as the domain foundation for the implemented Construct-X Participation module. Its central question is how to express an Agent's context-dependent involvement in a particular role.

The analysis focuses on:

- separation of Agent, role, role assignment, and context,
- n-ary relationships in RDF and OWL,
- roles of people and organizations in transactions and in relation to resources,
- organizational memberships,
- roles in activities and provenance relationships,
- temporal validity,
- controlled role values,
- suitability for direct reuse or as an alignment target,
- boundaries with existing Construct-X core modules.

The analysis uses only existing core decisions and external primary sources. Unfinished domain modules are not used as modeling foundations. The analysis itself is not a normative ontology specification. Classes, property names, definitions, and public IRIs are established in the term catalog and T-Box.

## 2. Summary of Findings

None of the evaluated ontologies alone adequately covers the cross-domain Construct-X scope:

- [W3C ORG](https://www.w3.org/TR/vocab-org/) provides a strong n-ary role and membership pattern, but is restricted to organizations.
- [PROV-O](https://www.w3.org/TR/prov-o/) qualifies an Agent's responsibility for an activity or entity, but deliberately carries provenance semantics.
- [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) extends the qualified PROV pattern for Agent roles in relation to resources, but remains a data catalog vocabulary.
- [ePO 5.2.0](https://docs.ted.europa.eu/EPO/latest/release-notes.html) uses an `AgentInRole` pattern comprising an Agent, role instance, and situational procurement context. Individual roles are modeled as a class hierarchy and are procurement-specific.
- [IFC 4.3](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssignsToActor.htm) provides `IfcRelAssignsToActor`, an objectified assignment between an actor, an optional role, and one or more objects. This is particularly relevant to construction, but is tied to the IFC object model and its role enumeration.

The strongest common foundation is therefore a combination rather than a single imported model:

1. The [W3C pattern for n-ary relationships](https://www.w3.org/TR/swbp-n-aryRelations/) as the structural foundation,
2. W3C ORG, ePO, IFC, PROV-O, and DCAT as documented application variants,
3. `core/agent` for the participating Agent,
4. SKOS for separately maintained controlled role concepts,
5. optionally OWL-Time for future temporal qualification.

Construct-X uses the central class `Participation` for this pattern. It describes a qualified assignment that currently holds or held historically, linking exactly one Agent to exactly one role in exactly one domain context. Optional start and end dates may bound the validity of this assignment. The class does not describe participation in activities or events.

## 3. Sources Evaluated

| Source | Version Used | Role in the Analysis | Provisional Use |
| --- | --- | --- | --- |
| [W3C N-ary Relations](https://www.w3.org/TR/swbp-n-aryRelations/) | Working Group Note, 12 April 2006 | General RDF/OWL design pattern for relationships with more than two arguments | Primary structural foundation |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 16 January 2014 | Membership between Agent, Organization, and role; optional temporal information | Reference for role assignment and distinction from organizational membership |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation, 30 April 2013 | Qualified Agent relationships to activities and entities | Alignment and specialization source for provenance cases |
| [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | W3C Recommendation, 22 August 2024 | Role-qualified attribution of an Agent to a resource | Reference for resource-related responsibility |
| [W3C SKOS](https://www.w3.org/TR/skos-reference/) | W3C Recommendation, 18 August 2009 | Controlled, hierarchical role concepts | Preferred foundation for role vocabularies |
| [W3C OWL-Time](https://www.w3.org/TR/owl-time/) | W3C Recommendation of 2017 with subsequently maintained draft | Instants, intervals, duration, and temporal relationships | Candidate for optional temporal qualification |
| [EU eProcurement Ontology](https://docs.ted.europa.eu/EPO/latest/business.html) | ePO 5.2.0, 10 October 2025 | `AgentInRole`, `playedBy`, and situational procurement context | Primary EU reference for contextual process roles |
| [buildingSMART IFC](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssignsToActor.htm) | IFC 4.3 documentation | Objectified assignment of an actor and role to IFC objects | Primary AEC mapping and requirements source |
| [Schema.org Role](https://schema.org/Role) | Schema.org V30.0, accessed 2026-08-27 | General wrapper for qualifying existing relationships | Broad web interoperability source |
| [SPAR PRO](https://sparontologies.github.io/pro/current/pro.html) | Current published documentation, accessed 2026-08-27 | Agent, role, context, and time as `RoleInTime` | Reference for an explicit role- and time-based model |
| [Participation Schema](https://vocab.org/participation/) | 25 September 2008 | Simple role model for people in groups | Historical comparative source, not recommended as the core |

The following existing Construct-X decisions were also evaluated:

- [Agent Specification](../../agent/docs/10_agent-specification.md)
- [Organization Source Analysis](../../organization/docs/01_source-analysis.md)
- [Organization Conceptual Model](../../organization/docs/03_concept-model.md)
- [Organization Scope and Competency Questions](../../organization/docs/02_scope-and-competency-questions.md)

## 4. Basic Domain Concepts

### 4.1 Agent

An Agent is the entity that acts, bears responsibility, or is referenced as a participant in a context. Construct-X already provides `core/agent` for this purpose. People and organizations are integrated as specific Agent types.

The Participation module should not introduce a second Person, Organization, or Actor hierarchy. In particular, a contextual seller, contractor, or designer is an existing Agent in a particular role, rather than a new master data type.

### 4.2 Role

A role describes the function in which an Agent acts in relation to a context. It must be separated from the Agent's identity and intrinsic type.

Example:

- Organization A is an `Organization` as a master data object.
- It acts as a seller in context X.
- It acts as a recipient in context Y.

W3C ORG and DCAT model roles as subclasses of `skos:Concept`. This approach is particularly suitable for Construct-X because roles can:

- receive stable IRIs,
- have multilingual labels and definitions,
- be organized in Concept Schemes,
- be connected hierarchically or through mappings,
- be versioned outside the Participation T-Box.

The role values themselves should therefore not be embedded as a complete list in the Participation T-Box. Roles such as seller, recipient, designer, contractor, or data publisher belong in controlled domain vocabularies or profiles.

### 4.3 Role Assignment

A role assignment is the separate relationship resource that keeps together at least Agent, role, and context. It is not identical to the abstract role concept.

| Component | Target |
| --- | --- |
| Agent | Existing Agent |
| Role | Controlled role concept |
| Context | Resource to which the role applies |

A role assignment instance may carry additional information where required, such as a validity period, status, identifier, or evidence. This is the main reason for objectifying the relationship.

### 4.4 Participation and Actual Execution

The name `Participation` is semantically broader than a role assignment. In foundational participation patterns, participation often means that an object or Agent actually participates in an event or process. A role assignment, by contrast, may express an intended, contractual, organizational, or documented function without asserting that an action has already occurred.

Examples:

- Appointment as a contractor is a contextual role.
- Performing specific work is activity participation.
- Attribution as the author of a document is an attribution.
- Membership in an association is an organizational relationship.

These statements must not automatically be equated. The subsequent specification must therefore establish whether the module owns only role assignments or also actual event participation.

## 5. W3C Pattern for N-ary Relationships

RDF properties represent binary relationships. A statement involving Agent, role, and context requires at least three domain arguments. Once period, status, or origin of the assignment is also required, a direct property such as `hasSeller` is insufficient.

For such cases, the W3C Working Group Note recommends a dedicated class for the relationship and a binary property for each argument. It explicitly distinguishes this approach from RDF reification: the subject being described is a relationship instance, rather than an RDF statement represented as `rdf:Statement`.

For Construct-X, the structural foundation is a separate Assignment resource connecting context, Agent, and role.

Advantages:

- Agent, role, and context remain separately addressable.
- Multiple roles of the same Agent in the same context are possible.
- The same Agent may have different roles in different contexts.
- Time, status, identifier, and evidence may be added to the relationship.
- Domain modules need not create person- or organization-specific role classes.

The W3C Note provides the pattern, but no domain-specific names, role values, or Construct-X cardinalities.

## 6. W3C Organization Ontology

### 6.1 Pattern

W3C ORG models `org:Membership` as an n-ary relationship between:

- exactly one `foaf:Agent` through `org:member`,
- exactly one `org:Organization` through `org:organization`,
- optionally one or more `org:Role` resources through `org:role`,
- optionally a period through `org:memberDuring`.

`org:Role` is a subclass of `skos:Concept`. ORG separates the abstract role value from the specific membership instance. A direct `org:memberOf` statement can be derived from the complete relationship.

### 6.2 Strengths

- Established and normatively published n-ary pattern,
- clear separation of Agent, role, and relationship instance,
- support for controlled role taxonomies using SKOS,
- optional temporal qualification,
- a direct shortcut relationship can be derived without requiring a second authoritative representation.

### 6.3 Limitations

`org:Membership` requires an Organization as its context. It is not directly suitable for documents, contracts, deliveries, projects, products, activities, or arbitrary other domain resources.

Construct-X also already has a `Membership` in the Organization module. This describes organizational affiliation and must not silently be redefined as a more general process-role assignment.

### 6.4 Assessment

W3C ORG is the strongest source for the internal structure and distinction between role value and role instance. It is not a suitable direct superclass for all Participation cases. Future alignment of Construct-X `Membership` with a general Participation pattern is conceivable, but must be decided separately and checked for inference implications.

## 7. PROV-O and DCAT

### 7.1 PROV-O `Association`

PROV-O uses `prov:Association` to describe assigning an Agent responsibility for an activity. Its qualified pattern is:

| Resource | Property | Target |
| --- | --- | --- |
| `prov:Activity` | `prov:qualifiedAssociation` | `prov:Association` |
| `prov:Association` | `prov:agent` | `prov:Agent` |
| `prov:Association` | `prov:hadRole` | `prov:Role` |
| `prov:Association` | `prov:hadPlan` | `prov:Plan`, optional |

Structurally, this is very close to the implemented Participation pattern. Semantically, however, it concerns an activity and provenance, influence, and responsibility.

### 7.2 PROV-O `Attribution`

`prov:Attribution` attributes a `prov:Entity` to an Agent. The relationship is particularly useful when a generating activity is unknown or irrelevant. It is suitable for authorship, creation, or other provenance-related attributions of responsibility.

These semantics are also narrower than an arbitrary business or project role. Being a seller, recipient, or contact person does not by itself constitute provenance attribution.

### 7.3 DCAT `qualifiedAttribution`

DCAT 3 uses `prov:qualifiedAttribution` and `prov:Attribution`, but adds `dcat:hadRole` because `prov:hadRole` is oriented towards roles in relation to activities. DCAT defines `dcat:Role` as a `skos:Concept` and recommends controlled role values.

DCAT therefore supports two important points:

1. The qualified relationship pattern is also useful for Agent roles in relation to resources.
2. An existing qualified relationship should not be reused when its domain semantics and domain/range axioms do not fit.

### 7.4 Assessment

PROV-O and DCAT are valuable alignment and specialization targets:

- Activity-related Participation may later be aligned with `prov:Association`.
- Resource-related authorship or responsibility may be aligned with `prov:Attribution` or the DCAT pattern.

A generic Construct-X role assignment should nevertheless not universally be typed as PROV influence or attribution. This would introduce unintended provenance statements.

## 8. EU eProcurement Ontology

### 8.1 Pattern

ePO 5.2.0 defines `epo:AgentInRole` as a relative concept connecting an Agent with its function in a situational context. Its core relationships are:

- `epo:playedBy` to exactly one `foaf:Agent`,
- `epo:contextualisedBy` to a procurement object or Procurement Element.

Roles such as `AcquiringParty`, `OfferingParty`, `Buyer`, `Contractor`, or `Winner` are modeled as classes in a specialization hierarchy of `epo:AgentInRole`. The role instance therefore carries its role type through `rdf:type`.

### 8.2 Strengths

- Clear separation of Agent master data and situational function,
- the same Agent may have multiple roles,
- context is an explicit component of the role statement,
- practical use in European procurement processes,
- direct domain relevance to business roles such as Buyer, Contractor, and Offering Party.

### 8.3 Limitations

- Roles are modeled as OWL classes rather than values from a controlled role vocabulary.
- The class hierarchy is tailored to public procurement.
- Context is tied to ePO Procurement Elements.
- Direct adoption would introduce ePO semantics and dependencies into the Construct-X core.

### 8.4 Assessment

ePO is the most important reference for the domain concept “Agent in a role within a context.” Its structural principle should be adopted. The specific procurement hierarchy and modeling of each role as a class should not be adopted uncritically in a cross-domain Construct-X core.

## 9. buildingSMART IFC

### 9.1 `IfcRelAssignsToActor`

IFC uses an objectified relationship to assign exactly one `IfcActor` to one or more `IfcObjectDefinition` objects. `ActingRole` may specify the actor's role within that particular assignment. The IFC documentation specifically mentions responsibility for Controls, Groups, Products, Processes, and Resources.

IFC therefore structurally covers:

| Resource | Property | Target |
| --- | --- | --- |
| `IfcRelAssignsToActor` | `RelatingActor` | Exactly one `IfcActor` |
| `IfcRelAssignsToActor` | `ActingRole` | Optionally one `IfcActorRole` |
| `IfcRelAssignsToActor` | `RelatedObjects` | At least one `IfcObjectDefinition` |

### 9.2 `IfcActorRole`

`IfcActorRole` describes a role performed by a person, organization, or person within an organization. `IfcRoleEnum` includes Architect, Client, Contractor, Engineer, Manufacturer, Project Manager, Subcontractor, and Supplier. The IFC documentation itself states that such a list can never be complete and therefore provides `USERDEFINED` plus free text.

### 9.3 Strengths

- Established AEC source with high relevance to Construct-X,
- objectified, referenceable assignment,
- role explicitly applies within the respective object assignment,
- an actor may play different roles in relation to different objects,
- existing IFC roles provide future mapping candidates.

### 9.4 Limitations

- `IfcActor` and `IfcObjectDefinition` belong to the IFC schema and are not the general Construct-X Agent or context concepts.
- A relationship may group multiple Related Objects. Without additional rules, it is therefore unclear whether assignment metadata applies identically to each object.
- `ActingRole` is optional.
- `IfcRoleEnum` is a closed enumeration with a `USERDEFINED` escape mechanism and therefore insufficient as the foundation of an extensible Linked Data role vocabulary.
- Temporal validity is outside this core pattern.

### 9.5 Assessment

IFC is a primary mapping and requirements source, but unsuitable as a direct import for the core module. A robust mapping will later require a decision on whether an IFC assignment to multiple objects is represented as one Participation instance or several individual context assignments.

## 10. Other Comparative Models

### 10.1 Schema.org `Role`

Schema.org uses `Role` as a wrapper to extend an existing property relationship with `roleName`, `startDate`, `endDate`, or other information. The wrapper is integrated through the same domain property, such as `member`, `actor`, or `alumniOf`.

The pattern is flexible and widely used for web markup. However, it is too permissive for a quality-assured core:

- `roleName` allows text or a URL rather than a clearly controlled concept,
- semantics depend on the enclosing property,
- no uniform properties exist for Agent and context,
- the same information may be structured differently depending on the property.

Schema.org is therefore an alignment and mapping target rather than the preferred core structure.

### 10.2 SPAR PRO `RoleInTime`

The Publishing Roles Ontology models a `RoleInTime` situation with:

- exactly one Agent holding the role,
- a role value,
- at least one contextual entity,
- optionally a time interval.

Although PRO focuses on publishing roles, this pattern is very close to the implemented Construct-X requirement. The explicit distinction between `Role` and `RoleInTime` and the generic context reference are particularly valuable.

Direct reuse is discouraged by its connection to the SPAR ontology family, multiple imported ontology design patterns, and overall publishing-specific semantics. PRO is a strong design reference and a possible alignment target for document roles.

### 10.3 Participation Schema

The Participation Schema of 2008 describes roles held by people in groups, including a holder and start and end dates. It is simple, but restricted to groups, uses global domain/range declarations, and has no documented newer version since 2008.

It is therefore considered only a historical comparative source. W3C ORG and newer qualified patterns are more robust in domain and governance terms.

## 11. Pattern Comparison

| Model | Relationship Resource | Agent | Role | Context | Time | Main Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| W3C ORG Membership | Yes | Exactly one Agent | Optional SKOS-based role value | Exactly one Organization | Optional interval | Organizational membership only |
| PROV Association | Yes | Agent | `prov:Role` | Activity | Extensible through qualified PROV structures | Asserts activity responsibility/provenance |
| PROV/DCAT Attribution | Yes | Agent | `dcat:Role` as a SKOS Concept | PROV Entity / DCAT Resource | Extensible on the relationship node | Attribution rather than arbitrary involvement |
| ePO AgentInRole | Yes | Exactly one Agent | Role class as the instance type | Procurement Element | Not central to the pattern | Procurement-specific class hierarchy |
| IFC RelAssignsToActor | Yes | Exactly one IfcActor | Optionally one IfcActorRole | One or more IFC objects | Not central to the pattern | IFC schema and enumeration |
| Schema.org Role | Yes, as a wrapper | Property-dependent | Text or URL | Property-dependent | Start/end date | Too permissive and structurally inconsistent |
| SPAR PRO RoleInTime | Yes | Exactly one Agent | Role individual | At least one entity | Optional interval | Publishing scope and import depth |

## 12. Confirmed Architectural Implications

The following points are supported by the sources and confirmed for the MVP. Specific local properties and IRIs are established only in the term catalog.

### 12.1 Local Relationship Resource

A local qualified relationship pattern is more appropriate than direct properties such as `hasSeller`, `hasBuyer`, `hasPlanner`, or `hasContractor`. Role-specific shortcut relationships are excluded from the core module. Roles remain individually referenceable values of `Participation`.

A local resource also prevents Construct-X from asserting that every role assignment is an organizational membership, provenance attribution, activity association, or IFC assignment.

### 12.2 Reuse of `core/agent`

The participating actor should reference `conx-agent:Agent`. This permits people and organizations without duplicating their master data or types in the Participation module.

Whether further Agent types are permitted later remains a matter for the open Agent hierarchy. The Participation module should not define a closed union of Person and Organization.

### 12.3 Separate Role Vocabularies

The T-Box receives a local class `Role` as a subclass of `skos:Concept`. Specific roles are modeled as individuals. Construct-X-maintained role vocabularies should be provided as separately versioned SKOS Concept Schemes. The T-Box does not, however, require every external role value to belong to a Concept Scheme.

The MVP includes a minimal Construct-X role vocabulary demonstrating the Participation pattern with specific roles. The appropriate initial scope is established in the term catalog rather than derived from the T-Box.

### 12.4 Context Remains External

The domain context is not owned by the Participation module. It may, for example, be a document, contract, project, process, product, asset, or another domain resource.

A global OWL domain for the context side would therefore be problematic. The T-Box should not introduce a general local `Context` umbrella type solely for this property unless it has independent semantics.

### 12.5 One Assignment per Agent, Role, and Context

ORG, PRO, ePO, and IFC support the selected n-ary pattern. The Construct-X core requires:

- exactly one assigned Agent,
- exactly one role value,
- exactly one domain context.

Unqualified involvement without a role is not permitted. If an Agent requires multiple roles, or roles apply to multiple contexts, a separate `Participation` is used for each combination. From a domain perspective, exactly one `Participation` exists per combination of Agent, role, and context.

### 12.6 Temporal Validity

A `Participation` may optionally have a start date and an end date. Both values bound only the temporal validity of the role assignment. They describe neither the duration nor the beginning or end of an activity.

The MVP uses simple date values rather than a separate interval object. A general temporal model or OWL-Time is not incorporated into the Participation module. The Core SHACL Profile allows at most one value per date and checks consistent ordering when both are present.

### 12.7 No Equivalence with Authorization or Responsibility

A role value may designate a function, but does not automatically assert:

- technical access authorization,
- a legally effective power of attorney,
- a contractual obligation,
- execution of an activity,
- authorship or provenance,
- liability or definitive responsibility.

Such meanings require other domain models. Origin, evidence, status, authorization, and provenance information are also not earmarked as future extensions of the Participation module.

## 13. Boundaries with Existing Core Modules

| Module | Retained Responsibility | Relationship to Participation |
| --- | --- | --- |
| `core/agent` | Common superclass for participating people and organizations | Participation references the Agent |
| `core/person` | Personal master data | A Person may be the Agent in a role assignment |
| `core/organization` | Organizations, membership, hierarchy, and legal representation | An Organization may be an Agent or organizational context; Membership initially remains a separate organizational concept |
| `core/contact` | Contact points, methods, usage, and purpose | Contact roles and business roles must not be conflated |
| `core/address` | Addresses and location assignments | No role or context semantics are derived in the Participation module |
| `core/document` | Documents and document semantics | A Document may provide the context for a role assignment |

The boundary with `core/organization:Membership` is particularly important:

- Membership means affiliation with an Organization.
- A general role assignment means a function in relation to a context.
- A membership may have a role and period, but remains a membership in domain terms.

`Membership` and `Participation` remain independent concepts in the MVP. The existing Organization model does not require a role value for Membership, so it cannot be treated as a specialization of `Participation` without changing its meaning and cardinalities.

## 14. Confirmed MVP Scope

### Within the Participation Core

- The local class `Participation` for an actual contextual role assignment,
- reference to exactly one `core/agent:Agent`,
- reference to exactly one role value of the local class `Role`,
- reference to exactly one domain context,
- domain-level uniqueness of the Agent/role/context combination,
- optional simple start and end dates for assignment validity,
- neutral integration properties from Agent and context to the assignment,
- a minimal, separately maintained role vocabulary with role individuals,
- module metadata and definitions.

### Outside the Participation Core

- Specific role lists for delivery, procurement, projects, construction, or documents,
- personal, organizational, and contact data,
- organizational membership and staffing plans,
- legal representation, power of attorney, and signing authority,
- technical role and permission management,
- RACI matrices and detailed responsibility models,
- activity, process, or event ontologies,
- provenance modeling,
- origin, evidence, and status of the role assignment,
- contract and project modeling,
- a dedicated temporal ontology,
- role-specific direct shortcut relationships,
- external alignment axioms,
- IFC-specific classes or enumerations.

## 15. Confirmed Modeling Decisions

| Topic | MVP Decision |
| --- | --- |
| Meaning | Contextual role assignment only; no participation in activities or events |
| Central class | `Participation`, with the German label Beteiligung |
| Assertion | The instance asserts an assignment that currently holds or held historically, not a plan or possibility |
| Agent | Exactly one `core/agent:Agent` per Participation |
| Qualification | Exactly one role value; no unqualified Participation |
| Context | Exactly one domain context resource; context type remains open |
| Uniqueness | Exactly one Participation per Agent/role/context combination in domain terms |
| Role class | Local `Role` as a subclass of `skos:Concept` |
| Concept Scheme | No universal requirement for every role value; Construct-X vocabularies are maintained as Concept Schemes |
| Role representation | Roles are individuals rather than role classes |
| Initial vocabulary | Separate MVP artifact with `ClientRole`, `ContractorRole`, `SupplierRole`, `ArchitectRole`, and `EngineerRole`; further roles originate in the respective domain modules |
| Time | Optional start and end dates of validity |
| Membership | Remains separate from Participation |
| Alignments | No external equivalence assertions or alignment axioms in the MVP |
| Shortcut relationships | No role-specific direct properties or derivations in the core |
| Origin/evidence/status | Excluded and not planned as an extension of the Participation module |

## 16. Implementation Status and Further Use

The research supports an independent core module because the contextual Agent role cannot be housed neutrally in `core/agent`, Person, Organization, Document, or a single domain module.

Scope, term catalog, conceptual model, module boundaries, and SHACL requirements form the approved domain foundation of version `0.1.0`. The T-Box, minimal role vocabulary, Core SHACL Profile, and positive and negative test cases are implemented. Further roles are derived from the competency questions of the responsible domain module rather than added to the core preemptively.

The strongest starting proposition for this discussion is:

> The Participation module describes a separate qualified relationship in which exactly one existing Agent holds exactly one controlled role in relation to exactly one domain context. It may carry optional start and end dates of validity. The module describes neither the Agent's master data nor the context itself and, without further specialization, asserts no provenance, power of attorney, authorization, or actual activity execution.

## 17. Illustrative Mapping Example

> W3C ORG provides a proven pattern for qualified relationships. Construct-X generalizes this pattern to arbitrary domain contexts without automatically making every Participation an organizational membership.

The decision of 7 October 2026 adds optional `hasParticipation` navigation in Core 0.2.0. The source analysis remains the foundation of the qualified pattern; this navigation is a local modeling decision rather than a new assertion about the external standards evaluated.
