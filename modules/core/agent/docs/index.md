# Dokumentation des Agent Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Überblick

Agent stellt die gemeinsame Oberklasse für Personen und Organisationen bereit.

## 2. Einstieg für nichttechnische Leser

> „Agent“ bedeutet hier schlicht „Akteur“. Wenn eine Beziehung für Menschen
> und Organisationen gelten kann, darf sie auf Agent verweisen.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | minimaler Umfang und Nutzen |
| [Quellenanalyse](source-analysis.md) | Auswahl des Agentenbegriffs |
| [Konzeptmodell](concept-model.md) | Person und Organization unter Agent |
| [Modulgrenzen](module-boundaries.md) | propertyfreier Kern und Abhängigkeiten |
| [Begriffskatalog](term-catalog.md) | Referenz der einzigen lokalen Klasse |
| [SHACL-Anforderungen](shacl-requirements.md) | Begründung für kein eigenes Shape |
| [Core Shapes](core-shapes.md) | Status des Validierungsvertrags |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-agent.ttl`
- Core Shapes: nicht erforderlich
- HTML-Dokumentation: `agent.html`

## 5. Beispiele und Tests

Das [Konzeptdiagramm](diagrams/concept-model.md) zeigt Person und Organization
als konkrete Agententypen. Ontologietests prüfen die Unterklassenbeziehung.

## 6. Ergänzende Dokumente

- [Ausführliche Agent-Spezifikation](agent-specification.md)
- [Integrationsdiagramm](diagrams/agent-integration-model.md)
