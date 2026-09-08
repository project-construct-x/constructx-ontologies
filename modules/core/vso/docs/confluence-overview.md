# Construct-X VSO Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Die Value Semantics Ontology, kurz VSO, beschreibt, wie eine fachliche
Merkmalsdefinition mit einem konkreten Wert an eine Ressource gebunden wird.
Sie stellt dafür ein domänenunabhängiges Muster bereit.

## 2. Alltagsnahes Beispiel

> Eine Wand besitzt das Merkmal „Höhe“. Die konkrete Merkmalszuweisung
> verweist auf die Definition „Höhe“, enthält den Wert 2,80 und nutzt die
> Einheit Meter.

VSO sagt damit, wie Wert und Einheit verbunden werden. Ob jede Wand zwingend
eine Höhe benötigt, entscheidet ein fachliches Profil.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- die Zuweisung eines Merkmals zu einer beliebigen Ressource,
- die Referenz auf eine Merkmalsdefinition,
- ein Zustandsknoten mit genau einem konkreten Wert,
- eine optionale QUDT-Einheit.

**Nicht im Modul enthalten:**

- fachliche Merkmalsdefinitionen selbst,
- ISOProps-Identifikatoren und ISOProps-Metadaten,
- domänenspezifische Wertebereiche,
- die Pflicht, dass bestimmte Ressourcen bestimmte Merkmale besitzen.

## 4. Modellübersicht

```text
Ressource -> AssignedProperty -> Merkmalsdefinition
                    |
                    +-> PropertyState
                           +-> schema:value
                           +-> hasUsedUnit -> optionale QUDT-Einheit
```

Die zusätzliche Zuweisungsressource hält die Verbindung erweiterbar und trennt
die allgemeine Merkmalsdefinition vom konkreten Wert.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `AssignedProperty` | konkrete Zuweisung einer Merkmalsdefinition |
| `PropertyState` | Zustand, der den konkreten Wert trägt |
| `hasProperty` | verbindet eine Ressource mit ihrer Zuweisung |
| `hasPropertyReference` | verweist auf die Merkmalsdefinition |
| `hasPropertyState` | verbindet Zuweisung und Wertzustand |
| `schema:value` | enthält den konkreten Wert |
| `hasUsedUnit` | verweist optional auf eine QUDT-Einheit |

## 6. Validierung in verständlicher Sprache

Jede Merkmalszuweisung gehört genau einer Ressource, verweist auf genau eine
Merkmalsdefinition und besitzt genau einen Zustand. Dieser Zustand enthält
genau einen Wert und höchstens eine Einheit.

> **Beispiel:** Eine Höhenzuweisung mit zwei aktuellen Zuständen ist im Core
> ungültig, weil nicht eindeutig ist, welcher Wert gelten soll. Ein Textmerkmal
> ohne Einheit kann dagegen vollständig gültig sein.

## 7. Abhängigkeiten

OPM liefert die grundlegenden Property-Konzepte, QUDT die Einheiten und
Schema.org die Wertproperty. Diese Ontologien werden referenziert und nicht
vollständig importiert. Das separate Profil `vso-isoprops` kann zusätzliche
ISOProps-Regeln anwenden, ohne den offenen VSO-Core zu verändern.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/vso` |
| Präfix | `conx-vso` |

- [Ontologie](../ontology/conx-vso.ttl)
- [Core Shapes](../shapes/conx-vso-core.shacl.ttl)
- [HTML-Dokumentation](vso.html)
- [Beispiel mit Messwert](../examples/measured-property.ttl)
- [Beispiel mit Textwert](../examples/text-property.ttl)
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
