<a id="construct-x-identifier-core-module"></a>

# Construct-X Core-Modul Identifier

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/identifier`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Identifier stellt gemeinsame Datenanforderungen für fachliche Kennungen bereit. Person, Organization und Document können dasselbe ADMS/SKOS-Muster verwenden, ohne die Regeln für Kennungswerte erneut zu definieren.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Die Handelsregisternummer „HRB 1234“ gehört zu einer Organisation. Ihr Wert und die herausgebende Stelle werden gemeinsam als Identifier-Ressource gespeichert.

Die Web-IRI der Organisation und ihre Registernummer bleiben getrennt: Die IRI identifiziert die RDF-Ressource, während der Identifier eine fachliche Kennung abbildet.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst die wiederverwendbaren Anforderungen an `adms:Identifier`, genau eine `skos:notation` und eine optionale `adms:schemaAgency`. Es führt keine parallele Construct-X-Klasse für Kennungen ein, schreibt keine Kennungssysteme vor und entscheidet nicht, welche Kennungen ein Fachmodul benötigt.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Fachressource -> adms:identifier -> adms:Identifier
                                       |
                                       +-> skos:notation
                                       +-> adms:schemaAgency (optional)
```

Die Kennung wird als Ressource modelliert, damit Wert und Herkunft gemeinsam beschrieben werden können.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `adms:Identifier` | Wiederverwendbare Kennungsressource |
| `adms:identifier` | Verknüpft eine Fachressource mit ihrer Kennung |
| `skos:notation` | Enthält den Kennungswert |
| `adms:schemaAgency` | Bezeichnet optional die herausgebende Stelle oder das Kennungssystem |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Jede Kennungsressource benötigt genau eine nicht leere `skos:notation`. `adms:schemaAgency` ist optional, darf aber höchstens einmal vorkommen und muss auf eine Ressource verweisen.

> Ein Identifier ohne Notation ist ungültig. Ein Identifier mit einer Notation und ohne herausgebende Stelle ist gültig, sofern das verwendende Modul diese nicht verlangt.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

Die gemeinsamen Regeln verwenden ADMS und SKOS direkt. Person, Organization und Document importieren das versionierte Identifier Shape zur Prüfung strukturierter Kennungen.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/identifier` |
| Shape-Präfix | `conx-id-sh` |

- [Ontologie-Metadaten](../ontology/conx-id.ttl)
- [Core Shapes](../shapes/conx-id-core.shacl.ttl)
- [HTML-Dokumentation](identifier.html)
- [Minimales Kennungsbeispiel](../tests/valid/minimal-identifier.ttl)
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
