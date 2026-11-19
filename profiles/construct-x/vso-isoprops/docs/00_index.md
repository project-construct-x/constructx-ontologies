# Construct-X VSO ISOProps Profile

**Status:** Draft and implemented  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `profile/vso-isoprops`

## 1. Overview

This profile validates VSO property assignments against ISOProps v2.2 property
definitions.

## 2. Composition

The profile is applied together with:

- VSO ontology `https://www.construct-x.org/ontology/vso/0.1.0`;
- VSO Core Shapes `https://www.construct-x.org/shapes/vso/core/0.1.0`;
- profile Shapes `https://www.construct-x.org/shapes/vso/isoprops/0.1.0`.

## 3. Validation Contract

The profile requires versioned ISOProps metadata, applies the approved
conservative datatype mapping, and checks that the used QUDT unit is allowed by
the referenced definition.
Mapped literal contents are checked as well: declaring the word "warm" as
an xsd:decimal does not make it a valid measurement. This validation gap was
corrected in the draft on 11 November 2026; see ISOP-VALUE-002.

> A measured property whose ISOProps definition permits metres is valid when
> its VSO state uses the matching QUDT metre unit. A unit not listed by the
> definition violates the profile.

## 4. Documentation

- [Source Analysis](01_source-analysis.md)
- [SHACL Requirements](02_shacl-requirements.md)

## 5. Boundaries

Domain-specific property restrictions remain outside this profile. The profile
adds ISOProps interoperability rules without changing the open VSO Core.
