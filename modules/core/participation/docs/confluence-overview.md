# Construct-X Participation Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Participation-Modul beschreibt, dass ein Agent eine bestimmte Rolle in
Bezug auf einen fachlichen Kontext einnimmt. Der Kontext bleibt offen und kann
beispielsweise ein Vertrag, Dokument oder anderes fachliches Objekt sein.

## 2. Alltagsnahes Beispiel

> Anna Müller wirkt als Architektin an einem Bauvorhaben mit. Anna ist die
> Beteiligte, „Architektin“ ist ihre Rolle und das Bauvorhaben ist der Kontext.
> Beginn und Ende dieser Zuordnung können zusätzlich angegeben werden.

Hat Anna im selben Kontext außerdem eine zweite Rolle, wird dafür eine zweite
Participation angelegt.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- die qualifizierte Verbindung aus Agent, Rolle und Kontext,
- eine allgemeine, SKOS-basierte Rollenklasse,
- optionale Datumsgrenzen für die Gültigkeit,
- ein kleines, getrenntes Startvokabular allgemeiner Rollen.

**Nicht im Modul enthalten:**

- Personen- oder Organisationsstammdaten,
- die fachliche Definition des Kontextobjekts,
- Aktivitäten, Ereignisse und tatsächlich ausgeführte Leistungen,
- Organisationsmitgliedschaften, Berechtigungen, Provenienz und Nachweise,
- geplante oder nur mögliche Rollen.

## 4. Modellübersicht

```text
Agent <- participant - Participation - context -> fachlicher Kontext
                              |
                              +-> role -> Role
                              +-> startDate / endDate
```

Eine Participation steht immer für genau eine Kombination aus Agent, Rolle
und Kontext.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Participation` | konkrete, geltende oder historisch geltende Rollenzuordnung |
| `Role` | kontrolliert beschriebene Rolle |
| `participant` | verweist auf genau einen Agenten |
| `role` | verweist auf genau eine Rolle |
| `context` | verweist auf genau einen fachlichen Kontext |
| `startDate` / `endDate` | optionale zeitliche Gültigkeit |

Das Startvokabular enthält unter anderem Auftraggeber-, Auftragnehmer-,
Lieferanten-, Architekten- und Ingenieurrollen. Fachmodule dürfen eigene
Rollenlisten bereitstellen.

## 6. Validierung in verständlicher Sprache

Jede Participation benötigt genau einen Agenten, genau eine Rolle und genau
einen Kontext. Anfang und Ende dürfen jeweils höchstens einmal vorkommen; der
Anfang darf nicht nach dem Ende liegen. Dieselbe Kombination aus Agent, Rolle
und Kontext darf im gemeinsam geprüften Datengraphen nicht doppelt vorkommen.

> **Beispiel:** „Anna ist Architektin“ reicht nicht, wenn der Kontext fehlt.
> Erst mit dem zugehörigen Bauvorhaben ist eindeutig, wofür die Rolle gilt.

## 7. Abhängigkeiten

`participant` verweist auf `Agent` aus `core/agent`. Rollen basieren auf SKOS;
die allgemeinen Startrollen liegen in einem getrennt versionierten
Participation-Role-Vokabular. Person, Organization, Document und andere
Fachmodelle können gemeinsam mit Participation verwendet werden, sind aber
keine zwingenden T-Box-Imports.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/participation` |
| Präfix | `conx-part` |

- [Ontologie](../ontology/conx-part.ttl)
- [Core Shapes](../shapes/conx-part-core.shacl.ttl)
- [HTML-Dokumentation](participation.html)
- [Beispiel einer zeitlich begrenzten Beteiligung](../tests/valid/dated-participation.ttl)
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

