<a id="construct-x-participation-core-module"></a>

# Construct-X Core-Modul Participation

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.2.0<br>
**Stand:** 7. Oktober 2026<br>
**Geltungsbereich:** `core/participation`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Participation beschreibt einen Agenten, der in einem fachlichen Kontext eine bestimmte Rolle innehat. Der Kontext bleibt offen und kann ein Vertrag, ein Dokument oder eine andere Fachressource sein.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Anna Müller ist als Architektin an einem Bauprojekt beteiligt. Anna ist die Beteiligte, „Architektin“ die Rolle und das Projekt der Kontext. Beginn und Ende der Zuordnung können zusätzlich erfasst werden.

Eine zweite Rolle für Anna im selben Kontext wird durch eine zweite Participation dargestellt.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst die qualifizierte Beziehung zwischen Agent, Rolle und Kontext, eine auf SKOS basierende Klasse Role sowie optionale Gültigkeitsdaten. Es umfasst keine Akteursstammdaten, Kontextdefinitionen, Tätigkeiten, Berechtigungen, Mitgliedschaften, Herkunftsangaben, Nachweise oder lediglich geplanten Rollen.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Agent <- participant - Participation - context -> Fachlicher Kontext
                              |
                              +-> role -> Role
                              +-> startDate / endDate
```

Eine Participation beschreibt genau eine Kombination aus Agent, Rolle und Kontext. Der Kontext kann zusätzlich über `hasParticipation` auf sie verweisen.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Participation` | Aktuelle oder historische Rollenzuordnung |
| `Role` | Kontrollierte Beschreibung einer Rolle |
| `participant` | Verweist auf genau einen Agenten |
| `role` | Verweist auf genau eine Rolle |
| `context` | Verweist auf genau einen fachlichen Kontext |
| `hasParticipation` | Optionale Navigation vom Kontext zur Beteiligung |
| `startDate` / `endDate` | Optionaler Gültigkeitszeitraum |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Jede Participation benötigt genau einen Agenten, eine Rolle und einen Kontext. Anfangs- und Enddatum dürfen jeweils höchstens einmal vorkommen; der Beginn darf nicht nach dem Ende liegen. Dieselbe Kombination darf im geprüften Datengraphen nicht doppelt vorkommen. Wird `hasParticipation` verwendet, muss die Ziel-Participation ausdrücklich denselben Kontext nennen.

> „Anna ist Architektin“ ist ohne Kontext unvollständig. Das Bauprojekt macht deutlich, wo diese Rolle gilt.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

`participant` verweist auf `Agent` aus `core/agent`. Rollen basieren auf SKOS; allgemeine Startrollen werden in einem separat versionierten Vokabular gepflegt. Person, Organization, Document und Domänenmodelle können Participation nutzen, ohne dadurch verpflichtende T-Box-Imports zu werden.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.2.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/participation` |
| Präfix | `conx-part` |

- [Ontologie](../ontology/conx-part.ttl)
- [Core Shapes](../shapes/conx-part-core.shacl.ttl)
- [HTML-Dokumentation](participation.html)
- [Beteiligungsbeispiel mit Gültigkeitsdaten](../tests/valid/dated-participation.ttl)
- [Änderungsprotokoll](../CHANGELOG.md)

<a id="9-further-documentation"></a>

## 9. Weiterführende Dokumentation

- [Umfang und Kompetenzfragen](02_scope-and-competency-questions.md)
- [Quellenanalyse](01_source-analysis.md)
- [Konzeptmodell](03_concept-model.md)
- [Modulabgrenzung](04_module-boundaries.md)
- [Begriffskatalog](05_term-catalog.md)
- [SHACL-Anforderungen](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Konzeptdiagramm](08_concept-diagram.md)
