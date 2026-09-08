# Quellenanalyse für das Participation-Modul

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 27. August 2026  
**Geltungsbereich:** `core/participation`  
**Umsetzungsstand:** Als T-Box, Rollen-Vokabular und Core Shapes 0.1.0 umgesetzt

## 1. Ziel und Methode

Diese Analyse untersucht bestehende Ontologien, Standards und
Ontologie-Entwurfsmuster als fachliche Grundlage des implementierten
Construct-X-Participation-Moduls. Im Mittelpunkt steht die Frage, wie eine
kontextabhängige Beteiligung eines Agenten mit einer bestimmten Rolle
ausgedrückt werden kann.

Untersucht werden insbesondere:

- die Trennung zwischen Agent, Rolle, Rollenzuordnung und Kontext,
- n-stellige Beziehungen in RDF und OWL,
- Rollen von Personen und Organisationen in Vorgängen und an Ressourcen,
- organisationsbezogene Mitgliedschaften,
- Rollen in Aktivitäten und Provenienzbeziehungen,
- zeitliche Gültigkeit,
- kontrollierte Rollenwerte,
- Eignung zur direkten Wiederverwendung oder als Alignment-Ziel,
- Abgrenzung zu den bestehenden Construct-X-Core-Modulen.

Die Analyse verwendet ausschließlich bestehende Core-Festlegungen und externe
Primärquellen. Unfertige Domain-Module werden nicht als Modellgrundlage
herangezogen. Die Analyse selbst ist keine normative Ontologiespezifikation.
Klassen, Property-Namen, Definitionen und öffentliche IRIs sind im
Begriffskatalog und in der T-Box festgelegt.

## 2. Kurzfazit

Keine der untersuchten Ontologien deckt den fachübergreifenden
Construct-X-Anwendungsbereich allein passend ab:

- [W3C ORG](https://www.w3.org/TR/vocab-org/) besitzt ein sehr gutes
  n-stelliges Rollen- und Mitgliedschaftsmuster, ist aber auf Organisationen
  begrenzt.
- [PROV-O](https://www.w3.org/TR/prov-o/) qualifiziert die Verantwortung eines
  Agenten für eine Aktivität oder Entität, trägt jedoch bewusst
  Provenienzsemantik.
- [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) erweitert das qualifizierte
  PROV-Muster für Agentenrollen gegenüber Ressourcen, bleibt aber ein
  Datenkatalogvokabular.
- [ePO 5.2.0](https://docs.ted.europa.eu/EPO/latest/release-notes.html)
  verwendet ein `AgentInRole`-Muster aus Agent, Rolleninstanz und situativem
  Beschaffungskontext. Die einzelnen Rollen werden dort als Klassenhierarchie
  modelliert und sind beschaffungsspezifisch.
- [IFC 4.3](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssignsToActor.htm)
  kennt mit `IfcRelAssignsToActor` eine objektifizierte Zuordnung zwischen
  Akteur, optionaler Rolle und einem oder mehreren Objekten. Das ist für die
  Bauwirtschaft besonders relevant, aber an das IFC-Objektmodell und seine
  Rollen-Enumeration gebunden.

Die stärkste gemeinsame Grundlage ist daher kein einzelnes Importmodell,
sondern die Kombination aus:

1. dem [W3C-Muster für n-stellige Beziehungen](https://www.w3.org/TR/swbp-n-aryRelations/)
   als struktureller Grundlage,
2. W3C ORG, ePO, IFC, PROV-O und DCAT als belegte Anwendungsvarianten,
3. `core/agent` für den beteiligten Agenten,
4. SKOS für getrennt gepflegte, kontrollierte Rollenbegriffe,
5. optional OWL-Time für eine spätere zeitliche Qualifizierung.

Construct-X verwendet für dieses Muster die zentrale Klasse `Participation`.
Sie beschreibt eine tatsächlich geltende oder historisch gegoltene,
qualifizierte Zuordnung von genau einem Agenten zu genau einer Rolle in genau
einem fachlichen Kontext. Optionale
Start- und Enddaten können die Gültigkeit dieser Zuordnung begrenzen. Die
Klasse beschreibt keine Aktivitäts- oder Ereignisteilnahme.

## 3. Bewertete Quellen

| Quelle | Verwendeter Stand | Rolle in der Analyse | Vorläufige Nutzung |
| --- | --- | --- | --- |
| [W3C N-ary Relations](https://www.w3.org/TR/swbp-n-aryRelations/) | Working Group Note, 12. April 2006 | Allgemeines RDF-/OWL-Entwurfsmuster für Beziehungen mit mehr als zwei Argumenten | Primäre strukturelle Grundlage |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 16. Januar 2014 | Mitgliedschaft zwischen Agent, Organisation und Rolle; optionale Zeitangabe | Referenz für Rollenzuordnung und Abgrenzung zur Organisationsmitgliedschaft |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation, 30. April 2013 | Qualifizierte Agentenbeziehungen zu Aktivitäten und Entitäten | Alignment- und Spezialisierungsquelle für Provenienzfälle |
| [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | W3C Recommendation, 22. August 2024 | Rollenqualifizierte Attribution eines Agenten zu einer Ressource | Referenz für ressourcenbezogene Verantwortung |
| [W3C SKOS](https://www.w3.org/TR/skos-reference/) | W3C Recommendation, 18. August 2009 | Kontrollierte, hierarchische Rollenbegriffe | Bevorzugte Grundlage für Rollen-Vokabulare |
| [W3C OWL-Time](https://www.w3.org/TR/owl-time/) | W3C Recommendation von 2017 mit später gepflegtem Entwurfsstand | Zeitpunkte, Intervalle, Dauer und zeitliche Relationen | Kandidat für optionale Zeitqualifizierung |
| [EU eProcurement Ontology](https://docs.ted.europa.eu/EPO/latest/business.html) | ePO 5.2.0, 10. Oktober 2025 | `AgentInRole`, `playedBy` und situativer Beschaffungskontext | Primäre EU-Referenz für kontextuelle Prozessrollen |
| [buildingSMART IFC](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssignsToActor.htm) | IFC 4.3-Dokumentation | Objektifizierte Zuordnung von Akteur und Rolle zu IFC-Objekten | Primäre AEC-Mapping- und Anforderungsquelle |
| [Schema.org Role](https://schema.org/Role) | Schema.org V30.0, abgerufen 2026-08-27 | Allgemeiner Wrapper zur Qualifizierung bestehender Beziehungen | Breite Web-Interoperabilitätsquelle |
| [SPAR PRO](https://sparontologies.github.io/pro/current/pro.html) | Aktuelle publizierte Dokumentation, abgerufen 2026-08-27 | Agent, Rolle, Kontext und Zeit als `RoleInTime` | Referenz für ein explizites rollen- und zeitbezogenes Modell |
| [Participation Schema](https://vocab.org/participation/) | 25. September 2008 | Einfaches Rollenmodell für Personen in Gruppen | Historische Vergleichsquelle, nicht als Kern empfohlen |

Zusätzlich wurden folgende bestehende Construct-X-Festlegungen ausgewertet:

- [Agent-Spezifikation](../../agent/docs/agent-specification.md)
- [Organisations-Quellenanalyse](../../organization/docs/source-analysis.md)
- [Organisations-Konzeptmodell](../../organization/docs/concept-model.md)
- [Organisations-Scope und Kompetenzfragen](../../organization/docs/scope-and-competency-questions.md)

## 4. Fachliche Grundbegriffe

### 4.1 Agent

Ein Agent ist die Entität, die in einem Kontext handelt, Verantwortung trägt
oder als Beteiligter referenziert wird. Construct-X besitzt dafür bereits
`core/agent`. Personen und Organisationen sind dort als konkrete Agententypen
integriert.

Das Participation-Modul sollte keine zweite Person-, Organisations- oder
Actor-Hierarchie einführen. Insbesondere ist ein kontextueller Verkäufer,
Auftragnehmer oder Planer kein neuer Stammdatentyp, sondern ein bereits
existierender Agent in einer bestimmten Rolle.

### 4.2 Rolle

Eine Rolle beschreibt die Funktion, in der ein Agent gegenüber einem Kontext
auftritt. Sie ist von der Identität und vom intrinsischen Typ des Agenten zu
trennen.

Beispiel:

```text
Organisation A
  - ist als Stammdatenobjekt eine Organization
  - tritt in Kontext X als Verkäufer auf
  - tritt in Kontext Y als Empfänger auf
```

W3C ORG und DCAT modellieren Rollen als Unterklassen von `skos:Concept`. Dieser
Ansatz ist für Construct-X besonders geeignet, weil Rollen damit:

- stabile IRIs erhalten,
- mehrsprachig bezeichnet und definiert werden können,
- in Concept Schemes organisiert werden können,
- hierarchisch oder über Mappings verbunden werden können,
- ausserhalb der Participation-T-Box versioniert werden können.

Die Rollenwerte selbst sollten daher nicht als vollständige Liste in die
Participation-T-Box eingebettet werden. Rollen wie Verkäufer, Empfänger,
Planer, Auftragnehmer oder Datenherausgeber gehören in kontrollierte
fachliche Vokabulare beziehungsweise Profile.

### 4.3 Rollenzuordnung

Eine Rollenzuordnung ist die eigenständige Beziehungsressource, die mindestens
Agent, Rolle und Kontext zusammenhaelt. Sie ist nicht identisch mit dem
abstrakten Rollenbegriff.

```text
Rollenzuordnung
  Agent   -> vorhandener Agent
  Rolle   -> kontrollierter Rollenbegriff
  Kontext -> Ressource, für die die Rolle gilt
```

Die Instanz der Rollenzuordnung kann bei Bedarf weitere Angaben tragen, etwa
einen Gültigkeitszeitraum, einen Status, eine Kennung oder einen Nachweis. Das
ist der zentrale Grund für die Objektivierung der Beziehung.

### 4.4 Beteiligung und tatsächliche Ausführung

Der Name `Participation` ist semantisch weiter als eine Rollenzuordnung. In
grundlegenden Participation-Patterns bedeutet Beteiligung häufig, dass ein
Objekt oder Agent tatsächlich an einem Ereignis oder Prozess teilnimmt. Eine
Rollenzuordnung kann dagegen auch eine vorgesehene, vertragliche,
organisatorische oder dokumentierte Funktion ausdrücken, ohne eine bereits
erfolgte Handlung zu behaupten.

Beispiele:

- Die Benennung als Auftragnehmer ist eine kontextuelle Rolle.
- Die Ausführung einer konkreten Arbeit ist eine Aktivitätsbeteiligung.
- Die Zuschreibung als Autor eines Dokuments ist eine Attribution.
- Die Mitgliedschaft in einem Verband ist eine Organisationsbeziehung.

Diese Aussagen dürfen nicht automatisch gleichgesetzt werden. Die spätere
Spezifikation muss deshalb festlegen, ob das Modul nur Rollenzuordnungen oder
auch tatsächliche Ereignisbeteiligungen verantwortet.

## 5. W3C-Muster für n-stellige Beziehungen

RDF-Properties stellen binäre Beziehungen dar. Eine Aussage mit Agent, Rolle
und Kontext benötigt jedoch mindestens drei fachliche Argumente. Sobald
zusätzlich Zeitraum, Status oder Herkunft der Zuordnung benötigt werden,
reicht eine direkte Property wie `hasSeller` nicht aus.

Die W3C Working Group Note empfiehlt für solche Fälle eine eigene Klasse für
die Beziehung und je eine binäre Property für ihre Argumente. Sie grenzt
diesen Ansatz ausdrücklich von RDF-Reifikation ab: Beschrieben wird eine
Beziehungsinstanz, nicht eine RDF-Aussage als `rdf:Statement`.

Für Construct-X folgt daraus als strukturelle Grundlage:

```text
Context --------> Assignment <-------- Agent
                       |
                       v
                      Role
```

Vorteile:

- Agent, Rolle und Kontext bleiben getrennt adressierbar.
- Mehrere Rollen desselben Agenten im selben Kontext sind möglich.
- Derselbe Agent kann in verschiedenen Kontexten unterschiedliche Rollen
  besitzen.
- Zeit, Status, Kennung und Evidenz können an der Beziehung ergänzt werden.
- Domain-Module müssen keine person- oder organisationsspezifischen
  Rollenklassen erzeugen.

Die W3C Note liefert das Muster, aber keine fachlichen Namen, Rollenwerte oder
Construct-X-Kardinalitäten.

## 6. W3C Organization Ontology

### 6.1 Muster

W3C ORG modelliert `org:Membership` als n-stellige Beziehung zwischen:

- genau einem `foaf:Agent` über `org:member`,
- genau einer `org:Organization` über `org:organization`,
- optional einer oder mehreren `org:Role`-Ressourcen über `org:role`,
- optional einem Zeitraum über `org:memberDuring`.

`org:Role` ist eine Unterklasse von `skos:Concept`. ORG trennt den abstrakten
Rollenwert von der konkreten Mitgliedschaftsinstanz. Aus der vollständigen
Beziehung kann eine direkte `org:memberOf`-Aussage abgeleitet werden.

### 6.2 Stärken

- etabliertes und normativ publiziertes n-stelliges Muster,
- klare Trennung zwischen Agent, Rolle und Beziehungsinstanz,
- Unterstützung kontrollierter Rollentaxonomien mit SKOS,
- optionale Zeitqualifizierung,
- direkte Kurzbeziehung kann abgeleitet werden, ohne zweite Datenwahrheit zu
  verlangen.

### 6.3 Grenzen

`org:Membership` setzt als Kontext zwingend eine Organisation voraus. Es passt
nicht unmittelbar für Dokumente, Verträge, Lieferungen, Projekte, Produkte,
Aktivitäten oder beliebige andere fachliche Ressourcen.

Construct-X besitzt ausserdem bereits eine `Membership` im
Organisationsmodul. Diese beschreibt organisationsbezogene Zugehörigkeit und
darf nicht stillschweigend durch eine allgemeinere Prozessrollenzuordnung
umdefiniert werden.

### 6.4 Bewertung

W3C ORG ist die stärkste Quelle für die interne Struktur und für die
Abgrenzung von Rollenwert und Rolleninstanz. Es ist kein geeigneter direkter
Oberbegriff für alle Participation-Fälle. Eine spätere Ausrichtung der
Construct-X-`Membership` zu einem allgemeinen Participation-Muster ist
denkbar, muss aber getrennt entschieden und auf Inferenzfolgen geprüft werden.

## 7. PROV-O und DCAT

### 7.1 PROV-O `Association`

PROV-O beschreibt mit `prov:Association` die Zuweisung von Verantwortung eines
Agenten für eine Aktivität. Das qualifizierte Muster lautet:

```text
prov:Activity
  -> prov:qualifiedAssociation
       -> prov:Association
            prov:agent   -> prov:Agent
            prov:hadRole -> prov:Role
            prov:hadPlan -> prov:Plan (optional)
```

Das ist strukturell sehr nah am implementierten Participation-Muster. Semantisch ist
es jedoch auf eine Aktivität und auf Provenienz beziehungsweise Einfluss und
Verantwortung bezogen.

### 7.2 PROV-O `Attribution`

`prov:Attribution` schreibt eine `prov:Entity` einem Agenten zu. Die Beziehung
ist insbesondere sinnvoll, wenn eine erzeugende Aktivität unbekannt oder
irrelevant ist. Sie eignet sich für Autorenschaft, Urheberschaft oder andere
provenienzbezogene Verantwortungszuschreibungen.

Auch diese Semantik ist enger als eine beliebige Geschäfts- oder Projektrolle.
Ein Verkäufer, Empfänger oder Ansprechpartner ist nicht allein deshalb eine
Provenienz-Attribution.

### 7.3 DCAT `qualifiedAttribution`

DCAT 3 verwendet `prov:qualifiedAttribution` und `prov:Attribution`, ergänzt
aber `dcat:hadRole`, weil `prov:hadRole` auf Rollen gegenüber Aktivitäten
ausgerichtet ist. DCAT definiert `dcat:Role` als `skos:Concept` und empfiehlt
kontrollierte Rollenwerte.

DCAT bestätigt damit zwei wichtige Punkte:

1. Das qualifizierte Beziehungsmuster ist auch für Agentenrollen gegenüber
   Ressourcen sinnvoll.
2. Eine bestehende qualifizierte Beziehung sollte nicht wiederverwendet werden,
   wenn ihre fachliche Semantik und ihre Domain-/Range-Axiome nicht passen.

### 7.4 Bewertung

PROV-O und DCAT sind wertvolle Alignment- und Spezialisierungsziele:

- Aktivitätsbezogene Participation kann später zu `prov:Association`
  ausgerichtet werden.
- Ressourcenbezogene Urheberschaft oder Verantwortung kann zu
  `prov:Attribution` beziehungsweise dem DCAT-Muster ausgerichtet werden.

Eine generische Construct-X-Rollenzuordnung sollte aber nicht pauschal als
PROV-Einfluss oder Attribution typisiert werden. Sonst würden fachlich
unbeabsichtigte Provenienzaussagen entstehen.

## 8. EU eProcurement Ontology

### 8.1 Muster

ePO 5.2.0 definiert `epo:AgentInRole` als relatives Konzept, das einen Agenten
mit seiner Funktion in einem situativen Kontext verbindet. Die Kernbeziehungen
sind:

- `epo:playedBy` zu genau einem `foaf:Agent`,
- `epo:contextualisedBy` zu einem Beschaffungsobjekt beziehungsweise
  Procurement Element.

Rollen wie `AcquiringParty`, `OfferingParty`, `Buyer`, `Contractor` oder
`Winner` werden als Klassen in einer Spezialisierungshierarchie von
`epo:AgentInRole` modelliert. Die Rolleninstanz trägt damit ihren Rollentyp
über `rdf:type`.

### 8.2 Stärken

- klare Trennung von Agentenstammdaten und situativer Funktion,
- derselbe Agent kann mehrere Rollen besitzen,
- der Kontext ist ein expliziter Bestandteil der Rollenaussage,
- in europäischen Beschaffungsprozessen praktisch erprobt,
- direkte fachliche Nähe zu Geschäftsrollen wie Buyer, Contractor und
  Offering Party.

### 8.3 Grenzen

- Rollen werden als OWL-Klassen statt als Werte aus einem kontrollierten
  Rollen-Vokabular modelliert.
- Die Klassenhierarchie ist auf öffentliche Beschaffung zugeschnitten.
- Der Kontext ist an ePO Procurement Elements gebunden.
- Eine direkte Übernahme würde ePO-Semantik und Abhängigkeiten in den
  Construct-X-Core ziehen.

### 8.4 Bewertung

ePO ist die wichtigste Referenz für die fachliche Idee "Agent in Rolle im
Kontext". Das Strukturprinzip sollte übernommen werden. Die konkrete
Beschaffungshierarchie und das Modellieren jeder Rolle als Klasse sollten nicht
unbesehen in einen fachübergreifenden Construct-X-Core übernommen werden.

## 9. buildingSMART IFC

### 9.1 `IfcRelAssignsToActor`

IFC verwendet eine objektifizierte Beziehung, um genau einen `IfcActor` einem
oder mehreren `IfcObjectDefinition`-Objekten zuzuordnen. `ActingRole` kann die
Rolle des Akteurs innerhalb genau dieser Zuordnung angeben. Die IFC-Dokumentation
nennt insbesondere Verantwortung für Controls, Groups, Products, Processes
und Resources.

Damit deckt IFC strukturell folgende Elemente ab:

```text
IfcRelAssignsToActor
  RelatingActor  -> genau ein IfcActor
  ActingRole     -> optional eine IfcActorRole
  RelatedObjects -> mindestens ein IfcObjectDefinition
```

### 9.2 `IfcActorRole`

`IfcActorRole` beschreibt eine Rolle, die von einer Person, Organisation oder
Person-in-Organisation ausgeführt wird. `IfcRoleEnum` enthält unter anderem
Architect, Client, Contractor, Engineer, Manufacturer, Project Manager,
Subcontractor und Supplier. Die IFC-Dokumentation stellt selbst klar, dass eine
solche Liste nie vollständig sein kann, und sieht deshalb `USERDEFINED` plus
Freitext vor.

### 9.3 Stärken

- etablierte AEC-Quelle mit hoher Relevanz für Construct-X,
- objektifizierte, referenzierbare Zuordnung,
- Rolle gilt ausdrücklich innerhalb der jeweiligen Objektzuordnung,
- ein Akteur kann gegenüber verschiedenen Objekten unterschiedliche Rollen
  spielen,
- vorhandene IFC-Rollen liefern spätere Mappingkandidaten.

### 9.4 Grenzen

- `IfcActor` und `IfcObjectDefinition` sind Bestandteile des IFC-Schemas und
  nicht der allgemeine Construct-X-Agenten- beziehungsweise Kontextbegriff.
- Eine Beziehung kann mehrere Related Objects bündeln. Dadurch ist nicht ohne
  Zusatzregeln klar, ob Metadaten der Zuordnung für jedes Objekt identisch
  gelten.
- `ActingRole` ist optional.
- `IfcRoleEnum` ist eine geschlossene Enumeration mit `USERDEFINED`-Ausweg und
  deshalb keine ausreichende Grundlage für ein erweiterbares Linked-Data-
  Rollen-Vokabular.
- Zeitliche Gültigkeit ist nicht Bestandteil dieses Kernmusters.

### 9.5 Bewertung

IFC ist eine primäre Mapping- und Anforderungsquelle, aber kein geeigneter
direkter Import für das Core-Modul. Für eine robuste Abbildung muss später
entschieden werden, ob eine IFC-Zuordnung zu mehreren Objekten als eine
Participation-Instanz oder als mehrere einzelne Kontextzuordnungen abgebildet
wird.

## 10. Weitere Vergleichsmodelle

### 10.1 Schema.org `Role`

Schema.org verwendet `Role` als Wrapper, um eine bestehende Property-Beziehung
um `roleName`, `startDate`, `endDate` oder weitere Angaben zu ergänzen. Der
Wrapper wird über dieselbe fachliche Property eingebunden, beispielsweise
`member`, `actor` oder `alumniOf`.

Das Muster ist für Web-Markup flexibel und weit verbreitet. Für einen
qualitätsgesicherten Core ist es jedoch zu offen:

- `roleName` erlaubt Text oder URL statt eines klaren kontrollierten Konzepts,
- die Semantik hängt von der jeweils umschliessenden Property ab,
- es gibt keine einheitlichen Properties für Agent und Kontext,
- die gleiche Information kann je nach Property unterschiedlich strukturiert
  werden.

Schema.org ist daher ein Alignment- und Mappingziel, nicht die bevorzugte
Kernstruktur.

### 10.2 SPAR PRO `RoleInTime`

Die Publishing Roles Ontology modelliert eine `RoleInTime`-Situation mit:

- genau einem haltenden Agenten,
- einem Rollenwert,
- mindestens einer kontextgebenden Entität,
- optional einem Zeitintervall.

Obwohl PRO auf Publikationsrollen ausgerichtet ist, ist dieses Muster dem
umgesetzten Construct-X-Bedarf sehr nahe. Besonders wertvoll sind die explizite
Trennung von `Role` und `RoleInTime` sowie der generische Kontextbezug.

Gegen eine direkte Wiederverwendung sprechen die Bindung an die SPAR-
Ontologiefamilie, mehrere importierte Ontology Design Patterns und die
publikationsspezifische Gesamtsemantik. PRO ist eine starke Entwurfsreferenz
und ein mögliches Alignmentziel für Dokumentrollen.

### 10.3 Participation Schema

Das Participation Schema von 2008 beschreibt Rollen, die Personen in Gruppen
einnehmen, einschliesslich Holder sowie Start- und Enddatum. Es ist einfach,
aber auf Gruppen begrenzt, verwendet globale Domain-/Range-Festlegungen und
besitzt seit 2008 keinen dokumentierten neueren Stand.

Es wird deshalb nur als historische Vergleichsquelle betrachtet. W3C ORG und
die neueren qualifizierten Muster sind fachlich und governance-seitig
belastbarer.

## 11. Mustervergleich

| Modell | Beziehungsressource | Agent | Rolle | Kontext | Zeit | Hauptgrenze |
| --- | --- | --- | --- | --- | --- | --- |
| W3C ORG Membership | Ja | genau ein Agent | optional, SKOS-basierter Rollenwert | genau eine Organisation | optionales Intervall | nur Organisationsmitgliedschaft |
| PROV Association | Ja | Agent | `prov:Role` | Aktivität | über qualifizierte PROV-Strukturen erweiterbar | behauptet Aktivitätsverantwortung/Provenienz |
| PROV/DCAT Attribution | Ja | Agent | `dcat:Role` als SKOS Concept | PROV Entity / DCAT Resource | am Beziehungsknoten erweiterbar | Attribution statt beliebiger Beteiligung |
| ePO AgentInRole | Ja | genau ein Agent | Rollenklasse als Typ der Instanz | Procurement Element | nicht Kern des Musters | beschaffungsspezifische Klassenhierarchie |
| IFC RelAssignsToActor | Ja | genau ein IfcActor | optional eine IfcActorRole | ein oder mehrere IFC-Objekte | nicht Kern des Musters | IFC-Schema und Enumeration |
| Schema.org Role | Ja, als Wrapper | property-abhängig | Text oder URL | property-abhängig | Start-/Enddatum | zu offen und strukturell uneinheitlich |
| SPAR PRO RoleInTime | Ja | genau ein Agent | Rollenindividuum | mindestens eine Entität | optionales Intervall | Publikationsscope und Importtiefe |

## 12. Bestätigte Architekturfolgerungen

Die folgenden Punkte sind durch die Quellen belegt und für den MVP fachlich
bestätigt. Die konkreten lokalen Properties und IRIs werden erst im
Begriffskatalog festgelegt.

### 12.1 Lokale Beziehungsressource

Ein lokales qualifiziertes Beziehungsmuster ist fachlich besser geeignet als
direkte Properties wie `hasSeller`, `hasBuyer`, `hasPlanner` oder
`hasContractor`. Rollenspezifische Kurzbeziehungen werden nicht Bestandteil des
Core-Moduls. Die Rollen bleiben als Individuen referenzierbare Werte der
`Participation`.

Eine lokale Ressource verhindert zugleich, dass Construct-X alle
Rollenzuordnungen als Organisationsmitgliedschaft, Provenienz-Attribution,
Aktivitätsassoziation oder IFC-Zuordnung behauptet.

### 12.2 Wiederverwendung von `core/agent`

Der beteiligte Akteur sollte auf `conx-agent:Agent` verweisen. Das erlaubt
Personen und Organisationen, ohne ihre Stammdaten oder Typen im
Participation-Modul zu duplizieren.

Ob spätere weitere Agenttypen zugelassen werden, bleibt der offenen
Agent-Hierarchie überlassen. Das Participation-Modul sollte keine geschlossene
Union aus Person und Organisation definieren.

### 12.3 Getrennte Rollen-Vokabulare

Die T-Box erhält eine lokale Klasse `Role` als Unterklasse von `skos:Concept`.
Konkrete Rollen werden als Individuen modelliert. Construct-X-gepflegte
Rollen-Vokabulare sollen als separat versionierte SKOS Concept Schemes
bereitgestellt werden. Die T-Box erzwingt jedoch nicht, dass jeder externe
Rollenwert zwingend in einem Concept Scheme steht.

Zum MVP gehört ein minimales Construct-X-Rollen-Vokabular, das die Verwendung
des Participation-Musters mit konkreten Rollen zeigt. Der fachlich stimmige
Startumfang wird im Begriffskatalog festgelegt und nicht aus der T-Box
abgeleitet.

### 12.4 Kontext bleibt extern

Der fachliche Kontext gehört nicht dem Participation-Modul. Er kann später
beispielsweise ein Dokument, Vertrag, Projekt, Prozess, Produkt, Asset oder eine
andere fachliche Ressource sein.

Eine globale OWL-Domain für die Kontextseite wäre deshalb problematisch. Die
T-Box sollte keinen allgemeinen lokalen `Context`-Sammeltyp allein für diese
Property einführen, solange dafür keine eigenständige Semantik vorliegt.

### 12.5 Eine Zuordnung pro Agent, Rolle und Kontext

ORG, PRO, ePO und IFC bestätigen das gewählte n-stellige Muster. Für den
Construct-X-Kern gilt:

- genau einen zugeordneten Agenten,
- genau einen Rollenwert,
- genau einen fachlichen Kontext.

Unqualifizierte Beteiligungen ohne Rolle sind nicht zulässig. Benötigt ein
Agent mehrere Rollen oder gelten Rollen für mehrere Kontexte, wird für jede
Kombination eine eigene `Participation` verwendet. Pro Kombination aus Agent,
Rolle und Kontext existiert fachlich genau eine `Participation`.

### 12.6 Zeitliche Gültigkeit

Eine `Participation` kann optional ein Startdatum und ein Enddatum besitzen.
Beide Werte begrenzen ausschließlich die zeitliche Gültigkeit der
Rollenzuordnung. Sie beschreiben weder Dauer noch Beginn oder Ende einer
Aktivität.

Der MVP verwendet einfache Datumswerte statt eines eigenen Intervallobjekts.
Ein allgemeines Zeitmodell oder OWL-Time wird nicht in das Participation-Modul
gezogen. Das Core-SHACL-Profil erlaubt höchstens einen Wert pro Datum und
prüft bei gemeinsamem Auftreten eine widerspruchsfreie Reihenfolge.

### 12.7 Keine Gleichsetzung mit Berechtigung oder Verantwortung

Ein Rollenwert kann eine Funktion bezeichnen, behauptet aber nicht automatisch:

- eine technische Zugriffsberechtigung,
- eine rechtswirksame Vollmacht,
- eine vertragliche Pflicht,
- die Ausführung einer Aktivität,
- Urheberschaft oder Provenienz,
- Haftung oder abschliessende Verantwortlichkeit.

Solche Bedeutungen benötigen andere fachliche Modelle. Herkunft, Nachweis,
Status, Berechtigungs- und Provenienzangaben werden im Participation-Modul auch
nicht als spätere Erweiterung vorgemerkt.

## 13. Abgrenzung zu bestehenden Core-Modulen

| Modul | Verbleibende Zuständigkeit | Bezug zu Participation |
| --- | --- | --- |
| `core/agent` | Gemeinsame Oberklasse für beteiligte Personen und Organisationen | Participation referenziert den Agenten |
| `core/person` | Personenstammdaten | Eine Person kann Agent einer Rollenzuordnung sein |
| `core/organization` | Organisationen, Mitgliedschaft, Hierarchie und rechtliche Vertretung | Eine Organisation kann Agent oder organisationsbezogener Kontext sein; Membership bleibt zunächst eigenes Organisationskonzept |
| `core/contact` | Kontaktpunkte, Methoden, Nutzung und Zweck | Kontaktrolle und Geschäftsrolle dürfen nicht vermischt werden |
| `core/address` | Adressen und Adresszuordnungen | Keine Rollen- oder Kontextsemantik im Participation-Modul ableiten |
| `core/document` | Dokumente und Dokumentsemantik | Ein Dokument kann Kontext einer Rollenzuordnung sein |

Besonders kritisch ist die Grenze zur `core/organization:Membership`:

- Membership bedeutet Zugehörigkeit zu einer Organisation.
- Eine allgemeine Rollenzuordnung bedeutet eine Funktion gegenüber einem
  Kontext.
- Eine Mitgliedschaft kann eine Rolle und einen Zeitraum besitzen, bleibt aber
  fachlich eine Mitgliedschaft.

`Membership` und `Participation` bleiben im MVP unabhängige Konzepte. Eine
Mitgliedschaft benötigt im bestehenden Organisationsmodell keinen Rollenwert
und kann deshalb nicht ohne Bedeutungs- und Kardinalitätsänderung als
Spezialisierung von `Participation` behandelt werden.

## 14. Bestätigter MVP-Korridor

### Im Participation-Kern

- die lokale Klasse `Participation` für eine tatsächliche kontextuelle
  Rollenzuordnung,
- Referenz auf genau einen `core/agent:Agent`,
- Referenz auf genau einen Rollenwert der lokalen Klasse `Role`,
- Referenz auf genau einen fachlichen Kontext,
- fachliche Eindeutigkeit der Kombination aus Agent, Rolle und Kontext,
- optionale einfache Start- und Enddaten für die Gültigkeit der Zuordnung,
- neutrale Integrationsproperties von Agent und Kontext zur Zuordnung,
- ein minimales, separat gepflegtes Rollen-Vokabular mit Rollenindividuen,
- Metadaten und Definitionen des Moduls.

### Ausserhalb des Participation-Kerns

- konkrete Rollenlisten für Lieferung, Beschaffung, Projekt, Bau oder
  Dokumente,
- Person-, Organisations- und Kontaktdaten,
- Organisationsmitgliedschaft und Stellenpläne,
- rechtliche Vertretung, Vollmacht und Zeichnungsberechtigung,
- technische Rollen- und Berechtigungsverwaltung,
- RACI-Matrizen und detaillierte Verantwortungsmodelle,
- Aktivitäts-, Prozess- oder Ereignisontologie,
- Provenienzmodellierung,
- Herkunft, Nachweis und Status der Rollenzuordnung,
- Vertrags- und Projektmodellierung,
- eigene Zeitontologie,
- rollenspezifische direkte Kurzbeziehungen,
- externe Alignment-Axiome,
- IFC-spezifische Klassen oder Enumerationen.

## 15. Bestätigte Modellentscheidungen

| Thema | Entscheidung für den MVP |
| --- | --- |
| Bedeutung | Ausschließlich kontextuelle Rollenzuordnung; keine Teilnahme an Aktivitäten oder Ereignissen |
| Zentrale Klasse | `Participation` mit deutscher Bezeichnung Beteiligung |
| Aussage | Die Instanz behauptet eine tatsächlich geltende oder historisch gegoltene Zuordnung, keine Planung oder Möglichkeit |
| Agent | Genau ein `core/agent:Agent` pro Participation |
| Qualifizierung | Genau ein Rollenwert; keine unqualifizierte Participation |
| Kontext | Genau eine fachliche Kontextressource; der Kontexttyp bleibt offen |
| Eindeutigkeit | Pro Kombination aus Agent, Rolle und Kontext fachlich genau eine Participation |
| Rollenklasse | Lokale `Role` als Unterklasse von `skos:Concept` |
| Concept Scheme | Keine globale Pflicht für jeden Rollenwert; Construct-X-Vokabulare werden als Concept Schemes gepflegt |
| Rollenform | Rollen sind Individuen, keine Rollenklassen |
| Startvokabular | Separates MVP-Artefakt mit `ClientRole`, `ContractorRole`, `SupplierRole`, `ArchitectRole` und `EngineerRole`; weitere Rollen folgen aus den jeweiligen Fachmodulen |
| Zeit | Optionales Start- und Enddatum der Gültigkeit |
| Membership | Bleibt getrennt von Participation |
| Alignments | Keine externen Gleichsetzungen oder Alignment-Axiome im MVP |
| Kurzbeziehungen | Keine rollenspezifischen direkten Properties oder Ableitungen im Core |
| Herkunft/Nachweis/Status | Nicht Bestandteil und nicht als Ausbau des Participation-Moduls vorgesehen |

## 16. Umsetzungsstand und weitere Verwendung

Die Recherche stützt ein eigenständiges Core-Modul, weil die
kontextabhängige Agentenrolle weder in `core/agent` noch in Person,
Organisation, Dokument oder einem einzelnen Domain-Modul fachlich neutral
aufgehoben ist.

Scope, Begriffskatalog, Konzeptmodell, Modulgrenzen und SHACL-Anforderungen
bilden die freigegebene fachliche Grundlage der Version `0.1.0`. T-Box,
minimales Rollen-Vokabular, Core-SHACL-Profil sowie positive und negative
Testfälle sind umgesetzt. Weitere Rollen werden nicht vorsorglich in den Core
aufgenommen, sondern aus den Kompetenzfragen des jeweils zuständigen
Fachmoduls abgeleitet.

Die belastbarste Ausgangsthese für diese Diskussion lautet:

> Das Participation-Modul beschreibt eine eigenständige, qualifizierte
> Beziehung, in der genau ein vorhandener Agent genau eine kontrolliert
> bezeichnete Rolle gegenüber genau einem fachlichen Kontext einnimmt. Sie
> kann optionale Start- und Enddaten ihrer Gültigkeit tragen. Das Modul
> beschreibt weder die Stammdaten des Agenten noch den Kontext selbst und
> behauptet ohne weitere
> Spezialisierung keine Provenienz, Vollmacht, Berechtigung oder tatsächliche
> Aktivitätsausführung.

## 17. Verständliches Übertragungsbeispiel

> W3C ORG liefert ein bewährtes Muster für qualifizierte Beziehungen.
> Construct-X verallgemeinert dieses Muster auf beliebige fachliche Kontexte,
> ohne jede Participation automatisch zu einer Organisationsmitgliedschaft zu
> machen.
