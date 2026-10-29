# Term Catalog for the Contact Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/contact`

## 1. Purpose

This catalog describes the local terms of Contact T-Box 0.1.0 and the associated reference vocabularies. The SHACL cardinalities refer to the core profile, rather than strict OWL restrictions.

## 2. Namespaces

### Contact Ontology

```text
Ontology IRI: https://www.construct-x.org/ontology/contact
Version IRI:  https://www.construct-x.org/ontology/contact/0.1.0
Namespace:    https://www.construct-x.org/ontology/contact#
Prefix:       conx-contact
```

### Contact Channel Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/contact-channel
Version IRI:    https://www.construct-x.org/vocab/contact-channel/0.1.0
Namespace:      https://www.construct-x.org/vocab/contact-channel#
Prefix:         contact-channel
```

### Contact Usage Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/contact-usage
Version IRI:    https://www.construct-x.org/vocab/contact-usage/0.1.0
Namespace:      https://www.construct-x.org/vocab/contact-usage#
Prefix:         contact-usage
```

### Contact Purpose Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/contact-purpose
Version IRI:    https://www.construct-x.org/vocab/contact-purpose/0.1.0
Namespace:      https://www.construct-x.org/vocab/contact-purpose#
Prefix:         contact-purpose
```

### Contact Platform Vocabulary

```text
Vocabulary IRI: https://www.construct-x.org/vocab/contact-platform
Version IRI:    https://www.construct-x.org/vocab/contact-platform/0.1.0
Namespace:      https://www.construct-x.org/vocab/contact-platform#
Prefix:         contact-platform
```

## 3. Classes

### 3.1 `conx-contact:ContactPoint`

| Item | Specification |
| --- | --- |
| Definition | Contact information block through which a resource can be reached in a particular usage context and for particular purposes |
| Module | `core/contact` |
| Usage | Groups one or more specific contact methods |
| Source | UBL `Contact`, Schema.org `ContactPoint`, vCard n-ary contact resources |
| Data protection | May contain or reference personal contact values |

Example:

```turtle
ex:private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:private-email,
                                  ex:private-mobile .
```

### 3.2 `conx-contact:ContactMethod`

| Item | Specification |
| --- | --- |
| Definition | Individual communication channel within a contact point |
| Module | `core/contact` |
| Usage | Holds exactly one channel and its associated value, URI, or address reference |
| Source | UBL `Communication`, vCard email/telephone/IMPP/URL |
| Data protection | The specific value may be personal or business-critical |

Example:

```turtle
ex:private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .
```

### 3.3 `conx-contact:ContactChannel`

| Item | Specification |
| --- | --- |
| Definition | Controlled type of communication channel |
| Module | T-Box class in `core/contact`, values in the SKOS vocabulary |
| Examples | Email, telephone, mobile telephone, fax, website, messenger, social profile, postal address |
| Source | UBL `ChannelCode`, vCard communication properties, Schema.org contact fields |

### 3.4 `conx-contact:ContactUsage`

| Item | Specification |
| --- | --- |
| Definition | Usage context of a contact point |
| Module | T-Box class in `core/contact`, values in the SKOS vocabulary |
| Examples | Private, business, official |
| Source | vCard Home/Work, Construct-X domain distinctions |

### 3.5 `conx-contact:ContactPurpose`

| Item | Specification |
| --- | --- |
| Definition | Domain-specific purpose for which a contact point is intended to be used |
| Module | T-Box class in `core/contact`, values in the SKOS vocabulary |
| Examples | General, delivery, billing, support, sales, technical, emergency |
| Source | Schema.org `contactType`, UBL Contact Note, and business process requirements |

### 3.6 `conx-contact:ContactPlatform`

| Item | Specification |
| --- | --- |
| Definition | Platform or service through which a social, messenger, or web profile can be reached |
| Module | T-Box class in `core/contact`, values in the SKOS vocabulary |
| Examples | LinkedIn, Instagram, X, Facebook, GitHub, WhatsApp, Signal, Microsoft Teams |
| Source | UBL `SocialMediaProfile`, web and messaging practice |

## 4. Object Properties

### 4.1 `conx-contact:hasContactPoint`

| Item | Specification |
| --- | --- |
| Definition | Links an entity holding contact information to a contact point |
| Domain | No restrictive `rdfs:domain`; intended direction from the entity holding contact information to the contact point |
| Range | `conx-contact:ContactPoint` |
| Cardinality | `0..n` |
| Inverse | `conx-contact:isContactPointFor` |
| Source | Schema.org `contactPoint`, SEMIC Contact Point |

### 4.2 `conx-contact:isContactPointFor`

| Item | Specification |
| --- | --- |
| Definition | Inverse navigation relationship from a contact point to the entity holding the contact information |
| Domain | `conx-contact:ContactPoint` |
| Range | No restrictive `rdfs:range`; conceptually, the entity holding contact information |
| Cardinality | `0..n` |
| Requirement | Not mandatory |

### 4.3 `conx-contact:hasContactMethod`

| Item | Specification |
| --- | --- |
| Definition | Links a contact point to a specific contact method |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactMethod` |
| Cardinality | Core Shape `1..n` |

### 4.4 `conx-contact:contactChannel`

| Item | Specification |
| --- | --- |
| Definition | Specifies the channel of a contact method |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-contact:ContactChannel` |
| Cardinality | Core Shape: exactly `1` |

### 4.5 `conx-contact:contactUsage`

| Item | Specification |
| --- | --- |
| Definition | Specifies the usage context of a contact point |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactUsage` |
| Cardinality | Core Shape `0..1` |

### 4.6 `conx-contact:contactPurpose`

| Item | Specification |
| --- | --- |
| Definition | Specifies a domain-specific purpose of a contact point |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactPurpose` |
| Cardinality | `0..n` |

### 4.7 `conx-contact:contactPlatform`

| Item | Specification |
| --- | --- |
| Definition | Specifies the platform of a social, messenger, or web contact method |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-contact:ContactPlatform` |
| Cardinality | `0..1` |

### 4.8 `conx-contact:usesAddressAssignment`

| Item | Specification |
| --- | --- |
| Definition | Links a postal contact method to an existing address assignment |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-addr:AddressAssignment` |
| Cardinality | Core Shape: exactly `1` for channel `postalAddress` |

## 5. Value Properties

### 5.1 `conx-contact:contactValue`

| Item | Specification |
| --- | --- |
| Definition | Literal value of a contact method |
| Domain | `conx-contact:ContactMethod` |
| Range | `xsd:string`; for email, telephone, mobile telephone, and fax, the core profile checks only that the value is non-empty |
| Examples | Email address, telephone number, messenger handle |

### 5.2 `conx-contact:contactURI`

| Item | Specification |
| --- | --- |
| Definition | IRI or URL of a contact method |
| Domain | `conx-contact:ContactMethod` |
| Range | IRI |
| Examples | Website, social profile, mailto URI, tel URI |

### 5.3 `conx-contact:contactName`

| Item | Specification |
| --- | --- |
| Definition | Display or functional name of a contact point |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` or `rdf:langString` |
| Examples | “Goods Receiving,” “Site Management,” “Invoicing Department” |

### 5.4 `conx-contact:departmentName`

| Item | Specification |
| --- | --- |
| Definition | Textual department information for a contact point |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` or `rdf:langString` |
| Note | Does not represent an organizational hierarchy |

### 5.5 `conx-contact:functionTitle`

| Item | Specification |
| --- | --- |
| Definition | Textual function or role of the contact point within the communication context |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` or `rdf:langString` |
| Note | Does not constitute an organizational role model |

### 5.6 `conx-contact:availableLanguage`

| Item | Specification |
| --- | --- |
| Definition | Language in which the contact point can be used |
| Domain | `conx-contact:ContactPoint` |
| Range | BCP 47 language code as a string, or a language resource in a future version |
| Source | Schema.org `availableLanguage`, vCard `language` |

### 5.7 `conx-contact:availabilityNote`

| Item | Specification |
| --- | --- |
| Definition | Free-text information about availability |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` or `rdf:langString` |
| Examples | “Mon–Fri 08:00–16:00,” “emergencies only,” “by prior arrangement” |

## 6. Implemented Initial Values

### 6.1 `contact-channel`

| Term | German | English | Note |
| --- | --- | --- | --- |
| `email` | E-Mail | Email | Non-empty string |
| `phone` | Telefon | Phone | General telephone number as a non-empty string |
| `mobilePhone` | Mobiltelefon | Mobile phone | Dedicated mobile telephone channel as a non-empty string |
| `fax` | Fax | Fax | UBL `Telefax`, Schema.org `faxNumber` |
| `website` | Website | Website | URL/IRI |
| `messenger` | Messenger | Messenger | Handle or URI; platform may be specified |
| `socialProfile` | Social-Media-Profil | Social media profile | URI; platform may be specified |
| `postalAddress` | Postanschrift | Postal address | Reference to the Address module |

### 6.2 `contact-usage`

| Term | German | English |
| --- | --- | --- |
| `private` | Privat | Private |
| `business` | Beruflich/geschäftlich | Business |
| `official` | Offiziell | Official |

### 6.3 `contact-purpose`

| Term | German | English |
| --- | --- | --- |
| `general` | Allgemein | General |
| `delivery` | Lieferung | Delivery |
| `billing` | Rechnung | Billing |
| `support` | Support | Support |
| `sales` | Vertrieb | Sales |
| `technical` | Technisch | Technical |
| `emergency` | Notfall | Emergency |

### 6.4 `contact-platform`

| Term | Usage |
| --- | --- |
| `linkedin` | Professional social profile |
| `instagram` | Social profile |
| `x` | Social profile, formerly Twitter |
| `facebook` | Social profile |
| `github` | Developer profile |
| `whatsapp` | Messenger |
| `signal` | Messenger |
| `microsoftTeams` | Messenger or collaboration |

The platform vocabulary should not be considered exhaustive.

## 7. Compact Target Example

```turtle
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix contact-channel: <https://www.construct-x.org/vocab/contact-channel#> .
@prefix contact-purpose: <https://www.construct-x.org/vocab/contact-purpose#> .
@prefix contact-usage: <https://www.construct-x.org/vocab/contact-usage#> .
@prefix ex: <https://example.org/id/> .

ex:person-123
    conx-contact:hasContactPoint ex:person-123-private-contact .

ex:person-123-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-123-private-email,
                                  ex:person-123-private-mobile .

ex:person-123-private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .

ex:person-123-private-mobile
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:mobilePhone ;
    conx-contact:contactValue "+49 171 1234567" .
```

## 8. Deliberately Reserved for Later Profiles

| Topic | Rationale |
| --- | --- |
| `availableLanguage` as a literal or language resource | A BCP 47 code is pragmatic; a language resource would provide stronger semantics |
| URI or literal variants for email and telephone | The core MVP checks these channels as non-empty strings; mailto/tel profiles may follow later |
| Strict regular expressions | Email and telephone validation can quickly become country-specific and error-prone |

The interaction of these concepts is illustrated in the [Contact Concept Diagram](diagrams/contact-concept-model.md).
