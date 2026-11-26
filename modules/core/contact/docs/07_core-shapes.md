# Contact Core Shapes

**Status:** Implemented  
**Version:** 0.3.0  
**As of:** 26 November 2026  
**Scope:** Contact Core Shapes

The Contact Core Shapes validate the general, use-case-independent data contracts of the Construct-X Contact Ontology. The T-Box remains semantically open under the open-world assumption; the core profile, by contrast, checks concrete data submissions.

```text
Shape graph: modules/core/contact/shapes/conx-contact-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/contact/core
Version IRI: https://www.construct-x.org/shapes/contact/core/0.3.0
Namespace:   https://www.construct-x.org/shapes/contact/core#
Version:     0.3.0
```

## 1. Validated Contracts

- Values of `hasContactPoint` must be typed as `conx-contact:ContactPoint`.
- `hasContactPoint` does not impose the type `conx-agent:Agent` on its subject.
- Every `ContactPoint` must be a blank node or IRI, be explicitly typed as `conx-contact:ContactPoint`, and have at least one `ContactMethod`.
- `contactUsage` may occur at most once and must reference the approved `contact-usage` vocabulary.
- `contactPurpose` references the approved `contact-purpose` vocabulary.
- Descriptive text values such as `contactName`, `departmentName`, `functionTitle`, and `availabilityNote` must not be empty.
- Every `ContactMethod` must be a blank node or IRI, be explicitly typed as `conx-contact:ContactMethod`, and have exactly one approved `contactChannel`.
- Email, telephone, mobile telephone, and fax use exactly one non-empty `contactValue` of datatype `xsd:string`.
- Websites and social profiles use exactly one IRI through `contactURI`.
- Messenger uses exactly one non-empty `contactValue` or exactly one IRI through `contactURI`.
- Postal contact methods use exactly one `usesLocationAssignment` referencing a `conx-addr:LocationAssignment`.
- `contactPlatform` may occur at most once and must reference the approved `contact-platform` vocabulary.

Additional properties remain permitted. The profile does not use `sh:closed true` and requires no RDFS or OWL inference.

## 2. Reference Graphs

To validate controlled values, the following graphs are loaded together with the data:

- `datasets/reference/vocabularies/contact-channel/contact-channel.ttl`,
- `datasets/reference/vocabularies/contact-usage/contact-usage.ttl`,
- `datasets/reference/vocabularies/contact-purpose/contact-purpose.ttl`,
- `datasets/reference/vocabularies/contact-platform/contact-platform.ttl`,
- `modules/core/address/ontology/conx-addr.ttl`,
- `datasets/reference/vocabularies/address-roles/address-roles.ttl`, when postal location assignments are fully validated.

The small sets of contact values are additionally recorded as closed `sh:in` lists in the shape graph. New channels, usages, purposes, or platforms should therefore be versioned deliberately.

## 3. Test Data

Valid test graphs are located in `modules/core/contact/tests/valid`. Targeted error cases are located in `modules/core/contact/tests/invalid`. The automated tests load the required reference graphs, run PySHACL without inference, and check error message IDs.

The automated shape tests can be run from the repository root as follows:

```text
uv run pytest tests/test_contact_shapes.py
```

Direct `pyshacl` calls must also load the reference graphs listed above into the validation data graph. The automated test suite handles this.

## 4. Deliberately Excluded Checks

- Whether a telephone number can actually be reached,
- whether an email address exists,
- strict email or telephone number syntax,
- whether a social profile URL actually belongs to the specified platform,
- who may view or use private contact information,
- opening hours, service areas, priorities, and deliverability,
- person, organization, role, or address details beyond the `LocationAssignment` reference.

These areas belong in later domain-specific profiles or standalone modules.

## 5. Illustrative Example

> A contact point without a contact method is invalid because nobody can be reached through it. A business contact point with a correctly typed email method, by contrast, satisfies the core contract.
For a postal method, `usesLocationAssignment` must reference a `LocationAssignment` with exactly one `hasAssignedAddress` of type `Address`.

