# Construct-X Participation Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul beschreibt eine tatsächlich geltende oder historisch geltende Rolle
eines Agenten in einem fachlichen Kontext.

## 2. Verständliches Beispiel

> Anna Müller wirkt in einem Bauvorhaben als Architektin mit. Participation
> verbindet Anna, die Rolle „Architektin“ und das Bauvorhaben.

```text
Participation -> Person
              -> Rolle: Architect
              -> fachlicher Kontext
```

## 3. Modellumfang

Jede Participation besitzt genau einen Agenten, eine Rolle und einen Kontext.
Start- und Enddatum sind optional. Aktivitäten, Berechtigungen und Membership
bleiben außerhalb des Moduls.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-part.ttl`
- Core Shapes: `shapes/conx-part-core.shacl.ttl`
- Beispiele und Tests: `tests/valid/` und `tests/invalid/`
- Referenzvokabular: allgemeine Participation-Rollen
