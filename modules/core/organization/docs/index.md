# Dokumentation des Organization Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`

## 1. Überblick

Organization beschreibt Organisationen, Legal Entities, interne Einheiten,
Mitgliedschaften und rechtliche Vertretungen.

## 2. Einstieg für nichttechnische Leser

> Eine GmbH ist eine Legal Entity. Eine Abteilung ist eine
> OrganizationalUnit. Mitgliedschaft und Vertretung werden als eigene
> Beziehungen beschrieben.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | Standards und Registermodelle |
| [Konzeptmodell](concept-model.md) | Organisationsarten und Beziehungen |
| [Modulgrenzen](module-boundaries.md) | Zuständigkeiten anderer Core-Module |
| [Begriffskatalog](term-catalog.md) | Klassen und Properties |
| [SHACL-Anforderungen](shacl-requirements.md) | vollständiger Regelkatalog |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-org.ttl`
- Core Shapes: `../shapes/conx-org-core.shacl.ttl`
- HTML-Dokumentation: `organization.html`

## 5. Beispiele und Tests

Gültige Graphen zeigen Legal Entity, Organisationseinheit, Membership und
LegalRepresentation. Ungültige Graphen erklären verletzte Pflichtbeziehungen.

## 6. Ergänzende Dokumente

Das [ausführliche Organisationsdiagramm](diagrams/organization-concept-model.md)
zeigt Stammdaten, Modulübergänge und Prozessrollen.
