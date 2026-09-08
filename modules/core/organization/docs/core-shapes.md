# Organization Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Organization Core Shapes

Die Organization Core Shapes validieren die allgemeinen, anwendungsfallunabhängigen Datenverträge der Construct-X Organisationsontologie. Die T-Box bleibt unter der Open-World-Annahme semantisch offen; das Core-Profil prüft konkrete Datenlieferungen.

```text
Shape-Graph:  modules/core/organization/shapes/conx-org-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/organization/core
Versions-IRI: https://www.construct-x.org/shapes/organization/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/organization/core#
Version:      0.1.0
```

## 1. Geprüfte Verträge

- Alle fünf lokalen Ressourcentypen werden über IRIs referenziert und passend typisiert.
- Jede `Organization` besitzt mindestens einen nicht leeren Namen.
- Jede `LegalEntity` besitzt zusätzlich einen rechtlichen Namen, genau ein `xsd:date`-Registerdatum, mindestens einen strukturierten ADMS-Identifier und mindestens eine AddressAssignment mit `LegalAddressRole`.
- `legalForm` ist optional, höchstens einmal vorhanden und verweist auf ein SKOS-Konzept.
- Jede `OrganizationalUnit` besitzt mindestens eine `unitOf`-Beziehung.
- Jede `Membership` verbindet genau einen Agenten mit genau einer Organisation.
- Jede `LegalRepresentation` verbindet genau eine Legal Entity mit genau einer Person.
- Direkte Selbsthierarchien, Selbstzuordnungen von Units und Selbstmitgliedschaften werden abgelehnt.

Zusätzliche Properties bleiben zulässig. Das Profil verwendet kein `sh:closed true`. Inverse Hierarchierichtungen müssen nicht redundant im Datengraph gespeichert werden.

## 2. Zusammenspiel

Die Organization Shapes übernehmen keine fremden Datenverträge:

- Address Core prüft AddressAssignments, Rollen und Adressen.
- Contact Core prüft Kontaktpunkte und die als Website-Kontakt modellierte Homepage.
- Person Core prüft enthaltene Personendaten.
- Das importierte `identifier/core` Shape prüft Typ, genau eine literale `skos:notation` und optional eine textuelle `adms:schemaAgency`.

Die automatisierten Tests laden diese Shape- und T-Box-Graphen gemeinsam und führen PySHACL ohne Inferenz aus. Das Address-Rollen- sowie die Contact-Referenzvokabulare werden dem Datengraph hinzugefügt.

## 3. Testdaten

Gültige Testgraphen liegen unter `modules/core/organization/tests/valid`. Gezielte Fehlerfälle liegen unter `modules/core/organization/tests/invalid`. Die acht ungültigen Graphen decken alle 36 stabilen Fehlercodes aus dem [SHACL-Anforderungsdokument](shacl-requirements.md) ab.

Die Tests werden aus dem Repository-Stamm ausgeführt:

```text
uv run pytest tests/test_organization_ontology.py tests/test_organization_shapes.py -q
```

## 4. Bewusst nicht geprüft

- geschlossene Listen rechtlich zulässiger Kennungs-, Rechtsform- oder Tätigkeitsschemata,
- Register-, VIES-, GLEIF- oder andere externe Live-Prüfungen,
- Mitgliedschaftsrolle und Gültigkeitszeitraum,
- Vertretungsart und Gesamtvertretungsregeln,
- Credentials, Finanzdaten, Prozessrollen, Provenienz und Zugriffsschutz.

Diese Bereiche gehören in spätere Fach- oder Jurisdiktionsprofile beziehungsweise eigenständige Module.

## 5. Verständliches Beispiel

> Eine Legal Entity benötigt im Core einen rechtlichen Namen, ein
> Registerdatum und mindestens eine gültige Kennung. Bankkonto und
> Versicherungsnachweis werden dagegen nicht vom Organization-Shape geprüft.
