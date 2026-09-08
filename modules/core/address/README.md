# Construct-X Address Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul beschreibt strukturierte Adressen und ihre kontextbezogene Zuordnung
zu Personen, Organisationen oder anderen Ressourcen.

## 2. Verständliches Beispiel

> Eine Organisation kann dieselbe Anschrift als Liefer- und Rechnungsadresse
> verwenden. Die Anschrift wird nur einmal gespeichert; ihre Rollen stehen an
> der Adresszuordnung.

```text
Organisation -> AddressAssignment -> Address
                    +-> Lieferadresse
                    +-> Rechnungsadresse
```

## 3. Modellumfang

Zum Core gehören `Address`, `AddressAssignment`, `AddressRole` und
administrative Gebiete. Kontaktkanäle und Koordinatenmodelle bleiben in ihren
zuständigen Modulen.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-addr.ttl`
- Core Shapes: `shapes/conx-addr-core.shacl.ttl`
- Beispiele: `examples/`
- Tests: `tests/valid/` und `tests/invalid/`
- Referenzdaten: Adressrollen sowie ISO- und NUTS-Gebiete unter `datasets/reference/`
