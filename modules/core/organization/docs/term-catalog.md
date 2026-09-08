# Begriffskatalog für den Organisations-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`  
**Umsetzungsstand:** T-Box und Core Shapes 0.1.0 implementiert

## 1. Zweck

Dieser Katalog übersetzt den bestätigten Scope und die Quellenanalyse in
konkrete Begriffe. Er beschreibt lokale Klassen und Properties sowie die
Wiederverwendung bestehender Construct-X-Module und externer Vokabulare.

Kardinalitäten mit dem Hinweis „Core SHACL“ sind im
[SHACL-Anforderungsdokument](shacl-requirements.md) beschrieben und im
ausführbaren Core-Shape umgesetzt. Sie werden bewusst nicht als harte
OWL-Kardinalitäten modelliert.

Grundlagen:

- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Quellenanalyse](source-analysis.md)
- [Agent-Spezifikation](../../agent/docs/agent-specification.md)
- [Kennungsmodell](../../../../docs/architecture/identifier-model.md)
- [Adressrollen](../../address/docs/address-roles.md)
- [Kontakt-Termkatalog](../../contact/docs/term-catalog.md)

## 2. Namensraum

```text
Ontologie-IRI: https://www.construct-x.org/ontology/organization
Versions-IRI:  https://www.construct-x.org/ontology/organization/0.1.0
Namespace:     https://www.construct-x.org/ontology/organization#
Prefix:        conx-org
```

Die IRIs sind durch Modulmetadaten und T-Box 0.1.0 festgelegt.

Wiederverwendete Namespaces:

```text
conx-agent:   https://www.construct-x.org/ontology/agent#
conx-person:  https://www.construct-x.org/ontology/person#
conx-addr:    https://www.construct-x.org/ontology/address#
conx-contact: https://www.construct-x.org/ontology/contact#
adms:         http://www.w3.org/ns/adms#
skos:         http://www.w3.org/2004/02/skos/core#
```

## 3. Modellierungsregeln

1. `Organization` ist eine Unterklasse von `conx-agent:Agent`.
2. `LegalEntity` und `OrganizationalUnit` sind Spezialisierungen von
   `Organization`.
3. Es gibt im MVP keine lokalen Klassen `EconomicActor`, `Enterprise`,
   `FormalOrganization` oder `Post`.
4. Einzelunternehmen und Freiberufler bleiben `conx-person:Person` und handeln
   über kontextuelle Agentenrollen.
5. Mitgliedschaft und rechtliche Vertretung werden als eigenständige
   Beziehungsressourcen modelliert.
6. OWL beschreibt Bedeutung, Domain, Range, Unterklassen und inverse
   Beziehungen möglichst offen.
7. SHACL übernimmt Mindestwerte, Maximalwerte, Datentypen und geschlossene
   Profilregeln.
8. Fachliche Kennungen verwenden ausschließlich `adms:Identifier`; es wird
   keine lokale Identifier-Klasse eingeführt.
9. Adresse und Kontakt werden über die bereits vorhandenen domänenoffenen
   Zuordnungsproperties angebunden.
10. Jurisdiktionsspezifische Kennungs-, Rechtsform- und Registerregeln gehören
    nicht in Version 0.1.0.
11. Organisations-, Einheits-, Mitgliedschafts- und Vertretungsinstanzen
    erhalten IRIs im Namensraum des jeweiligen Datenhalters.

## 4. Begriffsübersicht

### 4.1 Klassen

| Lokaler Begriff | Oberklasse | MVP |
| --- | --- | --- |
| `conx-org:Organization` | `conx-agent:Agent` | Ja |
| `conx-org:LegalEntity` | `conx-org:Organization` | Ja |
| `conx-org:OrganizationalUnit` | `conx-org:Organization` | Ja |
| `conx-org:Membership` | keine lokale Oberklasse | Ja |
| `conx-org:LegalRepresentation` | keine lokale Oberklasse | Ja |

### 4.2 Lokale Properties

| Property | Domain | Range | Core SHACL 0.1.0 |
| --- | --- | --- | --- |
| `conx-org:name` | `Organization` | `xsd:string` oder `rdf:langString` | `1..n` |
| `conx-org:legalName` | `LegalEntity` | `xsd:string` oder `rdf:langString` | `1..n` |
| `conx-org:alternativeName` | `Organization` | `xsd:string` oder `rdf:langString` | `0..n` |
| `conx-org:legalForm` | `LegalEntity` | `skos:Concept` | `0..1` |
| `conx-org:registrationDate` | `LegalEntity` | `xsd:date` | `1` |
| `conx-org:activity` | `Organization` | `skos:Concept` | `0..n` |
| `conx-org:subOrganizationOf` | `Organization` | `Organization` | `0..n` |
| `conx-org:hasSubOrganization` | `Organization` | `Organization` | `0..n` |
| `conx-org:unitOf` | `OrganizationalUnit` | `Organization` | `1..n` |
| `conx-org:hasUnit` | `Organization` | `OrganizationalUnit` | `0..n` |
| `conx-org:member` | `Membership` | `conx-agent:Agent` | `1` |
| `conx-org:membershipOrganization` | `Membership` | `Organization` | `1` |
| `conx-org:representedOrganization` | `LegalRepresentation` | `LegalEntity` | `1` |
| `conx-org:representative` | `LegalRepresentation` | `conx-person:Person` | `1` |

### 4.3 Wiederverwendete Properties

| Property | Verwendung |
| --- | --- |
| `adms:identifier` | Kennungen von Organisation, Legal Entity, Organisationseinheit oder Mitgliedschaft |
| `conx-addr:hasAddressAssignment` | rechtliche, registrierte, Hauptsitz- oder postalische Adresszuordnung |
| `conx-contact:hasContactPoint` | allgemeine, offizielle und funktionsbezogene Kontaktpunkte einschließlich Homepage |

## 5. Klassen

### 5.1 `conx-org:Organization`

| Punkt | Festlegung |
| --- | --- |
| Definition | Organisierter kollektiver Akteur mit einem gemeinsamen Zweck oder einer dauerhaft erkennbaren Struktur |
| Oberklasse | `conx-agent:Agent` |
| Unterklassen im MVP | `conx-org:LegalEntity`, `conx-org:OrganizationalUnit` |
| Kernanforderung | mindestens ein `conx-org:name` |
| Ausschlüsse | bloßer Standort, Projekt, einzelne Person und kontextuelle Geschäftsrolle |
| Primäre Quelle | W3C Organization Ontology |
| Alignment | `rdfs:subClassOf org:Organization` als konservativer Kandidat; keine Äquivalenz ohne Einzelprüfung |
| Instanziierung | Unternehmen, Behörde, Verband, Arbeitsgemeinschaft oder Organisationsverbund, soweit der lokale Scope erfüllt ist |

Beispiel:

```turtle
ex:bauverband
    a conx-org:Organization ;
    conx-org:name "Bauverband Beispielregion"@de .
```

`Organization` behauptet weder eine eigene Rechtspersönlichkeit noch eine
bestimmte Rechtsform oder wirtschaftliche Tätigkeit.

### 5.2 `conx-org:LegalEntity`

| Punkt | Festlegung |
| --- | --- |
| Definition | Organisation mit eigenständiger rechtlicher Identität, die im relevanten Rechtsraum als Träger von Rechten und Pflichten behandelt wird |
| Oberklasse | `conx-org:Organization` |
| Kernanforderungen | `name`, `legalName`, `registrationDate`; mindestens eine strukturierte ADMS-Kennung wird durch das Core Shape geprüft |
| Primäre Quellen | SEMIC Core Business Vocabulary, Gaia-X LegalPerson, GLEIF |
| Alignment | Ausrichtung zu SEMIC `LegalEntity`, W3C `org:FormalOrganization` und Gaia-X `LegalPerson` prüfen; keine pauschale Äquivalenz |
| Ausschlüsse | Abteilungen, bloße Standorte sowie selbständig tätige Personen ohne getrennt modellierte rechtliche Organisation |

Beispiel:

```turtle
ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date .
```

Die lokale Klasse ist bewusst organisationsbezogen. Sie darf daher nicht
ungeprüft mit einem externen Begriff gleichgesetzt werden, der auch
selbständige natürliche Personen einschließt.

### 5.3 `conx-org:OrganizationalUnit`

| Punkt | Festlegung |
| --- | --- |
| Definition | Organisatorischer Teil einer oder mehrerer übergeordneter Organisationen mit eigener Funktion oder Zuständigkeit, aber ohne daraus abgeleitete eigene Rechtspersönlichkeit |
| Oberklasse | `conx-org:Organization` |
| Kernanforderungen | `name` und mindestens ein `unitOf` |
| Primäre Quelle | W3C Organization Ontology `org:OrganizationalUnit` |
| Alignment | `rdfs:subClassOf org:OrganizationalUnit` als Kandidat |
| Beispiele | Abteilung, Geschäftsbereich, Niederlassung ohne eigene Rechtspersönlichkeit, funktionale Werksorganisation |
| Ausschlüsse | physischer Standort ohne organisatorische Funktion und Tochtergesellschaft mit eigener Rechtspersönlichkeit |

Eine Organisationseinheit kann eine eigene Adresse, Kontaktpunkte und Kennungen
besitzen. Das macht sie nicht automatisch zur `LegalEntity`.

### 5.4 `conx-org:Membership`

| Punkt | Festlegung |
| --- | --- |
| Definition | Eigenständige Beziehung, durch die ein Agent Mitglied einer Organisation ist |
| Oberklasse | keine lokale Oberklasse |
| Kernanforderungen | genau ein `member` und genau eine `membershipOrganization` |
| Primäre Quelle | W3C Organization Ontology `org:Membership` |
| Alignment | Alignment zu `org:Membership`, `org:member` und `org:organization` prüfen |
| Mögliche Kennung | Mitgliedsnummer als `adms:identifier` der Membership |
| Beispiele | Person in Verband, Unternehmen in Innung, Unternehmen bei Berufsgenossenschaft |

Beispiel:

```turtle
ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband .
```

Rolle, Status und Gültigkeitszeitraum werden im MVP nicht als Pflichtbegriffe
eingeführt. Die Beziehungsressource hält diese Erweiterung offen.

### 5.5 `conx-org:LegalRepresentation`

| Punkt | Festlegung |
| --- | --- |
| Definition | Rechtliche Vertretungsbeziehung einer Person gegenüber einer Legal Entity |
| Oberklasse | keine lokale Oberklasse |
| Kernanforderungen | genau eine `representedOrganization` und genau ein `representative` |
| Primäre Quellen | SEMIC Power of Attorney, Schema.org `legalRepresentative`, UBL und BRIS-Anforderungen |
| Alignment | Kein direktes Klassenäquivalent bestätigt; Property-Mappings später prüfen |
| Datenschutzgrenze | keine Kopie von Namen, Titel, Geburtsdatum oder Geburtsort der Person |

Beispiel:

```turtle
ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

Die eigene Ressource ermöglicht spätere Angaben zu Vertretungsart, Zeitraum oder
Gesamtvertretung, ohne das MVP bereits damit zu belasten.

## 6. Namens- und Registrierungsproperties

### 6.1 `conx-org:name`

| Punkt | Festlegung |
| --- | --- |
| Definition | Allgemein verwendbare Bezeichnung einer Organisation |
| Domain | `conx-org:Organization` |
| Range | `xsd:string` oder `rdf:langString` |
| Core SHACL | mindestens ein nicht leerer Wert |
| Verbindlichkeit | verpflichtend für jede Organisation einschließlich Unterklassen |
| Quellen | W3C ORG, Schema.org `name`, Gaia-X `name`, UBL `PartyName` |
| Alignment | `rdfs:subPropertyOf schema:name` prüfen; keine Äquivalenz erzwingen |

### 6.2 `conx-org:legalName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Rechtlich beziehungsweise registeramtlich geführter Name einer Legal Entity |
| Domain | `conx-org:LegalEntity` |
| Range | `xsd:string` oder `rdf:langString` |
| Core SHACL | mindestens ein nicht leerer Wert |
| Verbindlichkeit | verpflichtend für `LegalEntity` |
| Quellen | SEMIC `legalName`, Schema.org `legalName`, UBL `RegistrationName` |
| Alignment | SEMIC und Schema.org als Kandidaten |

Der Wert darf mit `name` identisch sein, wird aber nicht automatisch daraus
abgeleitet. Eine Organisation kann unter einem kürzeren Namen auftreten als im
Register.

### 6.3 `conx-org:alternativeName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Weitere gebräuchliche Bezeichnung, Kurzform oder Handelsname einer Organisation |
| Domain | `conx-org:Organization` |
| Range | `xsd:string` oder `rdf:langString` |
| Core SHACL | `0..n`, nicht leer |
| Verbindlichkeit | optional |
| Quellen | SEMIC `alternativeName`, Schema.org `alternateName`, UBL `TradePartyName` |

Eine allgemeine Namenshistorie und zeitliche Gültigkeit einzelner Namen gehören
nicht in den MVP.

### 6.4 `conx-org:legalForm`

| Punkt | Festlegung |
| --- | --- |
| Definition | Klassifikation der Rechtsform einer Legal Entity in der relevanten Jurisdiktion |
| Domain | `conx-org:LegalEntity` |
| Range | `skos:Concept` |
| Core SHACL | `0..1` |
| Verbindlichkeit | optional im MVP; spätere Profile dürfen einen Wert verlangen |
| Quellen | SEMIC `legalFormType`, GLEIF/ISO 20275, Schema.org |
| Wertebereich | noch nicht geschlossen; ISO 20275/GLEIF bevorzugter Kandidat |

Freitext kann in externen Datenquellen vorkommen, ist aber nicht der bevorzugte
normative Wertebereich.

### 6.5 `conx-org:registrationDate`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kalenderdatum, an dem eine Legal Entity im maßgeblichen Register registriert wurde |
| Domain | `conx-org:LegalEntity` |
| Range | ausschließlich `xsd:date` |
| Core SHACL | genau ein Wert |
| Verbindlichkeit | verpflichtend für `LegalEntity` im implementierten MVP-Profil |
| Quellen | SEMIC `registrationDate`; Register- und GLEIF-Daten |

`registrationDate` ist nicht automatisch Gründungsdatum oder tatsächlicher
Beginn der Geschäftstätigkeit. `foundingDate` und `activityStartDate` werden im
MVP nicht eingeführt.

### 6.6 `conx-org:activity`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontrolliert klassifizierter Tätigkeitsbereich einer Organisation |
| Domain | `conx-org:Organization` |
| Range | `skos:Concept` |
| Core SHACL | `0..n` |
| Verbindlichkeit | optional |
| Quellen | SEMIC `legalEntityActivity`, NACE, Schema.org |
| Wertebereich | offen im MVP; NACE Rev. 2.1 bevorzugte europäische Quelle |

Eine Unterscheidung von Haupt- und Nebentätigkeit ist nicht Bestandteil von
Version 0.1.0.

## 7. Strukturproperties

### 7.1 `conx-org:subOrganizationOf`

| Punkt | Festlegung |
| --- | --- |
| Definition | Ordnet eine Organisation einer übergeordneten Organisation in einer allgemeinen Organisationshierarchie unter |
| Domain | `conx-org:Organization` |
| Range | `conx-org:Organization` |
| Core SHACL | `0..n`; Wert darf nicht identisch mit dem Subjekt sein |
| Inverse Property | `conx-org:hasSubOrganization` |
| Quelle | W3C ORG, Schema.org, Gaia-X |
| Alignment | `org:subOrganizationOf`, `schema:parentOrganization` prüfen |

Die Beziehung behauptet keine gesellschaftsrechtliche Eigentums- oder
Kontrollquote.

### 7.2 `conx-org:hasSubOrganization`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine Organisation mit einer ihr organisatorisch untergeordneten Organisation |
| Domain | `conx-org:Organization` |
| Range | `conx-org:Organization` |
| Core SHACL | `0..n` |
| Inverse Property | `conx-org:subOrganizationOf` |
| Quelle | W3C ORG, Schema.org, Gaia-X |

Die Datenhaltung darf eine bevorzugte Richtung wählen; OWL kann die inverse
Beziehung inferieren. Das SHACL-Profil soll nicht beide Richtungen als explizite
Eingabepflicht verlangen.

### 7.3 `conx-org:unitOf`

| Punkt | Festlegung |
| --- | --- |
| Definition | Ordnet eine Organisationseinheit einer übergeordneten Organisation zu |
| Domain | `conx-org:OrganizationalUnit` |
| Range | `conx-org:Organization` |
| Core SHACL | mindestens ein Wert; kein globales Maximum |
| Inverse Property | `conx-org:hasUnit` |
| Quelle | W3C ORG `unitOf` |

Mehrere Werte bleiben für Matrixorganisationen möglich. Ein späteres engeres
Profil darf genau eine primäre Zuordnung verlangen.

### 7.4 `conx-org:hasUnit`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine Organisation mit einer enthaltenen Organisationseinheit |
| Domain | `conx-org:Organization` |
| Range | `conx-org:OrganizationalUnit` |
| Core SHACL | `0..n` |
| Inverse Property | `conx-org:unitOf` |
| Quelle | W3C ORG `hasUnit` |

## 8. Mitgliedschaftsproperties

### 8.1 `conx-org:member`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt den Agenten, der Subjekt einer Mitgliedschaft ist |
| Domain | `conx-org:Membership` |
| Range | `conx-agent:Agent` |
| Core SHACL | genau ein Wert, explizit als Agent beziehungsweise bestätigte Unterklasse typisiert |
| Quelle | W3C ORG `member` |

Der Wertebereich erlaubt Personen und Organisationen. Eine Mitgliedschaft selbst
ist kein Agent.

### 8.2 `conx-org:membershipOrganization`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die Organisation, in der die Mitgliedschaft besteht |
| Domain | `conx-org:Membership` |
| Range | `conx-org:Organization` |
| Core SHACL | genau ein Wert |
| Quelle | W3C ORG `organization` |
| Alignment | `org:organization` prüfen; lokaler Name vermeidet die Mehrdeutigkeit eines sehr generischen Property-Namens |

Direkte Kurzbeziehungen wie `hasMember` und `memberOf` werden im MVP nicht als
zweite verpflichtende Datenrichtung eingeführt. Sie können später als
ableitbare Komfortproperties geprüft werden.

## 9. Vertretungsproperties

### 9.1 `conx-org:representedOrganization`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die Legal Entity, auf die sich eine rechtliche Vertretungsbeziehung bezieht |
| Domain | `conx-org:LegalRepresentation` |
| Range | `conx-org:LegalEntity` |
| Core SHACL | genau ein Wert |
| Quelle | SEMIC, Schema.org, UBL und Registeranforderungen |

### 9.2 `conx-org:representative`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die Person, die eine Legal Entity rechtlich vertritt |
| Domain | `conx-org:LegalRepresentation` |
| Range | `conx-person:Person` |
| Core SHACL | genau ein Wert, explizit als Person typisiert |
| Datenschutz | Es wird nur die Personenressource referenziert; Personendaten werden nicht in der Vertretung dupliziert |

Eine direkte Shortcut-Property von Legal Entity zu Person ist im MVP nicht
vorgesehen. Dadurch bleibt die Vertretungsbeziehung später um Art, Zeitraum und
Vertretungsregeln erweiterbar.

## 10. Wiederverwendete Integrationsbegriffe

### 10.1 `adms:identifier`

Organisationen, Legal Entities, Organisationseinheiten und Mitgliedschaften
können ADMS-Identifier besitzen. Das allgemeine Muster lautet:

```turtle
ex:bau-gmbh
    adms:identifier [
        a adms:Identifier ;
        skos:notation "HRB 12345"^^ex-scheme:local-register-number ;
        adms:schemaAgency "Zuständige Registerstelle"
    ] .
```

Der Datentyp im Beispiel ist noch kein beschlossener Construct-X-Wert. Die
Identifier-Scheme-Liste für Organisationen wird erst in einer späteren Phase
festgelegt. Das MVP darf VAT-ID, LEI, EUID, EORI oder GLN nicht als gemeinsam
verpflichtende Kennungen behandeln.

Eine Mitgliedsnummer gehört an die `Membership`, nicht automatisch an das
Mitglied:

```turtle
ex:membership-4711
    adms:identifier [
        a adms:Identifier ;
        skos:notation "4711"^^ex-scheme:association-membership-number ;
        adms:schemaAgency "Bauverband Beispielregion"
    ] .
```

### 10.2 `conx-addr:hasAddressAssignment`

Organisationen und Organisationseinheiten verwenden das bestehende
AddressAssignment-Muster. Für Legal Entities sind insbesondere die Rollen
`LegalAddressRole`, `HeadquartersAddressRole`, `RegistrationAddressRole` und
`PostalAddressRole` relevant.

Es werden keine Properties wie `street`, `houseNumber`, `postalCode` oder `city`
im Namespace `conx-org` eingeführt.

### 10.3 `conx-contact:hasContactPoint`

Organisationen und Organisationseinheiten verwenden die bestehende
Kontaktontologie. Die offizielle Homepage wird als vorhandener
Website-Kontaktkanal modelliert:

```turtle
ex:bau-gmbh
    conx-contact:hasContactPoint ex:bau-gmbh-official-contact .

ex:bau-gmbh-official-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:official ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:bau-gmbh-website .

ex:bau-gmbh-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactURI <https://example.org/> .
```

Es wird keine lokale Property `homepage` eingeführt.

## 11. Ausdrücklich zurückgestellte Begriffe

| Begriff | Grund |
| --- | --- |
| `EconomicActor` | keine direkt übernommene Klasse einer ausgewerteten Kernontologie; wirtschaftliche Aktivität wird über Rollen ausgedrückt |
| `Enterprise` | rechtlich und statistisch kontextabhängiger Begriff, insbesondere für KMU-Bewertungen |
| `EconomicOperator` | Markt- beziehungsweise Prozessrolle, keine intrinsische Organisationsklasse |
| `FormalOrganization` | externes W3C-ORG-Konzept reicht als späteres Alignment-Ziel |
| `Post` / Stelle | kein bestätigter Bedarf an dauerhaft eingerichteten oder unbesetzten Positionen |
| `BusinessProfile` | erst bei mehreren getrennten Geschäftsauftritten derselben Person erforderlich |
| `hasLegalRepresentative` | direkte Abkürzung würde die erweiterbare Vertretungsressource umgehen |
| `hasMember` / `memberOf` | direkte Abkürzungen sind aus der Membership ableitbar und im MVP nicht als zweite Datenrichtung nötig |
| `foundingDate` | nicht identisch mit Registerdatum und aktuell nicht benötigt |
| `activityStartDate` | fachlich zu unscharf und aktuell nicht benötigt |
| `homepage` | bereits über `core/contact` abbildbar |
| `FinancialAccount` | gehört in ein späteres Zahlungs- oder Finanzmodell |
| Credential-Klasse | kein eigenes Credential-Modul im MVP beschlossen |

## 12. Validierungsprofile

### 12.1 Organization Core

- expliziter Typ `conx-org:Organization` oder eine bestätigte Unterklasse,
- mindestens ein nicht leerer `name`-Wert,
- Objektwerte für Hierarchie, ADMS-Identifier, AddressAssignments und
  ContactPoints,
- keine globale Pflicht für Registerkennung, Rechtsform oder Adresse.

### 12.2 Legal Entity Core

- alle Regeln von Organization Core,
- mindestens ein nicht leerer `legalName`-Wert,
- genau ein `registrationDate` als `xsd:date`,
- mindestens ein struktureller ADMS-Identifier,
- `legalForm` höchstens einmal und als `skos:Concept`,
- Anforderungen an eine Legal-Address-Zuordnung werden im
  SHACL-Anforderungsdokument gegen die vorhandenen Address Shapes geprüft.

### 12.3 Organizational Unit Core

- alle Regeln von Organization Core,
- mindestens eine `unitOf`-Beziehung zu einer Organization,
- kein Zwang zu eigener Rechtsform, rechtlichem Namen oder Registerdatum.

### 12.4 Relationship Core

- `Membership`: genau ein `member` und eine `membershipOrganization`,
- `LegalRepresentation`: genau eine `representedOrganization` und eine
  `representative`-Person,
- keine eingebetteten Namen oder Geburtsdaten in der Vertretung.

## 13. Entscheidungen für die SHACL-Anforderungen

Die zuvor offenen Abnahmepunkte sind im
[SHACL-Anforderungsdokument](shacl-requirements.md) wie folgt entschieden:

1. `registrationDate` ist für jede `LegalEntity` genau einmal als `xsd:date`
   verpflichtend.
2. Jede `LegalEntity` benötigt mindestens einen strukturierten ADMS-Identifier;
   konkrete Kennungsschemata bleiben im Core offen.
3. `legalForm` bleibt optional und ist auf höchstens ein SKOS-Konzept begrenzt.
4. Mitgliedschaftsrolle und Gültigkeitszeitraum gehören noch nicht in den MVP.
5. Die Hierarchiebeziehungspaare sind als OWL-Inversen implementiert; SHACL
   verlangt nicht, beide Richtungen explizit zu liefern.
6. Jede `LegalEntity` benötigt mindestens eine AddressAssignment mit
   `LegalAddressRole`.

Das fachliche Zusammenspiel ist im
[Organisationsdiagramm](diagrams/organization-concept-model.md) dargestellt.

## 14. Verständliches Beispiel

> `legalName` bezeichnet den rechtlichen Namen einer Legal Entity. Ein kurzer
> Markenname kann zusätzlich als `name` oder `alternativeName` erscheinen,
> ersetzt den rechtlichen Namen aber nicht.
