# Person Core Shapes

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Person Core Shapes

The Person Core Shapes validate the general, use-case-independent data contracts of the Construct-X Person ontology. The T-Box remains semantically open under the open-world assumption; the Core profile, by contrast, checks specific data submissions.

```text
Shape graph: modules/core/person/shapes/conx-person-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/person/core
Version IRI: https://www.construct-x.org/shapes/person/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/person/core#
Version:     0.1.0
```

## 1. Validated Contracts

- Persons are referenced through IRIs and explicitly typed as `conx-person:Person`.
- `fullName` and `givenName` are mandatory and must not be empty.
- Additional name values and `birthPlaceName` are strings or language-tagged strings and must not be empty.
- `birthDate` may occur at most once as a complete `xsd:date`.
- `sex` and `gender` may each occur at most once and use the four approved values from their reference vocabularies.
- `citizenship` references a `conx-addr:Country` IRI from the Construct-X country vocabulary.
- `adms:identifier` remains optional; its values are checked by the imported `identifier/core` shape for the Identifier type, exactly one literal `skos:notation`, and an optional textual `adms:schemaAgency`.
- `hasIdentityEvidence` references an IRI; the evidence’s content, validity, and trust status remain outside the Person profile.

Additional properties remain permitted. The profile does not use `sh:closed true` and requires no RDFS or OWL inference.

## 2. Reference Graphs

The following are loaded together with the data to validate controlled values:

- `datasets/reference/vocabularies/human-sex/human-sex.ttl`,
- `datasets/reference/vocabularies/gender/gender.ttl`,
- `datasets/reference/administrative-territories/iso-3166-1-countries/data/countries.ttl`.

The two small Sex and Gender value sets are additionally recorded as closed `sh:in` lists in the shape graph. Countries are not copied; they are checked through their class and Concept Scheme.

## 3. Test Data

Valid test graphs are located under `modules/core/person/tests/valid`. Targeted error cases are located under `modules/core/person/tests/invalid`. The automated tests load the required reference graphs, run PySHACL without inference, and check error paths and requirement identifiers.

The combined Person and Identifier shapes are validated from the repository root as follows:

```text
uv run pytest tests/test_person_shapes.py -q
```

The test suite loads the imported Identifier shape together with the reference graphs listed above.

## 4. Intentionally Not Checked

- specific Person identifier schemes or a closed list of schemes,
- a finalized machine-readable issuer model,
- internal structure and trustworthiness of identity evidence,
- contact, address, organization, or project relationships,
- general provenance, reification, and access rights.

These areas belong in future domain profiles or separate modules.

## 5. Illustrative Example

> A Person with a full name satisfies the minimal Core contract. An identifier, if present, must additionally have exactly one notation; details of an identity document are not checked here.