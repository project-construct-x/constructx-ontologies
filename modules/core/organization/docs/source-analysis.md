# Quellenanalyse für die Organisationsontologie

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 27. August 2026  
**Geltungsbereich:** `core/organization`  
**Gegenstand:** Organisationen, rechtlich registrierte Einheiten und organisationsbezogene Selbstbeschreibungen

## 1. Ziel und Methode

Diese Analyse bewertet bestehende Ontologien, Austauschformate, Registermodelle
und Projektanforderungen als fachliche Grundlage des implementierten
Construct-X-Moduls `core/organization`. Sie beantwortet insbesondere:

- welche Organisationsarten fachlich unterschieden werden müssen,
- welche Angaben echte Organisationsstammdaten sind,
- welche Angaben nur in einem Prozess, einer Rolle oder Geschäftsbeziehung gelten,
- welche Identifikatoren strukturiert und nach ihrem Schema unterschieden werden müssen,
- welche Aussagen als zeitgebundener Nachweis oder Credential statt als einfache
  Property modelliert werden sollten,
- welche vorhandenen Construct-X-Module wiederzuverwenden sind,
- welche Quellen als konzeptionelle Grundlage, Alignment-Ziel, Mappingquelle oder
  lediglich als Anforderungsindikator geeignet sind.

Die Quellen werden nicht gleich gewichtet. Eine Klasse oder Kardinalität wird
nicht allein deshalb übernommen, weil sie in einem einzelnen Austauschformat
oder Gaia-X-Profil vorkommt.

## 2. Quellenhierarchie

| Quellenart | Bedeutung für Construct-X | Beispiele |
| --- | --- | --- |
| Normatives oder breit wiederverwendbares Begriffsmodell | Grundlage für Klassen, Beziehungen und Begriffsabgrenzungen | W3C Organization Ontology, SEMIC Core Business Vocabulary, bestehende Construct-X-Architektur |
| Amtliches Register-, Code- oder Prüfmodell | Grundlage für Kennungsschemata, kontrollierte Werte und Prüfverfahren | BRIS/EUID, VIES, GLEIF/LEI, ISO 20275, NACE, BZSt, EORI |
| Branchen- oder Austauschformat | Quelle für benötigte Felder und Mappings, nicht automatisch für die Ontologiestruktur | UBL, GS1, eForms |
| Breites Web- oder Alignment-Vokabular | Quelle für etablierte Begriffe und Interoperabilität | Schema.org, FOAF, GoodRelations |
| Spezialmodell | Analyse- und späteres Alignment-Ziel bei entsprechendem Use Case | FIBO, W3C VC, DID Core |
| Projektinterner Anforderungsindikator | Liefert mögliche Attribute und Prozesse, besitzt aber keine normative Modellautorität | Tabelle zur Selbstbeschreibung, 1Lieferscheinformat, derzeitige Delivery-Note-Ontologie |

### 2.1 Verbindlicher Umgang mit 1Lieferschein

Die im Repository vorhandene Delivery-Note-Ontologie und das zugehörige
Konzeptmodell sind **Work in Progress und keine Source of Truth für
`core/organization`**. Insbesondere dürfen bestehende Klassen wie `Buyer`,
`Seller`, `Shipper`, `Carrier` oder `Party` nicht in die Organisationsontologie
kopiert werden.

Das 1Lieferscheinformat wird ausschließlich informativ ausgewertet:

- Welche Akteure müssen in Lieferprozessen referenziert werden?
- Welche Organisations-, Standort-, Kontakt- und Kennungsdaten werden im
  Datenaustausch tatsächlich benötigt?
- Welche kontextuellen Kennungen treten zwischen Geschäftspartnern auf?

Die Antwort auf diese Fragen ist ein Anforderungshinweis, keine Übernahme der
gegenwärtigen Delivery-Note-Modellierung.

## 3. Kurzfazit

Als begriffliche Hauptgrundlagen eignen sich zwei komplementäre Quellen:

1. Die [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) bildet
   allgemeine Organisationen, formale Organisationen, Organisationseinheiten,
   Hierarchien, Mitgliedschaften, Rollen, Stellen und Standorte ab.
2. Das [SEMIC Core Business Vocabulary 2.3.0](https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/)
   bildet registrierte rechtliche Einheiten mit rechtlichem Namen, Rechtsform,
   rechtlicher Kennung, Tätigkeit, Registrierungsdatum und registrierter Adresse
   ab. Es ist mit dem im Projekt bereits festgelegten ADMS-Kennungsmodell
   kompatibel.

Die von der Nutzerseite ergänzte
[Gaia-X-Klasse `LegalPerson`](https://docs.gaia-x.eu/ontology/development/classes/LegalPerson/)
ist ein wichtiges Alignment- und Selbstbeschreibungsprofil. Sie ist jedoch kein
hinreichendes allgemeines Organisationsmodell: Ihre Pflichtangaben und
Kardinalitäten sind Gaia-X-spezifisch, ihr `name` ist sogar optional, und sie
fasst sehr unterschiedliche Kennungen unter `registrationNumber` zusammen.

Für Construct-X zeichnet sich deshalb folgende fachliche Schichtung ab:

- `Organization` für einen organisierten kollektiven Akteur,
- `LegalEntity` für rechtlich registrierte, geschäftsfähige Einheiten,
- `OrganizationalUnit` für Einheiten, die nur innerhalb einer Organisation
  sinnvoll identifiziert sind,
- Rollen- oder Beteiligungszuordnungen für Verkäufer, Käufer, Transporteur,
  Hersteller und ähnliche Prozessrollen,
- externe Nachweisressourcen für Compliance, Befähigungen, Versicherungen und
  zeitabhängige Statusaussagen, sobald dafür ein konkreter Use Case besteht.

`org:FormalOrganization` bleibt ein externes Alignment-Ziel und wird nicht als
lokale Construct-X-Klasse eingeführt.

Der lokale Begriff `LegalEntity` ist gegenüber `LegalPerson` vorzuziehen. Er
vermeidet eine Verwechslung mit natürlichen Personen im Modul `core/person` und
kann dennoch zu `legal:LegalEntity` und `gx:LegalPerson` ausgerichtet werden.

## 4. Bewertete Quellen

| Quelle | Verwendeter Stand | Rolle | Vorläufige Nutzung |
| --- | --- | --- | --- |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 2014 | Allgemeine Organisationsstruktur | Primäre Referenz für Organisation, Einheit, Hierarchie, Mitgliedschaft, Rolle, Stelle und Standort |
| [SEMIC Core Business Vocabulary](https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/) | 2.3.0, SEMIC Recommendation vom 12. Mai 2026 | Registrierte rechtliche Einheiten | Primäre Referenz für Legal Entity, Rechtsname, Rechtsform, Registrierung und ADMS-Kennungen |
| [Gaia-X LegalPerson](https://docs.gaia-x.eu/ontology/development/classes/LegalPerson/) | Entwicklungsversion, abgerufen 2026-08-27 | Gaia-X-Selbstbeschreibung | Alignment- und Profilquelle, nicht unverändert übernehmen |
| [Schema.org Organization](https://schema.org/Organization) | Entwicklungsversion, abgerufen 2026-08-27 | Web-Interoperabilität | Benennungs-, Feld- und Alignmentquelle |
| [OASIS UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) | 2.5 CS01 | Geschäfts- und Dokumentenaustausch | Feldanalyse und Mappingquelle für `Party`, `PartyLegalEntity`, Register und Finanzkonten |
| [GS1 Web Vocabulary: Organization](https://ref.gs1.org/voc/Organization) | laufend gepflegt, abgerufen 2026-08-27 | Lieferketten und GS1-Identifikation | Referenz für GLN, Organisationsnamen und Supply-Chain-Interoperabilität |
| [GS1 GLN Data Model](https://www.gs1.org/standards/gln-data-model-solution-standard/current-standard) | aktueller Standard | Rechtliche Einheit, Funktion und Standort | Typisierte Verwendung von GLNs, nicht jede GLN als Legal-Entity-ID interpretieren |
| [GLEIF LEI Model in RDF](https://www.gleif.org/en/lei-data/semantic-representation-of-the-lei/lei-model-in-rdf-resource-description-framework) | laufend gepflegt | Rechtliche Einheiten, LEI und Eigentumsbeziehungen | Referenz und mögliches Alignment für LEI-Daten |
| [GLEIF ISO 20275 ELF Code List](https://www.gleif.org/about-lei/code-lists/iso-20275-entity-legal-forms-code-list) | Version Februar 2026 | Rechtsformen nach Jurisdiktion | Bevorzugtes kontrolliertes Vokabular für Rechtsformen |
| [EU eProcurement Ontology](https://docs.ted.europa.eu/EPO/latest/conceptual.html) | 5.2, abgerufen 2026-08-27 | Beschaffungsrollen und Akteure | Referenz für kontextuelle Agentenrollen |
| [EU eForms Parties](https://docs.ted.europa.eu/eforms/latest/schema/parties.html) | aktueller Stand | Organisationen und rollenspezifische Touchpoints | Bestätigung der Trennung von Organisation, Rolle und Kontaktpunkt |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99 | Minimales Agentenmodell | Alignment über `core/agent`, nicht als Organisationskern ausreichend |
| [GoodRelations](https://www.heppnetz.de/ontologies/goodrelations/v1.html) | 1.0 | E-Commerce-Unternehmen und Kennungen | Historische Alignmentquelle, heute weitgehend von Schema.org überlappt |
| [FIBO](https://spec.edmcouncil.org/fibo/index.html) | aktueller veröffentlichter Stand | Finanz-, Eigentums- und Kontrollstrukturen | Spätere Spezialreferenz; für den MVP zu umfangreich |
| [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) | 2.0 | Strukturierte Kennungen | Gemäß Construct-X-Identifier-Architektur wiederverwenden |
| [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/) | 2.0 Recommendation | Herausgeber, Subjekt, Gültigkeit, Status und Evidenz | Grundlage für externe Nachweise, nicht für Organisationsstammdaten |
| [W3C DID Core](https://www.w3.org/TR/did-core/) | 1.0 Recommendation | Dezentrale Identifikatoren und Kontrolle | DID als technischer Identifikator; kein Beweis rechtlicher Existenz |
| [NACE Rev. 2.1](https://ec.europa.eu/eurostat/web/nace) | seit 2025 für europäische Statistiken | Wirtschaftszweigklassifikation | Bevorzugte europäische Klassifikation für Unternehmenstätigkeiten |
| [VIES](https://europa.eu/youreurope/business/finance-and-tax/vat/check-vat-number-vies/index_en.htm) | abgerufen 2026-08-27 | Prüfung von EU-Umsatzsteuerkennungen | Externes Prüfverfahren mit dokumentiertem Zeitpunkt und Ergebnis |
| [BRIS-Unternehmenssuche](https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu/general-information-find-company_en) | abgerufen 2026-08-27 | Verbund nationaler Unternehmensregister | Prüfung von Registerdaten und EUID im jeweiligen Abdeckungsbereich |
| [EORI](https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operations/economic-operators-registration-and-identification-number-eori_en) | abgerufen 2026-08-27 | Zollkennung | Bedingte Kennung für Zollbeteiligte, nicht allgemeine Organisationspflicht |
| [BZSt zur Wirtschafts-Identifikationsnummer](https://www.bzst.de/SharedDocs/Downloads/DE/Presse/20241104_einfuehrung_widnr.pdf?__blob=publicationFile&v=3) | Einführung und Abgrenzung der W-IdNr. | Deutsche Steuerkennungen | Belegt die notwendige Unterscheidung von W-IdNr., USt-IdNr. und Steuernummer |
| [EU-KMU-Definition](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32003H0361) | Empfehlung 2003/361/EG | KMU-Kriterien | Grundlage einer zeitbezogenen Einstufung, nicht eines einfachen Kern-Boolean |
| [EU-Verordnung 651/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0651) | insbesondere Art. 2 Nr. 18 und Anhang I | Unternehmen in Schwierigkeiten und KMU | Kontextabhängige Rechtsprüfung, nicht Stammdatum |
| [EU-Sanktionsressourcen](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en) | laufend aktualisiert | Sanktionslisten und Rechtsakte | Quelle für datierte Prüfungen, nicht für dauerhaftes Compliance-Boolean |

Projektintern wurden zusätzlich ausgewertet:

- [Kennungsmodell](../../../../docs/architecture/identifier-model.md)
- [Agent-Spezifikation](../../agent/docs/agent-specification.md)
- [Adressrollen](../../address/docs/address-roles.md)
- [Kontakt-Quellenanalyse](../../contact/docs/source-analysis.md)
- die vom Nutzer bereitgestellte Tabelle „Ideen für die Selbstbeschreibung von
  Organisationen“.

## 5. Analyse der Organisationsklassen

### 5.1 `Organization`

Die W3C Organization Ontology versteht eine Organisation als bewusst
strukturierte soziale Einheit. Sie kann als Agent handeln, Mitglieder besitzen,
an Standorten tätig sein und in über- oder untergeordnete Einheiten gegliedert
werden. Das passt zur vorhandenen Construct-X-Klasse `Agent` und ist breiter als
eine juristische Person.

Beispiele sind Unternehmen, Behörden, Vereine, Arbeitsgemeinschaften und andere
organisierte Kollektive. Eine Organisation muss nicht zwingend selbst in einem
öffentlichen Register eingetragen oder Träger eigener Rechtspersönlichkeit sein.

### 5.2 `FormalOrganization`

`org:FormalOrganization` beschreibt Organisationen, die in der Welt allgemein
anerkannt sind und beispielsweise Verträge schließen, Konten führen oder
rechtliche Verantwortung tragen können. Diese Klasse eignet sich als
externe semantische Zwischenschicht zwischen einer allgemeinen Organisation und
einer konkret registrierten `LegalEntity`.

Construct-X führt dafür keine gleichnamige lokale Klasse ein. Der lokale Kern
verwendet unmittelbar `Organization` und `LegalEntity`; eine Ausrichtung von
`LegalEntity` zu `org:FormalOrganization` bleibt Aufgabe eines Alignment-Moduls.

### 5.3 `LegalEntity` statt lokaler `LegalPerson`

SEMIC beschreibt `legal:LegalEntity` als geschäftsfähige Einheit, die bei einer
zuständigen Stelle registriert ist und in einem Unternehmensregister erscheint.
Gaia-X beschreibt eine `LegalPerson`, die durch mindestens eine
Registrierungsnummer eindeutig identifiziert wird.

Construct-X verwendet `LegalEntity`:

- Der Begriff kollidiert sprachlich weniger mit `core/person`.
- Er lässt sich zu SEMIC direkt und zu Gaia-X als Alignment abbilden.
- Er macht sichtbar, dass nicht jede `Organization` eine registrierte rechtliche
  Einheit ist.
- Er verhindert, dass Niederlassungen, Abteilungen oder temporäre
  Arbeitsgemeinschaften automatisch als eigene juristische Person behandelt
  werden.

Einzelunternehmen und selbständig tätige natürliche Personen bleiben im MVP
Instanzen von `core/person:Person`. Die EU-KMU-Definition betrachtet eine
wirtschaftlich tätige natürliche Person zwar als Unternehmen unabhängig von
ihrer Rechtsform. Daraus folgt aber weder eine eigene Rechtspersönlichkeit noch
die Zugehörigkeit zur Klasse `Organization`.

Construct-X führt deshalb keine lokale Klasse `EconomicActor` ein. Der Begriff
war eine mögliche lokale Abstraktion, ist aber keine unmittelbar übernommene
Klasse der ausgewerteten Kernontologien. Wirtschaftliches Handeln einer Person
oder Organisation wird in einem Geschäftsprozess über eine kontextuelle
Agentenrolle beschrieben. Eine eigene Geschäftsprofilressource bleibt einer
späteren Anforderung vorbehalten, falls mehrere getrennte Geschäftstätigkeiten
derselben Person unterschieden werden müssen.

### 5.4 `OrganizationalUnit`

Eine Organisationseinheit besitzt ihre Bedeutung innerhalb einer übergeordneten
Organisation. Abteilung, Geschäftsbereich, Niederlassung und Werk sind nicht
pauschal synonym:

- Eine Abteilung ist typischerweise eine organisatorische Einheit.
- Eine Niederlassung kann eine Organisationseinheit, ein registrierter
  Unternehmensteil oder beides sein.
- Ein Werk oder Depot ist häufig primär ein Standort mit organisatorischer
  Funktion.
- Eine Betriebsstätte ist ein rechtlich und steuerlich geprägter Standortbegriff
  und nicht automatisch eine eigene Organisation.

Das implementierte Modell hält deshalb Organisationseinheit und Standort
getrennt; eine Verbindung bleibt einem zuständigen Standortmodell vorbehalten.

### 5.5 Rollen sind keine Organisationsunterklassen

Verkäufer, Käufer, Versender, Empfänger, Transporteur, Auftraggeber, Hersteller
und Abholer sind Rollen in einem bestimmten Liefer-, Vertrags- oder
Produktkontext. EU ePO verwendet dafür ein `AgentInRole`-Muster; eForms hält
Organisationsdaten zentral und referenziert die Organisation aus dem jeweiligen
Rollenkontext.

Das bestätigt das implementierte Construct-X-Muster:

```text
AgentRoleAssignment
  assignedAgent -> Organization oder Person
  role          -> kontrollierter Rollenwert
  context       -> Lieferschein, Sendung, Artikel, Vertrag oder Projekt
```

Eine Organisation kann so im selben Vorgang Verkäufer und Versender sein, ohne
zweimal als Stammdatenobjekt angelegt oder als zwei Klassen typisiert zu werden.

## 6. Quellenbewertung im Einzelnen

### 6.1 W3C Organization Ontology

**Stärken**

- sauberer allgemeiner Organisationsbegriff,
- `FormalOrganization` und `OrganizationalUnit`,
- Eltern-/Unterorganisationsbeziehungen,
- direkte und reifizierte Mitgliedschaften,
- Rollen, Stellen und Standorte,
- etablierte Verbindung zum Agentenbegriff.

**Grenzen**

- keine detaillierten Register-, Steuer- oder LEI-Daten,
- kein ausgearbeitetes Rechtsformmodell,
- keine Compliance- oder Credential-Semantik.

**Bewertung:** Beste strukturelle Referenz, aber allein kein vollständiger
Legal-Entity-Kern.

### 6.2 SEMIC Core Business Vocabulary

SEMIC konzentriert sich auf formal registrierte rechtliche Einheiten. Relevante
Begriffe sind unter anderem:

- rechtlicher Name und alternativer Name,
- rechtliche Kennung und weitere Kennungen,
- Rechtsform,
- registrierte Adresse,
- Registrierungsdatum,
- Unternehmenstätigkeit,
- Kontaktpunkt,
- rechtlicher Status und Vertretungsvollmacht.

Besonders wertvoll ist die Trennung zwischen allgemeiner Kennung und einer von
einer zuständigen Stelle verliehenen rechtlichen Kennung. Identifikatoren werden
mit ADMS strukturiert und können Notation, Schema, Aussteller und Ausgabedatum
tragen.

**Bewertung:** Fachlich stärkste Quelle für den `LegalEntity`-Teil. Der Scope ist
aber enger als `Organization`, weil informelle Organisationen und interne
Einheiten nicht im Mittelpunkt stehen.

### 6.3 Gaia-X `LegalPerson`

Gaia-X verlangt für `LegalPerson` aktuell:

- mindestens eine `registrationNumber`,
- genau eine `legalAddress`,
- genau eine `headquartersAddress`.

Als zulässige Registrierungsnummern nennt die Dokumentation lokale
Registerkennungen, EUID, EORI, VAT-ID und LEI. Zusätzlich werden Beziehungen zu
über- und untergeordneten rechtlichen Personen vorgesehen.

**Positive Übernahmen**

- rechtliche Identität braucht mindestens eine belastbare Register- oder
  Behördenkennung,
- Legal- und Headquarters-Adresse sind unterschiedliche Rollen,
- internationale Kennungsschemata müssen explizit unterschieden werden,
- Konzern- oder Mandatsbeziehungen sind für Selbstbeschreibungen relevant.

**Kritische Punkte**

- VAT-ID, EORI und LEI sind keine universellen Registrierungsnummern für jede
  rechtliche Einheit.
- `name` ist nur `0..1` und nicht ausdrücklich der Registername; als allgemeines
  Legal-Entity-Profil ist das zu schwach.
- Genau eine Legal- und Headquarters-Adresse ist eine Gaia-X-Profilentscheidung,
  keine allgemeine Ontologiewahrheit. Mehrere zeitlich, sprachlich oder
  jurisdiktionsbezogen relevante Zuordnungen müssen grundsätzlich möglich
  bleiben.
- Die Beschreibungen von `parentOrganizationOf` und `subOrganisationOf` wirken
  in der aktuellen Entwicklungsdokumentation teilweise gegenläufig zu den
  Property-Namen. Sie dürfen nicht ungeprüft übernommen werden.
- Die Dokumentation ist eine Entwicklungsversion; IRIs und Semantik können sich
  ändern.

**Bewertung:** Wichtiges Alignment und späteres Gaia-X-SHACL-Profil, aber keine
direkte Vorlage für die Construct-X-T-Box.

### 6.4 Schema.org

Schema.org deckt mit `legalName`, `legalAddress`, `legalRepresentative`,
`companyRegistration`, `leiCode`, `vatID`, `taxID`, `iso6523Code`,
`parentOrganization`, `subOrganization`, `department`, `member`, `employee`,
`foundingDate`, `contactPoint` und `location` einen großen Feldumfang ab.

Die Properties haben häufig sehr breite Wertebereiche und viele Kennungen sind
direkte Strings. Das ist für Web-Markup praktisch, aber für prüfbare
Stammdaten zu wenig strukturiert. `iso6523Code` ist als internationaler
Kennungsbezug interessant; Construct-X sollte dennoch das bereits etablierte
ADMS-Muster verwenden und ISO-6523-ICD gegebenenfalls als Kennungsschema führen.

**Bewertung:** Sehr gute Benennungs- und Alignmentquelle, keine normative
Kardinalitäts- oder Qualitätsgrundlage.

### 6.5 UBL

UBL trennt im `Party`-Aggregat unter anderem:

- `PartyIdentification`,
- `PartyName` und Handelsname,
- postalische Adresse,
- Steuerangaben,
- `PartyLegalEntity`,
- Kontakt,
- Finanzkonto.

`PartyLegalEntity` enthält insbesondere Registrierungsname, Company-ID,
Registrierungsadresse, Registerschema und Hauptsitzpartei. Das Registerschema
kann Kennung, Name, Typ und Jurisdiktion tragen. `FinancialAccount` bildet
Kontokennung, Kontoname, Kontotyp, Währung und weitere Bankinformationen als
eigenes Aggregat ab.

**Bewertung:** UBL bestätigt die benötigten Felder und die Trennung von
Rechtseinheit, Adresse, Kontakt und Konto. Als XML-Austauschschema ist es aber
weder Ontologieimport noch Klassenhierarchie-Vorlage.

### 6.6 GS1 und GLN

GS1 ist für Lieferketten und damit auch für 1Lieferschein besonders relevant.
Eine GLN kann je nach GLN-Typ eine rechtliche Einheit, Funktion, physische
Location oder digitale Location identifizieren. Daraus folgt:

- GLN ist ein wichtiges Kennungsschema für Construct-X,
- die bloße Existenz einer GLN beweist nicht, dass das Subjekt eine
  `LegalEntity` ist,
- Kennung und identifizierter Ressourcentyp müssen gemeinsam validiert werden,
- Standort-GLNs gehören an Standorte, Funktions-GLNs gegebenenfalls an
  Organisationseinheiten oder Funktionsressourcen.

### 6.7 GLEIF, LEI und Rechtsformen

Der LEI-Datensatz unterscheidet Level-1-Daten („who is who“) und
Level-2-Beziehungen („who owns whom“). Level 1 umfasst unter anderem rechtlichen
Namen, Legal- und Headquarters-Adresse, Register und Registerkennung,
Rechtsform, Erstellungsdatum und Status.

Die GLEIF-RDF-Ontologien sind für spätere LEI- und Konzern-Alignments wertvoll.
Die ISO-20275-ELF-Liste enthält in der Version Februar 2026 mehr als 3.600
Rechtsformen in mehr als 200 Jurisdiktionen. Sie ist deshalb einem frei
erfundenen lokalen Rechtsform-String vorzuziehen.

Ein LEI darf trotzdem nicht allgemein verpflichtend werden. Er ist nur für
Einheiten vorhanden, die einen LEI beantragt haben oder regulatorisch benötigen.

### 6.8 ePO und eForms

ePO und eForms liefern zwei für Construct-X besonders wichtige Muster:

1. Rollen wie Buyer oder Winner sind kontextuelle Rollen einer Organisation.
2. Rollenspezifische Kontaktdaten werden über eigene Touchpoints geführt, wenn
   sie von den allgemeinen Organisationskontakten abweichen.

eForms unterscheidet außerdem technische Dokumentkennungen von amtlichen
Organisationskennungen. Mehrere durch Rechtsbehörden ausgestellte Kennungen sind
möglich. Anforderungen an Name, Adresse, Website und Kontakt variieren je nach
Rolle und Verfahren.

**Bewertung:** Starke Bestätigung dafür, Pflichtangaben in SHACL-Profilen für
konkrete Anwendungsrollen festzulegen und nicht global in OWL zu verankern.

### 6.9 FOAF, GoodRelations und FIBO

- FOAF liefert nur einen sehr kleinen Agenten- und Organisationsbegriff und ist
  bereits über `core/agent` relevant.
- GoodRelations enthält etablierte E-Commerce-Begriffe wie rechtlichen Namen,
  VAT-ID, Tax-ID, DUNS und GLN. Viele davon sind heute in Schema.org aufgegangen.
- FIBO bietet sehr tiefe Modelle für rechtliche Einheiten, Eigentum, Kontrolle
  und Finanzorganisationen. Die Import- und Begriffskomplexität wäre für einen
  ersten Construct-X-Organisationskern unverhältnismäßig.

Diese Quellen eignen sich als spätere Alignments oder Detailreferenzen, nicht als
primäre Importbasis des MVP.

## 7. Auswertung der Selbstbeschreibungstabelle

### 7.1 Namen, Rechtsform und Adressen

| Eingabe | Quellenbefund | Kritische Bewertung | Vorläufige Modellzuordnung |
| --- | --- | --- | --- |
| Name verpflichtend | SEMIC: `legalName`; Schema.org: `legalName`; UBL: `RegistrationName` | Für ein striktes `LegalEntity`-Selbstbeschreibungsprofil sinnvoll. Eine allgemeine `Organization` braucht mindestens eine Bezeichnung, aber nicht zwingend einen Registername. | `legalName` für Legal Entity; allgemeines `name` für Organization |
| Rechtsform verpflichtend | SEMIC `legalFormType`; GLEIF/ISO 20275 | Nur für rechtliche Einheiten und soweit eine eigene Rechtsform anwendbar ist. Ein lokaler Freitext allein reicht für verlässliche Prüfung nicht. | Referenz auf kontrolliertes Rechtsformkonzept; Freitext höchstens ergänzend |
| Legal Address verpflichtend | Gaia-X, SEMIC, UBL und GLEIF kennen registrierte/rechtliche Adresse | Als Profilpflicht plausibel. Straße plus Hausnummer ist international nicht immer vorhanden; die Komponentenpflicht muss jurisdiktionsabhängig sein. | Bestehendes `core/address` mit `LegalAddressRole` |
| Headquarters Address | Gaia-X und GLEIF unterscheiden sie von Legal Address | Nicht immer verschieden und nicht in jedem Profil zwingend. Dieselbe Adresse kann beide Rollen besitzen. | `AddressAssignment` mit `HeadquartersAddressRole` |

Construct-X darf keine neuen Properties für Straße, Hausnummer, Postleitzahl oder
Ort in `core/organization` definieren. Dafür existiert `core/address`. Das
Organisationsprofil kann verlangen, dass mindestens eine passende
`AddressAssignment` vorhanden ist und die referenzierte Adresse ein
jurisdiktionsgerechtes Adressprofil erfüllt.

### 7.2 Vertretungsberechtigte

Die Tabellenstruktur `Titel, Vorname, Nachname, Geburtsdatum, Ort` sollte nicht
direkt in die Organisation eingebettet werden. Eine vertretungsberechtigte
Person bleibt eine Ressource aus `core/person`. Die Vertretung ist eine
eigenständige, potenziell zeitgebundene Beziehung mit mindestens:

- vertretener Organisation,
- vertretender Person oder Organisation,
- Art beziehungsweise Rolle der Vertretung,
- Einzel- oder Gesamtvertretung, soweit benötigt,
- Rechtsgrundlage oder Registerbezug,
- Gültigkeitszeitraum,
- optionalem Nachweis.

Geburtsdatum und Geburtsort sind personenbezogene Daten und dürfen nicht
pauschal als öffentliches Organisationsstammdatum wiederholt werden. Wenn ein
Registerabgleich sie benötigt, gehören sie in ein zugriffsgeschütztes
Prüfverfahren oder Credential. BRIS bestätigt, dass Register Informationen über
rechtliche Vertreter liefern können; die konkrete Verfügbarkeit ist jedoch
register- und dokumentabhängig.

### 7.3 Identifikationsnummern

| Kennung aus der Tabelle | Geltungsbereich | Pflichtbewertung | Modellierung und Prüfung |
| --- | --- | --- | --- |
| USt-IdNr. / VAT-ID | Umsatzsteuerregistrierung, insbesondere EU-Binnenmarkt | Nicht universell verpflichtend | `adms:Identifier` mit VAT-Schema und Jurisdiktion; VIES-Prüfung als datiertes Prüfergebnis |
| „Steuer-ID“ | Begriff ist für Organisationen zu unpräzise | In dieser Form nicht verwendbar | In Deutschland W-IdNr., USt-IdNr. und Steuernummer unterscheiden; keine persönliche IdNr. einer natürlichen Person übernehmen |
| LEI | Finanzmarkt- und freiwillige LEI-Registrierung | Nur verpflichtend, wenn vorhanden oder regulatorisch verlangt | `adms:Identifier` mit LEI-Schema; gegen GLEIF prüfen |
| EUID | Über BRIS verbundene Unternehmen und Zweigniederlassungen in dessen Geltungsbereich | Nur für abgedeckte Registerfälle | `adms:Identifier` mit EUID-Schema; gegen BRIS beziehungsweise Ursprungsregister prüfen |
| Handelsregistereintrag | Eingetragene Einheiten nach jeweiliger Jurisdiktion | Bedingt verpflichtend | Kennung plus Registerschema, Registerbehörde und Jurisdiktion; Gericht nicht als universelles Modellmerkmal erzwingen |
| EORI | Wirtschaftsbeteiligte bei Zollvorgängen | Nur für Zollkontext | `adms:Identifier` mit EORI-Schema; externe EORI-Validierung |
| GLN | GS1-identifizierte Einheit, Funktion oder Location | Nur bei GS1-Nutzung | Kennungsschema und GLN-Typ mit der identifizierten Ressource abgleichen |
| DID | beliebiges DID-Subjekt und kontrollierte Verifikationsmethoden | Optional | Technischer Identifikator beziehungsweise kontrollierter Identifier; rechtliche Bindung separat nachweisen |
| NorthData-, Schufa-, Creditreform-ID | Anbieter- oder plattformspezifischer Datensatz | Optional und nicht vertrauensbegründend | Generische externe Kennung mit Schema und Anbieter; keine eigene Core-Property pro Anbieter |

Die Eingangstabelle verlangt VAT-ID, Steuer-ID, LEI und EUID gleichzeitig. Das
ist als allgemeine Regel fachlich falsch: Die Kennungen haben unterschiedliche
Geltungsbereiche und nicht jede Organisation kann sie besitzen. Ein späteres
Self-Description-Shape sollte stattdessen verlangen:

1. mindestens eine rechtlich belastbare Kennung aus einem zulässigen Schema,
2. das zur Jurisdiktion und Organisationsart passende Kennungsschema,
3. zusätzliche Kennungen nur, wenn der betreffende Anwendungsfall sie verlangt,
4. getrennte Prüfberichte für externe Registerabfragen.

### 7.4 Tätigkeit und Klassifikation

`Beginn der Tätigkeit`, Gründung und Registereintragung sind nicht dasselbe:

- `foundingDate` bezeichnet typischerweise die Gründung,
- `registrationDate` die Eintragung,
- `activityStartDate` den tatsächlichen Beginn einer wirtschaftlichen Tätigkeit.

Bevor `Beginn der Tätigkeit` verpflichtend wird, muss geklärt werden, welche
dieser Aussagen gemeint ist und aus welchem Register sie belastbar stammt.
SEMIC bietet `registrationDate`, Schema.org `foundingDate`; ein eigenständiger
Tätigkeitsbeginn wäre eine zusätzliche Construct-X-Anforderung.

Für die Klassifikation wirtschaftlicher Tätigkeiten ist in Europa NACE Rev. 2.1
die naheliegende Referenz. Die Klassifikation sollte als kontrolliertes Konzept
mit Version und gegebenenfalls primärer beziehungsweise sekundärer Tätigkeit
modelliert werden, nicht als untypisierter String.

### 7.5 Kontoinformationen

IBAN, Kontoinhaber und BIC sind keine intrinsischen Eigenschaften einer
Organisation. UBL führt ein Finanzkonto als eigenes Aggregat. Außerdem können
Konten:

- mehreren Organisationen zugeordnet sein,
- nur für bestimmte Zahlungen, Verträge oder Währungen gelten,
- von Zahlungsdienstleistern verwaltet werden,
- sicherheits- und zugriffssensitiv sein.

Empfehlung: nicht in den Organisations-Core aufnehmen. Ein späteres
Payment-/Finance-Modul oder ein Vertragsprofil soll `FinancialAccount` und die
zeit- beziehungsweise zweckgebundene Kontozuordnung besitzen.

### 7.6 Status- und Compliance-Aussagen

| Tabellenangabe | Warum kein einfacher Core-Boolean? | Empfohlene Form |
| --- | --- | --- |
| Unternehmen nicht in Schwierigkeiten | Der EU-Begriff hängt von Rechtsform, Kapital, Verlusten, Insolvenz, Alter und Beihilfekontext ab. Ein fehlender Insolvenzregistereintrag genügt nicht. | Datiertes Assessment oder Credential mit Rechtsgrundlage, Prüfer und Gültigkeit |
| Einhaltung Russland-Sanktionen | Sanktionsregime und Listen ändern sich; außerdem können Eigentümer, Kontrolle, Güter und Transaktionen relevant sein. | Screening-Ergebnis mit geprüften Listen/Regimen, Zeitpunkt, Prüfer und Subjektumfang |
| KMU-Status | Hängt von Beschäftigten, Umsatz/Bilanz und verbundenen beziehungsweise Partnerunternehmen ab. | Zeitbezogene Klassifikation oder Credential mit Referenz auf EU-Definition und Berichtsperiode |
| Vorsteuerabzugsberechtigung | Steuerrechtlich, jurisdiktions-, perioden- und vorgangsabhängig | Steuerlicher Nachweis oder Credential; nicht pauschal in OWL inferieren |
| Kreditwürdigkeit | Anbieter-, Bewertungszeitpunkt- und Methodikabhängig | Externe Bewertung mit Anbieter, Datum, Skala und Gültigkeit; nicht aus Anbieter-ID ableiten |

Die kryptografische Prüfbarkeit eines Credentials beweist nur Integrität,
Aussteller und gegebenenfalls Status. Das W3C VC Data Model stellt ausdrücklich
keine Garantie dafür dar, dass der inhaltliche Claim wahr oder für den konkreten
Entscheidungsprozess ausreichend ist. Der Verifier braucht weiterhin eine
Vertrauens- und Prüfpolicy.

### 7.7 Mitgliedschaften, Versicherungen und Befähigungen

Mitgliedschaften sind Beziehungen, keine einfachen Eigenschaften der
Organisation. Eine Mitgliedschaft sollte mindestens Organisation, aufnehmende
Organisation, Mitgliedschaftsart, Mitgliedsnummer, Zeitraum und Status
zusammenhalten. Die Mitgliedsnummer identifiziert die Mitgliedschaft im Kontext
des Verbands und ist nicht zwingend eine globale Organisationskennung.

Berufsgenossenschaft, Verband und Innung können damit dasselbe Grundmuster
verwenden. Der Nachweis kann als separates Credential verknüpft werden.

Versicherungsbestätigungen, Bauvorlageberechtigung und öffentliche Bestellung
sind ebenfalls externe, zeit- und geltungsbereichsabhängige Nachweise. Dafür
sind mindestens relevant:

- Inhaber beziehungsweise Credential Subject,
- Aussteller,
- Nachweistyp,
- Gültigkeitsbeginn und -ende,
- Status beziehungsweise Widerruf,
- fachlicher und räumlicher Geltungsbereich,
- referenziertes Regelwerk oder Schema.

Sie gehören nicht als fest eingebaute Klassen oder Booleans in den ersten
Organisations-Core.

### 7.8 Webadresse und DID

Schema.org und eForms führen sowohl Website als auch Kontaktpunkte. Construct-X
verwendet dafür das bereits implementierte Kontaktmodell: Eine offizielle
Homepage ist eine Website-Kontaktmethode an einem Kontaktpunkt mit
`contact-usage:official` und `contact-purpose:general`. Rollenspezifische
Webseiten können getrennte Kontaktpunkte besitzen. Eine eigene Homepage-
Property im Organisationsmodul ist nicht erforderlich.

Der Abgleich von Impressum, Domaininhaber und Registerdaten ist ein
Prüfverfahren. Er kann nicht durch eine einfache SHACL-Regex ersetzt werden.

Ein `did:web` belegt technisch die Kontrolle über den entsprechenden Webpfad,
nicht automatisch die Identität der im Handelsregister eingetragenen Einheit.
Die Bindung zwischen DID und rechtlicher Kennung braucht einen vertrauenswürdigen
Nachweis oder eine nachvollziehbare Register-/Credential-Kette.

### 7.9 Bewertung der vorgeschlagenen Prüfregeln

| Prüfziel | Mit OWL/SHACL prüfbar | Externe Prüfung | Ergebnis, das gespeichert werden sollte |
| --- | --- | --- | --- |
| Name, Rechtsform und Legal Address vollständig | Vorhandensein, Datentypen, kontrollierte Rechtsform und AddressAssignment | Abgleich mit zuständigem Ursprungsregister; BRIS nur in seinem Abdeckungsbereich | Register, Abrufzeitpunkt, gefundene Entität, verglichene Felder, Match-Ergebnis |
| VAT-ID vorhanden und formal passend | Schema, Notation und länderspezifisches Muster | VIES oder zuständige nationale Stelle; VIES ist eine Suchmaschine über nationale Daten und liefert nicht in jedem Staat Namen/Adresse | Zeitpunkt, Requester, Status, bestätigter Name/Adresse soweit verfügbar, technische Fehler getrennt von „ungültig“ |
| LEI vorhanden und aktiv | LEI-Schema und formales Format | GLEIF-Datensatz beziehungsweise API | LEI-Status, Legal Name, Registerbezug, geprüfter Datensatzstand |
| EUID oder nationale Registernummer vorhanden | Schema, Notation, Register und Jurisdiktion | BRIS beziehungsweise nationales Register | Register, EUID/Register-ID, Status, Abrufdatum und Feldvergleich |
| Website gehört zur Organisation | URI-Syntax und HTTPS-Policy eines Profils | Impressum, Registerabgleich, Domain- und gegebenenfalls DNS-/Zertifikatsprüfung | geprüfte URL, Methode, Zeitpunkt, gefundene Identitätsmerkmale und Ergebnis |
| DID wird von der Organisation kontrolliert | DID-Syntax und referenzierbares DID Document | Challenge oder Signaturprüfung plus separate Bindung zur rechtlichen Identität | DID, Verifikationsmethode, Challenge-Zeitpunkt und Identitätsnachweis |
| Kein relevanter Sanktionstreffer | Nur Vorhandensein eines strukturierten Prüfergebnisses | Screening gegen die für Jurisdiktion und Vorgang relevanten aktuellen Listen, gegebenenfalls einschließlich Eigentum und Kontrolle | Listen/Regime, Version oder Abrufdatum, Suchparameter, Ergebnis, Prüfer und Gültigkeit |
| KMU-Status oder „nicht in Schwierigkeiten“ | Vollständigkeit eines Assessments und verwendete Rechtsgrundlage | Berechnung beziehungsweise fachliche Prüfung aus Finanz-, Personal-, Beteiligungs- und Insolvenzdaten | Berichtsperiode, Eingangsdaten, Regelwerkversion, Ergebnis, Aussteller und Gültigkeit |

Ein Timeout oder die Nichtverfügbarkeit eines Registers darf dabei nicht als
„Kennung ungültig“ oder „Prüfung bestanden“ gespeichert werden. Technisches
Prüfergebnis, fachliches Match und Vertrauensentscheidung sind drei getrennte
Ebenen.

## 8. Informative Anforderungen aus 1Lieferschein

Aus dem aktuellen Projektstand lassen sich folgende Bedarfe ableiten, ohne die
Delivery-Note-Ontologie als Referenzmodell zu behandeln:

### 8.1 Benötigte Akteursrollen

- Ersteller beziehungsweise Issuer,
- Verkäufer,
- Versender,
- Käufer,
- Empfänger,
- Transporteur,
- Auftraggeber beziehungsweise Originator,
- Hersteller,
- Abholpartei.

Diese Liste belegt den Bedarf an einer wiederverwendbaren Organisation und an
kontextuellen Rollen. Sie belegt nicht den Bedarf an gleichnamigen
Organisationsunterklassen.

### 8.2 Benötigte Organisationsinformationen

- rechtlicher und gegebenenfalls handelsüblicher Name,
- Partei- und Registerkennungen,
- Adressen und physische Locations,
- Standorte, Werke, Depots oder Niederlassungen,
- allgemeine und rollenspezifische Kontakte,
- Organisationseinheiten,
- geschäftspartnerbezogene Nummern wie Debitor, Kreditor, Kostenstelle,
  Baustelle, Standort oder Mandant.

Gerade die letzte Gruppe ist **kein Organisationsstammdatum**. Eine
Debitorennummer wird beispielsweise von einem Verkäufer für einen Kunden
vergeben und gilt nur in dieser Geschäftsbeziehung. Solche Kennungen gehören an
eine Beteiligungs-, Partner- oder Vertragszuordnung mit ausstellender
Organisation und Kontext.

## 9. Vorläufige Modulgrenzen

| Modul | Verantwortet | Nicht verantwortlich |
| --- | --- | --- |
| `core/agent` | gemeinsame Oberklasse `Agent` | Organisationsstruktur und rechtliche Daten |
| `core/organization` | Organisation, Legal Entity, Organisationseinheit, allgemeine Hierarchie, Mitgliedschaft und rechtliche Vertretung | Adressbestandteile, Kontaktkanäle, Bankkonten, Nachweisinhalte, Lieferrollen und Stellen im MVP |
| `core/person` | natürliche Person und deren intrinsische Kerndaten | Vertretungsverhältnis zur Organisation |
| `core/address` | Adresse und rollenbasierte `AddressAssignment` | Organisationshierarchie |
| `core/contact` | Kontaktpunkt, Kontaktmethode, Zweck und Nutzungskontext | Organisationsrolle und Mitgliedschaft |
| vorhandenes `core/participation` | Agentenrolle in Lieferschein, Projekt, Vertrag oder anderem Kontext | Organisationsstammdaten |
| externe Nachweissysteme | Bei Bedarf referenzierte Nachweise zu Versicherung, Befähigung, Mitgliedschaft oder Compliance | Im MVP ist kein eigenes Construct-X-Credential-Modul beschlossen |
| künftiges Payment-/Finance-Modul | Bankkonto und zweckbezogene Kontozuordnung | allgemeine Organisation |
| Domänenmodule | domänenspezifische Rollen, Profile und Pflichtangaben | Duplikate von Person, Organisation, Kontakt und Adresse |

Ein Import von `core/address` oder `core/contact` in die Organisations-T-Box ist
nicht automatisch erforderlich. Die Module können in einem Daten- oder
SHACL-Profil gemeinsam verwendet werden. So bleibt die Organisationsontologie
klein und vermeidet unnötige Importkopplung.

## 10. Vorläufiger Begriffskern

Die folgende Liste ist ein Ergebnis der Analyse, noch kein verbindlicher
Termkatalog.

### 10.1 Wahrscheinliche Klassen

- `Organization`
- `LegalEntity`
- `OrganizationalUnit`
- `Membership`
- `LegalRepresentation`

### 10.2 Wahrscheinliche Kerneigenschaften

- allgemeiner Name,
- rechtlicher Name,
- alternativer beziehungsweise Handelsname,
- Rechtsform,
- Registrierungsdatum,
- wirtschaftliche Tätigkeit beziehungsweise Klassifikation,
- über- und untergeordnete Organisation,
- Zugehörigkeit einer Organisationseinheit,
- ADMS-Kennungen,
- Verweise auf bestehende AddressAssignments und ContactPoints in Profilen.

Eine offizielle Homepage wird mit dem bestehenden Kontaktmodell als Website-
Kontaktmethode mit `contact-usage:official` und `contact-purpose:general`
abgebildet. Sie benötigt keine eigene Property im Organisationsmodul.

### 10.3 Nicht in den ersten Organisationskern

- IBAN, BIC und Kontoinhaber,
- pauschale Compliance-Booleans,
- Kreditratings und Bonitätsscores,
- eingebettete Personendaten von Vertretungsberechtigten,
- Lieferrollen wie Buyer, Seller oder Carrier,
- Debitoren-, Kreditoren-, Mandanten- und Kostenstellennummern ohne
  Beziehungskontext,
- Versicherungs-, Mitgliedschafts- und Befähigungsnachweise als flache
  Properties,
- eine lokale Klasse `EconomicActor` oder `FormalOrganization`,
- die W3C-ORG-Klasse `Post` beziehungsweise eine lokale Stelle im MVP,
- ein eigenes Credential-Modul ohne bestätigten modulübergreifenden Bedarf,
- eine lokale Ersatzklasse für `adms:Identifier`.

## 11. Profil- und Validierungsfolgen

Pflichtangaben gehören überwiegend in SHACL-Profile, nicht in die allgemeine
OWL-T-Box. Voraussichtlich werden mindestens drei Ebenen benötigt:

1. **Organization Core:** minimale strukturelle Konsistenz für beliebige
   Organisationen.
2. **Legal Entity Core:** rechtlicher Name, Registrierungsdatum, geeignete
   strukturierte Kennung und die noch zu bewertende Legal-Address-Zuordnung;
   Rechtsform bleibt im MVP optional.
3. **Spätere Self-Description-Profile:** strengere, use-case- oder
   jurisdiktionsbezogene Anforderungen einschließlich aktueller
   Registerprüfung und benötigter Nachweise.

Jurisdiktionsspezifische Profile sind nicht Teil des MVP. Spätere Profile können
Gaia-X, Lieferprozess, Beschaffung oder nationale Registeranforderungen
abbilden. Dadurch kann beispielsweise ein Gaia-X-Profil genau eine Legal- und
Headquarters-Adresse verlangen, ohne diese Kardinalität für jede Organisation
weltweit zu behaupten.

Externe Prüfungen wie VIES, GLEIF, BRIS, EORI, Domain- oder Sanktionsprüfung
sind keine reinen SHACL-Constraints. SHACL kann prüfen, dass ein strukturiertes
Prüfergebnis mit Datum, Status und Prüfdienst vorhanden ist. Die eigentliche
Live-Abfrage benötigt jedoch einen separaten Validierungsdienst.

## 12. Konsolidierter Entscheidungsstand

| Thema | Entscheidung für den MVP |
| --- | --- |
| Wirtschaftlicher Akteur | Keine lokale Klasse `EconomicActor` oder `Enterprise`; wirtschaftliches Handeln wird über kontextuelle Agentenrollen beschrieben |
| Einzelunternehmen und Freiberufler | Bleiben `Person`; keine automatische Typisierung als `Organization` oder lokale `LegalEntity` |
| Formale Organisation | Keine lokale Klasse `FormalOrganization`; späteres Alignment von `LegalEntity` zu W3C ORG prüfen |
| Organisationsteil oder Standort | Eigene Rechtspersönlichkeit führt zu `LegalEntity`; organisatorische Einordnung zu `OrganizationalUnit`; physischer Ort bleibt eine getrennte Standortressource |
| Mitgliedschaft | Bestandteil von Version 0.1.0 als eigene Beziehungsressource |
| Stelle / `Post` | Nicht Bestandteil des MVP; erst bei bestätigtem Bedarf an dauerhaft eingerichteten, auch unbesetzten Positionen |
| Rechtliche Vertretung | Bestandteil von `core/organization` als Beziehungsressource zwischen `LegalEntity` und `Person` |
| Kennungsschemata | ADMS-Struktur im MVP; keine globale falsche Pflichtliste aus VAT-ID, LEI, EUID und EORI |
| Jurisdiktionen | Jurisdiktionsspezifische Positivlisten und Prüfprofile werden nach dem MVP behandelt |
| Homepage | Wiederverwendung von `core/contact` als offizieller allgemeiner Website-Kontakt |
| Credentials | Kein eigenes Credential-Modul im MVP; externe Nachweise werden erst bei konkretem Bedarf angebunden |
| Personendaten von Vertretungsberechtigten | Nur Verweis auf eine `Person`; keine Duplikation von Name, Geburtsdatum oder Geburtsort |
| Datumsbegriff | `registrationDate` für die Registrierung einer `LegalEntity`; kein unscharfes `activityStartDate` im MVP |

Noch offen, aber für die fachliche MVP-Spezifikation nicht blockierend, sind die
konkreten Alignment-IRIs, kontrollierten Rechtsform- und Tätigkeitsvokabulare
sowie die spätere Auswahl nationaler Register- und Kennungsschemata.

## 13. Gesamtbewertung

Die Organisationsontologie sollte nicht aus der langen Attributliste einer
Selbstbeschreibung heraus gebaut werden. Ein großer Teil der Tabelle beschreibt
nicht die Organisation selbst, sondern Kennungen in bestimmten Regimen,
Beziehungen, Konten, Bewertungen oder zeitgebundene Nachweise.

Ein belastbarer Kern entsteht aus der Kombination von W3C ORG und SEMIC Core
Business Vocabulary, ergänzt um Alignments zu Gaia-X, Schema.org, GS1, GLEIF und
ePO. UBL, eForms und 1Lieferschein liefern wertvolle Anforderungen für Mappings
und Anwendungsprofile. Register- und Prüfdienste liefern Evidenz, dürfen aber
nicht mit der Ontologiesemantik vermischt werden.

Die wichtigste Architekturentscheidung lautet daher:

> Organisationsidentität, Prozessrolle, Beziehung, Kontakt, Adresse und
> überprüfbarer Nachweis sind getrennte Ressourcen beziehungsweise Module, die
> in anwendungsspezifischen Profilen zusammengeführt werden.

Damit bleibt `core/organization` wiederverwendbar und kann dennoch die strengen
Selbstbeschreibungs-, Gaia-X- und Lieferprozessanforderungen des Netzwerks
unterstützen.

## 14. Verständliches Übertragungsbeispiel

> Ein Handelsregister liefert rechtlichen Namen, Registerdatum und Kennung.
> Organization übernimmt diese Stammdaten, modelliert die externe
> Registerprüfung selbst aber nicht als Teil der Organisation.
