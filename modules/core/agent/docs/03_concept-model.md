# Conceptual Model of the Agent Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Purpose

The conceptual model identifies the common abstraction for entities that act or bear responsibility.

## 2. Model in Plain Language

An Agent is a general actor. Person and Organization are more specific types of this actor.

## 3. Terms

| Term | Meaning |
| --- | --- |
| `Agent` | General actor |
| `Person` | Natural person from `core/person` |
| `Organization` | Collective actor from `core/organization` |

## 4. Relationships

The Agent module defines no domain-specific relationships of its own. Other modules may use `Agent` as a range.

## 5. Illustrative Example

A `Participation` references an `Agent` through `participant`. That agent may be a `Person` or an `Organization`.

A project role can therefore be fulfilled by a person or an organization without defining the role relationship twice.

## 6. Boundaries

Master data remains in Person and Organization. Contact and address relationships likewise remain in their respective domain modules.

## 7. Decisions

The Agent core remains free of properties and therefore requires no dedicated Core Shape.