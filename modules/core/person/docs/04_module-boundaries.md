# Module Boundaries of the Person Ontology

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

## 1. Objective

This document assigns classes and relationships to the responsible Construct-X modules. It prevents the Person ontology from becoming an aggregate model for organization, contact, address, project, and digital identity.

The described Core modules are implemented in version `0.1.0`. A cross-module reference still does not imply an automatic OWL import.

## 2. Guiding Principles

1. A module owns only the terms belonging to its domain core.
2. Wherever possible, relationships are defined by the module responsible for their domain meaning.
3. Reusable cross-cutting concepts are not hidden in `person`.
4. Data can be connected across modules without every consuming module having to import every other module.
5. Dependencies should remain directed and acyclic.
6. External ontologies are imported only when their axioms are necessary for local semantics. Alignment solely through `rdfs:subClassOf`, `rdfs:subPropertyOf`, or equivalences must be assessed separately.

## 3. Implemented Core Module Structure

| Module | Responsibility |
| --- | --- |
| `core/agent` | Minimal shared superclass |
| `core/person` | Natural persons and intrinsic personal data; specialization of Agent |
| `core/organization` | Organizations, memberships, and representation; specialization of Agent |
| `core/identifier` | Shared ADMS/SKOS identifier contract |
| `core/contact` | Contact points and contact methods with unrestricted domains |
| `core/address` | Address and AddressAssignment model |
| `core/participation` | Qualified Agent roles in domain contexts |
| `core/document` | Documents, references, and distributions |

A possible identity or credential profile remains outside the Person core. Geographic positions are connected through the open extension point of the Address module; the Person documentation does not propose a separate `core/location`.

## 4. Decision on the `Agent` Class

A shared `Agent` superclass is useful because several cross-cutting relationships concern both natural persons and organizations:

- issuing or responsible authorities,
- memberships and roles,
- potentially authorization and participation.

Nevertheless, it is not defined in the Person ontology. A `conx-person:Agent` would permanently make organizations dependent on a Person module and distort future module boundaries.

The target model therefore uses a minimal class in `core/agent`:

| Superclass | Subclass |
| --- | --- |
| `conx-agent:Agent` | `conx-person:Person` |
| `conx-agent:Agent` | `conx-org:Organization` |

For external interoperability, alignment with `foaf:Agent` and, for `Person`, with `foaf:Person` or `schema:Person` should be assessed. The local module retains ownership of its terms and quality requirements.

The specific proposal provides no Agent-specific properties and no mandatory shape without substantive constraints in the first Agent release. All domain-specific Person terms are described in the [Term Catalog](05_term-catalog.md).

## 5. Concept Ownership

| Module | Owns | Explicitly does not own |
| --- | --- | --- |
| `core/agent` | Minimal `Agent` superclass; at most genuinely generic Agent relationships | Person attributes, organizational structure, contact values |
| `core/person` | `Person`, names, birth details, `sex`, `gender`, citizenship, and evidence links | Memberships, roles, addresses, contact point details, credential and key details |
| `core/identifier` | Shared ADMS/SKOS contract and `ADMSIdentifierShape` | Domain-specific mandatory identifiers and concrete identification schemes |
| `core/contact` | `ContactPoint`, `ContactMethod`, contact channel, usage context, contact purpose, email, telephone, and other channels | Person names, organizational structure, postal address components |
| `core/address` | `Address`, `AddressAssignment`, address roles, and postal structure | Person and Organization themselves |
| `core/organization` | `Organization`, `LegalEntity`, `OrganizationalUnit`, `Membership`, and legal representation | Intrinsic personal data and general contextual roles |
| `core/participation` | General qualified role of an Agent in a domain context | Person core and organizational membership |
| Future Identity module | Identity documents, credentials, verification methods, status, and revocation | Biographical Person profile |

## 6. Implemented Dependencies

### 6.1 Hard Semantic Dependencies

A hard dependency arises only when a module requires another module’s classes or properties in its own axioms.

| Module | Dependency | Reason |
| --- | --- | --- |
| `core/person` | `core/agent` | `Person` is a subclass of `Agent` |
| `core/organization` | `core/agent` | `Organization` is an Agent; members can be Agents |
| `person/core` shape | `identifier/core` shape | Person identifiers use the shared ADMS/SKOS contract |

### 6.2 Composition without Mandatory Imports

Instance data may jointly use terms from different modules. This does not automatically imply an import from the Person module to the respective domain module.

Address example:

```turtle
ex:person-123 a conx-person:Person ;
    conx-addr:hasAddressAssignment ex:address-assignment-1 .
```

Since `conx-addr:hasAddressAssignment` belongs to the Address module, an application can load the Person and Address modules together. The Person module does not need to redefine the property.

Contact example:

```turtle
ex:person-123
    conx-contact:hasContactPoint ex:private-contact-point .

ex:private-contact-point
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:private-email .

ex:private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "person@example.org" .
```

The two-stage pattern supports usage context, purpose, and potentially validity later, without attaching these details to the Person or the individual contact value itself.

## 7. Boundary with Organizations

The Person module defines no membership or employment semantics. The existing Organization module uses a relationship model based on the W3C ORG pattern:

| Relationship resource | Connected information |
| --- | --- |
| `Membership` | Person/Agent |
| `Membership` | Organization |
| `Membership` | Role |
| `Membership` | Period |

Direct relationships such as `isMemberOf` and `hasMember` can provide a simple view of this structure. However, their definitions, inverse relationships, domains, ranges, and possible derivation rules must all belong to the Organization module. This avoids cyclic domain ownership between `person` and `organization`.

The company address belongs to the organization or a site. A Person does not automatically receive it as their own address. Business contact points may be assigned to a Person, position, or organization through the Contact module.

## 8. Boundary with Projects

Project participation typically carries a role, period, assignment, or area of responsibility. It therefore belongs in the Project module and should not be reduced to a single direct Person property.

The Project module may reference persons or, more generally, Agents as participants. The Person module does not require an inverse property for this purpose. If an inverse navigation relationship is required, it is defined together with the participation semantics in the Project module.

## 9. Boundary with Contact and Address

Contact and Address remain separate:

- A contact point describes a communication channel, such as email or telephone.
- An address describes a postal or spatial reference.
- A contact point describes the usage context and purposes for which an entity can be reached. The entity has an outgoing `hasContactPoint` reference to this contact point.
- An address assignment describes the resource and role for which an address applies.

The Contact module requires no fixed OWL domain of `Agent`. `hasContactPoint` remains without a restrictive domain in the open core because projects, positions, and other resources can hold contact information alongside persons and organizations. Specific SHACL profiles may permit the property for their respective target classes.

## 10. Boundary with Identifiers and Identity Evidence

Three layers must be distinguished:

| Layer | Meaning | Responsibility |
| --- | --- | --- |
| Resource IRI | Identity of the RDF node in the respective data space | Data holder and namespace concept |
| Domain identifier | Identifier according to a known scheme | `core/identifier` and Identifier Scheme vocabulary |
| Identity evidence | Assertion or document that binds attributes to a Person | External or future Identity module |

A public key is a verification method rather than a sufficient natural person identifier. Key material, controllers, verification relationships, and revocation should follow W3C Controlled Identifiers. Verifiable assertions about a Person can be connected through a Verifiable Credential.

The Person module may define a generic evidence link but should neither copy nor restrict its internal structure before the target model has been established.

## 11. Countries and Geographic Concepts

The Construct-X country vocabulary uses stable country IRIs and types them as `conx-addr:Country`. The Person module uses these resources for citizenship. Geographic positions remain connected through the open `conx-addr:hasGeographicPosition` extension point; a separate Location model is not a prerequisite for the Person core.

## 12. Import and Alignment Strategy

For implementation, each external source must be assigned to one of the following categories:

| Category | Meaning |
| --- | --- |
| Import | The external axioms are necessary for local semantics and are resolved using versioned references |
| Reference | Local axioms use external resources without importing the complete ontology |
| Alignment | Local terms are aligned with external terms through mapping axioms |
| Analysis source | The source influences the design but does not necessarily appear in the RDF model |

Implemented classification:

| Source | Classification |
| --- | --- |
| ADMS and SKOS for identifiers | Reuse through `core/identifier` |
| Construct-X ISO 3166-1 country vocabulary | Reference to A-Box resources |
| FOAF, Schema.org, and SEMIC Core Person | Conservative alignments or documented references |
| vCard | Analysis and alignment source for Contact |
| W3C ORG | Alignment and reuse source for the Organization module |
| W3C Controlled Identifiers and VC Data Model | Basis for a future Identity module |

The specific references are documented as `referenced-not-imported` in the respective `module.yaml` files. Since no T-Box uses `owl:imports`, no new entry is created in `network/imports.lock.yaml`.

## 13. Implementation Status

`core/agent`, `core/person`, `core/contact`, `core/organization`, `core/address`, `core/participation`, and `core/identifier` are implemented and have defined domain boundaries. Further detailing of identity evidence after selecting a security and trust model remains a non-blocking follow-up task.

## 14. Illustrative Example

> Anna’s birth date belongs to the Person. Her office address belongs to an AddressAssignment, and her role in the office belongs to a Membership. The Person module does not store this information again.