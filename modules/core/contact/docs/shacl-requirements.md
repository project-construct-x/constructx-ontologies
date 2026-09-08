# Fachliche SHACL-Anforderungen für das Kontaktmodul

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Contact Core Shapes

## 1. Zweck

Dieses Dokument legt die Datenqualitätsanforderungen für das Kontaktmodul fest. Es beschreibt Shape-Targets, Constraints, Schweregrade, Fehlermeldungen sowie gültige und ungültige Szenarien. Der ausführbare Shape-Graph ist in `modules/core/contact/shapes/conx-contact-core.shacl.ttl` umgesetzt.

## 2. Umgesetztes Shape-Set

```text
Shape-Graph:  modules/core/contact/shapes/conx-contact-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/contact/core
Versions-IRI: https://www.construct-x.org/shapes/contact/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/contact/core#
Prefix:       conx-contact-sh
Version:      0.1.0
```

## 3. Validierungsprinzipien

### 3.1 OWL und SHACL

- OWL beschreibt die offene Bedeutung der Begriffe.
- SHACL prüft den konkret gelieferten Datengraphen.
- Pflichtfelder, Maximalwerte und kanalspezifische Wertformen werden im Core-Shape geprüft.
- Die Shapes bleiben für zusätzliche Properties offen; `sh:closed true` ist nicht vorgesehen.
- SHACL-Maximalwerte werden nicht automatisch als OWL-Kardinalitäten übernommen.

### 3.2 Schweregrade

Alle Core-Verstöße verwenden `sh:Violation`. Empfehlungen wie `contactPlatform` bei Social Profiles oder `availableLanguage` bei Supportkontakten erzeugen im Core keine Warnung.

Anwendungsprofile dürfen später strengere Regeln mit `sh:Warning` oder `sh:Info` ergänzen.

### 3.3 Fehlermeldungen

Jede Constraint-Komponente erhält mindestens:

- eine deutsche `sh:message`,
- eine englische `sh:message`,
- einen stabilen Anforderungsbezeichner,
- einen nachvollziehbaren Ergebnispfad.

### 3.4 Referenzdaten

Die Validierung muss gemeinsam mit den freigegebenen Kontaktvokabularen ausgeführt werden:

- Construct-X `contact-channel`,
- Construct-X `contact-usage`,
- Construct-X `contact-purpose`,
- Construct-X `contact-platform`,
- Construct-X Address Ontology beziehungsweise Address-Core-Daten, wenn `postalAddress` verwendet wird.

Die kleinen Startwertemengen können im ersten Shape-Set als geschlossene `sh:in`-Listen aufgenommen werden. Alternativ können Typ und `skos:inScheme` gegen geladene Referenzgraphen geprüft werden. Für Version `0.1.0` ist eine geschlossene Startmenge fachlich vorzuziehen, damit neue Werte bewusst versioniert werden.

## 4. Verantwortungsgrenzen

| Anforderung | Zuständiges Shape-Set | Regel im Kontakt-Shape |
| --- | --- | --- |
| Kontaktträger verweist auf Kontaktpunkt | `contact/core` | Werte von `hasContactPoint` prüfen |
| Kontaktpunkt und Kontaktmethoden | `contact/core` | Vollständig validieren |
| Kontaktkanal, Nutzung und Zweck | `contact/core` plus Referenzvokabulare | Werte gegen freigegebene Vokabulare prüfen |
| Postalische Kontaktadresse | `contact/core` plus `address/core` | `usesAddressAssignment` verlangt `conx-addr:AddressAssignment`; Address-Details prüft Address-Shape |
| Personendaten | `person/core` | Nicht im Kontakt-Shape prüfen |
| Organisationsstruktur | `organization/core` | Nicht im Kontakt-Shape prüfen |
| Lieferscheinpflichten | `domain/delivery-note` | Nicht im Kontakt-Core erzwingen |
| Zugriff, Einwilligung und Geheimhaltung | Governance- oder Datenschutzprofil | Nicht im Kontakt-Core prüfen |

## 5. Shape-Katalog

| Shape-IRI | Typ | Target beziehungsweise Verwendung | Aufgabe |
| --- | --- | --- | --- |
| `conx-contact-sh:NonEmptyStringOrLangStringShape` | wiederverwendbares Node Shape | von Textwerten referenziert | Erlaubt nicht leere `xsd:string`- und `rdf:langString`-Werte |
| `conx-contact-sh:NonEmptyStringShape` | wiederverwendbares Node Shape | von technischen Werten referenziert | Erlaubt nicht leere `xsd:string`-Werte |
| `conx-contact-sh:ContactCarrierShape` | Node Shape | Subjekte von `conx-contact:hasContactPoint` | Prüft Werte von `hasContactPoint`, ohne das Subjekt hart als Agent zu typisieren |
| `conx-contact-sh:ContactPointShape` | Node Shape | `conx-contact:ContactPoint` und Objekte von `hasContactPoint` | Prüft Kontaktblock, Usage, Purpose und Methoden |
| `conx-contact-sh:ContactMethodShape` | Node Shape | `conx-contact:ContactMethod` und Objekte von `hasContactMethod` | Prüft Kanal und kanalspezifischen Payload |
| `conx-contact-sh:ContactChannelConceptShape` | Node Shape | Werte von `contactChannel` | Prüft freigegebene Kanalwerte |
| `conx-contact-sh:ContactUsageConceptShape` | Node Shape | Werte von `contactUsage` | Prüft freigegebene Usage-Werte |
| `conx-contact-sh:ContactPurposeConceptShape` | Node Shape | Werte von `contactPurpose` | Prüft freigegebene Purpose-Werte |
| `conx-contact-sh:ContactPlatformConceptShape` | Node Shape | Werte von `contactPlatform` | Prüft freigegebene Plattformwerte |
| `conx-contact-sh:PostalAddressAssignmentReferenceShape` | Node Shape | Werte von `usesAddressAssignment` | Prüft Referenz auf `conx-addr:AddressAssignment` |

## 6. Targets

### 6.1 `ContactCarrierShape`

Target:

- `sh:targetSubjectsOf conx-contact:hasContactPoint`.

Das Shape verlangt keinen expliziten Typ `conx-agent:Agent`. Die fachliche Lesrichtung bleibt zwar `Agent -> ContactPoint`, aber eine harte Typisierung im Core-Shape würde spätere Kontaktträger wie Projekte, Baustellen oder Services blockieren.

### 6.2 `ContactPointShape`

Targets:

- `sh:targetClass conx-contact:ContactPoint`,
- `sh:targetObjectsOf conx-contact:hasContactPoint`,
- `sh:targetSubjectsOf conx-contact:hasContactMethod`,
- `sh:targetSubjectsOf conx-contact:contactUsage`,
- `sh:targetSubjectsOf conx-contact:contactPurpose`,
- `sh:targetSubjectsOf conx-contact:contactName`,
- `sh:targetSubjectsOf conx-contact:departmentName`,
- `sh:targetSubjectsOf conx-contact:functionTitle`,
- `sh:targetSubjectsOf conx-contact:availableLanguage`,
- `sh:targetSubjectsOf conx-contact:availabilityNote`,
- `sh:targetSubjectsOf conx-contact:isContactPointFor`.

Ressourcen, die wie Kontaktpunkte verwendet werden, müssen dadurch explizit als `conx-contact:ContactPoint` typisiert sein.

### 6.3 `ContactMethodShape`

Targets:

- `sh:targetClass conx-contact:ContactMethod`,
- `sh:targetObjectsOf conx-contact:hasContactMethod`,
- `sh:targetSubjectsOf conx-contact:contactChannel`,
- `sh:targetSubjectsOf conx-contact:contactValue`,
- `sh:targetSubjectsOf conx-contact:contactURI`,
- `sh:targetSubjectsOf conx-contact:usesAddressAssignment`,
- `sh:targetSubjectsOf conx-contact:contactPlatform`.

Ressourcen, die Kanalwerte tragen, müssen dadurch explizit als `conx-contact:ContactMethod` typisiert sein.

## 7. Node-Constraints

| ID | Fokus | Constraint | SHACL-Anforderung |
| --- | --- | --- | --- |
| `CON-CAR-001` | Kontaktträger | Werte von `hasContactPoint` | Jeder Wert muss Blank Node oder IRI und `conx-contact:ContactPoint` sein |
| `CON-CP-001` | `ContactPoint` | Ressourcenform | Kontaktpunkte müssen Blank Node oder IRI sein |
| `CON-CP-002` | `ContactPoint` | Expliziter Typ | Kontaktpunkte müssen explizit `conx-contact:ContactPoint` sein |
| `CON-CM-001` | `ContactMethod` | Ressourcenform | Kontaktmethoden müssen Blank Node oder IRI sein |
| `CON-CM-002` | `ContactMethod` | Expliziter Typ | Kontaktmethoden müssen explizit `conx-contact:ContactMethod` sein |

Kontaktpunkte und Kontaktmethoden dürfen im Core als Blank Nodes modelliert werden. IRIs sind für wiederverwendbare oder separat zu pflegende Kontakte empfohlen, aber nicht zwingend.

## 8. Property-Constraints für `ContactPoint`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `CON-CP-010` | `hasContactMethod` | 1 | offen | Blank Node oder IRI, explizit `conx-contact:ContactMethod` |
| `CON-CP-020` | `contactUsage` | 0 | 1 | IRI aus `contact-usage` |
| `CON-CP-021` | `contactPurpose` | 0 | offen | IRI aus `contact-purpose` |
| `CON-CP-030` | `contactName` | 0 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `CON-CP-031` | `departmentName` | 0 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `CON-CP-032` | `functionTitle` | 0 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `CON-CP-033` | `availableLanguage` | 0 | offen | Nicht leerer Sprachcode als `xsd:string`; BCP-47 fachlich empfohlen |
| `CON-CP-034` | `availabilityNote` | 0 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `CON-CP-040` | `isContactPointFor` | 0 | offen | Blank Node oder IRI; keine Pflicht zur inversen Pflege |

`contactUsage` beschreibt den Nutzungskontext. `contactPurpose` beschreibt die fachliche Funktion. Beide dürfen nicht zu einer unscharfen Property `contactType` zusammengelegt werden.

## 9. Property-Constraints für `ContactMethod`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `CON-CM-010` | `contactChannel` | 1 | 1 | IRI aus `contact-channel` |
| `CON-CM-020` | Payload | 1 | 1 | Genau eine zulässige Wertform gemäß Kanal |
| `CON-CM-030` | `contactValue` | kanalabhängig | kanalabhängig | Nicht leerer `xsd:string` |
| `CON-CM-031` | `contactURI` | kanalabhängig | kanalabhängig | IRI |
| `CON-CM-032` | `usesAddressAssignment` | kanalabhängig | kanalabhängig | IRI oder Blank Node vom Typ `conx-addr:AddressAssignment` |
| `CON-CM-033` | `contactPlatform` | 0 | 1 | IRI aus `contact-platform` |

Payload bedeutet hier der konkrete Kontaktwert. Je Methode ist genau ein Payload-Typ zulässig:

- `contactValue`,
- `contactURI`,
- `usesAddressAssignment`.

Eine Methode darf nicht gleichzeitig eine Telefonnummer, eine URL und eine Adresszuordnung tragen.

## 10. Kanalbezogene Payload-Regeln

| Kanal | Erforderlicher Payload | Nicht zulässig im Core | Hinweis |
| --- | --- | --- | --- |
| `contact-channel:email` | genau ein `contactValue` als nicht leerer String | `contactURI`, `usesAddressAssignment` | Strenge Mail-Syntax späteres Profil |
| `contact-channel:phone` | genau ein `contactValue` als nicht leerer String | `contactURI`, `usesAddressAssignment` | Internationale Formatierung nicht im Core erzwingen |
| `contact-channel:mobilePhone` | genau ein `contactValue` als nicht leerer String | `contactURI`, `usesAddressAssignment` | Spezifischer Mobilfunkkanal |
| `contact-channel:fax` | genau ein `contactValue` als nicht leerer String | `contactURI`, `usesAddressAssignment` | UBL `Telefax`, schema.org `faxNumber` |
| `contact-channel:website` | genau ein `contactURI` | `contactValue`, `usesAddressAssignment` | IRI statt freiem String |
| `contact-channel:socialProfile` | genau ein `contactURI` | `contactValue`, `usesAddressAssignment` | Plattform optional als Wert aus `contact-platform` |
| `contact-channel:messenger` | genau ein `contactValue` oder genau ein `contactURI` | `usesAddressAssignment` | Handle oder URI je Plattform |
| `contact-channel:postalAddress` | genau ein `usesAddressAssignment` | `contactValue`, `contactURI` | Verweist auf `conx-addr:AddressAssignment` |

Die Syntaxvalidierung für E-Mail und Telefonnummern bleibt bewusst pragmatisch. Ein zu strenges Regex im Core würde echte internationale oder quellspezifische Werte ablehnen. Strengere Profile dürfen E.164, `mailto:` oder organisationsspezifische Regeln verlangen.

## 11. Kontrollierte Werte

### 11.1 `contact-channel`

Die zulässige Startmenge lautet:

```text
contact-channel:email
contact-channel:phone
contact-channel:mobilePhone
contact-channel:fax
contact-channel:website
contact-channel:messenger
contact-channel:socialProfile
contact-channel:postalAddress
```

### 11.2 `contact-usage`

Die zulässige Startmenge lautet:

```text
contact-usage:private
contact-usage:business
contact-usage:official
```

`contact-usage:private` ist keine Zugriffsbeschränkung. Es bezeichnet nur den fachlichen Verwendungskontext.

### 11.3 `contact-purpose`

Die zulässige Startmenge lautet:

```text
contact-purpose:general
contact-purpose:delivery
contact-purpose:billing
contact-purpose:support
contact-purpose:sales
contact-purpose:technical
contact-purpose:emergency
```

### 11.4 `contact-platform`

Das Plattformvokabular ist Teil des MVP. Die Startmenge lautet:

```text
contact-platform:linkedin
contact-platform:instagram
contact-platform:x
contact-platform:facebook
contact-platform:github
contact-platform:whatsapp
contact-platform:signal
contact-platform:microsoftTeams
```

Das Shape prüft vorhandene Plattformwerte gegen diese freigegebene Startmenge.

## 12. Postalische Kontaktadressen

Postalische Kontaktmethoden verwenden ausschließlich:

```text
ContactMethod -> usesAddressAssignment -> conx-addr:AddressAssignment
```

Der direkte Verweis auf `conx-addr:Address` ist im Kontakt-MVP nicht zulässig. Grund: `AddressAssignment` trägt die fachliche Verwendung der Adresse, etwa Lieferadresse, Rechnungsadresse, Meldeadresse, Abteilung, z. Hd. und c/o. Diese Informationen dürfen bei postalischer Kontaktierbarkeit nicht abgeschnitten werden.

Das Kontakt-Shape prüft nur:

- genau ein `usesAddressAssignment` bei Kanal `postalAddress`,
- Wert ist Blank Node oder IRI,
- Wert ist `conx-addr:AddressAssignment`.

Die innere Adressstruktur, `assignedAddress`, `addressRole` und Adressbestandteile prüft das Address-Core-Shape.

## 13. Fehlermeldungskatalog

### 13.1 Kontaktträger

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `CON-CAR-001` | Jeder Wert von hasContactPoint muss eine ContactPoint-Ressource sein. | Every hasContactPoint value must be a ContactPoint resource. |

### 13.2 Kontaktpunkte

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `CON-CP-001` | Ein ContactPoint muss eine Ressource sein und darf kein Literal sein. | A ContactPoint must be a resource and must not be a literal. |
| `CON-CP-002` | Eine als Kontaktpunkt verwendete Ressource muss explizit als conx-contact:ContactPoint typisiert sein. | A resource used as contact point must be explicitly typed as conx-contact:ContactPoint. |
| `CON-CP-010` | Ein ContactPoint muss mindestens eine ContactMethod besitzen. | A ContactPoint must have at least one ContactMethod. |
| `CON-CP-020` | contactUsage darf höchstens einmal vorkommen und muss auf einen freigegebenen Usage-Wert verweisen. | contactUsage may occur at most once and must reference an approved usage value. |
| `CON-CP-021` | Jeder contactPurpose-Wert muss auf einen freigegebenen Purpose-Wert verweisen. | Every contactPurpose value must reference an approved purpose value. |
| `CON-CP-030` | contactName muss ein nicht leerer String oder sprachmarkierter String sein. | contactName must be a non-empty string or language-tagged string. |
| `CON-CP-031` | departmentName muss ein nicht leerer String oder sprachmarkierter String sein. | departmentName must be a non-empty string or language-tagged string. |
| `CON-CP-032` | functionTitle muss ein nicht leerer String oder sprachmarkierter String sein. | functionTitle must be a non-empty string or language-tagged string. |
| `CON-CP-033` | availableLanguage muss als nicht leerer Sprachcode angegeben werden. | availableLanguage must be provided as a non-empty language code. |
| `CON-CP-034` | availabilityNote muss ein nicht leerer String oder sprachmarkierter String sein. | availabilityNote must be a non-empty string or language-tagged string. |
| `CON-CP-040` | isContactPointFor darf nur auf Ressourcen zeigen. | isContactPointFor may only reference resources. |

### 13.3 Kontaktmethoden

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `CON-CM-001` | Eine ContactMethod muss eine Ressource sein und darf kein Literal sein. | A ContactMethod must be a resource and must not be a literal. |
| `CON-CM-002` | Eine als Kontaktmethode verwendete Ressource muss explizit als conx-contact:ContactMethod typisiert sein. | A resource used as contact method must be explicitly typed as conx-contact:ContactMethod. |
| `CON-CM-010` | Eine ContactMethod muss genau einen freigegebenen Kontaktkanal besitzen. | A ContactMethod must have exactly one approved contact channel. |
| `CON-CM-020` | Eine ContactMethod muss genau einen zum Kanal passenden Payload besitzen. | A ContactMethod must have exactly one payload matching its channel. |
| `CON-CM-030` | contactValue muss als nicht leerer String angegeben werden, wenn der Kanal einen Literalwert verlangt. | contactValue must be provided as a non-empty string when the channel requires a literal value. |
| `CON-CM-031` | contactURI muss eine IRI sein, wenn der Kanal eine URI verlangt. | contactURI must be an IRI when the channel requires a URI. |
| `CON-CM-032` | Eine postalische Kontaktmethode muss genau eine conx-addr:AddressAssignment referenzieren. | A postal contact method must reference exactly one conx-addr:AddressAssignment. |
| `CON-CM-033` | contactPlatform darf höchstens einmal vorkommen und muss auf eine freigegebene Plattform verweisen. | contactPlatform may occur at most once and must reference an approved platform. |

## 14. Gültige Szenarien

### V-01: Privater Kontaktpunkt mit E-Mail und Mobiltelefon

```turtle
ex:person-1
    conx-contact:hasContactPoint ex:person-1-private-contact .

ex:person-1-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-1-private-email,
                                  ex:person-1-private-mobile .

ex:person-1-private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .

ex:person-1-private-mobile
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:mobilePhone ;
    conx-contact:contactValue "+49 171 1234567" .
```

Erwartung: gültig.

### V-02: Beruflicher Lieferkontakt mit postalischer Adresszuordnung

```turtle
ex:company-1
    conx-contact:hasContactPoint ex:company-1-delivery-contact .

ex:company-1-delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:delivery ;
    conx-contact:contactName "Wareneingang Tor 4"@de ;
    conx-contact:hasContactMethod ex:company-1-delivery-email,
                                  ex:company-1-delivery-postal .

ex:company-1-delivery-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "wareneingang@example.org" .

ex:company-1-delivery-postal
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesAddressAssignment ex:company-1-delivery-address-assignment .

ex:company-1-delivery-address-assignment
    a conx-addr:AddressAssignment ;
    conx-addr:addressRole roles:DeliveryAddressRole ;
    conx-addr:assignedAddress ex:address-1 .

ex:address-1
    a conx-addr:Address .
```

Erwartung: gültig, wenn das Address-Core-Shape die Adresszuordnung akzeptiert.

### V-03: Offizieller Website-Kontakt

```turtle
ex:agent-1
    conx-contact:hasContactPoint ex:agent-1-official-contact .

ex:agent-1-official-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:official ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:agent-1-website .

ex:agent-1-website
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactURI <https://example.org/contact> .
```

Erwartung: gültig.

### V-04: Social Profile mit Plattform

```turtle
ex:person-2
    conx-contact:hasContactPoint ex:person-2-business-contact .

ex:person-2-business-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-2-linkedin .

ex:person-2-linkedin
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin ;
    conx-contact:contactURI <https://www.linkedin.com/in/example> .
```

Erwartung: gültig.

### V-05: Messenger mit Handle

```turtle
ex:support-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactPurpose contact-purpose:support ;
    conx-contact:hasContactMethod ex:support-chat .

ex:support-chat
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:messenger ;
    conx-contact:contactValue "@support-desk" .
```

Erwartung: gültig.

## 15. Ungültige Szenarien

### I-01: Kontaktpunkt als Literal

```turtle
ex:person-1
    conx-contact:hasContactPoint "max@example.org" .
```

Erwarteter Verstoss: `CON-CAR-001`.

### I-02: Kontaktpunkt ohne Methode

```turtle
ex:contact-1
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private .
```

Erwarteter Verstoss: `CON-CP-010`.

### I-03: Kontaktmethode ohne Kanal

```turtle
ex:method-1
    a conx-contact:ContactMethod ;
    conx-contact:contactValue "max@example.org" .
```

Erwarteter Verstoss: `CON-CM-010`.

### I-04: Kontaktmethode mit mehreren Kanälen

```turtle
ex:method-2
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email,
                                contact-channel:phone ;
    conx-contact:contactValue "max@example.org" .
```

Erwarteter Verstoss: `CON-CM-010`.

### I-05: Unbekannter Kanal

```turtle
ex:method-3
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel ex:unsupported-channel ;
    conx-contact:contactValue "max@example.org" .
```

Erwarteter Verstoss: `CON-CM-010`.

### I-06: Website als Literal statt IRI

```turtle
ex:method-4
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:website ;
    conx-contact:contactValue "https://example.org/contact" .
```

Erwarteter Verstoss: `CON-CM-020` oder `CON-CM-031`.

### I-07: E-Mail mit URI-Payload

```turtle
ex:method-5
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactURI <mailto:max@example.org> .
```

Erwarteter Verstoss: `CON-CM-020` oder `CON-CM-030`.

### I-08: Postalische Methode mit direkter Adresse

```turtle
ex:method-6
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesAddress ex:address-1 .
```

Erwarteter Verstoss: `CON-CM-020` oder `CON-CM-032`. Die Property `usesAddress` ist nicht Teil des MVP.

### I-09: Postalische Methode mit Freitextadresse

```turtle
ex:method-7
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:contactValue "Musterstrasse 1, 12345 Berlin" .
```

Erwarteter Verstoss: `CON-CM-020` oder `CON-CM-032`.

### I-10: Mehrere Usage-Werte

```turtle
ex:contact-2
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private,
                              contact-usage:business ;
    conx-contact:hasContactMethod ex:method-8 .
```

Erwarteter Verstoss: `CON-CP-020`.

### I-11: Unbekannter Purpose-Wert

```turtle
ex:contact-3
    a conx-contact:ContactPoint ;
    conx-contact:contactPurpose ex:dispatch ;
    conx-contact:hasContactMethod ex:method-9 .
```

Erwarteter Verstoss: `CON-CP-021`.

### I-12: Leerer funktionaler Kontaktname

```turtle
ex:contact-4
    a conx-contact:ContactPoint ;
    conx-contact:contactName "   " ;
    conx-contact:hasContactMethod ex:method-10 .
```

Erwarteter Verstoss: `CON-CP-030`.

### I-13: Plattform mehrfach angegeben

```turtle
ex:method-11
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin,
                                 contact-platform:instagram ;
    conx-contact:contactURI <https://example.org/profile> .
```

Erwarteter Verstoss: `CON-CM-033`.

## 16. Bewusst nicht validiert

Das Kontakt-Core-Shape prüft nicht:

- ob eine Telefonnummer wirklich erreichbar ist,
- ob eine E-Mail-Adresse existiert,
- ob eine Social-Profile-URL wirklich zur angegebenen Plattform gehört,
- ob private Kontaktdaten veröffentlicht werden dürfen,
- ob ein Kontaktpunkt aktuell besetzt ist,
- ob ein Kontaktpunkt eine Person, Abteilung oder Rolle repräsentiert,
- ob `contactName` ein Personenname oder eine Funktionsbezeichnung ist,
- ob eine Organisation einen Lieferkontakt besitzen muss,
- ob `availableLanguage` tatsächlich von der Kontaktstelle bedient wird.

Diese Punkte gehören in strengere Prozessprofile, Governance-Regeln oder operative Systeme.

## 17. Testartefakte

Die Implementierung umfasst folgende Testgraphen:

```text
modules/core/contact/tests/valid/minimal-email-contact.ttl
modules/core/contact/tests/valid/business-delivery-contact.ttl
modules/core/contact/tests/valid/website-and-social-contact.ttl
modules/core/contact/tests/valid/messenger-contact.ttl
modules/core/contact/tests/invalid/contact-point-missing-method.ttl
modules/core/contact/tests/invalid/contact-method-invalid-channel.ttl
modules/core/contact/tests/invalid/contact-method-invalid-payload.ttl
modules/core/contact/tests/invalid/postal-contact-invalid-address-reference.ttl
modules/core/contact/tests/invalid/invalid-usage-and-purpose.ttl
modules/core/contact/tests/invalid/invalid-text-values.ttl
```

Automatisierte Tests prüfen:

1. alle gültigen Dateien sind konform,
2. jede ungültige Datei erzeugt mindestens den erwarteten Anforderungsbezeichner,
3. deutsche und englische Meldungen sind vorhanden,
4. kanalbezogene Payload-Regeln greifen ohne OWL-Inferenz,
5. Kontaktvokabulare und Address-Core-Daten werden in der Validierungsumgebung mitgeladen,
6. zusätzliche Properties anderer Module bleiben erlaubt.

## 18. Umgesetzte Artefakte

1. Referenzvokabulare `contact-channel`, `contact-usage`, `contact-purpose` und `contact-platform`.
2. `core/contact` T-Box.
3. Core Shapes aus diesem Dokument.
4. Gültige und ungültige Testgraphen.
5. Automatisierte Tests für Ontologie, Referenzvokabulare und Shapes.
6. HTML-Dokumentation und Modulmetadaten.

## 19. Abnahmekriterien für die Core-Shape-Implementierung

Die Umsetzung ist fachlich vollständig, wenn:

1. jede Anforderung `CON-*` in einem nachvollziehbaren Constraint umgesetzt ist,
2. `ContactPoint` mindestens eine `ContactMethod` verlangt,
3. jede `ContactMethod` genau einen freigegebenen Kanal besitzt,
4. die Payload-Regeln je Kanal greifen,
5. postalische Kontaktmethoden ausschließlich `usesAddressAssignment` verwenden,
6. Usage, Purpose, Channel und Platform gegen freigegebene Vokabulare validiert werden,
7. die inverse Beziehung optional bleibt,
8. keine Adress-, Personen- oder Organisationssemantik im Kontakt-Shape dupliziert wird.

## 20. Verständliches Beispiel

> Ein geschäftlicher Rechnungskontakt besitzt eine E-Mail-Methode. Das Shape
> prüft, dass Methode, Kanal und E-Mail-Wert zusammenpassen. Es prüft nicht, ob
> das Postfach tatsächlich erreichbar ist.
