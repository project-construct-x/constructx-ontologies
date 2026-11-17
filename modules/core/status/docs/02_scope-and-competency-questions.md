# Status Scope and Competency Questions

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Included Scope

The module describes the business-time state of any resource. An assignment
has one owner, kind, value, reference date and offset-bearing reference time.
Optional information includes descriptions, reasons, a reporting Agent,
recording time, an immediate predecessor and VSO/ISOProps conditions.

Multiple kinds may coexist on one object. The caller may optionally link the
uniquely latest known assignment per kind through hasCurrentStatus. The
validator checks business time and, for equal instants, explicit predecessor
order. Additional vocabulary concepts may be supplied by other organizations.

## 2. Competency Questions

| Question | Model path |
| --- | --- |
| What status statements concern this object? | hasStatus |
| Which dimension does this statement describe? | hasStatusKind |
| What state was reported? | hasStatusValue |
| At what business time was it reported to apply? | referenceDate + referenceTime |
| Which uniquely latest known statement is explicitly linked as current for a kind? | hasCurrentStatus + hasStatusKind, checked against business time and predecessor order |
| What was the immediately preceding known statement? | previousStatus |
| Why was the state reported? | hasStatusReason / reasonText |
| Which actor reported it? | reportedBy |
| Which measurement supports the statement? | hasCondition through VSO to state and ISOProps definition |

## 3. Exclusions and Limits

No subject property, Condition class, numeric interval, workflow transition
catalog, correction relation or automatic migration of Document status exists.
A predecessor link is not an allowed transition between vocabulary values.

An absence of hasCurrentStatus does not mean no status exists. A missing
previousStatus does not assert that the assignment is the first ever.
The graph is not required to contain a complete lifetime history.
An unresolved latest tie prevents a current link but does not invalidate
the history itself. Planned future validity and automatic activation of
statuses are outside this MVP; comparisons use the supplied snapshot and
do not depend on the validator's wall clock.
SHACL validates a supplied snapshot; preventing later overwrites requires
the application to preserve published assignments and measurements.

## 4. Example Scenario

A delivery has transport status Shipped at 10:00+01:00 and temperature inspection
Failed at 10:05+01:00. Both can be current because they describe different
kinds. Two current TemperatureInspection assignments would fail validation.
