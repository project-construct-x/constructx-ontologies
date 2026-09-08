# Scope und Kompetenzfragen des Participation-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`  

## 1. Zweck

Das Participation-Modul beschreibt eine tatsächlich geltende oder historisch
gegoltene, kontextbezogene Rollenzuordnung eines Agenten. Es beantwortet,
welcher Agent in welchem fachlichen Kontext welche Rolle besitzt oder besass.

Das Modul beschreibt keine Aktivitäten oder Ereignisse und behauptet nicht,
dass der Agent eine bestimmte Handlung ausgeführt hat. Stammdaten des Agenten
und die Semantik des Kontexts verbleiben in ihren zuständigen Modulen.

## 2. Bestätigter Scope

| Bereich | Entscheidung für den MVP |
| --- | --- |
| Zentrale Klasse | `Participation` mit deutscher Bezeichnung Beteiligung |
| Bedeutung | Tatsächlich geltende oder historisch gegoltene, qualifizierte Rollenzuordnung; keine Planung, Möglichkeit oder Aktivitätsteilnahme |
| Agent | Genau ein `core/agent:Agent` pro Participation |
| Rolle | Genau ein Wert der lokalen Klasse `Role`; keine unqualifizierte Participation |
| Kontext | Genau eine fachliche Ressource; kein lokaler Sammeltyp für Kontexte |
| Eindeutigkeit | Pro Kombination aus Agent, Rolle und Kontext fachlich genau eine Participation |
| Zeit | Start- und Enddatum optional; beide beschreiben nur die Gültigkeit der Zuordnung |
| Rollenklasse | Lokale `Role` als Unterklasse von `skos:Concept` |
| Rollenwerte | Ausschließlich Individuen, keine Rollenklassen |
| Concept Schemes | Keine globale Pflicht; Construct-X-gepflegte Rollen-Vokabulare verwenden SKOS Concept Schemes |
| Startvokabular | Ein minimales, separat gepflegtes Rollen-Vokabular gehört zum MVP |
| Membership | Bleibt ein eigenständiges Konzept von `core/organization` |
| Alignments | Keine externen Gleichsetzungen oder Alignment-Axiome im MVP |
| Kurzbeziehungen | Keine rollenspezifischen direkten Properties im Core |
| Herkunft, Nachweis und Status | Nicht Bestandteil des Moduls und nicht als späterer Participation-Ausbau vorgesehen |

## 3. Fachliches Zielbild

Die nachfolgende Darstellung verwendet die im Begriffskatalog festgelegten
Property-Namen und ihre öffentlichen IRIs.

```text
Participation
  participant -> genau ein Agent
  role        -> genau eine Role
  context     -> genau eine fachliche Ressource
  startDate   -> optional höchstens ein Datum
  endDate     -> optional höchstens ein Datum
```

Eine `Participation` ist immer qualifiziert. Eine Aussage der Form "Agent A ist
irgendwie an Kontext X beteiligt" reicht für eine gültige Participation nicht
aus.

## 4. Modellgrundsätze

### 4.1 Agent, Rolle und Kontext bleiben getrennt

Der Agent bleibt dieselbe Person oder Organisation, unabhängig von seinen
Rollen. Die Rolle wird nicht als Unterklasse des Agenten modelliert.

```text
Organisation A
  Participation 1 -> Rolle Auftragnehmer -> Projekt X
  Participation 2 -> Rolle Lieferant      -> Vertrag Y
```

Organisation A wird dadurch weder zu einer Klasse `ContractorOrganization`
noch zu einer zweiten Organisationsinstanz.

### 4.2 Eine Participation bildet genau eine Kombination ab

Eine Instanz verbindet genau einen Agenten, genau eine Rolle und genau einen
Kontext. Mehrere Agenten, Rollen oder Kontexte werden nicht in einer einzigen
Participation gebündelt.

```text
Participation 1 = Agent A + Auftragnehmer + Projekt X
Participation 2 = Agent B + Auftragnehmer + Projekt X
Participation 3 = Agent A + Lieferant      + Projekt X
```

Dieses Muster vermeidet Mehrdeutigkeit und erlaubt, jede Zuordnung einzeln zu
referenzieren und zu validieren.

### 4.3 Rollen sind Individuen

Die lokale Klasse `Role` ordnet alle für Participation geeigneten Rollenwerte
ein:

```text
Role
  rdfs:subClassOf skos:Concept

role:example-role
  rdf:type Role
```

Konkrete Rollenwerte werden als Individuen in getrennten Vokabularen gepflegt.
Rollenklassen nach dem ePO-Muster werden nicht Teil des lokalen Core-Modells.

### 4.4 Der Kontext bleibt fachlich offen

Ein Kontext kann beispielsweise ein Vertrag, Dokument, Projekt,
Lieferschein, Produkt oder eine andere fachliche Ressource sein. Diese
Ressourcen besitzen derzeit keine gemeinsame notwendige Core-Oberklasse.

Das Participation-Modul führt deshalb keine Klasse `Context` oder
`ParticipationContext` ein. Das jeweilige Fachprofil kann einschränken, welche
Kontexttypen es zulässt.

### 4.5 Zeitangaben beschreiben Gültigkeit

Start- und Enddatum sind optional. Wenn sie vorhanden sind, geben sie an, ab
wann beziehungsweise bis wann die Rollenzuordnung gilt.

```text
Person A + Projektleiter + Projekt X
  startDate = 2026-01-01
  endDate   = 2026-06-30
```

Die Daten beschreiben nicht die Dauer einer Aktivität. Eine Participation kann
nur ein Start- und ein Enddatum besitzen. Wenn beide vorhanden sind, darf das
Enddatum nicht vor dem Startdatum liegen.

## 5. Kompetenzfragen

### PCQ-01: Welcher Agent besitzt in einem Kontext welche Rolle?

Eine `Participation` verbindet genau einen vorhandenen Agenten mit genau einer
Rolle und genau einem Kontext.

Konzeptionelles Beispiel:

```text
Participation P1
  participant = Organisation A
  role        = Auftragnehmer
  context     = Projekt X
```

Die Participation behauptet, dass diese Zuordnung tatsächlich gilt oder in
dem angegebenen Zeitraum gegolten hat.

### PCQ-02: Kann eine Person oder Organisation mehrere Rollen im selben Kontext besitzen?

Ja. Für jede Rolle wird eine eigene Participation verwendet.

```text
P1 = Organisation A + Auftragnehmer + Projekt X
P2 = Organisation A + Lieferant      + Projekt X
```

Dadurch bleibt eindeutig, welche weiteren Angaben zu welcher Rolle gehören.

### PCQ-03: Können mehrere Agenten dieselbe Rolle im selben Kontext besitzen?

Ja. Jeder Agent erhält eine eigene Participation.

```text
P1 = Organisation A + Planer + Projekt X
P2 = Organisation B + Planer + Projekt X
```

Eine gemeinsam handelnde, selbst als Organisation modellierte
Arbeitsgemeinschaft kann alternativ als ein Agent referenziert werden.

### PCQ-04: Sind Beteiligungen ohne bekannte Rolle erlaubt?

Nein. Das Modul beschreibt ausschließlich qualifizierte Beteiligungen. Eine
Participation ohne Rolle beantwortet nicht, in welcher Funktion der Agent im
Kontext steht, und ist im Core-Profil ungültig.

Ein allgemeiner Ersatzwert wie `unknown` oder `unspecified` ist für den MVP
nicht vorgesehen. Liegt kein Rollenwert vor, wird keine Participation erzeugt.

### PCQ-05: Kann eine Participation mehrere Kontexte bündeln?

Nein. Gelten Agent und Rolle für mehrere Kontexte, wird je Kontext eine eigene
Participation verwendet.

```text
P1 = Organisation A + Auftragnehmer + Vertrag X
P2 = Organisation A + Auftragnehmer + Vertrag Y
```

Damit entstehen keine mehrdeutigen Kombinationen aus mehreren Rollen und
Kontexten.

### PCQ-06: Kann dieselbe Kombination mehrfach vorkommen?

Pro Kombination aus Agent, Rolle und Kontext existiert fachlich genau eine
Participation.

```text
Agent A + Auftragnehmer + Projekt X = genau eine Participation
```

Optionale Start- und Enddaten gehören zu dieser Zuordnung. Mehrere getrennte
Gültigkeitsabschnitte derselben Kombination sind im MVP nicht vorgesehen. Ein
späterer Bedarf an unterbrochenen oder wiederkehrenden Zuordnungen würde eine
neue fachliche Entscheidung erfordern.

### PCQ-07: Wie wird die zeitliche Gültigkeit beschrieben?

Eine Participation darf optional ein Startdatum, ein Enddatum oder beide
besitzen:

- nur Startdatum: Die Zuordnung gilt ab diesem Datum, ein Ende ist nicht
  angegeben.
- nur Enddatum: Die Zuordnung galt bis zu diesem Datum, ein Beginn ist nicht
  angegeben.
- Start- und Enddatum: Die Zuordnung gilt innerhalb des angegebenen
  Zeitraums.
- kein Datum: Die Zuordnung besteht, ohne dass ihre zeitlichen Grenzen
  ausgedrückt werden.

Die konkreten Property-Namen und der Datentyp sind im Begriffskatalog
festgelegt. Der MVP verwendet ein einfaches vollständiges Kalenderdatum als
`xsd:date`.

### PCQ-08: Wie werden Rollen definiert und gepflegt?

`Role` ist eine lokale Unterklasse von `skos:Concept`. Konkrete Rollen sind
Individuen. Construct-X-gepflegte Rollenlisten werden als versionierte SKOS
Concept Schemes ausserhalb der Participation-T-Box bereitgestellt.

Die T-Box erzwingt keine Scheme-Zugehörigkeit für jeden Rollenwert. Damit
können auch externe, ausdrücklich als lokale `Role` eingeordnete Werte in
Fachprofilen verwendet werden.

### PCQ-09: Welches Rollen-Vokabular gehört zum MVP?

Zum MVP gehört ein kleines, separat versioniertes Rollen-Vokabular. Es soll
mehrere konkrete Rollen enthalten, damit Datenbeispiele, Shapes und Abfragen
das Participation-Muster realistisch zeigen können.

Die konkreten Startrollen werden im Begriffskatalog festgelegt. Das
Participation-Modul selbst definiert keine universelle Rollenliste und mischt
nicht ungeprüft Bau-, Vertrags-, Liefer- und Dokumentrollen in seiner T-Box.

`AddressRole` ist ein vergleichbares Muster für kontrollierte Rollenwerte,
aber kein Participation-Rollen-Vokabular: Es klassifiziert die Funktion einer
Adresse innerhalb einer Adresszuordnung und nicht die Rolle eines Agenten.

### PCQ-10: Ist eine Organisationsmitgliedschaft eine Participation?

Im MVP nicht. `core/organization:Membership` beschreibt die Zugehörigkeit
eines Agenten zu einer Organisation und benötigt aktuell keinen Rollenwert.
Eine `Participation` verlangt dagegen immer genau eine Rolle.

Beide Konzepte bleiben deshalb unabhängig. Das Participation-Modul verändert
die bestehende Membership nicht.

### PCQ-11: Behauptet eine Participation die Ausführung einer Aktivität?

Nein. Die Rolle `Auftragnehmer` in einem Projekt behauptet beispielsweise
nicht, dass eine bestimmte Bauleistung bereits ausgeführt wurde.

Aktivitäten, Ereignisse und ihre tatsächlichen Teilnehmer werden später in
einer anderen Ontologie beschrieben.

### PCQ-12: Werden rollenspezifische Kurzbeziehungen erzeugt?

Nein. Aus:

```text
Organisation A + Verkäufer + Vertrag X
```

wird im Core keine zusätzliche Property-Aussage wie
`Organisation A isSellerOf Vertrag X` erzeugt. Die Rolle bleibt ein Individuum
an der Participation und die qualifizierte Beziehung ist die einzige
massgebliche Darstellung.

### PCQ-13: Wie werden Herkunft, Nachweis oder Status beschrieben?

Gar nicht im Participation-Modul. Eine vorhandene Participation behauptet eine
tatsächlich geltende oder historisch gegoltene Zuordnung. Statuswerte wie
geplant, vorgeschlagen oder widerrufen passen nicht zu dieser Bedeutung.

Provenienz, Nachweise, Berechtigungen und Vollmachten sind eigenständige
fachliche Themen und werden nicht als späterer Ausbau dieses Moduls
vorgemerkt.

## 6. Ausdrücklich ausserhalb des Participation-Kerns

- Aktivitäten, Ereignisse und Prozessabläufe,
- tatsächliche Ausführung einzelner Handlungen,
- geplante, vorgeschlagene oder mögliche Rollenzuordnungen,
- unqualifizierte Beteiligungen ohne Rolle,
- Person-, Organisations-, Kontakt- und Adressstammdaten,
- Organisationsmitgliedschaften, Stellen und Beschäftigungsmodelle,
- rechtliche Vertretung, Vollmacht und Zeichnungsberechtigung,
- technische Rollen, Benutzerkonten und Zugriffsberechtigungen,
- RACI-Matrizen und detaillierte Verantwortungsmodelle,
- Herkunft, Nachweis, Status und Provenienz einer Rollenzuordnung,
- Vertrags-, Projekt-, Dokument- und Liefersemantik,
- eigene Zeitintervalle oder eine allgemeine Zeitontologie,
- rollenspezifische direkte Kurzproperties,
- externe Alignment-Axiome zu ORG, PROV-O, DCAT, ePO, IFC, Schema.org oder PRO.

## 7. Modulgrenzen

| Modul oder Artefakt | Zuständigkeit im Zusammenspiel |
| --- | --- |
| `core/agent` | Liefert die gemeinsame Klasse für den genau einen beteiligten Agenten |
| `core/person` | Beschreibt Personenstammdaten; eine Person kann Participant sein |
| `core/organization` | Beschreibt Organisationen und Membership; eine Organisation kann Participant oder Kontext sein |
| `core/document` | Stellt Dokumentsemantik bereit; ein Dokument kann Kontext einer Rollenzuordnung sein |
| Fachmodule | Definieren zulässige Kontexttypen und verwenden passende Rollen-Vokabulare |
| Rollen-Vokabular | Liefert konkrete Rollenindividuen getrennt von der Participation-T-Box |
| Spätere Aktivitätsontologie | Beschreibt Aktivitäten, Ereignisse und tatsächliche Aktivitätsteilnahme |

## 8. Anforderungen an die Core-Validierung

Das implementierte Core-SHACL-Profil prüft:

- genau einen Agenten je `Participation`,
- genau einen Rollenwert je `Participation`,
- genau einen Kontext je `Participation`,
- explizite Typisierung des Agenten als `core/agent:Agent`,
- explizite Typisierung des Rollenwerts als lokale `Role`,
- höchstens ein Start- und ein Enddatum,
- vollständige Datumswerte mit dem festgelegten Datentyp,
- ein Enddatum, das nicht vor dem Startdatum liegt,
- fachliche Eindeutigkeit der Kombination aus Agent, Rolle und Kontext,
- Verwendung der freigegebenen Werte des minimalen Rollen-Vokabulars dort, wo
  das entsprechende geschlossene Profil angewendet wird.

Die T-Box selbst soll keine Pflichtfelder oder Eindeutigkeitsregeln als
OWL-Kardinalitäten tragen. Diese Anforderungen sind im Core-SHACL-Profil
umgesetzt.

## 9. Abnahmekriterien für die Modellierungsfreigabe

Der [implementierte Begriffskatalog](term-catalog.md) und das
[fachliche Konzeptmodell](concept-model.md) konnten erstellt werden, weil:

1. Bedeutung und Name der zentralen Klasse bestätigt sind,
2. Agent, Rolle und Kontext jeweils genau einmal vorkommen,
3. unqualifizierte Beteiligungen ausgeschlossen sind,
4. Rollen als Individuen einer lokalen `Role` modelliert werden,
5. der Kontext typmäßig offen bleibt,
6. die zeitliche Gültigkeit optional über Start- und Enddatum umgesetzt ist,
7. Membership, Aktivitäten, Provenienz und Berechtigungen abgegrenzt sind,
8. externe Alignments und direkte Rollenproperties nicht zum MVP gehören,
9. ein minimales Rollen-Vokabular als separates MVP-Artefakt feststeht.

Die öffentlichen Begriffe, Property-Namen, Datumsdatentypen und der
Startumfang des Rollen-Vokabulars sind fachlich bestätigt. Weitere Rollen
werden erst aus den Quellen und Kompetenzfragen des jeweils zuständigen
Fachmoduls abgeleitet. Die [Modulgrenzen](module-boundaries.md), das
[SHACL-Anforderungsdokument](shacl-requirements.md), T-Box,
Rollen-Vokabular und [Core Shapes](core-shapes.md) sind für Version `0.1.0`
umgesetzt.

## 10. Verständliches Beispiel

> Eine Organisation kann im selben Kontext Lieferant und Auftragnehmer sein.
> Dafür werden zwei Participation-Ressourcen mit unterschiedlichen Rollen
> verwendet, statt beide Bedeutungen in eine unklare Aussage zu packen.
