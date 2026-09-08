# Fachliches Konzeptmodell des Participation-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`  
**Umsetzungsstand:** Als T-Box, Rollen-Vokabular und Core Shapes umgesetzt

## 1. Ziel

Das Konzeptmodell führt Quellenanalyse, bestätigten Scope und Begriffskatalog
in einem konsistenten fachlichen Modell zusammen. Es beschreibt eine
qualifizierte Beziehung zwischen Agent, Rolle und Kontext, ohne die Semantik
dieser Ressourcen zu duplizieren.

Die visuellen Sichten stehen in den
[Participation-Diagrammen](diagrams/participation-concept-model.md). Klassen,
Properties und Kardinalitäten sind im [Begriffskatalog](term-catalog.md)
dokumentiert.

## 2. Modellkern

Der MVP besitzt zwei lokale Klassen:

```text
Participation
Role
```

Der fachliche Kern lautet:

```text
Participation
  participant -> genau ein Agent
  role        -> genau eine Role
  context     -> genau eine fachliche Ressource
  startDate   -> optional ein xsd:date
  endDate     -> optional ein xsd:date
```

`Participation` ist die konkrete Zuordnung. `Role` ist der kontrollierte
Rollenwert. Agent und Kontext werden aus ihren zuständigen Modulen
referenziert.

## 3. Bedeutung von Participation

Eine `Participation` beschreibt eine tatsächlich geltende oder historisch
gegoltene Rollenzuordnung. Sie ist weder eine Planung noch eine Behauptung über
die Ausführung einer Aktivität.

Beispiel:

```text
Organisation A ist Auftragnehmer im Vertrag X.
```

Diese Aussage enthält drei voneinander getrennte Elemente:

1. `Organisation A` ist der Agent.
2. `Auftragnehmer` ist die Rolle.
3. `Vertrag X` ist der Kontext.

Die Participation verbindet diese Elemente. Sie macht aus dem Agenten keine
Unterklasse `Contractor` und aus dem Vertrag keine Participation-eigene
Kontextklasse.

## 4. Qualifizierte Beziehung

Eine direkte Property wie `isContractorOf` könnte Agent und Kontext verbinden,
verliert aber die Rolle als eigenständig pflegbaren Wert und kann keine
Angaben zur Gültigkeit der Beziehung tragen.

Das qualifizierte Muster objektiviert deshalb die Beziehung:

```text
Agent A ---------> Participation P ---------> Kontext X
                         |
                         v
                     Rolle R
```

Die Participation ist keine RDF-Reifikation eines Triples. Sie ist eine
eigenständige fachliche Beziehungsressource gemäß dem W3C-Muster für
n-stellige Beziehungen.

## 5. Agent

`participant` verweist auf genau einen `conx-agent:Agent`. Dadurch können
Personen und Organisationen dasselbe Participation-Muster verwenden.

```text
conx-agent:Agent
  |- conx-person:Person
  `- conx-org:Organization
```

Das Modell schliesst die Agent-Hierarchie nicht auf diese beiden Typen. Ein
späterer weiterer Agententyp kann Participation verwenden, ohne die
Participation-T-Box zu ändern.

Mehrere Agenten werden nicht in einer Participation gebündelt. Handeln mehrere
Agenten gemeinsam, gibt es entweder je Agent eine eigene Participation oder
eine vorhandene Organisation beziehungsweise Arbeitsgemeinschaft wird als
gemeinsamer Agent referenziert.

## 6. Rolle

### 6.1 Rollenwert und Zuordnung

Die lokale Klasse `Role` ist Unterklasse von `skos:Concept`. Ihre Instanzen sind
kontrollierte Rollenwerte:

```text
Role
  |- ClientRole
  |- ContractorRole
  |- SupplierRole
  |- ArchitectRole
  `- EngineerRole
```

Die Rollen sind Individuen und keine Unterklassen von Agent oder Participation.
Eine Rolle wird erst durch ihre Verwendung in einer Participation einem Agenten
und Kontext zugeordnet.

### 6.2 Mehrere Rollen

Ein Agent kann im selben Kontext mehrere Rollen besitzen. Jede Rolle erhält
eine eigene Participation:

```text
P1 = Organisation A + ContractorRole + Projekt X
P2 = Organisation A + SupplierRole   + Projekt X
```

Dadurch bleibt jede Kombination einzeln referenzierbar. Eine Participation mit
zwei Rollen wäre unklar, sobald Start- und Enddatum oder weitere fachliche
Regeln je Rolle abweichen.

### 6.3 Rollen-Vokabulare

Die Participation-T-Box definiert keine abgeschlossene Rollenliste. Ein
minimales Construct-X-Vokabular soll die Verwendung illustrieren und einen
unmittelbar nutzbaren Startumfang bereitstellen. Weitere Fachvokabulare können
beispielsweise Vertrags-, Liefer-, Dokument- oder Lebenszyklusrollen enthalten.

Construct-X-gepflegte Rollen-Vokabulare verwenden SKOS Concept Schemes. Die
allgemeine T-Box erzwingt jedoch keine Scheme-Zugehörigkeit, damit externe
Rollenwerte nach ausdrücklicher Typisierung verwendbar bleiben.

## 7. Kontext

### 7.1 Offener Ressourcenbezug

Der Kontext ist die Ressource, gegenüber der die Rolle gilt. Je nach Fachmodul
kann das beispielsweise sein:

- ein Vertrag,
- ein Projekt,
- ein Dokument,
- ein Lieferschein,
- ein Produkt oder Asset,
- eine andere fachlich definierte Ressource.

Diese Ressourcen besitzen keine notwendige gemeinsame lokale Oberklasse. Das
Participation-Modul führt deshalb keine Klasse `Context` ein und setzt keine
fachlich einschränkende Range auf `context`.

### 7.2 Genau ein Kontext

Eine Participation besitzt genau einen Kontext. Gilt dieselbe Rolle für zwei
Verträge, werden zwei Participation-Instanzen angelegt:

```text
P1 = Organisation A + ContractorRole + Vertrag X
P2 = Organisation A + ContractorRole + Vertrag Y
```

Mehrere Kontexte in derselben Instanz würden unklar lassen, ob die
Rollenzuordnung und ihre Gültigkeitsdaten für jeden Kontext identisch gelten.

Fachprofile dürfen den offenen Kontext einschränken. Ein Dokumentprofil kann
beispielsweise nur `Document` als Kontext zulassen, ohne die allgemeine
Participation-T-Box zu verändern.

## 8. Eindeutigkeit

Pro Kombination aus Agent, Rolle und Kontext existiert fachlich genau eine
Participation:

```text
(participant, role, context) -> eine Participation
```

Diese Regel verhindert doppelte Beziehungsressourcen für dieselbe Aussage. Sie
wird mit SHACL gegen den Datengraphen geprüft. Ein `owl:hasKey` wird
nicht vorgesehen, weil eine Verletzung als Datenqualitätsfehler gemeldet und
nicht über `owl:sameAs` logisch zusammengeführt werden soll.

Mehrere getrennte Gültigkeitsabschnitte derselben Kombination sind im MVP
nicht modellierbar. Ein solcher Bedarf würde entweder die Eindeutigkeitsregel
oder das Zeitmodell grundlegend ändern und erfordert deshalb eine eigene
spätere Modellentscheidung.

## 9. Zeitliche Gültigkeit

`startDate` und `endDate` sind optionale Datumswerte an der Participation:

| Angaben | Bedeutung |
| --- | --- |
| kein Datum | Die Zuordnung gilt oder galt; zeitliche Grenzen sind nicht angegeben |
| nur `startDate` | Beginn der Gültigkeit ist angegeben, Ende nicht |
| nur `endDate` | Ende der Gültigkeit ist angegeben, Beginn nicht |
| beide Daten | Gültigkeit ist durch Anfang und Ende begrenzt |

Wenn beide Werte vorhanden sind, darf `endDate` nicht vor `startDate` liegen.
Die Daten bezeichnen weder Beginn noch Ende einer Aktivität und verändern
nicht die Laufzeit des Kontextobjekts.

Der MVP verwendet einfache `xsd:date`-Werte. Eine lokale Intervallklasse oder
ein Import von OWL-Time ist nicht erforderlich.

## 10. Abgrenzung zu Aktivitäten

Participation beschreibt Rollen, keine Aktivitätsteilnahme:

```text
Participation:
  Organisation A ist Contractor im Projekt X.

Spätere Aktivitätsontologie:
  Organisation A führt Aktivität Y aus.
```

Die erste Aussage beweist die zweite nicht. Eine Rolle kann bestehen, ohne dass
eine konkrete Aktivität bereits begonnen oder beendet wurde. Eine spätere
Aktivitätsontologie darf auf Agent, Participation oder Rolle verweisen, besitzt
aber ihre eigene Ereignis- und Ausführungssemantik.

## 11. Abgrenzung zu Membership

`core/organization:Membership` und `Participation` bleiben getrennt:

| Membership | Participation |
| --- | --- |
| Zugehörigkeit zu einer Organisation | Rolle gegenüber einem beliebigen Kontext |
| Kontext ist eine Organization | Kontexttyp bleibt offen |
| Rollenwert im aktuellen MVP nicht erforderlich | genau eine Role erforderlich |
| eigene Kennung wie Mitgliedsnummer möglich | keine Participation-eigene Kennung vorgesehen |

Membership wird deshalb nicht als Unterklasse von Participation modelliert.
Das Participation-Modul verändert keine bestehende Organisationssemantik.

## 12. Keine rollenspezifischen Kurzproperties

Das Modell führt keine Properties wie `isClientOf`, `isContractorOf` oder
`isSupplierOf` ein. Die vollständige Aussage bleibt:

```text
Participation -> participant
              -> role
              -> context
```

Damit können Rollen durch neue Individuen erweitert werden, ohne für jeden
Wert eine neue T-Box-Property und zusätzliche Inferenzregel einzuführen.

## 13. Herkunft, Nachweis und Status

Das Vorhandensein einer Participation behauptet eine tatsächlich geltende oder
historisch gegoltene Zuordnung. Das Modul besitzt deshalb keine Statuswerte für
geplante, vorgeschlagene oder widerrufene Beziehungen.

Herkunft, Nachweis, Provenienz, Vollmacht und Berechtigung werden weder im MVP
modelliert noch als spätere Erweiterung dieses Moduls vorgemerkt. Andere
Modelle können Participation-Ressourcen referenzieren, ohne dass deren
Semantik in den Participation-Kern gezogen wird.

## 14. Konzeptionelles Gesamtbeispiel

Die folgenden Namen sind in Version `0.1.0` implementierte Ontologie- und
Vokabularbegriffe:

```turtle
@prefix conx-part: <https://www.construct-x.org/ontology/participation#> .
@prefix part-role: <https://www.construct-x.org/vocab/participation-role#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .

ex:contractor-participation
    a conx-part:Participation ;
    conx-part:participant ex:bauunternehmen-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-4711 ;
    conx-part:startDate "2026-01-15"^^xsd:date ;
    conx-part:endDate "2026-12-31"^^xsd:date .

ex:supplier-participation
    a conx-part:Participation ;
    conx-part:participant ex:bauunternehmen-a ;
    conx-part:role part-role:SupplierRole ;
    conx-part:context ex:contract-4711 .
```

Dasselbe Unternehmen besitzt zwei unterschiedliche Rollen im selben Vertrag.
Deshalb werden zwei Participation-Instanzen verwendet.

## 15. Modellentscheidungen

1. `Participation` ist die einzige lokale Klasse für die konkrete
   Rollenzuordnung.
2. Eine Participation bildet genau eine Kombination aus Agent, Rolle und
   Kontext ab.
3. `participant`, `role` und `context` sind im Core-Profil jeweils genau einmal
   erforderlich.
4. Rollen werden als Individuen der lokalen, SKOS-basierten Klasse `Role`
   gepflegt.
5. Der Kontext bleibt typmäßig offen und wird durch Fachprofile
   eingeschränkt.
6. Start- und Enddatum sind optionale `xsd:date`-Werte für die Gültigkeit.
7. Aktivitäten und Ereignisse sind nicht Bestandteil des Modells.
8. Membership bleibt ein unabhängiges Organisationskonzept.
9. Es gibt keine rollenspezifischen Kurzproperties und keine externen
   Alignment-Axiome im MVP.
10. Herkunft, Nachweis, Status, Provenienz, Vollmacht und Berechtigung sind
    ausgeschlossen.
11. Ein minimales Rollen-Vokabular mit den freigegebenen Rollen `ClientRole`,
    `ContractorRole`, `SupplierRole`, `ArchitectRole` und `EngineerRole` wird
    getrennt von der T-Box bereitgestellt.
12. Kardinalität, Datumsreihenfolge und Eindeutigkeit sind in SHACL und nicht
    als harte OWL-Kardinalitäten umgesetzt.
13. Weitere Rollen werden bei der Entwicklung des jeweils zuständigen
    Fachmoduls fachlich hergeleitet und nicht vorsorglich in den Core gezogen.
