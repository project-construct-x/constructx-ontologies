# Construct-X NUTS 2 Regions

This A-Box reference vocabulary provides the 271 NUTS 2 values allowed by
Gaia-X release `v2.3.0` for `Address.region`. These include the regular EU-27
regions and the `ZZ` extra-regio codes listed by Gaia-X.

<a id="kennung-und-version"></a>

## Identification and Version

```text
Vocabulary IRI: https://www.construct-x.org/vocab/administrative-area/nuts-2
Version IRI:    https://www.construct-x.org/vocab/administrative-area/nuts-2/0.1.0
Namespace:      https://www.construct-x.org/vocab/administrative-area/nuts-2#
Prefix:         nuts
Version:        0.1.0
Status:         draft
```

Each region is both a `conx-addr:AdministrativeArea` and a `skos:Concept`.
The code is stored as `skos:notation` with datatype `id-scheme:nuts-2`;
`conx-addr:broaderAdministrativeTerritory` references the ISO 3166-1 country.

```turtle
nuts:DEA5
    a conx-addr:AdministrativeArea, skos:Concept ;
    skos:prefLabel "Arnsberg" ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DEA5"^^id-scheme:nuts-2 ;
        adms:schemaAgency "Eurostat"
    ] ;
    conx-addr:broaderAdministrativeTerritory countries:DEU .
```

<a id="quelle-und-reproduzierbarkeit"></a>

## Source and Reproducibility

The published version was generated from the Gaia-X `NUTS2Region`
enumeration in release `v2.3.0`, commit
`57131b2cec747de8a08a4115bea198369778aef6`. This makes the list reproducible
against the exact Gaia-X version used to test the Address alignment. It does
not claim to automatically match the latest Eurostat NUTS classification.

The vocabulary can be regenerated using the import script:

```bash
uv run python scripts/import_gaia_x_nuts2.py
```

Alternatively, a locally verified `region-codes.yaml` can be supplied
through `--source`.

## License and attribution

The [Construct-X NUTS 2 vocabulary](data/nuts-2-regions.ttl) is distributed
under the [Eclipse Public License 2.0](LICENSE-EPL-2.0.txt).
The 271 region codes and names come from the `NUTS2Region` enumeration in
Gaia-X Service Characteristics `v2.3.0`. Construct-X assigns each region an
IRI, represents its code as a typed identifier and links it to its country.
For example, Gaia-X supplies the code `DEA5` and the name “Arnsberg”.
Construct-X links that region to the country resource `countries:DEU`.

The [Gaia-X source file](https://gitlab.com/gaia-x/technical-committee/service-characteristics-working-group/service-characteristics/-/blob/57131b2cec747de8a08a4115bea198369778aef6/linkml/region-codes.yaml)
and [upstream license](https://gitlab.com/gaia-x/technical-committee/service-characteristics-working-group/service-characteristics/-/blob/57131b2cec747de8a08a4115bea198369778aef6/LICENSE)
are pinned to the commit used for this edition. The full license text is
included with the vocabulary in the release package.
