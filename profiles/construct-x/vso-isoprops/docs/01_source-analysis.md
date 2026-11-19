# ISOProps v2.2 Source Analysis

**Status:** Consolidated analysis baseline  
**Version:** 0.1.0  
**As of:** 1 September 2026  
**Scope:** `profile/vso-isoprops`

## 1. Reviewed Source

The profile was derived from the supplied `isoprops.ttl` source file. The source graph declares:

- ontology IRI: `https://w3id.org/isoprops`,
- version IRI: `https://w3id.org/isoprops`,
- version info: `v2.2`,
- preferred namespace: `https://w3id.org/isoprops#`,
- preferred prefix: `isoprops`,
- modified date: `2025-01-15`,
- no `owl:imports` statements.

The profile references ISOProps but does not copy or import the external ontology.

## 2. Integration Terms

The VSO property reference targets `isoprops:Property`. The integration profile uses the following ISOProps metadata:

- `isoprops:globallyUniqueIdentifier`,
- `isoprops:versionNumber`,
- `isoprops:revisionNumber`,
- `isoprops:status`,
- `isoprops:dataType`,
- `isoprops:hasUnit`.

ISOProps v2.2 defines the data-type tokens `BOOLEAN`, `INTEGER`, `RATIONAL`, `REAL`, `COMPLEX`, `STRING` and `DATETIME`. It does not supply a complete normative RDF datatype mapping. The approved conservative mapping is therefore documented and implemented by this profile.

## 3. Scope Boundary

This profile validates the interoperability contract between VSO assignments and ISOProps property definitions. It does not reproduce every ISO 23386 metadata restriction from the ISOProps T-Box and does not introduce domain-specific property rules.
