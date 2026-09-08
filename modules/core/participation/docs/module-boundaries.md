# Modulgrenzen des Participation-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`

## 1. Ziel

Dieses Dokument ordnet die Begriffe des Participation-Moduls den zuständigen
Construct-X-Modulen zu. Es verhindert, dass eine allgemeine kontextuelle
Rollenzuordnung zugleich Agentenstammdaten, Kontextsemantik, Aktivitäten,
Mitgliedschaften, Nachweise oder Berechtigungen modelliert.

Das Participation-Modul beschreibt ausschließlich die Aussage:

```text
Ein Agent nimmt genau eine Rolle gegenüber genau einem Kontext ein.
```

Die Aussage kann optional durch Beginn und Ende ihrer Gültigkeit ergänzt
werden.

## 2. Leitprinzipien

1. `Participation` besitzt die qualifizierte Beziehung zwischen Agent, Rolle
   und Kontext.
2. Agent, Rollenwert und Kontext behalten ihre fachliche Identität ausserhalb
   der Participation.
3. Rollen werden als Individuen einer lokalen, SKOS-basierten Klasse `Role`
   modelliert.
4. Der Kontext bleibt typmäßig offen und wird von seinem Fachmodul
   beschrieben.
5. Eine Participation behauptet eine tatsächlich geltende oder historisch
   gegoltene Zuordnung, keine Planung oder Möglichkeit.
6. Aktivitäts- und Ereignisteilnahme wird nicht durch Participation
   beschrieben.
7. Beziehungen mit eigener fachlicher Semantik bleiben in ihrem
   Ursprungsmodul.
8. Weitere Rollen werden erst im Entwicklungsprozess des zuständigen
   Fachmoduls hergeleitet.

## 3. Eigentümerschaft nach Modul

| Modul oder Artefakt | Besitzt | Besitzt ausdrücklich nicht |
| --- | --- | --- |
| `core/participation` | `Participation`, `Role`, `participant`, `role`, `context`, `startDate`, `endDate` | Agentenstammdaten, Kontextklassen, Aktivitäten, Mitgliedschaft, Provenienz, Berechtigung |
| `core/agent` | gemeinsame Klasse `Agent` | konkrete Rollen und Rollenzuordnungen |
| `core/person` | Personen und intrinsische Personendaten | allgemeine kontextuelle Agentenrollen |
| `core/organization` | Organisationen, Organisationseinheiten, `Membership`, rechtliche Vertretung | allgemeine Prozess-, Vertrags- oder Dokumentrollen |
| `core/document` | Dokumente und Dokumentsemantik | allgemeine Agentenrollenzuordnung |
| spätere Aktivitätsontologie | Aktivitäten, Ereignisse und deren tatsächliche Teilnahme | allgemeine ressourcenbezogene Rollenzuordnung |
| Fachmodule | eigene Kontexttypen, fachliche Verbindlichkeit und fachspezifische Rollen-Vokabulare | generisches Participation-Muster |
| `participation-role` | fünf allgemeine Startrollen als Referenzdaten | T-Box-Begriffe und fachmodulspezifische Rollenlisten |

## 4. Modellkern und Beziehungsrichtung

Die Participation ist eine eigenständige fachliche Beziehungsressource:

```text
Agent <--- participant --- Participation --- context ---> Kontext
                              |
                              `--- role ---> Role
```

Die Properties gehen von der Participation zu ihren drei Bestandteilen aus.
Der MVP führt keine inversen Beziehungen wie `hasParticipation` oder
`isParticipationOf` ein. Anwendungen können Participations durch Abfragen
über `participant`, `role` und `context` auffinden.

Rollenspezifische Properties wie `isContractorOf`, `hasSeller` oder
`hasArchitect` werden ebenfalls nicht im Core definiert. Sie würden für
jeden neuen Rollenwert eine T-Box-Änderung erzeugen und die Rolle wieder in
die Property statt in den kontrollierten Wert verlagern.

## 5. Abgrenzung zu Agent

`participant` verweist auf genau einen `conx-agent:Agent`. Das
Participation-Modul definiert weder neue Agentenarten noch eine geschlossene
Auswahl aus Person und Organisation.

Dadurch können heute insbesondere folgende vorhandene Typen verwendet werden:

```text
conx-person:Person       rdfs:subClassOf conx-agent:Agent
conx-org:Organization    rdfs:subClassOf conx-agent:Agent
```

Spätere Agent-Unterklassen werden automatisch anschlussfähig, ohne die
Participation-T-Box zu erweitern. Namen, Kennungen, Anschriften und
Kontaktdaten des Agenten bleiben in ihren jeweiligen Modulen.

## 6. Abgrenzung des Kontextes

Der Kontext ist die genau eine Ressource, gegenüber der die Rolle gilt. Das
Participation-Modul definiert bewusst weder `Context` noch eine geschlossene
Oberklasse für Kontextressourcen.

Mögliche Kontexte sind beispielsweise:

- ein Vertrag,
- ein Projekt,
- ein Dokument,
- ein Produkt oder Asset,
- eine Ausschreibung,
- eine andere fachlich identifizierte Ressource.

Das Modul, das die Kontextressource definiert, besitzt auch deren
Eigenschaften, Lebenszyklus und Validierungsregeln. Aus der Verwendung als
`context` folgt keine neue Typisierung der Ressource.

Ein Fachprofil darf den Kontext für seinen Anwendungsfall einschränken. Ein
Dokumentprofil kann beispielsweise einen bestimmten Dokumenttyp verlangen,
ohne dass diese Einschränkung in das allgemeine Participation-Core-Shape
übernommen wird.

## 7. Rollenklasse und Rollen-Vokabulare

Die Participation-T-Box definiert nur die allgemeine Klasse `Role` als
Unterklasse von `skos:Concept`. Konkrete Rollen sind Referenzdaten und keine
Unterklassen von Agent oder Participation.

Das minimale Vokabular `participation-role` enthält ausschließlich:

- `ClientRole`,
- `ContractorRole`,
- `SupplierRole`,
- `ArchitectRole`,
- `EngineerRole`.

Diese Rollen illustrieren den allgemeinen Modellkern. Insbesondere
`ArchitectRole` und `EngineerRole` bezeichnen Funktionen im jeweiligen Kontext
und keine Berufe oder Agententypen.

Fachspezifische Rollen werden bei der Entwicklung des jeweiligen Fachmoduls
aus dessen Quellen und Kompetenzfragen abgeleitet. Rollen für einen
Lieferschein werden daher erst im Entwicklungsprozess des Lieferscheinmoduls
festgelegt. Sie können in einem eigenen SKOS Concept Scheme liegen und werden
durch die explizite Typisierung als `conx-part:Role` mit Participation
verwendbar.

Das offene Core-Profil verlangt keine Zugehörigkeit zum minimalen
`participation-role`-Scheme. Ein Fachprofil darf dagegen genau sein eigenes
freigegebenes Rollen-Scheme verlangen.

## 8. Abgrenzung zu Membership

`conx-org:Membership` bleibt eine eigenständige Organisationsbeziehung. Eine
Membership behauptet, dass ein Agent Mitglied einer Organisation ist. Eine
Participation behauptet allgemeiner, dass ein Agent eine Rolle gegenüber
einem fachlichen Kontext einnimmt.

```text
Membership:
  Agent + Organization

Participation:
  Agent + Role + offener Kontext
```

Membership wird im MVP weder Unterklasse von Participation noch durch eine
Participation ersetzt. Eine spätere Ausrichtung kann nur erfolgen, wenn
beide Modelle in ihren Kardinalitäten, Zeitangaben und Rollenfolgen
tatsächlich kompatibel sind.

## 9. Abgrenzung zu Aktivitäten und Ereignissen

Eine Participation sagt nicht aus, dass der Agent eine Aktivität ausgeführt
oder an einem Ereignis teilgenommen hat.

```text
Organisation A hat ContractorRole im Vertrag X.
```

Diese Aussage belegt keine konkrete Bauleistung. Eine spätere
Aktivitätsontologie kann Aktivitäten, Ereignisse, Ausführende und Zeitpunkte
modellieren und dabei auf vorhandene Agents oder Participations verweisen.
Die entsprechende Ausführungssemantik wird nicht nachträglich in
Participation aufgenommen.

## 10. Abgrenzung zu Dokumenten und weiteren Fachmodulen

Ein Dokument kann Kontext einer Participation sein. Das Document-Modul besitzt
jedoch Dokumenttyp, Version, Inhalt, Status und weitere Dokumentsemantik.

Ein Fachmodul darf insbesondere:

- seine Ressourcen als Kontext verwenden,
- ein eigenes Rollen-Vokabular bereitstellen,
- bestimmte Rollen und Kontexttypen verpflichtend machen,
- zusätzliche fachliche Constraints auf Participations formulieren.

Es darf dafür das generische Modell wiederverwenden, ohne `Participation`,
`participant`, `role` oder `context` erneut zu definieren.

## 11. Zeitliche Gültigkeit

`startDate` und `endDate` beschreiben ausschließlich die Gültigkeit der
Rollenzuordnung. Sie beschreiben nicht:

- Beginn oder Ende des Kontextobjekts,
- Dauer einer Aktivität,
- Erstellungs- oder Änderungszeitpunkt der RDF-Aussage,
- Publikations- oder Bearbeitungsstatus.

Fehlende Datumswerte bedeuten nur, dass die jeweilige Grenze nicht angegeben
ist. Sie erlauben keine Aussage über unbegrenzte oder ewige Gültigkeit.

## 12. Eindeutigkeit und Identität

Pro Kombination aus Agent, Rolle und Kontext existiert fachlich genau eine
Participation:

```text
(participant, role, context) -> eine Participation
```

Start- und Enddatum gehören nicht zum Eindeutigkeitsschlüssel. Zwei
Participations mit identischem Agenten, Rollenwert und Kontext bleiben daher
auch dann ein Duplikat, wenn sie unterschiedliche Datumswerte tragen. Diese
Folge ist Bestandteil der bestätigten Modellentscheidung.

Die Regel wird nicht als `owl:hasKey` modelliert. Sie gehört in das
Core-SHACL-Profil und gilt innerhalb des jeweils gemeinsam validierten
Datengraphen.

## 13. Ausgeschlossene Semantik

Das Participation-Modul besitzt weder heute noch als vorgemerkte Erweiterung:

- geplante, angefragte oder mögliche Rollen,
- Participation-Status,
- Herkunft und Provenienz der Aussage,
- Nachweise und Belege,
- Vollmachten und Berechtigungen,
- Vertrags- oder Vergütungsbedingungen,
- Verantwortlichkeit für konkrete Aktivitäten,
- Zugriffsschutz und Datenschutzregeln.

Andere Module können eine Participation referenzieren. Daraus folgt nicht,
dass deren Semantik Teil des Participation-Kerns wird.

## 14. T-Box-, A-Box- und Shape-Trennung

### 14.1 Participation-T-Box

- `Participation`
- `Role`
- `participant`
- `role`
- `context`
- `startDate`
- `endDate`

### 14.2 Referenzdaten

- minimales Concept Scheme `participation-role`
- fünf freigegebene allgemeine Rollenindividuen
- spätere, getrennt versionierte Rollen-Schemes der Fachmodule

### 14.3 Core Shapes

- Pflicht- und Maximalwerte
- Ressourcenformen und Typanforderungen
- Datumsdatentyp und Datumsreihenfolge
- Eindeutigkeit von Agent, Rolle und Kontext

Die T-Box enthält keine geschlossene Rollenaufzählung und keine harten
OWL-Kardinalitäten für diese Datenqualitätsregeln.

## 15. Abhängigkeits- und Alignment-Strategie

| Quelle oder Modul | Einordnung für den MVP |
| --- | --- |
| `core/agent` | referenziert, weil `participant` auf `conx-agent:Agent` verweist |
| SKOS | wiederverwendet für `Role` und Rollen-Vokabulare |
| `participation-role` | getrennt versionierter Referenzdatensatz, nicht in der T-Box eingeschlossen |
| Person, Organization, Document und Fachmodule | keine zwingenden Imports; gemeinsame Nutzung in Daten und Profilen |
| W3C ORG, PROV-O, DCAT, ePO, IFC, Schema.org und PRO | Analysequellen und spätere Alignment-Kandidaten, keine Gleichsetzungen im MVP |

Eine reine Referenz auf fremde Begriffe erzeugt keinen automatischen
`owl:imports`-Eintrag. Tatsächliche Imports oder Alignment-Axiome werden nur
nach separater fachlicher Prüfung eingeführt.

## 16. Umsetzungsstand der Modulgrenzen

Die beschriebenen Modulgrenzen sind in Version `0.1.0` umgesetzt:

1. Die T-Box referenziert `core/agent` und SKOS, ohne fremde Fachsemantik zu übernehmen.
2. Das minimale Rollen-Vokabular ist getrennt von der T-Box bereitgestellt.
3. Das Core-SHACL-Profil setzt die freigegebenen Kardinalitäten und Datumsregeln um.
4. Positive und negative Testdaten decken den SHACL-Vertrag ab.
5. Person und Organization werden als konkrete Agent-Unterklassen im Integrationstest geprüft.
6. Modul- und Shape-Dokumentation sowie Netzwerkansichten sind erzeugt.

Weitere Module können `Participation` verwenden und ihre fachlichen Kontexttypen
und Rollen-Vokabulare selbst festlegen, ohne die Core-T-Box zu erweitern.

## 17. Verständliches Beispiel

> Participation beschreibt „Anna ist Architektin im Bauvorhaben“. Eine
> Membership beschreibt dagegen „Anna ist Mitglied im Architekturbüro“.
> Obwohl beide Aussagen Rollen enthalten, gehören sie in verschiedene Module.
