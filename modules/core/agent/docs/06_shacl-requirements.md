# Domain-Specific SHACL Requirements of the Agent Module

**Status:** No dedicated shape required  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/agent`

## 1. Purpose

This document explains why the Agent module has no executable shape graph despite following the standard documentation structure.

## 2. Shape Set

No Agent Core Shape is defined for version 0.1.0.

## 3. Validation Requirements

`Agent` has no mandatory properties of its own. General validation would therefore express no additional data contract.

## 4. Validation Failure Behavior

There are no Agent-specific error codes. Specific errors arise in the modules that define a relationship or subclass.

## 5. Valid Example

A resource of type `conx-agent:Agent` is valid without any additional information.

## 6. Invalid Example

There is no general invalid Agent example because the Agent core specifies no mandatory information.

## 7. Deliberately Excluded Checks

Names, contact information, addresses, and roles are validated by their respective domain modules.

## 8. Tests

Ontology tests verify the class and its classification as a subclass of `foaf:Agent`.