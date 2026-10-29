# Module Boundaries of the Agent Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Purpose

The Agent core prevents cyclic dependencies between Person and Organization.

## 2. Responsibilities

`core/agent` contains only the shared type `Agent`. Personal data belongs in `core/person`, and organizational data belongs in `core/organization`.

## 3. Dependencies

Person, Organization, and Participation reference Agent. Agent itself does not depend on these modules.

## 4. Deliberate Exclusions

No names, identifiers, contact information, addresses, roles, or permissions are defined in the Agent module.

## 5. Illustrative Example

> A telephone number belongs to a contact point. Even if the contact point is used by an agent, the telephone number does not become an Agent property.

## 6. Integration Rule

New core modules may use Agent when both people and organizations can be meaningful values of the same relationship.