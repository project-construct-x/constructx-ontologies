# Dokumentation des Document Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`

## 1. Überblick

Document trennt fachliche Dokumente, kontextbezogene Referenzen und technische
Dateibereitstellungen.

## 2. Einstieg für nichttechnische Leser

> Ein Prüfbericht ist das Dokument. Die PDF-Datei ist eine Distribution. Ein
> Vertrag kann über eine DocumentReference gezielt auf den Bericht verweisen.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | Standards und Modellalternativen |
| [Konzeptmodell](concept-model.md) | Dokument, Referenz und Distribution |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Participation, Evidence und Rechten |
| [Begriffskatalog](term-catalog.md) | Klassen, Properties und Vokabulare |
| [SHACL-Anforderungen](shacl-requirements.md) | fachlicher Regelkatalog |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-doc.ttl`
- Core Shapes: `../shapes/conx-doc-core.shacl.ttl`
- HTML-Dokumentation: `document.html`
- Referenzvokabulare: Dokumenttyp und Dokumentstatus

## 5. Beispiele und Tests

Gültige Beispiele zeigen vollständige Dokumente und Referenzen. Ungültige
Graphen unter `../tests/invalid/` erklären Fehler bei Metadaten, Kennungen und
Distributionen.

## 6. Ergänzende Dokumente

Das [ausführliche Document-Diagramm](diagrams/document-concept-model.md) enthält
weitere Sichten auf Referenzen, Distributionen und Participation.
