# Status Term Catalog

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Namespace and Classes

Namespace: `https://www.construct-x.org/ontology/status#`; prefix: `conx-status`.

| Class | Meaning |
| --- | --- |
| `StatusAssignment` | An identified statement of one status value for one status kind and one resource at a business reference date and time. The resource links to it through hasStatus. |
| `StatusKind` | A reusable status dimension, such as transport status or temperature inspection. Concrete kinds are vocabulary individuals. |
| `StatusValue` | A reusable state selected by an assignment; its applicability to a kind is declared with hasAllowedStatusValue. |
| `StatusReason` | A reusable explanation for a status. Applicability declarations on kinds are positive and non-exhaustive. |

The three concept classes are subclasses of skos:Concept. The labels
"Vocabulary of status kinds", "Vocabulary of status values" and "Vocabulary
of status reasons" name scheme instances, not additional classes.

## 2. Object Properties

| Property | Domain | Range | Multiplicity |
| --- | --- | --- | --- |
| `hasStatus` | Any resource | conx-status:StatusAssignment | 0..n per object; exactly 1 owner per assignment |
| `hasCurrentStatus` | Any resource | conx-status:StatusAssignment | 0..1 per object and kind |
| `hasStatusKind` | conx-status:StatusAssignment | conx-status:StatusKind | 1 |
| `hasStatusValue` | conx-status:StatusAssignment | conx-status:StatusValue | 1 |
| `hasStatusReason` | conx-status:StatusAssignment | conx-status:StatusReason | 0..n |
| `hasAllowedStatusValue` | conx-status:StatusKind | conx-status:StatusValue | 0..n |
| `hasAllowedStatusReason` | conx-status:StatusKind | conx-status:StatusReason | 0..n |
| `previousStatus` | conx-status:StatusAssignment | conx-status:StatusAssignment | 0..1 |
| `reportedBy` | conx-status:StatusAssignment | conx-agent:Agent | 0..1 |
| `hasCondition` | conx-status:StatusAssignment | conx-vso:AssignedProperty | 0..n |

previousStatus and reportedBy deliberately retain the agreed names. They are
documented exceptions to the repository test's narrower relationship-prefix
pattern. hasCurrentStatus is a subproperty of hasStatus, not a globally
functional property.

reportedBy accepts Core Person and Organization instances when their existing
Core class definitions are supplied as context. For example, a reporter
typed only as conx-person:Person qualifies as an Agent through the Person
ontology. No additional rdf:type Agent assertion is required. The maximum
of one reporter applies across all Agent subclasses together.

If hasCurrentStatus is present, its target must be the uniquely latest known
assignment for that object and kind. Business date/time with UTC offset
determines recency; explicit predecessor paths resolve equal-time order.
An unresolved latest tie prohibits a current link. recordedAt does not affect
this decision. The link remains optional even when the latest status is unique.

## 3. Literal Attributes

| Attribute | Format | Multiplicity |
| --- | --- | --- |
| `referenceDate` | xsd:date | 1 |
| `referenceTime` | xsd:time | 1 |
| `recordedAt` | Valid xsd:dateTime; T separator; optional UTC offset | 0..1 |
| `description` | xsd:string or rdf:langString | 0..n |
| `reasonText` | xsd:string or rdf:langString | 0..n |

referenceDate uses YYYY-MM-DD; referenceTime requires an explicit UTC offset
and permits at most six fractional second digits (microseconds).
recordedAt remains optional. If supplied, its date, clock time and lexical
form must be valid; an optional UTC offset uses Z or ±hh:mm, at most 14:00
in either direction. For example, `2026-11-11T10:05:00` is valid without an
offset, while `2026-11-11 10:05:00Z` is invalid. recordedAt does not inherit
referenceTime's six-digit fractional-second limit.
The XSD end-of-day spelling is supported for recordedAt: for example,
`2026-12-31T24:00:00Z` means `2027-01-01T00:00:00Z`. With hour 24, minutes,
seconds and all fractional digits must be zero; the calendar date and any
UTC offset must still be valid. Validation preserves the supplied spelling.
description describes the statement, while reasonText explains the statement
as a whole. No pairing between each reasonText and each reason concept is implied.

## 4. Metadata on Our Vocabulary Terms

| Property | Format | Multiplicity |
| --- | --- | --- |
| skos:prefLabel | Nonempty language-tagged text | 1..n; at most one per language |
| skos:definition | Nonempty language-tagged text | 1..n |
| skos:notation | Nonempty xsd:string code | 1 |
| skos:inScheme | Typed skos:ConceptScheme IRI | 1..n |
| skos:altLabel | Nonempty language-tagged text | 0..n |
| skos:scopeNote | Nonempty language-tagged text | 0..n |

Preferred and alternative labels must not share the same literal.
Codes are unique within each scheme. The initial release supplies German and
English labels and definitions. External terms are not subjected to this
local publication contract.

## 5. Initial Vocabulary and Example

| Kind | Allowed values | Positively associated reasons |
| --- | --- | --- |
| TransportStatus | InProgress, Shipped, Delivered | VehicleBreakdown, AccessBlocked |
| TemperatureInspection | NotChecked, Passed, Failed | TemperatureExceeded |
| QuantityInspection | NotChecked, Passed, Failed | QuantityMismatch |

For example, TemperatureInspection + Failed + TemperatureExceeded is a
complete kind/value/reason combination. A reason not linked to the kind
also remains valid in Core. A value not linked to the kind does not.
