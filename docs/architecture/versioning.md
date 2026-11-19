<a id="versionierung"></a>

# Versioning

Each ontology module and reference-data artifact is versioned in a traceable way. Construct-X distinguishes three models.

<a id="1-ontologien-und-shacl-graphen"></a>

## 1. Ontologies and SHACL Graphs

Ontologies and SHACL graphs are versioned as complete graphs using SemVer.

Rules:

- The stable graph IRI remains unchanged.
- Each publication receives a SemVer version IRI.
- Term IRIs do not contain a version number.
- Published versions are immutable.
- The unversioned graph IRI points to the current recommended version.
- Older versions remain accessible through their version IRIs.
- Removed IRIs must never be reused for other terms.

SHACL graphs are organized into named shape sets for each module. This allows
general Core rules and later application profiles to be versioned
independently:

```text
Stable Core shape graph: https://www.construct-x.org/shapes/address/core
Core shape version:      https://www.construct-x.org/shapes/address/core/0.1.0
Shape namespace:         https://www.construct-x.org/shapes/address/core#
```

Address Ontology example:

```text
Ontology IRI: https://www.construct-x.org/ontology/address
Version IRI:  https://www.construct-x.org/ontology/address/0.1.0
Namespace:    https://www.construct-x.org/ontology/address#
```

<a id="2-referenzvokabulare"></a>

## 2. Reference Vocabularies

Reference vocabularies are also versioned as complete graphs using SemVer.

Rules:

- The stable vocabulary IRI remains unchanged.
- Each publication receives a SemVer version IRI.
- Vocabulary terms do not contain a version number.
- Published versions are immutable.
- Wherever possible, terms are deprecated rather than deleted.

Example:

```text
Vocabulary:         https://www.construct-x.org/vocab/wall-type
Vocabulary version: https://www.construct-x.org/vocab/wall-type/1.2.0
Term:               https://www.construct-x.org/vocab/wall-type#ExternalWall
```

A new vocabulary version does not automatically create new IRIs for terms that continue to exist unchanged.

<a id="3-referenzobjekte"></a>

## 3. Reference Objects

Reference objects under `/id/` are versioned individually and do not use SemVer.

Rules:

- A conceptual version of an object has a GUID.
- A revision retains the GUID and increments the revision number.
- A new conceptual version of an object receives a new GUID.
- Published revisions are immutable.
- Normative and reproducible references use the GUID and revision number.

Example:

```text
Current revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000

Exact revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

The SemVer version of a published graph and the revision of a reference object described within it are independent pieces of information.

The detailed rules are defined in `docs/architecture/construct-x-namespace-konzept.md`.
