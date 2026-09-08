# Begriffskatalog für den Participation-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/participation`  
**Umsetzungsstand:** Begriffe, Startrollen, T-Box und Core Shapes implementiert

## 1. Zweck

Dieser Katalog übersetzt den bestätigten Scope und die Quellenanalyse in
konkrete lokale Begriffe. Er beschreibt Klassen, Properties, Kardinalitäten,
Definitionen und den umgesetzten Startumfang eines minimalen Rollen-Vokabulars.

Die Kardinalitäten sind im Core-SHACL-Profil umgesetzt. Sie werden bewusst
nicht als harte OWL-Kardinalitäten in die T-Box übernommen.

Grundlagen:

- [Quellenanalyse](source-analysis.md)
- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Agent-Spezifikation](../../agent/docs/agent-specification.md)
- [Fachliches Konzeptmodell](concept-model.md)
- [Participation-Diagramme](diagrams/participation-concept-model.md)

## 2. Namensräume

### 2.1 Participation-Ontologie

```text
Ontologie-IRI: https://www.construct-x.org/ontology/participation
Versions-IRI:  https://www.construct-x.org/ontology/participation/0.1.0
Namespace:     https://www.construct-x.org/ontology/participation#
Prefix:        conx-part
```

### 2.2 Minimales Rollen-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/participation-role
Versions-IRI:  https://www.construct-x.org/vocab/participation-role/0.1.0
Namespace:     https://www.construct-x.org/vocab/participation-role#
Prefix:        part-role
```

Die IRIs sind durch Modul- und Dataset-Metadaten sowie die maschinenlesbaren
Artefakte für Version `0.1.0` verbindlich umgesetzt.

Wiederverwendete Namespaces:

```text
conx-agent: https://www.construct-x.org/ontology/agent#
skos:       http://www.w3.org/2004/02/skos/core#
xsd:        http://www.w3.org/2001/XMLSchema#
```

## 3. Modellierungsregeln

1. `Participation` beschreibt eine tatsächlich geltende oder historisch
   gegoltene Rollenzuordnung.
2. Eine Participation besitzt genau einen Agenten, genau eine Rolle und genau
   einen fachlichen Kontext.
3. Unqualifizierte Beteiligungen ohne Rolle sind nicht zulässig.
4. Pro Kombination aus Agent, Rolle und Kontext existiert fachlich genau eine
   Participation.
5. Rollen werden als Individuen der lokalen Klasse `Role` modelliert.
6. `Role` ist eine Unterklasse von `skos:Concept`.
7. Construct-X-gepflegte Rollenwerte werden in getrennt versionierten SKOS
   Concept Schemes gepflegt.
8. Der Kontexttyp bleibt offen; es wird keine lokale Klasse `Context`
   eingeführt.
9. Start- und Enddatum sind optional und beschreiben nur die Gültigkeit der
   Zuordnung.
10. Aktivitäten, Ereignisse, Provenienz, Nachweise, Status, Vollmacht und
    Berechtigungen werden nicht durch Participation modelliert.
11. Es werden keine rollenspezifischen Kurzproperties wie `isSellerOf`
    eingeführt.
12. OWL beschreibt Klassen, Bedeutung, Domain und Range. Mindestwerte,
    Maximalwerte, Datumsreihenfolge und Eindeutigkeit gehören in SHACL.

## 4. Begriffsübersicht

### 4.1 Klassen

| Lokaler Begriff | Oberklasse | MVP |
| --- | --- | --- |
| `conx-part:Participation` | keine lokale Oberklasse | Ja |
| `conx-part:Role` | `skos:Concept` | Ja |

### 4.2 Lokale Properties

| Property | Domain | Range | Core SHACL |
| --- | --- | --- | --- |
| `conx-part:participant` | `Participation` | `conx-agent:Agent` | genau `1` |
| `conx-part:role` | `Participation` | `Role` | genau `1` |
| `conx-part:context` | `Participation` | typmäßig offen | genau `1` |
| `conx-part:startDate` | `Participation` | `xsd:date` | `0..1` |
| `conx-part:endDate` | `Participation` | `xsd:date` | `0..1` |

Es sind im MVP keine inversen Properties vorgesehen. Die Navigation erfolgt
über die `Participation`-Ressource und ihre drei Kernbeziehungen.

## 5. Klassen

### 5.1 `conx-part:Participation`

| Punkt | Festlegung |
| --- | --- |
| Deutsche Bezeichnung | Beteiligung |
| Englische Bezeichnung | Participation |
| Definition | Tatsächlich geltende oder historisch gegoltene Zuordnung genau eines Agenten zu genau einer Rolle in genau einem fachlichen Kontext |
| Oberklasse | keine lokale Oberklasse |
| Kernanforderungen | genau ein `participant`, genau eine `role`, genau ein `context` |
| Optionale Angaben | höchstens ein `startDate` und ein `endDate` |
| Eindeutigkeit | Kombination aus `participant`, `role` und `context` ist fachlich eindeutig |
| Primäre Quellen | W3C N-ary Relations, W3C ORG Membership, ePO AgentInRole, IFC RelAssignsToActor |
| Alignment | Kein Klassenalignment im MVP |
| Ausschlüsse | geplante Rolle, Aktivitätsteilnahme, Provenienz, Berechtigung, Vollmacht und unqualifizierte Beteiligung |

Konzeptionelles Beispiel:

```turtle
ex:participation-1
    a conx-part:Participation ;
    conx-part:participant ex:bauunternehmen-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:contract-4711 ;
    conx-part:startDate "2026-01-15"^^xsd:date .
```

Die Instanz behauptet eine wirksame Rollenzuordnung. Sie behauptet nicht, dass
das Bauunternehmen bereits eine konkrete Aktivität ausgeführt hat.

### 5.2 `conx-part:Role`

| Punkt | Festlegung |
| --- | --- |
| Deutsche Bezeichnung | Rolle |
| Englische Bezeichnung | Role |
| Definition | Kontrolliert bezeichneter funktionaler Part, den ein Agent innerhalb einer Participation gegenüber einem Kontext einnimmt |
| Oberklasse | `skos:Concept` |
| Instanzen | Rollenwerte als Individuen, beispielsweise Auftraggeber oder Auftragnehmer |
| Concept Scheme | Keine globale Pflicht; für Construct-X-gepflegte Vokabulare vorgesehen |
| Primäre Quellen | W3C ORG `Role`, DCAT `Role`, IFC `IfcActorRole` |
| Alignment | Kein Alignment im MVP; klassenbasierte externe Rollenmodelle erfordern spätere Transformation |
| Ausschlüsse | Agententyp, Beruf, Berechtigungsrolle oder Rollenklasse als lokale Modellierungsform |

`Role` beschreibt den abstrakten Rollenwert. Sie ist nicht die konkrete
Zuordnung. Erst eine `Participation` verbindet den Rollenwert mit Agent und
Kontext.

## 6. Properties

### 6.1 `conx-part:participant`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt den Agenten, dessen Rolle durch die Participation beschrieben wird |
| Domain | `conx-part:Participation` |
| Range | `conx-agent:Agent` |
| Core SHACL | genau ein Wert |
| Inverse | keine lokale inverse Property im MVP |
| Quelle | W3C ORG `member`, ePO `playedBy`, IFC `RelatingActor` |

Eine Participation darf nicht mehrere Personen oder Organisationen bündeln.
Mehrere Agenten in derselben Rolle und demselben Kontext erhalten getrennte
Participation-Instanzen.

### 6.2 `conx-part:role`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die genau eine kontrollierte Rolle des Agenten in der Participation |
| Domain | `conx-part:Participation` |
| Range | `conx-part:Role` |
| Core SHACL | genau ein Wert |
| Quelle | W3C ORG `role`, PROV/DCAT `hadRole`, IFC `ActingRole` |

Eine Participation ohne Rollenwert ist ungültig. Besitzt derselbe Agent im
selben Kontext mehrere Rollen, wird für jede Rolle eine eigene Participation
verwendet.

### 6.3 `conx-part:context`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die genau eine fachliche Ressource, gegenüber der die Rollenzuordnung gilt |
| Domain | `conx-part:Participation` |
| Range | keine fachlich einschränkende lokale Klasse |
| Core SHACL | genau ein Ressourcenwert |
| Quelle | W3C-Muster für n-stellige Beziehungen, ePO `contextualisedBy`, SPAR PRO `relatesToEntity` |

Mögliche Kontextressourcen sind beispielsweise ein Vertrag, Projekt,
Dokument, Lieferschein, Produkt oder Asset. Das Participation-Modul inferiert
aus der Verwendung von `context` keinen lokalen Kontexttyp.

### 6.4 `conx-part:startDate`

| Punkt | Festlegung |
| --- | --- |
| Definition | Datum, ab dem die durch die Participation beschriebene Rollenzuordnung gilt oder galt |
| Domain | `conx-part:Participation` |
| Range | `xsd:date` |
| Core SHACL | `0..1` |
| Abgrenzung | kein Beginn einer Aktivität oder eines Kontextobjekts |
| Quelle | W3C ORG `memberDuring`, Schema.org Role `startDate`, SPAR PRO `RoleInTime` |

Das Fehlen des Startdatums bedeutet nur, dass der Beginn nicht angegeben ist.
Es bedeutet nicht, dass die Participation schon immer galt.

### 6.5 `conx-part:endDate`

| Punkt | Festlegung |
| --- | --- |
| Definition | Datum, bis zu dem die durch die Participation beschriebene Rollenzuordnung gilt oder galt |
| Domain | `conx-part:Participation` |
| Range | `xsd:date` |
| Core SHACL | `0..1` |
| Zusatzregel | Wenn Start- und Enddatum vorliegen, darf `endDate` nicht vor `startDate` liegen |
| Abgrenzung | kein Ende einer Aktivität oder eines Kontextobjekts |
| Quelle | W3C ORG `memberDuring`, Schema.org Role `endDate`, SPAR PRO `RoleInTime` |

Das Fehlen des Enddatums bedeutet nur, dass kein Ende angegeben ist. Daraus
darf ohne weitere Information keine unbegrenzte oder dauerhafte Zuordnung
abgeleitet werden.

## 7. Minimales Rollen-Vokabular

Das MVP soll ein kleines, getrennt versioniertes SKOS Concept Scheme enthalten.
Es dient als unmittelbar nutzbarer Startpunkt und verdeutlicht die Verwendung
von Rollenindividuen. Es ist keine abgeschlossene universelle Rollenliste.

### 7.1 Freigegebene Startwerte

| IRI-Suffix | Notation | Deutsch | Englisch | Verbindliche Bedeutung |
| --- | --- | --- | --- | --- |
| `ClientRole` | `client` | Auftraggeber | Client | Agent, in dessen Auftrag oder Interesse der jeweilige Kontext bearbeitet wird |
| `ContractorRole` | `contractor` | Auftragnehmer | Contractor | Agent, der im Kontext vertraglich zur Ausführung vereinbarter Leistungen verpflichtet ist |
| `SupplierRole` | `supplier` | Lieferant | Supplier | Agent, der im Kontext Güter, Materialien oder Betriebsmittel bereitstellt |
| `ArchitectRole` | `architect` | Architekt | Architect | Agent, der im Kontext eine architektonische Planungs- oder Gestaltungsfunktion wahrnimmt |
| `EngineerRole` | `engineer` | Ingenieur | Engineer | Agent, der im Kontext eine ingenieurtechnische Planungs-, Berechnungs- oder Gestaltungsfunktion wahrnimmt |

Diese fünf Werte bilden den fachlich freigegebenen, quellenbasierten
Startumfang. `ArchitectRole` und `EngineerRole` bezeichnen ausschließlich eine
Funktion im angegebenen Kontext. Sie klassifizieren den Agenten weder als
Beruf noch als Organisationstyp. Entsprechend werden auch `ClientRole`,
`ContractorRole` und `SupplierRole` nicht als Agenten- oder
Organisationsklassen behandelt.

Fachspezifische Rollen, beispielsweise Rollen eines Lieferscheins, werden
nicht vorsorglich in dieses minimale Vokabular aufgenommen. Ihr Rollenbestand
wird während der Entwicklung des jeweiligen Fachmoduls aus dessen eigenen
Kompetenzfragen und Quellen abgeleitet. Solche Rollen können in einem
getrennten SKOS Concept Scheme gepflegt und dennoch als `conx-part:Role`
verwendet werden.

### 7.2 Pflegegrundsätze

- Jeder Wert ist Instanz von `conx-part:Role` und `skos:Concept`.
- Jeder Wert besitzt deutsche und englische Vorzugsbezeichnungen und
  Definitionen.
- Jeder Wert besitzt eine stabile, sprachunabhängige `skos:notation`.
- Neue Werte werden im Rollen-Vokabular ergänzt und erfordern keine Änderung
  der Participation-T-Box.
- Entfernte Werte werden als veraltet gekennzeichnet und nicht
  bedeutungsverändert wiederverwendet.
- Fachlich engere Rollen-Vokabulare dürfen eigene Concept Schemes bilden.
- Ähnlich benannte Rollen werden nicht ohne Definitionsvergleich als
  `skos:exactMatch` ausgerichtet.

### 7.3 Abgrenzung zu AddressRole

Das vorhandene AddressRole-Vokabular verwendet dasselbe technische Prinzip:
lokale Rollenklasse plus getrennte SKOS-Individuen. Inhaltlich gehört es nicht
zum Participation-Vokabular. AddressRole beschreibt die Funktion einer Adresse
in einer Adresszuordnung; `conx-part:Role` beschreibt die Funktion eines
Agenten gegenüber einem Kontext.

## 8. Eindeutigkeit und mehrere Rollen

### 8.1 Mehrere Agenten

```turtle
ex:participation-a
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x .

ex:participation-b
    a conx-part:Participation ;
    conx-part:participant ex:organization-b ;
    conx-part:role part-role:EngineerRole ;
    conx-part:context ex:project-x .
```

### 8.2 Mehrere Rollen desselben Agenten

```turtle
ex:participation-c
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:ContractorRole ;
    conx-part:context ex:project-x .

ex:participation-d
    a conx-part:Participation ;
    conx-part:participant ex:organization-a ;
    conx-part:role part-role:SupplierRole ;
    conx-part:context ex:project-x .
```

Die Kombination aus Agent, Rolle und Kontext darf nicht durch eine zweite
Participation dupliziert werden. Diese Eindeutigkeit ist als SHACL-SPARQL-
Constraint umgesetzt und kein `owl:hasKey`-Axiom.

## 9. Ausdrücklich nicht eingeführte Begriffe

| Begriff | Grund |
| --- | --- |
| `AgentRoleAssignment` | `Participation` ist als zentraler Begriff bestätigt |
| `AgentInRole` | Wird nicht als zweite Klasse neben `Participation` benötigt |
| `Context` / `ParticipationContext` | Die Kontextressource bleibt typmäßig offen |
| `ActivityParticipation` | Aktivitäten und Ereignisse gehören in eine spätere Ontologie |
| `ParticipationStatus` | Eine Participation behauptet eine tatsächlich geltende oder gegoltene Zuordnung |
| `ParticipationEvidence` | Nachweise gehören nicht in dieses Modul |
| `hasParticipation` / `isParticipationOf` | Keine inverse oder zweite Pflichtdatenrichtung im MVP |
| `isSellerOf` und vergleichbare Properties | Rollen bleiben Individuen; keine Property pro Rollenwert |
| lokales Zeitintervall | Einfache optionale Datumswerte reichen für den MVP |
| externe Alignment-Axiome | Werden nur bei konkretem Bedarf in getrennten Alignment-Modulen bewertet |

## 10. Implementiertes Core-Validierungsprofil

Eine Instanz von `Participation` ist im implementierten Core-Profil gültig, wenn:

1. genau ein `participant` vorhanden und als `conx-agent:Agent` typisiert ist,
2. genau eine `role` vorhanden und als `conx-part:Role` typisiert ist,
3. genau ein `context` als RDF-Ressource vorhanden ist,
4. `startDate` und `endDate` jeweils höchstens einmal als `xsd:date`
   vorkommen,
5. ein vorhandenes `endDate` nicht vor einem vorhandenen `startDate` liegt,
6. keine zweite Participation dieselbe Kombination aus Agent, Rolle und
   Kontext beschreibt.

Ob ein Fachprofil ausschließlich Werte eines bestimmten Rollen-Concept-Schemes
zulässt, entscheidet dieses Profil. Der offene Core verlangt nur die
Typisierung als `conx-part:Role`.

## 11. Freigabeentscheidung

Am 27. August 2026 wurden für die weitere Spezifikation bestätigt:

1. die Property-Namen `participant`, `role`, `context`, `startDate` und
   `endDate`,
2. Namespace und Prefix `conx-part`,
3. IRI und Prefix `participation-role` beziehungsweise `part-role`,
4. die fünf Startrollen und ihre Definitionen aus Abschnitt 7.1,
5. die spätere Ableitung weiterer Rollen aus den jeweiligen Fachmodulen.

Das fachliche Zusammenspiel ist im [Konzeptmodell](concept-model.md), in den
[Participation-Diagrammen](diagrams/participation-concept-model.md) und in den
[Modulgrenzen](module-boundaries.md) dargestellt. Der ausführbare
Validierungsvertrag ist in den [SHACL-Anforderungen](shacl-requirements.md)
spezifiziert und in den [Core Shapes](core-shapes.md) umgesetzt.

## 12. Verständliches Beispiel

> `participant` nennt Anna, `role` nennt die Rolle Architektin und `context`
> nennt das Bauvorhaben. Erst die Kombination der drei Properties ergibt die
> vollständige fachliche Aussage.
