# Dokumentation des Identifier Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Überblick

Identifier stellt einen gemeinsamen ADMS/SKOS-Datenvertrag für fachliche
Kennungen bereit.

## 2. Einstieg für nichttechnische Leser

> Eine Kennung besteht nicht nur aus dem Text „HRB 1234“. Sie kann zusätzlich
> erklären, welches Register zuständig ist und welches Schema verwendet wird.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | Umfang des gemeinsamen Vertrags |
| [Quellenanalyse](source-analysis.md) | Entscheidung für ADMS und SKOS |
| [Konzeptmodell](concept-model.md) | Struktur einer Kennung |
| [Modulgrenzen](module-boundaries.md) | Trennung von Struktur und Fachregeln |
| [Begriffskatalog](term-catalog.md) | verwendete externe Begriffe |
| [SHACL-Anforderungen](shacl-requirements.md) | drei stabile Regelgruppen |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- Ontologie-Metadaten: `../ontology/conx-id.ttl`
- Core Shapes: `../shapes/conx-id-core.shacl.ttl`
- Architekturentscheidung: [Kennungsmodell](../../../../docs/architecture/identifier-model.md)

## 5. Beispiele und Tests

`../tests/valid/` zeigt minimale Kennungen und Kennungen mit Schema-Agentur.
`../tests/invalid/` zeigt fehlende oder mehrfach vorhandene Notationen.

## 6. Ergänzende Dokumente

Das Identifier-Scheme-Vokabular unter `datasets/reference/vocabularies/`
definiert Datentypen für konkrete Kennungssysteme.
