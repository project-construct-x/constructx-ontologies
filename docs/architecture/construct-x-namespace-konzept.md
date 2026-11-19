<a id="construct-x-namespace--und-iri-konzept"></a>

# Construct-X Namespace and IRI Concept

Document date: 2026-08-18

This document defines the binding namespace, IRI, and versioning concept for the Construct-X ontology network. It also addresses readers without in-depth Semantic Web knowledge and explicitly distinguishes ontologies, SHACL graphs, reference vocabularies, and persistent reference objects.

<a id="inhaltsverzeichnis"></a>

## Table of Contents

1. [Decision Summary](#1-decision-summary)
2. [Authority and Guiding Principle](#2-authority-and-guiding-principle)
3. [Established Models](#3-established-models)
4. [Public Namespaces and Resource Types](#4-public-namespaces-and-resource-types)
5. [Prefix and Naming Conventions](#5-prefix-and-naming-conventions)
6. [Versioning Rules](#6-versioning-rules)
7. [Repository Structure and Public IRIs](#7-repository-structure-and-public-iris)
8. [Dereferencing and Delivery](#8-dereferencing-and-delivery)
9. [Catalog Following the QUDT Model](#9-catalog-following-the-qudt-model)
10. [Examples from Current Modules](#10-examples-from-current-modules)
11. [Technical and Organizational Validation Rules](#11-technical-and-organizational-validation-rules)
12. [Identified Deviations and Adjustments](#12-identified-deviations-and-adjustments)
13. [Binding Recommendation](#13-binding-recommendation)

<a id="1-entscheidung-in-kurzform"></a>

## 1. Decision Summary

The provisional canonical authority is:

```text
https://www.construct-x.org
```

Construct-X uses dereferenceable HTTPS IRIs and does not define its own URNs. URNs may be used only when required by an integrated external system.

The central patterns are:

```text
Ontology:
https://www.construct-x.org/ontology/{module}

Ontology version:
https://www.construct-x.org/ontology/{module}/{semver}

Ontology term:
https://www.construct-x.org/ontology/{module}#{localName}

SHACL graph:
https://www.construct-x.org/shapes/{module}/{shape-set}

SHACL version:
https://www.construct-x.org/shapes/{module}/{shape-set}/{semver}

SHACL shape:
https://www.construct-x.org/shapes/{module}/{shape-set}#{localName}

Stable reference vocabulary:
https://www.construct-x.org/vocab/{vocabulary}

Specific vocabulary version:
https://www.construct-x.org/vocab/{vocabulary}/{semver}

Stable vocabulary term:
https://www.construct-x.org/vocab/{vocabulary}#{localName}

Reference object at its current revision:
https://www.construct-x.org/id/{type}/{guid}

Exact revision of a reference object:
https://www.construct-x.org/id/{type}/{guid}/revision/{revision}
```

Ontologies and reference vocabularies are published as complete graphs and versioned using SemVer. Their term IRIs remain independent of versions. Reference objects under `/id/`, by contrast, have an individual lifecycle. A revision retains its GUID and increments the revision number. A new conceptual version receives a new GUID and references the version it replaces.

Example of a reference vocabulary:

```text
Stable vocabulary:
https://www.construct-x.org/vocab/wall-type

Vocabulary version:
https://www.construct-x.org/vocab/wall-type/1.2.0

Stable vocabulary term:
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

Example of a reference object:

```text
Current revision of a property version:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000

Exact revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

The IRI without a revision segment may point to the current revision of the conceptual version identified by the GUID. Normative, audit-related, or reproducible references must always use the specific revision IRI.

<a id="2-authority-und-grundsatz"></a>

## 2. Authority and Guiding Principle

Before the first stable public release, it must be verified that `https://www.construct-x.org` can serve as the permanent canonical authority.

Public IRIs should remain stable in terms of their domain meaning. Repository categories such as `core`, `domain`, and `alignments` must not be part of public ontology IRIs. The module under `modules/core/address` is therefore publicly identified as `https://www.construct-x.org/ontology/address`, not as `/ontology/core/address`.

<a id="3-orientierung-an-etablierten-vorbildern"></a>

## 3. Established Models

Construct-X follows established Linked Data and OWL principles: stable IRIs for terms, versioned graphs for published releases, and traceable catalog entries for publications.

### 3.1 QUDT

QUDT separates stable term IRIs from versioned graph publications. Construct-X adopts this principle for ontologies, SHACL graphs, and reference vocabularies.

| Area | Stable IRI | Versioned IRI | Example |
| --- | --- | --- | --- |
| Ontology graph | yes | yes | `https://www.construct-x.org/ontology/vso/0.1.0` |
| SHACL graph | yes | yes | `https://www.construct-x.org/shapes/address/core/0.2.0` |
| Reference vocabulary | yes | yes | `https://www.construct-x.org/vocab/wall-type/1.0.0` |
| Term | yes | no | `https://www.construct-x.org/vocab/wall-type#ExternalWall` |

Construct-X also applies QUDT's principle of stable term IRIs to reference vocabularies. A new publication of a vocabulary graph therefore does not create new IRIs for terms that continue to exist unchanged.

Example: If a new wall type is added to the `wall-type` vocabulary in version `1.1.0`, the existing term `https://www.construct-x.org/vocab/wall-type#ExternalWall` remains unchanged.

<a id="4-oeffentliche-namensraeume-und-ressourcenarten"></a>

## 4. Public Namespaces and Resource Types

<a id="41-oeffentliche-namensraeume"></a>

### 4.1 Public Namespaces

| Artifact or resource | Pattern | Example |
| --- | --- | --- |
| Ontology series | `/ontology/{module}` | `https://www.construct-x.org/ontology/vso` |
| Term namespace | `/ontology/{module}#` | `https://www.construct-x.org/ontology/vso#AssignedProperty` |
| Specific ontology version | `/ontology/{module}/{semver}` | `https://www.construct-x.org/ontology/vso/0.1.0` |
| SHACL graph | `/shapes/{module}/{shape-set}` | `https://www.construct-x.org/shapes/address/core` |
| Shape namespace | `/shapes/{module}/{shape-set}#` | `https://www.construct-x.org/shapes/address/core#AddressShape` |
| Specific SHACL version | `/shapes/{module}/{shape-set}/{semver}` | `https://www.construct-x.org/shapes/address/core/0.2.0` |
| Reference vocabulary | `/vocab/{vocabulary}` | `https://www.construct-x.org/vocab/wall-type` |
| Specific vocabulary version | `/vocab/{vocabulary}/{semver}` | `https://www.construct-x.org/vocab/wall-type/1.2.0` |
| Reference vocabulary term | `/vocab/{vocabulary}#{localName}` | `https://www.construct-x.org/vocab/wall-type#ExternalWall` |
| Reference object at its current revision | `/id/{type}/{guid}` | `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000` |
| Exact revision of a reference object | `/id/{type}/{guid}/revision/{revision}` | `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2` |
| Alignment | `/alignment/{alignment}` | `https://www.construct-x.org/alignment/address-vcard` |
| Network catalog | `/catalog` | `https://www.construct-x.org/catalog` |
| Documentation | `/docs/{module}` | `https://www.construct-x.org/docs/vso` |

The base IRI of a reference object, for example `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000`, represents the conceptual version of the reference object and may point to its current revision. The exact revision IRI, for example `.../revision/2`, permanently identifies an immutable state. Audits, references in standards, tests, and reproducible data processing must use the exact revision IRI.

<a id="42-ressourcenarten"></a>

### 4.2 Resource Types

- `/ontology/` contains T-Box terms such as classes, ObjectProperties, DataProperties, and formal axioms.
- `/vocab/` contains controlled A-Box reference data such as selection values, status values, or classification terms.
- `/id/` contains independently managed reference objects with a stable identity and their own lifecycle.

Operational A-Box resources, such as specific buildings, walls, or people, receive their IRIs from the respective data holder rather than from the Construct-X ontology network.

<a id="43-t-box-begriffe-und-referenzdaten-trennen"></a>

### 4.3 Separating T-Box Terms and Reference Data

T-Box terms describe domain classes and properties. Reference data describes values, catalog entries, or real-world or managed reference objects.

Examples:

```text
Wall class:
https://www.construct-x.org/ontology/wall#Wall

Selection value "External wall":
https://www.construct-x.org/vocab/wall-type#ExternalWall

ISOProps property definition:
https://www.construct-x.org/id/property/{guid}

Specific wall belonging to a data holder:
https://data.example.com/building/123/wall/456
```

The GUID identifies a conceptual version of the reference object. Changes within that conceptual version are managed as revisions and retain the GUID. When a new conceptual version is created, a new GUID is assigned. The new version references the previously valid version.

Wall-height revision example: If only an English label is added to a `WallHeight` property version, this can be treated as a new revision. The GUID remains unchanged, and the revision number increases, for example, from `1` to `2`.

```text
Revision 1:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/1

Revision 2:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Both states remain accessible. Revision `1` documents the originally published state, and revision `2` documents the state with the added English label.

Example of a new conceptual version:

```text
Previous version:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2

New conceptual version:
https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1
```

The new version references the old version using `dcterms:replaces`:

```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1>
    dcterms:replaces
        <https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2> .
```

<a id="5-praefix--und-benennungskonventionen"></a>

## 5. Prefix and Naming Conventions

Construct-X ontologies use prefixes following this pattern:

```text
conx-{module-abbreviation}
```

The module abbreviation must be short, unique, stable, and entirely lowercase. The hyphen is mandatory.

Examples:

```turtle
@prefix conx-vso:  <https://www.construct-x.org/ontology/vso#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-org:  <https://www.construct-x.org/ontology/organization#> .
@prefix conx-doc:  <https://www.construct-x.org/ontology/document#> .
@prefix conx-unit: <https://www.construct-x.org/ontology/units#> .
```

Prefixes of imported or referenced ontologies, such as `owl`, `rdf`, `rdfs`, `sh`, `opm`, `qudt`, `schema`, `vcard`, `org`, `locn`, `skos`, and `isoprops`, remain unchanged.

New Construct-X terms use:

- Classes: `UpperCamelCase`, for example `PhysicalObject`, `PropertyState`, or `PostalAddress`.
- ObjectProperties: `lowerCamelCase`, phrased as a verbal relationship, for example `hasAddress`, `hasPropertyReference`, `isPartOf`, `belongsToOrganization`, or `containsElement`.
- DataProperties: `lowerCamelCase`, without a relationship prefix such as `has` or `is`, for example `name`, `revisionNumber`, `creationDate`, or `globallyUniqueIdentifier`.
- SHACL shapes: class name followed by `Shape`, for example `AddressShape`.

Local names contain no spaces, umlauts, or language-dependent name components. Translations are provided through labels with language tags. These rules do not apply retroactively to terms from imported ontologies.

<a id="6-versionierungsregeln"></a>

## 6. Versioning Rules

Construct-X distinguishes three versioning models:

1. Ontologies and SHACL graphs are versioned as complete graphs using SemVer.
2. Reference vocabularies are also versioned as complete graphs using SemVer.
3. Reference objects under `/id/` have an individual lifecycle consisting of a GUID, conceptual version, and revision.

<a id="61-ontologien-und-shacl-graphen"></a>

### 6.1 Ontologies and SHACL Graphs

The following rules apply to ontologies and SHACL graphs:

1. The stable graph IRI remains unchanged.
2. Each publication receives a SemVer version IRI.
3. Published versions are immutable.
4. The unversioned graph IRI points to the current recommended version.
5. Term IRIs do not contain a version number.
6. Older publications remain accessible through their version IRIs.
7. Internal release imports use specific version IRIs.
8. An import closure must not contain multiple versions of the same ontology.
9. A new major version does not automatically create new term IRIs.
10. If the domain meaning of a term changes fundamentally, a new term is created and the old term is deprecated.
11. Removed IRIs must never be reused for other terms.

Each SHACL graph belongs to a named `shape-set`. A shape set groups rules
that are versioned together as a coherent set, for example `core`, `delivery`,
`invoice`, or `construction-site`. Different shape sets may have independent
versions. Shape IRIs belong to their shape set's stable hash namespace and
do not contain a version number.

Example:

```text
Stable shape graph: https://www.construct-x.org/shapes/address/core
Specific version:   https://www.construct-x.org/shapes/address/core/0.2.0
Stable shape:       https://www.construct-x.org/shapes/address/core#AddressShape
```

Example:

```text
Stable ontology IRI:
https://www.construct-x.org/ontology/address

Specific version:
https://www.construct-x.org/ontology/address/0.2.0

Stable term:
https://www.construct-x.org/ontology/address#PostalAddress
```

<a id="62-referenzvokabulare"></a>

### 6.2 Reference Vocabularies

Reference vocabularies follow the same graph-based publication model as ontologies but use the `/vocab/` path.

Rules:

1. Each reference vocabulary has a stable graph IRI.
2. Each publication receives a SemVer version IRI.
3. Published versions are immutable.
4. The stable vocabulary IRI returns the current recommended publication.
5. The IRIs of the terms it contains remain independent of versions.
6. Editorial corrections without semantic changes result in a patch version.
7. Backward-compatible additions result in a minor version.
8. Incompatible structural or semantic changes result in a major version.
9. Wherever possible, terms are deprecated rather than deleted.
10. Removed term IRIs must never be reassigned.

Example:

```text
Stable vocabulary IRI:
https://www.construct-x.org/vocab/wall-type

Specific version:
https://www.construct-x.org/vocab/wall-type/1.2.0

Stable term:
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

| Vocabulary change | Version change |
| --- | --- |
| Corrected a typo in a label | `1.0.0` -> `1.0.1` |
| Added a new wall type | `1.0.0` -> `1.1.0` |
| Incompatible change to the term hierarchy | `1.0.0` -> `2.0.0` |

A new vocabulary version does not automatically create new IRIs for all terms. If the domain meaning of `ExternalWall` remains unchanged, `https://www.construct-x.org/vocab/wall-type#ExternalWall` also remains unchanged.

<a id="63-referenzobjekte"></a>

### 6.3 Reference Objects

Reference objects are versioned individually and explicitly do not use SemVer. Their lifecycle is based on GUIDs and revisions.

Rules:

1. Reference objects are versioned individually, without SemVer.
2. A conceptual version has a GUID.
3. A revision retains the GUID and increments the revision number.
4. A new conceptual version receives a new GUID.
5. The new version references the version it replaces.
6. Published revisions are immutable.
7. Earlier versions and revisions remain accessible.
8. Normative and reproducible references use the GUID and revision number.
9. GUIDs and revision IRIs must never be reassigned.
10. Splitting and merging create new GUIDs and documented provenance or replacement relationships.

The SemVer version of a published graph and the revision of a reference object described within it are independent pieces of information.

Example: A property dictionary may be published as the graph `https://www.construct-x.org/vocab/property-dictionary/1.3.0`. An individual property reference object within it may still have the revision IRI `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2`. Graph version `1.3.0` and object revision `2` describe different things.

<a id="7-repository-struktur-und-oeffentliche-iris"></a>

## 7. Repository Structure and Public IRIs

Repository categories organize work in the monorepo. They are not public IRI segments.

Examples:

```text
Repository:
modules/core/address

Public ontology:
https://www.construct-x.org/ontology/address

Repository:
modules/core/participation

Public ontology:
https://www.construct-x.org/ontology/participation
```

<a id="8-dereferenzierung-und-auslieferung"></a>

## 8. Dereferencing and Delivery

Construct-X IRIs should be dereferenceable. Depending on the requested format, RDF, HTML documentation, or other representations can be delivered. `303 See Other` may be used for non-information resources. Content negotiation should support machine-readable and human-readable representations.

<a id="81-ontologien"></a>

### 8.1 Ontologies

```text
GET https://www.construct-x.org/ontology/vso
```

This IRI may point to or return the current recommended ontology version.

<a id="82-ontologieversionen"></a>

### 8.2 Ontology Versions

```text
GET https://www.construct-x.org/ontology/vso/0.1.0
```

This IRI permanently returns the immutable state of version `0.1.0`.

<a id="83-referenzvokabulare"></a>

### 8.3 Reference Vocabularies

```text
GET https://www.construct-x.org/vocab/wall-type
```

This IRI may return the current recommended vocabulary publication.

```text
GET https://www.construct-x.org/vocab/wall-type/1.2.0
```

This IRI permanently returns the immutable state of vocabulary version `1.2.0`.

<a id="84-persistente-id-ressourcen"></a>

### 8.4 Persistent ID Resources

```text
GET https://www.construct-x.org/id/property/{guid}
```

This IRI represents the conceptual version of the reference object and may point to its current revision.

```text
GET https://www.construct-x.org/id/property/{guid}/revision/2
```

This IRI permanently returns the immutable state of revision `2`.

Since the description returned by the base IRI may change with a new revision, it is insufficient for reproducible validation or normative references. These must always use the revision-specific IRI.

Example: A validation rule that needs to establish which property definition was used on 2026-08-18 references `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2` rather than just the base IRI without a revision segment.

<a id="9-katalog-nach-qudt-vorbild"></a>

## 9. Catalog Following the QUDT Model

The central artifact catalog describes graph publications. Individual reference objects may also be managed through their own registries or RDF descriptions.

For ontology and SHACL publications, the catalog documents at least:

- stable graph IRI;
- current version IRI;
- SemVer;
- term or shape namespace;
- previous publication;
- publication date;
- status;
- documentation and download links.

For vocabulary publications, the catalog documents at least:

- stable vocabulary IRI;
- current version IRI;
- SemVer;
- term namespace;
- previous publication;
- publication date;
- status;
- documentation and download links.

Example catalog entry:

```yaml
id: wall-type
kind: vocabulary
stable_iri: https://www.construct-x.org/vocab/wall-type
version_iri: https://www.construct-x.org/vocab/wall-type/1.2.0
version: 1.2.0
namespace: https://www.construct-x.org/vocab/wall-type#
previous_version_iri: https://www.construct-x.org/vocab/wall-type/1.1.0
status: released
published: 2026-08-18
```

For reference objects or their registries, at least the following are documented:

- reference object type;
- GUID;
- current revision number;
- current revision IRI;
- replaced or replacing version;
- status;
- publication and modification dates.

Example registry entry:

```yaml
type: property
guid: 550e8400-e29b-41d4-a716-446655440000
current_revision: 2
current_revision_iri: https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
replaces: null
replaced_by: https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1
status: released
published: 2026-08-18
modified: 2026-08-18
```

<a id="10-beispiele-aktueller-module"></a>

## 10. Examples from Current Modules

### 10.1 VSO

```text
Ontology IRI:  https://www.construct-x.org/ontology/vso
Namespace:     https://www.construct-x.org/ontology/vso#
Version IRI:   https://www.construct-x.org/ontology/vso/0.1.0
Prefix:        conx-vso
Repository:    modules/core/vso/ontology/conx-vso.ttl
```

### 10.2 Address

```text
Ontology IRI:  https://www.construct-x.org/ontology/address
Namespace:     https://www.construct-x.org/ontology/address#
Version IRI:   https://www.construct-x.org/ontology/address/0.2.0
Prefix:        conx-addr
Repository:    modules/core/address/ontology/conx-addr.ttl
```

### 10.3 Participation

```text
Ontology IRI:  https://www.construct-x.org/ontology/participation
Namespace:     https://www.construct-x.org/ontology/participation#
Version IRI:   https://www.construct-x.org/ontology/participation/0.2.0
Prefix:        conx-part
Repository:    modules/core/participation/ontology/conx-part.ttl
```

<a id="11-technische-und-organisatorische-pruefregeln"></a>

## 11. Technical and Organizational Validation Rules

Manual validation and reviews should check at least the following rules:

- Ontology IRIs and version IRIs match the defined pattern.
- SHACL IRIs, shape sets, shape namespaces, and SHACL version IRIs match the defined pattern.
- Vocabulary IRIs and version IRIs match the defined pattern.
- SemVer in ontology, shape, or vocabulary paths matches the version metadata.
- Stable ontology terms do not contain version numbers.
- Stable vocabulary terms do not contain version numbers.
- Published ontology, SHACL, and vocabulary versions have not been modified after publication.
- A reference object's revision IRI, GUID, and revision number are consistent.
- Each revision number is assigned only once within a GUID.
- A new conceptual version has a new GUID.
- Replaced and replacing versions use different GUIDs.
- Earlier revision IRIs remain accessible.
- Normative references to reference objects include the GUID and revision.
- Repository categories such as `core`, `domain`, and `alignments` do not appear in public ontology IRIs.
- Construct-X prefixes follow the pattern `conx-{module-abbreviation}`.

Simple example of an error:

```text
Incorrect:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000
```

This IRI may identify the current revision. However, it is insufficient for a normative or reproducible reference because the returned description may change with a new revision.

```text
Correct:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Another example of an error:

```text
Incorrect:
https://www.construct-x.org/vocab/wall-type/1.2.0#ExternalWall
```

The term contains a version number in its path. The correct form uses the stable term namespace:

```text
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

<a id="12-festgestellte-abweichungen-und-anpassungen"></a>

## 12. Identified Deviations and Adjustments

State analyzed before the earlier VSO migration:

- VSO ontology IRI: `https://www.construct-x.org/ontology/value-semantics`
- VSO namespace: `https://www.construct-x.org/ontology/value-semantics#`
- VSO version IRI: `https://www.construct-x.org/ontology/value-semantics/0.1.0`
- Repository path: `modules/core/value-semantics/ontology/conx-vso.ttl`

Technical adjustments:

- Changed the public module segment from `value-semantics` to `vso`.
- Changed the repository module folder from `modules/core/value-semantics` to `modules/core/vso`.
- Retained the `conx-vso` prefix because it follows the convention.
- Domain classes, properties, and axioms were not renamed.

Open decision:

- Before the first stable release, it must be confirmed that `https://www.construct-x.org` will serve as the permanent canonical authority.

<a id="13-verbindliche-empfehlung"></a>

## 13. Binding Recommendation

```text
Ontologies:          https://www.construct-x.org/ontology/{module}
Ontology versions:   https://www.construct-x.org/ontology/{module}/{semver}
Ontology terms:      https://www.construct-x.org/ontology/{module}#{localName}

Vocabularies:        https://www.construct-x.org/vocab/{vocabulary}
Vocabulary versions: https://www.construct-x.org/vocab/{vocabulary}/{semver}
Vocabulary terms:    https://www.construct-x.org/vocab/{vocabulary}#{localName}

Reference objects:   https://www.construct-x.org/id/{type}/{guid}
Exact revisions:     https://www.construct-x.org/id/{type}/{guid}/revision/{revision}

SHACL:               https://www.construct-x.org/shapes/{module}/{shape-set}
Alignments:          https://www.construct-x.org/alignment/{alignment}
Catalog:             https://www.construct-x.org/catalog
Documentation:       https://www.construct-x.org/docs/{module}
```

Ontologies and reference vocabularies follow the same graph-based publication model. Reference objects follow an individual lifecycle model based on GUIDs and revisions.
