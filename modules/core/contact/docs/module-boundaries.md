# Modulgrenzen des Kontaktmoduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

## 1. Ziel

Dieses Dokument ordnet die Kontaktbegriffe den zuständigen Construct-X-Modulen zu. Das Kontaktmodul soll Kontaktierbarkeit beschreiben, ohne Person, Organisation, Adresse, Projekt oder Datenschutzlogik zu übernehmen.

## 2. Leitprinzipien

1. Das Kontaktmodul besitzt Kontaktpunkte und Kontaktmethoden.
2. Der Kontaktträger verweist ausgehend auf seine Kontaktpunkte.
3. Kontaktkontext und Kontaktzweck sind kontrollierte A-Box-Werte.
4. Postalische Adressen werden referenziert und nicht kopiert.
5. Plattformen wie LinkedIn oder Instagram werden als Datenwerte oder Vokabularressourcen modelliert, nicht als T-Box-Properties.
6. Zugriffsschutz, Einwilligung und Datenschutzfolgen liegen ausserhalb des Kontaktmoduls.

## 3. Zuständigkeit nach Modul

| Modul | Besitzt | Besitzt ausdrücklich nicht |
| --- | --- | --- |
| `core/contact` | `ContactPoint`, `ContactMethod`, `hasContactPoint`, `hasContactMethod`, Kontaktkanal, Nutzungskontext, Zweck, Plattformreferenz | Personennamen, Organisationsstruktur, Adressbestandteile, Datenschutzberechtigungen |
| `core/agent` | Gemeinsame Oberklasse für Personen und Organisationen | Konkrete Kontaktwerte |
| `core/person` | Intrinsische Personendaten | E-Mail, Telefon, private oder berufliche Kontaktlogik |
| `core/organization` | Organisationen, Stellen, Mitgliedschaften und Rollen | Allgemeine Kontaktkanalstruktur |
| `core/address` | Strukturierte Adresse, Adresszuordnung und Adressrollen | E-Mail, Telefon, Messenger, Social Profile |
| `domain/delivery-note` | Lieferscheinrollen, Lieferprozesse und dokumentenspezifische Anforderungen | Allgemeines Kontaktmodell |

## 4. Dokumentierte Abhängigkeiten

### 4.1 Harte semantische Abhängigkeiten

| Abhängigkeit | Bewertung |
| --- | --- |
| `core/contact -> core/agent` | Fachlich plausibel, weil Personen und Organisationen Kontaktträger sind; kein harter Import und keine harte Domain |
| `core/contact -> core/address` | Referenz für `usesAddressAssignment` mit Range `conx-addr:AddressAssignment` |
| `core/person -> core/contact` | Nicht erforderlich; Personendaten verwenden Kontaktbegriffe nur in Instanzdaten oder Profilen |
| `core/organization -> core/contact` | Nicht erforderlich für die Organisations-T-Box, aber gemeinsam in Datenprofilen nutzbar |

Die T-Box sollte Imports nur verwenden, wenn die fremden Axiome wirklich benötigt werden. Eine reine Range-Referenz kann gegebenenfalls als referenziert, aber nicht importiert dokumentiert werden.

### 4.2 Domain-Entscheidung

Die fachliche Lesrichtung ist:

```text
Agent -> hasContactPoint -> ContactPoint
```

Eine harte `rdfs:domain conx-agent:Agent` hat aber eine Nebenwirkung: Jede Ressource, die `hasContactPoint` verwendet, wird automatisch als `Agent` inferiert. Das ist dann korrekt, wenn wirklich nur Personen und Organisationen Kontaktträger sein dürfen.

Falls später auch Projekte, Baustellen, Services oder Geraete eigene Kontaktpunkte bekommen sollen, ist eine offene Domain stabiler. In dem Fall kann ein SHACL-Profil für Agenten trotzdem verlangen, dass Personen und Organisationen `hasContactPoint` korrekt verwenden.

Umgesetzte Entscheidung: fachliche Lesrichtung dokumentieren, aber in der offenen T-Box keine harte RDFS-Domain setzen.

## 5. Abgrenzung zu Adresse

Eine postalische Adresse bleibt eine `conx-addr:Address` beziehungsweise `conx-addr:AddressAssignment`.

Das Kontaktmodul darf nur ausdrücken, dass eine Adresse als Kontaktweg verwendet wird. Es definiert keine eigenen Felder für:

- Strasse,
- Hausnummer,
- Postleitzahl,
- Ort,
- Land,
- Verwaltungseinheit,
- c/o oder z. Hd.

Für Lieferscheinfälle ist die Verbindung zu `AddressAssignment` gesetzt, weil vorhandene Rollen wie `DeliveryAddressRole` oder `InvoiceAddressRole` wiederverwendet werden können.

## 6. Abgrenzung zu Organisation

UBL `Contact.Department` und `Contact.JobTitle` sind für Austauschdaten relevant. Sie dürfen aber nicht als vollständige Organisationsstruktur interpretiert werden.

Für den Kontakt-MVP ist ein optionaler Text an `ContactPoint` vertretbar:

```text
contactName       "Wareneingang Tor 4"
departmentName    "Logistik"
functionTitle     "Schichtleitung"
```

Das behauptet keine Mitgliedschaft, keine Stelle und keine Organisationshierarchie. Sobald echte Rollen, Stellen oder Mitgliedschaften benötigt werden, gehört die Semantik in `core/organization`.

## 7. Abgrenzung zu Person

Private Kontaktdaten einer Person werden nicht als Properties von `Person` modelliert. Stattdessen:

```text
Person -> hasContactPoint -> ContactPoint
ContactPoint -> contactUsage private
ContactPoint -> hasContactMethod -> ContactMethod
```

Dadurch bleibt `core/person` auf intrinsische Personendaten begrenzt. Kontaktwerte können separat validiert, ausgeblendet, ersetzt oder gelöscht werden.

## 8. Abgrenzung zu Lieferschein und weiteren Domain-Modulen

Das Kontaktmodul liefert generische Begriffe wie `contactPurpose:delivery`. Ein Lieferscheinprofil kann diese enger verwenden, etwa:

```text
Lieferpartei muss optional oder verpflichtend einen delivery-Kontakt besitzen.
```

Die Pflicht selbst gehört nicht in die Contact-T-Box, sondern in ein Domain-Shape des Lieferscheinmoduls.

## 9. T-Box- und A-Box-Trennung

### T-Box

- `ContactPoint`
- `ContactMethod`
- `hasContactPoint`
- `isContactPointFor`
- `hasContactMethod`
- `contactChannel`
- `contactUsage`
- `contactPurpose`
- `contactPlatform`
- `contactValue`
- `contactURI`
- `usesAddressAssignment`
- optionale beschreibende Textproperties wie `contactName`, `departmentName`, `functionTitle`, `availabilityNote`

### A-Box beziehungsweise Referenzvokabulare

- `contact-channel`: E-Mail, Telefon, Mobiltelefon, Fax, Website, Messenger, Social Profile, postalische Adresse
- `contact-usage`: privat, beruflich, offiziell
- `contact-purpose`: allgemein, Lieferung, Rechnung, Support, Vertrieb, Technik, Notfall
- `contact-platform`: LinkedIn, Instagram, X, Facebook, GitHub, WhatsApp, Signal, Teams usw.

Konkrete Personen, Telefonnummern, Mailadressen und URLs sind Instanzdaten der Datenhalter.

## 10. Import- und Alignment-Strategie

| Quelle | Einordnung |
| --- | --- |
| `core/agent` | Referenz oder Import je nach Domain-/Range-Entscheidung |
| `core/address` | Referenz für `usesAddressAssignment`; Import nur, wenn die T-Box die fremden Axiome wirklich laden muss |
| UBL | Analyse- und Mappingquelle |
| Schema.org | Alignment-Kandidat für `ContactPoint`, keine direkte Kopie |
| vCard RDF | Alignment-Kandidat für E-Mail, Telefon, URL, Adresse und Usage-Typen |
| SKOS | Wahrscheinlich direkte Wiederverwendung für kontrollierte Vokabulare |

Neue Einträge in `network/imports.lock.yaml` sind erst erforderlich, wenn tatsächliche `owl:imports` eingeführt werden.

## 11. Verständliches Beispiel

> Eine Organisation besitzt einen Rechnungskontakt mit einer E-Mail-Adresse.
> Organization beschreibt die Organisation; Contact beschreibt Kontaktpunkt,
> Zweck und E-Mail-Methode. Kein Modul kopiert die Begriffe des anderen.
