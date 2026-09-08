# Begriffskatalog für den Personen-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

## 1. Zweck

Dieser Katalog übersetzt den bestätigten Scope und die Quellenanalyse in konkrete Begriffe. Er beschreibt für jeden Begriff Name, Definition, Modulzuständigkeit, Domain, Range, Kardinalität, Verbindlichkeit, Quelle, Alignment, Beispiel und Datenschutzrelevanz.

Die Angaben bilden die fachliche Grundlage der implementierten T-Box und Core Shapes. Die konkreten Shape-Regeln stehen im [SHACL-Anforderungsprofil](shacl-requirements.md) und sind unter `shapes/conx-person-core.shacl.ttl` maschinenlesbar umgesetzt.

## 2. Namensräume

### Personenontologie

```text
Ontologie-IRI: https://www.construct-x.org/ontology/person
Versions-IRI:  https://www.construct-x.org/ontology/person/0.1.0
Namespace:     https://www.construct-x.org/ontology/person#
Prefix:        conx-person
```

### Agent-Ontologie

```text
Ontologie-IRI: https://www.construct-x.org/ontology/agent
Versions-IRI:  https://www.construct-x.org/ontology/agent/0.1.0
Namespace:     https://www.construct-x.org/ontology/agent#
Prefix:        conx-agent
```

### Referenzvokabular für menschliches Geschlecht

```text
Vokabular-IRI: https://www.construct-x.org/vocab/human-sex
Versions-IRI:  https://www.construct-x.org/vocab/human-sex/0.1.0
Namespace:     https://www.construct-x.org/vocab/human-sex#
Prefix:        human-sex
```

### Referenzvokabular für Gender

```text
Vokabular-IRI: https://www.construct-x.org/vocab/gender
Versions-IRI:  https://www.construct-x.org/vocab/gender/0.1.0
Namespace:     https://www.construct-x.org/vocab/gender#
Prefix:        gender
```

Die Version `0.1.0` ist in den Modul- und Vokabularmetadaten festgelegt.

## 3. Modellierungsregeln

- OWL beschreibt Bedeutung, Vererbung, Domain und Range möglichst offen.
- Das Core-SHACL-Profil beschreibt Pflichtfelder, maximale Kardinalitäten und zugelassene Wertemengen.
- Ein fehlender optionaler Wert ist keine negative Aussage und kein Ersatzcode.
- Mehrsprachige oder in mehreren Schriftsystemen geführte Namen dürfen mehrere Literalwerte besitzen.
- Kontrollierte Wertemengen werden als getrennt versionierte A-Box-Vokabulare gepflegt.
- Personeninstanzen erhalten IRIs im Namespace des jeweiligen Datenhalters, nicht im Construct-X-Ontologienamespace.

## 4. Klassen

### 4.1 `conx-agent:Agent`

| Punkt | Festlegung |
| --- | --- |
| Definition | Akteur, der in einem fachlichen Kontext handeln, Verantwortung tragen oder Herausgeber beziehungsweise Beteiligter sein kann |
| Modul | `modules/core/agent` |
| Oberklasse | Keine lokale Oberklasse im MVP |
| Unterklassen | zunächst `conx-person:Person`; später `conx-org:Organization` |
| Verbindlichkeit | Abstrakter gemeinsamer Typ; keine Pflichtattribute |
| Quelle | FOAF Agent, SEMIC Agent, W3C ORG |
| Alignment | `rdfs:subClassOf foaf:Agent` empfohlen; keine ungeprüfte Äquivalenz |
| Datenschutz | Keine unmittelbaren personenbezogenen Werte; konkrete Unterklassen können personenbezogen sein |

Beispiel:

```turtle
ex:person-123 a conx-person:Person, conx-agent:Agent .
```

Die ausführliche Festlegung steht in der [Agent-Spezifikation](../../agent/docs/agent-specification.md).

### 4.2 `conx-person:Person`

| Punkt | Festlegung |
| --- | --- |
| Definition | Reale natürliche Person, lebend oder verstorben |
| Modul | `modules/core/person` |
| Oberklasse | `conx-agent:Agent` |
| Ausschlüsse | Fiktive Personen, Organisationen, Softwaredienste und Rollen |
| Verbindlichkeit | Instanzen verwenden das Personen-Core-Shape |
| Quelle | SEMIC Core Person als Hauptquelle |
| Alignment | `rdfs:subClassOf foaf:Person`; Alignment zu `schema:Person` prüfen, aber wegen dessen weiterem Scope keine Äquivalenz empfehlen |
| Datenschutz | Die Instanz ist personenbezogen; Zugriff und Veröffentlichung werden außerhalb der T-Box geregelt |

Beispiel:

```turtle
ex:person-123 a conx-person:Person .
```

## 5. Namensbegriffe

### 5.1 `conx-person:fullName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Vollständiger, direkt ausgebbarer Name einer Person in einer gewünschten Schreibweise |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | OWL ohne Maximum; Core SHACL mindestens `1` |
| Verbindlichkeit | Verpflichtend |
| Quelle | SEMIC `fullName`, vCard `fn`, Schema.org `name` |
| Alignment | SEMIC `fullName`; `rdfs:subPropertyOf schema:name` prüfen |
| Datenschutz | Direkt identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:fullName "Dr. Maria Anna Beispiel"@de .
```

### 5.2 `conx-person:givenName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Primärer Vorname oder die als primäre Vornamen geführte Namensfolge einer Person |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | OWL ohne Maximum; Core SHACL mindestens `1` |
| Verbindlichkeit | Verpflichtend |
| Quelle | SEMIC `givenName`, UBL `FirstName`, Schema.org und vCard |
| Alignment | `schema:givenName`, vCard `given-name`, SEMIC `givenName` |
| Datenschutz | Direkt identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:givenName "Maria" .
```

### 5.3 `conx-person:familyName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Familien- oder Nachname einer Person |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optionales Kernfeld; empfohlen, wenn vorhanden |
| Quelle | SEMIC `familyName`, UBL `FamilyName`, Schema.org und vCard |
| Alignment | `schema:familyName`, vCard `family-name`, SEMIC `familyName` |
| Datenschutz | Direkt identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:familyName "Beispiel" .
```

Die optionale Kardinalität berücksichtigt Personen ohne Familiennamen. Ein konkretes Anwendungsprofil darf das Feld verpflichtend machen, wenn sein Rechts- oder Prozesskontext dies verlangt.

### 5.4 `conx-person:additionalName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Weiterer Vorname, Zweitname oder zusätzliche Vornamenskomponente |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optional |
| Quelle | Schema.org `additionalName`, vCard `additional-name`, UBL `MiddleName` |
| Alignment | `schema:additionalName`; UBL-Mapping dokumentieren |
| Datenschutz | Direkt identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:additionalName "Anna" .
```

### 5.5 `conx-person:birthName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Vollständiger Name, der für die Person bei der Geburt geführt wurde |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optional |
| Quelle | SEMIC `birthName` |
| Alignment | SEMIC `birthName`; kein erzwungenes Schema.org-Alignment |
| Datenschutz | Direkt identifizierend und historisch; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:birthName "Maria Anna Altname" .
```

Der Begriff ersetzt keine allgemeine Namenshistorie und enthält keinen Zeitraum.

## 6. Geburtsdaten

### 6.1 `conx-person:birthDate`

| Punkt | Festlegung |
| --- | --- |
| Definition | Vollständiges Kalenderdatum der Geburt einer Person |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | ausschließlich `xsd:date` |
| Kardinalität | `0..1` |
| Verbindlichkeit | Optional, aber Bestandteil des MVP |
| Quelle | SEMIC `dateOfBirth`, UBL `BirthDate`, Schema.org `birthDate` |
| Alignment | `schema:birthDate`; SEMIC-Alignment mit engerem lokalen Datentyp |
| Datenschutz | Stark identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:birthDate "1985-04-23"^^xsd:date .
```

`xsd:gYear` und `xsd:gYearMonth` sind im MVP nicht zulässig.

### 6.2 `conx-person:birthPlaceName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Textuelle Bezeichnung des Geburtsortes einer Person |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | `xsd:string` oder `rdf:langString` |
| Kardinalität | `0..1` |
| Verbindlichkeit | Optional |
| Quelle | UBL `BirthplaceName` |
| Alignment | UBL-Mapping; kein direktes Alignment zu objektwertigen Orts-Properties |
| Datenschutz | Zusammen mit Name und Datum stark identifizierend; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:birthPlaceName "Bochum"@de .
```

## 7. Geschlechtsangaben

### 7.1 `conx-person:sex`

| Punkt | Festlegung |
| --- | --- |
| Definition | Für den Informationsaustausch geführte Klassifikation des menschlichen Geschlechts gemäß ISO/IEC 5218:2022 |
| Modul | Property in `core/person`; Werte in getrenntem Referenzvokabular |
| Domain | `conx-person:Person` |
| Range | `skos:Concept` aus `https://www.construct-x.org/vocab/human-sex` |
| Kardinalität | `0..1` |
| Verbindlichkeit | Optional |
| Quelle | ISO/IEC 5218:2022, SEMIC `sex`, EU Authority Table `human-sex` |
| Alignment | SEMIC `sex`; Wert-Alignment zur EU-Tabelle vor Implementierung prüfen |
| Datenschutz | Sensibles personenbezogenes Merkmal; sehr hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:sex human-sex:female .
```

### 7.2 `conx-person:gender`

| Punkt | Festlegung |
| --- | --- |
| Definition | Geschlechtsidentität, Ausdruck oder soziale beziehungsweise rechtliche Einordnung im jeweiligen Anwendungskontext |
| Modul | Property in `core/person`; Werte in getrenntem Referenzvokabular |
| Domain | `conx-person:Person` |
| Range | `skos:Concept` aus `https://www.construct-x.org/vocab/gender` |
| Kardinalität | `0..1` |
| Verbindlichkeit | Optional |
| Quelle | SEMIC `gender`; Schema.org als breite Alignment-Quelle |
| Alignment | Externe Werte erst nach Einzelprüfung ausrichten |
| Datenschutz | Sensibles personenbezogenes Merkmal; sehr hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:gender gender:woman .
```

## 8. `human-sex`-Referenzvokabular

| Lokaler Begriff | ISO/IEC-5218-Code | Deutsche Bezeichnung | Englische Bezeichnung | Verwendung |
| --- | --- | --- | --- | --- |
| `human-sex:notKnown` | `0` | Nicht bekannt | Not known | Wert wurde ausdrücklich als unbekannt übermittelt |
| `human-sex:male` | `1` | Männlich | Male | Klassifikationswert für den Datenaustausch |
| `human-sex:female` | `2` | Weiblich | Female | Klassifikationswert für den Datenaustausch |
| `human-sex:notApplicable` | `9` | Nicht anwendbar | Not applicable | Nur quellengetreu; nicht als weitere Genderkategorie verwenden |

Umgesetztes RDF-Muster:

- ein eigenes `skos:ConceptScheme`,
- ein `skos:Concept` je Code,
- numerischer Code als `skos:notation` mit einem eindeutig benannten ISO/IEC-5218-Datentyp,
- deutsche und englische `skos:prefLabel`,
- `skos:exactMatch` oder `skos:closeMatch` zu EU-Ressourcen erst nach Einzelprüfung,
- unabhängige Versionierung von der Personen-T-Box.

Code `0` und das Fehlen von `conx-person:sex` haben verschiedene Bedeutungen:

```text
keine Property     = keine Aussage im Datensatz
Code 0             = ausdrücklich übermittelter Wert „nicht bekannt“
```

## 9. Gender-Referenzvokabular

| Lokaler Begriff | Deutsche Bezeichnung | Englische Bezeichnung | Semantik |
| --- | --- | --- | --- |
| `gender:man` | Mann | Man | Die Person identifiziert sich als Mann |
| `gender:woman` | Frau | Woman | Die Person identifiziert sich als Frau |
| `gender:nonBinaryOrDiverse` | Nicht-binär oder divers | Non-binary or gender-diverse | Vorläufiger erweiterbarer Sammelbegriff außerhalb der binären Werte |
| `gender:notDisclosed` | Keine Angabe | Not disclosed | Die Person hat ausdrücklich entschieden, keine Genderangabe offenzulegen |

`gender:notDisclosed` ist keine Genderidentität. Der Wert wird im ersten Profil dennoch als zulässige Antwort auf dieselbe Property geführt, damit eine ausdrückliche Nichtoffenlegung von einer fehlenden Aussage unterschieden werden kann:

```text
keine Property             = im Datensatz liegt keine Aussage vor
gender:notDisclosed        = die Person möchte keine Angabe offenlegen
```

`gender:nonBinaryOrDiverse` ist bewusst ein breiter Startbegriff. Spätere präzisere Identitäten können als eigene Konzepte ergänzt und mit `skos:broader gender:nonBinaryOrDiverse` eingeordnet werden. „Other“ wird nicht als bevorzugte Bezeichnung verwendet, weil es keine fachlich aussagekräftige Identität bezeichnet; es kann bei Quellmappings als Ausgangswert dokumentiert werden.

## 10. Staatsangehörigkeit

### 10.1 `conx-person:citizenship`

| Punkt | Festlegung |
| --- | --- |
| Definition | Rechtliche Zugehörigkeit einer Person zu einem Staat |
| Modul | Property in `core/person`; Werte im vorhandenen Länder-Referenzdatensatz |
| Domain | `conx-person:Person` |
| Range | `conx-addr:Country` aus dem ISO-3166-1-Ländervokabular |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optional |
| Quelle | SEMIC `citizenship`, UBL `CitizenshipCountry`, Schema.org `nationality` |
| Alignment | SEMIC und Schema.org prüfen |
| Datenschutz | Personenbezogen und je nach Kontext sensibel; hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123
    conx-person:citizenship <https://www.construct-x.org/vocab/country#DEU> .
```

Staatenlosigkeit wird im MVP nicht modelliert. Aus dem Fehlen der Property darf sie nicht abgeleitet werden.

## 11. Identifikatoren

### 11.1 Wiederverwendung von `adms:identifier`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft die Person mit einem strukturierten fachlichen Identifikator |
| Modul | Externer ADMS-Begriff gemäß Construct-X-Identifier-Modell; keine lokale Ersatzproperty |
| Domain | Im lokalen Shape auf `conx-person:Person` angewendet |
| Range | `adms:Identifier` |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optional |
| Quelle | ADMS 2.0 und Construct-X-Identifier-Modell |
| Alignment | Direkte Wiederverwendung |
| Datenschutz | Häufig stark oder eindeutig identifizierend; sehr hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 adms:identifier [
    a adms:Identifier ;
    skos:notation "P-4711"^^id-scheme:project-person-id ;
    adms:schemaAgency "Beispielorganisation"
] .
```

Konkrete Identifikatorschemata werden erst nach der internen Projektklärung angelegt.

## 12. Identitätsnachweise

### 12.1 `conx-person:hasIdentityEvidence`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine Person mit einer externen Ressource, die Aussagen zu ihrer Identität belegt oder überprüfbar macht |
| Modul | `core/person` |
| Domain | `conx-person:Person` |
| Range | referenzierbare externe Ressource mit IRI; spätere Identitätsmodule dürfen engere Unterklassen definieren |
| Kardinalität | `0..n` |
| Verbindlichkeit | Optional |
| Quelle | UBL `IdentityDocumentReference`, W3C Controlled Identifiers und VC Data Model |
| Alignment | Kein vorschnelles Äquivalenz-Alignment; mögliche Unterproperties im Identitätsmodul |
| Datenschutz | Nachweise können besonders sensible Daten oder Zugriffspfade enthalten; sehr hohe Schutzrelevanz |

Beispiel:

```turtle
ex:person-123 conx-person:hasIdentityEvidence ex:credential-789 .

ex:credential-789 a ex:VerifiableCredential .
```

Mögliche Zielressourcen:

- Ausweisdokumentreferenz,
- Führerscheinreferenz,
- Verifiable Credential,
- behördlicher Registerauszug,
- anderer digital prüfbarer Nachweis.

Die Property behauptet nur eine Nachweisbeziehung. Sie behauptet nicht automatisch Gültigkeit, Vertrauenswürdigkeit oder kryptografische Verifikation. Diese Semantik gehört zum Zielressourcenmodell.

## 13. Begriffe anderer Module

Die folgenden benötigten Beziehungen werden nicht im Personenmodul definiert:

| Bedarf | Zuständiger Begriff beziehungsweise Modul | Begründung |
| --- | --- | --- |
| Kontaktpunkt und Kontaktmethoden | vorhandenes `core/contact` mit ausgehendem `hasContactPoint`, `ContactPoint` und `ContactMethod` | Ohne harte Agent-Domain auch für Projekte, Stellen und weitere Ressourcen wiederverwendbar |
| Melde-, Wohn- und Postadresse | vorhandenes `core/address` mit `AddressAssignment` | Adresssemantik existiert bereits |
| Mitgliedschaft und Beschäftigung | vorhandenes `core/organization` | Rolle, Organisation und Zeitraum bilden eine eigene Beziehung |
| Projektbeteiligung | zuständiges Projektmodul | Projektrolle und Zeitraum gehören zum Projektkontext |
| Nachweisdetails | künftiges Identitäts- oder Credential-Modul | Gültigkeit, Herausgeber, Status, Widerruf und Schlüssel sind eigenständig |
| `issuedBy` und `issuedThrough` | Identifier-/Identitätsarchitektur | Nicht auf Personenidentifikatoren beschränken |

## 14. Implementiertes Core-SHACL-Profil

| Property | Minimum | Maximum | Zusätzliche Regel |
| --- | ---: | ---: | --- |
| `fullName` | 1 | offen | `xsd:string` oder `rdf:langString`; nicht leer |
| `givenName` | 1 | offen | `xsd:string` oder `rdf:langString`; nicht leer |
| `familyName` | 0 | offen | Literal nicht leer |
| `additionalName` | 0 | offen | Literal nicht leer |
| `birthName` | 0 | offen | Literal nicht leer |
| `birthDate` | 0 | 1 | ausschließlich `xsd:date` |
| `birthPlaceName` | 0 | 1 | Literal nicht leer |
| `sex` | 0 | 1 | Wert aus freigegebenem `human-sex`-Scheme |
| `gender` | 0 | 1 | Wert aus dem freigegebenen Gender-Scheme |
| `citizenship` | 0 | offen | Wert aus freigegebenem Ländervokabular |
| `adms:identifier` | 0 | offen | Jeder Wert ist eine `adms:Identifier`-Ressource mit genau einer `skos:notation`; `adms:schemaAgency` ist optional |
| `hasIdentityEvidence` | 0 | offen | IRI; strengere Regeln im Zielmodul |

Die Maximalwerte sind SHACL-Entscheidungen und sollen nicht automatisch als OWL-Kardinalitäten übernommen werden.

## 15. Kompaktes Beispiel des Zielprofils

```turtle
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix human-sex: <https://www.construct-x.org/vocab/human-sex#> .
@prefix gender: <https://www.construct-x.org/vocab/gender#> .
@prefix country: <https://www.construct-x.org/vocab/country#> .
@prefix ex: <https://example.org/id/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:person-123 a conx-person:Person ;
    conx-person:fullName "Maria Anna Beispiel" ;
    conx-person:givenName "Maria" ;
    conx-person:additionalName "Anna" ;
    conx-person:familyName "Beispiel" ;
    conx-person:birthDate "1985-04-23"^^xsd:date ;
    conx-person:birthPlaceName "Bochum" ;
    conx-person:sex human-sex:female ;
    conx-person:gender gender:woman ;
    conx-person:citizenship country:DEU ;
    conx-person:hasIdentityEvidence ex:credential-789 .
```

Das Beispiel erläutert das Zielprofil; Instanzdaten und SHACL-Testfälle sind noch kein Bestandteil dieses T-Box-Releases.

Das vollständige fachliche Zusammenspiel ist im [Personendiagramm](diagrams/person-concept-model.md) dargestellt.

## 16. Noch nicht finalisierte Begriffe

| Thema | Grund für die Zurückstellung |
| --- | --- |
| Erweiterung des Gender-Wertevokabulars | Feinere nicht-binäre beziehungsweise genderdiverse Konzepte und Governance werden später ergänzt |
| `issuedBy` und `issuedThrough` | Eigentümerschaft zwischen generischem Identifier- und Identitätsmodell ist noch offen |
| Kontaktbegriffe und Kontaktrollen | Werden im separaten Kontaktmodul spezifiziert |
| Organisations- und Projektbeziehungen | Werden von den jeweiligen Modulen besessen |
| Staatenlosigkeitsstatus | Für den MVP ausdrücklich zurückgestellt |
