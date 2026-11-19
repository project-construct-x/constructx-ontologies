# Core SHACL Shapes

**Status:** Implemented\
**Version:** 0.2.0\
**As of:** 19 November 2026\
**Scope:** Address Core Shapes

The Address Core Shapes validate the general contracts of the Address Ontology independently of a specific use case. They mirror the OWL cardinalities and make the ranges described in the T-Box executable as closed-world data checks.

```text
Shape graph: modules/core/address/shapes/conx-addr-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/address/core
Version IRI: https://www.construct-x.org/shapes/address/core/0.2.0
Namespace:   https://www.construct-x.org/shapes/address/core#
Version:     0.2.0
```

`core` is the name of the shape set. Additional use-case-specific shape sets can be versioned independently under the same module path.

## 1. OWL and SHACL Serve Different Purposes

OWL describes the semantics of admissible models under the open-world assumption. A missing role is not automatically incorrect because it may simply be unknown. Furthermore, two resources linked through `hasCountry` may be interpreted as the same resource under a maximum-cardinality restriction.

SHACL, by contrast, checks the data graph currently available. If a mandatory role is missing or two countries are specified, a validation error occurs immediately. The parallel rules therefore do not constitute unnecessary duplication:

- OWL exposes the model semantics to reasoners and ontology users.
- SHACL checks concrete data submissions and provides understandable paths to validation errors.

## 2. Cardinalities Represented in Both OWL and SHACL

| Class | Property | Cardinality |
| ----- | -------- | ----------- |
| `LocationAssignment` | `assignedAddress` | At most 1 |
| `LocationAssignment` | `hasGeoReference` | At most 1 |
| `LocationAssignment` | `locationRole` | At least 1 |
| `LocationAssignment` | `careOf` | At most 1 |
| `Address` | `hasCountry` | At most 1 |
| `Address` | `houseNumber` | At most 1 |
| `Address` | `postOfficeBoxNumber` | At most 1 |
| `Address` | `postalCode` | At most 1 |
| `AdministrativeArea` | `broaderAdministrativeTerritory` | At most 1 |

A union of two OWL existential restrictions requires an address or a geolocation. The SHACL `sh:or` accepts either or both.

`plotIdentifier` deliberately retains a cardinality of `0..n`: an address may be associated with multiple plots or land parcels.

## 3. Additional T-Box Contracts Checked

The shapes enforce the existing OWL/RDFS contracts as data checks:

- Values of object relationships must be instances of the specified range class.
- Roles, countries, and administrative units must be referenced through IRIs.
- `hasGeoReference` must reference a resource rather than a literal.
- Textual labels accept `xsd:string` or `rdf:langString`.
- Codes and recipient-related text values accept only `xsd:string`.
- Resources using Address properties must explicitly have the appropriate Address type.

The final rule is enforced more strictly in SHACL than by an RDFS domain. An RDFS domain infers the type, whereas SHACL can report a missing or incorrect type as a data issue.

## 4. Deliberately Not Enforced in the Core

- Street, building number, locality, postal code, or country as universally mandatory fields
- Membership in exactly one specific role or ISO reference dataset
- At most one language-tagged value per language
- Country-specific postal code patterns
- Dependencies such as “either a post office box number or a street address is required”
- Consistency between the country and the complete administrative hierarchy

These rules depend on the use case or profile. They will be added later in shapes for delivery, invoice, construction site, or post office box addresses.

## 5. Test Data

The complete valid graph is located at:

```text
modules/core/address/tests/valid/complete-address.ttl
```

Targeted error cases are located at:

```text
modules/core/address/tests/invalid/assignment-missing-required-values.ttl
modules/core/address/tests/invalid/invalid-core-values.ttl
```

For example, an individual file can be validated as follows:

```text
uv run pyshacl -s modules/core/address/shapes/conx-addr-core.shacl.ttl -e modules/core/address/ontology/conx-addr.ttl -i none modules/core/address/tests/valid/complete-address.ttl
```

The automated tests additionally verify that every general OWL cardinality is mirrored in the shape graph.

## 6. Illustrative Example

> A site gate can be recorded with a site-access role and a geographic reference alone. An assignment with only a role fails validation.
