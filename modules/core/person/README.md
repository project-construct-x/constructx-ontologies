# Construct-X Person Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul beschreibt intrinsische Kerndaten realer natürlicher Personen.

## 2. Verständliches Beispiel

> Anna Müller wird mit Namen und Geburtsdatum als Person beschrieben. Ihre
> Telefonnummer liegt an einem Kontaktpunkt, ihre Firmenzugehörigkeit an einer
> Membership und ihre Personalnummer an einer Identifier-Ressource.

```text
Person -> ContactPoint
       -> Membership
       -> Identifier
```

## 3. Modellumfang

Zum Core gehören Namen, Geburtsangaben, `sex`, `gender`, Staatsangehörigkeit,
Kennungen und eine offene Verknüpfung zu Identitätsnachweisen.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-person.ttl`
- Core Shapes: `shapes/conx-person-core.shacl.ttl`
- Beispiele und Tests: `tests/valid/` und `tests/invalid/`
- Referenzvokabulare: `human-sex` und `gender`
