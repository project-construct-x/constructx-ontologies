# Dokumentation des Person Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

## 1. Überblick

Person beschreibt intrinsische Kerndaten realer natürlicher Personen.

## 2. Einstieg für nichttechnische Leser

> Name und Geburtsdatum beschreiben eine Person direkt. Telefonnummer,
> Firmenzugehörigkeit und Kennung sind dagegen verknüpfte Informationen mit
> eigenen Datenverträgen.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | Personenstandards und Modellentscheidungen |
| [Konzeptmodell](concept-model.md) | Personenkern und Modulübergänge |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Organization, Contact und Address |
| [Begriffskatalog](term-catalog.md) | Klassen, Properties und Vokabulare |
| [SHACL-Anforderungen](shacl-requirements.md) | vollständiger Regelkatalog |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-person.ttl`
- Core Shapes: `../shapes/conx-person-core.shacl.ttl`
- HTML-Dokumentation: `person.html`
- Referenzvokabulare: `human-sex` und `gender`

## 5. Beispiele und Tests

Gültige Graphen zeigen minimale und vollständige Personen. Ungültige Graphen
erklären Fehler bei Namen, Datentypen, kontrollierten Werten und Identifiern.

## 6. Ergänzende Dokumente

Das [ausführliche Personendiagramm](diagrams/person-concept-model.md) zeigt
Kontaktdaten und Übergänge zu weiteren Modulen.
