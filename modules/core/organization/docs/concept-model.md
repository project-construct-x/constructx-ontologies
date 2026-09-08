# Fachliches Konzeptmodell der Organisationsontologie

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`  
**Umsetzungsstand:** T-Box und Core Shapes 0.1.0 implementiert

## 1. Ziel

Das Konzeptmodell beschreibt den organisationsbezogenen Kern des Construct-X-
Ontologienetzwerks. Es führt die Quellenanalyse, die bestätigten Scope-
Entscheidungen und den Begriffskatalog in einem konsistenten Modell zusammen.

Die vollständigen Diagramme stehen im
[fachlichen Organisationsdiagramm](diagrams/organization-concept-model.md).
Klassen- und Propertydetails sind im [Begriffskatalog](term-catalog.md)
dokumentiert.

## 2. Modellkern

Der MVP enthält fünf lokale Klassen:

```text
Organization
LegalEntity
OrganizationalUnit
Membership
LegalRepresentation
```

Die Klassen bilden drei unterschiedliche Aspekte ab:

1. Organisationsidentität und interne Struktur,
2. Mitgliedschaft eines Agenten in einer Organisation,
3. rechtliche Vertretung einer Legal Entity durch eine Person.

Person, Adresse, Kontaktpunkt, Identifier und Prozessrolle werden nicht erneut
definiert.

## 3. Klassenhierarchie

```text
conx-agent:Agent
  ├── conx-person:Person
  └── conx-org:Organization
        ├── conx-org:LegalEntity
        └── conx-org:OrganizationalUnit
```

`Organization` ist die einzige direkte lokale Organisationsunterklasse von
`Agent`. `LegalEntity` und `OrganizationalUnit` spezialisieren `Organization`.

### 3.1 `Organization`

Eine Organisation ist ein organisierter kollektiver Akteur mit gemeinsamem
Zweck oder dauerhaft erkennbarer Struktur. Der Begriff umfasst mehr als
rechtlich registrierte Unternehmen, beispielsweise auch Verbände,
Arbeitsgemeinschaften oder organisatorische Verbünde.

Eine Organisation ist nicht automatisch:

- eine juristische oder registrierte rechtliche Einheit,
- wirtschaftlich tätig,
- Eigentümer einer anderen Organisation,
- ein physischer Standort,
- Verkäufer, Käufer oder anderer Prozessbeteiligter.

### 3.2 `LegalEntity`

Eine `LegalEntity` ist im lokalen Construct-X-Scope eine Organisation mit
eigenständiger rechtlicher Identität. Sie besitzt zusätzlich zum allgemeinen
Namen einen rechtlichen Namen und ein Registrierungsdatum.

Der lokale Begriff wird enger verwendet als externe Modelle, die auch
selbständige natürliche Personen als Legal Entity behandeln. Deshalb ist eine
spätere Subklassen- oder Mappingbeziehung fachlich plausibel, eine
`owl:equivalentClass`-Aussage aber nicht vorab gerechtfertigt.

### 3.3 `OrganizationalUnit`

Eine `OrganizationalUnit` ist ein organisatorischer Teil einer übergeordneten
Organisation. Sie hat eine eigene Funktion oder Zuständigkeit, aber nicht allein
dadurch eine eigene Rechtspersönlichkeit.

Jede Organisationseinheit benötigt im implementierten Core-Profil mindestens
eine `unitOf`-Beziehung. Mehrere Beziehungen bleiben für Matrixorganisationen
möglich.

## 4. Kein allgemeiner `EconomicActor`

Version 0.1.0 führt keine Klasse `EconomicActor`, `Enterprise` oder lokale
`EconomicOperator` ein.

Die EU-Begriffe „Unternehmen“ und „Wirtschaftsteilnehmer“ umfassen abhängig vom
Rechts- und Prozesskontext auch natürliche Personen, öffentliche Stellen und
temporäre Gruppen. Das macht sie für eine feste Organisationsunterklasse
ungeeignet.

Eine selbständig tätige Person bleibt deshalb:

```text
conx-person:Person
```

Sie kann in einem Geschäftskontext über dieselbe Agentenrollenzuordnung wie eine
Organisation als Verkäufer, Auftragnehmer oder anderer wirtschaftlicher
Beteiligter auftreten.

## 5. Namen und Registrierung

### 5.1 Namensebenen

| Property | Bedeutung | Zielklasse |
| --- | --- | --- |
| `name` | allgemein verwendbare Organisationsbezeichnung | `Organization` |
| `legalName` | rechtlich oder registeramtlich geführter Name | `LegalEntity` |
| `alternativeName` | Handelsname, Kurzform oder weitere gebräuchliche Bezeichnung | `Organization` |

Jede Organisation benötigt mindestens einen `name`. Jede Legal Entity benötigt
zusätzlich mindestens einen `legalName`. Beide Werte dürfen identisch sein.

Mehrsprachige Werte bleiben möglich. Eine vollständige Namenshistorie mit
Gültigkeitszeiträumen gehört nicht in den MVP.

### 5.2 Registrierung

`registrationDate` bezeichnet ausschließlich das Registerdatum einer
`LegalEntity`. Es ist nicht gleichbedeutend mit:

- Gründungsdatum,
- Beginn der wirtschaftlichen Tätigkeit,
- Beginn einer konkreten Mitgliedschaft,
- Datum der Ausstellung einer Kennung.

Der Termkatalog sieht genau ein vollständiges `xsd:date` vor. Das
[SHACL-Anforderungsdokument](shacl-requirements.md) bestätigt diese Pflicht und
deckt sie mit gültigen und ungültigen Szenarien ab.

### 5.3 Rechtsform und Tätigkeit

`legalForm` und `activity` verweisen auf kontrollierte Konzepte. Der MVP legt
noch keine geschlossenen Wertemengen fest:

- ISO 20275/GLEIF ist bevorzugter Kandidat für Rechtsformen,
- NACE Rev. 2.1 ist bevorzugter europäischer Kandidat für Tätigkeiten.

Ohne Jurisdiktionsprofil wäre eine abgeschlossene globale Liste nicht
belegbar. Beide Properties bleiben daher im allgemeinen MVP optional.

## 6. Kennungen

Das Modell verwendet ausschließlich das bestehende ADMS-Profil:

```text
Organization / LegalEntity / OrganizationalUnit / Membership
  └── adms:identifier
        └── adms:Identifier
              ├── skos:notation
              └── adms:schemaAgency
```

Die stabile Ressourcen-IRI und fachliche Kennungen bleiben getrennt.

### 6.1 Kennungskategorien

| Kategorie | Beispiele | Modellhinweis |
| --- | --- | --- |
| Rechtliche Registrierung | nationale Registerkennung, EUID | spätere jurisdiktionsbezogene Auswahl |
| Steuer | VAT-ID, W-IdNr., nationale Steuernummer | nicht für jede Organisation vorhanden |
| Finanzmarkt | LEI | zusätzliche belastbare Kennung, aber nicht universell vorhanden |
| Zoll | EORI | nur für relevante Zollbeteiligte |
| Lieferkette | GLN | Typ der identifizierten Ressource beachten |
| Technisch | DID | Kontrolle eines Identifikators, nicht automatisch rechtliche Identität |
| Mitgliedschaft | Verbands- oder Innungsmitgliedsnummer | Identifier der `Membership` |

Version 0.1.0 schließt diese Schemata nicht in einer globalen Positivliste. Das
Das implementierte Core Shape prüft die ADMS-Struktur, aber keinen nationalen
Registerdienst ersetzen.

## 7. Organisationshierarchie

Das Modell unterscheidet zwei Beziehungen.

### 7.1 Allgemeine Unterorganisation

```text
Organization
  └── subOrganizationOf -> Organization
```

Die inverse Beziehung ist `hasSubOrganization`. Sie kann für organisatorische
Verbünde, Dachorganisationen oder andere Unterordnungen verwendet werden.

Die Beziehung bedeutet nicht automatisch:

- gesellschaftsrechtliches Eigentum,
- Mehrheitskontrolle,
- Konzernabschlusszugehörigkeit,
- identische rechtliche Verantwortung.

### 7.2 Organisationseinheit

```text
OrganizationalUnit
  └── unitOf -> Organization
```

Die inverse Beziehung ist `hasUnit`. Sie ist spezieller als die allgemeine
Unterorganisationsbeziehung und drückt aus, dass die Einheit innerhalb der
übergeordneten Organisation definiert ist.

Die beiden Beziehungspaare sollen in OWL als invers modellierbar sein. Das
Das Core-SHACL-Profil verlangt trotzdem nicht, beide Richtungen explizit zu
speichern.

## 8. Organisationseinheit und Standort

Organisation und Ort werden als unabhängige Dimensionen modelliert.

| Gegenstand | Organisationstyp | Standortressource |
| --- | --- | --- |
| Einkaufsabteilung | `OrganizationalUnit` | nur wenn eigener physischer Ort benötigt wird |
| Niederlassung ohne eigene Rechtspersönlichkeit | `OrganizationalUnit` | typischerweise ja |
| Tochtergesellschaft | `LegalEntity` | optional eigener Sitz oder mehrere Standorte |
| Werk | häufig `OrganizationalUnit` | physischer Werksstandort getrennt |
| Depot | nur bei eigener organisatorischer Funktion | physischer Depotstandort getrennt |
| Baustelle | keine Organization allein aufgrund des Orts | Projekt- oder Baustellenstandort |
| Konzern | `Organization`, falls als eigener Verbund benötigt | kein einzelner notwendiger Standort |

Eine Ressource wird nicht gleichzeitig als Organisationseinheit und physischer
Ort verwendet. So können dieselbe Einheit mehrere Standorte und derselbe
Standort mehrere organisatorische Nutzer besitzen, ohne Identitäten zu
vermischen.

Die konkrete Beziehung zu einer künftigen Standortklasse bleibt zurückgestellt.
Adressen können bereits jetzt über `conx-addr:hasAddressAssignment` an die
Organisation oder Organisationseinheit gebunden werden.

## 9. Mitgliedschaft

Eine Mitgliedschaft verbindet einen Agenten mit einer Organisation:

```text
Membership
  ├── member                 -> Agent
  └── membershipOrganization -> Organization
```

Der Member kann sein:

- eine `Person`,
- eine `Organization`,
- eine `LegalEntity`,
- eine `OrganizationalUnit`, sofern dies fachlich zulässig ist.

Die aufnehmende Ressource ist immer eine `Organization`. Dadurch können
Mitgliedschaften in Verband, Innung oder Berufsgenossenschaft mit demselben
Muster beschrieben werden.

Eine Mitgliedsnummer wird als ADMS-Identifier der `Membership` geführt. Sie wird
nicht als globale Kennung des Mitglieds interpretiert.

### 9.1 Abgrenzung zur Stelle

Eine Mitgliedschaft sagt, dass ein Agent zu einer Organisation gehört. Eine
Stelle im Sinn von W3C ORG `Post` wäre dagegen eine dauerhaft eingerichtete
Position, die auch unbesetzt existieren kann.

Da der MVP weder unbesetzte Positionen noch vollständige Organigramme benötigt,
enthält er keine `Post`-Klasse. Ein Rollenwert an einer späteren Membership macht
eine Stelle ebenfalls nicht automatisch erforderlich.

## 10. Rechtliche Vertretung

Rechtliche Vertretung wird als eigene Beziehungsressource modelliert:

```text
LegalRepresentation
  ├── representedOrganization -> LegalEntity
  └── representative          -> Person
```

Die Ressource verhindert die Duplikation von Personendaten. Sie enthält im MVP
nur die beiden notwendigen Beziehungen.

Spätere Erweiterungen können an der Vertretungsressource ansetzen:

- Vertretungsart,
- Einzel- oder Gesamtvertretung,
- Gültigkeitszeitraum,
- Registerbezug,
- externe Nachweisressource.

Diese Erweiterungen sind nicht Teil von Version 0.1.0. Eine direkte parallele
Property `hasLegalRepresentative` wird zunächst nicht eingeführt.

## 11. Adresse und Kontakt

### 11.1 Adresszuordnung

Eine Organisation verwendet das bestehende Muster:

```text
Organization
  └── conx-addr:hasAddressAssignment
        └── AddressAssignment
              ├── assignedAddress -> Address
              └── addressRole     -> AddressRole
```

Für Legal Entities sind besonders relevant:

- `LegalAddressRole`,
- `HeadquartersAddressRole`,
- `RegistrationAddressRole`,
- `PostalAddressRole`.

Straße, Hausnummer, Postleitzahl und Ort werden nicht in `core/organization`
dupliziert.

### 11.2 Kontakt und Homepage

Eine Organisation verwendet das bestehende Kontaktmodell:

```text
Organization
  └── conx-contact:hasContactPoint
        └── ContactPoint
              └── hasContactMethod -> ContactMethod
```

Eine offizielle Homepage ist ein Kontaktpunkt mit:

```text
contactUsage   = contact-usage:official
contactPurpose = contact-purpose:general
contactChannel = contact-channel:website
contactURI     = offizielle Web-IRI
```

Damit ist keine lokale Property `homepage` erforderlich. Liefer-, Rechnungs-
oder Supportkontakte können getrennte Kontaktpunkte derselben Organisation
sein.

## 12. Prozessrollen

Geschäftsrollen werden außerhalb des Organisationskerns modelliert:

```text
AgentRoleAssignment
  ├── assignedAgent -> Person oder Organization
  ├── role          -> kontrollierter Rollenwert
  └── context       -> Lieferschein, Sendung, Vertrag, Artikel oder Projekt
```

Beispiele für Rollenwerte sind Verkäufer, Käufer, Versender, Empfänger,
Transporteur, Hersteller und Auftraggeber.

Dieses Muster löst zugleich den Fall einer selbständig tätigen Person: Sie kann
als Verkäufer oder Auftragnehmer auftreten, ohne als Organisation klassifiziert
zu werden.

## 13. Externe Nachweise und Bewertungen

Der MVP führt kein eigenes Credential-Modul ein. Versicherungen, Befähigungen,
KMU-Status, Steuerstatus, Kreditwürdigkeit und Sanktionsprüfungen bleiben
außerhalb des Organisationskerns.

Das Modell behauptet insbesondere keine flachen Booleans wie:

- `isCompliantWithRussiaSanctions`,
- `isNotInDifficulty`,
- `isSME`,
- `isInputTaxDeductible`.

Solche Aussagen benötigen Zeitpunkt, Rechtsgrundlage, Aussteller, geprüften
Gegenstand und gegebenenfalls Gültigkeit. Eine spätere externe Nachweisressource
kann verknüpft werden, sobald ein konkreter Use Case vorliegt.

## 14. Konzeptionelles Gesamtbeispiel

```turtle
@prefix conx-org: <https://www.construct-x.org/ontology/organization#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .

ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date ;
    adms:identifier ex:bau-gmbh-register-id ;
    conx-addr:hasAddressAssignment ex:bau-gmbh-legal-address ;
    conx-contact:hasContactPoint ex:bau-gmbh-official-contact .

ex:einkauf
    a conx-org:OrganizationalUnit ;
    conx-org:name "Einkauf"@de ;
    conx-org:unitOf ex:bau-gmbh .

ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband ;
    adms:identifier ex:membership-number-4711 .

ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

Die referenzierten Identifier-, Address-, Contact- und Person-Ressourcen werden
von ihren zuständigen Modellen beschrieben und hier nicht dupliziert.

## 15. Implementierte Modellinvarianten

1. Jede `Organization` besitzt mindestens einen Namen.
2. Jede `LegalEntity` ist eine `Organization` und besitzt zusätzlich rechtlichen
   Namen und Registrierungsdatum.
3. Jede `OrganizationalUnit` ist eine `Organization` und besitzt mindestens eine
   `unitOf`-Beziehung.
4. Jede `Membership` verbindet genau einen Agenten mit genau einer Organisation.
5. Jede `LegalRepresentation` verbindet genau eine Legal Entity mit genau einer
   Person.
6. Personendaten werden nicht in Organisation oder Vertretung dupliziert.
7. Adressen und Kontakte werden ausschließlich über ihre bestehenden
   Zuordnungsmuster angebunden.
8. Eine Homepage wird als Website-Kontakt modelliert.
9. Kennungen verwenden ADMS; Mitgliedsnummern gehören an die Membership.
10. Prozessrollen sind keine Organisationsunterklassen.
11. Organisationseinheit und physischer Standort bleiben getrennte Ressourcen.
12. Es gibt im MVP weder `EconomicActor`, lokale `FormalOrganization`, `Post`
    noch eine Credential-Klasse.

## 16. Implementierungsstand

Das vollständige fachliche
[SHACL-Anforderungsdokument](shacl-requirements.md) ist aus diesem Modell
abgeleitet. T-Box, Shape-Graph sowie gültige und ungültige Testgraphen sind für
Version `0.1.0` implementiert. Als nächste Schritte folgen generierte
HTML-Dokumentation, Netzwerkmetadaten und später eigenständige Alignments oder
strengere Fachprofile.
