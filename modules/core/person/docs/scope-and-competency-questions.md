# Scope und Kompetenzfragen der Personenontologie

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

## 1. Zweck

Die Personenontologie beschreibt natürliche Personen und deren unmittelbar personenbezogene Kerndaten. Sie soll Personen in Construct-X eindeutig referenzierbar machen, ohne Organisationsstrukturen, Projekte, Adressen, Qualifikationen oder digitale Identitätsnachweise selbst auszumodellieren.

Dieses Dokument legt den fachlichen Scope und die Kompetenzfragen fest. Klassen, Properties, IRIs, Kardinalitäten und Imports sind bis zur anschließenden Modellierungsphase als Vorschläge zu verstehen.

## 2. Bestätigter Scope

| Bereich | Entscheidung für den MVP |
| --- | --- |
| Gegenstand | Reale natürliche Personen; keine fiktiven Figuren und keine Organisationen |
| Referenzierung | Jede Person wird durch eine vom jeweiligen Datenhalter kontrollierte IRI referenziert |
| Namen | `fullName` und `givenName` verpflichtend; `familyName`, `additionalName` und `birthName` im Kern optional |
| Geburt | Vollständiges Geburtsdatum als `xsd:date`; Geburtsort als einfacher Textwert |
| Geschlecht | `sex` und `gender` als zwei getrennte, optionale Angaben; `sex` gemäß ISO/IEC 5218:2022 und vier Gender-Startwerte |
| Staatsangehörigkeit | Verknüpfung mit bestehenden ISO-3166-1-Länderressourcen; mehrere Werte sind möglich |
| Identifikatoren | Generische, strukturierte Identifikatoren gemäß dem Construct-X-ADMS-Profil |
| Identitätsnachweise | Generische Verknüpfung zu extern modellierten Dokumenten, Credentials oder Verifikationsmethoden |
| Kontakt | Zuordnung über ein eigenständiges, wiederverwendbares Kontaktmodul |
| Adresse | Zuordnung über das vorhandene Adressmodul und dessen `AddressAssignment`-Muster |
| Organisation und Projekt | Beziehungen werden in den jeweils zuständigen Modulen modelliert |
| Agent | Minimale gemeinsame Oberklasse in einem separaten Modul `core/agent` |

## 3. Fachliches Zielbild

```text
Agent
  └── Person
        ├── Namen
        ├── Geburtsdaten
        ├── sex / gender
        ├── Staatsangehörigkeiten
        ├── Identifikatoren
        └── Verweise auf externe Identitätsnachweise

Person       ── hasContactPoint ── Kontaktpunkt ── Kontaktmethode
Person       ── Adresszuordnung  ── Adresse
Person       ── Mitgliedschaft   ── Organisation      (`core/organization`)
Person       ── Beteiligung      ── Projekt           (Projektmodul)
```

Die Pfeile zeigen fachliche Verknüpfungen, nicht automatisch OWL-Imports. Die zuständigen Module und Abhängigkeitsregeln sind in [module-boundaries.md](module-boundaries.md) festgelegt.

## 4. Kompetenzfragen

### CQ-01: Wie wird eine natürliche Person eindeutig referenziert?

Eine Person erhält eine stabile IRI im Namensraum des Datenhalters. Die IRI ist die technische RDF-Identität der Ressource. Ausweisnummern, Personalnummern, Registerkennzeichen, Credentials oder öffentliche Schlüssel sind zusätzliche Identifikations- beziehungsweise Nachweisressourcen und ersetzen die Personen-IRI nicht.

Das Modell muss darstellen können:

- eine Person mit mehreren Identifikatoren,
- das jeweilige Identifikatorschema,
- die ausstellende Stelle beziehungsweise Schema-Agentur,
- einen Verweis auf einen externen Identitätsnachweis,
- einen Nachweis, dessen Inhaber oder Subjekt die Person ist.

### CQ-02: Wie werden Namen und Namensänderungen dargestellt?

Der MVP umfasst:

- Vorname (`givenName`) verpflichtend,
- Nachname (`familyName`) als optionales Kernfeld,
- weitere Vornamen oder Zweitnamen (`additionalName`) optional,
- vollständiger Name (`fullName`) als verpflichtende, direkt ausgebbare Bezeichnung,
- Geburtsname (`birthName`) optional.

`familyName` bleibt optional, damit Personen ohne Familiennamen nicht aus dem Modell ausgeschlossen werden. `additionalName` ist gegenüber dem kulturell engeren Begriff `middleName` zu bevorzugen, kann aber auf `schema:additionalName` und UBL `MiddleName` abgebildet werden. Eine allgemeine Historisierung beliebiger Namensänderungen ist nicht Teil des MVP. Der Geburtsname bildet lediglich den ausdrücklich gewünschten Ausgangsfall ab.

### CQ-03: Wie werden `sex` und `gender` unterschieden?

Beide Angaben sind optional und werden nicht als Synonyme behandelt:

- `sex` beschreibt eine biologische beziehungsweise in amtlichen Kontexten erfasste Geschlechtsangabe.
- `gender` beschreibt Geschlechtsidentität, Ausdruck oder eine soziale beziehungsweise rechtliche Einordnung im jeweiligen Anwendungskontext.

Beide Angaben verweisen auf kontrollierte Konzepte. Für `sex` wird ein getrennt versioniertes Referenzvokabular auf Basis von [ISO/IEC 5218:2022](https://www.iso.org/standard/81682.html) verwendet:

| Code | Bedeutung       | Modellhinweis                                                                                                     |
| ---- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| `0`  | Nicht bekannt   | Positive Aussage, dass der Wert beim Ersteller nicht bekannt ist                                                  |
| `1`  | Männlich        | Klassifikationswert für den Datenaustausch                                                                        |
| `2`  | Weiblich        | Klassifikationswert für den Datenaustausch                                                                        |
| `9`  | Nicht anwendbar | Kein Wert für weitere Geschlechtsidentitäten; bei natürlichen Personen nur mit begründetem Quellkontext verwenden |

Das vollständige Fehlen der Property bedeutet „keine Aussage vorhanden“ und ist nicht gleichbedeutend mit Code `0`. ISO/IEC 5218 beschreibt ausdrücklich menschliches Geschlecht für den Informationsaustausch und keine Genderidentitäten.

Für `gender` wird ein eigenes Construct-X-Referenzvokabular mit vier Startwerten verwendet:

- `gender:man` für Mann,
- `gender:woman` für Frau,
- `gender:nonBinaryOrDiverse` als vorläufiger erweiterbarer Sammelbegriff für nicht-binäre oder genderdiverse Identitäten,
- `gender:notDisclosed` für die ausdrücklich gewählte Nichtoffenlegung.

`gender:notDisclosed` ist keine Identität und unterscheidet sich vom vollständigen Fehlen der Property. Die EU-Tabelle `grammatical-gender` darf nicht für Personen verwendet werden.

### CQ-04: Wie werden Geburtsdatum und Geburtsort beschrieben?

Das Geburtsdatum gehört zum MVP. Es werden ausschließlich vollständige Datumswerte mit `xsd:date` unterstützt. Teilangaben wie nur Jahr oder Jahr/Monat gehören nicht zum MVP.

Der Geburtsort wird bewusst als einfacher Textwert modelliert. Eine Verknüpfung mit einer Ortsressource ist im MVP nicht erforderlich.

### CQ-05: Wie wird Staatsangehörigkeit abgebildet?

Eine Person kann mit null, einer oder mehreren Länderressourcen aus dem bestehenden Construct-X-Ländervokabular verknüpft werden. Dieses basiert auf ISO 3166-1.

NUTS-2 und ISO 3166-2 sind dafür ungeeignet: Sie klassifizieren Regionen beziehungsweise administrative Unterteilungen und keine Staatsangehörigkeiten. Staatenlosigkeit wird im MVP nicht gesondert modelliert. Das Fehlen von `citizenship` bleibt deshalb eine bloße Abwesenheit der Aussage und darf nicht automatisch als Staatenlosigkeit interpretiert werden.

### CQ-06: Wie werden Identifikatoren und deren Herausgeber beschrieben?

Identifikatoren folgen dem bestehenden ADMS-Profil:

- `adms:Identifier` repräsentiert die Identifikatorressource,
- `skos:notation` enthält den Wert,
- der Datentyp der Notation kennzeichnet das Identifikatorschema,
- `adms:schemaAgency` kann den Namen der zuständigen Schema-Agentur enthalten.

Für eine maschinenlesbare Beziehung zur verantwortlichen ausstellenden Stelle ist ergänzend eine Beziehung wie `issuedBy` zu einem `Agent` vorzusehen. Ein technischer Ausgabedienst kann bei Bedarf getrennt als `issuedThrough` beschrieben werden. Konkrete Identifikatorschemata werden erst nach der internen Projektklärung festgelegt.

### CQ-07: Wie werden Ausweise, Credentials und öffentliche Schlüssel angebunden?

Die Personenontologie erhält die generische Beziehung `hasIdentityEvidence`. Ihr Ziel ist eine externe Ressource, beispielsweise eine Ausweisdokumentreferenz, eine Führerscheinreferenz, ein Verifiable Credential, ein behördlicher Registerauszug oder ein anderer digital prüfbarer Nachweis.

Die Detailmodelle für Dokumentnummern, Gültigkeit, Status, Widerruf, kryptografische Schlüssel und Nachweisverfahren gehören nicht in das Personenmodul. Ein öffentlicher Schlüssel belegt zunächst nur die Kontrolle über eine Verifikationsmethode. Erst ein durch einen vertrauenswürdigen Herausgeber ausgestellter Nachweis kann ihn belastbar mit einer natürlichen Person verbinden.

### CQ-08: Wie werden private und berufliche Kontaktinformationen unterschieden?

Kontaktinformationen werden über ein separates Kontaktmodul zugeordnet. Die beschriebene Ressource verweist mit `hasContactPoint` auf einen Kontaktpunkt; dieser bündelt konkrete `ContactMethod`-Ressourcen wie E-Mail, Telefon, Website oder postalische Adresszuordnung. `hasContactPoint` erhält im offenen Kern keine feste OWL-Domain und bleibt dadurch auch für Organisationen, Projekte oder Stellen verwendbar.

Privat, beruflich oder offiziell wird als `contactUsage` am Kontaktpunkt modelliert. Ein davon getrennter `contactPurpose` kann Zwecke wie allgemein, Lieferung, Rechnung, Support oder Notfall ausdrücken. Dadurch werden Telefonnummern oder E-Mail-Adressen nicht als starre Properties der Person behandelt. Funktionale Kontakte wie „Bauleitung“ oder „Rechnungsstelle“ bleiben möglich, ohne sie als persönliche Namen zu missverstehen. Der Usage-Wert `private` ist keine Zugriffsregel; Berechtigungen bleiben außerhalb des Kontaktmodells.

### CQ-09: Welche Adressen dürfen einer Person zugeordnet werden?

Das vorhandene Adressmodul wird wiederverwendet. Für Personen sind insbesondere folgende Rollen relevant:

- `RegistrationAddressRole` für die Meldeadresse,
- `ResidenceAddressRole` für die Wohnadresse,
- `PostalAddressRole` für eine Korrespondenzadresse.

Eine Firmen- oder Standortadresse gehört primär zur Organisation beziehungsweise zum Standort. Sie soll nicht allein aufgrund einer Beschäftigung direkt zur Person kopiert werden. Eine direkte berufliche Korrespondenzadresse kann später über eine ausdrückliche Adressrolle abgebildet werden, falls ein belastbarer Anwendungsfall vorliegt.

### CQ-10: Wie wird eine Person mit Organisationen oder Projekten verbunden?

Mitgliedschaften, Beschäftigungen und Projektbeteiligungen sind keine intrinsischen Personeneigenschaften. Sie werden in den fachlich zuständigen Modulen modelliert:

- Organisationsmodul: Mitgliedschaft, Beschäftigung, Rolle, Stelle und inverse Beziehungen,
- Projektmodul: Beteiligung, Projektrolle und Gültigkeitszeitraum.

Einfache Abkürzungseigenschaften wie `isMemberOf` und `hasMember` können dort ergänzend definiert werden. Für Beziehungen mit Rolle und Zeitraum ist eine eigene Mitgliedschafts- oder Beteiligungsressource erforderlich. Das ist ein fachliches n-äres Beziehungsmuster und keine allgemeine RDF-Reifikation.

### CQ-11: Wie werden Quelle, Gültigkeit und Version personenbezogener Aussagen beschrieben?

Eine allgemeine Provenienz- und Historisierungsschicht für einzelne Aussagen ist nicht Teil des MVP. Das schließt nicht aus, dass externe Identifikator-, Dokument- oder Credential-Ressourcen ihre eigenen fachlich notwendigen Angaben zu Ausstellung, Ablauf, Status oder Widerruf besitzen.

### CQ-12: Welche Validierungsfragen beantwortet das Core-SHACL-Profil?

Das implementierte Core-Profil prüft:

- dass `fullName` und `givenName` jeweils mindestens einmal vorhanden sind,
- dass Geburtsdaten vollständige `xsd:date`-Werte sind,
- dass `sex` und `gender` jeweils höchstens einen Wert besitzen,
- dass `sex` nur Werte des freigegebenen ISO/IEC-5218-Vokabulars verwendet,
- dass `gender` nur einen der vier freigegebenen Startwerte verwendet,
- ob Staatsangehörigkeiten ausschließlich aus dem freigegebenen Ländervokabular stammen,
- welche Mindestangaben ein Identifikator und ein Identitätsnachweisverweis besitzen müssen.

## 5. Ausdrücklich außerhalb des Personenkerns

- Organisationsdaten, Beschäftigungsverhältnisse, Mitgliedschaften, Stellen und Rollen
- Projektbeteiligungen und Projektrollen
- vollständige Adress- und Kontaktmodelle
- Qualifikationen, Zertifikate und berufliche Befähigungen
- Detailmodelle für Ausweise, Identitätsdokumente und Verifiable Credentials
- öffentliche Schlüssel, Authentifizierung, Konten und Berechtigungen
- Bank- und Zahlungsdaten
- biometrische und gesundheitliche Daten
- Familien-, Haushalts- und soziale Beziehungen
- Vollmachten und rechtliche Vertretung
- Interessen, Präferenzen und Profile in sozialen Netzwerken
- allgemeine Provenienz, Aussagehistorie und RDF-Reifikation

Diese Ausschlüsse verhindern nicht die spätere Verknüpfung mit entsprechenden Ressourcen. Sie legen lediglich fest, dass deren Semantik nicht vom Personenmodul besessen wird.

## 6. Nicht blockierende Folgeentscheidungen

| Thema | Folgeentscheidung | Auswirkung |
| --- | --- | --- |
| Gender-Erweiterung | Feinere Unterteilung des Werts `nonBinaryOrDiverse` und langfristige Governance | Referenzvokabular |
| Identitätsnachweise | Detailmodell nach Auswahl des Sicherheits- und Vertrauensmodells | externes Identitäts- oder Credential-Profil |

## 7. Umgesetzte Abnahmekriterien

Die Ontologie und ihre Core Shapes wurden umgesetzt, nachdem:

1. die Modulgrenzen und die Rolle von `core/agent` bestätigt wurden,
2. die lokalen Begriffe samt Zuständigkeit festgelegt wurden,
3. Folgeentscheidungen als nicht blockierend eingeordnet wurden,
4. externe Vokabulare als referenziert oder ausgerichtet dokumentiert wurden,
5. das Core-SHACL-Profil abgestimmt wurde.

Der fachliche Begriffskatalog ist in [term-catalog.md](term-catalog.md) dokumentiert. Die gemeinsame Agent-Oberklasse ist in der [Agent-Spezifikation](../../agent/docs/agent-specification.md) beschrieben. Die ausführbaren Datenanforderungen sind fachlich in den [SHACL-Anforderungen](shacl-requirements.md) festgelegt.

## 8. Umsetzungsstand

`core/agent`, `core/person`, die Referenzvokabulare und das Core-SHACL-Profil
sind implementiert, getestet, dokumentiert und in den Netzwerkmetadaten
registriert.

## 9. Verständliches Beispiel

> Anna Müller kann mit vollständigem Namen und Geburtsdatum beschrieben
> werden. Eine fehlende Genderangabe bedeutet nur, dass im Datensatz keine
> Aussage vorliegt; sie wird nicht automatisch als `notDisclosed` interpretiert.
