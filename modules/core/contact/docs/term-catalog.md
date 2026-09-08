# Begriffskatalog für das Kontaktmodul

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

## 1. Zweck

Dieser Katalog beschreibt die lokalen Begriffe der Contact-T-Box 0.1.0 und die zugehörigen Referenzvokabulare. Die SHACL-Kardinalitäten beziehen sich auf das Core-Profil, nicht auf harte OWL-Beschränkungen.

## 2. Namensräume

### Kontaktontologie

```text
Ontologie-IRI: https://www.construct-x.org/ontology/contact
Versions-IRI:  https://www.construct-x.org/ontology/contact/0.1.0
Namespace:     https://www.construct-x.org/ontology/contact#
Prefix:        conx-contact
```

### Kontaktkanal-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/contact-channel
Versions-IRI:  https://www.construct-x.org/vocab/contact-channel/0.1.0
Namespace:     https://www.construct-x.org/vocab/contact-channel#
Prefix:        contact-channel
```

### Kontaktverwendungs-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/contact-usage
Versions-IRI:  https://www.construct-x.org/vocab/contact-usage/0.1.0
Namespace:     https://www.construct-x.org/vocab/contact-usage#
Prefix:        contact-usage
```

### Kontaktzweck-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/contact-purpose
Versions-IRI:  https://www.construct-x.org/vocab/contact-purpose/0.1.0
Namespace:     https://www.construct-x.org/vocab/contact-purpose#
Prefix:        contact-purpose
```

### Kontaktplattform-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/contact-platform
Versions-IRI:  https://www.construct-x.org/vocab/contact-platform/0.1.0
Namespace:     https://www.construct-x.org/vocab/contact-platform#
Prefix:        contact-platform
```

## 3. Klassen

### 3.1 `conx-contact:ContactPoint`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontaktblock, über den eine Ressource in einem bestimmten Nutzungskontext und für bestimmte Zwecke erreichbar ist |
| Modul | `core/contact` |
| Verwendung | Bündelt eine oder mehrere konkrete Kontaktmethoden |
| Quelle | UBL `Contact`, Schema.org `ContactPoint`, vCard n-äre Kontaktressourcen |
| Datenschutz | Kann personenbezogene Kontaktwerte enthalten oder auf solche verweisen |

Beispiel:

```turtle
ex:private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:private-email,
                                  ex:private-mobile .
```

### 3.2 `conx-contact:ContactMethod`

| Punkt | Festlegung |
| --- | --- |
| Definition | Einzelner Kommunikationsweg innerhalb eines Kontaktpunkts |
| Modul | `core/contact` |
| Verwendung | Trägt genau einen Kanal und den zugehörigen Wert, URI oder eine Adressreferenz |
| Quelle | UBL `Communication`, vCard E-Mail/Telefon/IMPP/URL |
| Datenschutz | Der konkrete Wert kann personenbezogen oder geschäftskritisch sein |

Beispiel:

```turtle
ex:private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .
```

### 3.3 `conx-contact:ContactChannel`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontrollierter Typ eines Kommunikationskanals |
| Modul | T-Box-Klasse in `core/contact`, Werte im SKOS-Vokabular |
| Beispiele | E-Mail, Telefon, Mobiltelefon, Fax, Website, Messenger, Social Profile, postalische Adresse |
| Quelle | UBL `ChannelCode`, vCard Kommunikationsproperties, schema.org Kontaktfelder |

### 3.4 `conx-contact:ContactUsage`

| Punkt | Festlegung |
| --- | --- |
| Definition | Nutzungskontext eines Kontaktpunkts |
| Modul | T-Box-Klasse in `core/contact`, Werte im SKOS-Vokabular |
| Beispiele | privat, beruflich, offiziell |
| Quelle | vCard Home/Work, fachliche Construct-X-Abgrenzung |

### 3.5 `conx-contact:ContactPurpose`

| Punkt | Festlegung |
| --- | --- |
| Definition | Fachlicher Zweck, für den ein Kontaktpunkt verwendet werden soll |
| Modul | T-Box-Klasse in `core/contact`, Werte im SKOS-Vokabular |
| Beispiele | allgemein, Lieferung, Rechnung, Support, Vertrieb, Technik, Notfall |
| Quelle | schema.org `contactType`, UBL Contact Note und Geschäftsprozessbedarf |

### 3.6 `conx-contact:ContactPlatform`

| Punkt | Festlegung |
| --- | --- |
| Definition | Plattform oder Dienst, auf dem ein Social-, Messenger- oder Webprofil erreichbar ist |
| Modul | T-Box-Klasse in `core/contact`, Werte im SKOS-Vokabular |
| Beispiele | LinkedIn, Instagram, X, Facebook, GitHub, WhatsApp, Signal, Microsoft Teams |
| Quelle | UBL `SocialMediaProfile`, Web- und Messaging-Praxis |

## 4. Objekteigenschaften

### 4.1 `conx-contact:hasContactPoint`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft einen Kontaktträger mit einem Kontaktpunkt |
| Domain | Keine harte `rdfs:domain`; fachliche Lesrichtung vom Kontaktträger zum Kontaktpunkt |
| Range | `conx-contact:ContactPoint` |
| Kardinalität | `0..n` |
| Inverse | `conx-contact:isContactPointFor` |
| Quelle | schema.org `contactPoint`, SEMIC Contact Point |

### 4.2 `conx-contact:isContactPointFor`

| Punkt | Festlegung |
| --- | --- |
| Definition | Inverse Navigationsbeziehung vom Kontaktpunkt zum Kontaktträger |
| Domain | `conx-contact:ContactPoint` |
| Range | Keine harte `rdfs:range`; fachlich Kontaktträger |
| Kardinalität | `0..n` |
| Verbindlichkeit | Nicht verpflichtend |

### 4.3 `conx-contact:hasContactMethod`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft einen Kontaktpunkt mit einer konkreten Kontaktmethode |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactMethod` |
| Kardinalität | Core Shape `1..n` |

### 4.4 `conx-contact:contactChannel`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt den Kanal einer Kontaktmethode |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-contact:ContactChannel` |
| Kardinalität | Core Shape genau `1` |

### 4.5 `conx-contact:contactUsage`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt den Nutzungskontext eines Kontaktpunkts |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactUsage` |
| Kardinalität | Core Shape `0..1` |

### 4.6 `conx-contact:contactPurpose`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt einen fachlichen Zweck eines Kontaktpunkts |
| Domain | `conx-contact:ContactPoint` |
| Range | `conx-contact:ContactPurpose` |
| Kardinalität | `0..n` |

### 4.7 `conx-contact:contactPlatform`

| Punkt | Festlegung |
| --- | --- |
| Definition | Bestimmt die Plattform einer Social-, Messenger- oder Webkontaktmethode |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-contact:ContactPlatform` |
| Kardinalität | `0..1` |

### 4.8 `conx-contact:usesAddressAssignment`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine postalische Kontaktmethode mit einer bestehenden Adresszuordnung |
| Domain | `conx-contact:ContactMethod` |
| Range | `conx-addr:AddressAssignment` |
| Kardinalität | Für Kanal `postalAddress` im Core Shape genau `1` |

## 5. Werteigenschaften

### 5.1 `conx-contact:contactValue`

| Punkt | Festlegung |
| --- | --- |
| Definition | Literalwert einer Kontaktmethode |
| Domain | `conx-contact:ContactMethod` |
| Range | `xsd:string`; im Core-Profil für E-Mail, Telefon, Mobiltelefon und Fax nur nicht-leer geprüft |
| Beispiele | E-Mail-Adresse, Telefonnummer, Messenger-Handle |

### 5.2 `conx-contact:contactURI`

| Punkt | Festlegung |
| --- | --- |
| Definition | IRI oder URL einer Kontaktmethode |
| Domain | `conx-contact:ContactMethod` |
| Range | IRI |
| Beispiele | Website, Social Profile, mailto-URI, tel-URI |

### 5.3 `conx-contact:contactName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Anzeige- oder Funktionsname eines Kontaktpunkts |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` oder `rdf:langString` |
| Beispiele | "Wareneingang", "Bauleitung", "Rechnungsstelle" |

### 5.4 `conx-contact:departmentName`

| Punkt | Festlegung |
| --- | --- |
| Definition | Textuelle Abteilungsangabe für einen Kontaktpunkt |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` oder `rdf:langString` |
| Hinweis | Keine Organisationshierarchie |

### 5.5 `conx-contact:functionTitle`

| Punkt | Festlegung |
| --- | --- |
| Definition | Textuelle Funktion oder Rolle des Kontaktpunkts im Kommunikationskontext |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` oder `rdf:langString` |
| Hinweis | Kein Organisationsrollenmodell |

### 5.6 `conx-contact:availableLanguage`

| Punkt | Festlegung |
| --- | --- |
| Definition | Sprache, in der der Kontaktpunkt verwendet werden kann |
| Domain | `conx-contact:ContactPoint` |
| Range | BCP-47-Sprachcode als String oder spätere Sprachressource |
| Quelle | schema.org `availableLanguage`, vCard `language` |

### 5.7 `conx-contact:availabilityNote`

| Punkt | Festlegung |
| --- | --- |
| Definition | Freitext zur Erreichbarkeit |
| Domain | `conx-contact:ContactPoint` |
| Range | `xsd:string` oder `rdf:langString` |
| Beispiele | "Mo-Fr 8-16 Uhr", "nur für Notfälle", "nach vorheriger Anmeldung" |

## 6. Umgesetzte Startwerte

### 6.1 `contact-channel`

| Begriff | Deutsch | Englisch | Hinweis |
| --- | --- | --- | --- |
| `email` | E-Mail | Email | nicht-leerer String |
| `phone` | Telefon | Phone | allgemeine Telefonnummer als nicht-leerer String |
| `mobilePhone` | Mobiltelefon | Mobile phone | spezifischer Mobilfunkkanal als nicht-leerer String |
| `fax` | Fax | Fax | UBL `Telefax`, schema.org `faxNumber` |
| `website` | Website | Website | URL/IRI |
| `messenger` | Messenger | Messenger | Handle oder URI, Plattform möglich |
| `socialProfile` | Social-Media-Profil | Social media profile | URI und Plattform möglich |
| `postalAddress` | Postanschrift | Postal address | Verweis auf Address-Modul |

### 6.2 `contact-usage`

| Begriff | Deutsch | Englisch |
| --- | --- | --- |
| `private` | Privat | Private |
| `business` | Beruflich/geschäftlich | Business |
| `official` | Offiziell | Official |

### 6.3 `contact-purpose`

| Begriff | Deutsch | Englisch |
| --- | --- | --- |
| `general` | Allgemein | General |
| `delivery` | Lieferung | Delivery |
| `billing` | Rechnung | Billing |
| `support` | Support | Support |
| `sales` | Vertrieb | Sales |
| `technical` | Technisch | Technical |
| `emergency` | Notfall | Emergency |

### 6.4 `contact-platform`

| Begriff | Verwendung |
| --- | --- |
| `linkedin` | berufliches Social Profile |
| `instagram` | Social Profile |
| `x` | Social Profile, früher Twitter |
| `facebook` | Social Profile |
| `github` | Entwicklungsprofil |
| `whatsapp` | Messenger |
| `signal` | Messenger |
| `microsoftTeams` | Messenger beziehungsweise Kollaboration |

Das Plattformvokabular sollte nicht als abschliessend verstanden werden.

## 7. Kompaktes Zielbeispiel

```turtle
@prefix conx-contact: <https://www.construct-x.org/ontology/contact#> .
@prefix contact-channel: <https://www.construct-x.org/vocab/contact-channel#> .
@prefix contact-purpose: <https://www.construct-x.org/vocab/contact-purpose#> .
@prefix contact-usage: <https://www.construct-x.org/vocab/contact-usage#> .
@prefix ex: <https://example.org/id/> .

ex:person-123
    conx-contact:hasContactPoint ex:person-123-private-contact .

ex:person-123-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:person-123-private-email,
                                  ex:person-123-private-mobile .

ex:person-123-private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "max@example.org" .

ex:person-123-private-mobile
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:mobilePhone ;
    conx-contact:contactValue "+49 171 1234567" .
```

## 8. Bewusst späteren Profilen vorbehalten

| Thema | Grund |
| --- | --- |
| `availableLanguage` als Literal oder Sprachressource | BCP-47-Code ist pragmatisch, Sprachressource wäre semantisch stärker |
| URI- oder Literalvarianten für E-Mail und Telefon | Der Core-MVP prüft diese Kanäle als nicht-leere Strings; mailto-/tel-Profile können später folgen |
| Strenge Regex-Regeln | E-Mail- und Telefonvalidierung kann schnell länderspezifisch und fehleranfällig werden |

Das fachliche Zusammenspiel ist im [Kontakt-Konzeptdiagramm](diagrams/contact-concept-model.md) dargestellt.
