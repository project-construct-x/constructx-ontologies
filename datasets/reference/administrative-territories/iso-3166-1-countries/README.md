# Construct-X ISO 3166-1 Countries

This A-Box dataset provides the 249 currently assigned ISO 3166-1 entries
as referenceable resources of the class `conx-addr:Country`.

<a id="kennung-und-version"></a>

## Identification and Version

```text
Vocabulary IRI: https://www.construct-x.org/vocab/country
Version IRI:    https://www.construct-x.org/vocab/country/0.1.0
Namespace:      https://www.construct-x.org/vocab/country#
Prefix:         countries
Version:        0.1.0
Status:         draft
```

The resource IRI uses the alpha-3 code, for example `countries:DEU`.
Alpha-2, alpha-3, and numeric identifiers are each described as a separate
`adms:Identifier` resource according to the
[network-wide identifier profile](../../../../docs/architecture/identifier-model.md).

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

<a id="quellen-und-abgrenzung"></a>

## Sources and Scope

ISO 3166-1 is the normative basis for the identifiers. Machine-readable values
and German and English labels are extracted reproducibly from the official
EU Vocabularies country table, source version `20260617-0`.

The EU table also contains the internal or no longer currently assigned
entries `CPT`, `CRQ`, `FXX`, and `XKX`. These are not part of the current set of
249 ISO 3166-1 entries and are explicitly excluded by the import.

For Nepal (`NPL`, `524`) and St. Helena (`SHN`, `654`), the EU source version
used publishes the numeric identifier only with the UNSD M49 datatype.
The import accepts only these two substantiated values as fallbacks and
uses them to generate the ISO 3166-1 numeric identifiers.

Sources:

- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)
- [EU Vocabularies Country](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/country)

<a id="aktualisierung"></a>

## Updating

Update the dataset by running the following import from the project root:

```text
uv run python scripts/import_iso_3166.py
```

The import aborts if the source version, count, uniqueness, or known source
discrepancies no longer match the verified assumptions. Changes are then
reviewed and published as a new dataset version.

