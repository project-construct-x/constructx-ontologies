# Construct-X Identifier Scheme Datatypes

This reference vocabulary defines the stable RDF datatype IRIs used to
identify the identifier scheme of a `skos:notation` value. The underlying
identifier model continues to come from ADMS and SKOS.

<a id="kennung-und-version"></a>

## Identification and Version

```text
Vocabulary IRI: https://www.construct-x.org/vocab/identifier-scheme
Version IRI:    https://www.construct-x.org/vocab/identifier-scheme/0.2.0
Namespace:      https://www.construct-x.org/vocab/identifier-scheme#
Prefix:         id-scheme
Version:        0.2.0
Status:         draft
```

<a id="enthaltene-datentypen"></a>

## Included Datatypes

| Datatype | Identifier scheme |
| --- | --- |
| `id-scheme:iso-3166-1-alpha-2` | ISO 3166-1 Alpha-2 |
| `id-scheme:iso-3166-1-alpha-3` | ISO 3166-1 Alpha-3 |
| `id-scheme:iso-3166-1-numeric` | ISO 3166-1 numeric |
| `id-scheme:iso-3166-2` | ISO 3166-2 |
| `id-scheme:nuts-2` | NUTS level 2 |

The terms are described as `rdfs:Datatype` because ADMS uses `skos:notation`
for an identifier's value, and its datatype identifies the identifier scheme.
They are not an additional identifier class and replace neither
`adms:Identifier` nor the issuing agency.

<a id="verwendung"></a>

## Usage

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix id-scheme: <https://www.construct-x.org/vocab/identifier-scheme#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

[] a adms:Identifier ;
   skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2 ;
   adms:schemaAgency "International Organization for Standardization (ISO)" .
```
