# Status Conceptual Model

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. The Status Assignment

A status assignment is an identified statement, not a vocabulary term.
A resource points to it using hasStatus. Each assignment belongs to exactly
one resource; no inverse subject property is introduced.

A delivery can be shipped while its temperature inspection fails. The two
statements use different kinds and may independently be selected as current.

reportedBy optionally identifies the Agent who reports a statement. This can
be a Core Person, such as Alex Example reporting a delivery, or a Core
Organization, such as Example Logistics reporting dispatch. Both inherit
from Agent through their existing Core ontologies. Supply the corresponding
ontology as context when only the more specific type is asserted.

```text
Status assignment -> reportedBy -> Person: Alex Example
Status assignment -> reportedBy -> Organization: Example Logistics
```

These are alternatives for separate statements: each assignment permits at
most one reporter. The relationship identifies the reporting actor; it does
not by itself identify a driver, owner or measurement performer. See the
[complete examples and commands](../examples/reporting-actors/README.md).

## 2. Kinds, Values and Reasons

- StatusKind identifies the dimension: TransportStatus, TemperatureInspection
  or QuantityInspection in the initial reference vocabulary.
- StatusValue identifies the state. Passed and Failed are reused by both
  inspection kinds.
- StatusReason explains a statement. Several reasons can coexist.
- The three vocabularies are skos:ConceptScheme instances, not new classes.

A selected value requires a hasAllowedStatusValue link from the selected kind.
hasAllowedStatusReason only records positive applicability. Unlisted typed
reasons remain valid in Core, even if they are linked to a different kind.
A specialized application may impose additional combination rules.

## 3. Time and History

referenceDate is a calendar date in YYYY-MM-DD form. referenceTime supplies
the clock time and mandatory UTC offset: Z or ±hh:mm. Offsets range from
-14:00 to +14:00; ordinary clock hours are 00–23, with optional fractional
seconds with at most six digits (microseconds). Finer precision is rejected,
not rounded. A separate timezone on referenceDate is not used.

recordedAt is an optional xsd:dateTime and does not determine which status
is current. If present, it contains a valid date and time separated by T.
Its UTC offset is optional; an explicit offset uses Z or ±hh:mm, up to 14:00
in either direction. For example, both `2026-11-11T10:05:00` and
`2026-11-11T10:05:00Z` are valid recording timestamps. A space instead of T
or an offset of +15:00 is invalid. The six-digit fractional-second limit
belongs to referenceTime and does not apply to recordedAt.
For recordedAt, `2026-12-31T24:00:00Z` denotes exactly the same instant as
`2027-01-01T00:00:00Z`: midnight at the start of the next day. The hour 24
requires zero minutes, zero seconds and, if present, only zero fractional
digits. `24:00:00.000` is allowed; `24:00:00.1` is invalid. The original
spelling and any supplied offset are preserved. referenceTime continues to
use clock hours 00–23.
The model does not imply a validity interval.

previousStatus points to the immediately preceding known assignment for the
same object and kind. The predecessor may have the same timestamp or value.
Cycles and predecessors later in UTC are rejected. A strictly intermediate
known timestamp must not be skipped. Equal instants cannot determine an order
by themselves; an explicit predecessor link can supply one. That explicit
order must also be respected when checking for skipped assignments.

For example, A and B both occur at 08:00, with B explicitly following A.
If C occurs at 10:00, its immediate predecessor cannot be A: that would skip
B. Point C to B instead. Equal-time observations without an explicit order
remain unordered; Core does not invent a sequence between them.

The graph need not form one complete linear chain: optional navigation and
several observations may exist. hasCurrentStatus remains optional (0..1 per
object and kind). When present, it must identify the uniquely latest known
assignment in the supplied data and also be explicitly linked by hasStatus.

Compare referenceDate and referenceTime as instants including UTC offsets.
A later instant supersedes an earlier one. At equal instants, explicit
previousStatus links, including a chain of links, establish order. The current
assignment must follow every other assignment at that latest instant. If any
latest observations remain unordered, omit hasCurrentStatus until their order
is resolved. This also applies when they report the same value. Ambiguity at
older instants does not prevent a unique later statement from being current.

| Statement | Business time (UTC) | Recorded at (UTC) | Current selection |
| --- | --- | --- | --- |
| Shipped | 09:00 | 13:00 | Not permitted while the later delivery statement is known |
| Delivered | 12:00 | 12:05 | Permitted; still optional |

For an equal-time example, A and B both occur at 12:00. If B points to A via
previousStatus, B can be current. Without a known order, neither may be
selected. A more recent recordedAt, a preferred status value or an IRI does
not break the tie.

Applications set, update or remove the current link when data changes. SHACL
only checks it and does not automatically modify the graph. "Latest known"
refers to the supplied snapshot, not unknown reports elsewhere. Status
assignments describe reported states; scheduled future activation is outside
this MVP. Validation does not use the current wall-clock time.

See the [current status example](../examples/current-status-selection.ttl).

## 4. Conditions and Measurements

hasCondition refers to an existing vso:AssignedProperty. The measured object
owns the assignment through vso:hasProperty; it may differ from the owner of
the status. The assignment has one definition reference and one state.
The state has one value and, in the ISOProps profile, one allowed unit.

The ISOProps definition specifies the datatype and allowed units. Mapped
literal values must also be valid for their datatype: writing
`"warm"^^xsd:decimal` does not turn the word into a number. Reference
an exact definition revision. For a new measurement, create a new assignment
and state; do not overwrite values referenced by historical status statements.
This retention rule is an application responsibility across snapshots.

## 5. Minimal Example

A delivery was shipped at 10:00 in UTC+01:00:

```turtle
@prefix s: <https://www.construct-x.org/ontology/status#> .
@prefix kind: <https://www.construct-x.org/vocab/status-kind#> .
@prefix value: <https://www.construct-x.org/vocab/status-value#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/status/> .

ex:delivery s:hasStatus ex:report1 .
ex:report1 a s:StatusAssignment ;
    s:hasStatusKind kind:TransportStatus ;
    s:hasStatusValue value:Shipped ;
    s:referenceDate "2026-11-10"^^xsd:date ;
    s:referenceTime "10:00:00+01:00"^^xsd:time .
```

The vocabulary files provide the kind and value definitions. The
[complete condition example](../examples/status-with-condition.ttl) adds a
temperature value of 8.0 °C without introducing a separate Condition object.
