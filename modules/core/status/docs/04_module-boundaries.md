# Status Module Boundaries

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Responsibility

Status owns the meaning of a status assignment, its optional navigation,
and the three SKOS-based concept classes. It does not define deliveries,
projects, goods, measurement definitions or actors.

## 2. Dependencies

| Dependency | Use |
| --- | --- |
| Agent Core 0.1.0 | Type of the optional reportedBy actor |
| Person / Organization Core 0.1.0 (optional context) | Establish that a specifically typed reporting actor is an Agent |
| VSO Core 0.1.0 | AssignedProperty, PropertyState and their existing rules |
| VSO/ISOProps profile 0.1.0 | ISOProps v2.2 definition metadata, datatype and unit validation |
| SKOS | Concept types, labeling and vocabulary organization |
| Three status vocabularies 0.1.0 | Initial concepts and explicit compatibility links |

Dependencies are referenced or loaded for validation, not silently downloaded
through owl:imports. The runtime bundle uses local pinned versions.
The T-Box has no dependency on a domain ontology.

The default Status bundle includes Agent. For a reporter typed only as
conx-person:Person or conx-org:Organization, supply the respective existing
Core ontology through an additional `--data` argument or the Python API's
`additional_ontology`. These optional contexts are documented in the
[reporting actor examples](../examples/reporting-actors/README.md). The examples
do not duplicate class hierarchies or assert an extra Agent type.

## 3. Existing Document Status

Document's documentStatus links directly to a document-status concept.
Status Core's hasStatus links to a qualified assignment. They are not
equivalent properties. This release leaves the Document module unchanged.
A later integration must decide how their reported states remain consistent.

## 4. Validation Boundaries

Own vocabulary publication requirements apply to the three Construct-X status
vocabulary namespaces. External kinds, values and reasons require appropriate
types and value compatibility, but need not adopt our labels, codes or schemes.

The VSO/ISOProps rules apply to resources reached through hasCondition.
Global dependency targets are omitted only from the in-memory Status bundle;
the original source shapes remain unchanged. Unrelated VSO assignments in the
same graph are not automatically subjected to ISOProps rules.

Current-status validation is limited to the known history in the supplied
graph, grouped by object and kind. It cannot establish that external systems
have no newer reports. Applications maintain the optional link; validation
neither selects a status automatically nor activates scheduled future states.

Loading an actor ontology establishes its class hierarchy; it does not
automatically run that module's shapes. Status checks the reporter's Agent
type, IRI and multiplicity. Full Person or Organization data validation is
a separate composition with those Core shapes and their dependencies.

## 5. Example

A delivery's status can reference a temperature measurement owned by its goods.
Adding hasProperty from the delivery to that same measurement would create a
second VSO owner and fail. The status uses hasCondition instead.
