# Scope und Kompetenzfragen der Organisationsontologie

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`  
**Umsetzungsstand:** T-Box und Core Shapes 0.1.0 implementiert

## 1. Zweck

Die Organisationsontologie beschreibt Organisationen, rechtlich registrierte
Organisationen, interne Organisationseinheiten, Mitgliedschaften und rechtliche
Vertretungen. Sie stellt organisationsbezogene Stammdaten bereit, ohne
Personen-, Adress-, Kontakt-, Zahlungs-, Prozessrollen- oder Nachweismodelle zu
duplizieren.

Dieses Dokument legt den fachlichen Scope und die Kompetenzfragen des MVP fest.
Der zugehörige [Begriffskatalog](term-catalog.md) dokumentiert die implementierten
Klassen und Properties. Die fachliche Herleitung steht in der
[Quellenanalyse](source-analysis.md).

## 2. Bestätigter Scope

| Bereich | Entscheidung für den MVP |
| --- | --- |
| Allgemeine Organisation | `Organization` als organisierter kollektiver Akteur und Unterklasse von `conx-agent:Agent` |
| Rechtlich registrierte Organisation | `LegalEntity` als Unterklasse von `Organization` |
| Organisationseinheit | `OrganizationalUnit` für Abteilungen, Bereiche und vergleichbare Einheiten innerhalb einer Organisation |
| Wirtschaftlicher Akteur | Keine lokale Klasse `EconomicActor`, `Enterprise` oder `EconomicOperator` im Organisationskern |
| Einzelunternehmen und Freiberufler | Bleiben natürliche Personen und können über kontextuelle Agentenrollen wirtschaftlich handeln |
| Formale Organisation | Keine lokale Klasse `FormalOrganization`; externes W3C-ORG-Alignment später prüfen |
| Namen | Allgemeiner Name sowie rechtlicher und alternativer Name |
| Rechtsform | Optionale Referenz auf ein kontrolliertes Rechtsformkonzept; konkrete Wertemenge noch nicht geschlossen |
| Registrierung | `registrationDate` für die Registrierung einer `LegalEntity` |
| Tätigkeit | Optionale Referenz auf eine kontrollierte Tätigkeitsklassifikation; NACE ist bevorzugte europäische Quelle, aber nicht als MVP-Wertemenge festgelegt |
| Identifikatoren | Wiederverwendung von ADMS; keine lokale Identifier-Klasse und keine universelle Pflichtliste konkreter Schemata |
| Hierarchie | Allgemeine Über-/Unterordnungsbeziehung sowie spezielle Zugehörigkeit einer `OrganizationalUnit` |
| Mitgliedschaft | Eigene Beziehungsressource zwischen einem `Agent` und einer `Organization` |
| Stelle / `Post` | Nicht im MVP; erst bei Bedarf an dauerhaft eingerichteten, auch unbesetzten Positionen |
| Rechtliche Vertretung | Eigene Beziehungsressource von `LegalEntity` zu `Person` im Organisationsmodul |
| Adresse | Wiederverwendung von `core/address` und dessen `AddressAssignment`-Muster |
| Kontakt und Homepage | Wiederverwendung von `core/contact`; Homepage als offizieller allgemeiner Website-Kontakt |
| Prozessrollen | Verkäufer, Käufer, Versender, Empfänger, Transporteur und ähnliche Rollen bleiben kontextuelle Agentenrollen außerhalb des Organisationskerns |
| Nachweise | Kein eigenes Credential-Modul im MVP; externe Nachweise werden nicht ausmodelliert |
| Jurisdiktionen | Keine nationalen oder europäischen Positivlisten und Prüfprofile im MVP |

## 3. Fachliches Zielbild

```text
Agent
  ├── Person
  └── Organization
        ├── LegalEntity
        └── OrganizationalUnit

Membership
  ├── member                 -> Agent
  └── membershipOrganization -> Organization

LegalRepresentation
  ├── representedOrganization -> LegalEntity
  └── representative          -> Person

Organization ── hasAddressAssignment ── AddressAssignment ── Address
Organization ── hasContactPoint ─────── ContactPoint ─────── ContactMethod
```

Die Darstellung zeigt fachliche Verknüpfungen. Die verwendeten Core-Module und
externen Begriffe sind in `module.yaml` als aufgelöste Referenzen ohne
`owl:imports` dokumentiert; die Shapes werden für Integrationsprüfungen
gemeinsam geladen.

## 4. Kompetenzfragen

### OCQ-01: Wie wird eine Organisation eindeutig referenziert?

Jede Organisation erhält eine stabile IRI im Namensraum des jeweiligen
Datenhalters. Die Ressourcen-IRI ist von fachlichen Kennungen zu unterscheiden.
Eine Organisation kann null bis mehrere `adms:Identifier` besitzen.

Das Modell muss darstellen können:

- dieselbe Organisation mit mehreren Kennungen,
- Kennungen aus unterschiedlichen Schemata und Jurisdiktionen,
- die zuständige Schema-Agentur,
- Kennungen einer Organisationseinheit oder Mitgliedschaft,
- die Trennung zwischen globalen, registerbezogenen und nur kontextuell
  vergebenen Kennungen.

### OCQ-02: Was unterscheidet `Organization`, `LegalEntity` und `OrganizationalUnit`?

`Organization` ist der allgemeine Begriff für einen strukturierten kollektiven
Akteur. `LegalEntity` bezeichnet innerhalb des lokalen Scopes eine Organisation
mit eigener rechtlicher Identität. `OrganizationalUnit` bezeichnet einen
organisatorischen Teil, der nur im Zusammenhang mit mindestens einer
übergeordneten Organisation sinnvoll ist.

Eine Tochtergesellschaft mit eigener Rechtspersönlichkeit ist eine
`LegalEntity`. Eine Einkaufsabteilung ist eine `OrganizationalUnit`. Eine
Unternehmensgruppe oder Arbeitsgemeinschaft kann eine `Organization` sein, ohne
selbst automatisch `LegalEntity` zu sein.

### OCQ-03: Wie werden Einzelunternehmen und Freiberufler behandelt?

Eine selbständig tätige natürliche Person bleibt `conx-person:Person`. Sie wird
nicht allein aufgrund wirtschaftlicher Tätigkeit als `Organization` oder lokale
`LegalEntity` typisiert.

Im Liefer-, Vertrags- oder Beschaffungskontext kann die Person über eine
Agentenrollenzuordnung beispielsweise als Verkäufer, Auftragnehmer oder
Wirtschaftsteilnehmer auftreten. Geschäftliche Identifikatoren, Kontakte und
Adresszuordnungen können mit der Person verknüpft werden, ohne eine zweite
Scheinorganisation anzulegen.

Eine spätere `BusinessProfile`-Ressource ist nur dann zu prüfen, wenn mehrere
getrennte Geschäftstätigkeiten, Handelsnamen oder Außenauftritte derselben Person
unterscheidbar werden müssen. Sie ist kein Bestandteil von Version 0.1.0.

### OCQ-04: Wie werden Organisationsnamen unterschieden?

Der MVP unterscheidet:

- `name` als allgemein verwendbare Bezeichnung einer Organisation,
- `legalName` als amtlich beziehungsweise rechtlich geführten Namen einer
  `LegalEntity`,
- `alternativeName` für Handelsnamen, Kurzformen und weitere gebräuchliche
  Bezeichnungen.

`name` ist für jede Organisation verpflichtend. `legalName` ist zusätzlich für
jede `LegalEntity` verpflichtend. Mehrsprachige Namen dürfen mehrfach angegeben
werden; eine Sprache darf in späteren Shapes höchstens einen gleichartigen
bevorzugten Wert erhalten, wenn dieser Bedarf bestätigt wird.

### OCQ-05: Wie wird die Rechtsform dargestellt?

Eine Rechtsform wird als Referenz auf ein kontrolliertes Konzept modelliert und
nicht allein als freier String. GLEIF/ISO 20275 ist die bevorzugte internationale
Quelle. Da im MVP keine Jurisdiktionsprofile festgelegt werden, wird die konkrete
Wertemenge noch nicht geschlossen.

Die Rechtsform gehört nur zur `LegalEntity`. Sie wird im allgemeinen
Organization-Core nicht verlangt und bleibt auch im Legal-Entity-Core-Shape
optional.

### OCQ-06: Welche Kennungen gehören zur Organisation?

Alle Kennungen verwenden das bestehende ADMS-Muster:

```text
Organisation oder Beziehungsressource
  └── adms:identifier
        └── adms:Identifier
              ├── skos:notation
              └── adms:schemaAgency
```

Eine feste globale Liste aus VAT-ID, LEI, EUID, EORI und GLN wäre fachlich
falsch. Diese Schemata haben unterschiedliche Geltungsbereiche:

- nationale Registerkennung oder EUID für rechtliche Registrierung,
- VAT-ID für Umsatzsteuerkontexte,
- LEI für LEI-registrierte Einheiten,
- EORI für Zollvorgänge,
- GLN für GS1-identifizierte Rechtseinheiten, Funktionen oder Standorte,
- DID für technische Kontrolle, nicht als alleiniger Nachweis rechtlicher
  Identität.

Version 0.1.0 prüft deshalb die ADMS-Struktur, aber noch keine
jurisdiktionsabhängige Positivliste. Geschäftspartnerbezogene Debitoren-,
Kreditoren-, Mandanten- oder Standortnummern gehören an die jeweilige
Beziehungs- oder Prozessressource und nicht pauschal an die Organisation.

### OCQ-07: Wie werden Organisationseinheiten und Standorte getrennt?

Die Entscheidung erfolgt entlang zweier unabhängiger Fragen:

1. Besitzt die Ressource organisatorische Zuständigkeit, Leitung oder Funktion?
2. Beschreibt die Ressource einen physischen Ort mit Adresse oder Koordinaten?

Eine Abteilung ist nur `OrganizationalUnit`. Eine Baustelle ist primär ein
Standort beziehungsweise Projektort. Ein Werk oder Depot kann aus zwei
verbundenen Ressourcen bestehen: einer Organisationseinheit und einem Standort.

Eine Niederlassung ohne eigene Rechtspersönlichkeit ist typischerweise eine
`OrganizationalUnit` mit Standort und gegebenenfalls eigener Registerkennung.
Eine Tochtergesellschaft mit eigener Rechtspersönlichkeit ist dagegen
`LegalEntity`, auch wenn sie am gleichen Standort sitzt.

### OCQ-08: Wie werden Organisationshierarchien dargestellt?

Für allgemeine Beziehungen zwischen Organisationen sind
`subOrganizationOf` und die inverse Beziehung `hasSubOrganization` implementiert.
Sie drücken organisatorische Unterordnung aus, aber nicht automatisch
Eigentum, gesellschaftsrechtliche Kontrolle oder Konzernabschlussbeziehungen.

Für eine `OrganizationalUnit` wird die speziellere Beziehung `unitOf` mit der
inversen Beziehung `hasUnit` verwendet. Im Core-Profil muss jede
`OrganizationalUnit` mindestens einer übergeordneten `Organization` zugeordnet
sein. Mehrere Zuordnungen werden im fachlichen Modell nicht grundsätzlich
verboten, damit Matrixorganisationen nicht ausgeschlossen werden.

### OCQ-09: Wie wird Mitgliedschaft modelliert?

Mitgliedschaft ist eine eigenständige Beziehung zwischen einem `Agent` und einer
`Organization`:

```text
Membership
  member                 -> Agent
  membershipOrganization -> Organization
```

Der `member` kann eine Person oder eine Organisation sein. Damit lassen sich
auch Verbandsmitgliedschaft, Innung oder Berufsgenossenschaft abbilden. Eine
Mitgliedsnummer wird als `adms:Identifier` der `Membership` modelliert, weil sie
die konkrete Mitgliedschaft im System der aufnehmenden Organisation
identifiziert.

Rolle, Status und Zeitraum einer Mitgliedschaft sind plausible Erweiterungen,
werden aber erst im SHACL- und Ausbaustufenschnitt verbindlich bewertet.

### OCQ-10: Was bedeutet eine Stelle und warum gehört sie nicht in den MVP?

Eine Stelle im Sinn von W3C ORG `Post` ist eine dauerhaft eingerichtete Position
innerhalb einer Organisation, beispielsweise „Leitung Einkauf“. Sie kann ihren
Inhaber wechseln oder vorübergehend unbesetzt sein. Sie ist damit etwas anderes
als Mitgliedschaft, Rollenwert, Jobtitel oder rechtliche Vertretung.

Der aktuelle Construct-X-Use-Case benötigt keine eigenständig referenzierbaren,
unbesetzten Positionen oder vollständigen Organigramme. `Post` und lokale
Stellen-Properties werden deshalb in eine spätere Ausbaustufe verschoben.

### OCQ-11: Wie wird rechtliche Vertretung modelliert?

Rechtliche Vertretung wird im Organisationsmodul als eigene Beziehungsressource
modelliert:

```text
LegalRepresentation
  representedOrganization -> LegalEntity
  representative          -> Person
```

Die Vertretungsressource enthält keine Kopien von Titel, Vorname, Nachname,
Geburtsdatum oder Geburtsort. Diese Angaben bleiben ausschließlich an der
referenzierten Person. Vertretungsart, Gültigkeit, Einzel-/Gesamtvertretung und
Nachweis können später ergänzt werden, ohne das Grundmuster zu ändern.

Eine einfache direkte Property `hasLegalRepresentative` wird im MVP nicht als
zweite parallele Datenrichtung verlangt, weil sie die Beziehungsressource
umgehen und spätere Metadaten abschneiden würde.

### OCQ-12: Wie werden Organisationsadressen dargestellt?

Die Organisation verwendet `conx-addr:hasAddressAssignment`. Die
Adressbestandteile verbleiben vollständig in `core/address`. Relevante
Adressrollen sind insbesondere:

- `roles:LegalAddressRole`,
- `roles:HeadquartersAddressRole`,
- `roles:RegistrationAddressRole`,
- `roles:PostalAddressRole`.

Dieselbe Adresse kann über eine Zuordnung mehrere Rollen besitzen. Eine
Legal-Entity-Selbstbeschreibung kann später mindestens eine rechtliche Adresse
verlangen, ohne diese Kardinalität als OWL-Wahrheit für jede Organisation zu
formulieren.

### OCQ-13: Wie werden Kontakt und Homepage dargestellt?

Die Organisation verweist mit `conx-contact:hasContactPoint` auf bestehende
Kontaktpunkte. Eine offizielle Homepage wird ohne neue Organization-Property so
modelliert:

```text
Organization
  -> hasContactPoint
       contactUsage   -> official
       contactPurpose -> general
       hasContactMethod
         contactChannel -> website
         contactURI     -> offizielle Web-IRI
```

Rollenspezifische Liefer-, Rechnungs-, Support- oder Vertriebskontakte können
weitere Kontaktpunkte verwenden. Kontaktwerte werden nicht in die Organisation
kopiert.

### OCQ-14: Wie werden Verkäufer, Käufer und andere Geschäftsrollen abgebildet?

Verkäufer, Käufer, Versender, Empfänger, Transporteur, Hersteller und
Auftraggeber sind keine Unterklassen von `Organization`. Sie werden durch eine
Agentenrollenzuordnung mit dem jeweiligen Lieferschein, Vertrag, Artikel,
Projekt oder anderen Kontext verbunden.

Dadurch kann dieselbe Organisation mehrere Rollen im selben Vorgang übernehmen.
Auch eine natürliche Person kann als wirtschaftlicher Akteur auftreten, ohne als
Organisation typisiert zu werden.

### OCQ-15: Welches Datum und welche Tätigkeit gehören zum MVP?

`registrationDate` beschreibt das Datum der Registrierung einer `LegalEntity`.
Es ersetzt den unscharfen Begriff „Beginn der Tätigkeit“. `foundingDate` und
`activityStartDate` werden im MVP nicht eingeführt.

Eine wirtschaftliche Tätigkeit kann optional auf ein kontrolliertes Konzept
verweisen. NACE Rev. 2.1 ist für europäische Daten die bevorzugte Referenz, wird
aber ohne beschlossenes Jurisdiktionsprofil nicht zur geschlossenen
MVP-Wertemenge.

### OCQ-16: Wie werden Versicherung, Befähigung und Compliance behandelt?

Versicherungen, berufliche Befähigungen, KMU-Status, Steuerstatus,
Kreditwürdigkeit und Sanktionsprüfungen sind keine dauerhaften intrinsischen
Organisationseigenschaften. Das Organisationsmodul führt dafür weder einfache
Booleans noch ein eigenes Credential-Modul ein.

Solche Aussagen können später als externe, datierte Nachweis- oder
Prüfressourcen referenziert werden. Das konkrete Modell wird erst mit einem
bestätigten modulübergreifenden Use Case festgelegt.

### OCQ-17: Was legt das SHACL-Anforderungsdokument fest?

Das [SHACL-Anforderungsdokument](shacl-requirements.md) legt insbesondere fest:

- Mindest- und Maximalkardinalitäten von Name und Legal Name,
- Pflicht und Datentyp von `registrationDate`,
- Mindestangaben einer `LegalEntity`,
- Struktur und erlaubte Werte einer Organisationshierarchie,
- Mindestangaben von `Membership` und `LegalRepresentation`,
- Anforderungen an ADMS-Identifier ohne jurisdiktionsspezifische Positivliste,
- Wiederverwendung der bestehenden Address- und Contact-Shapes,
- gültige und ungültige Szenarien für jede Klasse und Beziehung.

## 5. Modulgrenzen

| Modul | Zuständigkeit im Zusammenspiel |
| --- | --- |
| `core/agent` | Gemeinsame Oberklasse von Person und Organisation |
| `core/organization` | Organisation, Legal Entity, Organisationseinheit, Hierarchie, Mitgliedschaft und rechtliche Vertretung |
| `core/person` | Natürliche Person; Ziel der Vertretungsbeziehung und möglicher Member |
| `core/address` | Adresse, AddressAssignment und Adressrollen |
| `core/contact` | Kontaktpunkt, Kontaktmethode, Nutzung, Zweck und Homepage |
| Domänen-/Participation-Modell | Verkäufer-, Käufer-, Liefer-, Projekt- und Vertragsrollen |
| Externe Nachweissysteme | Versicherung, Befähigung, Compliance, Registerabgleich und weitere Evidenz |

## 6. Ausdrücklich außerhalb des Organisationskerns

- natürliche Personendaten,
- eine Klasse `EconomicActor`, `Enterprise` oder lokale `EconomicOperator`,
- lokale `FormalOrganization` und `Post`,
- Stellenpläne und vollständige Organigramme,
- Standorte, Geometrien und Adressbestandteile,
- E-Mail, Telefon, Website und andere Kontaktwerte,
- Käufer-, Verkäufer-, Hersteller-, Transport- und Projektrollen,
- Bankkonten, IBAN, BIC und Kontoinhaber,
- Eigentums-, Beteiligungs- und Kontrollquoten,
- wirtschaftlich Berechtigte,
- Vollmachtstexte und detaillierte Vertretungsregeln,
- Versicherungs-, Befähigungs- und Compliance-Nachweise,
- Kreditratings und Bonitätsscores,
- nationale Register- und Validierungsdienste,
- allgemeine Provenienz und Historisierung einzelner Aussagen.

Die Ausschlüsse verhindern keine Verknüpfung mit externen Ressourcen. Sie legen
fest, dass deren Semantik nicht vom Organisationsmodul verantwortet wird.

## 7. Nicht blockierende Folgeentscheidungen

| Thema | Behandlung |
| --- | --- |
| Rechtsformvokabular | ISO 20275/GLEIF als bevorzugte Quelle; konkrete Übernahme nach Analyse von Lizenz, IRIs und Updateprozess |
| Tätigkeitsvokabular | NACE Rev. 2.1 bevorzugt; noch keine geschlossene MVP-Wertemenge |
| Registerkennungen | Konkrete nationale und europäische Schemata erst in späteren Profilen |
| Mitgliedschaftsrolle und Zeitraum | Nicht Bestandteil des Core-MVP; Erweiterung nach bestätigtem Use Case |
| Vertretungsart und Gültigkeit | Erweiterung der Beziehungsressource in einer späteren Ausbaustufe möglich |
| Standortmodul | Organisationskern referenziert Standorte erst, wenn eine zuständige lokale Standortklasse festgelegt ist |
| Externe Alignments | Maschinelles Alignment zu W3C ORG, SEMIC, Gaia-X und Schema.org erst nach IRI- und Importprüfung |

## 8. Abnahme des SHACL-Vertrags

Der fachliche SHACL-Vertrag ist umgesetzt, weil:

1. die fünf MVP-Klassen und ihre Zuständigkeiten bestätigt sind,
2. die festgelegten Properties und Kardinalitäten aus dem Termkatalog bestätigt
   sind,
3. die Trennung zwischen Organisationseinheit und Standort akzeptiert ist,
4. die Wiederverwendung von ADMS, Address und Contact bestätigt ist,
5. die zurückgestellten Jurisdiktions-, Credential- und Post-Themen nicht als
   MVP-Pflichten behandelt werden.

Das visuelle Zielmodell ist im
[Organisationsdiagramm](diagrams/organization-concept-model.md) dokumentiert.
Der vollständige Shape-Katalog, die Constraints, Fehlermeldungen und
Beispielszenarien stehen im
[SHACL-Anforderungsdokument](shacl-requirements.md).

## 9. Verständliches Beispiel

> Die Beispiel Bau GmbH ist eine Legal Entity. Ihre Planungsabteilung ist eine
> OrganizationalUnit. Anna Müller wird über Membership als Mitglied und über
> LegalRepresentation getrennt als rechtliche Vertreterin beschrieben.
