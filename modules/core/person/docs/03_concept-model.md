# Conceptual Model of the Person Module

**Status:** Confirmed through domain review and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/person`

## 1. Purpose

The model describes the intrinsic core data of a real natural person.

## 2. Model in Plain Language

A Person has names and may have information about birth, citizenship, human sex, gender, identifiers, and identity evidence.

## 3. Terms

The central term is `Person`. Controlled values for `sex` and `gender` are maintained in separate reference vocabularies.

## 4. Relationships

`Person` is a subclass of `Agent`. Contacts, addresses, and organizational relationships are connected through their responsible modules.

## 5. Illustrative Example

> Anna Müller is described once as a Person. Her business telephone number belongs to a contact point; her membership in an office belongs to a Membership. Neither is copied into the Person.

| Person | Related resource | Module |
| --- | --- | --- |
| Anna Müller | `ContactPoint` | `core/contact` |
| Anna Müller | `Membership` | `core/organization` |
| Anna Müller | `Identifier` | `core/identifier` |

## 6. Boundaries

The module describes neither organizations nor the internal structure of credentials or identity documents.

## 7. Decisions

`sex` and `gender` remain separate. Person identifiers use the shared Identifier contract.

The detailed diagram is available at [person-concept-model.md](diagrams/person-concept-model.md).