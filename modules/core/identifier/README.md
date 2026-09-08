# Construct-X Identifier Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul stellt den gemeinsamen ADMS/SKOS-Vertrag für fachliche Kennungen
bereit, ohne eine parallele Construct-X-Identifier-Klasse einzuführen.

## 2. Verständliches Beispiel

> Die Registernummer „HRB 1234“ wird als eigene Kennungsressource gespeichert.
> Dadurch können Wert, Kennungssystem und herausgebende Stelle gemeinsam
> beschrieben werden.

```text
Organisation -> Identifier -> HRB 1234
```

## 3. Modellumfang

Jede Kennung ist ein `adms:Identifier` mit genau einer `skos:notation`.
`adms:schemaAgency` ist optional. Fachmodule bestimmen selbst, welche
Kennungen sie verlangen.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie-Metadaten: `ontology/conx-id.ttl`
- Core Shapes: `shapes/conx-id-core.shacl.ttl`
- Beispiele: `tests/valid/`
- Fehlerbeispiele: `tests/invalid/`
