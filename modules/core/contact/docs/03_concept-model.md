# Conceptual Model of the Contact Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.2.0  
**As of:** 19 November 2026  
**Scope:** `core/contact`

## 1. Purpose

The model separates a contact point from the specific means through which it can be reached.

## 2. Model in Plain Language

A `ContactPoint` describes the usage context, for example “business contact for invoicing.” A `ContactMethod` contains exactly one channel, such as email, telephone, or website.

## 3. Terms

| Term | Meaning |
| --- | --- |
| `ContactPoint` | Grouped point of contact for a particular context |
| `ContactMethod` | Individual means of contact |
| `ContactChannel` | Type of contact channel |
| `ContactUsage` | Private, business, or official |
| `ContactPurpose` | For example, billing, delivery, or support |

## 4. Relationships

A contactable entity references a contact point through `hasContactPoint`. The contact point groups one or more contact methods.

## 5. Illustrative Example

> A company's accounting department can be reached in a business context for invoice-related matters. It has an email address and a telephone number.

The company references a ContactPoint named “Accounting,” which groups an email method and a telephone method.

## 6. Boundaries

Postal address components are not copied. A postal contact method references `core/address`.

## 7. Decisions

Contact channel, usage, and purpose are separate controlled values. Strict syntax checks are reserved for domain-specific profiles.

The detailed diagram is available in [contact-concept-model.md](diagrams/contact-concept-model.md).