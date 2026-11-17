# Construct-X Core-Modul VSO

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/vso`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Die Value Semantics Ontology beschreibt, wie eine Merkmalsdefinition und ein
konkreter Wert über ein domänenunabhängiges Muster einer Ressource zugewiesen
werden.

## 2. Alltagsbeispiel

> Eine Wand besitzt das Merkmal „Höhe“. Die konkrete Zuweisung verweist auf
> die Merkmalsdefinition „Höhe“, enthält den Wert 2,80 und verwendet die
> Einheit Meter.

VSO beschreibt, wie Wert und Einheit miteinander verbunden werden. Ein
Fachprofil legt fest, ob beispielsweise jede Wand eine Höhe besitzen muss.

## 3. Umfang und Abgrenzung

Das Modul umfasst die Zuweisung eines Merkmals zu einer Ressource, den Verweis
auf eine Merkmalsdefinition, einen Zustand mit genau einem Wert und eine
optionale QUDT-Einheit. Es enthält keine Merkmalsdefinitionen, keine
ISOProps-Identifikatoren oder -Metadaten, keine domänenspezifischen
Wertebereiche und keine Anforderungen an bestimmte Objekttypen.

## 4. Modellübersicht

```text
Ressource -> AssignedProperty -> Merkmalsdefinition
                    |
                    +-> PropertyState
                           +-> schema:value
                           +-> hasUsedUnit -> optionale QUDT-Einheit
```

Die Zuweisung wird als eigene Ressource modelliert. Dadurch bleibt die
Beziehung erweiterbar und die allgemeine Definition wird vom konkreten Wert
getrennt.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung |
| --- | --- |
| `AssignedProperty` | Konkrete Zuweisung einer Merkmalsdefinition |
| `PropertyState` | Zustand, der den konkreten Wert trägt |
| `hasProperty` | Verknüpft eine Ressource mit ihrer Merkmalszuweisung |
| `hasPropertyReference` | Verweist auf die Merkmalsdefinition |
| `hasPropertyState` | Verknüpft die Zuweisung mit dem Wertzustand |
| `schema:value` | Enthält den konkreten Wert |
| `hasUsedUnit` | Verweist optional auf eine QUDT-Einheit |

## 6. Validierung in Alltagssprache

Jede Merkmalszuweisung gehört genau zu einer Ressource, verweist auf genau
eine Merkmalsdefinition und besitzt genau einen Zustand. Der Zustand enthält
genau einen Wert und höchstens eine Einheit.

> Eine Höhenzuweisung mit zwei aktuellen Zuständen ist ungültig, weil der
> aktuelle Wert nicht eindeutig wäre. Ein textuelles Merkmal ohne Einheit
> kann vollständig gültig sein.

## 7. Abhängigkeiten

OPM stellt die grundlegenden Merkmalskonzepte bereit, QUDT die Einheiten und
Schema.org die Werteigenschaft. Diese Ontologien werden referenziert, aber
nicht vollständig importiert. Das separate Profil `vso-isoprops` kann
ISOProps-Regeln ergänzen, ohne den offenen VSO Core zu verändern.

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/vso` |
| Präfix | `conx-vso` |

- [Ontologie](../ontology/conx-vso.ttl)
- [Core Shapes](../shapes/conx-vso-core.shacl.ttl)
- [HTML-Dokumentation](vso.html)
- [Beispiel einer Messgröße](../examples/measured-property.ttl)
- [Änderungsprotokoll](../CHANGELOG.md)

## 9. Weiterführende Dokumentation

- [Umfang und Kompetenzfragen](02_scope-and-competency-questions.md)
- [Quellenanalyse](01_source-analysis.md)
- [Konzeptmodell](03_concept-model.md)
- [Modulabgrenzung](04_module-boundaries.md)
- [Begriffskatalog](05_term-catalog.md)
- [SHACL-Anforderungen](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Konzeptdiagramm](08_concept-diagram.md)
