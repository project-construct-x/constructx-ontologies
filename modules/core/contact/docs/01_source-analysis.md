# Source Analysis for the Contact Module

**Status:** Consolidated analysis baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 27 August 2026  
**Scope:** `core/contact`

## 1. Purpose and Method

This analysis evaluates existing contact models as a basis for a Construct-X Contact module. It examines:

- the structure of contact points and communication channels,
- the representation of email, telephone, fax, websites, messengers, and social profiles,
- the separation of contact value, usage context, and purpose,
- boundaries with postal addresses,
- suitability for people, organizations, and business documents such as delivery notes,
- risks arising from overly broad text fields, rigid platform-specific properties, or duplicated address modeling.

## 2. Summary of Findings

[OASIS UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) is the most important source for business processes. UBL provides `Contact` as a grouping structure and `Communication` as a generic channel with a code, text, and value. This aligns well with `ContactPoint` plus `ContactMethod`.

[Schema.org ContactPoint](https://schema.org/ContactPoint) supports the term `ContactPoint`, but is too permissive for Construct-X: `contactType` is text, and many ranges allow text or broadly defined resources. Nevertheless, Schema.org is useful as a source for terms such as `areaServed`, `availableLanguage`, `contactOption`, `email`, `faxNumber`, and `telephone`.

[W3C vCard RDF](https://www.w3.org/TR/vcard-rdf/) is the strongest source for traditional contact data. It supports email, telephone, instant messaging, URLs, addresses, and types such as Home and Work. The n-ary pattern in vCard supports our decision to avoid encoding context and value in properties such as `privateEmail` or `businessPhone`.

## 3. Sources Evaluated

| Source | Version Used | Role in the Analysis | Use |
| --- | --- | --- | --- |
| [OASIS UBL](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) | 2.5 CS01, April 2026 | Business processes and document exchange | Primary field analysis for Contact, Communication, Party, and SocialMediaProfile |
| [Schema.org ContactPoint](https://schema.org/ContactPoint) | Schema.org V30.0, accessed 2026-08-25 | Web interoperability and common terminology | Source for analysis and alignment, not copied directly |
| [W3C vCard RDF](https://www.w3.org/TR/vcard-rdf/) | W3C Interest Group Note, 2014 | Traditional contact structure for people and organizations | Source for analysis and alignment |
| [SEMIC Core Person Vocabulary](https://semiceu.github.io/Core-Person-Vocabulary/) | 2.1.2 | Supports Contact Point as a concept peripheral to Person | Source for defining boundaries |
| [Construct-X Address Ontology](../../address/docs/03_concept-model.md) | 0.1.0 plus reference vocabularies | Existing address model | Postal addresses are referenced rather than copied |
| [Construct-X Agent Ontology](../../agent/docs/10_agent-specification.md) | 0.1.0 | Common superclass for people and organizations | Entity holding contact information in the domain core |

## 4. UBL 2.5

### 4.1 `Contact`

UBL `Contact` describes a contactable person or department within an organization. The structure includes:

- `ID`,
- `Name`,
- `JobTitle`,
- `Department`,
- `Telephone`,
- `Telefax`,
- `ElectronicMail`,
- `Note`,
- `OtherCommunication`.

The meaning of `Name` is important: UBL recommends using this field for functional designations, rather than necessarily for personal names. This is relevant to Construct-X because contacts such as “Goods Receiving,” “Site Management,” or “Invoicing Department” must be modeled without turning them into natural persons.

### 4.2 `Communication`

UBL `Communication` is a generic communication method. It has:

- `ChannelCode` for the communication channel as a code,
- `Channel` for the communication channel as text,
- `Value` for the actual identifying value.

UBL therefore provides a clear precedent for `ContactMethod`: exactly one channel plus exactly one value or referenced resource.

### 4.3 `Party`, Websites, and Social Media

Alongside `Contact`, UBL `Party` includes `WebsiteURI`, `AdditionalWebSite`, `PostalAddress`, and `SocialMediaProfile`. `SocialMediaProfile` has ID, Name, TypeCode, and URI. Three conclusions follow:

1. Websites and social profiles are distinct contact channels.
2. Social profiles should be modeled generically, rather than through a platform-specific property for each provider.
3. Postal addresses are separate structures in UBL and must not be duplicated as address fields in the Construct-X Contact module.

### 4.4 Assessment

| UBL Concept | Construct-X Mapping |
| --- | --- |
| `Contact` | `ContactPoint` as a contact information block |
| `Communication` | `ContactMethod` as a channel plus value |
| `Telephone` | `ContactMethod` with channel `phone` |
| `ElectronicMail` | `ContactMethod` with channel `email` |
| `Telefax` | `ContactMethod` with channel `fax` |
| `OtherCommunication` | Extensible `ContactMethod` |
| `Note` | `availabilityNote` or a general contact note |
| `Name` | `contactName` for a functional contact designation |
| `Department` | Optional text field on the contact point, not an organizational structure |
| `JobTitle` | At most a functional description, not a membership model |
| `PostalAddress` | Reference to `core/address` |
| `SocialMediaProfile` | `ContactMethod` with channel `socialProfile`, platform, and URI |

## 5. Schema.org ContactPoint

Schema.org defines `ContactPoint` as a point of contact, such as a complaints or service department. The most important fields for Construct-X are:

- `contactType` for the purpose of a contact point,
- `telephone`, `email`, and `faxNumber`,
- `areaServed`,
- `availableLanguage`,
- `hoursAvailable`,
- `contactOption`.

The direction from `Person` or `Organization` to `ContactPoint` is established in Schema.org. This supports our preferred direction from the entity holding contact information to the contact point.

Its permissiveness is a concern: `contactType` is text and may conflate purpose, role, department, or usage context. Construct-X should therefore separate these concepts rather than copy a single `contactType`:

| Information Related to Schema.org | Construct-X Modeling |
| --- | --- |
| Contact purpose | `contactPurpose` |
| Private, business, official | `contactUsage` |
| Channel | `contactChannel` |
| Accessibility, toll-free service, etc. | Future `contactOption` vocabulary |
| Language | Optional `availableLanguage` |
| Opening hours | Future temporal/availability profile |

## 6. W3C vCard RDF

vCard RDF represents the IETF vCard model in RDF/OWL. Particularly relevant elements include:

- `hasEmail`,
- `hasTelephone`,
- `hasInstantMessage`,
- `hasURL`,
- `hasAddress`,
- types such as Home, Work, Voice, Cell, and Text.

vCard provides simple direct properties and n-ary patterns for more detailed contact resources. For Construct-X, the n-ary pattern is more appropriate because a telephone number may require several statements: channel, usage, purpose, preference, and potentially further parameters.

Direct vCard properties such as `vcard:hasEmail` are suitable alignment targets. Adopting them directly as the core model would be too restrictive because Construct-X requires delivery, invoicing, project, and organizational contacts in addition to traditional personal vCards.

## 7. SEMIC Core Person

SEMIC Core Person supports the relevance of contact points for people. At the same time, SEMIC separates the Person core from roles, organizations, and other identity aspects. For Construct-X, this means:

- A Person may reference contact points.
- Contact semantics do not belong in `core/person`.
- Contact should be reusable for organizations.

## 8. Construct-X Address

The existing Address module provides `Address`, `AddressAssignment`, and controlled address roles. The postal structure is therefore already covered.

The Contact module consequently has no fields such as `streetName`, `postalCode`, `localityName`, or `country`. A postal contact is modeled as a contact method referencing an existing address assignment.

Following a review against the Address conceptual model, the `AddressAssignment` variant has been selected for the MVP:

A `ContactMethod` references a `conx-addr:AddressAssignment` through `usesAddressAssignment`.

A direct reference to `Address` would bypass existing roles, c/o instructions, attention instructions, and department information. Particularly for delivery, invoicing, and correspondence, these details form part of the domain semantics of contactability.

## 9. Resulting Decisions

The following implemented decisions result from the analysis:

1. The Contact module includes a class `ContactPoint`.
2. A `ContactPoint` groups multiple `ContactMethod` resources.
3. A `ContactMethod` describes exactly one channel.
4. The preferred direction is from `Agent` to `ContactPoint` through `hasContactPoint`.
5. An inverse property `isContactPointFor` is optional.
6. Contact channels are modeled as an extensible SKOS vocabulary.
7. Private, business, and official usage are modeled separately through `contactUsage`.
8. Process purposes such as delivery, billing, support, and emergency are modeled separately through `contactPurpose`.
9. Social profiles remain generic and may reference a platform resource from `contact-platform`.
10. Postal addresses are referenced through `usesAddressAssignment` and remain in the Address module.
11. `contactType` is not adopted as an ambiguous catch-all property.
12. Opening hours, service areas, contact options, and stricter syntax profiles remain candidates for extension.

## 10. Open Issues

| Topic | Reason It Remains Open |
| --- | --- |
| Stricter syntax validation | Email and telephone values initially use non-empty strings in the core profile; stricter patterns belong in domain-specific profiles |
| Availability | `availabilityNote` can be implemented quickly; actual opening hours require a temporal model |

These issues do not block the MVP. They are candidates for later domain-specific profiles or standalone extensions.

## 11. Illustrative Mapping Example

> A UBL contact with email and telephone is imported as one ContactPoint with two ContactMethods. An ambiguous source field such as `contactType` is not copied; its domain meaning is separated into usage and purpose.
