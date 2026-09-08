# Construct-X German States according to ISO 3166-2

Dieser A-Box-Datensatz stellt ausschließlich die 16 Länder der Bundesrepublik
Deutschland als `conx-addr:AdministrativeArea` bereit. Jedes Land verweist mit
`conx-addr:broaderAdministrativeTerritory` auf `countries:DEU`.

## Kennung und Version

```text
Vokabular-IRI: https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de
Versions-IRI:  https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de/0.1.0
Namespace:     https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#
Prefix:        areas
Version:       0.1.0
Status:        draft
```

## Enthaltene Verwaltungseinheiten

| ISO 3166-2 | Bezeichnung der EU-Quelle |
| --- | --- |
| `DE-BB` | Land Brandenburg |
| `DE-BE` | Stadtstaat Berlin |
| `DE-BW` | Land Baden-Württemberg |
| `DE-BY` | Bayern |
| `DE-HB` | Stadtstaat Bremen |
| `DE-HE` | Land Hessen |
| `DE-HH` | Stadtstaat Hamburg |
| `DE-MV` | Land Mecklenburg-Vorpommern |
| `DE-NI` | Land Niedersachsen |
| `DE-NW` | Land Nordrhein-Westfalen |
| `DE-RP` | Land Rheinland-Pfalz |
| `DE-SH` | Land Schleswig-Holstein |
| `DE-SL` | Saarland |
| `DE-SN` | Freistaat Sachsen |
| `DE-ST` | Land Sachsen-Anhalt |
| `DE-TH` | Freistaat Thüringen |

## Bewusste Abgrenzung

Städte, Gemeinden, Regierungsbezirke und Kreise sind nicht enthalten. Für die
Adressangabe bleibt der Ort in Version 0.1.0 ein strukturierter Literalwert in
`conx-addr:localityName`. Damit muss nicht für jede gewöhnliche Adresse ein
vollständiger und laufend zu pflegender Verwaltungshierarchie-Graph geladen
werden. Weitere Ebenen können später als eigene, versionierte Datensätze
ergänzt werden, ohne die Address-T-Box zu verändern.

## Quellenqualität

Die ISO-3166-2-Kennungen und deutschen Bezeichnungen werden aus der offiziellen
EU-Vocabularies-ATU-Tabelle, Quellversion `20260617-0`, extrahiert. Die Quelle
veröffentlicht für ihre Sachsen-Ressource `DEU_LD_SN` in dieser Version
fälschlich die bereits Sachsen-Anhalt zugewiesene Notation `DE-ST`. Der Import
prüft exakt diesen Fehler und korrigiert die Sachsen-Ressource auf den
ISO-3166-2-Code `DE-SN`. Bei einer Änderung der Quelldaten bricht diese
Korrektur absichtlich ab und muss neu bewertet werden.

Quellen:

- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)
- [EU Vocabularies Administrative Territorial Units](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu)

## Aktualisierung

```text
uv run python scripts/import_iso_3166.py
```

Der Import erwartet genau die 16 ISO-Codes und mindestens ein deutsches
Vorzugslabel je Ressource.


