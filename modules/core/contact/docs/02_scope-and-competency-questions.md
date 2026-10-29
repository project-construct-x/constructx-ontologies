# Scope and Competency Questions of the Contact Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/contact`

## 1. Purpose

The Contact module describes contactability. It expresses the channels through which a resource can be reached, the usage context in which the information applies, and the purpose it serves.

The module does not own a person's identity, an organization's structure, or the postal address itself. These concepts remain in `core/person`, `core/organization`, and `core/address`, respectively.

## 2. Confirmed Scope

| Area | MVP Decision |
| --- | --- |
| Entity holding contact information | Primarily `conx-agent:Agent`, particularly people and organizations; no restrictive `rdfs:domain` on `hasContactPoint` |
| Direction | From the entity holding contact information through `hasContactPoint` |
| Inverse | `isContactPointFor` is optional as a convenience property, not mandatory |
| Contact point | Groups multiple specific contact methods within a usage context |
| Contact method | Describes exactly one channel and its value, URI, or address reference |
| Channels | Email, telephone, mobile telephone, fax, website, messenger, social profile, postal address |
| Postal address | No separate address structure; reference to `conx-addr:AddressAssignment` from the existing Address module |
| Private/business/official | Controlled A-Box vocabulary `ContactUsage` |
| Purpose | Separate A-Box vocabulary `ContactPurpose`, for example delivery, billing, support, emergency |
| Social profile | Modeled generically, with the platform represented through a dedicated extensible vocabulary |
| Access control | Outside the Contact ontology |
| Availability times | For the MVP, only a free-text note or a later profile; no dedicated temporal model |

## 3. Out of Scope

- Structured address components such as street, building number, locality, or country,
- personal names and personal identity,
- organizational memberships, posts, and roles,
- permissions, consent, and data protection processes,
- complete opening-hours or calendar logic,
- technical delivery protocols and messaging accounts as a dedicated account ontology,
- specific platform APIs such as LinkedIn, Instagram, or X represented through fixed properties.

## 4. Modeling Principle

A `ContactPoint` is not a single field such as a telephone number. It is a domain-specific contact information block. A person can therefore have, for example, a private contact point with email, mobile telephone, and a postal address:

```turtle
ex:person-123
    conx-contact:hasContactPoint ex:person-123-private-contact .

ex:person-123-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-123-private-email,
                                  ex:person-123-private-mobile .
```

This avoids properties such as `privateEmail`, `businessPhone`, or `deliveryMobile`, whose number would quickly proliferate as new channels and purposes are added.

## 5. Competency Questions

### CQ-01: Which contact points does a person or organization have?

An entity holding contact information references zero or more contact points through `hasContactPoint`. The preferred direction therefore remains from the Agent.

Example:

```turtle
ex:person-123 conx-contact:hasContactPoint ex:person-123-private-contact .
```

### CQ-02: How are private, business, and official contact contexts distinguished?

The usage context is described on the `ContactPoint` through `contactUsage`. The implemented initial values are:

| Value | Meaning |
| --- | --- |
| `contact-usage:private` | Contact point for private use |
| `contact-usage:business` | Contact point for professional or business use |
| `contact-usage:official` | Contact point for official, register-related, or institutional use |

`private` is not access control. It describes the domain-specific usage context, rather than who may read the value.

### CQ-03: How is the purpose of a contact point described?

Purpose is modeled separately from usage context through `contactPurpose`. This is important for delivery note and procurement processes because a business contact point may, for example, be used for delivery, billing, or support.

Implemented initial values:

| Value | Meaning |
| --- | --- |
| `contact-purpose:general` | General contact |
| `contact-purpose:delivery` | Delivery, goods receiving, or dispatch to the recipient |
| `contact-purpose:billing` | Invoicing and payment clarification |
| `contact-purpose:support` | Support or customer service |
| `contact-purpose:sales` | Sales or quotation-related communication |
| `contact-purpose:technical` | Technical inquiries |
| `contact-purpose:emergency` | Emergency or escalation contact |

### CQ-04: How are multiple communication channels grouped at a contact point?

A `ContactPoint` has multiple `ContactMethod` resources. Each `ContactMethod` has exactly one channel. This keeps the contact point grouped at the domain level while allowing channel values to be validated individually.

```turtle
ex:delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:delivery ;
    conx-contact:hasContactMethod ex:delivery-email,
                                  ex:delivery-phone .

ex:delivery-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "wareneingang@example.org" .
```

### CQ-05: How are postal contact addresses modeled?

Postal addresses are described through `core/address`. The Contact module provides a contact method with the channel `postalAddress` and links it to an existing `conx-addr:AddressAssignment`.

Implemented pattern:

```turtle
ex:private-postal-method
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesAddressAssignment ex:private-postal-address-assignment .
```

A direct reference to `conx-addr:Address` is excluded from the MVP. The Address ontology already specifies that domain-specific usage, role, and delivery instructions are expressed through `AddressAssignment`. These are precisely the details relevant to postal contactability.

### CQ-06: How are social media profiles modeled?

Social profiles are not modeled through separate properties for each platform. Instead, the channel `socialProfile` is used. A platform resource can describe the platform.

```turtle
ex:max-linkedin
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin ;
    conx-contact:contactURI <https://www.linkedin.com/in/example> .
```

This is more stable than `hasLinkedInProfile`, `hasInstagramProfile`, or `hasTwitterProfile`.

### CQ-07: How is a functional contact such as “Goods Receiving” or “Site Management” represented?

Functional contact designations belong to the contact point rather than the person. A contact point can therefore have an optional `contactName`.

Example:

```turtle
ex:delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactName "Wareneingang Tor 4"@de ;
    conx-contact:contactPurpose contact-purpose:delivery .
```

This does not assert a personal name.

### CQ-08: How is an inverse relationship handled?

An inverse property `isContactPointFor` is not included in version `0.1.0`. Data maintainers record the relationship through `hasContactPoint`, from the entity holding contact information to the contact point.

### CQ-09: Which validation questions does the Core SHACL Profile address?

For the MVP, the Core SHACL Profile specifies:

- `ContactPoint` and `ContactMethod` may be IRIs or blank nodes, but must be explicitly typed.
- A `ContactPoint` must have at least one `ContactMethod`.
- `contactUsage` may occur at most once.
- A `ContactMethod` must have exactly one `contactChannel`.
- The permitted value form depends on the channel: string, IRI, or `AddressAssignment`.
- Usage, Purpose, Channel, and Platform are checked against the approved Construct-X reference vocabularies.
- Email, telephone, mobile telephone, and fax values are checked only as non-empty strings.

## 6. Implemented Modeling Decisions

| Topic | Decision | Rationale |
| --- | --- | --- |
| Restrictive domain of `hasContactPoint` | No restrictive `rdfs:domain`, but document the domain-level direction from `Agent` to `ContactPoint` | Prevents unintended inference if projects, construction sites, or services later hold contact information |
| `contactName` vs. `functionalLabel` | `contactName` | UBL explicitly uses `Contact.Name` for functional names as well |
| Email and telephone as literal or URI | Non-empty string in the core profile | UBL and Schema.org use text; strict syntax rules depend on the domain-specific profile |
| Platform vocabulary | Dedicated extensible `contact-platform` vocabulary in the MVP | Platforms change frequently; fixed T-Box properties are avoided |

## 7. Acceptance Criteria for 0.1.0

The MVP covers the domain requirements when:

1. the classes `ContactPoint` and `ContactMethod` are implemented,
2. the four reference vocabularies `contact-channel`, `contact-usage`, `contact-purpose`, and `contact-platform` are available,
3. postal contact methods reference `core/address` through `usesAddressAssignment`,
4. the minimum rules for ContactPoint and ContactMethod are implemented and tested as Core Shapes.

## 8. Illustrative Example

> An organization's support desk can be reached in a business context for technical inquiries. It can have both a telephone number and an email address without requiring two separate contact points.