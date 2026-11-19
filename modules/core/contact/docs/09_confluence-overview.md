<a id="construct-x-contact-core-module"></a>

# Construct-X Core-Modul Contact

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/contact`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Contact beschreibt, wie Personen, Organisationen und andere Ressourcen erreicht werden können. Es trennt einen Kontaktpunkt und seinen Zweck von konkreten Kontaktmethoden wie E-Mail, Telefon oder Website.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Die Buchhaltung eines Unternehmens ist bei Rechnungsfragen per E-Mail und Telefon erreichbar. „Buchhaltung“ ist der Kontaktpunkt; E-Mail-Adresse und Telefonnummer sind zwei zugehörige Kontaktmethoden.

Nutzung und Zweck werden getrennt vom eigentlichen Kontaktwert beschrieben.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst Kontaktpunkte, Kontaktmethoden, Kanäle, Nutzungskontexte, Zwecke sowie optionale Angaben zu Plattform, Sprache und Erreichbarkeitszeiten. Es definiert keine Namen, Organisationsstrukturen, Adressbestandteile, Einwilligungen oder technischen Erreichbarkeitsprüfungen.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Kontaktierbare Ressource -> ContactPoint „Buchhaltung“
                              |       |
                              |       +-> Zweck: Rechnung
                              +-> ContactMethod -> Kanal: E-Mail
                              +-> ContactMethod -> Kanal: Telefon
```

Eine postalische Kontaktmethode verweist auf eine vorhandene `AddressAssignment`, statt Adressdaten zu kopieren.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `ContactPoint` | Kontaktpunkt für einen bestimmten Nutzungskontext |
| `ContactMethod` | Einzelne Kommunikationsmethode |
| `ContactChannel` | Kanal wie E-Mail oder Telefon |
| `ContactUsage` | Nutzung, etwa privat oder geschäftlich |
| `ContactPurpose` | Zweck, etwa Rechnung oder Unterstützung |
| `hasContactMethod` | Bündelt Methoden an einem Kontaktpunkt |
| `contactValue` | Enthält eine E-Mail-Adresse oder Telefonnummer |
| `usesAddressAssignment` | Verwendet eine vorhandene postalische Adresszuordnung |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Jeder Kontaktpunkt benötigt mindestens eine Methode. Jede Methode besitzt genau einen freigegebenen Kanal und muss den dazu passenden Wert bereitstellen: Text für E-Mail und Telefon, eine IRI für Websites oder eine Adresszuordnung für postalischen Kontakt.

> Ein Website-Kanal mit einer Telefonnummer als einfachem Text ist ungültig. Eine Website-Methode mit einer Web-IRI erfüllt die Core-Anforderungen, auch wenn der Core nicht prüft, ob die Website erreichbar ist.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

Postalische Kontaktmethoden verweisen auf `core/address`. Kanal, Nutzung, Zweck und Plattform stammen aus separat versionierten Construct-X-Vokabularen. Schema.org und vCard dienen als externe Referenz- und Alignment-Quellen.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/contact` |
| Präfix | `conx-contact` |

- [Ontologie](../ontology/conx-contact.ttl)
- [Core Shapes](../shapes/conx-contact-core.shacl.ttl)
- [HTML-Dokumentation](contact.html)
- [Gültiges Kontaktbeispiel](../tests/valid/business-delivery-contact.ttl)
- [Änderungsprotokoll](../CHANGELOG.md)

<a id="9-further-documentation"></a>

## 9. Weiterführende Dokumentation

- [Umfang und Kompetenzfragen](02_scope-and-competency-questions.md)
- [Quellenanalyse](01_source-analysis.md)
- [Konzeptmodell](03_concept-model.md)
- [Modulabgrenzung](04_module-boundaries.md)
- [Begriffskatalog](05_term-catalog.md)
- [SHACL-Anforderungen](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Konzeptdiagramm](08_concept-diagram.md)
