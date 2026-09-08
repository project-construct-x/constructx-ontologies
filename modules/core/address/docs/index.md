# Dokumentation des Address Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

## 1. Überblick

Address beschreibt strukturierte Anschriften, ihre Zuordnung zu Ressourcen und
die Rolle einer solchen Zuordnung.

## 2. Einstieg für nichttechnische Leser

> Eine Anschrift beantwortet „Wo?“. Eine AddressAssignment beantwortet
> zusätzlich „Für wen?“ und „Wofür?“, beispielsweise Lieferadresse.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md), gefolgt vom
[Konzeptdiagramm](diagrams/concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang und beantwortbare Fragen |
| [Quellenanalyse](source-analysis.md) | Vergleich externer Adressmodelle |
| [Konzeptmodell](concept-model.md) | Klassen, Beziehungen und Entscheidungen |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Contact, Agent und Geo |
| [Begriffskatalog](term-catalog.md) | kompakte Referenz der Begriffe |
| [SHACL-Anforderungen](shacl-requirements.md) | fachliche Validierungsregeln |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-addr.ttl`
- Core Shapes: `../shapes/conx-addr-core.shacl.ttl`
- HTML-Dokumentation: `address.html`

## 5. Beispiele und Tests

Das Beispiel `../examples/rub-address.ttl` zeigt eine vollständige Adresse.
Positive und negative Prüfbeispiele liegen unter `../tests/`.

## 6. Ergänzende Dokumente

- [Adressrollen](address-roles.md)
- [Administrative Gebiete](administrative-territories.md)
