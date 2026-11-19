<a id="construct-x-person-core-module"></a>

# Construct-X Core-Modul Person

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/person`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Person beschreibt intrinsische Kerndaten natürlicher Personen. Es trennt persönliche Merkmale von Kontaktmethoden, Adressen, Organisationsbeziehungen und fachlichen Rollen.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Anna Müller wird als Person mit ihrem Namen und Geburtsdatum beschrieben. Ihre Telefonnummer gehört zu einem ContactPoint, ihre Unternehmenszugehörigkeit zu einer Membership und ihre Personalnummer zu einer Identifier-Ressource.

Eine Telefonnummer kann sich ändern, ohne die Personenkerndaten oder eine Mitgliedschaft umzustrukturieren.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst vollständige Namen und Namensbestandteile, Geburtsangaben, `sex`, `gender`, Staatsangehörigkeit, strukturierte Kennungen und einen offenen Verweis auf Identitätsnachweise. Es umfasst keine E-Mail-Adressen, Telefonnummern, Adressbestandteile, Mitgliedschaften, Beschäftigungsverhältnisse, Projektrollen, internen Nachweisstrukturen oder ein Ortsmodell.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Agent
  +-> Person
        +-> Namens- und Geburtsangaben
        +-> sex / gender
        +-> citizenship -> Country
        +-> adms:identifier -> Identifier
        +-> hasIdentityEvidence -> externe Nachweisressource
```

Contact, Address und Organization können auf eine Person verweisen, bleiben aber eigenständige Module.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Person` | Reale natürliche Person und Unterklasse von `Agent` |
| `fullName` | Vollständiger Anzeigename |
| `givenName` / `familyName` | Vor- und Familienname |
| `birthDate` / `birthPlaceName` | Geburtsdatum und Geburtsort als Text |
| `sex` | Für den Datenaustausch verwendete Klassifikation |
| `gender` | Geschlechtsidentität oder entsprechende Klassifikation |
| `citizenship` | Rechtliche Zugehörigkeit zu einem Staat |
| `hasIdentityEvidence` | Offener Verweis auf eine Nachweisressource |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Jede Person benötigt mindestens einen vollständigen Namen und einen Vornamen. Textwerte dürfen nicht leer sein. Ein Geburtsdatum muss ein vollständiges Kalenderdatum sein; `sex` und `gender` verwenden die freigegebenen Vokabulare. Die Staatsangehörigkeit verweist auf Länderressourcen, und Kennungen folgen den gemeinsamen Identifier-Anforderungen.

> Der Geburtswert „1985“ ist ungültig, weil ein vollständiges Datum erwartet wird. Das Geburtsdatum kann fehlen, wenn der Anwendungsfall es nicht verlangt.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

`Person` spezialisiert `Agent` aus `core/agent`. Kennungen werden durch das importierte Shape aus `core/identifier` geprüft. Die Staatsangehörigkeit verwendet Länderreferenzdaten; für `sex` und `gender` bestehen separat versionierte Vokabulare. FOAF und SEMIC dienen als externe Referenz- und Alignment-Quellen.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/person` |
| Präfix | `conx-person` |

- [Ontologie](../ontology/conx-person.ttl)
- [Core Shapes](../shapes/conx-person-core.shacl.ttl)
- [HTML-Dokumentation](person.html)
- [Vollständiges Personenbeispiel](../tests/valid/complete-person.ttl)
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
