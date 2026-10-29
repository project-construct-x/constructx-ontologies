# Source Analysis of the Agent Module

**Status:** Consolidated analysis baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 27 August 2026  
**Scope:** `core/agent`

## 1. Purpose and Method

The analysis examined which common actor concept could connect people and organizations without merging their master data.

## 2. Sources Evaluated

| Source | Contribution |
| --- | --- |
| FOAF | General concept `foaf:Agent` |
| SEMIC Core Vocabularies | European agent and person models |
| W3C ORG | Agents in memberships and organizations |

## 3. Assessment

`foaf:Agent` supports broad interoperability. A local Construct-X concept nevertheless remains useful so that internal modules can reference a controlled common superclass.

## 4. Outcome

`conx-agent:Agent` is implemented as a subclass of `foaf:Agent`. An equivalence assertion was avoided because Construct-X maintains tighter control over the subset used.

## 5. Illustrative Example

> A participation references an actor. The same structure can therefore accommodate both “Anna Müller” and “Beispiel Bau GmbH.”

The detailed rationale is provided in the [Agent Specification](10_agent-specification.md).
