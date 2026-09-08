# Construct-X Identifier Scheme Datatypes

Dieses Referenzvokabular definiert die stabilen RDF-Datentyp-IRIs, mit denen
das in `skos:notation` verwendete Kennungssystem angegeben wird. Das fachliche
Kennungsmodell selbst stammt weiterhin aus ADMS und SKOS.

## Kennung und Version

```text
Vokabular-IRI: https://www.construct-x.org/vocab/identifier-scheme
Versions-IRI:  https://www.construct-x.org/vocab/identifier-scheme/0.2.0
Namespace:     https://www.construct-x.org/vocab/identifier-scheme#
Prefix:        id-scheme
Version:       0.2.0
Status:        draft
```

## Enthaltene Datentypen

| Datentyp | Kennungssystem |
| --- | --- |
| `id-scheme:iso-3166-1-alpha-2` | ISO 3166-1 Alpha-2 |
| `id-scheme:iso-3166-1-alpha-3` | ISO 3166-1 Alpha-3 |
| `id-scheme:iso-3166-1-numeric` | ISO 3166-1 numerisch |
| `id-scheme:iso-3166-2` | ISO 3166-2 |
| `id-scheme:nuts-2` | NUTS-Ebene 2 |

Die Begriffe sind als `rdfs:Datatype` beschrieben, weil ADMS für den Wert einer
Kennung `skos:notation` verwendet und dessen Datentyp das Kennungssystem
bezeichnet. Sie sind keine zusätzliche Kennungsklasse und ersetzen weder
`adms:Identifier` noch die herausgebende Stelle.

## Verwendung

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix id-scheme: <https://www.construct-x.org/vocab/identifier-scheme#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

[] a adms:Identifier ;
   skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2 ;
   adms:schemaAgency "International Organization for Standardization (ISO)" .
```
