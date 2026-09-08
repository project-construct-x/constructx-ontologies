# Scope und Kompetenzfragen des Agent-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Das Modul stellt einen gemeinsamen Oberbegriff für Akteure bereit. Dadurch
können Beziehungen auf Personen und Organisationen verweisen, ohne zwei
verschiedene Properties zu benötigen.

## 2. Bestätigter Scope

Der Core enthält ausschließlich `conx-agent:Agent` und dessen konservative
Einordnung unter `foaf:Agent`.

## 3. Nicht im Scope

Namen, Adressen, Kontakte, Mitgliedschaften und technische Nutzerkonten gehören
nicht in den Agent-Kern.

## 4. Kompetenzfragen

1. Kann eine Person als allgemeiner Akteur verwendet werden?
2. Kann eine Organisation dieselbe Akteursbeziehung verwenden?
3. Bleiben konkrete Stammdaten in den zuständigen Modulen?

Alle drei Fragen werden mit Ja beantwortet.

## 5. Verständliches Beispiel

> Ein Dokument kann von einem Akteur herausgegeben werden. Ob der Akteur eine
> Person oder Organisation ist, wird durch dessen genaueren Typ beschrieben.

```text
Dokument -> herausgegeben von -> Agent
                                  |
                                  +-> Person oder Organization
```

## 6. Modellentscheidung

Der Agent-Kern bleibt absichtlich klein. Details stehen in der
[fachlichen Spezifikation](agent-specification.md).

## 7. Abnahmekriterien

Person und Organization sind Unterklassen von Agent; der Agent-Kern übernimmt
keine fachfremden Properties.
