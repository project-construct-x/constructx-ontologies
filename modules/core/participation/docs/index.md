# Dokumentation des Participation Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`

## 1. Überblick

Participation beschreibt die Rolle eines Agenten in einem fachlichen Kontext.

## 2. Einstieg für nichttechnische Leser

> „Anna ist Architektin im Bauvorhaben A“ wird als eigene Participation
> gespeichert. So bleiben Person, Rolle und Bauvorhaben getrennt.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | n-stellige Beziehungen und Rollenmodelle |
| [Konzeptmodell](concept-model.md) | Agent, Rolle und Kontext |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Membership und Aktivitäten |
| [Begriffskatalog](term-catalog.md) | Klassen, Properties und Startrollen |
| [SHACL-Anforderungen](shacl-requirements.md) | vollständiger Regelkatalog |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-part.ttl`
- Core Shapes: `../shapes/conx-part-core.shacl.ttl`
- HTML-Dokumentation: `participation.html`
- Referenzvokabular: allgemeine Rollen

## 5. Beispiele und Tests

Die Testgraphen zeigen gültige Rollen, optionale Zeiträume und Fehler bei
fehlendem Agenten, fehlender Rolle oder doppelter Kombination.

## 6. Ergänzende Dokumente

Das [ausführliche Participation-Diagramm](diagrams/participation-concept-model.md)
zeigt weitere Integrations- und Zeitbeispiele.
