# Construct-X Organization Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul beschreibt Organisationen, rechtliche Einheiten, interne
Organisationseinheiten, Mitgliedschaften und rechtliche Vertretungen.

## 2. Verständliches Beispiel

> Die Beispiel Bau GmbH ist eine rechtliche Einheit. Sie besitzt eine interne
> Abteilung, Anna Müller ist Mitglied und vertritt die GmbH rechtlich.

```text
LegalEntity -> OrganizationalUnit
Membership: Person -> Organization
LegalRepresentation: Person -> LegalEntity
```

## 3. Modellumfang

Zum Core gehören Namen, Rechtsform, Registerdatum, Tätigkeit, Hierarchien,
Membership und LegalRepresentation. Kontakt, Adresse und Identifier werden aus
den zuständigen Core-Modulen verwendet.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-org.ttl`
- Core Shapes: `shapes/conx-org-core.shacl.ttl`
- Beispiele und Tests: `tests/valid/` und `tests/invalid/`
- Integrationen: Agent, Person, Address, Contact und Identifier
