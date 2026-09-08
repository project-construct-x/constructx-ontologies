# Person Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Person Core Shapes

Die Person Core Shapes validieren die allgemeinen, anwendungsfallunabhängigen Datenverträge der Construct-X Personenontologie. Die T-Box bleibt unter der Open-World-Annahme semantisch offen; das Core-Profil prüft dagegen konkrete Datenlieferungen.

```text
Shape-Graph:  modules/core/person/shapes/conx-person-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/person/core
Versions-IRI: https://www.construct-x.org/shapes/person/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/person/core#
Version:      0.1.0
```

## 1. Geprüfte Verträge

- Personen werden über IRIs referenziert und explizit als `conx-person:Person` typisiert.
- `fullName` und `givenName` sind verpflichtend und dürfen nicht leer sein.
- Weitere Namenswerte und `birthPlaceName` sind Strings oder sprachmarkierte Strings und dürfen nicht leer sein.
- `birthDate` darf höchstens einmal als vollständiges `xsd:date` vorkommen.
- `sex` und `gender` dürfen höchstens einmal vorkommen und verwenden die vier freigegebenen Werte ihrer Referenzvokabulare.
- `citizenship` verweist auf eine `conx-addr:Country`-IRI aus dem Construct-X-Ländervokabular.
- `adms:identifier` bleibt optional; seine Werte werden durch das importierte `identifier/core` Shape auf Identifier-Typ, genau eine literale `skos:notation` und optional eine textuelle `adms:schemaAgency` geprüft.
- `hasIdentityEvidence` verweist auf eine IRI; Inhalte, Gültigkeit und Vertrauensstatus des Nachweises bleiben außerhalb des Personenprofils.

Zusätzliche Properties bleiben zulässig. Das Profil verwendet kein `sh:closed true` und benötigt keine RDFS- oder OWL-Inferenz.

## 2. Referenzgraphen

Für die Prüfung kontrollierter Werte werden gemeinsam mit den Daten geladen:

- `datasets/reference/vocabularies/human-sex/human-sex.ttl`,
- `datasets/reference/vocabularies/gender/gender.ttl`,
- `datasets/reference/administrative-territories/iso-3166-1-countries/data/countries.ttl`.

Die beiden kleinen Geschlechtswertemengen sind zusätzlich als geschlossene `sh:in`-Listen im Shape-Graph festgehalten. Länder werden nicht kopiert, sondern über Klasse und Concept Scheme geprüft.

## 3. Testdaten

Gültige Testgraphen liegen unter `modules/core/person/tests/valid`. Gezielte Fehlerfälle liegen unter `modules/core/person/tests/invalid`. Die automatisierten Tests laden die erforderlichen Referenzgraphen, führen PySHACL ohne Inferenz aus und prüfen Fehlerpfade sowie Anforderungsbezeichner.

Die zusammengesetzten Person- und Identifier-Shapes werden aus dem
Repository-Stamm so validiert:

```text
uv run pytest tests/test_person_shapes.py -q
```

Die Testsuite lädt das importierte Identifier-Shape und die genannten
Referenzgraphen gemeinsam.

## 4. Bewusst nicht geprüft

- konkrete Personen-Identifier-Schemata oder eine geschlossene Schemaliste,
- ein endgültiges maschinenlesbares Issuer-Modell,
- interne Struktur und Vertrauenswürdigkeit von Identitätsnachweisen,
- Kontakt-, Adress-, Organisations- oder Projektbeziehungen,
- allgemeine Provenienz, Reifikation und Zugriffsrechte.

Diese Bereiche gehören in spätere Fachprofile oder eigenständige Module.

## 5. Verständliches Beispiel

> Eine Person mit vollständigem Namen erfüllt den minimalen Core-Vertrag. Eine
> vorhandene Kennung muss zusätzlich genau eine Notation besitzen; Details
> eines Ausweisdokuments werden hier nicht geprüft.
