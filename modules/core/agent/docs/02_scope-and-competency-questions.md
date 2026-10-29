# Scope and Competency Questions of the Agent Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Purpose

The module provides a common superclass for actors. This allows relationships to reference people and organizations without requiring two separate properties.

## 2. Confirmed Scope

The core contains only `conx-agent:Agent` and its conservative classification as a subclass of `foaf:Agent`.

## 3. Out of Scope

Names, addresses, contact information, memberships, and technical user accounts do not belong in the Agent core.

## 4. Competency Questions

1. Can a person be used as a general actor?
2. Can an organization use the same actor relationship?
3. Does specific master data remain in the responsible modules?

All three questions are answered affirmatively.

## 5. Illustrative Example

> A document can be issued by an actor. Whether the actor is a person or an organization is described by its more specific type.

A document references an `Agent` through an “issued by” relationship. The agent's more specific type is `Person` or `Organization`.

## 6. Modeling Decision

The Agent core is deliberately kept small. Details are provided in the [Domain Specification](10_agent-specification.md).

## 7. Acceptance Criteria

Person and Organization are subclasses of Agent; the Agent core does not introduce properties outside its scope.
