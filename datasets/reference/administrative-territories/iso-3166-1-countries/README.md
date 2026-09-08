# Construct-X ISO 3166-1 Countries

Dieser A-Box-Datensatz stellt die 249 aktuell vergebenen ISO-3166-1-Einträge
als referenzierbare Ressourcen der Klasse `conx-addr:Country` bereit.

## Kennung und Version

```text
Vokabular-IRI: https://www.construct-x.org/vocab/country
Versions-IRI:  https://www.construct-x.org/vocab/country/0.1.0
Namespace:     https://www.construct-x.org/vocab/country#
Prefix:        countries
Version:       0.1.0
Status:        draft
```

Die Ressourcen-IRI verwendet den Alpha-3-Code, beispielsweise
`countries:DEU`. Alpha-2-, Alpha-3- und numerische Kennung werden jeweils als
eigene `adms:Identifier`-Ressource nach dem
[netzwerkweiten Kennungsprofil](../../../../docs/architecture/identifier-model.md)
beschrieben.

```turtle
countries:DEU
    a conx-addr:Country, skos:Concept ;
    skos:prefLabel "Deutschland"@de,
                   "Germany"@en ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2
    ] .
```

## Quellen und Abgrenzung

Normative Grundlage der Kennungen ist ISO 3166-1. Die maschinenlesbaren Werte
und deutsch- sowie englischsprachigen Bezeichnungen werden reproduzierbar aus
der offiziellen EU-Vocabularies-Ländertabelle, Quellversion `20260617-0`,
extrahiert.

Die EU-Tabelle enthält zusätzlich die internen oder nicht mehr aktuell
vergebenen Einträge `CPT`, `CRQ`, `FXX` und `XKX`. Sie sind kein Bestandteil
der aktuellen Menge von 249 ISO-3166-1-Einträgen und werden vom Import
ausdrücklich ausgeschlossen.

Bei Nepal (`NPL`, `524`) und St. Helena (`SHN`, `654`) veröffentlicht die
verwendete EU-Quellversion die numerische Kennung nur mit dem Datentyp UNSD M49.
Der Import akzeptiert ausschließlich diese beiden belegten Werte als
Fallback und erzeugt daraus die ISO-3166-1-Numerisch-Kennung.

Quellen:

- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)
- [EU Vocabularies Country](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/country)

## Aktualisierung

Der Datensatz wird im Projektstamm mit folgendem Import aktualisiert:

```text
uv run python scripts/import_iso_3166.py
```

Der Import bricht ab, wenn Quellversion, Anzahl, Eindeutigkeit oder bekannte
Quellabweichungen nicht mehr den geprüften Annahmen entsprechen. Änderungen
werden anschließend als neue Datensatzversion geprüft und veröffentlicht.

