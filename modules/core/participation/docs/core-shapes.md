# Participation Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Participation Core Shapes

Die Participation Core Shapes validieren die allgemeinen,
anwendungsfallunabhängigen Datenverträge der Construct-X Participation-
Ontologie. Die T-Box bleibt unter der Open-World-Annahme semantisch offen; das
Core-Profil prüft konkrete Datenlieferungen.

```text
Shape-Graph:  modules/core/participation/shapes/conx-part-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/participation/core
Versions-IRI: https://www.construct-x.org/shapes/participation/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/participation/core#
Version:      0.1.0
```

## 1. Geprüfte Verträge

- Eine Participation muss eine IRI und explizit als
  `conx-part:Participation` typisiert sein.
- `participant`, `role` und `context` müssen jeweils genau einmal vorkommen.
- `participant` muss eine IRI und als `conx-agent:Agent` oder bekannte
  Unterklasse typisiert sein.
- `role` muss eine IRI und explizit als `conx-part:Role` typisiert sein.
- Das Core-Profil akzeptiert Rollen aus anderen Concept Schemes.
- `context` darf eine IRI oder ein Blank Node sein; ein Kontexttyp wird nicht
  verlangt.
- `startDate` und `endDate` dürfen jeweils höchstens einmal als `xsd:date`
  vorkommen.
- Wenn beide Daten angegeben sind, darf `startDate` nicht nach `endDate`
  liegen.
- Eine zweite Participation mit derselben Kombination aus Agent, Rolle und
  Kontext wird innerhalb des Validierungsgraphen abgelehnt.

Start- und Enddatum gehören nicht zum Eindeutigkeitsschlüssel. Das Profil
verwendet kein `sh:closed true`; zusätzliche Properties bleiben zulässig.

## 2. Referenzgraphen

Für die Validierung werden gemeinsam geladen:

- `modules/core/agent/ontology/conx-agent.ttl`,
- `modules/core/person/ontology/conx-person.ttl` und
  `modules/core/organization/ontology/conx-org.ttl` für die Integrationstests
  ihrer konkreten Agent-Unterklassen,
- `modules/core/participation/ontology/conx-part.ttl`,
- `datasets/reference/vocabularies/participation-role/participation-role.ttl`,
  wenn die Test- oder Anwendungsdaten Werte dieses Vokabulars verwenden.

Das Rollen-Vokabular dient nicht als geschlossene Core-Werteliste. Ein anderes
Fachvokabular bleibt gültig, wenn sein Rollenwert explizit als
`conx-part:Role` typisiert ist.

## 3. Eindeutigkeitsprüfung

Die Kombination aus `participant`, `role` und `context` wird durch einen
lokalen SHACL-SPARQL-Constraint geprüft. Die Regel kann nur Graphen erkennen,
die demselben Validierungslauf übergeben werden. Datenraum- oder
Dataset-Profile müssen daher festlegen, welche benannten Graphen gemeinsam
validiert werden.

## 4. Testdaten

Gültige Testgraphen liegen unter `modules/core/participation/tests/valid`.
Gezielte Fehlerfälle liegen unter
`modules/core/participation/tests/invalid`. Die automatisierten Tests laden
die erforderlichen Ontologie- und Referenzgraphen, führen PySHACL ohne
Inferenz aus und prüfen die stabilen Fehlercodes `PART-*`.

```text
uv run pytest tests/test_participation_shapes.py
```

## 5. Bewusst nicht geprüft

- konkreter fachlicher Typ des Kontextes,
- Zugehörigkeit einer Rolle zum minimalen Participation-Scheme,
- rechtlicher oder fachlicher Nachweis der Rollenzuordnung,
- Befähigung oder Berechtigung des Agenten,
- aktuelle Gültigkeit am Validierungsdatum,
- Aktivitäts- oder Ereignisteilnahme,
- Membership, Provenienz, Status oder direkte Rollenproperties,
- Duplikate in nicht gemeinsam geladenen Graphen.

Diese Bereiche gehören in Fachprofile, andere Module oder externe
Prüfdienste.

## 6. Verständliches Beispiel

> Eine Participation mit Anna als Agentin, „Architektin“ als Rolle und einem
> Bauvorhaben als Kontext ist vollständig. Fehlt die Rolle, ist nicht erkennbar,
> in welcher Funktion Anna beteiligt ist, und der Core meldet einen Fehler.
