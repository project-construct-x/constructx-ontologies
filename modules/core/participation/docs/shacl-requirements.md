# Fachliche SHACL-Anforderungen für den Participation-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Participation Core Shapes

## 1. Zweck

Dieses Dokument legt die ausführbaren Datenqualitätsanforderungen für das
Participation-Modul fest. Es beschreibt Shape-Targets, Constraints,
Schweregrade, stabile Fehlercodes sowie gültige und ungültige Szenarien.

Die ausführbare Umsetzung liegt in:

```text
modules/core/participation/shapes/conx-part-core.shacl.ttl
```

T-Box, Shape-Graph, Rollen-Vokabular und Testdaten setzen diese Anforderungen
in Version `0.1.0` um.

Grundlagen:

- [Quellenanalyse](source-analysis.md)
- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Begriffskatalog](term-catalog.md)
- [Fachliches Konzeptmodell](concept-model.md)
- [Modulgrenzen](module-boundaries.md)
- [Participation-Diagramme](diagrams/participation-concept-model.md)

## 2. Shape-Set

```text
Shape-Graph:  modules/core/participation/shapes/conx-part-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/participation/core
Versions-IRI: https://www.construct-x.org/shapes/participation/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/participation/core#
Prefix:       conx-part-sh
Version:      0.1.0
```

Diese Werte sind durch Shape-Graph und `module.yaml` für Version `0.1.0`
verbindlich umgesetzt.

## 3. Validierungsprinzipien

### 3.1 OWL und SHACL

- OWL beschreibt Klassen, Bedeutung, Domain, Range und
  Unterklassenbeziehungen unter der Open-World-Annahme.
- SHACL prüft den konkret gelieferten Datengraphen.
- Pflichtfelder, Maximalwerte, Datumsreihenfolge und Eindeutigkeit werden im
  Core Shape und nicht als harte OWL-Kardinalitäten umgesetzt.
- Das Shape bleibt für zusätzliche Properties offen. `sh:closed true` ist
  nicht vorgesehen.
- Die Validierung wird gemeinsam mit der Participation- und Agent-T-Box
  ausgeführt.
- Rollen-Vokabulare werden nur mitgeladen, wenn der jeweilige Test- oder
  Anwendungsgraph sie verwendet.
- Die Regeln müssen ohne aktivierte RDFS- oder OWL-Inferenz funktionieren.

### 3.2 Explizite Typisierung

Jede Ressource, die als Participation verwendet wird oder eine lokale
Participation-Property trägt, muss explizit als `conx-part:Participation`
typisiert sein.

Der Wert von `participant` muss als `conx-agent:Agent` oder als bekannte
Unterklasse von `Agent`, beispielsweise `conx-person:Person` oder
`conx-org:Organization`, typisiert sein. Eine blöß aus einer Property-Domain
abgeleitete Typisierung reicht nicht.

Jeder Rollenwert muss explizit `conx-part:Role` sein. Eine alleinige
Typisierung als `skos:Concept` reicht nicht, weil nicht jedes SKOS-Konzept eine
Agentenrolle bezeichnet.

Der Kontext benötigt keinen Participation-eigenen Typ.

### 3.3 Ressourcenform

| Ressource | Core-Anforderung | Begründung |
| --- | --- | --- |
| `Participation` | IRI | eigenständige, referenzierbare Beziehungsressource mit fachlicher Identität |
| `participant` | IRI | Agenten werden als fachlich identifizierbare Ressourcen referenziert |
| `role` | IRI | Rollen sind stabile kontrollierte Vokabularwerte |
| `context` | IRI oder Blank Node | der Kontexttyp bleibt offen und folgt dem besitzenden Fachmodul |

Literale sind für alle drei Kernbeziehungen ausgeschlossen. Blank Nodes für
Participation, Agent oder Rolle sind im Core-Profil nicht zulässig. Ein
späteres Fachprofil darf für den Kontext eine IRI verlangen.

### 3.4 Schweregrade

Alle in diesem Dokument definierten Core-Verstöße verwenden
`sh:Violation`. Das Core Shape erzeugt keine Warnungen für Empfehlungen wie
die Verwendung eines bestimmten Rollen-Schemes oder die Angabe von
Gültigkeitsdaten.

Spätere Fachprofile dürfen strengere Regeln und weitere Schweregrade
ergänzen.

### 3.5 Fehlermeldungen

Jeder Constraint erhält:

- eine deutsche `sh:message`,
- eine englische `sh:message`,
- den stabilen Anforderungsbezeichner aus diesem Dokument,
- einen konkreten Ergebnispfad, soweit SHACL ihn bestimmen kann.

Der Bezeichner steht in beiden Meldungen in eckigen Klammern, zum Beispiel
`[PART-010]`.

## 4. Verantwortungsgrenzen

| Anforderung | Zuständiges Shape-Set | Regel im Participation Core Shape |
| --- | --- | --- |
| Struktur einer Participation | `participation/core` | vollständig prüfen |
| Agententyp | `participation/core` mit Agent-T-Box | Agent-Referenz und Typ prüfen |
| Person- und Organisationsdaten | `person/core`, `organization/core` | nicht duplizieren |
| Rollenwert als `Role` | `participation/core` | IRI und expliziten Typ prüfen |
| Zugehörigkeit zum minimalen Rollen-Scheme | Referenzdatensatz oder Fachprofil | nicht im offenen Core erzwingen |
| Rollen für Lieferschein und weitere Fachmodule | jeweiliges Fachprofil | nicht vorsorglich im Participation Core prüfen |
| Typ und Inhalt des Kontextes | besitzendes Fachmodul | nur Ressourcenform prüfen |
| Aktivitäts- und Ereignisteilnahme | spätere Aktivitätsontologie | nicht prüfen |
| Membership | `organization/core` | nicht als Participation behandeln |
| Provenienz, Nachweis, Status und Berechtigung | andere Fach- oder Governance-Profile | nicht prüfen |

## 5. Beschlossene MVP-Verbindlichkeit

| Thema | Entscheidung |
| --- | --- |
| Participation | genau ein Agent, genau eine Rolle und genau ein Kontext |
| Agent | IRI und typisiert als `conx-agent:Agent` oder bekannte Unterklasse |
| Rolle | IRI und explizit als `conx-part:Role` typisiert |
| Kontext | genau eine IRI oder ein Blank Node; keine lokale Kontextklasse |
| Zeit | `startDate` und `endDate` jeweils optional und höchstens einmal als `xsd:date` |
| Datumsreihenfolge | bei zwei Angaben gilt `startDate <= endDate` |
| Eindeutigkeit | eine Participation pro Kombination aus Agent, Rolle und Kontext |
| Rollen-Scheme | im offenen Core nicht geschlossen |
| Zusätzliche Properties | erlaubt |
| Inverse Beziehungen | nicht erforderlich und nicht Teil des MVP |

Start- und Enddatum sind nicht Bestandteil des Eindeutigkeitsschlüssels.
Unterschiedliche Datumswerte legitimieren daher keine zweite Participation
mit derselben Kombination aus Agent, Rolle und Kontext.

## 6. Shape-Katalog

| Shape-IRI | Typ | Target beziehungsweise Verwendung | Aufgabe |
| --- | --- | --- | --- |
| `conx-part-sh:ParticipationShape` | Node Shape | Participation-Klasseninstanzen und Subjekte lokaler Participation-Properties | Gesamtvertrag der Rollenzuordnung |
| `conx-part-sh:ParticipationIriShape` | wiederverwendbares Node Shape | von `ParticipationShape` referenziert | verlangt eine IRI |
| `conx-part-sh:ExplicitParticipationTypeShape` | wiederverwendbares Node Shape | von `ParticipationShape` referenziert | verlangt den expliziten lokalen Typ |
| `conx-part-sh:AgentReferenceShape` | wiederverwendbares Node Shape | Wert von `participant` | prüft IRI und Agent-Typ |
| `conx-part-sh:RoleReferenceShape` | wiederverwendbares Node Shape | Wert von `role` | prüft IRI und expliziten Role-Typ |
| `conx-part-sh:ContextReferenceShape` | wiederverwendbares Node Shape | Wert von `context` | erlaubt IRI oder Blank Node |

Die Hilfs-Shapes besitzen keine globalen Targets. Sie werden nur von den
benannten Property- beziehungsweise Node-Shapes aufgerufen.

## 7. Targets

`conx-part-sh:ParticipationShape` besitzt folgende Targets:

- `sh:targetClass conx-part:Participation`,
- `sh:targetSubjectsOf conx-part:participant`,
- `sh:targetSubjectsOf conx-part:role`,
- `sh:targetSubjectsOf conx-part:context`,
- `sh:targetSubjectsOf conx-part:startDate`,
- `sh:targetSubjectsOf conx-part:endDate`.

Dadurch werden auch untypisierte Ressourcen erfasst, sobald sie eine lokale
Participation-Property verwenden. Ein Datenhalter kann die Typanforderung
nicht umgehen, indem nur `participant`, `role` und `context` angegeben werden.

Werte von `participant`, `role` oder `context` werden nicht selbst als
Participation getargetet.

## 8. Node-Constraints

| ID | Fokus | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-001` | Participation | Ressourcenform | Fokusknoten muss eine IRI sein |
| `PART-002` | Participation | expliziter Typ | Fokusknoten muss explizit `conx-part:Participation` sein |

`PART-002` gilt auch für jedes Subjekt einer lokalen Participation-Property.
Weitere Typen am selben Knoten bleiben erlaubt.

## 9. Participant-Constraints

| ID | Property | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-010` | `participant` | Mindestwert | mindestens ein Wert |
| `PART-011` | `participant` | Maximalwert | höchstens ein Wert |
| `PART-012` | `participant` | Ressourcenform | Wert muss eine IRI sein |
| `PART-013` | `participant` | Agententyp | Wert muss `conx-agent:Agent` oder Instanz einer bekannten Unterklasse sein |

Zusammen ergeben `PART-010` und `PART-011` genau einen Agenten. Ein Agent darf
in mehreren Participations vorkommen, sofern sich Rolle oder Kontext
unterscheiden.

Das Participation Shape prüft keine Namen, Identifier, Adressen oder
Kontaktdaten des Agenten.

## 10. Role-Constraints

| ID | Property | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-020` | `role` | Mindestwert | mindestens ein Wert |
| `PART-021` | `role` | Maximalwert | höchstens ein Wert |
| `PART-022` | `role` | Ressourcenform | Wert muss eine IRI sein |
| `PART-023` | `role` | Rollentyp | Wert muss explizit `conx-part:Role` sein |

Eine Participation ohne Rolle ist ungültig. Besitzt ein Agent im selben
Kontext zwei Rollen, werden zwei Participations angelegt.

`PART-023` verlangt weder `skos:inScheme` noch einen Wert aus
`participation-role`. Dadurch bleiben getrennte Fachvokabulare und externe,
ausdrücklich als `conx-part:Role` typisierte Rollenwerte zulässig.

## 11. Context-Constraints

| ID | Property | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-030` | `context` | Mindestwert | mindestens ein Wert |
| `PART-031` | `context` | Maximalwert | höchstens ein Wert |
| `PART-032` | `context` | Ressourcenform | Wert muss IRI oder Blank Node sein |

Der Core verlangt keinen bestimmten Kontexttyp. Insbesondere wird kein
`conx-part:Context` eingeführt oder vorausgesetzt. Literale sind als Kontext
ungeeignet, weil sie keine fachlich beschreibbare Ressource darstellen.

## 12. Zeitliche Constraints

| ID | Property oder Vergleich | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-040` | `startDate` | Maximalwert | höchstens ein Wert |
| `PART-041` | `startDate` | Datentyp | jeder Wert muss `xsd:date` sein |
| `PART-042` | `endDate` | Maximalwert | höchstens ein Wert |
| `PART-043` | `endDate` | Datentyp | jeder Wert muss `xsd:date` sein |
| `PART-044` | `startDate`, `endDate` | Reihenfolge | wenn beide Werte vorliegen, darf `startDate` nicht nach `endDate` liegen |

`PART-044` soll mit einer SHACL-Core-Vergleichskomponente wie
`sh:lessThanOrEquals` umgesetzt werden. Eine SPARQL-Regel ist dafür nur dann
zulässig, wenn die Core-Komponente im eingesetzten Validator nachweislich
nicht korrekt arbeitet.

Folgende Fälle bleiben gültig:

| Angaben | Bewertung |
| --- | --- |
| kein Datum | Gültigkeitsgrenzen nicht angegeben |
| nur `startDate` | Beginn angegeben, Ende unbekannt oder nicht angegeben |
| nur `endDate` | Ende angegeben, Beginn unbekannt oder nicht angegeben |
| beide Daten gleich | eintagesbezogene oder am selben Tag begrenzte Gültigkeit |
| `startDate` vor `endDate` | geordnete Gültigkeit |

Die Shapes prüfen nicht, ob die Participation am Validierungsdatum aktuell
gilt.

## 13. Eindeutigkeits-Constraint

| ID | Fokus | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `PART-050` | Participation | Tupel-Eindeutigkeit | keine andere Participation darf denselben `participant`, dieselbe `role` und denselben `context` besitzen |

SHACL Core besitzt keine allgemeine Komponente für einen zusammengesetzten
Schlüssel. `PART-050` ist daher als lokaler `sh:SPARQLConstraint` umgesetzt.

Die Abfrage muss:

1. nur vollständige Kombinationen aus Agent, Rolle und Kontext vergleichen,
2. eine andere Participation mit denselben drei RDF-Terms erkennen,
3. den Fokusknoten selbst ausschließen,
4. pro Duplikatpaar ein deterministisches Ergebnis erzeugen,
5. Datumswerte bewusst nicht in den Vergleich einbeziehen.

Die Eindeutigkeit gilt innerhalb des gesamten Datengraphen, der einem
Validierungslauf übergeben wird. Das Shape kann keine Duplikate erkennen, die
nur in einem nicht mitgeladenen externen Graphen oder einem anderen
Datenbestand liegen. Dataset- oder Datenraumprofile müssen deshalb festlegen,
welche benannten Graphen für diese Prüfung gemeinsam validiert werden.

## 14. Rollen-Vokabular und Core-Offenheit

Das minimale Rollen-Vokabular ist ein getrennt versionierter Referenzdatensatz.
Seine eigene Qualität wird durch automatisierte Dataset-Tests geprüft, nicht
durch eine geschlossene Werteliste im Participation Core Shape.

Jeder Wert des minimalen Vokabulars muss:

1. eine IRI besitzen,
2. `conx-part:Role` und `skos:Concept` sein,
3. genau dem Scheme `https://www.construct-x.org/vocab/participation-role`
   zugeordnet sein,
4. genau eine stabile `skos:notation` besitzen,
5. je eine deutsche und englische Vorzugsbezeichnung besitzen,
6. je eine deutsche und englische Definition besitzen.

Das Vokabular enthält in Version `0.1.0` genau die fünf freigegebenen
Startwerte. Diese Geschlossenheit ist eine Versionsaussage über den
Referenzdatensatz, keine globale Einschränkung aller Participations.

Weitere Rollen, beispielsweise Rollen eines Lieferscheins, werden im
Entwicklungsprozess des jeweiligen Fachmoduls definiert und dürfen ein eigenes
Concept Scheme verwenden.

## 15. Gültige Kernbeispiele

### 15.1 Minimale Participation

```turtle
ex:agent-a
    a conx-agent:Agent .

ex:contractor-role
    a conx-part:Role .

ex:participation-a
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role ex:contractor-role ;
    conx-part:context ex:contract-x .
```

### 15.2 Participation mit Gültigkeitsdaten

```turtle
ex:participation-b
    a conx-part:Participation ;
    conx-part:participant ex:agent-b ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x ;
    conx-part:startDate "2026-01-15"^^xsd:date ;
    conx-part:endDate "2026-12-31"^^xsd:date .
```

Der Rollenwert aus dem Referenzvokabular muss im gemeinsam geladenen Graphen
als `conx-part:Role` typisiert sein.

### 15.3 Externe Fachrolle

```turtle
domain-role:ExampleDocumentRole
    a conx-part:Role, skos:Concept ;
    skos:inScheme domain-role:ExampleRoleScheme .

ex:participation-c
    a conx-part:Participation ;
    conx-part:participant ex:agent-c ;
    conx-part:role domain-role:ExampleDocumentRole ;
    conx-part:context ex:document-x .
```

Das Beispiel bleibt im offenen Core gültig, obwohl die Rolle nicht zum
minimalen `participation-role`-Scheme gehört.

### 15.4 Blank Node als Kontext

```turtle
ex:participation-d
    a conx-part:Participation ;
    conx-part:participant ex:agent-d ;
    conx-part:role part-role:SupplierRole ;
    conx-part:context [ ex:localContextCode "A-17" ] .
```

Das Core Shape beurteilt nur die Ressourcenform des Kontextes. Ein Fachprofil
kann eine IRI oder einen konkreten Kontexttyp verlangen.

## 16. Ungültige Kernbeispiele

### 16.1 Fehlende Rolle

```turtle
ex:invalid-a
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:context ex:contract-x .
```

Erwarteter Verstoss: `PART-020`.

### 16.2 Mehrere Agenten

```turtle
ex:invalid-b
    a conx-part:Participation ;
    conx-part:participant ex:agent-a, ex:agent-b ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-x .
```

Erwarteter Verstoss: `PART-011`.

### 16.3 Rolle ohne lokalen Rollentyp

```turtle
ex:not-a-role
    a skos:Concept .

ex:invalid-c
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role ex:not-a-role ;
    conx-part:context ex:contract-x .
```

Erwarteter Verstoss: `PART-023`.

### 16.4 Literal als Kontext

```turtle
ex:invalid-d
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role part-role:ClientRole ;
    conx-part:context "Vertrag X" .
```

Erwarteter Verstoss: `PART-032`.

### 16.5 Verkehrte Datumsreihenfolge

```turtle
ex:invalid-e
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x ;
    conx-part:startDate "2026-12-31"^^xsd:date ;
    conx-part:endDate "2026-01-01"^^xsd:date .
```

Erwarteter Verstoss: `PART-044`.

### 16.6 Doppelte Kombination

```turtle
ex:duplicate-a
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-x ;
    conx-part:startDate "2026-01-01"^^xsd:date .

ex:duplicate-b
    a conx-part:Participation ;
    conx-part:participant ex:agent-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-x ;
    conx-part:startDate "2026-07-01"^^xsd:date .
```

Erwarteter Verstoss: `PART-050`. Die unterschiedlichen Startdaten heben das
Duplikat nicht auf.

## 17. Umgesetzte Testartefakte

### 17.1 Gültige Testgraphen

| Datei | Szenario |
| --- | --- |
| `tests/valid/minimal-participation.ttl` | genau ein Agent, eine Rolle und ein Kontext |
| `tests/valid/dated-participation.ttl` | beide Daten sowie Fälle mit nur einer Datumsgrenze |
| `tests/valid/multiple-roles-and-contexts.ttl` | mehrere unterschiedliche Kombinationen ohne Duplikat |
| `tests/valid/external-role.ttl` | lokale Role-Typisierung ausserhalb des minimalen Schemes |
| `tests/valid/blank-node-context.ttl` | offener Kontext als Blank Node |
| `tests/valid/agent-subclass.ttl` | Participant als Instanz einer Agent-Unterklasse |
| `tests/valid/person-and-organization-participants.ttl` | Person und Organization als konkrete Agent-Unterklassen |

### 17.2 Ungültige Testgraphen

| Datei | Erwartete Fehlercodes |
| --- | --- |
| `tests/invalid/missing-required-values.ttl` | `PART-010`, `PART-020`, `PART-030` |
| `tests/invalid/invalid-participant.ttl` | `PART-011`, `PART-012`, `PART-013` |
| `tests/invalid/invalid-role.ttl` | `PART-021`, `PART-022`, `PART-023` |
| `tests/invalid/invalid-context.ttl` | `PART-031`, `PART-032` |
| `tests/invalid/invalid-dates.ttl` | `PART-040`, `PART-041`, `PART-042`, `PART-043`, `PART-044` |
| `tests/invalid/duplicate-participation.ttl` | `PART-050` |
| `tests/invalid/untyped-or-blank-participation.ttl` | `PART-001`, `PART-002` |

Ein Fehlergraph darf mehrere unabhängige Ressourcen enthalten. Jeder
dokumentierte Fehlercode muss dennoch eindeutig einem absichtlich verletzten
Constraint zugeordnet werden können.

## 18. Anforderungen an automatisierte Tests

Die automatisierte Implementierung prüft:

1. Der Shape-Graph besteht die SHACL-Metavalidierung.
2. Alle gültigen Testgraphen validieren ohne `sh:Violation`.
3. Jeder ungültige Testgraph erzeugt alle dokumentierten Fehlercodes.
4. Jeder Fehlercode wird von mindestens einem Testgraphen ausgelöst.
5. Lokale Shape-IRIs und Fehlercodes sind eindeutig.
6. Alle benannten Constraints besitzen deutsche und englische Meldungen.
7. Die Validierung funktioniert mit `inference="none"`.
8. Participation- und Agent-T-Box werden als Ontologiegraph geladen.
9. Das minimale Rollen-Vokabular wird für entsprechende Fixtures mitgeladen.
10. Eine fachfremde, aber explizit als `Role` typisierte Rollen-IRI bleibt
    gültig.
11. Eine allein als `skos:Concept` typisierte Ressource wird als Rolle
    abgelehnt.
12. Eine Person oder Organisation wird über ihre bekannte Agent-Unterklasse
    als `participant` akzeptiert.
13. Ein Literal als Agent, Rolle oder Kontext wird abgelehnt.
14. Ein Blank Node wird als Kontext akzeptiert, aber nicht als Participation,
    Agent oder Rolle.
15. Nur Startdatum, nur Enddatum und gleiche Start-/Enddaten bleiben gültig.
16. Ein Enddatum vor dem Startdatum wird abgelehnt.
17. Die Tupel-Eindeutigkeit erkennt Duplikate unabhängig von Datumswerten.
18. Verschiedene Rollen desselben Agenten im selben Kontext bleiben gültig.
19. Dieselbe Rolle desselben Agenten in verschiedenen Kontexten bleibt
    gültig.
20. Das Shape bleibt für zusätzliche Properties anderer Module offen.

## 19. Bewusst nicht im Core validiert

Das Participation Core Shape prüft nicht:

- ob ein Kontext einen bestimmten fachlichen Typ besitzt,
- ob eine Rolle zum minimalen `participation-role`-Scheme gehört,
- ob die Rollenzuordnung rechtlich oder fachlich belegt ist,
- ob der Agent die Rolle ausüben darf oder dazu befähigt ist,
- ob eine Rolle mit einem bestimmten Kontexttyp kompatibel ist,
- ob die Participation am heutigen Tag aktuell gilt,
- ob fehlende Start- oder Enddaten fachlich plausibel sind,
- ob der Kontext selbst im angegebenen Zeitraum existiert,
- ob eine Aktivität ausgeführt oder ein Ereignis besucht wurde,
- ob eine Membership oder Vertretung aus der Participation folgt,
- ob gleiche Participations in nicht mitgeladenen Graphen existieren,
- ob Provenienz, Nachweise, Status oder Berechtigungen vorhanden sind,
- ob rollenspezifische direkte Beziehungen materialisiert wurden,
- ob externe Ontologien semantisch gleichwertige Begriffe besitzen.

Diese Punkte gehören in Fachprofile, andere Module, Governance-Regeln oder
externe Prüfdienste.

## 20. Umgesetzte Artefakte

1. Participation-T-Box und `module.yaml`.
2. Referenzvokabular `participation-role` samt `dataset.yaml`.
3. Core Shapes mit den Anforderungen `PART-*`.
4. Gültige und ungültige Testgraphen.
5. Automatisierte Ontologie-, Vokabular- und Shape-Tests.
6. Shape-Dokumentation und HTML-Dokumentation.
7. Core-Übersichten, Strukturtests und Build-Metadaten.

## 21. Abnahmekriterien für die Core-Shape-Implementierung

Die Implementierung ist fachlich vollständig, weil:

1. jede Anforderung `PART-*` in einem nachvollziehbaren Constraint umgesetzt
   ist,
2. genau ein Agent, eine Rolle und ein Kontext verlangt werden,
3. Agent und Rolle explizit gegen ihre lokalen Typen geprüft werden,
4. der Kontext ohne lokale Sammelklasse offen bleibt,
5. optionale Datumsgrenzen und ihre Reihenfolge korrekt geprüft werden,
6. der zusammengesetzte Schlüssel innerhalb des Validierungsgraphen greift,
7. externe Rollen-Schemes im Core zulässig bleiben,
8. das minimale Rollen-Vokabular getrennt von der T-Box versioniert wird,
9. keine Agenten-, Kontext-, Aktivitäts-, Membership- oder
   Provenienzsemantik dupliziert wird,
10. alle positiven und negativen Szenarien automatisiert geprüft sind.

## 22. Fachliche Freigabeentscheidung

Vor der Erstellung der `.ttl`-Artefakte wurden anhand dieses Dokuments
ausdrücklich bestätigt:

1. Participation, Agent und Rollenwert müssen IRIs sein; nur der Kontext darf
   auch als Blank Node vorliegen.
2. Ein Rollenwert muss explizit `conx-part:Role` sein; `skos:Concept` allein
   reicht nicht.
3. Das Core Shape bleibt offen für Rollen ausserhalb des minimalen
   Participation-Schemes.
4. Die Eindeutigkeitsregel gilt über den vollständigen, gemeinsam
   validierten Datengraphen und ignoriert Start- und Enddatum.
5. Alle Anforderungen verwenden `sh:Violation`; Empfehlungen werden nicht als
   Warnungen in das Core Shape aufgenommen.
