# Dokumentationsstandard für Core-Module

**Status:** Verbindliche Arbeitskonvention  
**Version:** 1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `modules/core/*`

## 1. Ziel

Alle Core-Module sollen unabhängig von ihrer fachlichen Größe gleich auffindbar
und ähnlich lesbar sein. Fachleute müssen Regeln präzise nachschlagen können;
Personen ohne RDF-, OWL- oder SHACL-Erfahrung sollen das Grundmodell anhand
einfacher Beispiele verstehen können.

## 2. Pflichtdateien

Jedes Core-Modul besitzt folgendes Dokumentationspaket:

```text
README.md
CHANGELOG.md
docs/index.md
docs/confluence-overview.md
docs/scope-and-competency-questions.md
docs/source-analysis.md
docs/concept-model.md
docs/module-boundaries.md
docs/term-catalog.md
docs/shacl-requirements.md
docs/core-shapes.md
docs/diagrams/concept-model.md
```

Ist ein Bereich nicht anwendbar, bleibt die Datei bestehen und erklärt den
Grund. Das gilt beispielsweise für ein Modul ohne eigenes Core Shape.

## 3. Dokumentkopf

Normative und fachlich aktuelle Dokumente beginnen nach dem Titel mit:

```text
**Status:** Implementiert oder fachlich bestätigt
**Version:** 0.1.0
**Stand:** 3. September 2026
**Geltungsbereich:** `core/<modul>`
```

Quellenanalysen dürfen zusätzlich den Recherchestand nennen. Historische
Arbeitsdokumente werden ausdrücklich als ergänzend und nicht normativ markiert.

## 4. Aufgabenteilung

| Dokument | Aufgabe |
| --- | --- |
| `README.md` | Kurzer Einstieg für Repository-Nutzende |
| `docs/index.md` | Zentrale Navigation und aktueller Modulstand |
| `docs/confluence-overview.md` | Kompakte Veröffentlichungsquelle für die Confluence-Modulseite |
| `scope-and-competency-questions.md` | Scope, Ausschlüsse und beantwortbare Fragen |
| `source-analysis.md` | Quellen, Alternativen und Begründung der Auswahl |
| `concept-model.md` | Fachliches Modell in verständlicher Form |
| `module-boundaries.md` | Zuständigkeiten und Abhängigkeiten |
| `term-catalog.md` | Klassen, Properties und kontrollierte Werte |
| `shacl-requirements.md` | Fachliche Validierungsanforderungen |
| `core-shapes.md` | Kurze Referenz des ausführbaren Shape-Graphs |
| `diagrams/concept-model.md` | Visueller Überblick mit Lesebeispiel |

## 5. Verständliche Beispiele

Jedes fachliche Dokument enthält mindestens eine konkrete Situation oder einen
kleinen Datenausschnitt. Ein Beispiel beginnt mit der fachlichen Aussage und
zeigt erst danach technische Details.

Beispiel:

> Eine Organisation besitzt eine Rechnungsadresse. Die Adresse selbst enthält
> Straße und Ort; die Rolle „Rechnungsadresse“ liegt an der Adresszuordnung.

```text
Organisation -> Adresszuordnung -> Adresse
                  |
                  +-> Rolle: Rechnungsadresse
```

Technische Turtle-Beispiele sollen kurz sein und nur Begriffe verwenden, die im
unmittelbaren Text erklärt werden.

## 6. Sprache und Benennung

- Fließtext und Überschriften sind deutsch.
- Umlaute werden ausgeschrieben und nicht als `ae`, `oe` oder `ue` ersetzt.
- Klassen, Properties, Präfixe und öffentliche IRIs bleiben unverändert.
- Das Repository verwendet die Bezeichnung „Construct-X Core-Modul“.
- Kapitel werden nummeriert; ergänzende Spezialdokumente dürfen davon
  abweichen.

## 7. Pflege

Alle Dokumente werden in `module.yaml` registriert und über `docs/index.md`
verlinkt. Änderungen an T-Box oder Core Shapes werden gleichzeitig in
Konzeptmodell, Begriffskatalog, SHACL-Dokumentation und Changelog nachvollzogen.
Relative Links müssen innerhalb des Repositorys auflösbar bleiben.

## 8. Confluence-Veröffentlichung

Die Datei `docs/confluence-overview.md` ist die einzige Veröffentlichungsquelle
für die kompakte Confluence-Seite eines Core-Moduls. Sie verdichtet die
fachlichen Bestandsdokumente, setzt aber keine zusätzlichen Regeln. Die
Repository-Dokumente bleiben die ausführliche menschlich lesbare Quelle;
Ontologie und Shapes bleiben die normativen maschinenlesbaren Artefakte.

Jede Confluence-Kurzfassung verwendet genau diese Kapitel:

1. Zweck
2. Alltagsnahes Beispiel
3. Umfang und Abgrenzung
4. Modellübersicht
5. Zentrale Klassen und Beziehungen
6. Validierung in verständlicher Sprache
7. Abhängigkeiten
8. Version, Status und Artefakte
9. Weiterführende Dokumentation

Eine Änderung beginnt im zuständigen Fachdokument und wird anschließend in der
Kurzfassung nachvollzogen. Die Confluence-Seite wird aus
`docs/confluence-overview.md` veröffentlicht und nicht unabhängig davon
redaktionell fortgeschrieben.
