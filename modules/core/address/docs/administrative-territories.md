# Administrative Gebietsreferenzen

Die Address-T-Box definiert mit `Country`, `AdministrativeArea` und
`AdministrativeTerritory` nur die fachliche Struktur. Konkrete Gebiete werden
als getrennte, versionierte A-Box-Datensätze gepflegt.

## Bereitgestellte Datensätze

| Datensatz | Versions-IRI | Umfang | Ressourcentyp |
| --- | --- | --- | --- |
| [ISO 3166-1 Countries](../../../../datasets/reference/administrative-territories/iso-3166-1-countries/README.md) | `https://www.construct-x.org/vocab/country/0.1.0` | 249 aktuelle ISO-3166-1-Einträge | `conx-addr:Country` |
| [German States according to ISO 3166-2](../../../../datasets/reference/administrative-territories/iso-3166-2-de/README.md) | `https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de/0.1.0` | 16 deutsche Länder | `conx-addr:AdministrativeArea` |

Die Länderressourcen verwenden den ISO-Alpha-3-Code in ihrer IRI, zum Beispiel
`countries:DEU`. Deutsche Länder verwenden ihren vollständigen ISO-3166-2-Code,
zum Beispiel `areas:DE-NW`. Kennungen werden nach dem
[netzwerkweiten ADMS-Kennungsprofil](../../../../docs/architecture/identifier-model.md)
modelliert.

Die Datentypen der ISO-Kennungen stammen aus dem versionierten
[Identifier-Scheme-Vokabular](../../../../datasets/reference/vocabularies/identifier-scheme/README.md).

## Verwendung an einer Adresse

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

`areas:DE-NW` verweist in seinem Referenzdatensatz direkt auf
`countries:DEU`. Die Adresse darf beide Links explizit enthalten, damit Land
und relevantes Bundesland ohne zusätzliche Pfadauflösung verfügbar sind.

## Warum keine Städte-A-Box?

Das Kernmodell benötigt für eine postalische Adresse den strukturierten
Ortsnamen, aber nicht zwingend eine referenzierbare Stadtressource. Ein
vollständiger kommunaler Datensatz hätte deutlich höhere Anforderungen an
Abdeckung, Gebietsstände, Fusionen, Mehrsprachigkeit und laufende Pflege.

Deshalb gilt zunächst:

- Ort oder Stadt: `conx-addr:localityName` als sprachmarkierter Literalwert.
- Stadtteil oder Ortsteil: `conx-addr:citySubdivisionName` als Literalwert.
- Land: Referenz auf einen ISO-3166-1-Eintrag.
- Bundesland: optionale Referenz auf einen deutschen ISO-3166-2-Eintrag.

Ein späterer Städte- oder Gemeindeschlüssel-Datensatz kann additive
`AdministrativeArea`-Ressourcen bereitstellen. Die bestehende T-Box und bereits
modellierte Adressen müssen dafür nicht geändert werden.

Weitere statistische Gebietsebenen wie NUTS können später als getrennte
Referenzdatensätze ergänzt werden. Sie sind nicht Bestandteil dieser ersten
Core-only-Veröffentlichung.

## EU-Vokabulare als Quelle

Die EU-Vokabulare sind für maschinenlesbare Bezeichnungen, Quellen-IRIs und die
technische Extraktion geeignet. Für die Identität der Codes bleibt ISO 3166 die
fachliche Grundlage. EU-interne Zusatzcodes werden nicht automatisch zu
Construct-X-Länderressourcen, und erkannte Quellabweichungen werden im Import
explizit validiert und dokumentiert.
