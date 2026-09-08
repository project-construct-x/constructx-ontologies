# Kennungsmodell im Construction-X-Ontologienetzwerk

## Entscheidung

Das Ontologienetzwerk verwendet fuer fachliche Kennungen das W3C-Vokabular
ADMS. Es wird keine parallele Construction-X-Klasse fuer Kennungen eingefuehrt.
Eine Ressource verweist mit `adms:identifier` auf eine Instanz von
`adms:Identifier`. Der Kennungswert steht in `skos:notation`; der Datentyp des
Literals bezeichnet das verwendete Kennungssystem.

Der gemeinsame semantische und validierende Vertrag ist im Core-Modul
[`identifier`](../../modules/core/identifier/README.md) versioniert. Das
ausfuehrbare `conx-id-sh:ADMSIdentifierShape` wird von den fachlichen
Core-Shape-Graphen wiederverwendet.

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix id-scheme: <https://www.construct-x.org/vocab/identifier-scheme#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://www.construct-x.org/vocab/country#DEU>
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2 ;
        adms:schemaAgency "International Organization for Standardization (ISO)"
    ] .
```

## Verwendete Kennungssysteme

| Datentyp-IRI | Bedeutung |
| --- | --- |
| `id-scheme:iso-3166-1-alpha-2` | zweistelliger ISO-3166-1-Code |
| `id-scheme:iso-3166-1-alpha-3` | dreistelliger ISO-3166-1-Code |
| `id-scheme:iso-3166-1-numeric` | dreistelliger numerischer ISO-3166-1-Code |
| `id-scheme:iso-3166-2` | ISO-3166-2-Code einer Verwaltungseinheit |
| `id-scheme:nuts-2` | Code einer Region der NUTS-Ebene 2 |

Die Datentyp-IRIs sind stabile Bezeichner der im Netzwerk verwendeten
Kennungssysteme. Sie fuehren keine neue Kennungslogik ein. Die Semantik von
Kennung, Kennungswert und herausgebender Stelle stammt aus ADMS und SKOS.
Der zugehoerige Graph wird als Referenzvokabular unter der stabilen IRI
`https://www.construct-x.org/vocab/identifier-scheme` und in Version `0.2.0`
unter `https://www.construct-x.org/vocab/identifier-scheme/0.2.0`
veroeffentlicht.

## Modellierungsregeln

1. Fachressourcen erhalten keine systemspezifischen Eigenschaften wie
   `isoAlpha2Code` oder `isoSubdivisionCode`.
2. Jede Kennung wird als eigene `adms:Identifier`-Ressource modelliert.
3. Der Wert wird genau einmal mit `skos:notation` angegeben.
4. Das Kennungssystem wird ueber den Datentyp der Notation bezeichnet.
5. Die herausgebende Stelle kann mit `adms:schemaAgency` dokumentiert werden.
6. Eine Ressource darf mehrere Kennungen aus unterschiedlichen Systemen
   besitzen.

Dasselbe Muster wird fuer Personen-, Organisations-, Mitgliedschafts-,
Dokument- und Dokumentreferenzkennungen wiederverwendet. Weitere Fachmodule
koennen es verwenden, ohne eine eigene Kennungsstruktur zu definieren.

## Abgrenzung

Das Kennungsmodell sagt nicht aus, welche Kennung eine Ressource im
Construction-X-Netzwerk adressierbar macht. Die stabile Ressourcen-IRI und ihre
fachlichen Kennungen sind getrennte Sachverhalte. Auch eine A-Box mit
ISO-Kennungen ersetzt keine allgemeine Stammdaten- oder Historisierungslogik.

## Normative Grundlage

- [Asset Description Metadata Schema (ADMS) 2.0](https://semiceu.github.io/ADMS/releases/2.00/)
- [SKOS Simple Knowledge Organization System](https://www.w3.org/TR/skos-reference/)
- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)


