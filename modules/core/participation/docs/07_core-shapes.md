# Participation Core Shapes

**Status:** Implemented  
**Version:** 0.3.0  
**As of:** 19 November 2026  
**Scope:** Participation Core Shapes

The Participation Core Shapes validate the general, use-case-independent data contracts of the Construct-X Participation Ontology. The T-Box remains semantically open under the open-world assumption; the core profile checks concrete data submissions.

```text
Shape graph: modules/core/participation/shapes/conx-part-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/participation/core
Version IRI: https://www.construct-x.org/shapes/participation/core/0.3.0
Namespace:   https://www.construct-x.org/shapes/participation/core#
Version:     0.3.0
```

## 1. Validated Contracts

- A Participation must be an IRI and explicitly typed as `conx-part:Participation`.
- `hasParticipant`, `hasRole`, and `hasContext` must each occur exactly once.
- `hasParticipant` must be an IRI typed as `conx-agent:Agent` or a known subclass.
- `hasRole` must be an IRI explicitly typed as `conx-part:Role`.
- The core profile accepts roles from other Concept Schemes.
- `hasContext` may be an IRI or blank node; no context type is required.
- `startDate` and `endDate` may each occur at most once as `xsd:date`.
- If both dates are supplied, `startDate` must not be later than `endDate`.
- A second Participation with the same Agent/role/context combination is rejected within the validation graph.

Start and end dates are not part of the uniqueness key. The profile does not use `sh:closed true`; additional properties remain permitted.

`HasParticipationShape` checks subjects of `hasParticipation`. `PART-060` requires complete Participation IRIs; `PART-061` requires the same explicit `hasContext` back-reference. The outgoing edge remains optional. Direct edges to Agents or role values do not follow this pattern.

## 2. Reference Graphs

The following are loaded together for validation:

- `modules/core/agent/ontology/conx-agent.ttl`,
- `modules/core/person/ontology/conx-person.ttl` and `modules/core/organization/ontology/conx-org.ttl` for integration tests of their specific Agent subclasses,
- `modules/core/participation/ontology/conx-part.ttl`,
- `datasets/reference/vocabularies/participation-role/participation-role.ttl` when test or application data uses values from this vocabulary.

The role vocabulary is not a closed core value list. Another domain vocabulary remains valid if its role value is explicitly typed as `conx-part:Role`.

## 3. Uniqueness Check

The combination of `hasParticipant`, `hasRole`, and `hasContext` is checked by a local SHACL-SPARQL constraint. The rule can detect duplicates only across graphs supplied to the same validation run. Data-space or dataset profiles must therefore establish which named graphs are validated together.

## 4. Test Data

Valid test graphs are located in `modules/core/participation/tests/valid`. Targeted error cases are located in `modules/core/participation/tests/invalid`. The automated tests load the required ontology and reference graphs, run PySHACL without inference, and check the stable `PART-*` error codes.

```text
uv run pytest tests/test_participation_shapes.py
```

## 5. Deliberately Excluded Checks

- Specific domain type of the context,
- membership of a role in the minimal Participation Scheme,
- legal or domain evidence supporting the role assignment,
- Agent qualifications or authorization,
- current validity on the validation date,
- activity or event participation,
- Membership, provenance, status, or direct role properties,
- duplicates in graphs not loaded together.

These areas belong in domain profiles, other modules, or external verification services.

## 6. Illustrative Example

> A Participation with Anna as the Agent, Architect as the role, and a construction project as the context is complete. If the role is missing, Anna's function is unclear and the core reports an error.