# Construct-X Document Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul trennt ein fachliches Dokument, seine kontextbezogene Referenz und
seine technische Bereitstellung als Datei.

## 2. Verständliches Beispiel

> Ein Vertrag verweist auf einen Prüfbericht. Der Bericht ist das Dokument;
> seine PDF- und XML-Dateien sind zwei Distributionen desselben Dokuments.

```text
Vertrag -> DocumentReference -> Document -> PDF
                                      +-> XML
```

## 3. Modellumfang

Der Core umfasst `Document`, `DocumentReference`, `DocumentDistribution`,
Metadaten, Status, Typ, Gültigkeit und Kennungen. Akteursrollen werden über
Participation modelliert.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-doc.ttl`
- Core Shapes: `shapes/conx-doc-core.shacl.ttl`
- Beispiele und Tests: `tests/valid/` und `tests/invalid/`
- Referenzvokabulare: Dokumenttyp und Dokumentstatus
