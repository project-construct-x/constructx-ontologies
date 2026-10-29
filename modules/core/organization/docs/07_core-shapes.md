# Organization Core Shapes

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Organization Core Shapes

The Organization Core Shapes validate the general, use-case-independent data contracts of the Construct-X Organization Ontology. The T-Box remains semantically open under the open-world assumption; the core profile checks concrete data submissions.

```text
Shape graph: modules/core/organization/shapes/conx-org-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/organization/core
Version IRI: https://www.construct-x.org/shapes/organization/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/organization/core#
Version:     0.1.0
```

## 1. Validated Contracts

- All five local resource types are referenced through IRIs and appropriately typed.
- Every `Organization` has at least one non-empty name.
- Every `LegalEntity` additionally has a legal name, exactly one registration date as `xsd:date`, at least one structured ADMS identifier, and at least one AddressAssignment with `LegalAddressRole`.
- `legalForm` is optional, occurs at most once, and references a SKOS concept.
- Every `OrganizationalUnit` has at least one `unitOf` relationship.
- Every `Membership` links exactly one Agent to exactly one Organization.
- Every `LegalRepresentation` links exactly one Legal Entity to exactly one Person.
- Direct self-hierarchies, self-assignment of units, and self-memberships are rejected.

Additional properties remain permitted. The profile does not use `sh:closed true`. Inverse hierarchy directions need not be stored redundantly in the data graph.

## 2. Interaction

The Organization Shapes do not take over external data contracts:

- Address Core checks AddressAssignments, roles, and addresses.
- Contact Core checks contact points and the homepage modeled as a website contact.
- Person Core checks included personal data.
- The imported `identifier/core` Shape checks type, exactly one literal `skos:notation`, and an optional textual `adms:schemaAgency`.

The automated tests load these shape and T-Box graphs together and run PySHACL without inference. The Address Role and Contact reference vocabularies are added to the data graph.

## 3. Test Data

Valid test graphs are located in `modules/core/organization/tests/valid`. Targeted error cases are located in `modules/core/organization/tests/invalid`. The eight invalid graphs cover all 36 stable error codes from the [SHACL Requirements Document](06_shacl-requirements.md).

The tests are run from the repository root:

```text
uv run pytest tests/test_organization_ontology.py tests/test_organization_shapes.py -q
```

## 4. Deliberately Excluded Checks

- Closed lists of legally permitted identifier, legal-form, or activity schemes,
- register, VIES, GLEIF, or other external live checks,
- membership role and validity period,
- representation type and joint representation rules,
- credentials, financial data, process roles, provenance, and access control.

These areas belong in future domain or jurisdiction profiles or separate modules.

## 5. Illustrative Example

> In the core, a Legal Entity requires a legal name, a registration date, and at least one valid identifier. Bank accounts and insurance evidence, by contrast, are not checked by the Organization Shape.