# Quellenanalyse für das Document Core Modul

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 27. August 2026  
**Geltungsbereich:** `core/document`  
**Gegenstand:** Dokumente, Dokumentreferenzen, Distributionen, Dokumentmetadaten, Nachweis- und Signaturabgrenzung

## 1. Ziel und Methode

Diese Analyse bewertet bestehende Ontologien, Vokabulare, Austauschformate und
Rechts-/Vertrauensmodelle als fachliche Grundlage des implementierten
Construct-X-Moduls `core/document`.

Untersucht wurden insbesondere:

- allgemeine Dokument- und Informationsobjektbegriffe,
- Dokumentreferenzen in Geschäfts- und Verwaltungsprozessen,
- Anhänge, externe Dateien, Distributionen und Formate,
- Titel, Datum, Sprache, Version, Status und Dokumenttyp,
- Identifikatoren und strukturierte Kennungen,
- Urheberschaft, Herausgeber, Aussteller und Empfänger,
- Nachweise, Credentials, Signaturen und Vertrauensinformationen,
- Zugriffsrechte und Nutzungsbedingungen,
- Abgrenzung zu `core/agent`, `core/participation`, `core/contact`,
  `core/organization`, `core/person`, `core/address`, `core/vso` und späteren
  Profilen.

Diese Datei ist bewusst nur eine Grundlagenrecherche. Sie legt keine
Construct-X-T-Box, keine SHACL-Regeln und keine finalen lokalen IRIs fest.

Nicht ausgewertet wurden die vorhandenen Domain-Arbeitsstände als
Modellvorlage. Sie können später Anforderungen liefern, sind aber nicht die
Quelle für die Struktur des Document Core.

## 2. Quellenhierarchie

| Quellenart | Bedeutung für Construct-X | Beispiele |
| --- | --- | --- |
| Allgemeine Metadaten- und Web-Vokabulare | Grundlage für stabile Basisbegriffe | Dublin Core Terms, Schema.org, FOAF |
| Linked-Data-Standards für Verteilung, Versionierung und Provenienz | Grundlage für Abgrenzung und Alignment | DCAT 3, PROV-O, ADMS, SKOS |
| Geschäfts- und Verwaltungsaustauschformate | Vergleichsquelle für wiederkehrende Dokumentreferenz- und Attachment-Strukturen | OASIS UBL 2.5, SEMIC CCCEV/CPSV-AP |
| Vertrauens-, Signatur- und Credential-Standards | Quelle für Abgrenzung zu Nachweis- und Signaturmodellen | W3C VC, W3C Data Integrity, DID Core, eIDAS, ETSI ESI |
| Technische Register für Dateiformate | Grundlage für Medientypen | IANA Media Types |
| Rechte- und Policy-Modelle | Kandidaten für spätere Profile, nicht für den ersten Document Core | ODRL |

Eine Klasse oder Property wird nicht allein deshalb übernommen, weil sie in
einer Quelle vorkommt. Entscheidend ist, ob sie fachübergreifend stabil,
modular abgrenzbar und im Construct-X-Core wiederverwendbar ist.

## 3. Kurzfazit

Die tragfähigste Grundlage für den Document Core ist eine Kombination aus:

1. [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
   für allgemeine Metadaten wie Titel, Beschreibung, Datum, Sprache,
   Identifier, Relation, Quelle, Version und Gültigkeit.
2. [Schema.org CreativeWork, DigitalDocument und MediaObject](https://schema.org/DigitalDocument)
   als breite Web-Interoperabilitätsquelle für digitale Dokumente,
   Medienobjekte, Encodings, URLs, Lizenzen und Publikationsdaten.
3. [OASIS UBL 2.5](https://docs.oasis-open.org/ubl/)
   als Vergleichsquelle für `DocumentReference`, `Attachment`,
   `ExternalReference`, Issue-Date/Time, Version, UUID, Dokumenttyp und
   referenzierte Dokumente in Geschäftsvorgängen. UBL wird nicht als
   Abhängigkeit geplant; ein Mapping zu UBL ist aktuell nicht vorgesehen.
4. [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) für die Trennung zwischen
   abstraktem Inhalt und konkreter Distribution, Download-URL, Medientyp,
   Verpackung und Kompression.
5. [PROV-O](https://www.w3.org/TR/prov-o/) für Herkunft, Ableitung,
   Generierung und Verantwortlichkeit, aber eher als Alignment- oder spätere
   Provenienzschicht.
6. [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) und
   [SKOS](https://www.w3.org/TR/skos-reference/) für strukturierte Kennungen
   und kontrollierte Vokabulare.

Der erste Document Core sollte deshalb nicht als Dokumentenmanagementsystem
gebaut werden. Ein guter Kern beschreibt nur:

- ein dokumentartiges Informationsobjekt,
- eine kontextbezogene Dokumentreferenz,
- eine angehängte oder extern referenzierte Datei,
- allgemeine Metadaten,
- strukturierte Identifier über das bestehende ADMS-/SKOS-Muster,
- klare Erweiterungspunkte für Signatur, Rechte, Nachweise, Versionierung und
  Provenienz.

Signaturen, Credentials, Zugriffsrechte, Freigabeprozesse, Archivierung,
Aktenpläne und domänenspezifische Dokumenttypen sollten nicht in den ersten
Document Core gezogen werden.

## 4. Bewertete Quellen

| Quelle | Verwendeter Stand | Rolle in der Analyse | Vorläufige Nutzung |
| --- | --- | --- | --- |
| [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | DCMI Recommendation, aktuelle Spezifikation abgerufen 2026-08-27 | allgemeine Ressourcenmetadaten | primäre Quelle für Titel, Beschreibung, Datum, Identifier, Sprache, Relation, Quelle, Version und Gültigkeit |
| [Schema.org DigitalDocument](https://schema.org/DigitalDocument), [CreativeWork](https://schema.org/CreativeWork), [MediaObject](https://schema.org/MediaObject) | Entwicklungsversion, abgerufen 2026-08-27 | Web-Interoperabilität | Alignment- und Benennungsquelle, nicht als strenges Kernmodell übernehmen |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99, abgerufen 2026-08-27 | einfacher Dokumentbegriff im Web-of-Data-Kontext | mögliches Alignment für `foaf:Document`, fachlich aber zu schmal |
| [OASIS UBL 2.5](https://docs.oasis-open.org/ubl/) | OASIS Standard laut Ankündigung vom 26./27. August 2026; Detailberichte zusätzlich gegen CS01/CSD-Reports geprüft | Geschäftsdokumente, Dokumentreferenzen, Attachments | Vergleichsquelle; keine Abhängigkeit und aktuell kein geplantes Mapping |
| [UBL AttachedDocument Summary Report](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/mod/summary/reports/UBL-AttachedDocument-2.5.html) | CS01-Report, abgerufen 2026-08-27 | Detailstruktur für `Attachment`, `DocumentReference`, `ExternalReference` | Feldanalyse als Vergleich, nicht als verbindliche Vorgabe |
| [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | W3C Recommendation, 22. August 2024 | Kataloge, Ressourcen, Distributionen, Download-URL, Medientyp | Referenz für konkrete Dateien und technische Distributionen |
| [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) | SEMIC Recommendation, 2024-02-01 | Identifier, Assets, Versionierungsnavigation, Status | Wiederverwendung gemäß bestehendem Construct-X-Kennungsmodell |
| [SKOS Reference](https://www.w3.org/TR/skos-reference/) | W3C Recommendation, 2009 | kontrollierte Konzepte und Notationen | Grundlage für Dokumenttypen, Statuswerte und Kennungssysteme |
| [PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation, 2013 | Provenienz, Ableitung, Generierung, Verantwortlichkeit | nicht in den Kern kopieren; als spätere Provenienz- und Alignmentquelle nutzen |
| [SEMIC CCCEV](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/core-criterion-and-core-evidence-vocabulary) | Version 2.2.0, Release 2026 | Evidenz, Kriterien und Anforderungen | wichtig für Abgrenzung: Evidence ist nicht einfach Document |
| [CPSV-AP 3.2.0](https://semiceu.github.io/CPSV-AP/releases/3.2.0/) | SEMIC Recommendation, 2024 | Public Services, Evidence, related documentation | Anforderungsquelle für Nachweise und zugehörige Dokumentation |
| [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model/) | W3C Recommendation, 15. Mai 2025 | Credentials, Issuer, Subject, Validity, Status, Evidence | Abgrenzung zu prüfbaren Nachweisen; nicht als Document Core kopieren |
| [W3C Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) | W3C Recommendation, 15. Mai 2025 | kryptografische Proofs für VC und ähnliche Dokumente | spätere Signatur-/Proof-Schicht, nicht Kern |
| [W3C DID Core](https://www.w3.org/TR/did-core/) | W3C Recommendation, 2022 | kontrollierte Identifier-Dokumente und Verification Methods | nur relevant für Identität und Signaturbindung |
| [eIDAS Regulation 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) und Änderungen | EU-Rechtsrahmen | elektronische Signaturen, Siegel, Zeitstempel, elektronische Dokumente, Zustelldienste | Rechts- und Vertrauenskontext, nicht T-Box-Kern |
| [ETSI ESI](https://www.etsi.org/technical-groups/esi/) | laufend gepflegte Standards | technische Standards für Signaturen, Siegel und Trust Services | spätere Signatur-/Trust-Profile |
| [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) | W3C Recommendation, 2018 | Permissions, Prohibitions, Duties für Assets | spätere Rechte-/Policy-Schicht |
| [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | W3C Recommendation, 2017 | Annotationen, Body, Target, SpecificResource, Selector | spätere Teilreferenzen und Kommentare |
| [IANA Media Types](https://www.iana.org/assignments/media-types) | Registerstand 2026-08-24 | kanonische Medientypen | bevorzugte Quelle für `mediaType`-Werte |
| [OWL-Time](https://www.w3.org/TR/owl-time/) | W3C Candidate Recommendation Draft, 2022 | Intervalle, Zeitpunkte, Gültigkeitszeitraeume | nur verwenden, wenn ein echtes Zeitmodell nötig wird |

Projektintern sind für die spätere Modellierungsphase relevant:

- [Identifier-Modell](../../../../docs/architecture/identifier-model.md)
- [Namespace-Konzept](../../../../docs/architecture/construct-x-namespace-konzept.md)
- [Dependency-Regeln](../../../../docs/architecture/dependency-rules.md)
- [Versionierungsregeln](../../../../docs/architecture/versioning.md)
- [Agent-Spezifikation](../../agent/docs/agent-specification.md)
- [Participation-Modul](../../participation/docs/index.md), sofern im lokalen
  Arbeitsstand vorhanden

## 5. Grundbegriffe: Dokument, Werk, Datei, Referenz

### 5.1 Dokument als Informationsobjekt

Ein Core-Dokument sollte nicht mit einer bestimmten Datei verwechselt werden.
Viele Quellen unterscheiden direkt oder indirekt zwischen:

- dem intellektuellen oder fachlichen Inhalt,
- einer konkreten digitalen oder physischen Ausprägung,
- einer Referenz auf diesen Inhalt,
- einer Datei oder Distribution, die diesen Inhalt trägt.

Dublin Core ist hier bewusst allgemein und beschreibt Ressourcen mit
Metadaten. Schema.org unterscheidet `CreativeWork`, `DigitalDocument` und
`MediaObject`. DCAT trennt `Resource` beziehungsweise `Dataset` von
`Distribution`. ADMS trennt `Asset` und `AssetDistribution`.

Für Construct-X folgt daraus:

- `Document` ist als eigene Construct-X-Klasse umgesetzt.
- Eine Datei, ein Download oder ein eingebettetes Binary ist nicht automatisch
  dasselbe wie das fachliche Dokument.
- Eine `DocumentReference` beschreibt den Kontext, in dem eine Ressource auf ein
  Dokument verweist.
- Eine konkrete Datei oder technische Bereitstellung wird DCAT-nah als
  Distribution gedacht, nicht als blosser Anhang-Literalwert.

### 5.2 Dokumentreferenz als eigener Beziehungsknoten

UBL bestätigt sehr stark, dass Dokumentreferenzen in Geschäftsprozessen nicht
nur einfache Links sind. `DocumentReference` besitzt Felder für ID, UUID,
IssueDate, IssueTime, DocumentType, DocumentTypeCode, DocumentDescription,
VersionID, LanguageID, LocaleCode, ValidityPeriod, IssuerParty, Attachment und
XPath.

Das spricht für eine eigene Referenzressource, wenn im Kontext mehr als nur
eine URI ausgesagt werden muss. Eine einfache direkte Link-Property reicht
nicht, sobald Referenztyp, referenziertes Dokumentdatum, Sprache, Version,
Gültigkeit oder Anhang zusammengehalten werden müssen.

### 5.3 Attachment und ExternalReference

UBL `Attachment` kann ein eingebettetes Dokument oder eine externe Referenz
enthalten. `ExternalReference` besitzt unter anderem URI, FileName, FormatCode,
EncodingCode, CharacterSetCode, MimeCode, HashAlgorithmMethod, DocumentHash,
ExpiryDate und ExpiryTime.

DCAT behandelt technische Dateien als Distributionen mit `accessURL`,
`downloadURL`, `mediaType`, `format`, `compressFormat`, `packageFormat`,
`byteSize` und weiteren technischen Bereitstellungsangaben.

Für Construct-X bedeutet das:

- Eine konkrete Datei oder technische Ausprägung soll DCAT-nah modelliert
  werden.
- Eine externe Datei braucht mindestens einen URI- beziehungsweise
  Distribution-Erweiterungspunkt.
- Medientypen sollten an IANA ausgerichtet werden.

## 6. Metadatenanalyse

### 6.1 Titel und Beschreibung

Dublin Core `title` und `description` sind die naheliegenden allgemeinen
Metadaten. Schema.org nutzt `name`, `headline`, `abstract` und `description`,
ist aber deutlich breiter und web-orientierter.

Umgesetzte Entscheidung:

- Titel und Beschreibung sollten sprachfähige Literale zulassen.
- Ein fachlicher Pflichttitel gehört eher in Profile als in die allgemeine
  T-Box.
- Wenn ein externes Vokabular direkt reicht, sollte ein Alignment oder sogar
  direkte Wiederverwendung geprüft werden, statt lokale Kopien zu erzwingen.

### 6.2 Datum, Ausgabezeit und Gültigkeit

Dublin Core bietet `date`, `created`, `issued`, `modified`, `valid` und weitere
Spezialisierungen. UBL trennt `IssueDate`, `IssueTime` und `ValidityPeriod`.
Schema.org trennt `dateCreated`, `dateModified`, `datePublished`, `expires`.
VC verwendet `validFrom` und `validUntil`.

Für Construct-X sollte die erste Entscheidung nicht lauten "ein allgemeines
documentDate reicht immer". Es gibt mindestens diese unterschiedlichen Aussagen:

| Aussage | Bedeutung | Wahrscheinliche Quelle |
| --- | --- | --- |
| Erstellungsdatum | wann das Dokument erzeugt wurde | DCT, Schema.org, PROV |
| Ausgabedatum | wann es fachlich ausgestellt wurde | UBL, DCT `issued`, VC `validFrom` |
| Änderungsdatum | wann der Inhalt zuletzt geändert wurde | DCT, Schema.org |
| Veröffentlichungsdatum | wann es publiziert wurde | Schema.org, DCT |
| Gültigkeit | Zeitraum, in dem das Dokument oder der Nachweis gilt | DCT `valid`, UBL `ValidityPeriod`, VC |
| Ablauf/Verfügbarkeit | wann ein Link oder Inhalt nicht mehr verlässlich ist | UBL `ExpiryDate`, Schema.org `expires` |

Empfehlung:

- Im Document Core sind die wichtigen Datumsbegriffe optional umgesetzt:
  erstellt, ausgegeben, geändert und gültig.
- Die lokalen Datumsproperties sind nachvollziehbar auf DCT beziehungsweise
  Schema.org ausgerichtet.
- Gültigkeitsgrenzen verwenden `xsd:date` oder `xsd:dateTime` und keine
  beliebigen flachen Strings.
- Issue-Date/Time kann für viele Geschäftsdokumente wichtig sein, muss aber
  fachlich gegen DCT `issued` abgegrenzt werden.

### 6.3 Sprache und Locale

Dublin Core `language`, Schema.org `inLanguage` und UBL `LanguageID`/
`LocaleCode` zeigen denselben Bedarf. Sprache ist bei Dokumenten zentral,
insbesondere bei mehrsprachigen Dokumenten und parallelen Fassungen.

Empfehlung:

- Sprache sollte im Kern möglich sein.
- BCP-47-Sprachcodes beziehungsweise ein kontrolliertes Sprachvokabular sollten
  in Profilen entschieden werden.
- Locale und Sprache nicht vermischen: Sprache beschreibt den Inhalt, Locale
  beschreibt eine regionale Sprach-/Darstellungsvariante.

### 6.4 Dokumenttyp und Status

Dublin Core `type`, Schema.org `creativeWorkStatus`, ADMS `status`, UBL
`DocumentTypeCode` und `DocumentStatusCode` zeigen, dass Typ und Status
wiederkehrende Bedarfe sind.

Kritisch ist aber:

- "Rechnung", "Lieferschein", "Vertrag" und "Prüfbericht" sind fachliche
  Dokumentarten und nicht automatisch Core-Klassen.
- Statuswerte wie `draft`, `issued`, `cancelled`, `obsolete`, `superseded`,
  `accepted` oder `rejected` sind oft workflow- oder domainabhängig.
- ADMS `status` beschreibt den Status in einem bestimmten Workflowkontext und
  sollte nicht pauschal als allgemeiner Rechtsstatus interpretiert werden.

Empfehlung:

- Ein kleines Dokumenttyp-Vokabular ist für den MVP umgesetzt.
- Dokumenttypen werden als kontrollierte Konzepte bewertet, nicht als harte
  Unterklassen des Document Core.
- Ein kleines Dokumentstatus-Vokabular ist für den MVP umgesetzt.
- Der Status beschreibt den Zustand eines Dokuments, zum Beispiel Entwurf,
  ausgegeben, ersetzt, widerrufen oder abgelaufen.
- Keine Workflow-Zustände wie "in Prüfung", "wartet auf Freigabe" oder
  "zugewiesen an Rechtsabteilung" in den Document Core aufnehmen.
- Keine domänenspezifische Positivliste im Core.

### 6.5 Version, Revision, Ableitung und Ersatz

Dublin Core bietet `hasVersion`, `isVersionOf`, `replaces`, `isReplacedBy` und
`source`. ADMS bietet `prev`, `next`, `last` und `versionNotes`. DCAT 3
ergänzt Versionierungsbeziehungen. PROV-O modelliert Ableitung und Revisionen
über `wasDerivedFrom` und qualifizierte Beziehungen.

Für Construct-X ist wichtig:

- Dokumentversionen sind nicht dasselbe wie Ontologieversionen.
- Eine Datei in anderem Format ist nicht zwingend eine neue fachliche Version.
- Eine korrigierte oder ersetzende Fassung sollte nicht nur über Dateiname
  abgeleitet werden.
- Für beweisrelevante Dokumente kann eine exakte Version entscheidend sein.

Empfehlung:

- Ein einfacher Versionshinweis kann als Metadatum starten.
- Strukturelle Versionierungsbeziehungen sollten bevorzugt bestehende DCT,
  ADMS, DCAT oder PROV-Beziehungen nutzen.
- Vor einer lokalen Versionierungslogik muss geklärt werden, ob sie für
  Dokumente anders ist als für andere Ressourcen im Netzwerk.

## 7. Identifier und Nummern

Dublin Core `identifier`, ADMS `Identifier`, SKOS `notation` und UBL `ID`/`UUID`
zeigen, dass Dokumente häufig mehrere Kennungen besitzen:

- fachliche Dokumentnummer,
- UUID,
- externe Register- oder Archivkennung,
- DOI, URN, ISBN oder ähnliche Publikationskennung,
- systeminterne ID.

Das bestehende Construct-X-Kennungsmodell ist hier massgeblich:

```text
Ressource
  adms:identifier
    adms:Identifier
      skos:notation "Wert"^^kennungssystem
      adms:schemaAgency "Herausgeber des Kennungssystems"
```

Empfehlung:

1. Keine lokalen Properties wie `invoiceNumber`, `documentNumber`,
   `uuidValue`, `doi` oder `archiveId` im Document Core einführen.
2. Dokumentkennungen über ADMS modellieren.
3. Kennungssysteme in einem Referenzvokabular führen, falls sie
   konstruktionsweit wiederverwendet werden.
4. Technische Integritätsprüfung wird nicht über das Document-Core-
   Kennungsmodell eingeführt.

## 8. Akteure: Creator, Issuer, Publisher, Sender, Receiver

Die Quellen verwenden viele Akteursbegriffe:

- Dublin Core: `creator`, `contributor`, `publisher`, `rightsHolder`.
- Schema.org: `author`, `creator`, `editor`, `publisher`, `provider`,
  `accountablePerson`, `copyrightHolder`.
- UBL: `IssuerParty`, `SenderParty`, `ReceiverParty`.
- VC: `issuer`, `holder`, `verifier`, `credentialSubject`.
- PROV-O: `wasAttributedTo`, `wasGeneratedBy`, `wasAssociatedWith`.

Diese Begriffe sind nicht deckungsgleich. Ein Autor ist nicht automatisch der
Aussteller, der Sender, der Herausgeber, der rechtlich Verantwortliche oder der
technische Uploader.

Für Construct-X folgt daraus:

- Akteursrollen an Dokumenten gehören sehr wahrscheinlich über
  `core/participation` modelliert.
- Das Document Core sollte nicht eigene Personen- oder Organisationsproperties
  für jeden möglichen Akteurstyp einführen.
- Ein späteres Profil kann verpflichten, dass ein bestimmter Dokumenttyp genau
  einen Aussteller oder Sender besitzt.
- Provenienzrollen sollten gegen PROV-O abgeglichen werden, wenn der Fokus auf
  Erzeugung, Ableitung oder Verarbeitung liegt.

Entscheidung für die nächste Modellierungsphase:

- Aussteller, Sender, Empfänger, Autor und Publisher werden nicht als eigene
  direkte Document-Core-Properties vorgesehen.
- Diese Rollen werden über das Participation-Muster modelliert: ein Agent
  spielt eine kontrollierte Rolle im Kontext eines Dokuments oder einer
  Dokumentreferenz.
- PROV-O bleibt für echte Provenienzfälle zuständig, also für Erzeugung,
  Ableitung, Revision oder Verarbeitung.

Beispiele:

```text
Rechnung 4711
  Participation: Organisation A als issuer
  Participation: Organisation B als recipient
```

```text
Tragwerksplan Version 3
  Participation: Person X als author
  Participation: Organisation Y als publisher
  Participation: Organisation Z als recipient
```

```text
Baugenehmigung
  Participation: Behörde A als issuer
  Participation: Antragsteller B als recipient
```

```text
PDF-Datei wurde aus Datensatz Y erzeugt
  PROV-O-Profil: Dokument wasGeneratedBy Exportlauf X
  PROV-O-Profil: Dokument wasDerivedFrom Datensatz Y
```

## 9. Evidence, Credentials und Nachweise

SEMIC CCCEV beschreibt Evidence als Nachweis dafür, dass eine Requirement
erfüllt ist. CPSV-AP verwendet Evidence im Kontext öffentlicher Services und
unterscheidet Evidence von related documentation.

W3C Verifiable Credentials modelliert prüfbare Claims mit Issuer,
Credential Subject, Gültigkeit, Status, Schema und optionaler Evidence. W3C
Data Integrity beschreibt kryptografische Proofs für solche und ähnliche
Dokumente.

Wichtig für die Modulgrenze:

- Nicht jedes Dokument ist Evidence.
- Nicht jede Evidence ist ein Dokument; sie kann auch ein Datensatz, ein
  Registereintrag, ein Artefakt oder eine strukturierte Antwort sein.
- Ein Credential ist nicht einfach ein Anhang, sondern eine signierbare und
  prüfbare Behauptungsstruktur.
- Ein Identitätsnachweis braucht Subjekt, Aussteller, Gültigkeit, Status und
  Vertrauensentscheidung.

Empfehlung:

- Der Document Core darf Dokumente referenzieren, die als Nachweis genutzt
  werden.
- Die Semantik "belegt Requirement X" gehört nicht in den allgemeinen
  Document Core, sondern in ein Evidence-/Requirement-Profil oder ein späteres
  spezialisiertes Modul.
- `core/person` und `core/organization` sollten Nachweise nicht als
  Dokumentfelder duplizieren, sondern auf externe Nachweisressourcen verweisen.

## 10. Signaturen, Siegel und Integritätsnachweise

eIDAS regelt unter anderem elektronische Signaturen, elektronische Siegel,
elektronische Zeitstempel, elektronische Dokumente, elektronische
Zustelldienste und Website-Zertifikate. ETSI ESI liefert dazu technische
Standards und Profile.

W3C Data Integrity beschreibt Proofs für verifizierbare Daten. DID Core
beschreibt Verification Methods und kontrollierte Identifier-Dokumente.

Für Construct-X ist die zentrale Abgrenzung:

- Eine digitale Signatur zeigt Kontrolle über einen Schlüssel und Integrität
  bezogen auf den signierten Inhalt.
- Ein qualifiziertes Siegel oder eine qualifizierte Signatur besitzt
  rechtsraumspezifische Bedeutung und braucht Trust-List-/Zertifikatskontext.
- Ein einfacher Link auf eine signierte PDF-Datei ist kein vollständiges
  Signaturmodell.

Empfehlung:

- Signatur-, Siegel-, Zeitstempel- und Trust-List-Details nicht in den ersten
  Document Core aufnehmen.
- Einen neutralen Erweiterungspunkt für Signatur-/Proof-Ressourcen erst dann
  einführen, wenn der konkrete Vertrauensscope geklärt ist.

## 11. Rechte, Lizenzen und Zugriff

Dublin Core und Schema.org bieten einfache Lizenz- und Rechtehinweise. ODRL ist
das deutlich stärkere Modell für maschinenlesbare Policies mit Permissions,
Prohibitions, Duties, Assets, Parties und Constraints.

Für Construct-X:

- Eine Lizenz-URI kann ein allgemeines Metadatum sein.
- Zugriffskontrolle, Vertraulichkeit, Weitergaberechte und
  Nutzungsbedingungen sind nicht nur Dokumentmetadaten, sondern Policy-Fragen.
- ODRL ist ein guter Kandidat für spätere Profile, aber für den ersten
  Document Core zu umfangreich.

Empfehlung:

- Keine eigene Rechte-/Policy-Ontologie im Document Core.
- Lizenzhinweise nur aufnehmen, wenn sie fachübergreifend im MVP gebraucht
  werden.
- Zugriffsrechte nicht als einfache Booleans an Dokumente hängen.

## 12. Teilreferenzen, XPath, Annotationen und Dokumentausschnitte

UBL `DocumentReference` kennt `XPath` als Ort innerhalb eines referenzierten
Dokuments. Das Web Annotation Data Model modelliert Bodies, Targets,
SpecificResources, Selector und States. Damit können Kommentare oder
Referenzen auf konkrete Bereiche eines Dokuments beschrieben werden.

Für Construct-X:

- Ein Dokumentausschnitt ist nicht dasselbe wie ein Dokument.
- Ein XPath, Seitenbereich, Bytebereich oder Fragment-Identifier ist
  formatabhängig.
- Annotationen können eigenständige Ressourcen mit Motivation, Body und Target
  sein.

Empfehlung:

- Keine eigene Ausschnitts- oder Annotationstiefe im ersten Document Core.
- Für einfache Quellen-/Mappingpfade können AnnotationProperties in
  Domain-Modulen reichen.
- Wenn fachlich erforderlich, später Web Annotation als Alignmentquelle nutzen.

## 13. Dateiformate und Medientypen

IANA ist die massgebliche Quelle für Media Types. DCAT empfiehlt
`dcat:mediaType`, wenn der Typ in IANA definiert ist, und `dcterms:format` für
allgemeinere Formatangaben.

Empfehlung:

1. Medientypen nicht als freie unkontrollierte Semantik interpretieren.
2. Wenn nur eine Angabe gebraucht wird, kann ein Literal mit IANA-Wert für den
   MVP genügen.

## 14. Vorläufige Modulgrenzen

| Bereich | Gehört in `core/document` | Gehört nicht in `core/document` |
| --- | --- | --- |
| Dokumentkern | allgemeines Dokument beziehungsweise dokumentartiges Informationsobjekt | Rechnungs-, Lieferschein-, Vertrags- oder Zertifikatsemantik |
| Referenz | kontextbezogene Dokumentreferenz | domänenspezifische Pflichtreferenzen |
| Distribution | konkrete Datei oder technische Bereitstellung | vollständiges Storage-, DMS- oder Archivmodell |
| Metadaten | Titel, Beschreibung, Sprache, Erstellungs-/Ausstellungs-/Änderungs-/Gültigkeitshinweise als Kandidaten | Workflowstatus ohne Profilkontext |
| Identifikator | Wiederverwendung von ADMS/SKOS | lokale Nummernproperties pro Dokumentart |
| Akteure | Verweis auf Agent-/Participation-Muster | eigene Properties für jeden Akteursrollenbegriff |
| Nachweise | Dokument kann Nachweisressource sein oder referenziert werden | Evidence-/Requirement-/Credential-Semantik |
| Signatur | möglicher Erweiterungspunkt | eIDAS-/ETSI-/Data-Integrity-Modell im Kern |
| Rechte | mögliche Lizenzreferenz | ODRL-Policy oder Zugriffskontrolle im Kern |
| Formate | Media-Type-/Distribution-Anschluss | eigene Liste aller Dateiformate |

## 15. Begriffskern als umgesetztes Analyseergebnis

Die folgende Liste zeigt, wie das Rechercheergebnis in Version `0.1.0`
umgesetzt wurde.

### 15.1 Implementierte Klassen

| Begriff | Bedeutung | Begründung |
| --- | --- | --- |
| `Document` | eigene Construct-X-Klasse für ein dokumentartiges Informationsobjekt | DCT, Schema.org, FOAF und UBL dienen nur als Alignment- und Vergleichsquellen |
| `DocumentReference` | Kontextressource, die auf ein Dokument oder eine externe Dokumentressource verweist | UBL zeigt, dass Referenzen eigene Metadaten tragen können |
| `DocumentDistribution` | konkrete Datei, Download- oder Bereitstellungsausprägung eines Dokuments | DCAT-nahe Trennung zwischen Dokumentinhalt und technischer Distribution |
| `DocumentType` | kontrollierter Dokumenttyp | kleines MVP-Vokabular umgesetzt |
| `DocumentStatus` | kontrollierter Zustand eines Dokuments | kleines MVP-Vokabular umgesetzt |

Optional später:

- fach- oder domainbezogene Dokumenttyp-Erweiterungen,
- fach- oder domainbezogene Status-Erweiterungen,
- Provenienz-, Signatur-, Credential- oder Rechteprofile.

### 15.2 Implementierte Beziehungen

| Begriff | Bedeutung | Hinweise |
| --- | --- | --- |
| `hasDocumentReference` | verbindet beliebige Kontextressource mit Dokumentreferenz | sollte keine harte RDFS-Domain besitzen |
| `referencesDocument` | verbindet Dokumentreferenz mit beschriebenem Dokument | nur wenn Ziel im Graph modelliert ist |
| `hasDistribution` | verbindet Dokument oder Dokumentreferenz mit einer konkreten Distribution | DCAT-nahe Trennung |
| `dcterms:references`, `dcat:accessURL`, `dcat:downloadURL` | verweist auf externe Dokumentressource oder technische Bereitstellung | direkte Wiederverwendung etablierter Properties |
| `documentType` | verweist auf kontrollierten Dokumenttyp | eher SKOS-Konzept als Klasse |
| `documentStatus` | verweist auf kontrollierten Statuswert | Core stellt kleine Wertemenge bereit, Profile können erweitern |

### 15.3 Implementierte Metadaten

| Kandidat | Bedeutung | Quelle |
| --- | --- | --- |
| Titel | Anzeigename oder fachlicher Dokumenttitel | DCT `title`, Schema.org `name` |
| Beschreibung | Freitextbeschreibung | DCT `description`, UBL `DocumentDescription` |
| Sprache | Sprache des Inhalts | DCT `language`, Schema.org `inLanguage`, UBL `LanguageID` |
| Ausgabedatum | fachliche Ausstellung | DCT `issued`, UBL `IssueDate` |
| Ausgabezeit | fachliche Ausstellungszeit | UBL `IssueTime` |
| Änderungsdatum | letzte bekannte Änderung | DCT `modified`, Schema.org `dateModified` |
| Version | Dokumentversion oder Ausgabebezeichnung | UBL `VersionID`, DCAT/ADMS/DCT |
| Gültigkeit | Zeitraum, in dem Dokument oder Nachweis gilt | DCT `valid`, UBL `ValidityPeriod`, VC |
| Dateiname | Name einer konkreten Datei | UBL `FileName` |
| Medientyp | technisches Format | IANA, DCAT, Schema.org |

## 16. Nicht in den ersten Document Core

Folgende Themen sollten trotz Quellenlage nicht direkt in den ersten Core:

- Signatur- und Siegelklassen,
- elektronische Zeitstempel,
- Trust-List- und Zertifikatsvalidierung,
- Credential-, Evidence- und Requirement-Modell,
- Archivierung, Aktenpläne, Retention und Records Management,
- Zugriffskontrolle, Rollenrechte und Policy-Auswertung,
- Rechnungs-, Lieferschein-, Vertrags-, Zertifikats- und Berichtsklassen,
- Workflowstatus und Freigaben,
- Volltextinhalt, OCR, Extraktion und Seiten-/Abschnittsmodell,
- Dateispeicherorte, Uploads, Repository- oder DMS-spezifische Konzepte,
- Format-spezifische Strukturen wie PDF-Seiten, XML-XPath oder IFC-Referenzen.

## 17. Profil- und Validierungsfolgen

Pflichtfelder sollten nicht in der allgemeinen T-Box versteckt werden. Für den
Document-Bereich zeichnen sich eher mehrere Ebenen ab:

1. **Document Core:** sehr allgemeine Struktur und Datentypkonsistenz.
2. **Document Reference Core Shapes:** prüfen, dass eine Dokumentreferenz
   mindestens auf ein beschriebenes Dokument oder eine externe Ressource zeigt.
3. **Distribution Shapes:** prüfen, dass Datei-/URI-/Format-Angaben
   konsistent sind.
4. **Dokumenttyp-Profile:** Rechnung, Lieferschein, Vertrag, Zertifikat,
   Prüfbericht usw. legen eigene Pflichtangaben fest.
5. **Participation-Profile:** Aussteller, Sender, Empfänger, Autor,
   Publisher und ähnliche Rollen können je Dokumenttyp verpflichtend werden.
6. **Trust-/Evidence-Profile:** Signatur, Credential, Nachweisstatus und
   externe Prüfung.

Die allgemeine Ontologie sollte deshalb möglichst keine fachlichen
Kardinalitäten wie "jedes Dokument hat genau einen Aussteller" oder "jedes
Dokument besitzt genau eine Datei" behaupten.

## 18. Konsolidierter und umgesetzter Entscheidungsstand

Diese Punkte bilden die Grundlage der implementierten T-Box und Core Shapes:

1. Der Document Core braucht einen eigenen schmalen Kern, aber kein grosses
   Dokumentenmanagementmodell.
2. Dokument, Dokumentreferenz und Distribution sind getrennt modelliert.
3. Eine Dokumentreferenz ist eine eigene Ressource, weil sie
   kontextbezogene Metadaten tragen kann.
4. Fachliche Dokumentarten gehören nicht als Klassen in den Core.
5. Dokumenttypen und Statuswerte sind als kleine kontrollierte
   MVP-Vokabulare umgesetzt und können später profiliert werden.
6. Identifier folgen dem gemeinsamen ADMS-/SKOS-Vertrag aus `core/identifier`.
7. Akteursrollen wie Aussteller, Sender, Empfänger, Autor, Publisher oder
   Rechteinhaber dürfen nicht vermischt werden.
8. Akteursbeziehungen werden über `core/participation` modelliert; PROV-O ist
   für Erzeugung, Ableitung, Revision und Verarbeitung relevant.
9. Distributionen besitzen Anschlüsse für URI, Dateiname und Medientyp, aber
   kein Storage-Modell.
10. IANA ist die bevorzugte Quelle für Medientypen.
11. Gültigkeit, Ablauf und Verfügbarkeit sind unterschiedliche Aussagen.
12. Evidence und Credential sind nicht mit Document gleichzusetzen.
13. Signaturen, Siegel und eIDAS-/ETSI-Vertrauen gehören nicht in den ersten
    Document Core.
14. Rechte und Zugriffskontrolle gehören nicht in den ersten Document Core;
    ODRL bleibt späteres Profil- oder Alignmentthema.
15. Teilreferenzen und Annotationen bleiben ausserhalb des MVP.

## 19. Umgesetzte Modellentscheidungen

T-Box und Core Shapes setzen folgende fachliche Leitplanken um:

1. Construct-X führt eine eigene Klasse `Document` ein. Externe Klassen wie
   `schema:DigitalDocument` oder `foaf:Document` sind Alignmentziele, aber
   nicht der lokale Kernbegriff.
2. Dateien und technische Bereitstellungen werden DCAT-nah als Distribution
   getrennt. `Attachment` bleibt nur UBL-Vergleichsbegriff.
3. Die wichtigsten Datumsbegriffe sind optional umgesetzt: erstellt,
   ausgegeben, geändert und gültig.
4. Ein kleines Dokumenttyp-Vokabular ist für den MVP umgesetzt.
5. Ein kleines Dokumentstatus-Vokabular ist für den MVP umgesetzt. Gemeint
   sind dokumentbezogene Zustände wie Entwurf, ausgegeben, ersetzt,
   widerrufen oder abgelaufen, nicht Workflowzustände.
6. Aussteller, Sender, Empfänger, Autor und Publisher werden über
   `core/participation` modelliert.
7. PROV-O wird nur für echte Provenienzfälle genutzt: Erzeugung, Ableitung,
   Revision oder Verarbeitung eines Dokuments.
8. UBL wird nur als Vergleichsquelle genutzt. Es ist aktuell weder eine
   Abhängigkeit noch ein Mapping zu UBL geplant.

## 20. Gesamtbewertung

Ein belastbarer `core/document`-Baustein sollte nicht aus einer langen Liste
möglicher Dokumentattribute entstehen. Die Quellen zeigen vielmehr mehrere
sauber getrennte Ebenen:

```text
fachlicher Kontext
  -> Dokumentreferenz
       -> Dokument oder externe Ressource
       -> Distribution / Datei
       -> Metadaten, Identifier, Typ, Status, Sprache, Version
```

Darüber liegen weitere, getrennte Schichten:

- Beteiligte Akteure und Rollen,
- Provenienz und Ableitung,
- Nachweise und Credentials,
- Signaturen und Trust Services,
- Rechte und Zugriffspolitik,
- domänenspezifische Dokumentarten und Profile.

Die wichtigste Architekturentscheidung für die nächste Phase lautet daher:

> Document Core beschreibt dokumentartige Ressourcen und Referenzen, aber nicht
> die fachliche Bedeutung, rechtliche Beweiskraft, Signaturgültigkeit oder
> Prozessrolle eines Dokuments.

Damit bleibt das Modul klein genug für den Core und anschlussfähig für
spätere Profile.

## 21. Verständliches Übertragungsbeispiel

> DCAT liefert das Muster für technische Distributionen, DCTERMS allgemeine
> Metadaten und UBL fachliche Referenzsituationen. Construct-X verbindet diese
> Beiträge, ohne eines der Quellmodelle vollständig zu kopieren.
