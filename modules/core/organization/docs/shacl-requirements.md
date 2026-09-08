# Fachliche SHACL-Anforderungen für den Organisations-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Organization Core Shapes

## 1. Zweck

Dieses Dokument legt die ausführbaren Qualitätsanforderungen für
Organisationsdaten fest. Es beschreibt Shape-Targets, Constraints,
Schweregrade, stabile Fehlercodes sowie gültige und ungültige Szenarien.

Es dokumentiert den implementierten Shape-Graph
`shapes/conx-org-core.shacl.ttl`.

Grundlagen:

- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Begriffskatalog](term-catalog.md)
- [Konzeptmodell](concept-model.md)
- [Quellenanalyse](source-analysis.md)
- [Organisationsdiagramm](diagrams/organization-concept-model.md)

## 2. Implementiertes Shape-Set

```text
Shape-Graph:  modules/core/organization/shapes/conx-org-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/organization/core
Versions-IRI: https://www.construct-x.org/shapes/organization/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/organization/core#
Prefix:       conx-org-sh
Version:      0.1.0
```

Diese IRIs sind durch Shape-Graph und Modulmetadaten für Version `0.1.0`
verbindlich umgesetzt.

## 3. Validierungsprinzipien

### 3.1 OWL und SHACL

- OWL beschreibt Bedeutung, Unterklassen, Domain, Range und inverse
  Beziehungen unter der Open-World-Annahme.
- SHACL prüft den tatsächlich gelieferten Datengraphen.
- Pflichtfelder und Maximalwerte werden ausschließlich durch die Core Shapes
  als Datenvertrag geschlossen.
- Die Shapes bleiben für zusätzliche Properties offen; `sh:closed true` ist
  nicht vorgesehen.
- SHACL-Maximalwerte werden nicht automatisch zu OWL-Kardinalitätsaxiomen.
- Die Validierung wird mit der Organization-, Agent-, Person-, Address- und
  Contact-T-Box sowie den benötigten Referenzgraphen ausgeführt.

### 3.2 Explizite Typisierung

Ressourcen, die Organization-, Legal-Entity-, Organizational-Unit-, Membership-
oder Legal-Representation-Properties verwenden, müssen explizit mit dem
passenden lokalen Typ versehen sein. Eine bloße Domain-Inferenz ersetzt diese
Datenanforderung nicht.

Unterklassenschlüsse zwischen `LegalEntity`, `OrganizationalUnit`,
`Organization` und `Agent` dürfen aus der geladenen T-Box folgen. Eine
`LegalEntity` muss daher nicht zusätzlich redundant als `Organization` und
`Agent` typisiert werden.

### 3.3 Ressourcenform

Alle fünf MVP-Ressourcentypen müssen als IRIs referenziert werden:

- `Organization`,
- `LegalEntity`,
- `OrganizationalUnit`,
- `Membership`,
- `LegalRepresentation`.

Blank Nodes sind für diese fachlich stabilen Ressourcen im Core-Profil nicht
zulässig. ADMS-Identifier und bestehende Address- oder Contact-Ressourcen folgen
den Regeln ihrer jeweiligen Shape-Sets und dürfen dort gegebenenfalls Blank
Nodes sein.

### 3.4 Schweregrade

Alle in diesem Dokument beschriebenen Core-Verstöße verwenden `sh:Violation`.
Das Core Shape erzeugt keine Warnungen für freiwillige Empfehlungen wie
Rechtsform, Tätigkeit, Headquarters-Adresse oder zusätzliche Kennungen.

Spätere Anwendungsprofile dürfen `sh:Warning` und `sh:Info` verwenden oder
strengere `sh:Violation`-Regeln ergänzen.

### 3.5 Fehlermeldungen

Jede Constraint-Komponente erhält:

- eine deutsche `sh:message`,
- eine englische `sh:message`,
- einen stabilen Anforderungsbezeichner,
- einen konkreten Ergebnispfad, soweit SHACL ihn bestimmen kann.

## 4. Verantwortungsgrenzen

| Anforderung | Zuständiges Shape-Set | Regel im Organization Shape |
| --- | --- | --- |
| Organisationsklassen, Namen und Struktur | `organization/core` | vollständig prüfen |
| Legal Name, Registerdatum und Rechtsform | `organization/core` | vollständig nach MVP-Regeln prüfen |
| ADMS-Identifier an Organisation und Membership | `organization/core` mit bestehendem ADMS-Muster | minimale Struktur lokal verschachtelt prüfen |
| Konkrete Register-, VAT-, LEI-, EUID-, EORI- oder GLN-Schemata | spätere Fach- oder Jurisdiktionsprofile | nicht gegen Positivliste prüfen |
| AddressAssignment und Adressbestandteile | `address/core` | bestehende Shapes wiederverwenden |
| Mindestens eine rechtliche Adresse der Legal Entity | `organization/core` plus `address/core` | AddressAssignment mit `LegalAddressRole` verlangen |
| Kontaktpunkte und Homepage | `contact/core` | keine Kontaktpayloads im Organization Shape duplizieren |
| Personendaten | `person/core` | nur Personenreferenz der Vertretung prüfen |
| Verkäufer-, Käufer- und andere Prozessrollen | Domänen-/Participation-Shapes | nicht im Organization Core prüfen |
| Versicherungen, Befähigungen und Compliance | spätere externe Nachweisprofile | nicht im Organization Core prüfen |
| Bankkonten und Zahlungsdaten | späteres Payment-/Finance-Shape | nicht im Organization Core prüfen |

## 5. Beschlossene MVP-Verbindlichkeit

Die im Termkatalog vorgemerkten SHACL-Fragen werden für dieses
Anforderungsdokument wie folgt entschieden:

| Thema | Entscheidung |
| --- | --- |
| `registrationDate` | für jede `LegalEntity` genau einmal als `xsd:date` verpflichtend |
| ADMS-Identifier der `LegalEntity` | mindestens ein struktureller Identifier verpflichtend; konkrete Schemata bleiben offen |
| `legalForm` | optional, höchstens ein Wert als IRI und `skos:Concept` |
| Mitgliedschaftsrolle und -zeitraum | nicht Bestandteil des MVP |
| Inverse Hierarchiebeziehungen | als OWL-Inversen implementiert; SHACL verlangt nicht beide Datenrichtungen |
| Rechtliche Adresse | mindestens eine AddressAssignment mit `LegalAddressRole` pro `LegalEntity` |
| Headquarters-Adresse | optional; keine Core-Pflicht |
| Rechtsform- und Tätigkeitsvokabular | offene `skos:Concept`-Referenz ohne geschlossene Werteliste |

Die Pflicht zu mindestens einem ADMS-Identifier belegt nur, dass eine
strukturierte Kennung geliefert wurde. Ohne späteres Jurisdiktionsprofil
entscheidet das Core Shape nicht, ob diese Kennung als rechtlich belastbarer
Registeridentifikator genügt.

## 6. Shape-Katalog

### 6.1 Lokale Shapes

| Shape-IRI | Typ | Target beziehungsweise Verwendung | Aufgabe |
| --- | --- | --- | --- |
| `conx-org-sh:NonEmptyStringOrLangStringShape` | wiederverwendbares Node Shape | von Namens-Property-Shapes referenziert | erlaubt nicht leere `xsd:string`- oder `rdf:langString`-Werte |
| `conx-id-sh:ADMSIdentifierShape` | wiederverwendbares Node Shape aus `identifier/core` | Werte von `adms:identifier` | prüft Typ, Notation und Schema-Agentur nach dem gemeinsamen Minimalvertrag |
| `conx-org-sh:LegalAddressAssignmentShape` | wiederverwendbares Node Shape | qualifizierte Werte von `hasAddressAssignment` | prüft AddressAssignment-Typ und `LegalAddressRole` |
| `conx-org-sh:OrganizationShape` | Node Shape | `Organization` und Subjekte allgemeiner Organization-Properties | prüft IRI, Typ, Name, optionale Stammdaten, Hierarchie und optionale Identifier |
| `conx-org-sh:LegalEntityShape` | Node Shape | `LegalEntity` und Subjekte rechtlicher Properties | ergänzt Legal Name, Registerdatum, Identifier-Minimum, Rechtsform und Legal Address |
| `conx-org-sh:OrganizationalUnitShape` | Node Shape | `OrganizationalUnit` und Subjekte von `unitOf` | ergänzt mindestens eine übergeordnete Organization |
| `conx-org-sh:MembershipShape` | Node Shape | `Membership` und Subjekte ihrer Properties | prüft genau einen Member und eine aufnehmende Organization |
| `conx-org-sh:LegalRepresentationShape` | Node Shape | `LegalRepresentation` und Subjekte ihrer Properties | prüft genau eine Legal Entity und eine Person |

### 6.2 Wiederverwendete Shapes

| Shape | Eigentümer | Nutzung |
| --- | --- | --- |
| `conx-addr-sh:ResourceWithAddressAssignmentShape` | `address/core` | prüft Werte von `hasAddressAssignment` |
| `conx-addr-sh:AddressAssignmentShape` | `address/core` | prüft `assignedAddress`, `addressRole` und weitere Assignment-Daten |
| `conx-addr-sh:AddressShape` | `address/core` | prüft die Adresse selbst |
| `conx-contact-sh:ContactCarrierShape` | `contact/core` | prüft Werte von `hasContactPoint` |
| `conx-contact-sh:ContactPointShape` | `contact/core` | prüft Kontaktpunkt, Usage, Purpose und Methoden |
| `conx-contact-sh:ContactMethodShape` | `contact/core` | prüft Kontaktkanal und Payload einschließlich Website-IRI |
| `conx-person-sh:PersonShape` | `person/core` | prüft die referenzierte Person einer Vertretung, sofern deren Personendaten im Graph enthalten sind |

Das Organization Shape importiert den versionierten Shape-Graph
`identifier/core` und verwendet dessen `conx-id-sh:ADMSIdentifierShape`. Die
fachlichen Mindestanzahlen an Organisation, Legal Entity und Membership bleiben
im Organization Shape definiert.

## 7. Targets

### 7.1 `OrganizationShape`

Targets:

- `sh:targetClass conx-org:Organization`,
- `sh:targetSubjectsOf conx-org:name`,
- `sh:targetSubjectsOf conx-org:alternativeName`,
- `sh:targetSubjectsOf conx-org:activity`,
- `sh:targetSubjectsOf conx-org:subOrganizationOf`,
- `sh:targetSubjectsOf conx-org:hasSubOrganization`,
- `sh:targetSubjectsOf conx-org:hasUnit`.

`adms:identifier`, `conx-addr:hasAddressAssignment` und
`conx-contact:hasContactPoint` sind generische Properties. Sie dürfen nicht
jedes ihrer Subjekte automatisch zum Organization-Target machen. Sie werden nur
innerhalb bereits erkannter Organisationen geprüft beziehungsweise durch ihre
eigenen Shape-Sets erfasst.

### 7.2 `LegalEntityShape`

Targets:

- `sh:targetClass conx-org:LegalEntity`,
- `sh:targetSubjectsOf conx-org:legalName`,
- `sh:targetSubjectsOf conx-org:legalForm`,
- `sh:targetSubjectsOf conx-org:registrationDate`,
- `sh:targetObjectsOf conx-org:representedOrganization`.

Das Shape referenziert zusätzlich den gemeinsamen Organization-Vertrag, damit
Name und allgemeine Organization-Properties auch bei einer nur als
`LegalEntity` typisierten Ressource geprüft werden.

### 7.3 `OrganizationalUnitShape`

Targets:

- `sh:targetClass conx-org:OrganizationalUnit`,
- `sh:targetSubjectsOf conx-org:unitOf`,
- `sh:targetObjectsOf conx-org:hasUnit`.

Auch dieses Shape referenziert den gemeinsamen Organization-Vertrag.

### 7.4 `MembershipShape`

Targets:

- `sh:targetClass conx-org:Membership`,
- `sh:targetSubjectsOf conx-org:member`,
- `sh:targetSubjectsOf conx-org:membershipOrganization`.

Ein Agent oder eine Organization wird nicht dadurch zum Membership-Target, dass
er beziehungsweise sie Objekt einer Membership-Property ist.

### 7.5 `LegalRepresentationShape`

Targets:

- `sh:targetClass conx-org:LegalRepresentation`,
- `sh:targetSubjectsOf conx-org:representedOrganization`,
- `sh:targetSubjectsOf conx-org:representative`.

## 8. Gemeinsame Literalregeln

`name`, `legalName` und `alternativeName` akzeptieren:

- `xsd:string`,
- `rdf:langString`.

Jeder Wert muss mindestens ein Nicht-Leerzeichen enthalten. Dafür ist eine
Regel entsprechend `sh:pattern "\\S"` vorzusehen.

Nicht zulässig sind:

- leere Literale,
- ausschließlich aus Leerzeichen bestehende Werte,
- numerische Werte,
- IRIs oder Blank Nodes als Namen.

`sh:uniqueLang` wird im Core nicht verwendet. Eine Organisation kann mehrere
Namen derselben Sprache oder in unterschiedlichen Schriftsystemen besitzen.

## 9. `OrganizationShape`

### 9.1 Node-Constraints

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `ORG-001` | Referenzierbare Organisation | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `ORG-002` | Organization-Typ | Fokusressource muss `conx-org:Organization` oder eine durch die geladene T-Box bestätigte Unterklasse sein |

### 9.2 Property-Constraints

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `ORG-010` | `conx-org:name` | 1 | offen | nicht leerer `xsd:string` oder `rdf:langString` |
| `ORG-011` | `conx-org:alternativeName` | 0 | offen | nicht leerer `xsd:string` oder `rdf:langString` |
| `ORG-020` | `conx-org:activity` | 0 | offen | IRI und Instanz von `skos:Concept` |
| `ORG-030` | `adms:identifier` | 0 | offen | Blank Node oder IRI, gültig nach `conx-id-sh:ADMSIdentifierShape` |
| `ORG-040` | `conx-org:subOrganizationOf` | 0 | offen | IRI und Instanz von `conx-org:Organization` |
| `ORG-041` | `conx-org:hasSubOrganization` | 0 | offen | IRI und Instanz von `conx-org:Organization` |
| `ORG-042` | direkte Selbstunterordnung | 0 | 0 | Fokusressource darf nicht ihr eigener Wert von `subOrganizationOf` oder `hasSubOrganization` sein |
| `ORG-043` | `conx-org:hasUnit` | 0 | offen | IRI und Instanz von `conx-org:OrganizationalUnit` |

### 9.3 Hierarchieregeln

`subOrganizationOf` und `hasSubOrganization` sind als inverse OWL-Properties
vorgesehen. Das Core Shape verlangt nur, dass vorhandene Werte korrekt typisiert
sind. Es verlangt nicht, dass beide Richtungen im Datengraph explizit stehen.

Die direkte Selbstreferenz ist unzulässig. Dafür ist eine kleine SPARQL-
Constraint oder ein gleichwertiges SHACL-Muster vorzusehen.

Längere Zyklen wie `A -> B -> C -> A` werden im MVP nicht geprüft. Ihre
Unzulässigkeit hängt von der später präzisierten Bedeutung unterschiedlicher
Hierarchiebeziehungen ab und würde rekursive Pfadvalidierung benötigen.

`subOrganizationOf` behauptet keine Eigentums- oder Kontrollbeziehung. Solche
Beziehungen werden daher weder verlangt noch aus der Hierarchie inferiert.

## 10. `LegalEntityShape`

### 10.1 Node-Constraints

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `LE-001` | Referenzierbare Legal Entity | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `LE-002` | Expliziter Legal-Entity-Typ | Fokusressource muss `sh:class conx-org:LegalEntity` erfüllen |
| `LE-003` | Organization-Vertrag | Fokusressource muss zusätzlich den gemeinsamen Organization-Vertrag erfüllen |

### 10.2 Property-Constraints

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `LE-010` | `conx-org:legalName` | 1 | offen | nicht leerer `xsd:string` oder `rdf:langString` |
| `LE-020` | `conx-org:registrationDate` | 1 | 1 | lexikalisch gültiges `xsd:date` |
| `LE-030` | `conx-org:legalForm` | 0 | 1 | IRI und Instanz von `skos:Concept` |
| `LE-040` | `adms:identifier` | 1 | offen | Blank Node oder IRI, gültig nach `conx-id-sh:ADMSIdentifierShape` |
| `LE-050` | `conx-addr:hasAddressAssignment` | qualifiziert 1 | offen | mindestens eine AddressAssignment mit `roles:LegalAddressRole` |

### 10.3 Registerdatum

`registrationDate` akzeptiert ausschließlich `xsd:date`. Unzulässig sind:

- untypisierte Datumsstrings,
- `xsd:gYear` oder `xsd:gYearMonth`,
- mehrere Registerdaten,
- ein Literal mit ungültiger `xsd:date`-Lexik.

Eine zeitabhängige Regel „Registerdatum darf nicht in der Zukunft liegen“ wird
im Core nicht eingeführt. Sie kann in einem strengeren Profil mit kontrollierter
Ausführungszeit ergänzt werden.

`registrationDate` ist nicht mit Gründung oder Tätigkeitsbeginn gleichzusetzen.

### 10.4 Rechtsform

`legalForm` ist im MVP optional. Falls vorhanden, muss der Wert:

1. eine IRI sein,
2. als `skos:Concept` typisiert sein.

Das Core Shape prüft keine geschlossene GLEIF-/ISO-20275-Wertemenge und keine
Übereinstimmung mit einer Jurisdiktion. Ein Literal wie `"GmbH"` ist trotzdem
unzulässig, weil dadurch das verwendete Rechtsformvokabular nicht erkennbar ist.

### 10.5 Rechtliche Adresse

Mindestens ein Wert von `conx-addr:hasAddressAssignment` muss:

- Blank Node oder IRI sein,
- als `conx-addr:AddressAssignment` typisiert sein,
- `conx-addr:addressRole roles:LegalAddressRole` besitzen.

Die Umsetzung verwendet fachlich eine qualifizierte Mindestkardinalität,
beispielsweise `sh:qualifiedValueShape` mit `sh:qualifiedMinCount 1`.

Das vorhandene Address Shape prüft zusätzlich:

- genau eine `assignedAddress`,
- mindestens eine `addressRole`,
- Typ und Struktur der zugeordneten Adresse.

Das Organization Shape dupliziert diese Regeln nicht. Es verlangt ebenfalls
keine weltweit unzutreffende Komponentenliste aus Straße, Hausnummer,
Postleitzahl und Ort. Länderspezifische Address-Profile können solche Regeln
später ergänzen.

Eine AddressAssignment darf gleichzeitig Legal-, Registration- und
Headquarters-Rolle besitzen. Das Core Shape verlangt keine drei getrennten
AddressAssignments.

## 11. ADMS-Identifier

Die Strukturregeln und Fehlercodes stammen aus dem importierten Shape-Graph
`identifier/core`. Das Organization Shape besitzt weiterhin die fachlichen
Kardinalitäten für Organization, Legal Entity und Membership.

### 11.1 Minimalstruktur

Jeder über `adms:identifier` referenzierte Identifier muss erfüllen:

| ID | Property | Anforderung |
| --- | --- | --- |
| `ID-001` | Typ | Ressource ist `adms:Identifier` |
| `ID-002` | `skos:notation` | genau ein Literal |
| `ID-003` | `adms:schemaAgency` | optional, höchstens ein `xsd:string` |

Der Identifier selbst darf Blank Node oder IRI sein. `skos:notation` muss ein
Literal sein; der Datentyp kann das Kennungsschema bezeichnen.

### 11.2 Legal-Entity-Minimum

Eine `LegalEntity` muss mindestens einen gültig strukturierten ADMS-Identifier
besitzen. Das Core Shape prüft noch nicht:

- ob der Notationsdatentyp in einer freigegebenen Registerschemaliste steht,
- ob die Kennung zur Jurisdiktion passt,
- ob VAT-ID, LEI, EUID, EORI oder GLN als Primärkennung genügt,
- ob die Kennung in einem externen Register existiert,
- ob Name und Adresse mit dem Registereintrag übereinstimmen.

Diese Prüfungen bleiben späteren Profilen und externen Validierungsdiensten
vorbehalten.

### 11.3 Identifier anderer Ressourcen

`Organization` und `OrganizationalUnit` dürfen optional ADMS-Identifier besitzen.
`Membership` darf eine Mitgliedsnummer als ADMS-Identifier tragen. Wenn solche
Identifier vorhanden sind, gilt dieselbe Minimalstruktur.

Eine Mitgliedsnummer gehört an die Membership und nicht automatisch an den
Member. Debitoren-, Kreditoren- oder Mandantennummern gehören an ihre jeweilige
Geschäftsbeziehung und liegen außerhalb dieses Shape-Sets.

## 12. `OrganizationalUnitShape`

### 12.1 Node-Constraints

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `UNIT-001` | Referenzierbare Organisationseinheit | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `UNIT-002` | Expliziter Unit-Typ | Fokusressource muss `sh:class conx-org:OrganizationalUnit` erfüllen |
| `UNIT-003` | Organization-Vertrag | Fokusressource muss zusätzlich den gemeinsamen Organization-Vertrag erfüllen |

### 12.2 Property-Constraints

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `UNIT-010` | `conx-org:unitOf` | 1 | offen | IRI und Instanz von `conx-org:Organization` |
| `UNIT-011` | direkte Selbstzuordnung | 0 | 0 | Organisationseinheit darf nicht `unitOf` ihrer selbst sein |

`unitOf` und `hasUnit` sind als inverse OWL-Properties implementiert. Das Shape
verlangt nicht, dass beide Richtungen explizit geliefert werden.

Mehrere `unitOf`-Werte bleiben zulässig. Das berücksichtigt
Matrixorganisationen. Ein engeres Profil darf später eine primäre oder genau
eine übergeordnete Organisation verlangen.

Eine Organisationseinheit benötigt weder `legalName`, `legalForm`,
`registrationDate` noch eine Legal Address. Sie darf eigene Kontakte,
Adresszuordnungen und strukturierte Identifier besitzen.

## 13. `MembershipShape`

### 13.1 Node-Constraints

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `MEM-001` | Referenzierbare Membership | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `MEM-002` | Expliziter Membership-Typ | Fokusressource muss `sh:class conx-org:Membership` erfüllen |

### 13.2 Property-Constraints

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `MEM-010` | `conx-org:member` | 1 | 1 | IRI und Instanz von `conx-agent:Agent` |
| `MEM-011` | `conx-org:membershipOrganization` | 1 | 1 | IRI und Instanz von `conx-org:Organization` |
| `MEM-012` | `adms:identifier` | 0 | offen | Blank Node oder IRI, gültig nach `conx-id-sh:ADMSIdentifierShape` |
| `MEM-020` | Selbstmitgliedschaft | 0 | 0 | derselbe IRI-Wert darf nicht gleichzeitig Member und aufnehmende Organization sein |

Der Member kann eine Person oder Organisation sein, weil beide Unterklassen von
`Agent` sind. Die Membership selbst darf nicht als Member verwendet werden,
sofern sie nicht entgegen dem Modell zusätzlich als Agent typisiert würde; ein
solcher Mehrfachtyp ist fachlich zu vermeiden.

Mitgliedschaftsrolle, Status, Beginn und Ende sind nicht Bestandteil von
Version 0.1.0. Shapes dürfen diese Angaben deshalb weder verlangen noch ihre
Abwesenheit beanstanden.

Die Selbstmitgliedschaftsregel benötigt eine SPARQL-Constraint oder ein
gleichwertiges SHACL-Muster, das Werte von `member` und
`membershipOrganization` vergleicht.

## 14. `LegalRepresentationShape`

### 14.1 Node-Constraints

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `REP-001` | Referenzierbare Vertretung | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `REP-002` | Expliziter Vertretungstyp | Fokusressource muss `sh:class conx-org:LegalRepresentation` erfüllen |

### 14.2 Property-Constraints

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `REP-010` | `conx-org:representedOrganization` | 1 | 1 | IRI und Instanz von `conx-org:LegalEntity` |
| `REP-011` | `conx-org:representative` | 1 | 1 | IRI und Instanz von `conx-person:Person` |

Die Vertretungsressource kopiert keine Personendaten. Verwendet eine
Vertretungsressource dennoch Properties wie `conx-person:birthDate` oder
`conx-person:fullName`, wird sie durch die Targets des Person Shape zusätzlich
als Personendatenressource erkannt und müsste dann den Person-Vertrag erfüllen.
Das Organization Shape selbst wird deshalb nicht mit `sh:closed true` versehen.

Nicht geprüft werden:

- Vertretungsart,
- Einzel- oder Gesamtvertretung,
- Beginn oder Ende der Vertretung,
- Registerquelle,
- Vollmachtstext,
- externer Nachweis.

Diese Begriffe sind nicht Teil des MVP.

## 15. Address- und Contact-Verträge

### 15.1 Address

Jeder vorhandene Wert von `conx-addr:hasAddressAssignment` wird durch das
Address-Core-Shape geprüft. Für Legal Entities ergänzt das Organization Shape
nur die qualifizierte Pflicht einer Legal Address.

Das Organization Shape prüft nicht selbst:

- Straße und Hausnummer,
- Postleitzahl und Ort,
- Land und Verwaltungseinheit,
- geografische Position,
- `attentionOf`, `careOf` oder Abteilungstext.

### 15.2 Contact

Jeder vorhandene Wert von `conx-contact:hasContactPoint` wird durch das
Contact-Core-Shape geprüft. Das Organization Shape verlangt im Core keinen
Kontaktpunkt und keine Homepage.

Eine gültige offizielle Homepage verwendet:

```text
contact-usage:official
contact-purpose:general
contact-channel:website
contactURI als IRI
```

Eine neue Property `conx-org:homepage` wird weder im Shape noch in der T-Box
vorgesehen.

## 16. Fehlermeldungskatalog

### 16.1 Organization

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `ORG-001` | Eine Organisation muss durch eine IRI referenziert werden. | An Organization must be referenced by an IRI. |
| `ORG-002` | Eine Ressource mit Organisationseigenschaften muss als conx-org:Organization oder bestätigte Unterklasse typisiert sein. | A resource using Organization properties must be typed as conx-org:Organization or an established subclass. |
| `ORG-010` | Eine Organisation muss mindestens einen nicht leeren Namen besitzen. | An Organization must have at least one non-empty name. |
| `ORG-011` | Jeder alternative Name muss ein nicht leerer String oder sprachmarkierter String sein. | Every alternative name must be a non-empty string or language-tagged string. |
| `ORG-020` | Jede Tätigkeit muss auf ein referenzierbares SKOS-Konzept verweisen. | Every activity must reference a SKOS concept by IRI. |
| `ORG-030` | Jeder Organisationsidentifikator muss eine gültig strukturierte ADMS-Identifier-Ressource sein. | Every Organization identifier must be a valid structured ADMS Identifier resource. |
| `ORG-040` | Jede übergeordnete Organisation muss durch eine Organization-IRI referenziert werden. | Every parent organization must be referenced by an Organization IRI. |
| `ORG-041` | Jede untergeordnete Organisation muss durch eine Organization-IRI referenziert werden. | Every subordinate organization must be referenced by an Organization IRI. |
| `ORG-042` | Eine Organisation darf nicht unmittelbar sich selbst über- oder untergeordnet sein. | An Organization must not be its own direct parent or subordinate organization. |
| `ORG-043` | Jeder Wert von hasUnit muss auf eine OrganizationalUnit-IRI verweisen. | Every hasUnit value must reference an OrganizationalUnit IRI. |

### 16.2 Legal Entity

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `LE-001` | Eine Legal Entity muss durch eine IRI referenziert werden. | A Legal Entity must be referenced by an IRI. |
| `LE-002` | Eine Ressource mit Legal-Entity-Eigenschaften muss explizit als conx-org:LegalEntity typisiert sein. | A resource using Legal Entity properties must be explicitly typed as conx-org:LegalEntity. |
| `LE-003` | Eine Legal Entity muss den allgemeinen Organization-Vertrag erfüllen. | A Legal Entity must conform to the general Organization contract. |
| `LE-010` | Eine Legal Entity muss mindestens einen nicht leeren rechtlichen Namen besitzen. | A Legal Entity must have at least one non-empty legal name. |
| `LE-020` | Eine Legal Entity muss genau ein Registrierungsdatum mit dem Datentyp xsd:date besitzen. | A Legal Entity must have exactly one registration date using datatype xsd:date. |
| `LE-030` | Die Rechtsform darf höchstens einmal vorkommen und muss auf ein SKOS-Konzept verweisen. | The legal form may occur at most once and must reference a SKOS concept. |
| `LE-040` | Eine Legal Entity muss mindestens einen gültig strukturierten ADMS-Identifier besitzen. | A Legal Entity must have at least one valid structured ADMS Identifier. |
| `LE-050` | Eine Legal Entity muss mindestens eine AddressAssignment mit der Rolle LegalAddressRole besitzen. | A Legal Entity must have at least one AddressAssignment with the LegalAddressRole. |

### 16.3 Organizational Unit

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `UNIT-001` | Eine Organisationseinheit muss durch eine IRI referenziert werden. | An Organizational Unit must be referenced by an IRI. |
| `UNIT-002` | Eine Ressource mit Unit-Eigenschaften muss explizit als conx-org:OrganizationalUnit typisiert sein. | A resource using Organizational Unit properties must be explicitly typed as conx-org:OrganizationalUnit. |
| `UNIT-003` | Eine Organisationseinheit muss den allgemeinen Organization-Vertrag erfüllen. | An Organizational Unit must conform to the general Organization contract. |
| `UNIT-010` | Eine Organisationseinheit muss mindestens einer Organization über unitOf zugeordnet sein. | An Organizational Unit must be assigned to at least one Organization through unitOf. |
| `UNIT-011` | Eine Organisationseinheit darf nicht unitOf ihrer selbst sein. | An Organizational Unit must not be unitOf itself. |

### 16.4 Membership

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `MEM-001` | Eine Membership muss durch eine IRI referenziert werden. | A Membership must be referenced by an IRI. |
| `MEM-002` | Eine Mitgliedschaftsressource muss explizit als conx-org:Membership typisiert sein. | A membership resource must be explicitly typed as conx-org:Membership. |
| `MEM-010` | Eine Membership muss genau einen durch eine Agent-IRI referenzierten Member besitzen. | A Membership must have exactly one member referenced by an Agent IRI. |
| `MEM-011` | Eine Membership muss genau eine aufnehmende Organization besitzen. | A Membership must have exactly one membership Organization. |
| `MEM-012` | Jeder Mitgliedschaftsidentifikator muss eine gültig strukturierte ADMS-Identifier-Ressource sein. | Every Membership identifier must be a valid structured ADMS Identifier resource. |
| `MEM-020` | Eine Organisation darf nicht Mitglied ihrer selbst sein. | An Organization must not be a member of itself. |

### 16.5 Legal Representation

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `REP-001` | Eine LegalRepresentation muss durch eine IRI referenziert werden. | A LegalRepresentation must be referenced by an IRI. |
| `REP-002` | Eine Vertretungsressource muss explizit als conx-org:LegalRepresentation typisiert sein. | A representation resource must be explicitly typed as conx-org:LegalRepresentation. |
| `REP-010` | Eine LegalRepresentation muss genau eine Legal Entity als vertretene Organisation referenzieren. | A LegalRepresentation must reference exactly one Legal Entity as the represented organization. |
| `REP-011` | Eine LegalRepresentation muss genau eine Person als rechtliche Vertretung referenzieren. | A LegalRepresentation must reference exactly one Person as its legal representative. |

### 16.6 Geteilte ADMS-Meldungen

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `ID-001` | Eine Identifikatorressource muss als adms:Identifier typisiert sein. | An identifier resource must be typed as adms:Identifier. |
| `ID-002` | Ein Identifikator muss genau eine literale skos:notation besitzen. | An identifier must have exactly one literal skos:notation. |
| `ID-003` | schemaAgency darf höchstens einmal als String angegeben werden. | schemaAgency may be provided at most once as a string. |

## 17. Gemeinsame Präfixe der Beispielszenarien

Die folgenden Präfixe gelten für alle Beispiele dieses Dokuments:

```turtle
@prefix conx-agent: <https://www.construct-x.org/ontology/agent#> .
@prefix conx-person: <https://www.construct-x.org/ontology/person#> .
@prefix conx-org: <https://www.construct-x.org/ontology/organization#> .
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix roles: <https://www.construct-x.org/vocab/address-role#> .
@prefix contact-channel: <https://www.construct-x.org/vocab/contact-channel#> .
@prefix contact-purpose: <https://www.construct-x.org/vocab/contact-purpose#> .
@prefix contact-usage: <https://www.construct-x.org/vocab/contact-usage#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.org/id/> .
@prefix ex-scheme: <https://example.org/id-scheme/> .
```

Die Beispiel-Datentypen unter `ex-scheme:` sind Platzhalter für noch nicht
festgelegte Organization-Identifier-Schemata. Sie dürfen nicht als bereits
veröffentlichte Construct-X-Schemes interpretiert werden.

## 18. Gültige Szenarien

### V-01: Minimale allgemeine Organisation

```turtle
ex:bauverband
    a conx-org:Organization ;
    conx-org:name "Bauverband Beispielregion"@de .
```

Erwartung: gültig. Eine allgemeine Organization benötigt weder Rechtsform,
Registerdatum, Identifier noch Adresse.

### V-02: Vollständige Legal Entity

```turtle
ex:bau-gmbh
    a conx-org:LegalEntity ;
    conx-org:name "Bau Beispiel"@de ;
    conx-org:legalName "Bau Beispiel GmbH"@de ;
    conx-org:registrationDate "2018-04-12"^^xsd:date ;
    adms:identifier ex:bau-gmbh-register-id ;
    conx-addr:hasAddressAssignment ex:bau-gmbh-legal-address .

ex:bau-gmbh-register-id
    a adms:Identifier ;
    skos:notation "HRB 12345"^^ex-scheme:local-register-number ;
    adms:schemaAgency "Zuständige Registerstelle" .

ex:bau-gmbh-legal-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:bau-gmbh-address ;
    conx-addr:addressRole roles:LegalAddressRole,
                          roles:RegistrationAddressRole .

ex:bau-gmbh-address
    a conx-addr:Address ;
    conx-addr:streetName "Beispielstraße" ;
    conx-addr:houseNumber "12" ;
    conx-addr:postalCode "44787" ;
    conx-addr:localityName "Bochum" .
```

Erwartung: gültig. Dieselbe AddressAssignment erfüllt rechtliche und
Registeradressrolle.

### V-03: Legal Entity mit optionaler Rechtsform und Tätigkeit

```turtle
ex:planung-ag
    a conx-org:LegalEntity ;
    conx-org:name "Planung AG" ;
    conx-org:legalName "Planung Beispiel Aktiengesellschaft"@de ;
    conx-org:registrationDate "2020-02-03"^^xsd:date ;
    conx-org:legalForm ex:legal-form-ag ;
    conx-org:activity ex:nace-activity ;
    adms:identifier ex:planung-ag-id ;
    conx-addr:hasAddressAssignment ex:planung-ag-legal-address .

ex:legal-form-ag a skos:Concept .
ex:nace-activity a skos:Concept .

ex:planung-ag-id
    a adms:Identifier ;
    skos:notation "REG-9876"^^ex-scheme:local-register-number .

ex:planung-ag-legal-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:planung-ag-address ;
    conx-addr:addressRole roles:LegalAddressRole .

ex:planung-ag-address a conx-addr:Address .
```

Erwartung: gültig. Das Core Shape prüft die SKOS-Typen, aber nicht, ob die
Konzepte aus ISO 20275 oder NACE stammen.

### V-04: Organisationseinheit mit Matrixzuordnung

```turtle
ex:central-procurement
    a conx-org:OrganizationalUnit ;
    conx-org:name "Zentraler Einkauf"@de ;
    conx-org:unitOf ex:bau-gmbh,
                    ex:planung-ag .
```

Erwartung: gültig, sofern beide Zielressourcen als Organization oder Unterklasse
typisiert und im Validierungsgraph verfügbar sind. Mehrere `unitOf`-Werte sind
im Core erlaubt.

### V-05: Mitgliedschaft einer Organisation

```turtle
ex:membership-4711
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh ;
    conx-org:membershipOrganization ex:bauverband ;
    adms:identifier ex:membership-number-4711 .

ex:membership-number-4711
    a adms:Identifier ;
    skos:notation "4711"^^ex-scheme:association-membership-number ;
    adms:schemaAgency "Bauverband Beispielregion" .
```

Erwartung: gültig. Die Mitgliedsnummer gehört zur Membership.

### V-06: Mitgliedschaft einer Person

```turtle
ex:person-123 a conx-person:Person ;
    conx-person:fullName "Maria Beispiel" ;
    conx-person:givenName "Maria" .

ex:person-membership
    a conx-org:Membership ;
    conx-org:member ex:person-123 ;
    conx-org:membershipOrganization ex:bauverband .
```

Erwartung: gültig. `Person` ist über die geladene T-Box eine Unterklasse von
`Agent`.

### V-07: Rechtliche Vertretung

```turtle
ex:representation-1
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123 .
```

Erwartung: gültig. Die Vertretung verweist auf die Person und enthält keine
kopierten Personendaten.

### V-08: Offizielle Homepage über Contact

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

Erwartung: gültig im gemeinsamen Organization-, Contact- und Address-
Validierungslauf. Das Organization Shape verlangt keine eigene Homepage-
Property.

### V-09: Hierarchie in einer Datenrichtung

```turtle
ex:regional-office
    a conx-org:Organization ;
    conx-org:name "Regionalorganisation West"@de ;
    conx-org:subOrganizationOf ex:bauverband .
```

Erwartung: gültig. `ex:bauverband conx-org:hasSubOrganization
ex:regional-office` muss nicht zusätzlich explizit gespeichert werden.

## 19. Ungültige Szenarien

### I-01: Organization als Blank Node

```turtle
[] a conx-org:Organization ;
   conx-org:name "Nicht stabil referenzierbar" .
```

Erwartete Verletzung: `ORG-001`.

### I-02: Organization-Property ohne Organization-Typ und ohne Namen

```turtle
ex:untyped-resource
    conx-org:alternativeName "Beispiel" .
```

Erwartete Verletzungen: `ORG-002`, `ORG-010`.

### I-03: Ungültige Namen und Tätigkeit

```turtle
ex:invalid-name-org
    a conx-org:Organization ;
    conx-org:name "   ", 42 ;
    conx-org:alternativeName "" ;
    conx-org:activity "Bauwirtschaft" .
```

Erwartete Verletzungen: `ORG-010`, `ORG-011`, `ORG-020`. Eine Tätigkeit muss
als IRI auf ein SKOS-Konzept verweisen.

### I-04: Unvollständige Legal Entity

```turtle
ex:incomplete-company
    a conx-org:LegalEntity ;
    conx-org:name "Unvollständig" .
```

Erwartete Verletzungen: `LE-010`, `LE-020`, `LE-040`, `LE-050`.

### I-05: Falsche und mehrere Registerdaten

```turtle
ex:invalid-date-company
    a conx-org:LegalEntity ;
    conx-org:name "Datum Fehler" ;
    conx-org:legalName "Datum Fehler GmbH" ;
    conx-org:registrationDate "2020"^^xsd:gYear,
                              "2020-01-02"^^xsd:date .
```

Erwartete Verletzung: `LE-020`; zusätzlich fehlen in diesem isolierten Beispiel
Identifier und Legal Address (`LE-040`, `LE-050`).

### I-06: Rechtsform als Literal und mehrfach

```turtle
ex:invalid-legal-form-company
    a conx-org:LegalEntity ;
    conx-org:legalForm "GmbH",
                       ex:legal-form-gmbh .

ex:legal-form-gmbh a skos:Concept .
```

Erwartete Verletzung: `LE-030`; weitere Legal-Entity-Pflichtverletzungen können
im isolierten Beispiel zusätzlich auftreten.

### I-07: Identifier ohne Typ oder Notation

```turtle
ex:invalid-identifier-company
    a conx-org:LegalEntity ;
    conx-org:name "Kennungsfehler" ;
    conx-org:legalName "Kennungsfehler GmbH" ;
    conx-org:registrationDate "2021-05-06"^^xsd:date ;
    adms:identifier ex:broken-identifier .

ex:broken-identifier
    adms:schemaAgency "Registerstelle" .
```

Erwartete Verletzungen: `ORG-030` beziehungsweise `LE-040`, `ID-001`,
`ID-002`; zusätzlich fehlt die Legal Address (`LE-050`).

### I-08: Adresse ohne Legal-Address-Rolle

```turtle
ex:no-legal-address-company
    a conx-org:LegalEntity ;
    conx-org:name "Adressfehler" ;
    conx-org:legalName "Adressfehler GmbH" ;
    conx-org:registrationDate "2019-03-04"^^xsd:date ;
    adms:identifier ex:valid-company-id ;
    conx-addr:hasAddressAssignment ex:postal-only-assignment .

ex:valid-company-id
    a adms:Identifier ;
    skos:notation "REG-1"^^ex-scheme:local-register-number .

ex:postal-only-assignment
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:postal-address ;
    conx-addr:addressRole roles:PostalAddressRole .

ex:postal-address a conx-addr:Address .
```

Erwartete Verletzung: `LE-050`. Die vorhandene Postadresse ersetzt die
rechtliche Adressrolle nicht.

### I-09: Organisationseinheit ohne übergeordnete Organization

```turtle
ex:orphan-unit
    a conx-org:OrganizationalUnit ;
    conx-org:name "Verwaiste Einheit" .
```

Erwartete Verletzung: `UNIT-010`.

### I-10: Organisationseinheit zeigt auf sich selbst

```turtle
ex:self-unit
    a conx-org:OrganizationalUnit ;
    conx-org:name "Selbstbezug" ;
    conx-org:unitOf ex:self-unit .
```

Erwartete Verletzung: `UNIT-011`.

### I-11: Ungültige Organisationshierarchie

```turtle
ex:self-parent
    a conx-org:Organization ;
    conx-org:name "Selbsthierarchie" ;
    conx-org:subOrganizationOf ex:self-parent .

ex:wrong-parent
    a conx-org:Organization ;
    conx-org:name "Falsche Oberorganisation" ;
    conx-org:subOrganizationOf ex:not-an-organization .

ex:wrong-child
    a conx-org:Organization ;
    conx-org:name "Falsche Unterorganisation" ;
    conx-org:hasSubOrganization ex:not-an-organization .

ex:wrong-unit-target
    a conx-org:Organization ;
    conx-org:name "Falsches Unit-Ziel" ;
    conx-org:hasUnit ex:not-a-unit .

ex:not-an-organization a skos:Concept .

ex:not-a-unit a conx-org:Organization ;
    conx-org:name "Keine Organisationseinheit" .
```

Erwartete Verletzungen: `ORG-040`, `ORG-041`, `ORG-042`, `ORG-043`.

### I-12: Membership ohne eindeutige Endpunkte

```turtle
ex:invalid-membership
    a conx-org:Membership ;
    conx-org:member ex:bau-gmbh,
                    ex:planung-ag .
```

Erwartete Verletzungen: `MEM-010`, `MEM-011`.

### I-13: Selbstmitgliedschaft

```turtle
ex:self-membership
    a conx-org:Membership ;
    conx-org:member ex:bauverband ;
    conx-org:membershipOrganization ex:bauverband .
```

Erwartete Verletzung: `MEM-020`.

### I-14: Vertretung verweist nicht auf eine Person

```turtle
ex:invalid-representation
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:bauverband .
```

Erwartete Verletzung: `REP-011`, weil `ex:bauverband` eine Organization und
keine Person ist.

### I-15: Vertretung mit mehreren Personen

```turtle
ex:ambiguous-representation
    a conx-org:LegalRepresentation ;
    conx-org:representedOrganization ex:bau-gmbh ;
    conx-org:representative ex:person-123,
                            ex:person-456 .
```

Erwartete Verletzung: `REP-011`. Mehrere Vertreter benötigen mehrere
Vertretungsressourcen; gemeinsame Vertretungsregeln sind nicht Teil des MVP.

### I-16: Website als Organization-Property oder Literalpayload

```turtle
ex:bau-gmbh
    conx-org:homepage "https://example.org/" ;
    conx-contact:hasContactPoint ex:broken-contact .

ex:broken-contact
    a conx-contact:ContactPoint ;
    conx-contact:hasContactMethod ex:broken-website .

ex:broken-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactValue "https://example.org/" .
```

Erwartung: `conx-org:homepage` wird vom offenen Organization Shape nicht als
bekannte Core-Property validiert, besitzt aber auch keine definierte
Construct-X-Semantik. Das Contact Shape meldet für den Literalpayload der
Website `CON-CM-020`. Dieses Szenario dokumentiert bewusst, dass offene Shapes
unbekannte Properties nicht verbieten.

## 20. Implementierter Testkatalog

### 20.1 Gültige Testgraphen

| Datei | Inhalt |
| --- | --- |
| `tests/valid/minimal-organization.ttl` | allgemeine Organization nur mit Name |
| `tests/valid/complete-legal-entity.ttl` | Legal Name, Registerdatum, Identifier, Legal Address, optionale Rechtsform und Tätigkeit |
| `tests/valid/organizational-unit.ttl` | Einheit mit einer und mehreren `unitOf`-Zuordnungen |
| `tests/valid/memberships.ttl` | Person- und Organization-Mitgliedschaften mit optionaler Mitgliedsnummer |
| `tests/valid/legal-representation.ttl` | Vertretungsressource zwischen Legal Entity und Person |
| `tests/valid/official-homepage.ttl` | Organization mit offizieller Website über Contact |

### 20.2 Ungültige Testgraphen

| Datei | Erwartete Fehlercodes |
| --- | --- |
| `tests/invalid/invalid-organization-name-and-type.ttl` | `ORG-001`, `ORG-002`, `ORG-010`, `ORG-011`, `ORG-020` |
| `tests/invalid/invalid-legal-entity-core.ttl` | `LE-001`, `LE-002`, `LE-003`, `LE-010`, `LE-020`, `LE-040`, `LE-050` |
| `tests/invalid/invalid-registration-and-legal-form.ttl` | `LE-020`, `LE-030` |
| `tests/invalid/invalid-identifier-and-address.ttl` | `ORG-030`, `LE-040`, `LE-050`, `ID-001`, `ID-002`, `ID-003` |
| `tests/invalid/invalid-organizational-unit.ttl` | `UNIT-001`, `UNIT-002`, `UNIT-003`, `UNIT-010`, `UNIT-011` |
| `tests/invalid/invalid-hierarchy.ttl` | `ORG-040`, `ORG-041`, `ORG-042`, `ORG-043` |
| `tests/invalid/invalid-membership.ttl` | `MEM-001`, `MEM-002`, `MEM-010`, `MEM-011`, `MEM-012`, `MEM-020` |
| `tests/invalid/invalid-legal-representation.ttl` | `REP-001`, `REP-002`, `REP-010`, `REP-011` |

## 21. Anforderungen an automatisierte Tests

Die automatisierten Tests prüfen mindestens:

1. Jeder gültige Testgraph validiert ohne `sh:Violation`.
2. Jeder ungültige Testgraph erzeugt alle für ihn dokumentierten Fehlercodes.
3. Jede lokale Shape-IRI und jeder Fehlercode ist eindeutig.
4. Alle Shape-Meldungen liegen auf Deutsch und Englisch vor.
5. Organization-, Agent-, Person-, Address- und Contact-T-Boxen werden im
   gemeinsamen Validierungslauf berücksichtigt.
6. Address- und Contact-Core-Shapes werden gemeinsam geladen, sobald der
   Testgraph entsprechende Properties verwendet.
7. Eine Legal Entity besteht nur mit Name, Legal Name, genau einem
   Registerdatum, mindestens einem ADMS-Identifier und mindestens einer Legal
   Address.
8. Eine Organization ohne rechtliche Spezialisierung bleibt ohne Registerdatum,
   Identifier und Adresse gültig.
9. Eine Organizational Unit besteht nur mit Name und mindestens einem `unitOf`.
10. Membership und LegalRepresentation erzwingen jeweils genau einen Wert pro
    Endpunktproperty.
11. Blank Nodes für die fünf lokalen MVP-Klassen werden abgelehnt.
12. Direkte Selbsthierarchie, Selbst-Unit und Selbstmitgliedschaft werden
    abgelehnt.
13. Inverse Hierarchierichtungen werden nicht beide als Eingabepflicht verlangt.
14. Das Organization Shape bleibt offen und verbietet keine fremden Properties.
15. Keine Regel verlangt `EconomicActor`, lokale `FormalOrganization`, `Post`,
    Credential-Klasse oder `homepage`.
16. Jeder dokumentierte Fehlercode wird von mindestens einem ungültigen
    Testgraphen ausgelöst.

## 22. Bewusst nicht im Core geprüft

- geschlossene Liste zulässiger Register- und Steuerkennungsschemata,
- Live-Prüfung gegen BRIS, VIES, GLEIF, EORI oder nationale Register,
- Abgleich von Legal Name, Rechtsform und Adresse mit Registerdaten,
- Vollständigkeit einer Adresse nach nationalem Recht,
- Pflicht einer separaten Headquarters-Adresse,
- geschlossene ISO-20275- oder NACE-Wertemenge,
- zukünftiges oder historisches Registerdatum,
- Eigentums- und Kontrollbeziehungen,
- längere Organisationshierarchiezyklen,
- Rolle, Status und Zeitraum einer Membership,
- Art, Zeitraum und Gesamtvertretungsregeln einer LegalRepresentation,
- Nachweise zu Mitgliedschaft, Versicherung oder Befähigung,
- KMU-, Steuer-, Bonitäts- und Sanktionsstatus,
- Bankkonten und Zahlungsdaten,
- Prozessrollen wie Buyer, Seller oder Carrier,
- Zugriffsschutz oder Datenschutzregeln,
- allgemeine Provenienz und Aussagehistorie.

## 23. Umsetzungsstand

Die `.shacl.ttl`-Implementierung setzt folgende bestätigte Punkte um:

1. der Shape-Katalog mit fünf fachlichen Node Shapes bestätigt ist,
2. `registrationDate` als verpflichtender Einzelwert bestätigt bleibt,
3. das strukturelle Identifier-Minimum trotz offener Schemaliste bestätigt ist,
4. mindestens eine Legal Address im Legal Entity Core bestätigt ist,
5. `legalForm` optional bleibt,
6. Mitgliedschaft und Vertretung ohne Rolle, Zeitraum und Credential ausreichen,
7. IRI-Pflicht für Membership und LegalRepresentation bestätigt ist,
8. die dokumentierten Fehlercodes und Testszenarien als Implementierungsvertrag
   akzeptiert sind.

T-Box, Shape-Graph, gültige und ungültige Testgraphen sowie automatisierte
Tests sind für Version `0.1.0` umgesetzt. HTML-Dokumentation und
Netzwerkmetadaten werden im anschließenden Dokumentationsschritt aktualisiert.
