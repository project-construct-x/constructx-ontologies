# Construct-X Person Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Person-Modul beschreibt intrinsische Kerndaten natürlicher Personen. Es
hält persönliche Merkmale getrennt von Kontaktwegen, Adressen,
Organisationsbeziehungen und fachlichen Rollen.

## 2. Alltagsnahes Beispiel

> Anna Müller wird mit ihrem Namen und Geburtsdatum als Person beschrieben.
> Ihre Telefonnummer liegt an einem Kontaktpunkt, ihre Firmenzugehörigkeit an
> einer Mitgliedschaft und ihre Projektnummer an einer Identifier-Ressource.

So kann sich beispielsweise eine Telefonnummer ändern, ohne den Personenkern
oder eine Mitgliedschaft umzubauen.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- vollständiger Name und Namensbestandteile,
- Geburtsdatum und textueller Geburtsort,
- Angaben zu `sex`, `gender` und Staatsangehörigkeit,
- strukturierte Kennungen über den gemeinsamen Identifier-Vertrag,
- eine offene Verknüpfung zu einem extern beschriebenen Identitätsnachweis.

**Nicht im Modul enthalten:**

- E-Mail, Telefon und Adressbestandteile,
- Mitgliedschaften, Beschäftigung und Projektrollen,
- interne Credential-, Schlüssel- oder Verifikationsdetails,
- ein eigenes Standort- oder Geomodell.

## 4. Modellübersicht

```text
Agent
  +-> Person
        +-> Namen und Geburtsangaben
        +-> sex / gender
        +-> citizenship -> Country
        +-> adms:identifier -> Identifier
        +-> hasIdentityEvidence -> externe Nachweisressource
```

Kontakt, Adresse und organisatorische Beziehungen können die Person
referenzieren, bleiben aber in ihren eigenen Modulen.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Person` | reale natürliche Person und Unterklasse von `Agent` |
| `fullName` | vollständiger Anzeigename |
| `givenName` / `familyName` | Vor- und Familienname |
| `birthDate` / `birthPlaceName` | Geburtsdatum und textueller Geburtsort |
| `sex` | Klassifikation für den Datenaustausch |
| `gender` | Geschlechtsidentität oder entsprechende Einordnung |
| `citizenship` | rechtliche Zugehörigkeit zu einem Staat |
| `hasIdentityEvidence` | offene Verbindung zu einer Nachweisressource |

## 6. Validierung in verständlicher Sprache

Jede Person benötigt mindestens einen vollständigen Namen und einen Vornamen.
Vorhandene Textwerte dürfen nicht leer sein. Das Geburtsdatum muss ein
vollständiges Kalenderdatum sein; `sex` und `gender` verwenden die jeweils
freigegebenen Wertelisten. Staatsangehörigkeiten verweisen auf Länderressourcen
und Kennungen auf den gemeinsamen Identifier-Vertrag.

> **Beispiel:** Eine Person mit dem Geburtswert „1985“ ist im Core ungültig,
> weil ein vollständiges Datum erwartet wird. Das Geburtsdatum darf aber ganz
> fehlen, wenn der Anwendungsfall es nicht benötigt.

## 7. Abhängigkeiten

`Person` spezialisiert `Agent` aus `core/agent`. Kennungen werden über das
importierte Core Shape aus `core/identifier` geprüft. Staatsangehörigkeiten
verwenden Länderressourcen aus dem Address-Referenzdatenbestand; `sex` und
`gender` besitzen getrennt versionierte Referenzvokabulare. FOAF und SEMIC
dienen als externe Referenz- und Alignmentquellen.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/person` |
| Präfix | `conx-person` |

- [Ontologie](../ontology/conx-person.ttl)
- [Core Shapes](../shapes/conx-person-core.shacl.ttl)
- [HTML-Dokumentation](person.html)
- [Vollständiges Personenbeispiel](../tests/valid/complete-person.ttl)
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

