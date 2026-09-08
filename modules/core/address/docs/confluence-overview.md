# Construct-X Address Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Address-Modul beschreibt strukturierte Anschriften und ihre Zuordnung zu
Personen, Organisationen oder anderen Ressourcen. Eine Adresse wird unabhängig
von ihrem Verwendungszweck gespeichert. Ob sie beispielsweise als Liefer-,
Rechnungs- oder Geschäftsadresse dient, wird an ihrer Zuordnung festgehalten.

## 2. Alltagsnahes Beispiel

> Eine Baufirma nutzt dieselbe Anschrift für Lieferungen und Rechnungen. Die
> Anschrift wird nur einmal angelegt. Zwei Rollen an der Adresszuordnung zeigen,
> wofür sie verwendet werden darf.

Dadurch entstehen keine widersprüchlichen Kopien derselben Straße,
Hausnummer und Postleitzahl.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- strukturierte Bestandteile wie Straße, Hausnummer, Postleitzahl und Ort,
- die Zuordnung einer Adresse zu einer Ressource,
- Rollen einer Adresszuordnung,
- Länder und administrative Gebiete als referenzierbare Konzepte,
- ein offener Anschluss für eine geografische Position.

**Nicht im Modul enthalten:**

- E-Mail, Telefon und andere Kontaktkanäle,
- ein eigenes Koordinaten- oder räumliches Referenzsystem,
- Personen- oder Organisationsstammdaten,
- länderspezifische Pflichtfelder und Postleitzahlenregeln.

## 4. Modellübersicht

```text
Ressource -> AddressAssignment -> Address
                 |
                 +-> AddressRole

Address -> Country
        -> AdministrativeArea
        -> externe geografische Position
```

Die `AddressAssignment` beantwortet „Für wen und wofür gilt die Anschrift?“;
`Address` beantwortet „Wie lautet die Anschrift?“.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Address` | strukturierte Anschrift |
| `AddressAssignment` | Zuordnung einer Anschrift zu einer Ressource |
| `AddressRole` | Zweck der Zuordnung, etwa Lieferadresse |
| `Country` | Staat aus dem Referenzdatensatz |
| `AdministrativeArea` | Verwaltungseinheit innerhalb eines Staates |
| `hasAddressAssignment` | führt von einer Ressource zu ihrer Adresszuordnung |
| `assignedAddress` | führt von der Zuordnung zur Anschrift |
| `addressRole` | nennt einen oder mehrere Verwendungszwecke |
| `hasGeographicPosition` | verbindet optional mit einem externen Geomodell |

## 6. Validierung in verständlicher Sprache

Eine Adresszuordnung ist nur vollständig, wenn sie auf genau eine Adresse
verweist und mindestens eine Rolle besitzt. Einzelwerte wie Hausnummer,
Postleitzahl und Land dürfen nicht mehrfach widersprüchlich angegeben werden.
Verknüpfte Rollen, Länder und Verwaltungseinheiten müssen als Ressourcen
referenziert werden.

> **Beispiel:** Eine Lieferadressenzuordnung ohne eigentliche Anschrift ist
> ungültig. Ob eine Lieferadresse zwingend eine Postleitzahl benötigt,
> entscheidet dagegen das jeweilige Fachprofil und nicht der offene Core.

## 7. Abhängigkeiten

Das Modul besitzt keine verpflichtende Abhängigkeit zu einem anderen
Construct-X Core-Modul. Adressrollen sowie ISO- und NUTS-Gebiete werden als
getrennt versionierte Referenzdaten verwendet. Andere Module wie Contact,
Person und Organization können das Address-Modell einbinden, ohne seine
Begriffe zu kopieren.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/address` |
| Präfix | `conx-addr` |

- [Ontologie](../ontology/conx-addr.ttl)
- [Core Shapes](../shapes/conx-addr-core.shacl.ttl)
- [HTML-Dokumentation](address.html)
- [Vollständiges Datenbeispiel](../examples/rub-address.ttl)
- [Changelog](../CHANGELOG.md)

## 9. Weiterführende Dokumentation

- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Quellenanalyse](source-analysis.md)
- [Konzeptmodell](concept-model.md)
- [Modulgrenzen](module-boundaries.md)
- [Begriffskatalog](term-catalog.md)
- [SHACL-Anforderungen](shacl-requirements.md)
- [Core-Shape-Referenz](core-shapes.md)
- [Konzeptdiagramm](diagrams/concept-model.md)

