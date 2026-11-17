# Status Concept Diagram

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Complete Model

The metadata cardinalities on the three concept classes describe our managed
vocabularies. These classes specialize skos:Concept. Label, definition,
alternative-label and scope-note properties use the skos: prefix. Preferred
labels are unique per language. Conditions reuse existing VSO/ISOProps classes.

```mermaid
flowchart TB
  O["Object: example delivery"]
  S["StatusAssignment<br/>referenceDate: date [1]<br/>referenceTime: time + UTC offset [1]<br/>recordedAt: dateTime [0..1]<br/>description: text [0..n]<br/>reasonText: text [0..n]"]
  P["Previous StatusAssignment<br/>Same contract"]
  O -->|"hasStatus [0..n]; one owner per assignment"| S
  O -->|hasStatus| P
  O -->|"hasCurrentStatus [0..1 per kind]"| S
  S -->|"previousStatus [0..1]"| P
  S -->|"reportedBy [0..1]"| A["Agent"]
  S -->|"hasStatusKind [1]"| K["StatusKind<br/>prefLabel [1..n]<br/>definition [1..n]<br/>notation [1]<br/>altLabel [0..n]<br/>scopeNote [0..n]"]
  S -->|"hasStatusValue [1]"| V["StatusValue<br/>prefLabel [1..n]<br/>definition [1..n]<br/>notation [1]<br/>altLabel [0..n]<br/>scopeNote [0..n]"]
  S -->|"hasStatusReason [0..n]"| R["StatusReason<br/>prefLabel [1..n]<br/>definition [1..n]<br/>notation [1]<br/>altLabel [0..n]<br/>scopeNote [0..n]"]
  K -->|"hasAllowedStatusValue [0..n]"| V
  K -->|"hasAllowedStatusReason [0..n]; open"| R
  K -->|"skos:inScheme [1..n]"| KS["Vocabulary of status kinds<br/>skos:ConceptScheme"]
  V -->|"skos:inScheme [1..n]"| VS["Vocabulary of status values<br/>skos:ConceptScheme"]
  R -->|"skos:inScheme [1..n]"| RS["Vocabulary of status reasons<br/>skos:ConceptScheme"]
  S -->|"hasCondition [0..n]"| AP["vso:AssignedProperty"]
  G["Measured resource: goods"] -->|vso:hasProperty| AP
  AP -->|"vso:hasPropertyReference [1]"| D["isoprops:Property<br/>Exact definition revision<br/>dataType: REAL"]
  AP -->|"vso:hasPropertyState [1]"| PS["vso:PropertyState<br/>schema:value [1]: 8.0"]
  D -->|"isoprops:hasUnit [1..n]"| U["QUDT unit: degree Celsius"]
  PS -->|"vso:hasUsedUnit [1]"| U

```

## 2. Reading Example

Start at the delivery. Follow hasStatus to a statement, then read its kind
as TemperatureInspection and its value as Failed. The reason may be
TemperatureExceeded. Following hasCondition leads to the goods' temperature
measurement, 8.0 °C, and the referenced ISOProps definition.

The same delivery can independently have a TransportStatus statement with
value Shipped. At most one statement per kind is selected through
hasCurrentStatus, and that statement must be the uniquely latest known one
for the delivery and kind. No subject property is needed.

## 3. History and Boundaries

previousStatus is the optional immediate known predecessor for the same owner
and kind. Explicit predecessor order also applies when timestamps tie.
referenceTime supports at most six fractional second digits. Current
selection is explicit and optional, and must match the uniquely latest known
business-time statement. recordedAt does not affect selection. If latest
timestamps tie, explicit predecessor order must resolve the tie before a
current link can be set. For example, B may be current when both A and B are
at 12:00 and B has previousStatus A; without that known order, omit the link.
Reasons remain open. No correction, interval or workflow class is shown
because these are outside this MVP.
