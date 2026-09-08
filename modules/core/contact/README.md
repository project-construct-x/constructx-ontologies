# Construct-X Contact Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul beschreibt Kontaktpunkte und konkrete Kontaktmethoden für Personen,
Organisationen und weitere kontaktierbare Ressourcen.

## 2. Verständliches Beispiel

> Die Buchhaltung einer Firma ist für Rechnungen per E-Mail und Telefon
> erreichbar. Der Kontaktpunkt beschreibt Zweck und Nutzung; die beiden
> Kontaktmethoden enthalten die konkreten Werte.

```text
Firma -> ContactPoint „Buchhaltung“ -> E-Mail
                                    -> Telefon
```

## 3. Modellumfang

Der Core trennt `ContactPoint`, `ContactMethod`, Kanal, Nutzung, Zweck und
Plattform. Postalische Kontakte verweisen auf eine AddressAssignment.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-contact.ttl`
- Core Shapes: `shapes/conx-contact-core.shacl.ttl`
- Beispiele und Tests: `tests/valid/` und `tests/invalid/`
- Referenzvokabulare: Kanal, Nutzung, Zweck und Plattform
