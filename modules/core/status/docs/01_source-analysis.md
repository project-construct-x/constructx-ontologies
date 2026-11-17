# Status Source Analysis

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Sources

- [UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/UBL-2.5.html):
  StatusType and ConditionType in the common aggregate schema.
- [SKOS Reference](https://www.w3.org/TR/skos-reference/):
  concepts, multilingual labels, codes and concept schemes.
- Existing [VSO Core](../../vso/docs/00_index.md) and
  [VSO/ISOProps profile](../../../../profiles/construct-x/vso-isoprops/docs/00_index.md).
- Existing [Participation](../../participation/docs/00_index.md) as a repository
  pattern for qualified assignments and open reference terms.

The UBL source reviewed is CS01 dated 15 April 2026; this is not a claim
about later UBL releases.

## 2. Selected Mapping

| UBL information | Status Core treatment |
| --- | --- |
| ConditionCode on StatusType | A StatusValue concept selected by hasStatusValue |
| ReferenceDate / ReferenceTime | Mandatory referenceDate and referenceTime, stricter than the UBL base schema |
| StatusReasonCode | Zero or more StatusReason concepts; intentionally permits multiple reasons |
| StatusReason / Description | reasonText / description |
| Condition.AttributeID and Measure | ISOProps definition reference and VSO state value with unit |
| MinimumMeasure / MaximumMeasure | Outside this MVP |
| XML parent context | Object-to-assignment hasStatus relation |
| Explicit status kind | Added by Construct-X to separate independent status dimensions |

This module is not a lossless implementation of every UBL StatusType field.
Attachments, substatus, sequence fields, percentages and indicators are not
introduced by this MVP. A numeric code mapping requires an explicit external
code-list mapping; textual labels alone do not establish equivalence.

## 3. Design Decisions

Status kind, value and reason are distinct SKOS concept classes. Their
vocabularies are reference data outside the ontology. A kind explicitly
permits its values; its reason links are non-exhaustive. Current and previous
status links are optional. A current link, when present, must identify the
uniquely latest known assignment per object and kind. This is based on
business instants and explicit predecessor order for equal instants, not
on recordedAt. Unresolved latest ties require the current link to be omitted.
No new Condition class is introduced.

VSO retains its general contract. The existing ISOProps profile supplies
definition metadata, datatype and unit checks for status conditions.

## 4. Example

"Temperature inspection failed because the temperature was too high" contains
three concepts: TemperatureInspection, Failed and TemperatureExceeded.
The observed 8.0 °C is a VSO value. The reason does not itself define a
temperature threshold, and the measured value does not prove compliance
without application-specific acceptance criteria.
