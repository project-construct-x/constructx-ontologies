# Construct-X Namespace- und IRI-Konzept

Dokumentstand: 2026-08-18

Dieses Dokument legt das verbindliche Namespace-, IRI- und Versionierungskonzept fuer das Construct-X-Ontologienetzwerk fest. Es richtet sich auch an Personen ohne vertiefte Semantic-Web-Kenntnisse und trennt bewusst zwischen Ontologien, SHACL-Graphen, Referenzvokabularen und persistenten Referenzobjekten.

## Inhaltsverzeichnis

1. [Entscheidung in Kurzform](#1-entscheidung-in-kurzform)
2. [Authority und Grundsatz](#2-authority-und-grundsatz)
3. [Orientierung an etablierten Vorbildern](#3-orientierung-an-etablierten-vorbildern)
4. [Oeffentliche Namensraeume und Ressourcenarten](#4-oeffentliche-namensraeume-und-ressourcenarten)
5. [Praefix- und Benennungskonventionen](#5-praefix--und-benennungskonventionen)
6. [Versionierungsregeln](#6-versionierungsregeln)
7. [Repository-Struktur und oeffentliche IRIs](#7-repository-struktur-und-oeffentliche-iris)
8. [Dereferenzierung und Auslieferung](#8-dereferenzierung-und-auslieferung)
9. [Katalog nach QUDT-Vorbild](#9-katalog-nach-qudt-vorbild)
10. [Beispiele aktueller Module](#10-beispiele-aktueller-module)
11. [Technische und organisatorische Pruefregeln](#11-technische-und-organisatorische-pruefregeln)
12. [Festgestellte Abweichungen und Anpassungen](#12-festgestellte-abweichungen-und-anpassungen)
13. [Verbindliche Empfehlung](#13-verbindliche-empfehlung)

## 1. Entscheidung in Kurzform

Als vorlaeufige kanonische Authority wird verwendet:

```text
https://www.construct-x.org
```

Construct-X verwendet dereferenzierbare HTTPS-IRIs und keine eigenen URNs. URNs duerfen nur verwendet werden, wenn ein eingebundenes externes System sie verbindlich vorgibt.

Die zentralen Muster lauten:

```text
Ontologie:
https://www.construct-x.org/ontology/{modul}

Ontologieversion:
https://www.construct-x.org/ontology/{modul}/{semver}

Ontologiebegriff:
https://www.construct-x.org/ontology/{modul}#{localName}

SHACL-Graph:
https://www.construct-x.org/shapes/{modul}/{shape-set}

SHACL-Version:
https://www.construct-x.org/shapes/{modul}/{shape-set}/{semver}

SHACL-Shape:
https://www.construct-x.org/shapes/{modul}/{shape-set}#{localName}

Stabiles Referenzvokabular:
https://www.construct-x.org/vocab/{vokabular}

Konkrete Vokabularversion:
https://www.construct-x.org/vocab/{vokabular}/{semver}

Stabiler Vokabularbegriff:
https://www.construct-x.org/vocab/{vokabular}#{localName}

Referenzobjekt in seiner aktuellen Revision:
https://www.construct-x.org/id/{typ}/{guid}

Exakte Revision eines Referenzobjekts:
https://www.construct-x.org/id/{typ}/{guid}/revision/{revision}
```

Ontologien und Referenzvokabulare werden als vollstaendige Graphen veroeffentlicht und mit SemVer versioniert. Ihre Begriffs-IRIs bleiben versionsunabhaengig. Referenzobjekte unter `/id/` besitzen dagegen einen individuellen Lebenszyklus. Eine Revision behaelt ihre GUID und erhoeht die Revisionsnummer. Eine neue fachliche Version erhaelt eine neue GUID und verweist auf die ersetzte Version.

Beispiel fuer ein Referenzvokabular:

```text
Stabiles Vokabular:
https://www.construct-x.org/vocab/wall-type

Vokabularversion:
https://www.construct-x.org/vocab/wall-type/1.2.0

Stabiler Vokabularbegriff:
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

Beispiel fuer ein Referenzobjekt:

```text
Aktuelle Revision einer Property-Version:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000

Exakte Revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Die IRI ohne Revisionssegment kann auf die aktuelle Revision der durch die GUID identifizierten fachlichen Version verweisen. Fuer normative, pruefungsrelevante oder reproduzierbare Verweise ist immer die konkrete Revisions-IRI zu verwenden.

## 2. Authority und Grundsatz

Vor dem ersten stabilen oeffentlichen Release muss geprueft werden, ob `https://www.construct-x.org` dauerhaft als kanonische Authority verwendet werden kann.

Die oeffentlichen IRIs sollen fachlich stabil sein. Interne Repository-Kategorien duerfen nicht Bestandteil oeffentlicher Ontologie-IRIs werden. Das Core-Modul unter `modules/core/address` wird deshalb als `https://www.construct-x.org/ontology/address` identifiziert, nicht als `/ontology/core/address`.

## 3. Orientierung an etablierten Vorbildern

Construct-X orientiert sich an etablierten Linked-Data- und OWL-Prinzipien: stabile IRIs fuer Begriffe, versionierte Graphen fuer veroeffentlichte Staende und nachvollziehbare Katalogeintraege fuer Publikationen.

### 3.1 QUDT

QUDT trennt stabile Begriffs-IRIs von versionierten Graphveroeffentlichungen. Construct-X uebernimmt dieses Prinzip fuer Ontologien, SHACL-Graphen und Referenzvokabulare.

| Bereich | Stabile IRI | Versionierte IRI | Beispiel |
| --- | --- | --- | --- |
| Ontologiegraph | ja | ja | `https://www.construct-x.org/ontology/vso/0.1.0` |
| SHACL-Graph | ja | ja | `https://www.construct-x.org/shapes/address/core/0.1.0` |
| Referenzvokabular | ja | ja | `https://www.construct-x.org/vocab/wall-type/1.0.0` |
| Begriff | ja | nein | `https://www.construct-x.org/vocab/wall-type#ExternalWall` |

Construct-X uebertraegt das QUDT-Prinzip der stabilen Begriffs-IRIs auch auf Referenzvokabulare. Eine neue Veroeffentlichung des Vokabulargraphen erzeugt daher keine neuen IRIs fuer unveraendert fortbestehende Begriffe.

Beispiel: Wenn im Vokabular `wall-type` in Version `1.1.0` ein neuer Wandtyp ergaenzt wird, bleibt der bestehende Begriff `https://www.construct-x.org/vocab/wall-type#ExternalWall` unveraendert erhalten.

## 4. Oeffentliche Namensraeume und Ressourcenarten

### 4.1 Oeffentliche Namensraeume

| Artefakt oder Ressource | Muster | Beispiel |
| --- | --- | --- |
| Ontologieserie | `/ontology/{modul}` | `https://www.construct-x.org/ontology/vso` |
| Begriffsnamespace | `/ontology/{modul}#` | `https://www.construct-x.org/ontology/vso#AssignedProperty` |
| Konkrete Ontologieversion | `/ontology/{modul}/{semver}` | `https://www.construct-x.org/ontology/vso/0.1.0` |
| SHACL-Graph | `/shapes/{modul}/{shape-set}` | `https://www.construct-x.org/shapes/address/core` |
| Shape-Namespace | `/shapes/{modul}/{shape-set}#` | `https://www.construct-x.org/shapes/address/core#AddressShape` |
| Konkrete SHACL-Version | `/shapes/{modul}/{shape-set}/{semver}` | `https://www.construct-x.org/shapes/address/core/0.1.0` |
| Referenzvokabular | `/vocab/{vokabular}` | `https://www.construct-x.org/vocab/wall-type` |
| Konkrete Vokabularversion | `/vocab/{vokabular}/{semver}` | `https://www.construct-x.org/vocab/wall-type/1.2.0` |
| Begriff eines Referenzvokabulars | `/vocab/{vokabular}#{localName}` | `https://www.construct-x.org/vocab/wall-type#ExternalWall` |
| Referenzobjekt in seiner aktuellen Revision | `/id/{typ}/{guid}` | `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000` |
| Exakte Revision eines Referenzobjekts | `/id/{typ}/{guid}/revision/{revision}` | `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2` |
| Alignment | `/alignment/{alignment}` | `https://www.construct-x.org/alignment/address-vcard` |
| Netzwerkkatalog | `/catalog` | `https://www.construct-x.org/catalog` |
| Dokumentation | `/docs/{modul}` | `https://www.construct-x.org/docs/vso` |

Die Basis-IRI eines Referenzobjekts, zum Beispiel `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000`, repraesentiert die fachliche Version des Referenzobjekts und kann auf deren aktuelle Revision verweisen. Die exakte Revisions-IRI, zum Beispiel `.../revision/2`, bezeichnet dagegen dauerhaft einen unveraenderlichen Stand. Fuer Audits, Normverweise, Tests und reproduzierbare Datenverarbeitung ist die exakte Revisions-IRI zu verwenden.

### 4.2 Ressourcenarten

- `/ontology/` enthaelt T-Box-Begriffe wie Klassen, ObjectProperties, DataProperties und formale Axiome.
- `/vocab/` enthaelt kontrollierte A-Box-Referenzdaten wie Auswahlwerte, Statuswerte oder Klassifikationsbegriffe.
- `/id/` enthaelt eigenstaendig verwaltete Referenzobjekte mit stabiler Identitaet und eigenem Lebenszyklus.

Operative A-Box-Ressourcen wie konkrete Gebaeude, Waende oder Personen erhalten ihre IRIs durch den jeweiligen Datenhalter und nicht durch das Construct-X-Ontologienetzwerk.

### 4.3 T-Box-Begriffe und Referenzdaten trennen

T-Box-Begriffe beschreiben fachliche Klassen und Eigenschaften. Referenzdaten beschreiben Werte, Katalogeintraege oder reale beziehungsweise verwaltete Referenzobjekte.

Beispiele:

```text
Wandklasse:
https://www.construct-x.org/ontology/wall#Wall

Auswahlwert "Aussenwand":
https://www.construct-x.org/vocab/wall-type#ExternalWall

ISOProps-Merkmalsdefinition:
https://www.construct-x.org/id/property/{guid}

Konkrete Wand eines Datenhalters:
https://data.example.com/building/123/wall/456
```

Die GUID identifiziert eine fachliche Version des Referenzobjekts. Aenderungen innerhalb dieser fachlichen Version werden als Revisionen gefuehrt und behalten die GUID. Entsteht eine neue fachliche Version, wird eine neue GUID vergeben. Die neue Version verweist auf die zuvor gueltige Version.

Beispiel Wandhoehe als Revision: Wenn bei einer Property-Version `Wandhoehe` nur eine englische Benennung ergaenzt wird, kann dies als neue Revision behandelt werden. Die GUID bleibt erhalten, und die Revisionsnummer wird beispielsweise von `1` auf `2` erhoeht.

```text
Revision 1:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/1

Revision 2:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Beide Staende bleiben erreichbar. Revision `1` dokumentiert den urspruenglich veroeffentlichten Stand, Revision `2` den Stand mit ergaenzter englischer Benennung.

Beispiel fuer eine neue fachliche Version:

```text
Bisherige Version:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2

Neue fachliche Version:
https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1
```

Die neue Version verweist mit `dcterms:replaces` auf die alte Version:

```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1>
    dcterms:replaces
        <https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2> .
```

## 5. Praefix- und Benennungskonventionen

Construct-X-Ontologien verwenden Praefixe nach folgendem Muster:

```text
conx-{modulkuerzel}
```

Das Modulkuerzel muss kurz, eindeutig, stabil und vollstaendig kleingeschrieben sein. Der Bindestrich ist verbindlich.

Beispiele:

```turtle
@prefix conx-vso:  <https://www.construct-x.org/ontology/vso#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-org:  <https://www.construct-x.org/ontology/organization#> .
@prefix conx-doc:  <https://www.construct-x.org/ontology/document#> .
@prefix conx-unit: <https://www.construct-x.org/ontology/units#> .
```

Praefixe importierter oder referenzierter Ontologien wie `owl`, `rdf`, `rdfs`, `sh`, `opm`, `qudt`, `schema`, `vcard`, `org`, `locn`, `skos` oder `isoprops` bleiben unveraendert.

Neue Construct-X-Begriffe verwenden:

- Klassen: `UpperCamelCase`, zum Beispiel `PhysicalObject`, `PropertyState` oder `PostalAddress`.
- ObjectProperties: `lowerCamelCase` und als verbale Beziehung formuliert, zum Beispiel `hasAddress`, `hasPropertyReference`, `isPartOf`, `belongsToOrganization` oder `containsElement`.
- DataProperties: `lowerCamelCase`, jedoch ohne Beziehungspraefix wie `has` oder `is`, zum Beispiel `name`, `revisionNumber`, `creationDate` oder `globallyUniqueIdentifier`.
- SHACL-Shapes: Klassenname plus `Shape`, zum Beispiel `AddressShape`.

Lokale Namen enthalten keine Leerzeichen, Umlaute oder sprachabhaengigen Namensbestandteile. Uebersetzungen werden ueber Labels mit Sprach-Tags abgebildet. Diese Regeln gelten nicht rueckwirkend fuer Begriffe importierter Ontologien.

## 6. Versionierungsregeln

Construct-X unterscheidet drei Versionierungsmodelle:

1. Ontologien und SHACL-Graphen werden als vollstaendige Graphen mit SemVer versioniert.
2. Referenzvokabulare werden ebenfalls als vollstaendige Graphen mit SemVer versioniert.
3. Referenzobjekte unter `/id/` besitzen einen individuellen Lebenszyklus aus GUID, fachlicher Version und Revision.

### 6.1 Ontologien und SHACL-Graphen

Fuer Ontologien und SHACL-Graphen gilt:

1. Die stabile Graph-IRI bleibt unveraendert.
2. Jede Veroeffentlichung erhaelt eine SemVer-Versions-IRI.
3. Veroeffentlichte Versionen sind unveraenderlich.
4. Die unversionierte Graph-IRI verweist auf die aktuelle empfohlene Version.
5. Begriffs-IRIs enthalten keine Versionsnummer.
6. Aeltere Veroeffentlichungen bleiben ueber ihre Versions-IRIs erreichbar.
7. Interne Release-Imports verwenden konkrete Versions-IRIs.
8. Eine Import-Closure darf nicht mehrere Versionen derselben Ontologie enthalten.
9. Eine neue Major-Version erzeugt nicht automatisch neue Begriffs-IRIs.
10. Aendert sich die fachliche Identitaet eines Begriffs grundlegend, wird ein neuer Begriff angelegt und der alte Begriff als veraltet gekennzeichnet.
11. Entfernte IRIs duerfen niemals fuer andere Begriffe wiederverwendet werden.

Jeder SHACL-Graph gehoert zu einem benannten `shape-set`. Ein Shape-Set bildet
eine fachlich gemeinsam versionierte Regelmenge, beispielsweise `core`,
`delivery`, `invoice` oder `construction-site`. Unterschiedliche Shape-Sets
duerfen unabhaengige Versionsstaende besitzen. Shape-IRIs liegen im stabilen
Hash-Namespace ihres Shape-Sets und enthalten keine Versionsnummer.

Beispiel:

```text
Stabiler Shape-Graph: https://www.construct-x.org/shapes/address/core
Konkrete Version:     https://www.construct-x.org/shapes/address/core/0.1.0
Stabiles Shape:       https://www.construct-x.org/shapes/address/core#AddressShape
```

Beispiel:

```text
Stabile Ontologie-IRI:
https://www.construct-x.org/ontology/address

Konkrete Version:
https://www.construct-x.org/ontology/address/0.1.0

Stabiler Begriff:
https://www.construct-x.org/ontology/address#PostalAddress
```

### 6.2 Referenzvokabulare

Referenzvokabulare folgen demselben graphbezogenen Veroeffentlichungsmodell wie Ontologien, verwenden aber den Pfad `/vocab/`.

Regeln:

1. Jedes Referenzvokabular besitzt eine stabile Graph-IRI.
2. Jede Veroeffentlichung erhaelt eine SemVer-Versions-IRI.
3. Veroeffentlichte Versionen sind unveraenderlich.
4. Die stabile Vokabular-IRI liefert die aktuell empfohlene Veroeffentlichung.
5. Die IRIs der enthaltenen Begriffe bleiben versionsunabhaengig.
6. Redaktionelle Korrekturen ohne semantische Aenderung erzeugen eine Patch-Version.
7. Rueckwaertskompatible Ergaenzungen erzeugen eine Minor-Version.
8. Inkompatible strukturelle oder semantische Aenderungen erzeugen eine Major-Version.
9. Begriffe werden moeglichst nicht geloescht, sondern als veraltet gekennzeichnet.
10. Entfernte Begriffs-IRIs duerfen niemals neu vergeben werden.

Beispiel:

```text
Stabile Vokabular-IRI:
https://www.construct-x.org/vocab/wall-type

Konkrete Version:
https://www.construct-x.org/vocab/wall-type/1.2.0

Stabiler Begriff:
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

| Aenderung am Vokabular | Versionsaenderung |
| --- | --- |
| Tippfehler in einem Label korrigiert | `1.0.0` -> `1.0.1` |
| neuer Wandtyp ergaenzt | `1.0.0` -> `1.1.0` |
| inkompatible Aenderung der Begriffshierarchie | `1.0.0` -> `2.0.0` |

Eine neue Vokabularversion erzeugt nicht automatisch neue IRIs fuer alle Begriffe. Wenn `ExternalWall` fachlich unveraendert bleibt, bleibt auch `https://www.construct-x.org/vocab/wall-type#ExternalWall` unveraendert.

### 6.3 Referenzobjekte

Referenzobjekte werden individuell versioniert und verwenden ausdruecklich kein SemVer. Der Lebenszyklus beruht auf GUID und Revision.

Regeln:

1. Referenzobjekte werden individuell und nicht mit SemVer versioniert.
2. Eine fachliche Version besitzt eine GUID.
3. Eine Revision behaelt die GUID und erhoeht die Revisionsnummer.
4. Eine neue fachliche Version erhaelt eine neue GUID.
5. Die neue Version verweist auf die ersetzte Version.
6. Veroeffentlichte Revisionen sind unveraenderlich.
7. Fruehere Versionen und Revisionen bleiben erreichbar.
8. Normative und reproduzierbare Referenzen verwenden GUID und Revisionsnummer.
9. GUIDs und Revisions-IRIs duerfen niemals neu vergeben werden.
10. Fragmentierung und Zusammenfuehrung erzeugen neue GUIDs und dokumentierte Herkunfts- beziehungsweise Ersetzungsbeziehungen.

Die SemVer-Version eines veroeffentlichten Graphen und die Revision eines darin beschriebenen Referenzobjekts sind voneinander unabhaengige Angaben.

Beispiel: Ein Property-Dictionary kann als Graph `https://www.construct-x.org/vocab/property-dictionary/1.3.0` veroeffentlicht werden. Darin kann ein einzelnes Property-Referenzobjekt trotzdem die Revisions-IRI `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2` besitzen. Die Graphversion `1.3.0` und die Objektrevision `2` beschreiben unterschiedliche Dinge.

## 7. Repository-Struktur und oeffentliche IRIs

Repository-Kategorien strukturieren die Arbeit im Monorepo. Sie sind keine oeffentlichen IRI-Segmente.

Beispiele:

```text
Repository:
modules/core/address

Oeffentliche Ontologie:
https://www.construct-x.org/ontology/address

Repository:
modules/core/document

Oeffentliche Ontologie:
https://www.construct-x.org/ontology/document
```

## 8. Dereferenzierung und Auslieferung

Construct-X-IRIs sollen dereferenzierbar sein. Je nach angefragtem Format koennen RDF, HTML-Dokumentation oder andere Darstellungen ausgeliefert werden. Fuer nicht-informationsressourcen kann `303 See Other` verwendet werden. Content Negotiation soll maschinenlesbare und menschenlesbare Darstellungen unterstuetzen.

### 8.1 Ontologien

```text
GET https://www.construct-x.org/ontology/vso
```

Diese IRI kann auf die aktuelle empfohlene Ontologieversion verweisen oder diese ausliefern.

### 8.2 Ontologieversionen

```text
GET https://www.construct-x.org/ontology/vso/0.1.0
```

Diese IRI liefert dauerhaft den unveraenderlichen Stand der Version `0.1.0`.

### 8.3 Referenzvokabulare

```text
GET https://www.construct-x.org/vocab/wall-type
```

Diese IRI kann die aktuelle empfohlene Vokabularveroeffentlichung liefern.

```text
GET https://www.construct-x.org/vocab/wall-type/1.2.0
```

Diese IRI liefert dauerhaft den unveraenderlichen Stand der Vokabularversion `1.2.0`.

### 8.4 Persistente ID-Ressourcen

```text
GET https://www.construct-x.org/id/property/{guid}
```

Diese IRI repraesentiert die fachliche Version des Referenzobjekts und kann auf ihre aktuelle Revision verweisen.

```text
GET https://www.construct-x.org/id/property/{guid}/revision/2
```

Diese IRI liefert dauerhaft den unveraenderlichen Stand der Revision `2`.

Da sich die ueber die Basis-IRI ausgelieferte Beschreibung bei einer neuen Revision aendern kann, ist sie nicht fuer reproduzierbare Pruefungen oder normative Referenzen ausreichend. Dafuer wird immer die revisionsgebundene IRI verwendet.

Beispiel: Eine Validierungsregel, die nachweisen soll, welche Property-Definition am 2026-08-18 verwendet wurde, referenziert `https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2` statt nur die Basis-IRI ohne Revisionssegment.

## 9. Katalog nach QUDT-Vorbild

Der zentrale Artefaktkatalog beschreibt Graphveroeffentlichungen. Einzelne Referenzobjekte koennen zusaetzlich ueber eigene Registries oder ihre RDF-Beschreibungen verwaltet werden.

Fuer Ontologie- und SHACL-Veroeffentlichungen dokumentiert der Katalog mindestens:

- stabile Graph-IRI;
- aktuelle Versions-IRI;
- SemVer;
- Begriffs- oder Shape-Namespace;
- vorherige Veroeffentlichung;
- Veroeffentlichungsdatum;
- Status;
- Dokumentations- und Downloadlinks.

Fuer Vokabularveroeffentlichungen dokumentiert der Katalog mindestens:

- stabile Vokabular-IRI;
- aktuelle Versions-IRI;
- SemVer;
- Begriffsnamespace;
- vorherige Veroeffentlichung;
- Veroeffentlichungsdatum;
- Status;
- Dokumentations- und Downloadlinks.

Beispiel fuer einen Katalogeintrag:

```yaml
id: wall-type
kind: vocabulary
stable_iri: https://www.construct-x.org/vocab/wall-type
version_iri: https://www.construct-x.org/vocab/wall-type/1.2.0
version: 1.2.0
namespace: https://www.construct-x.org/vocab/wall-type#
previous_version_iri: https://www.construct-x.org/vocab/wall-type/1.1.0
status: released
published: 2026-08-18
```

Fuer Referenzobjekte beziehungsweise deren Registry werden mindestens dokumentiert:

- Typ des Referenzobjekts;
- GUID;
- aktuelle Revisionsnummer;
- IRI der aktuellen Revision;
- ersetzte beziehungsweise ersetzende Version;
- Status;
- Veroeffentlichungs- und Aenderungsdatum.

Beispiel fuer einen Registry-Eintrag:

```yaml
type: property
guid: 550e8400-e29b-41d4-a716-446655440000
current_revision: 2
current_revision_iri: https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
replaces: null
replaced_by: https://www.construct-x.org/id/property/a471c218-1234-5678-9012-abcdefabcdef/revision/1
status: released
published: 2026-08-18
modified: 2026-08-18
```

## 10. Beispiele aktueller Module

### 10.1 VSO

```text
Ontologie-IRI:  https://www.construct-x.org/ontology/vso
Namespace:      https://www.construct-x.org/ontology/vso#
Versions-IRI:   https://www.construct-x.org/ontology/vso/0.1.0
Praefix:        conx-vso
Repository:     modules/core/vso/ontology/conx-vso.ttl
```

### 10.2 Address

```text
Ontologie-IRI:  https://www.construct-x.org/ontology/address
Namespace:      https://www.construct-x.org/ontology/address#
Versions-IRI:   https://www.construct-x.org/ontology/address/0.1.0
Praefix:        conx-addr
Repository:     modules/core/address/ontology/conx-addr.ttl
```

## 11. Technische und organisatorische Pruefregeln

CI und Reviews sollen mindestens folgende Regeln pruefen:

- Ontologie-IRI und Versions-IRI entsprechen dem festgelegten Muster.
- SHACL-IRI, Shape-Set, Shape-Namespace und SHACL-Versions-IRI entsprechen dem festgelegten Muster.
- Vokabular-IRI und Versions-IRI entsprechen dem festgelegten Muster.
- SemVer im Ontologie-, Shape- oder Vokabularpfad stimmt mit den Versionsmetadaten ueberein.
- stabile Ontologiebegriffe enthalten keine Versionsnummer.
- stabile Vokabularbegriffe enthalten keine Versionsnummer.
- veroeffentlichte Ontologie-, SHACL- und Vokabularversionen wurden nicht nachtraeglich veraendert.
- Revisions-IRI, GUID und Revisionsnummer eines Referenzobjekts stimmen ueberein.
- innerhalb einer GUID wird eine Revisionsnummer nur einmal vergeben.
- eine neue fachliche Version besitzt eine neue GUID.
- ersetzte und ersetzende Versionen verwenden unterschiedliche GUIDs.
- fruehere Revisions-IRIs bleiben erreichbar.
- normative Referenzen auf Referenzobjekte enthalten GUID und Revision.
- Repository-Kategorien wie `core`, `domain` und `alignments` kommen nicht in oeffentlichen Ontologie-IRIs vor.
- Construct-X-Praefixe folgen dem Muster `conx-{modulkuerzel}`.

Verstaendliches Fehlerbeispiel:

```text
Falsch:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000
```

Diese IRI kann fuer die aktuelle Revision stehen. Sie reicht aber nicht fuer eine normative oder reproduzierbare Referenz, weil sich die ausgelieferte Beschreibung bei einer neuen Revision aendern kann.

```text
Richtig:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Weiteres Fehlerbeispiel:

```text
Falsch:
https://www.construct-x.org/vocab/wall-type/1.2.0#ExternalWall
```

Der Begriff enthaelt eine Versionsnummer im Pfad. Richtig ist der stabile Begriffsnamespace:

```text
https://www.construct-x.org/vocab/wall-type#ExternalWall
```

## 12. Festgestellte Abweichungen und Anpassungen

Analysierter Stand vor frueherer Umstellung der VSO:

- VSO-Ontologie-IRI: `https://www.construct-x.org/ontology/value-semantics`
- VSO-Namespace: `https://www.construct-x.org/ontology/value-semantics#`
- VSO-Version-IRI: `https://www.construct-x.org/ontology/value-semantics/0.1.0`
- Repository-Pfad: `modules/core/value-semantics/ontology/conx-vso.ttl`

Technische Anpassung:

- Oeffentliches Modulsegment von `value-semantics` auf `vso` umgestellt.
- Repository-Modulordner von `modules/core/value-semantics` auf `modules/core/vso` umgestellt.
- Praefix `conx-vso` beibehalten, da er der Konvention entspricht.
- Fachliche Klassen, Properties und Axiome wurden nicht umbenannt.

Offene Entscheidung:

- Vor dem ersten stabilen Release muss bestaetigt werden, dass `https://www.construct-x.org` dauerhaft als kanonische Authority verwendet wird.

## 13. Verbindliche Empfehlung

```text
Ontologien:          https://www.construct-x.org/ontology/{modul}
Ontologieversionen:  https://www.construct-x.org/ontology/{modul}/{semver}
Ontologiebegriffe:   https://www.construct-x.org/ontology/{modul}#{localName}

Vokabulare:          https://www.construct-x.org/vocab/{vokabular}
Vokabularversionen:  https://www.construct-x.org/vocab/{vokabular}/{semver}
Vokabularbegriffe:   https://www.construct-x.org/vocab/{vokabular}#{localName}

Referenzobjekte:     https://www.construct-x.org/id/{typ}/{guid}
Exakte Revisionen:   https://www.construct-x.org/id/{typ}/{guid}/revision/{revision}

SHACL:               https://www.construct-x.org/shapes/{modul}/{shape-set}
Alignments:          https://www.construct-x.org/alignment/{alignment}
Katalog:             https://www.construct-x.org/catalog
Dokumentation:       https://www.construct-x.org/docs/{modul}
```

Ontologien und Referenzvokabulare folgen demselben graphbezogenen Veroeffentlichungsmodell. Referenzobjekte folgen dagegen einem individuellen, auf GUID und Revision basierenden Lebenszyklusmodell.
