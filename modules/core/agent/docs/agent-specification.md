# Fachliche Spezifikation des Agent-Kerns

**Status:** Implementierte Spezifikation der T-Box 0.1.0  
**Stand:** 27. August 2026

## 1. Zweck

`core/agent` stellt eine minimale gemeinsame Oberklasse für Akteure im Construct-X-Ontologienetzwerk bereit. Das Modul verhindert, dass allgemeine Beziehungen entweder im Personen- oder im Organisationsmodul verankert und dadurch fachlich einseitig werden.

Der Agent-Kern ist ein Integrationspunkt, kein eigenständiges Stammdatenmodell. Personen- und Organisationsdaten verbleiben in ihren zuständigen Modulen.

## 2. Entscheidung

Construct-X führt die lokale Klasse `conx-agent:Agent` in einem separaten Kernmodul ein.

```text
conx-agent:Agent
  ├── conx-person:Person
  └── conx-org:Organization
```

Die Klasse wird nicht als `conx-person:Agent` definiert. Andernfalls müsste das Organisationsmodul von der Personenontologie abhängen, obwohl Organisationen keine Personen sind.

## 3. Öffentliche IRIs

```text
Ontologie-IRI: https://www.construct-x.org/ontology/agent
Versions-IRI:  https://www.construct-x.org/ontology/agent/0.1.0
Namespace:     https://www.construct-x.org/ontology/agent#
Prefix:        conx-agent
```

Die Version `0.1.0` ist die aktuelle Entwurfsfassung des minimalen Agent-Kerns.

## 4. Klasse `conx-agent:Agent`

| Punkt | Festlegung |
| --- | --- |
| Bezeichnung | Agent / Akteur |
| Definition | Entität, die in einem fachlichen Kontext handeln, Verantwortung tragen oder als Herausgeber beziehungsweise Beteiligter referenziert werden kann |
| Modul | `modules/core/agent` |
| Oberklasse | Keine lokale Oberklasse im MVP |
| Lokale Unterklassen | `conx-person:Person`, `conx-org:Organization` |
| Pflichtattribute | Keine |
| Instanziierung | Direkte Instanzen sind technisch möglich, sollen aber nur verwendet werden, wenn kein genauerer lokaler Agententyp bekannt ist |
| Primäre Quellen | FOAF, SEMIC Core Vocabularies, W3C Organization Ontology |
| Externes Alignment | `rdfs:subClassOf foaf:Agent` implementiert |

### Definitionen

Deutsch:

> Eine Entität, die in einem fachlichen Kontext handeln, Verantwortung tragen oder als Beteiligter referenziert werden kann.

Englisch:

> An entity that can act, bear responsibility, or be referenced as a participant in a domain context.

Die Definition bleibt bewusst allgemeiner als „natürliche oder juristische Person“. Dadurch können später auch andere klar definierte Akteurstypen ergänzt werden, ohne diese schon im MVP zu behaupten.

## 5. Umfang des MVP

Der Agent-Kern enthält in Version `0.1.0` genau:

- die Klasse `conx-agent:Agent`,
- deutsch- und englischsprachige Labels und Definitionen,
- Modul- und Ontologiemetadaten,
- ein konservatives Alignment zu `foaf:Agent`.

Der Agent-Kern enthält zunächst keine eigenen Properties. Das hält ihn stabil und verhindert, dass fachliche Beziehungen ohne klaren Eigentümer im Basismodul gesammelt werden.

## 6. Ausdrücklich außerhalb des Agent-Kerns

- Namen und Geburtsdaten,
- `sex`, `gender` und Staatsangehörigkeit,
- Organisationsname und Organisationsstruktur,
- Kontaktpunktwerte und Kontaktrollen,
- Adressen und Adressrollen,
- Mitgliedschaften, Beschäftigung und Stellen,
- Projektbeteiligungen,
- Identifikatorstruktur,
- Credentials, Schlüssel und Identitätsdokumente,
- generische Berechtigungs- oder Vollmachtsmodelle,
- Softwareagenten als bereits festgelegte Unterklasse.

Ein späterer `SoftwareAgent` ist möglich, aber erst nach einem bestätigten Construct-X-Anwendungsfall. Technische Services werden nicht automatisch als Agenten klassifiziert.

## 7. Warum keine Agent-Properties im MVP?

Eine Property mit Domain `Agent` wirkt automatisch auf Personen und Organisationen. Das ist nur dann korrekt, wenn die Beziehung wirklich für alle relevanten Agenttypen gilt und vom Agent-Modul fachlich verantwortet wird.

Für die bisher diskutierten Beziehungen liegen geeignetere Eigentümer vor:

| Beziehung | Eigentümer | Verwendung von `Agent` |
| --- | --- | --- |
| Kontaktzuordnung | `core/contact` | `hasContactPoint` bleibt domänenoffen und kann für Agenten verwendet werden |
| Mitgliedschaft | `core/organization` | `member` verwendet `conx-agent:Agent` als Wertebereich |
| Rechtliche Vertretung | `core/organization` | Die vertretene Ressource ist eine Legal Entity; die vertretende Ressource ist eine Person |
| Projektbeteiligung | Projektmodul | Beteiligter kann ein Agent sein |
| `issuedBy` | Identifier-/Identitätsmodell | Herausgeber kann ein Agent sein |
| `hasIdentityEvidence` | `core/person` | Domain bleibt Person, nicht jeder Agent |
| Adresse | `core/address` | `hasAddressAssignment` bleibt domänenoffen und kann für Agenten verwendet werden |

## 8. Alignment-Strategie

### 8.1 FOAF

FOAF ist das naheliegende breite Alignment-Ziel:

```turtle
conx-agent:Agent rdfs:subClassOf foaf:Agent .
```

`rdfs:subClassOf` ist gegenüber `owl:equivalentClass` zu bevorzugen. FOAF beschreibt einen Agenten sehr breit als etwas, das handeln kann. Construct-X soll seinen lokalen Scope kontrollieren und kann deshalb enger bleiben.

### 8.2 SEMIC

SEMIC bestätigt das Muster einer gemeinsamen Agent-Oberklasse für Person und Organisation. Vor einer maschinenlesbaren Ausrichtung sind die kanonische IRI, Version und Importwirkung des konkret verwendeten SEMIC-Artefakts zu prüfen.

### 8.3 Schema.org

Ein direktes Alignment zu `schema:Thing` bringt keinen fachlichen Mehrwert. `schema:Person` wird am Personenbegriff und `schema:Organization` am Organisationsbegriff bewertet.

### 8.4 W3C ORG

W3C ORG verwendet `foaf:Agent` für Mitglieder und andere Akteure. Das lokale FOAF-Alignment ermöglicht dem Organisationsmodul eine kompatible Spezialisierung, ohne ORG in den Agent-Kern kopieren zu müssen.

## 9. Abhängigkeitsrichtung

```text
core/person       ──importiert/referenziert──> core/agent
core/organization ──importiert/referenziert──> core/agent
domain/project    ──referenziert optional────> core/agent
```

Person und Organisation referenzieren den Agent-Kern als gemeinsame Oberklasse.
`core/agent` selbst darf nicht von `person`, `contact`, `organization` oder
`project` abhängen. Dadurch bleiben die Abhängigkeiten zyklusfrei.

## 10. Kompetenzfragen

### ACQ-01: Kann eine natürliche Person als allgemeiner Akteur verwendet werden?

Ja. Jede `conx-person:Person` ist eine Unterklasse von `conx-agent:Agent`.

### ACQ-02: Kann eine Organisation denselben Kontaktmechanismus verwenden wie eine Person?

Ja. Person und Organisation können dieselbe domänenoffene Property
`conx-contact:hasContactPoint` verwenden. Das Kontaktmodul besitzt diese
Property und validiert die Kontaktpunktstruktur. Das Agent-Modul definiert keine
eigene Kontakt-Property.

### ACQ-03: Kann die ausstellende Stelle eines Identifikators oder Nachweises modelliert werden?

Ja. Eine in der Identifier- oder Identitätsarchitektur definierte Beziehung `issuedBy` kann `conx-agent:Agent` als Wertebereich verwenden.

### ACQ-04: Gehören Namen, Kontaktinformationen oder Adressen direkt zum Agenten?

Nein. Natürliche Personen und Organisationen besitzen unterschiedliche
Namenssemantik. Kontaktwerte werden über das Kontaktmodul zugeordnet. Adressen
werden über das Adressmodul zugeordnet. Beide Muster bleiben domänenoffen, damit
auch Projekte, Standorte oder spätere Ressourcen sie verwenden können.

### ACQ-05: Muss jeder Agent als Person oder Organisation klassifiziert sein?

Nein. Die T-Box erzwingt keine abgeschlossene Klassenaufteilung. Anwendungsprofile können genauere Typen verlangen.

## 11. Implementierter OWL- und SHACL-Umfang

### OWL

Die T-Box enthält:

- eine Ontologie-Ressource mit versionierter Metadatenstruktur,
- `conx-agent:Agent` als `owl:Class`,
- Labels und Definitionen in Deutsch und Englisch,
- ein konservatives FOAF-Alignment.

Es sind keine OWL-Kardinalitäten und keine Disjunktheitsaxiome erforderlich.

### SHACL

Ein eigenständiges Core Shape für `Agent` bringt ohne Agent-Properties zunächst keinen Validierungsnutzen. Validierungsregeln werden auf konkreten Unterklassen oder Beziehungen definiert:

- Person-Shape für Personendaten,
- Kontakt-Shape für Kontaktzuordnungen,
- Organization-Shapes für Organisationsdaten, Mitgliedschaften und rechtliche
  Vertretungen.

Das Agent-Modul besitzt deshalb in Version `0.1.0` kein eigenes Shape-Artefakt.

## 12. Konzeptionelles Beispiel

```turtle
@prefix conx-agent: <https://www.construct-x.org/ontology/agent#> .
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix ex: <https://example.org/id/> .

ex:person-123 a conx-person:Person .

# Folgt semantisch aus der implementierten Unterklassenbeziehung:
# ex:person-123 a conx-agent:Agent .
```

Das Beispiel zeigt die Inferenz aus der implementierten T-Box.

## 13. Aktueller Integrationsstand

Das Agent-Modul ist inzwischen in die implementierten Kernmodule eingebunden:

| Modul | Agent-Bezug | Eigentümer der fachlichen Details |
| --- | --- | --- |
| `core/person` | `conx-person:Person rdfs:subClassOf conx-agent:Agent` | Personennamen, Geburtsdaten, Sex, Gender, Staatsangehörigkeit und Identitätsnachweise |
| `core/organization` | `conx-org:Organization rdfs:subClassOf conx-agent:Agent` | Organisationsklassen, Mitgliedschaft und rechtliche Vertretung |
| `core/contact` | Agenten können `conx-contact:hasContactPoint` verwenden | Kontaktpunkt, Kontaktmethode, Nutzungskontext und Zweck |
| `core/address` | Agenten können `conx-addr:hasAddressAssignment` verwenden | AddressAssignment, Address und AddressRole |

Die zugehörige Übersicht steht im
[Integrationsdiagramm](diagrams/agent-integration-model.md).

## 14. Umgesetzte Abnahmekriterien

1. Definition und Scope von `Agent` sind bestätigt.
2. Die öffentlichen IRIs sind in den Modulmetadaten und der T-Box festgelegt.
3. `rdfs:subClassOf foaf:Agent` ist gegenüber Äquivalenz und reinem Mapping bewertet.
4. Der Importbedarf für FOAF ist technisch geprüft.
5. Es ist bestätigt, dass Version `0.1.0` ohne Agent-Shape den Modulkonventionen entspricht.
6. Das Personenmodell verwendet `conx-agent:Agent` als direkte Oberklasse.
7. Das Organisationsmodell verwendet `conx-agent:Agent` als direkte Oberklasse.
8. Kontakt- und Adresszuordnung bleiben in ihren Fachmodulen und werden nicht in
   den Agent-Kern verschoben.

## 15. Folgeaufgaben

`core/agent`, `core/person`, `core/contact`, `core/address` und
`core/organization` sind als Kernmodule fachlich aufeinander abgestimmt. Für den
Agent-Kern bleibt aktuell kein eigenes Shape erforderlich. Nächste sinnvolle
Arbeiten liegen in der Dokumentations- und Visualisierungsunterstützung: OntoLens
sollte wiederverwendete externe Properties und externe Domain-/Range-Knoten
besser sichtbar machen.
