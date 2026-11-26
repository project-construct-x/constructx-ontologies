# Construct-X German States according to ISO 3166-2

This A-Box dataset provides only the 16 states of the Federal Republic of
Germany as `conx-addr:AdministrativeArea` resources. Each state references
`countries:DEU` through `conx-addr:hasBroaderAdministrativeTerritory`.

<a id="kennung-und-version"></a>

## Identification and Version

```text
Vocabulary IRI: https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de
Version IRI:    https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de/0.2.0
Namespace:      https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#
Prefix:         areas
Version:        0.2.0
Status:         draft
```

<a id="enthaltene-verwaltungseinheiten"></a>

## Included Administrative Areas

The German labels from the EU source are retained below.

| ISO 3166-2 | Label in the EU source |
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

<a id="bewusste-abgrenzung"></a>

## Deliberate Scope Boundaries

Cities, municipalities, administrative regions, and districts are not included.
For address data in version 0.1.0, the locality remains a structured literal
value in `conx-addr:localityName`. This avoids having to load a complete
administrative hierarchy graph requiring ongoing maintenance for every
ordinary address. Additional levels can later be added as separate,
versioned datasets without changing the Address T-Box.

<a id="quellenqualität"></a>

## Source Quality

The ISO 3166-2 identifiers and German labels are extracted from the official
EU Vocabularies ATU table, source version `20260617-0`. In this version, the
source incorrectly publishes the notation `DE-ST`, already assigned to
Saxony-Anhalt, for its Saxony resource `DEU_LD_SN`. The import checks for this
specific error and corrects the Saxony resource to the ISO 3166-2 code `DE-SN`.
If the source data changes, this correction deliberately aborts and must be
reassessed.

Sources:

- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)
- [EU Vocabularies Administrative Territorial Units](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu)

<a id="aktualisierung"></a>

## Updating

```text
uv run python scripts/import_iso_3166.py
```

The import expects exactly the 16 ISO codes and at least one German
preferred label per resource.


