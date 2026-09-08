# Quellenanalyse für das Kontaktmodul

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 27. August 2026  
**Geltungsbereich:** `core/contact`

## 1. Ziel und Methode

Diese Analyse bewertet bestehende Kontaktmodelle als Grundlage für ein Construct-X-Kontaktmodul. Untersucht wurden:

- Struktur von Kontaktpunkten und Kommunikationskanälen,
- Umgang mit E-Mail, Telefon, Fax, Website, Messenger und Social Profiles,
- Trennung von Kontaktwert, Verwendungskontext und Zweck,
- Abgrenzung zu postalischen Adressen,
- Eignung für Personen, Organisationen und Geschäftsdokumente wie Lieferscheine,
- Risiken durch zu breite Textfelder, zu harte Plattformproperties oder doppelte Adressmodellierung.

## 2. Kurzfazit

[OASIS UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) ist die wichtigste Quelle für Geschäftsprozesse. UBL kennt `Contact` als bündelnde Struktur und `Communication` als generischen Kanal mit Code, Text und Wert. Das passt gut zu `ContactPoint` plus `ContactMethod`.

[Schema.org ContactPoint](https://schema.org/ContactPoint) bestätigt den Begriff `ContactPoint`, ist aber für Construct-X zu offen: `contactType` ist Text, viele Wertebereiche erlauben Text oder sehr breite Ressourcen. Als Quelle für Begriffe wie `areaServed`, `availableLanguage`, `contactOption`, `email`, `faxNumber` und `telephone` ist Schema.org dennoch nützlich.

[W3C vCard RDF](https://www.w3.org/TR/vcard-rdf/) ist die stärkste Quelle für klassische Kontaktdaten. Es unterstützt E-Mail, Telefon, Instant Messaging, URL, Adresse sowie Typen wie Home und Work. Das n-äre Muster aus vCard stützt unsere Entscheidung, Kontext und Wert nicht in Properties wie `privateEmail` oder `businessPhone` einzubauen.

## 3. Bewertete Quellen

| Quelle | Verwendeter Stand | Rolle in der Analyse | Nutzung |
| --- | --- | --- | --- |
| [OASIS UBL](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) | 2.5 CS01, April 2026 | Geschäftsprozess- und Dokumentenaustausch | Primäre Feldanalyse für Contact, Communication, Party, SocialMediaProfile |
| [Schema.org ContactPoint](https://schema.org/ContactPoint) | Schema.org V30.0, abgerufen 2026-08-25 | Web-Interoperabilität und gängige Begriffe | Analyse- und Alignment-Quelle, keine direkte Kopie |
| [W3C vCard RDF](https://www.w3.org/TR/vcard-rdf/) | W3C Interest Group Note, 2014 | Klassische Kontaktstruktur für Personen und Organisationen | Analyse- und Alignment-Quelle |
| [SEMIC Core Person Vocabulary](https://semiceu.github.io/Core-Person-Vocabulary/) | 2.1.2 | bestätigt Contact Point als Randbegriff der Person | Abgrenzungsquelle |
| [Construct-X Address Ontology](../../address/docs/concept-model.md) | 0.1.0 plus Referenzvokabulare | bestehendes Adressmodell | Postalische Adressen werden referenziert, nicht kopiert |
| [Construct-X Agent Ontology](../../agent/docs/agent-specification.md) | 0.1.0 | gemeinsame Oberklasse für Personen und Organisationen | Kontaktträger im fachlichen Kern |

## 4. UBL 2.5

### 4.1 `Contact`

UBL `Contact` beschreibt eine kontaktierbare Person oder Abteilung in einer Organisation. Die Struktur enthält unter anderem:

- `ID`,
- `Name`,
- `JobTitle`,
- `Department`,
- `Telephone`,
- `Telefax`,
- `ElectronicMail`,
- `Note`,
- `OtherCommunication`.

Wichtig ist die Bedeutung von `Name`: UBL empfiehlt, das Feld für funktionale Bezeichnungen zu nutzen und nicht zwingend für Personennamen. Das ist für Construct-X relevant, weil Kontakte wie "Wareneingang", "Bauleitung" oder "Rechnungsstelle" modelliert werden müssen, ohne daraus eine natürliche Person zu machen.

### 4.2 `Communication`

UBL `Communication` ist eine generische Kommunikationsmethode. Sie besitzt:

- `ChannelCode` für den Kommunikationsweg als Code,
- `Channel` für den Kommunikationsweg als Text,
- `Value` für den eigentlichen identifizierenden Wert.

Damit liefert UBL ein klares Vorbild für `ContactMethod`: genau ein Kanal plus genau ein Wert oder eine referenzierte Ressource.

### 4.3 `Party`, Website und Social Media

UBL `Party` enthält neben `Contact` auch `WebsiteURI`, `AdditionalWebSite`, `PostalAddress` und `SocialMediaProfile`. `SocialMediaProfile` besitzt ID, Name, TypeCode und URI. Daraus folgen drei Punkte:

1. Websites und Social Profiles sind eigene Kontaktkanäle.
2. Social Profiles sollten generisch modelliert werden, nicht als Plattformproperty je Anbieter.
3. Postalische Adressen sind in UBL eigenständige Strukturen und dürfen im Construct-X-Kontaktmodul nicht als Adressfelder dupliziert werden.

### 4.4 Bewertung

| UBL-Konzept | Construct-X-Zuordnung |
| --- | --- |
| `Contact` | `ContactPoint` als Kontaktblock |
| `Communication` | `ContactMethod` als Kanal plus Wert |
| `Telephone` | `ContactMethod` mit Kanal `phone` |
| `ElectronicMail` | `ContactMethod` mit Kanal `email` |
| `Telefax` | `ContactMethod` mit Kanal `fax` |
| `OtherCommunication` | Erweiterbare `ContactMethod` |
| `Note` | `availabilityNote` oder allgemeine Kontaktanmerkung |
| `Name` | `contactName` für funktionale Kontaktbezeichnung |
| `Department` | optionales Textfeld am Kontaktpunkt, keine Organisationsstruktur |
| `JobTitle` | höchstens Funktionsbeschreibung, kein Mitgliedschaftsmodell |
| `PostalAddress` | Referenz auf `core/address` |
| `SocialMediaProfile` | `ContactMethod` mit Kanal `socialProfile`, Plattform und URI |

## 5. Schema.org ContactPoint

Schema.org definiert `ContactPoint` als Kontaktstelle, beispielsweise eine Beschwerde- oder Serviceabteilung. Die wichtigsten Felder für Construct-X sind:

- `contactType` für den Zweck eines Kontaktpunkts,
- `telephone`, `email` und `faxNumber`,
- `areaServed`,
- `availableLanguage`,
- `hoursAvailable`,
- `contactOption`.

Die Richtung `Person` oder `Organization` zu `ContactPoint` ist in schema.org etabliert. Das bestätigt unsere bevorzugte Lesrichtung vom Kontaktträger zum Kontaktpunkt.

Kritisch ist die Offenheit: `contactType` ist Text und kann Zweck, Rolle, Abteilung oder Nutzungskontext vermischen. Construct-X sollte daher nicht ein einziges `contactType` kopieren, sondern trennen:

| schema.org-nahe Information | Construct-X-Modellierung |
| --- | --- |
| Kontaktzweck | `contactPurpose` |
| Privat, beruflich, offiziell | `contactUsage` |
| Kanal | `contactChannel` |
| Barrierefrei, toll-free usw. | späteres `contactOption`-Vokabular |
| Sprache | optional `availableLanguage` |
| Öffnungszeiten | späteres Zeit-/Verfügbarkeitsprofil |

## 6. W3C vCard RDF

vCard RDF bildet die IETF-vCard-Welt in RDF/OWL ab. Relevant sind insbesondere:

- `hasEmail`,
- `hasTelephone`,
- `hasInstantMessage`,
- `hasURL`,
- `hasAddress`,
- Typen wie Home, Work, Voice, Cell und Text.

vCard kennt direkte einfache Properties und n-äre Muster für detailliertere Kontaktressourcen. Für Construct-X ist das n-äre Muster fachlich besser, weil eine Telefonnummer mehrere Aussagen benötigen kann: Kanal, Verwendung, Zweck, bevorzugte Nutzung und gegebenenfalls weitere Parameter.

Direkte vCard-Properties wie `vcard:hasEmail` sind als Alignment-Ziele geeignet. Eine direkte Übernahme als Kernmodell wäre zu eng, weil Construct-X neben klassischen Personen-VCards auch Liefer-, Rechnungs-, Projekt- und Organisationskontakte benötigt.

## 7. SEMIC Core Person

SEMIC Core Person bestätigt, dass Kontaktpunkte für Personen relevant sind. Gleichzeitig trennt SEMIC den Personenkern von Rollen, Organisationen und weiteren Identitätsaspekten. Für Construct-X folgt daraus:

- Die Person darf Kontaktpunkte referenzieren.
- Die Kontaktsemantik gehört nicht in `core/person`.
- Kontakt soll für Organisationen wiederverwendbar sein.

## 8. Construct-X Address

Das vorhandene Address-Modul besitzt `Address`, `AddressAssignment` und kontrollierte Address-Rollen. Damit ist die postalische Struktur bereits abgedeckt.

Das Kontaktmodul besitzt deshalb keine Felder wie `streetName`, `postalCode`, `localityName` oder `country`. Ein postalischer Kontakt wird als Kontaktmethode mit Referenz auf eine bestehende Adresszuordnung modelliert.

Nach Rückprüfung mit dem Address-Konzeptmodell ist die Variante `AddressAssignment` für den MVP festgelegt:

```text
ContactMethod -> usesAddressAssignment -> conx-addr:AddressAssignment
```

Der direkte Verweis auf `Address` würde vorhandene Rollen, c/o, z. Hd. und Abteilung umgehen. Gerade für Lieferung, Rechnung und Korrespondenz sind diese Angaben Teil der fachlichen Kontaktierbarkeit.

## 9. Ergebnisentscheidungen

Aus der Analyse folgen diese umgesetzten Entscheidungen:

1. Das Kontaktmodul erhält eine Klasse `ContactPoint`.
2. Ein `ContactPoint` bündelt mehrere `ContactMethod`-Ressourcen.
3. Eine `ContactMethod` beschreibt genau einen Kanal.
4. Die bevorzugte Lesrichtung ist `Agent -> hasContactPoint -> ContactPoint`.
5. Eine inverse Property `isContactPointFor` ist optional.
6. Kontaktkanäle werden als erweiterbares SKOS-Vokabular modelliert.
7. Privat, beruflich und offiziell werden als `contactUsage` getrennt modelliert.
8. Prozesszwecke wie Lieferung, Rechnung, Support und Notfall werden als `contactPurpose` getrennt modelliert.
9. Social Profiles bleiben generisch und können eine Plattformressource aus `contact-platform` erhalten.
10. Postalische Adressen werden über `usesAddressAssignment` referenziert und bleiben im Address-Modul.
11. `contactType` wird nicht als unscharfe Sammelproperty übernommen.
12. Öffnungszeiten, Servicegebiete, Kontaktoptionen und strengere Syntaxprofile bleiben Erweiterungskandidaten.

## 10. Offene Punkte

| Thema | Warum offen |
| --- | --- |
| Strengere Syntaxvalidierung | E-Mail- und Telefonwerte starten im Core-Profil als nicht-leere Strings; strengere Muster gehören in fachliche Profile |
| Verfügbarkeit | `availabilityNote` ist schnell umsetzbar, echte Öffnungszeiten brauchen ein Zeitmodell |

Diese Punkte blockieren den MVP nicht. Sie sind Kandidaten für spätere Fachprofile oder eigenständige Erweiterungen.

## 11. Verständliches Übertragungsbeispiel

> Ein UBL-Kontakt mit E-Mail und Telefon wird als ein ContactPoint mit zwei
> ContactMethods übernommen. Ein unscharfes Quellfeld wie `contactType` wird
> nicht kopiert, sondern fachlich in Nutzung und Zweck getrennt.
