# Term Catalog of the Agent Module

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Purpose

The catalog documents the deliberately minimal set of public terms.

## 2. Namespace

`https://www.construct-x.org/ontology/agent#` with the prefix `conx-agent`.

## 3. Classes

| Class | Definition |
| --- | --- |
| `conx-agent:Agent` | Entity that can act, bear responsibility, or be referenced as a participant |

## 4. Properties

The module defines no properties of its own.

## 5. Controlled Values

The module has no reference vocabulary.

## 6. Illustrative Example

```turtle
ex:anna a conx-person:Person .
```

Since `Person` is a subclass of `Agent`, `ex:anna` can be used wherever an Agent is expected.

## 7. Exclusions

Specialized agent types are added in their respective modules only when a domain-specific need has been confirmed.