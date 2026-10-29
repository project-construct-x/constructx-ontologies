# Administrative Territory References

The Address T-Box defines only the domain structure through `Country`, `AdministrativeArea`, and `AdministrativeTerritory`. Specific territories are maintained as separate, versioned A-Box datasets.

## Available Datasets

| Dataset | Version IRI | Coverage | Resource Type |
| --- | --- | --- | --- |
| [ISO 3166-1 Countries](../../../../datasets/reference/administrative-territories/iso-3166-1-countries/README.md) | `https://www.construct-x.org/vocab/country/0.1.0` | 249 current ISO 3166-1 entries | `conx-addr:Country` |
| [German States according to ISO 3166-2](../../../../datasets/reference/administrative-territories/iso-3166-2-de/README.md) | `https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de/0.1.0` | 16 German federal states | `conx-addr:AdministrativeArea` |
| [NUTS 2 Regions](../../../../datasets/reference/administrative-territories/nuts-2/README.md) | `https://www.construct-x.org/vocab/administrative-area/nuts-2/0.1.0` | 271 Gaia-X-compatible NUTS 2 values | `conx-addr:AdministrativeArea` |

Country resources use the ISO alpha-3 code in their IRI, for example `countries:DEU`. German federal states use their complete ISO 3166-2 code, for example `areas:DE-NW`. Identifiers are modeled according to the [network-wide ADMS identifier profile](../../../../docs/architecture/identifier-model.md).

The datatypes of the ISO identifiers come from the versioned [Identifier Scheme Vocabulary](../../../../datasets/reference/vocabularies/identifier-scheme/README.md).

## Use with an Address

```turtle
@prefix areas: <https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix countries: <https://www.construct-x.org/vocab/country#> .
@prefix ex: <https://example.org/id/> .

ex:rub-address
    a conx-addr:Address ;
    conx-addr:streetName "Universitätsstraße"@de ;
    conx-addr:houseNumber "150" ;
    conx-addr:postalCode "44801" ;
    conx-addr:localityName "Bochum"@de ;
    conx-addr:hasCountry countries:DEU ;
    conx-addr:hasAdministrativeArea areas:DE-NW .
```

In its reference dataset, `areas:DE-NW` references `countries:DEU` directly. The address may explicitly contain both links so that the country and relevant federal state are available without additional path traversal.

## Why No City A-Box?

For a postal address, the core model requires a structured locality name, but not necessarily a referenceable city resource. A comprehensive municipal dataset would entail substantially greater requirements for coverage, territorial configurations, mergers, multilingual support, and ongoing maintenance.

The following therefore applies initially:

- Locality or city: `conx-addr:localityName` as a language-tagged literal.
- City or locality subdivision: `conx-addr:citySubdivisionName` as a literal.
- Country: reference to an ISO 3166-1 entry.
- Federal state: optional reference to a German ISO 3166-2 entry.
- NUTS 2 region: optional reference to a NUTS 2 entry if an exchange profile requires this statistical territorial level.

A future city or municipality code dataset can provide additional `AdministrativeArea` resources. This requires no changes to the existing T-Box or previously modeled addresses.

The NUTS 2 A-Box replaces neither the locality name nor the federal state. An address can therefore reference, for example, both `areas:DE-NW` and `nuts:DEA5`. The open cardinality of `0..n` for `hasAdministrativeArea` supports such parallel administrative or statistical levels.

## EU Vocabularies as a Source

The EU vocabularies are suitable for machine-readable labels, source IRIs, and technical extraction. ISO 3166 remains the domain authority for code identity. Additional EU-specific codes do not automatically become Construct-X country resources, and detected source discrepancies are explicitly validated and documented during import.