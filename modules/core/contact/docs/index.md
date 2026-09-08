# Dokumentation des Contact Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

## 1. Überblick

Contact beschreibt Kontaktpunkte, konkrete Kontaktmethoden, Nutzung und Zweck.

## 2. Einstieg für nichttechnische Leser

> Ein Kontaktpunkt kann „Buchhaltung“ heißen und für Rechnungen gedacht sein.
> E-Mail und Telefon sind einzelne Methoden dieses Kontaktpunkts.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | Bewertung von vCard, Schema.org und UBL |
| [Konzeptmodell](concept-model.md) | Kontaktpunkt und Kontaktmethode |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Address und Agent |
| [Begriffskatalog](term-catalog.md) | Klassen, Properties und Startwerte |
| [SHACL-Anforderungen](shacl-requirements.md) | vollständiger Regelkatalog |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-contact.ttl`
- Core Shapes: `../shapes/conx-contact-core.shacl.ttl`
- HTML-Dokumentation: `contact.html`

## 5. Beispiele und Tests

Unter `../tests/valid/` liegen Beispiele für E-Mail, Website, Messenger und
postalische Kontakte. `../tests/invalid/` erklärt typische Strukturfehler.

## 6. Ergänzende Dokumente

Das [ausführliche Kontakt-Konzeptdiagramm](diagrams/contact-concept-model.md)
zeigt zusätzliche Alltagssituationen und Quellenabbildungen.
