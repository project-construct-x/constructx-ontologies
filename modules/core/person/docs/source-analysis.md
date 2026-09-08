# Quellenanalyse für die Personenontologie

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 20. August 2026  
**Geltungsbereich:** `core/person`

## 1. Ziel und Methode

Diese Analyse bewertet vorhandene Personen-, Kontakt-, Organisations- und Identitätsmodelle als Grundlage für den Construct-X-Personenkern. Untersucht wurden insbesondere:

- fachliche Abdeckung und Begriffsdefinitionen,
- Eignung als normativer Kern oder als Alignment-Ziel,
- Abgrenzung zu den weiteren Construct-X-Core-Modulen,
- Identifikatoren und Identitätsnachweise,
- Namens-, Geburts-, Geschlechts- und Staatsangehörigkeitsdaten,
- Kontakt-, Adress-, Organisations- und Projektbezüge,
- Risiken durch zu breite Domains, unklare Wertebereiche oder sensible Identifikatoren.

Die Analyse wurde als Grundlage für die lokalen IRIs, Referenzen und Axiome der T-Box 0.1.0 sowie für die Person Core Shapes verwendet.

## 2. Kurzfazit

Der [SEMIC Core Person Vocabulary 2.1.2](https://semiceu.github.io/Core-Person-Vocabulary/releases/2.1.2/) ist die fachlich geeignetste Hauptreferenz. Er beschreibt reale natürliche Personen, trennt `sex` und `gender`, unterstützt mehrere Staatsangehörigkeiten und verwendet ADMS für Identifikatoren.

[UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-CatalogueRequest-2.5.html) liefert wichtige Austauschfelder aus Geschäftsprozessen, mischt im Person-Aggregat jedoch intrinsische Daten mit Beschäftigung, Kontakt, Finanzkonto und Dokumentreferenzen. Diese Felder müssen in Construct-X auf getrennte Module verteilt werden.

[Schema.org Person](https://schema.org/Person), [FOAF](https://xmlns.com/foaf/spec/) und [vCard RDF](https://www.w3.org/TR/vcard-rdf/) sind wertvolle Interoperabilitätsquellen, aber allein nicht präzise genug für ein qualitätsgesichertes Kernmodell. Das [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) bestätigt die Auslagerung von Mitgliedschaften und Rollen. [W3C Controlled Identifiers](https://www.w3.org/TR/cid/) und das [Verifiable Credentials Data Model 2.1](https://www.w3.org/TR/vc-data-model-2.1/) bestätigen die Trennung zwischen Person, Schlüssel und überprüfbarem Identitätsnachweis.

## 3. Bewertete Quellen

| Quelle | Verwendeter Stand | Rolle in der Analyse | Vorläufige Nutzung |
| --- | --- | --- | --- |
| [SEMIC Core Person Vocabulary](https://semiceu.github.io/Core-Person-Vocabulary/releases/2.1.2/) | 2.1.2 | Europäisches semantisches Personenmodell | Primäre fachliche Referenz und Alignment-Kandidat |
| [OASIS UBL](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-CatalogueRequest-2.5.html) | 2.5 CS01 | Geschäfts- und Dokumentenaustausch | Feldanalyse und Mappingquelle |
| [Schema.org Person](https://schema.org/Person) | Entwicklungsversion, abgerufen 2026-08-20 | Breite Web-Interoperabilität | Alignment- und Benennungsquelle |
| [W3C vCard Ontology](https://www.w3.org/TR/vcard-rdf/) | W3C Interest Group Note, 2014 | Strukturierte Namen und Kontakte | Referenz des eigenständigen Kontaktmoduls |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99 | Agent-/Person-Grundmodell und Web-Identität | Alignment-Kandidat mit Einschränkungen |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 2014 | Organisation, Mitgliedschaft, Rolle und Stelle | Grundlage des Organisationsmoduls |
| [ADMS](https://semiceu.github.io/ADMS/releases/2.00/) | 2.0 | Strukturierte Identifikatoren | Wiederverwendung gemäß Construct-X-Architektur |
| [W3C Controlled Identifiers](https://www.w3.org/TR/cid/) | W3C Recommendation | Schlüssel und Verifikationsmethoden | Grundlage für externes Identitätsmodell |
| [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model-2.1/) | 2.1 | Herausgeber, Subjekt, Evidenz, Status und Gültigkeit | Grundlage für externe Nachweise |
| [ISO/IEC 5218](https://www.iso.org/standard/81682.html) | 2022, Edition 2 | Sprachunabhängige Codes für menschliches Geschlecht im Informationsaustausch | Normative Grundlage des `sex`-Vokabulars |
| [EU Authority Table Human Sex](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http%3A%2F%2Fpublications.europa.eu%2Fresource%2Fdataset%2Fhuman-sex) | angezeigter Stand 20241211-0 | Bestehende kontrollierte Werte für `sex` | Alignment- und Wiederverwendungskandidat |
| [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) und [EU Country Authority Table](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/country) | laufend gepflegt | Länderreferenzen | Über bestehendes Construct-X-Vokabular wiederverwenden |
| [Data Privacy Vocabulary](https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/) | 2.0 Final Community Group Report | Datenschutz und Verarbeitungszwecke | Spätere Governance-Schicht, nicht Person-T-Box |

Zusätzlich wurden die vorhandenen Construct-X-Festlegungen ausgewertet:

- [Identifier-Modell](../../../../docs/architecture/identifier-model.md)
- [Namespace-Konzept](../../../../docs/architecture/construct-x-namespace-konzept.md)
- [Adressrollen](../../address/docs/address-roles.md)
- [Adress-Konzeptmodell](../../address/docs/concept-model.md)
- [ISO-3166-1-Länderdatensatz](../../../../datasets/reference/administrative-territories/iso-3166-1-countries/README.md)
- [Identifier-Scheme-Vokabular](../../../../datasets/reference/vocabularies/identifier-scheme/README.md)

## 4. Analyse der Person- und Agent-Konzepte

### 4.1 SEMIC Core Person

SEMIC definiert `Person` als reale natürliche Person, lebend oder verstorben. Fiktive Personen sind ausgeschlossen. Die Klasse ist sowohl `foaf:Person` als auch `cv:Agent` untergeordnet. Das entspricht dem Construct-X-Ziel genauer als das breitere Schema.org-Modell.

Die Quelle deckt Namen, Geburt, Tod, Wohnsitz, Staatsangehörigkeit, Identifikatoren, Kontaktpunkte, `sex` und `gender` ab. Einige dieser Bereiche gehen über den Construct-X-MVP hinaus oder gehören dort in andere Module. SEMIC ist deshalb eine fachliche Baseline, aber nicht als vollständige Kopie zu übernehmen.

### 4.2 Schema.org

`schema:Person` umfasst auch fiktive Personen. Außerdem besitzt die Klasse eine sehr breite Zahl von Properties, unter anderem Beschäftigung, Mitgliedschaft, Zugehörigkeit, Qualifikationen, Beziehungen, Besitz und Onlineprofile. Viele Wertebereiche erlauben alternativ Ressourcen, Text oder URLs.

Diese Offenheit ist für Web-Markup nützlich, aber für ein prüfbares Construct-X-Modul zu schwach. Geeignet sind vor allem:

- etablierte Benennungen wie `givenName`, `familyName` und `additionalName`,
- Alignments für allgemeine Interoperabilität,
- `ContactPoint` als Bestätigung eines eigenständigen Kontaktkonzepts.

### 4.3 FOAF

FOAF bietet die bewährten Klassen `foaf:Agent`, `foaf:Person` und `foaf:Organization`. Es ist deshalb ein Alignment-Ziel des implementierten `core/agent`.

Der Schwerpunkt liegt jedoch auf sozialen und webbasierten Identitäten. Properties wie `foaf:mbox`, Konten und OpenID sind kein geeigneter Kern für Construct-X. Besonders `foaf:mbox` ist als inverse-funktionale Property konzipiert und kann E-Mail-Adressen zu starken, personenbezogenen Identifikatoren machen. Das ist für Datenminimierung und wechselnde Kontaktinformationen problematisch.

### 4.4 Bewertung

| Frage | Entscheidung |
| --- | --- |
| Lokale Klasse `Person`? | Ja, mit Construct-X-eigenem Namespace und Profil |
| Reale natürliche Person als Bedeutung? | Ja, wie SEMIC; keine fiktiven Personen |
| Gemeinsame Klasse `Agent`? | Ja, aber in separatem `core/agent` |
| FOAF direkt wiederverwenden? | Primär als Alignment; Importbedarf später prüfen |
| Schema.org direkt als Kern verwenden? | Nein; Wertebereiche und Scope sind zu breit |

## 5. Namensmodell

### 5.1 Vergleich

| Konzept | SEMIC Core Person | UBL 2.5 | Schema.org | vCard RDF | Construct-X-Bewertung |
| --- | --- | --- | --- | --- | --- |
| Vollständiger Name | `fullName`, stark empfohlen | Kein gleichwertiges Person-Feld | `name` | `fn` | Als verpflichtende ausgebbare Bezeichnung aufnehmen |
| Vorname | `givenName`; alle Vornamen können geordnet in einem Wert stehen | `FirstName` | `givenName` | `given-name` | Kernbegriff aufnehmen |
| Nachname | `familyName` | `FamilyName` | `familyName` | `family-name` | Kernbegriff aufnehmen |
| Zweit-/weitere Namen | Nicht als eigenes Kernfeld; über `givenName` abdeckbar | `MiddleName` | `additionalName` | `additional-name` | Optional als `additionalName` aufnehmen |
| Geburtsname | `birthName` als kompletter Name bei Geburt | Kein direktes Äquivalent | Kein spezifischer Kernbegriff | Kein spezifischer Kernbegriff | Optional aufnehmen |
| Titel/Präfix/Suffix | Nicht Kern des gewünschten Profils | `Title`, `NameSuffix` | `honorificPrefix`, `honorificSuffix` | entsprechende Komponenten | Für MVP ausschließen |
| Weitere Familiennamen | Patronymic/Matronymic möglich | `OtherName`, Beispiel zweiter Familienname | kein präzises Muster | über Namenskomponenten möglich | Für MVP ausschließen |

### 5.2 Empfehlung

Der MVP verwendet fünf Begriffe: `fullName`, `givenName`, `additionalName`, `familyName` und `birthName`. `fullName` und `givenName` sind im Core-SHACL-Profil verpflichtend. `familyName` bleibt als Kernbegriff optional, damit Personen ohne Familiennamen nicht ausgeschlossen werden. Mehrfachwerte sollen auf RDF-Ebene nicht unnötig verhindert werden, weil Namen sprach- und kulturabhängig sind.

Eine Reihenfolge mehrerer Vornamen kann durch einen einzigen Literalwert erhalten bleiben. Eine detaillierte Namenskomponenten- oder Namenshistorienklasse ist für den MVP nicht erforderlich.

## 6. Geburtsdaten

| Thema | Quellenlage | Empfehlung |
| --- | --- | --- |
| Geburtsdatum | SEMIC erlaubt `xsd:date`, `xsd:gYearMonth` oder `xsd:gYear`; UBL verwendet `BirthDate`; Schema.org `Date` | `birthDate` aufnehmen und im MVP ausschließlich vollständige `xsd:date`-Werte zulassen |
| Geburtsort | UBL hat sowohl `BirthplaceName` als Text als auch `BirthplaceLocation`; Schema.org erwartet `Place`; SEMIC verwendet eine Location-Ressource | Nutzerentscheidung respektieren und `birthPlaceName` als einfachen String aufnehmen |
| Sterbedaten | SEMIC und Schema.org unterstützen Datum und Ort | Nicht Teil des aktuellen MVP |

Ein Textwert für den Geburtsort ist absichtlich weniger semantisch als eine Ortsressource, hält den Kern aber klein. Eine spätere zusätzliche Objektbeziehung kann ergänzt werden, ohne den MVP-Wert zu entwerten.

## 7. `sex` und `gender`

SEMIC trennt beide Begriffe ausdrücklich:

- `sex` bezieht sich auf biologische Geschlechtsmerkmale beziehungsweise deren amtliche Erfassung.
- `gender` umfasst Identitäten, Ausdrucksformen und gesellschaftliche Rollen und soll kontextangemessen kontrolliert werden.

UBL bietet `GenderCode`, nennt aber je nach Geschäftskontext unterschiedliche Codesysteme wie ISO/IEC 5218 oder ICAO 9303. Schema.org erlaubt für `gender` sowohl `GenderType` als auch freien Text und unterscheidet kein eigenes `sex`-Kernfeld. vCard besitzt eine kombinierte strukturierte Geschlechtsangabe, ist hier aber kein hinreichend präzises Zielmodell.

### Empfehlung

1. `sex` und `gender` werden als getrennte optionale Objektbeziehungen modelliert.
2. Werte sollen SKOS-Konzepte oder gleichwertige kontrollierte Ressourcen sein, keine unkontrollierten Freitexte.
3. Für `sex` wird ein separat versioniertes SKOS-Vokabular auf Basis von ISO/IEC 5218:2022 mit den Codes `0`, `1`, `2` und `9` verwendet.
4. Das Fehlen von `sex` bedeutet „keine Aussage“. Code `0` bedeutet dagegen die ausdrückliche Aussage „nicht bekannt“.
5. Code `9` bedeutet „nicht anwendbar“ und darf nicht als Sammelwert für weitere Geschlechtsidentitäten interpretiert werden. Im Personenkontext ist seine Verwendung nur quellengetreu und begründet sinnvoll.
6. Ein Alignment zur EU Authority Table `human-sex` bleibt einer späteren Einzelprüfung vorbehalten; Version 0.1.0 verwendet zunächst eigene stabile Construct-X-IRIs.
7. Für `gender` wird ein separat versioniertes Construct-X-Startvokabular mit `man`, `woman`, `nonBinaryOrDiverse` und `notDisclosed` verwendet.
8. `nonBinaryOrDiverse` ist ein vorläufiger breiter Begriff, der später durch präzisere Unterkonzepte erweitert werden kann.
9. `notDisclosed` bezeichnet eine ausdrückliche Nichtoffenlegung und keine Genderidentität; das Fehlen der Property bleibt eine nicht vorhandene Aussage.
10. Die EU Authority Table `grammatical-gender` ist linguistisch und darf nicht für Geschlechtsangaben von Personen verwendet werden.

## 8. Staatsangehörigkeit und Länder

SEMIC modelliert Staatsangehörigkeit als rechtliche Beziehung zwischen einer Person und einer Jurisdiktion. Null, eine oder mehrere Staatsangehörigkeiten sind möglich. UBL 2.5 besitzt `CitizenshipCountry` mit Kardinalität `0..n`; das frühere `NationalityID` ist als veraltet markiert, während `NationalityCode` weiterhin vorkommt. Schema.org verwendet `nationality` mit `Country` als Wertebereich.

Construct-X verfügt bereits über ein ISO-3166-1-basiertes Ländervokabular mit stabilen IRIs, beispielsweise:

```text
https://www.construct-x.org/vocab/country#DEU
```

Die Länderressourcen besitzen Alpha-2-, Alpha-3- und numerische ADMS-Identifikatoren. Für die Staatsangehörigkeit soll daher die Länderressource selbst referenziert werden, nicht ein untypisierter Stringcode.

### Bewertung der Alternativen

| System | Eignung für Staatsangehörigkeit | Grund |
| --- | --- | --- |
| ISO 3166-1 | Geeignet | Identifiziert Staaten und abhängige Gebiete auf Länderebene |
| ISO 3166-2 | Nicht als Staatsangehörigkeitswert | Identifiziert administrative Unterteilungen innerhalb von Staaten |
| NUTS-2 | Nicht geeignet | Statistische EU-Regionen, keine Staaten oder Staatsangehörigkeiten |

Die aktuelle Typisierung der Länder als `conx-addr:Country` ist wiederverwendbar, zeigt aber eine Modulgrenze: `Country` ist kein ausschließliches Adresskonzept. Eine spätere Verlagerung in ein geografisches Kernmodul ist architektonisch plausibel, für den Personen-MVP aber nicht erforderlich.

Staatenlosigkeit wird im MVP nicht gesondert modelliert. Sie darf nicht allein aus dem Fehlen von `citizenship` abgeleitet werden, weil auch unbekannte oder nicht freigegebene Daten fehlen können.

## 9. Identifikatoren

### 9.1 Quellenvergleich

SEMIC verwendet `adms:Identifier` und ergänzt unter anderem:

- `skos:notation` für den Identifikatorwert,
- `adms:schemaAgency` für die zuständige Agentur,
- `dct:issued` für das Ausgabedatum,
- `dct:creator` für einen ausstellenden Agenten,
- eine Beziehung zur identifizierten Ressource.

UBL 2.5 bietet eine allgemeine Person-ID und mehrere `NationalID`-Werte. Schema.org lässt für `identifier` wahlweise `PropertyValue`, Text oder URL zu. vCard bietet `hasUID`; FOAF verwendet teilweise starke webbasierte Kennzeichen wie Mailboxen.

### 9.2 Construct-X-Entscheidung

Das bestehende [Construct-X-Identifier-Modell](../../../../docs/architecture/identifier-model.md) ist maßgeblich:

- keine parallele lokale Identifier-Klasse,
- `adms:Identifier` als gemeinsame Struktur,
- `skos:notation` als Wert,
- der Datentyp der Notation identifiziert das Schema,
- `adms:schemaAgency` beschreibt die Schema-Agentur,
- Schemas werden im zentralen Identifier-Scheme-Vokabular geführt.

Die Personenontologie soll diese Struktur verwenden und nur die Beziehung zwischen Person und Identifikator festlegen, sofern sie nicht bereits generisch vorhanden ist. Konkrete nationale, projektbezogene oder betriebliche Identifikatorschemata werden noch nicht ausgewählt.

### 9.3 Herausgeber und technischer Dienst

Die verantwortliche ausstellende Stelle und der technische Ausgabedienst sind nicht zwingend identisch. Das Zielmodell sollte deshalb unterscheiden können:

- `issuedBy`: fachlich beziehungsweise rechtlich verantwortlicher `Agent`,
- `issuedThrough`: optionaler technischer Dienst oder Service.

Organisationen und Services werden dabei nur referenziert. Ihre interne Modellierung gehört in eigene Module.

## 10. Identitätsdokumente, Credentials und öffentliche Schlüssel

UBL erlaubt mehrere `IdentityDocumentReference`-Einträge an einer Person und nennt beispielsweise einen Führerschein. Das bestätigt den Bedarf für eine generische Verbindung, liefert aber kein hinreichendes Sicherheits- oder Vertrauensmodell.

W3C Controlled Identifiers beschreibt kontrollierte Identifikator-Dokumente, Verifikationsmethoden, öffentliche Schlüssel und Service-Endpunkte. Ein erfolgreicher kryptografischer Nachweis zeigt, dass jemand den zugehörigen privaten Schlüssel kontrolliert. Er beweist nicht automatisch Name, Geburtsdatum oder die Existenz einer natürlichen Person.

Das W3C Verifiable Credentials Data Model ergänzt die notwendige Behauptungsstruktur:

- `issuer` für die ausstellende Entität,
- `credentialSubject` für das Subjekt der Aussagen,
- `evidence` für unterstützende Nachweise,
- Gültigkeit und Status einschließlich Widerrufsmechanismen.

### Empfehlung

Das Personenmodul erhält die generische Beziehung `hasIdentityEvidence`. Zulässige Ziele sind externe Ressourcen, etwa Ausweisdokument- oder Führerscheinreferenzen, Verifiable Credentials, behördliche Registerauszüge und andere digital prüfbare Nachweise. Dokument-, Credential- und Schlüsselressourcen werden außerhalb des Moduls modelliert. Insbesondere werden weder Ausweisfelder noch Schlüsselmaterial direkt an `Person` gehängt.

Die folgenden Ebenen bleiben getrennt:

```text
Personen-IRI
   ├── strukturierter fachlicher Identifikator
   ├── Identitätsdokument oder Credential
   └── Verifikationsmethode / öffentlicher Schlüssel
```

Eine belastbare Identitätskette entsteht erst durch explizite Aussagen über Subjekt, Herausgeber, Gültigkeit, Status und verwendete Verifikationsmethode.

## 11. Kontaktmodell

### 11.1 Quellenlage

SEMIC `Contact Point` umfasst insbesondere Kontaktseite, E-Mail und Telefon. Schema.org `ContactPoint` ergänzt unter anderem `contactType`, Servicegebiet, verfügbare Sprache und Öffnungszeiten. Die Typisierung über `contactType` ist dort textbasiert und daher nur begrenzt kontrollierbar.

UBL `Contact` enthält:

- ID und Bezeichnung,
- funktionalen Namen,
- Position und Abteilung,
- Telefon, Fax und E-Mail,
- Notizen und weitere Kommunikationswege.

Die UBL-Dokumentation weist darauf hin, dass ein Kontaktname funktional und nicht zwingend der Name einer Person ist. Das ist für Construct-X wichtig: „Bauleitung“ oder „Rechnungsstelle“ kann ein Kontaktzweck sein, ohne eine natürliche Person zu behaupten. Die ausgewertete UBL-Contact-Struktur ist unter anderem im [UBL Qualification Application Request 2.5](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-QualificationApplicationRequest-2.5.html) dokumentiert.

vCard RDF besitzt strukturierte E-Mail-, Telefon- und weitere Kommunikationsressourcen. Mit Typen wie `Home` und `Work` können Verwendungszusammenhänge ausgedrückt werden. Das n-äre Property-Muster ist besser geeignet als eine starre Property `privateEmail` oder `businessPhone`.

### 11.2 Empfehlung

Ein separates `core/contact` soll mindestens drei Ebenen unterscheiden:

```text
Ressource ── hasContactPoint ── ContactPoint ── hasContactMethod ── ContactMethod
                                      │                              │
                                      ├── ContactUsage               └── ContactChannel + Wert
                                      └── ContactPurpose
```

- `ContactPoint` bündelt die Erreichbarkeit eines Kontaktträgers in einem Nutzungskontext.
- `ContactMethod` beschreibt genau einen Kanal und dessen Wert, URI oder Adresszuordnung.
- `ContactUsage` unterscheidet insbesondere privat, beruflich und offiziell.
- `ContactPurpose` beschreibt davon getrennt einen Zweck wie allgemein, Lieferung, Rechnung, Support oder Notfall.
- `hasContactPoint` besitzt im offenen Kern keine feste OWL-Domain, damit das Muster außer für Agenten auch für Projekte, Stellen oder andere identifizierbare Ressourcen verwendet werden kann.

Die genaue Modellierung von E-Mail- und Telefonwerten, Normalisierung, Mehrsprachigkeit und Erreichbarkeitszeiten liegt im implementierten Kontaktmodul. Die Personenontologie kopiert diese Felder nicht.

## 12. Adressen

UBL trennt `ResidenceAddress` von anderen geschäftlichen Adressen. Das vorhandene Construct-X-Adressmodul ist bereits allgemeiner: Eine `AddressAssignment` kann eine identifizierbare Ressource mit einer Adresse und einer Adressrolle verbinden.

Für Personen sind bestehende Rollen unmittelbar verwendbar:

- Meldeadresse über `RegistrationAddressRole`,
- Wohnadresse über `ResidenceAddressRole`,
- Korrespondenz über `PostalAddressRole`.

Eine Organisations- oder Standortadresse darf nicht automatisch als Adresse eines Angestellten interpretiert werden. Soll eine berufliche Korrespondenzadresse direkt an einer Person erscheinen, benötigt sie einen ausdrücklichen Kontext. Das kann später eine zusätzliche Adressrolle oder eine Zuordnung über Stelle/Organisation sein.

## 13. Organisationen, Beschäftigung und Projekte

UBL führt im Person-Aggregat Felder wie `JobTitle`, `OrganizationDepartment` und `RoleCode`. Schema.org bietet `worksFor`, `memberOf` und `affiliation`. Diese Felder sind für den Datenaustausch praktisch, würden im Personenkern aber Organisations- und Beziehungskonzepte vermischen.

W3C ORG bietet das passendere Zielbild:

- `org:Organization`,
- `org:memberOf` und `org:hasMember`,
- `org:Membership` für eine n-äre Beziehung,
- `org:Role` und `org:Post`,
- zeitliche Gültigkeit einer Mitgliedschaft.

Mitgliedschaften sind deshalb im Organisationsmodul definiert. Beschäftigung,
Positionen und weitere fachliche Beziehungen bleiben außerhalb des
Personenkerns. Die Person bleibt Ziel oder Beteiligter dieser Beziehungen,
besitzt deren Semantik aber nicht.

## 14. UBL-Person im Detail

Die UBL-2.5-Personenkomponente wurde vollständig gegen den bestätigten Scope eingeordnet:

| UBL-Feld | Kardinalität | Construct-X-Zuordnung |
| --- | --- | --- |
| `ID` | `0..1` | Generischer ADMS-Identifikator |
| `FirstName` | `0..1` | `givenName` |
| `FamilyName` | `0..1` | `familyName` |
| `Title` | `0..1` | Nicht im MVP |
| `MiddleName` | `0..1` | `additionalName` |
| `OtherName` | `0..1` | Nicht im MVP; möglicher weiterer Familienname |
| `NameSuffix` | `0..1` | Nicht im MVP |
| `JobTitle` | `0..1` | Organisationsmodul |
| `NationalityID` | `0..1` | Veraltet; nicht übernehmen |
| `NationalID` | `0..n` | Strukturierter Identifikator |
| `NationalityCode` | `0..1` | Durch Länderressource statt Literalcode ersetzen |
| `GenderCode` | `0..1` | Quelleninput für getrennte `sex`-/`gender`-Entscheidung |
| `BirthDate` | `0..1` | `birthDate` |
| `BirthplaceName` | `0..1` | `birthPlaceName` als String |
| `OrganizationDepartment` | `0..1` | Organisationsmodul |
| `RoleCode` | `0..1` | Organisations- oder Projektmodul |
| `BirthplaceLocation` | `0..1` | Außerhalb des MVP |
| `CitizenshipCountry` | `0..n` | Verknüpfung mit ISO-3166-1-Länderressourcen |
| `Contact` | `0..1` | Kontaktmodul |
| `FinancialAccount` | `0..1` | Ausdrücklich außerhalb des Personenkerns |
| `IdentityDocumentReference` | `0..n` | Generische Verbindung; Details im Identitätsmodul |
| `ResidenceAddress` | `0..1` | Adressmodul mit `ResidenceAddressRole` |

UBL bestätigt damit beinahe alle benötigten Datengruppen, aber nicht deren gewünschte modulare Trennung.

## 15. Implementiertes Construct-X-Zielprofil

Die folgende Tabelle dokumentiert das aus der Analyse abgeleitete und in
Version `0.1.0` umgesetzte Zielprofil.

| Begriff | Art | Vorgeschlagener Bereich | MVP-Profil | Herkunft/Begründung |
| --- | --- | --- | --- | --- |
| `Agent` | Klasse in `core/agent` | - | gemeinsame Oberklasse | FOAF, SEMIC, ORG |
| `Person` | Klasse | `Agent` | reale natürliche Person | SEMIC als Hauptdefinition |
| `fullName` | Datatype Property | sprachfähiges Literal oder String | verpflichtend | SEMIC `fullName`, vCard `fn` |
| `givenName` | Datatype Property | sprachfähiges Literal oder String | verpflichtend | SEMIC, UBL, Schema.org, vCard |
| `additionalName` | Datatype Property | sprachfähiges Literal oder String | optional | Schema.org, vCard, UBL `MiddleName` |
| `familyName` | Datatype Property | sprachfähiges Literal oder String | optionales Kernfeld | SEMIC, UBL, Schema.org, vCard |
| `birthName` | Datatype Property | sprachfähiges Literal oder String | optional | SEMIC |
| `birthDate` | Datatype Property | zunächst `xsd:date` | optional, höchstens ein Wert | SEMIC, UBL, Schema.org |
| `birthPlaceName` | Datatype Property | `xsd:string` | optional, höchstens ein Wert | UBL und Nutzerentscheidung |
| `sex` | Object Property | ISO/IEC-5218-Konzept | optional, höchstens ein Wert | SEMIC und ISO/IEC 5218:2022 |
| `gender` | Object Property | Konzept aus dem Construct-X-Gender-Vokabular | optional, höchstens ein Wert | SEMIC und bestätigtes Startvokabular |
| `citizenship` | Object Property | bestehende Länderressource | optional, mehrere Werte | SEMIC, UBL, ISO 3166-1 |
| Personen-Identifier-Beziehung | Object Property | `adms:Identifier` | optional, mehrere Werte | ADMS und Construct-X-Profil |
| `hasIdentityEvidence` | Object Property | externe Nachweisressource | optional, mehrere Werte | UBL, Controlled Identifiers, VC |

Kontakt- und Adressbeziehungen erscheinen absichtlich nicht als Besitz des Personenmoduls. Sie werden über die Properties der zuständigen Module auf Personeninstanzen angewendet.

## 16. T-Box- und A-Box-Abgrenzung

In der Implementierung werden folgende Artefaktarten getrennt:

### T-Box

- Klassen `Agent` und `Person`,
- Personen-Properties und ihre Definitionen,
- Domain-, Range-, Subklassen- und Alignment-Axiome,
- gegebenenfalls semantische Einschränkungen, die unabhängig von einem Anwendungsprofil gelten.

### A-Box beziehungsweise Referenzvokabulare

- konkrete Länder wie `country:DEU`,
- kontrollierte Werte für `sex` und `gender`,
- konkrete Identifikatorschemata,
- Kontakt- und Adressrollen,
- konkrete Personen, Identifikatoren und Nachweise in Datenhalter-Namespaces.

Kontrollierte Werte sollen in separaten Vokabularen versioniert werden und nicht als feste Individuen in die Personen-T-Box eingebettet sein.

## 17. Datenschutz- und Governance-Bewertung

Personen-IRIs und personenbezogene Identifier dürfen nicht mit globaler öffentlicher Auffindbarkeit gleichgesetzt werden. Welche Daten veröffentlicht, ausgetauscht oder zugriffsgeschützt werden, ist eine Governance- und Berechtigungsfrage oberhalb der Ontologie.

Für den Modellumfang gelten dennoch folgende Grundsätze:

- keine E-Mail-Adresse als standardmäßiger Identitätsschlüssel,
- keine öffentlichen Schlüssel direkt als Person-Identifier,
- keine unnötige Kopie von Organisations- oder Standortdaten an Personen,
- sensible Nachweise nur als kontrollierte externe Ressourcen,
- ausdrückliche Unterscheidung zwischen unbekannt, nicht freigegeben und fachlich nicht vorhanden, sobald der Anwendungsfall dies benötigt.

Das W3C Data Privacy Vocabulary kann später Verarbeitung, Zweck, Rechtsgrundlage und technische Maßnahmen beschreiben. Es wird nicht Teil der Personen-T-Box.

## 18. Ergebnisentscheidungen

Aus der Quellenanalyse folgen für die Modellierungsphase diese belastbaren Entscheidungen:

1. SEMIC Core Person 2.1.2 ist die primäre fachliche Referenz.
2. Construct-X definiert eine eigene, auf reale natürliche Personen begrenzte Klasse `Person`.
3. `Agent` ist als minimale gemeinsame Klasse in einem separaten Kernmodul umgesetzt.
4. Der Namenskern besteht aus `fullName`, `givenName`, `additionalName`, `familyName` und `birthName`.
5. `fullName` und `givenName` werden im Core-SHACL-Profil verpflichtend.
6. Geburtsdaten werden nur als vollständige `xsd:date`-Werte akzeptiert; Geburtsort bleibt ein Textwert.
7. `sex` und `gender` werden getrennt und optional modelliert; `sex` basiert auf ISO/IEC 5218:2022 und `gender` startet mit vier Construct-X-Konzepten.
8. Staatsangehörigkeit verweist auf ISO-3166-1-basierte Construct-X-Länderressourcen; NUTS-2 ist ausgeschlossen.
9. Identifikatoren verwenden das bestehende ADMS-Profil.
10. `hasIdentityEvidence` verknüpft Personen generisch mit externen Nachweisressourcen.
11. Identitätsdokumente, Credentials und öffentliche Schlüssel werden nicht in der Personenontologie detailliert.
12. Kontakt ist als eigenständiges, domänenoffenes Zuordnungsmodell mit ausgehender Beziehung vom Kontaktträger umgesetzt.
13. Adressen verwenden das vorhandene `AddressAssignment`-Modell.
14. Mitgliedschaften, Beschäftigung und Projektbeteiligung liegen bei Organisation beziehungsweise Projekt.
15. Allgemeine Aussageprovenienz und Reifikation bleiben außerhalb des MVP.

## 19. Offene Punkte nach der T-Box-Implementierung

- feinere Erweiterung und langfristige Governance des Gender-Vokabulars,
- direkte Wiederverwendung oder Alignment der EU Authority Table `human-sex`,
- maschinenlesbares Issuer-Modell zusätzlich zu `adms:schemaAgency`,
- erstes kontrolliertes Rollen-Vokabular des Kontaktmoduls,
- langfristige Eigentümerschaft der Klasse `Country`,
- genaue Import-, Referenz- und Alignment-Entscheidung je externer Quelle.

Diese Punkte blockieren die T-Box 0.1.0 nicht. Sie bilden die gezielte Entscheidungsliste für Alignments und Folgemodule. Die einzelnen lokalen Begriffe sind im [Begriffskatalog](term-catalog.md), ihre implementierten Validierungsverträge im [SHACL-Anforderungsprofil](shacl-requirements.md) beschrieben.

## 20. Verständliches Übertragungsbeispiel

> SEMIC liefert ein breites Personenmodell, UBL geschäftliche Personendaten und
> vCard Kontaktmuster. Construct-X übernimmt daraus nur intrinsische
> Personendaten; Kontakt und Organisation bleiben in eigenen Core-Modulen.
