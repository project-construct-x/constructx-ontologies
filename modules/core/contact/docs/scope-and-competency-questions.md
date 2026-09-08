# Scope und Kompetenzfragen des Kontaktmoduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

## 1. Zweck

Das Kontaktmodul beschreibt Kontaktierbarkeit. Es soll ausdrücken, über welche Kanäle eine Ressource erreichbar ist, in welchem Nutzungskontext diese Angaben gelten und welchem Zweck sie dienen.

Das Modul besitzt nicht die Identität der Person, die Struktur einer Organisation oder die postalische Adresse selbst. Diese Begriffe bleiben in `core/person`, `core/organization` beziehungsweise `core/address`.

## 2. Bestätigter Scope

| Bereich | Entscheidung für den MVP |
| --- | --- |
| Kontaktträger | Fachlich primär `conx-agent:Agent`, insbesondere Personen und Organisationen; keine harte `rdfs:domain` an `hasContactPoint` |
| Lesrichtung | Ausgehend vom Kontaktträger: `hasContactPoint` |
| Inverse | `isContactPointFor` optional als Komfortproperty, nicht verpflichtend |
| Kontaktpunkt | Bündelt mehrere konkrete Kontaktmethoden in einem Nutzungskontext |
| Kontaktmethode | Beschreibt genau einen Kanal und dessen Wert, URI oder Adressreferenz |
| Kanäle | E-Mail, Telefon, Mobiltelefon, Fax, Website, Messenger, Social Profile, postalische Adresse |
| Postalische Adresse | Keine eigene Adressstruktur; Referenz auf `conx-addr:AddressAssignment` aus dem bestehenden Address-Modul |
| Privat/beruflich/offiziell | Kontrolliertes A-Box-Vokabular `ContactUsage` |
| Zweck | Getrenntes A-Box-Vokabular `ContactPurpose`, zum Beispiel Lieferung, Rechnung, Support, Notfall |
| Social Profile | Generisch modellieren, Plattform über eigenes erweiterbares Vokabular |
| Zugriffsschutz | Nicht Teil der Kontaktontologie |
| Erreichbarkeitszeiten | Für den MVP nur als Freitextnotiz oder späteres Profil, kein eigenes Zeitmodell |

## 3. Nicht im Scope

- strukturierte Adressbestandteile wie Strasse, Hausnummer, Ort oder Land,
- Personennamen und Personenidentität,
- Organisationsmitgliedschaften, Stellen und Rollen,
- Berechtigungen, Einwilligungen und Datenschutzprozesse,
- vollständige Öffnungszeiten- oder Kalenderlogik,
- technische Zustellprotokolle und Messaging-Konten als eigene Kontoontologie,
- konkrete Plattform-APIs wie LinkedIn, Instagram oder X als harte Properties.

## 4. Modellgrundsatz

Ein `ContactPoint` ist kein einzelnes Feld wie eine Telefonnummer. Er ist ein fachlicher Kontaktblock. Dadurch kann eine Person beispielsweise einen privaten Kontaktpunkt mit E-Mail, Mobiltelefon und Postadresse besitzen:

```turtle
ex:person-123
    conx-contact:hasContactPoint ex:person-123-private-contact .

ex:person-123-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-123-private-email,
                                  ex:person-123-private-mobile .
```

Das vermeidet Properties wie `privateEmail`, `businessPhone` oder `deliveryMobile`, die bei neuen Kanälen und Zwecken schnell explodieren.

## 5. Kompetenzfragen

### CQ-01: Welche Kontaktpunkte besitzt eine Person oder Organisation?

Ein Kontaktträger verweist mit `hasContactPoint` auf null bis beliebig viele Kontaktpunkte. Die bevorzugte Lesrichtung bleibt dadurch ausgehend vom Agenten.

Beispiel:

```turtle
ex:person-123 conx-contact:hasContactPoint ex:person-123-private-contact .
```

### CQ-02: Wie wird zwischen privater, beruflicher und offizieller Erreichbarkeit unterschieden?

Der Nutzungskontext wird am `ContactPoint` über `contactUsage` beschrieben. Der implementierte Startwertumfang lautet:

| Wert | Bedeutung |
| --- | --- |
| `contact-usage:private` | Privat verwendbarer Kontaktpunkt |
| `contact-usage:business` | Beruflich oder geschäftlich verwendbarer Kontaktpunkt |
| `contact-usage:official` | Offiziell, registerbezogen oder institutionell verwendbarer Kontaktpunkt |

`private` ist keine Zugriffskontrolle. Es beschreibt den fachlichen Verwendungskontext, nicht wer den Wert lesen darf.

### CQ-03: Wie wird der Zweck eines Kontaktpunkts beschrieben?

Der Zweck wird getrennt vom Nutzungskontext über `contactPurpose` modelliert. Das ist für Lieferschein- und Beschaffungsprozesse wichtig, weil ein beruflicher Kontaktpunkt beispielsweise für Lieferung, Rechnung oder Support verwendet werden kann.

Implementierte Startwerte:

| Wert | Bedeutung |
| --- | --- |
| `contact-purpose:general` | Allgemeine Kontaktaufnahme |
| `contact-purpose:delivery` | Lieferung, Warenannahme oder Zustellung |
| `contact-purpose:billing` | Rechnung und Zahlungsklärung |
| `contact-purpose:support` | Support oder Kundenservice |
| `contact-purpose:sales` | Vertrieb oder Angebotskommunikation |
| `contact-purpose:technical` | Technische Rückfragen |
| `contact-purpose:emergency` | Notfall- oder Eskalationskontakt |

### CQ-04: Wie werden mehrere Kommunikationskanäle an einem Kontaktpunkt gebündelt?

Ein `ContactPoint` besitzt mehrere `ContactMethod`-Ressourcen. Jede `ContactMethod` hat genau einen Kanal. Dadurch bleibt ein Kontaktpunkt fachlich gebündelt, aber die Kanalwerte bleiben einzeln validierbar.

```turtle
ex:delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:business ;
    conx-contact:contactPurpose contact-purpose:delivery ;
    conx-contact:hasContactMethod ex:delivery-email,
                                  ex:delivery-phone .

ex:delivery-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "wareneingang@example.org" .
```

### CQ-05: Wie werden postalische Kontaktadressen modelliert?

Postalische Adressen werden über `core/address` beschrieben. Das Kontaktmodul sieht eine Kontaktmethode mit Kanal `postalAddress` vor und verbindet diese mit einer bestehenden `conx-addr:AddressAssignment`.

Umgesetztes Muster:

```turtle
ex:private-postal-method
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:postalAddress ;
    conx-contact:usesAddressAssignment ex:private-postal-address-assignment .
```

Der direkte Verweis auf `conx-addr:Address` entfällt für den MVP. Die Adressontologie legt bereits fest, dass fachliche Verwendung, Rolle und Zustellhinweise über `AddressAssignment` ausgedrückt werden. Genau diese Informationen sind für postalische Kontaktierbarkeit relevant.

### CQ-06: Wie werden Social-Media-Profile modelliert?

Social Profiles werden nicht als eigene Properties pro Plattform modelliert. Stattdessen wird der Kanal `socialProfile` verwendet. Eine Plattformressource kann die Plattform beschreiben.

```turtle
ex:max-linkedin
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:socialProfile ;
    conx-contact:contactPlatform contact-platform:linkedin ;
    conx-contact:contactURI <https://www.linkedin.com/in/example> .
```

Das ist stabiler als `hasLinkedInProfile`, `hasInstagramProfile` oder `hasTwitterProfile`.

### CQ-07: Wie wird ein funktionaler Kontakt wie "Wareneingang" oder "Bauleitung" abgebildet?

Funktionale Kontaktbezeichnungen gehören an den Kontaktpunkt, nicht an die Person. Ein Kontaktpunkt kann deshalb ein optionales `contactName` erhalten.

Beispiel:

```turtle
ex:delivery-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactName "Wareneingang Tor 4"@de ;
    conx-contact:contactPurpose contact-purpose:delivery .
```

Damit wird kein Personenname behauptet.

### CQ-08: Wie wird eine inverse Beziehung behandelt?

Eine inverse Property `isContactPointFor` ist in Version `0.1.0` nicht enthalten. Datenhalter führen die Beziehung mit `hasContactPoint` vom Kontaktträger zum Kontaktpunkt.

### CQ-09: Welche Validierungsfragen beantwortet das Core-SHACL-Profil?

Das Core-SHACL-Profil legt für den MVP fest:

- `ContactPoint` und `ContactMethod` dürfen IRI oder Blank Node sein, müssen aber explizit typisiert werden.
- Ein `ContactPoint` muss mindestens eine `ContactMethod` besitzen.
- `contactUsage` darf höchstens einmal vorkommen.
- Eine `ContactMethod` muss genau einen `contactChannel` besitzen.
- Die erlaubte Wertform hängt vom Kanal ab: String, IRI oder `AddressAssignment`.
- Usage, Purpose, Channel und Platform werden gegen die freigegebenen Construct-X-Referenzvokabulare geprüft.
- E-Mail-, Telefon-, Mobiltelefon- und Faxwerte werden nur als nicht-leere Strings geprüft.

## 6. Umgesetzte Modellentscheidungen

| Thema | Entscheidung | Grund |
| --- | --- | --- |
| Harte Domain von `hasContactPoint` | Keine harte `rdfs:domain`, aber fachliche Lesrichtung `Agent -> ContactPoint` dokumentieren | Verhindert unbeabsichtigte Inferenz, falls später Projekte, Baustellen oder Services Kontaktträger werden |
| `contactName` vs. `functionalLabel` | `contactName` | UBL verwendet `Contact.Name` ausdrücklich auch für funktionale Namen |
| E-Mail und Telefon als Literal oder URI | Nicht-leerer String im Core-Profil | UBL und schema.org verwenden Text; strenge Syntaxregeln sind fachprofilabhängig |
| Plattformvokabular | Eigenes erweiterbares `contact-platform`-Vokabular im MVP | Plattformen wechseln häufig, harte T-Box-Properties werden vermieden |

## 7. Abnahmekriterien für 0.1.0

Der MVP ist fachlich abgedeckt, wenn:

1. die Klassen `ContactPoint` und `ContactMethod` implementiert sind,
2. die vier Referenzvokabulare `contact-channel`, `contact-usage`, `contact-purpose` und `contact-platform` vorliegen,
3. postalische Kontaktmethoden über `usesAddressAssignment` auf `core/address` verweisen,
4. die Mindestregeln für ContactPoint und ContactMethod als Core Shapes umgesetzt und getestet sind.

## 8. Verständliches Beispiel

> Die Supportstelle einer Organisation ist geschäftlich für technische Fragen
> erreichbar. Sie kann gleichzeitig eine Telefonnummer und eine E-Mail-Adresse
> besitzen, ohne zwei getrennte Kontaktstellen anzulegen.
