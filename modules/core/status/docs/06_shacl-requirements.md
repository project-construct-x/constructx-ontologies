# Status SHACL Requirements

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Validation Contract

The caller supplies a graph containing the status owners, statements and
referenced context. The validator loads the pinned local ontologies,
reference vocabularies and scoped dependency shapes. Explicit typing and
hasStatus membership are required; no inference is assumed.

Missing local dependencies or unexpected dependency versions are setup errors.
An unresolved external term is a data/reference error; supply its definition
and, for values, the compatibility link. The validator does not fetch URLs.

## 2. Rule Catalog

| Rule ID | Named shape or constraint | Requirement |
| --- | --- | --- |
| `STATUS-001` | `StatusAssignmentShape` | A status assignment must be an IRI typed as StatusAssignment. |
| `STATUS-010` | `OwnerShape` | Each assignment must have exactly one explicit hasStatus owner. |
| `STATUS-020` | `KindShape` | Exactly one IRI-valued StatusKind is required; provide referenced vocabulary data. |
| `STATUS-021` | `ValueShape` | Exactly one IRI-valued StatusValue is required; provide referenced vocabulary data. |
| `STATUS-023` | `ReasonShape` | Every optional reason must be a defined StatusReason IRI; kind applicability is not required. |
| `STATUS-030` | `ReferenceDateShape` | Exactly one valid calendar date (YYYY-MM-DD) is required; the offset belongs to referenceTime. |
| `STATUS-031` | `ReferenceTimeShape` | Exactly one valid clock time with explicit UTC offset (Z or ±hh:mm, at most 14:00) and at most six fractional second digits is required. |
| `STATUS-032` | `RecordedAtShape / RecordedAtEndOfDayConstraint` | recordedAt is optional (0..1). A supplied value must be a valid xsd:dateTime with a T separator; an optional UTC offset must be Z or ±hh:mm, at most 14:00 in either direction. End-of-day 24:00:00 is supported with only zero fractional digits and a valid calendar date. |
| `STATUS-033` | `DescriptionShape` | description must be plain or language-tagged text. |
| `STATUS-034` | `ReasonTextShape` | reasonText must be plain or language-tagged text. |
| `STATUS-040` | `ReporterShape` | reportedBy must be at most one Agent IRI (known subclasses are supported). |
| `STATUS-050` | `PreviousShape` | previousStatus must be at most one StatusAssignment IRI. |
| `STATUS-070` | `ConditionShape` | A condition must satisfy the VSO and ISOProps contracts. |
| `STATUS-071` | `ConditionStateShape` | The condition state must satisfy the existing VSO state rules. |
| `STATUS-072` | `ConditionDefinitionShape` | The referenced definition must satisfy the existing ISOProps metadata rules. |
| `STATUS-022` | `AllowedValueConstraint` | The selected value must have an explicit hasAllowedStatusValue link from the selected kind. |
| `STATUS-051` | `PreviousContextConstraint` | The previous assignment must belong to the same resource and status kind. |
| `STATUS-052` | `HistoryCycleConstraint` | previousStatus must not form a cycle, including self-links. |
| `STATUS-053` | `HistoryTimeConstraint` | The predecessor must not be later than the assignment when UTC offsets are taken into account. |
| `STATUS-054` | `ImmediatePreviousConstraint` | Reject a skipped assignment ordered between the endpoints by time or explicit predecessor links, for the same owner and kind. |
| `STATUS-060` | `HasStatusShape` | hasStatus must reference a typed StatusAssignment IRI. |
| `STATUS-061` | `HasCurrentStatusShape` | hasCurrentStatus must reference a typed StatusAssignment IRI. |
| `STATUS-062` | `CurrentMembershipConstraint` | A current assignment must also be explicitly linked by hasStatus from this resource. |
| `STATUS-063` | `CurrentKindUniquenessConstraint` | At most one current assignment per resource and status kind is allowed. |
| `STATUS-064` | `CurrentLatestConstraint` | A current selection must not be superseded by a later business instant or an explicit successor at the same instant, for the same object and kind. |
| `STATUS-065` | `CurrentUnambiguousConstraint` | Equal-time assignments competing with the current selection must have a known predecessor order; unresolved latest ties prohibit a current link. |
| `STATUS-080` | `KindConceptShape / ValueConceptShape / ReasonConceptShape` | Vocabulary references must be correctly typed IRIs. |
| `STATUS-081` | `AllowedValueLinkShape` | An allowed value must be a StatusValue IRI. |
| `STATUS-082` | `AllowedReasonLinkShape` | An applicability declaration must reference a StatusReason IRI. |
| `STATUS-VOCAB-001` | `ManagedMetadataPolicyShape` | Managed vocabulary metadata policy. |
| `STATUS-VOCAB-010` | `PreferredLabelShape` | Provide at least one language-tagged preferred label, unique per language and distinct from alternative labels. |
| `STATUS-VOCAB-011` | `DefinitionShape` | Provide at least one nonempty language-tagged definition. |
| `STATUS-VOCAB-012` | `NotationShape` | Provide exactly one nonempty string code. |
| `STATUS-VOCAB-013` | `SchemeMembershipShape` | Provide at least one IRI-valued, typed concept scheme membership. |
| `STATUS-VOCAB-014` | `AlternativeLabelShape` | Alternative labels must be nonempty language-tagged text. |
| `STATUS-VOCAB-015` | `ScopeNoteShape` | Scope notes must be nonempty language-tagged text. |
| `STATUS-VOCAB-016` | `UniqueNotationConstraint` | A managed code must be unique among concepts in each scheme. |

Own-vocabulary metadata errors may be nested under STATUS-VOCAB-001.
Condition diagnostics preserve existing VSO-* and ISOP-* identifiers as well
as the Status wrapper identifiers.

## 3. Historical Consistency

History checks use the business instants obtained from the calendar date and
offset-bearing clock time. recordedAt does not influence ordering.
Its datatype and lexical format are both checked: a literal marked as
xsd:dateTime is still invalid if it uses a space instead of T, omits seconds,
or supplies an offset outside ±14:00. Calendar and clock validity are also
checked. recordedAt and its UTC offset remain optional; fractional seconds
are allowed without the six-digit limit used for referenceTime.
End-of-day notation is accepted: `2026-12-31T24:00:00Z` denotes
`2027-01-01T00:00:00Z`. The end-of-day branch checks the exact xsd:dateTime
datatype and the original calendar date as well as the lexical pattern.
Minutes, seconds and fractional digits must all be zero with hour 24.
The input graph is preserved, including its literal spellings. Providing
both equivalent spellings on one assignment still violates the maximum
of one recordedAt value. referenceTime retains its 00–23 hour range.
The graph may contain repeated values and equal instants. A previousStatus
link must not skip a known statement ordered between its endpoints for the
same owner and kind. Ordering combines timestamps with explicit predecessor
paths, including ties. Core does not require a complete chain or a current
assignment. Unordered equal-time observations remain allowed.

referenceTime supports up to six fractional digits. For example,
08:00:00.000001Z precedes 08:00:00.000002Z. A seventh fractional digit fails
STATUS-031 so the validator cannot silently lose a meaningful difference.

hasCurrentStatus remains optional. If present, the linked assignment must be
the uniquely latest known one for its owner and kind. Compare complete
business instants, not local clock strings or recordedAt. An explicit
previousStatus path resolves equal-time order; the selected assignment must
follow all its equal-time competitors. Unordered ties are acceptable when
no current link is set. Older ambiguous observations do not affect a unique
later maximum. SHACL does not set or update the link.

SHACL validates one supplied graph. It cannot prove that a store has not
overwritten a previously published status or measurement; retention is a
separate application requirement.

## 4. Condition Requirements

Reuse the existing AssignedPropertyShape, PropertyStateShape,
ISOPropsAssignmentShape and ISOPropsPropertyShape. Validate all of the
referenced definition metadata, not only the selected numerical value.

The shared ISOProps rule ISOP-VALUE-002 checks actual literal validity for
the mapped datatypes, including integer bounds and numeric lexical forms.
For example, `"warm"^^xsd:decimal` and `"128"^^xsd:byte` are invalid even
though they name a permitted datatype. COMPLEX values with other datatypes
remain opaque; their application-specific structure is not checked here.

The ISOProps profile requires one unit even for dimensionless values;
the existing unit:UNITLESS pattern applies where appropriate.
Do not add a second owner or several states to one VSO assignment.

## 5. Examples of Acceptance and Rejection

| Situation | Result |
| --- | --- |
| Status with date and 10:00:00+01:00; no recordedAt | Valid |
| recordedAt `2026-11-11T10:05:00` typed as xsd:dateTime, without an offset | Valid |
| recordedAt `2026-11-11T10:05:00Z` or `2026-11-11T10:05:00+14:00` typed as xsd:dateTime | Valid |
| recordedAt `2026-12-31T24:00:00Z` typed as xsd:dateTime | Valid; midnight at the beginning of 1 January 2027 |
| recordedAt `2024-02-29T24:00:00.000` typed as xsd:dateTime, without an offset | Valid; midnight at the beginning of 1 March 2024 |
| recordedAt `2026-11-11T24:01:00Z` or `2026-11-11T24:00:00.1Z` typed as xsd:dateTime | Invalid: STATUS-032; hour 24 requires all smaller components to be zero |
| recordedAt `2026-02-29T24:00:00Z` typed as xsd:dateTime | Invalid: STATUS-032; 2026 is not a leap year |
| recordedAt `2026-11-11 10:05:00Z` typed as xsd:dateTime | Invalid: STATUS-032; the separator must be T |
| recordedAt `2026-11-11T10:05:00+15:00` typed as xsd:dateTime | Invalid: STATUS-032; offset exceeds 14:00 |
| recordedAt `2026-02-29T10:05:00Z` typed as xsd:dateTime | Invalid: STATUS-032; the calendar date does not exist |
| Status with 10:00:00 and no offset | Invalid: STATUS-031 |
| TransportStatus with Passed | Invalid: STATUS-022 |
| TemperatureInspection with a typed unassigned reason | Valid |
| Two current statuses of the same kind on one object | Invalid: STATUS-063 |
| Reporter typed as Core Person with Person ontology context | Valid |
| Reporter typed as Core Organization with Organization ontology context | Valid |
| Only a Person/Organization type is supplied, without the class context | Invalid: STATUS-040; the Agent subclass relationship is not known |
| One assignment references both a Person and an Organization as reporters | Invalid: STATUS-040; at most one reporter is allowed |
| Shipped at 09:00Z selected while Delivered at 12:00Z is known | Invalid: STATUS-064, even if Shipped was recorded later |
| A and B at 12:00Z, B follows A, A selected | Invalid: STATUS-064 |
| A and B at 12:00Z, B follows A, B selected | Valid |
| A and B at 12:00Z, no known order, either selected | Invalid: STATUS-065, even if both report the same value |
| The same unordered observations, no current link | Valid |
| Shipped at 09:00Z recorded after Delivered at 12:00Z | Valid; ingestion does not select the current status |
| Temperature defined as REAL, value 8.0, allowed °C | Valid |
| The same definition with value "warm" | Invalid: ISOP-VALUE-001 |
| The same definition with `"warm"^^xsd:decimal` | Invalid: ISOP-VALUE-002 |
| A and B at 08:00, B follows A; C at 10:00 incorrectly points to A | Invalid: STATUS-054 |
| 10:00:00.1234567Z | Invalid: STATUS-031; precision exceeds microseconds |
