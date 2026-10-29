# VSO Review Report

Source file: `modules/core/vso/ontology/conx-vso.ttl`

Review updated: 2026-09-01

## Executive Summary

The VSO 0.1.0 core model is syntactically valid and its previously open modelling questions have been decided. The ontology now has an executable, versioned Core Shape graph, public examples and focused positive and negative tests.

The VSO remains system-neutral. OPM, QUDT and Schema.org are referenced but not imported. ISOProps-specific constraints are implemented in the separate `profiles/construct-x/vso-isoprops` profile.

## Parsed Facts

- Ontology triples: 73
- Shape graph triples: 78
- Ontology IRI: `https://www.construct-x.org/ontology/vso`
- Version IRI: `https://www.construct-x.org/ontology/vso/0.1.0`
- Shape graph IRI: `https://www.construct-x.org/shapes/vso/core`
- Shape version IRI: `https://www.construct-x.org/shapes/vso/core/0.1.0`
- Preferred prefix: `conx-vso`
- `owl:imports`: none
- Ontology A-Box instances: none

## Resolved Modelling Decisions

1. `AssignedProperty` is the concrete assignment associated with one resource. It remains a subclass of `opm:Property`.
2. Every assignment references exactly one property definition by IRI.
3. Every assignment has exactly one `PropertyState`.
4. Every state has exactly one `schema:value`; no additional VSO value property is introduced.
5. Every state may have zero or one unit. A present unit is an IRI typed as `qudt:Unit`.
6. The OPM subclass and subproperty axioms remain in place.
7. The type and vocabulary of a referenced property definition remain open in the Core.
8. ISOProps constraints belong to the separate `profiles/construct-x/vso-isoprops` profile.

## Implemented Validation Contract

The Core Shapes enforce six stable requirements:

- `VSO-LINK-001`: `hasProperty` points to an assignment resource.
- `VSO-ASSIGN-001`: every assignment belongs to exactly one resource.
- `VSO-ASSIGN-010`: every assignment has exactly one IRI property reference.
- `VSO-ASSIGN-020`: every assignment has exactly one property state.
- `VSO-STATE-010`: every state has exactly one `schema:value`.
- `VSO-STATE-020`: a state has at most one IRI-valued `qudt:Unit`.

## Documentation Cleanup

The damaged German encoding, typo, mixed `de-DE` tags and copied `hasPropertyState` documentation were corrected. The unused `isoprops:` prefix and its obsolete lock entry were removed from the VSO Core context.

## Remaining Follow-Up

The following work is deliberately outside the completed Core contract:

- add domain profiles that constrain value datatypes or require units for selected properties,
- confirm the permanent public authority before the first stable release,
- add release metadata such as `dcterms:issued` when version 0.1.0 is published.
