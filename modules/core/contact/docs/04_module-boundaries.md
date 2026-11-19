# Module Boundaries of the Contact Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.2.0  
**As of:** 19 November 2026  
**Scope:** `core/contact`

## 1. Purpose

This document assigns contact concepts to the responsible Construct-X modules. The Contact module describes contactability without taking over person, organization, address, project, or data protection logic.

## 2. Guiding Principles

1. The Contact module owns contact points and contact methods.
2. The entity holding contact information references its contact points.
3. Contact context and contact purpose are controlled A-Box values.
4. Postal addresses are referenced rather than copied.
5. Platforms such as LinkedIn or Instagram are modeled as data values or vocabulary resources, rather than T-Box properties.
6. Access control, consent, and data protection implications fall outside the Contact module.

## 3. Responsibilities by Module

| Module | Owns | Explicitly Does Not Own |
| --- | --- | --- |
| `core/contact` | `ContactPoint`, `ContactMethod`, `hasContactPoint`, `hasContactMethod`, contact channel, usage context, purpose, platform reference | Personal names, organizational structure, address components, data protection permissions |
| `core/agent` | Common superclass for people and organizations | Specific contact values |
| `core/person` | Intrinsic personal data | Email, telephone, private or business contact logic |
| `core/organization` | Organizations, posts, memberships, and roles | General contact channel structure |
| `core/address` | Structured address, location assignment, and address roles | Email, telephone, messenger, social profile |
| `domain/delivery-note` | Delivery note roles, delivery processes, and document-specific requirements | General contact model |

## 4. Documented Dependencies

### 4.1 Hard Semantic Dependencies

| Dependency | Assessment |
| --- | --- |
| `core/contact -> core/agent` | Plausible from a domain perspective because people and organizations hold contact information; no mandatory import or restrictive domain |
| `core/contact -> core/address` | Reference for `usesLocationAssignment` with range `conx-addr:LocationAssignment` |
| `core/person -> core/contact` | Not required; personal data uses contact concepts only in instance data or profiles |
| `core/organization -> core/contact` | Not required for the Organization T-Box, but both can be used together in data profiles |

The T-Box should use imports only when the external axioms are actually required. A range reference alone may be documented as referenced but not imported.

### 4.2 Domain Decision

The intended domain-level direction is from `Agent` to `ContactPoint` through `hasContactPoint`.

However, a restrictive `rdfs:domain conx-agent:Agent` has a side effect: every resource using `hasContactPoint` is automatically inferred to be an `Agent`. This is appropriate if only people and organizations may hold contact information.

If projects, construction sites, services, or devices should later have their own contact points, an unrestricted domain is more stable. An SHACL profile for agents can still require people and organizations to use `hasContactPoint` correctly.

Implemented decision: document the intended domain-level direction, but do not impose a restrictive RDFS domain in the open T-Box.

## 5. Boundary with Address

A postal address remains a `conx-addr:Address` or `conx-addr:LocationAssignment`.

The Contact module may only express that an address is used as a means of contact. It defines no fields of its own for:

- street,
- building number,
- postal code,
- locality,
- country,
- administrative unit,
- c/o or “for the attention of.”

For delivery note use cases, the link to `LocationAssignment` has been established because existing roles such as `DeliveryAddressRole` or `InvoiceAddressRole` can be reused.

## 6. Boundary with Organization

UBL `Contact.Department` and `Contact.JobTitle` are relevant to exchange data. However, they must not be interpreted as a complete organizational structure.

For the Contact MVP, optional text on `ContactPoint` is acceptable:

```text
contactName       "Goods Receiving Gate 4"
departmentName    "Logistics"
functionTitle     "Shift Supervisor"
```

This asserts no membership, post, or organizational hierarchy. Once actual roles, posts, or memberships are required, their semantics belong in `core/organization`.

## 7. Boundary with Person

A person's private contact information is not modeled as properties of `Person`. Instead:

- `Person` references a `ContactPoint` through `hasContactPoint`.
- The `ContactPoint` has `contactUsage` set to `private`.
- The `ContactPoint` references a `ContactMethod` through `hasContactMethod`.

This keeps `core/person` restricted to intrinsic personal data. Contact values can be validated, hidden, replaced, or deleted separately.

## 8. Boundary with Delivery Note and Other Domain Modules

The Contact module provides generic concepts such as `contactPurpose:delivery`. A delivery note profile may use them more narrowly, for example:

> A delivery party may or must have a delivery contact, depending on the profile.

The requirement itself belongs in a domain shape of the Delivery Note module, rather than in the Contact T-Box.

## 9. T-Box and A-Box Separation

### T-Box

- `ContactPoint`
- `ContactMethod`
- `hasContactPoint`
- `isContactPointFor`
- `hasContactMethod`
- `contactChannel`
- `contactUsage`
- `contactPurpose`
- `contactPlatform`
- `contactValue`
- `contactURI`
- `usesLocationAssignment`
- Optional descriptive text properties such as `contactName`, `departmentName`, `functionTitle`, and `availabilityNote`

### A-Box or Reference Vocabularies

- `contact-channel`: email, telephone, mobile telephone, fax, website, messenger, social profile, postal address
- `contact-usage`: private, business, official
- `contact-purpose`: general, delivery, billing, support, sales, technical, emergency
- `contact-platform`: LinkedIn, Instagram, X, Facebook, GitHub, WhatsApp, Signal, Teams, etc.

Specific people, telephone numbers, email addresses, and URLs are instance data maintained by data holders.

## 10. Import and Alignment Strategy

| Source | Classification |
| --- | --- |
| `core/agent` | Reference or import depending on the domain/range decision |
| `core/address` | Reference for `usesLocationAssignment`; import only if the T-Box actually needs to load the external axioms |
| UBL | Source for analysis and mapping |
| Schema.org | Alignment candidate for `ContactPoint`, not copied directly |
| vCard RDF | Alignment candidate for email, telephone, URL, address, and usage types |
| SKOS | Likely to be reused directly for controlled vocabularies |

New entries in `network/imports.lock.yaml` are required only when actual `owl:imports` are introduced.

## 11. Illustrative Example

> An organization has a billing contact with an email address. Organization describes the organization; Contact describes the contact point, purpose, and email method. Neither module copies the concepts of the other.