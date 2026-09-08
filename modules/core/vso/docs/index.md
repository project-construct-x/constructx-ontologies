# Dokumentation des VSO Core-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Überblick

VSO verbindet Ressourcen mit konkreten Merkmalszuweisungen, Zuständen, Werten
und optionalen Einheiten.

## 2. Einstieg für nichttechnische Leser

> Eine Wand hat nicht einfach den Wert „2,80“. Erst die Kombination aus
> Merkmal „Höhe“, Wert 2,80 und Einheit Meter ist eindeutig verständlich.

Der einfachste Einstieg ist das [Konzeptmodell](concept-model.md).

## 3. Dokumentationspaket

| Dokument | Inhalt |
| --- | --- |
| [Confluence-Kurzfassung](confluence-overview.md) | Veröffentlichungsquelle der kompakten Modulseite |
| [Scope und Kompetenzfragen](scope-and-competency-questions.md) | fachlicher Umfang |
| [Quellenanalyse](source-analysis.md) | OPM, QUDT und Schema.org |
| [Konzeptmodell](concept-model.md) | Zuweisung, Zustand, Wert und Einheit |
| [Modulgrenzen](module-boundaries.md) | Abgrenzung zu Fach- und ISOProps-Profilen |
| [Begriffskatalog](term-catalog.md) | Klassen und Properties |
| [SHACL-Anforderungen](shacl-requirements.md) | stabile VSO-Regeln |
| [Core Shapes](core-shapes.md) | ausführbarer Datenvertrag |
| [Konzeptdiagramm](diagrams/concept-model.md) | visuelle Kurzfassung |

## 4. Technische Artefakte

- T-Box: `../ontology/conx-vso.ttl`
- Core Shapes: `../shapes/conx-vso-core.shacl.ttl`
- HTML-Dokumentation: `vso.html`

## 5. Beispiele und Tests

`../examples/measured-property.ttl` zeigt einen Messwert mit Einheit;
`../examples/text-property.ttl` einen Textwert ohne Einheit. Ungültige Fälle
liegen unter `../tests/invalid/`.

## 6. Ergänzende Dokumente

- [Integrationsanalyse](integration-analysis.md)
- [Review-Bericht](review-report.md)
