<a id="construct-x-address-core-module"></a>

# Construct-X Core-Modul Address

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/address`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Address beschreibt strukturierte Adressen und ihre Zuordnung zu Personen, Organisationen oder anderen Ressourcen. Eine Adresse wird unabhängig von ihrem Verwendungszweck gespeichert; die Nutzung als Liefer-, Rechnungs- oder Geschäftsadresse wird an der Zuordnung festgehalten.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Ein Bauunternehmen verwendet dieselbe Adresse für Lieferungen und Rechnungen. Die Adresse wird einmal angelegt. Zwei Rollen an der Zuordnung beschreiben, wofür sie genutzt werden kann.

So werden widersprüchliche Kopien derselben Straße, Hausnummer und Postleitzahl vermieden.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst strukturierte Adressbestandteile, Adresszuordnungen, Zuordnungsrollen, Länder, Verwaltungsgebiete und einen offenen Verweis auf eine geografische Position. Es definiert keine Kontaktkanäle, kein Koordinatenreferenzsystem, keine Personen- oder Organisationsstammdaten und keine länderspezifischen Postregeln.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Ressource -> AddressAssignment -> Address
                 |
                 +-> AddressRole

Address -> Country
        -> AdministrativeArea
        -> externe geografische Position
```

`AddressAssignment` beantwortet die Frage „für wen und zu welchem Zweck?“, `Address` die Frage „wie lautet die Adresse?“.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Address` | Strukturierte Adresse |
| `AddressAssignment` | Zuordnung einer Adresse zu einer Ressource |
| `AddressRole` | Zweck der Zuordnung, etwa Lieferadresse |
| `Country` | Land aus dem Referenzdatensatz |
| `AdministrativeArea` | Verwaltungsgebiet innerhalb eines Landes |
| `assignedAddress` | Verknüpft die Zuordnung mit der Adresse |
| `addressRole` | Gibt einen oder mehrere Verwendungszwecke an |
| `hasGeographicPosition` | Verweist optional auf ein externes geografisches Modell |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Eine Adresszuordnung ist nur vollständig, wenn sie auf genau eine Adresse verweist und mindestens eine Rolle besitzt. Felder mit höchstens einem Wert dürfen keine widersprüchlichen Mehrfachwerte enthalten. Verknüpfte Rollen und Gebiete müssen Ressourcen sein.

> Eine Lieferadresszuordnung ohne Adresse ist ungültig. Ob eine Lieferadresse eine Postleitzahl enthalten muss, entscheidet ein Fachprofil, nicht der offene Core.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

Das Modul besitzt keine verpflichtende Abhängigkeit von einem anderen Construct-X Core-Modul. Adressrollen sowie ISO- und NUTS-Gebiete werden separat als Referenzdaten versioniert. Contact, Person und Organization können das Adressmodell wiederverwenden, ohne seine Begriffe zu kopieren.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/address` |
| Präfix | `conx-addr` |

- [Ontologie](../ontology/conx-addr.ttl)
- [Core Shapes](../shapes/conx-addr-core.shacl.ttl)
- [HTML-Dokumentation](address.html)
- [Vollständiges Datenbeispiel](../examples/rub-address.ttl)
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
