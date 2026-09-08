# Construct-X Contact Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Contact-Modul beschreibt, wie Personen, Organisationen und andere
Ressourcen erreichbar sind. Es trennt eine Kontaktstelle mit ihrem Zweck von
den konkreten Kontaktwegen wie E-Mail, Telefon oder Website.

## 2. Alltagsnahes Beispiel

> Die Buchhaltung einer Firma ist für Rechnungsfragen per E-Mail und Telefon
> erreichbar. „Buchhaltung“ ist der Kontaktpunkt; E-Mail-Adresse und
> Telefonnummer sind zwei Kontaktmethoden dieses Kontaktpunkts.

Die Angaben „geschäftlich“ und „Rechnung“ beschreiben Nutzung und Zweck, ohne
sie in den eigentlichen Kontaktwert zu mischen.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- Kontaktpunkte und einzelne Kontaktmethoden,
- Kanäle wie E-Mail, Telefon, Website, Messenger und Postanschrift,
- Nutzungskontexte wie privat, geschäftlich und offiziell,
- Zwecke wie Rechnung, Lieferung, Support oder Notfall,
- optionale Plattform-, Sprach- und Erreichbarkeitsangaben.

**Nicht im Modul enthalten:**

- Personennamen und Organisationsstrukturen,
- Straßen, Hausnummern und andere Adressbestandteile,
- Datenschutzberechtigungen und Einwilligungen,
- die technische Prüfung, ob eine Adresse wirklich erreichbar ist.

## 4. Modellübersicht

```text
Kontaktträger -> ContactPoint „Buchhaltung"
                    |       |
                    |       +-> Zweck: Rechnung
                    +-> ContactMethod -> Kanal: E-Mail
                    +-> ContactMethod -> Kanal: Telefon
```

Eine postalische Kontaktmethode speichert die Adresse nicht erneut, sondern
verweist auf eine `AddressAssignment` aus dem Address-Modul.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `ContactPoint` | Kontaktstelle für einen bestimmten Nutzungskontext |
| `ContactMethod` | einzelner Kommunikationsweg |
| `ContactChannel` | Art des Wegs, etwa E-Mail oder Telefon |
| `ContactUsage` | Nutzung, etwa privat oder geschäftlich |
| `ContactPurpose` | fachlicher Zweck, etwa Rechnung oder Support |
| `hasContactPoint` | verbindet einen Kontaktträger mit einer Kontaktstelle |
| `hasContactMethod` | bündelt Kontaktwege an einem Kontaktpunkt |
| `contactValue` | enthält beispielsweise E-Mail-Adresse oder Telefonnummer |
| `usesAddressAssignment` | bindet eine vorhandene postalische Adresse ein |

## 6. Validierung in verständlicher Sprache

Jeder Kontaktpunkt benötigt mindestens eine Kontaktmethode. Jede Methode hat
genau einen freigegebenen Kanal und muss die dazu passende Information
enthalten: E-Mail und Telefon verwenden einen nicht leeren Text, Websites eine
IRI und postalische Kontakte eine Adresszuordnung.

> **Beispiel:** Der Kanal „Website“ mit einer Telefonnummer als Text ist
> ungültig. Eine Website-Methode mit einer Webadresse als IRI erfüllt den
> allgemeinen Core-Vertrag. Ob die Seite erreichbar ist, wird nicht geprüft.

## 7. Abhängigkeiten

Postalische Kontaktmethoden referenzieren `core/address`. Kanal, Nutzung,
Zweck und Plattform stammen aus getrennt versionierten Construct-X-
Referenzvokabularen. Schema.org und vCard dienen als externe Referenz- und
Alignmentquellen; ihre vollständigen Modelle werden nicht importiert.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/contact` |
| Präfix | `conx-contact` |

- [Ontologie](../ontology/conx-contact.ttl)
- [Core Shapes](../shapes/conx-contact-core.shacl.ttl)
- [HTML-Dokumentation](contact.html)
- [Gültiges Kontaktbeispiel](../tests/valid/business-delivery-contact.ttl)
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

