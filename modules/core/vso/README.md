# Construct-X VSO Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Die Value Semantics Ontology beschreibt, wie eine Merkmalsdefinition mit einem
konkreten Wert an eine Ressource gebunden wird.

## 2. Verständliches Beispiel

> Eine Wand besitzt das Merkmal „Höhe“. Ihre konkrete Merkmalszuweisung trägt
> den Wert 2,80 und verweist auf die Einheit Meter.

```text
Wand -> AssignedProperty „Höhe“ -> PropertyState -> 2,80 m
```

## 3. Modellumfang

Der Core umfasst Merkmalszuweisung, Merkmalsreferenz, Zustand, Wert und
optionale Einheit. Fachliche Wertetypen und ISOProps-Regeln liegen in Profilen.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-vso.ttl`
- Core Shapes: `shapes/conx-vso-core.shacl.ttl`
- Beispiele: `examples/measured-property.ttl` und `examples/text-property.ttl`
- Tests: `tests/valid/` und `tests/invalid/`
