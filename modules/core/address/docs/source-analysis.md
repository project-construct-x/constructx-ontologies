# Quellenanalyse: Adressmodelle in vCard, Schema.org und UBL 2.5

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Stand der Recherche:** 13. August 2026  
**Geltungsbereich:** `core/address`

## 1. Ziel und Abgrenzung

Dieser Bericht stellt die Adresskonzepte aus drei Ausgangsquellen gegenüber. Er dokumentiert die ursprüngliche Entscheidungsgrundlage der inzwischen implementierten Construct-X Address Ontology. Die verbindlichen Festlegungen stehen im aktuellen Konzeptmodell und in der T-Box.

Unterschieden werden:

- eigentliche Bestandteile einer Adresse,
- geerbte oder benachbarte Kontakt- und Geoinformationen,
- die Rolle einer Adresse in einem Vorgang, beispielsweise Liefer- oder Registrierungsadresse,
- formale Modellmerkmale wie Kardinalitäten, Reihenfolge und Mehrsprachigkeit.

## 2. Untersuchte Quellen

1. [W3C vCard Ontology](https://www.w3.org/TR/vcard-rdf/), W3C Interest Group Note vom 22. Mai 2014, Namespace `http://www.w3.org/2006/vcard/ns#`.
2. [Schema.org PostalAddress](https://schema.org/PostalAddress) und [Schema.org Data Model](https://schema.org/docs/datamodel.html), Entwicklungsversion V30.0 vom 19. März 2026, abgerufen am 13. August 2026.
3. Lokale Datei `D:\Sciebo\Construction-X Privat\200_Arbeitspakete\300_Arbeitspaket_3\400_AP3.4\2026-07-07_Lieferschein_Ontologie\UBL-CommonAggregateComponents-2.5.xsd`, UBL 2.5 Committee Specification 01 vom 15. April 2026. SHA-256: `CE667698A58840658811CD3A2C763DCA18985FEA454D379D0DA11B891B347478`. Vergleichbare offizielle Quellen sind die [UBL-2.5-Spezifikation](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/UBL-2.5.html) und das [offizielle Common-Aggregate-Components-XSD](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/xsd/common/UBL-CommonAggregateComponents-2.5.xsd).

## 3. Kurzfazit

| Quelle | Hauptzweck | Granularität | Stärkste Seite | Wesentliche Grenze |
| --- | --- | --- | --- | --- |
| vCard RDF | Kontaktdaten für Personen, Organisationen, Gruppen und Orte | kompakt | etabliertes RDF/OWL-Modell und einfaches Verknüpfen einer Adresse mit einem Objekt | nur fünf aktuelle direkte Adressbestandteile; Postfach und erweiterte Adresse sind veraltet |
| Schema.org | breit verwendbares Web-Markup | kompakt bis mittel | hohe praktische Verbreitung, einfache JSON-LD-Nutzung, Land und Region können Ressourcen sein | bewusst flexibles Modell ohne Pflichtfelder oder adressspezifische Kardinalitäten; erbt fachfremde Kontaktfelder |
| UBL 2.5 | strukturierter Geschäfts- und Logistikdatenaustausch | sehr fein | 28 Adresskomponenten, Rollen im Geschäftsprozess, Codes, Freitextzeilen und Geokoordinaten | XML- und austauschformatorientiert; einige Begriffe überlappen semantisch oder sind stark an Post- und Geschäftsvorgänge gebunden |

Keine Quelle ist allein vollständig für Construct-X. vCard und Schema.org eignen sich gut für Interoperabilität im RDF- und Web-Umfeld. UBL liefert den größten fachlichen Feldumfang, sollte aber nicht unverändert als Ontologiestruktur übernommen werden.

## 4. Gegenüberstellung der Konzepte

| Semantisches Konzept | vCard RDF | Schema.org | UBL 2.5 | Bewertung für die spätere Modellierung |
| --- | --- | --- | --- | --- |
| Adressobjekt | `vcard:Address` | `schema: PostalAddress` | `cac:Address` / `AddressType` | Gemeinsamer Kern vorhanden; Schema.org und vCard fokussieren eine postalisch zustellbare Adresse, UBL definiert allgemeine Adressinformationen. |
| Verknüpfung zum Träger | `vcard:hasAddress` mit Wertebereich `vcard:Address` | `schema:address`; zusätzlich spezialisierte Beziehungen wie `billingAddress` und `deliveryAddress` | unterschiedliche ASBIE-Elemente wie `PostalAddress`, `DeliveryAddress` und `RegistrationAddress` | Die Rolle gehört eher an die Beziehung zwischen Objekt und Adresse als in die Adresse selbst. |
| Adressart | Typisierung eines Adressobjekts unter anderem mit `vcard:Home` oder `vcard:Work` | kein direktes Feld; geerbtes `contactType` ist allgemein für Kontaktpunkte | `cbc:AddressTypeCode` | Nicht vorschnell gleichsetzen: privat/geschäftlich, Lieferzweck und fachlicher Adresstyp sind verschiedene Dimensionen. |
| Identität | RDF-IRI des Adressobjekts; kein eigenes aktuelles Adress-ID-Feld | RDF/JSON-LD-`@id` oder geerbtes `schema:identifier` | `cbc:ID` mit Identifikationsschema | Eine adressspezifische Kennung und die globale IRI-Identität sollten getrennt bleiben. |
| Adressformat | kein Feld | kein Feld | `cbc:AddressFormatCode` | UBL-spezifischer Zusatz, potenziell nützlich für Rendering- oder Austauschprofile. |
| Straße als Gesamttext | `vcard:street-address` | `schema:streetAddress` | `cac:AddressLine/cbc:Line` als unstrukturierte Zeile | Die beiden RDF-Quellen zerlegen Straßenname und Hausnummer nicht. Eine direkte Abbildung auf UBL `StreetName` wäre daher verlustbehaftet. |
| Straßenname | nur im Gesamttext | nur im Gesamttext | `cbc:StreetName` | UBL bietet die feinste strukturierte Darstellung. |
| zusätzlicher Straßenname | kein aktuelles Feld | höchstens unspezifisch über `extendedAddress` | `cbc:AdditionalStreetName` | Relevant für internationale Adressen und lokal gebräuchliche Parallelbezeichnungen. |
| Hausnummer | nur im Gesamttext | nur im Gesamttext | `cbc:BuildingNumber` | Für Bau- und Logistikfälle wahrscheinlich ein wichtiger eigenständiger Bestandteil. |
| Gebäude-/Blockname | kein Feld | höchstens `extendedAddress` | `cbc:BuildingName`, `cbc:BlockName` | UBL trennt physische Lagebestandteile sauberer. |
| Untereinheit im Gebäude | kein aktuelles Feld; `extended-address` ist veraltet | `extendedAddress` für Wohnung, c/o oder alternativen Namen | `cbc:Floor`, `cbc:Room`, `cbc:InhouseMail` | Ein einziges Erweiterungsfeld ist interoperabel, getrennte Bestandteile sind präziser. Beide Repräsentationen können parallel nötig sein. |
| Postfach | `post-office-box` ist veraltet | `postOfficeBoxNumber` | `cbc:Postbox` | Schema.org und UBL behandeln das Postfach weiterhin ausdrücklich. |
| freie Adresszeilen | kein aktuelles `label`; `label` ist veraltet | über `streetAddress` oder `extendedAddress`, aber ohne geordnete Zeilenstruktur | `cac:AddressLine` 0..n; jede vorhandene AddressLine enthält `cbc:Line` 1..n | Für verlustfreien Import und landesspezifische Druckformen sollte eine geordnete Freitextdarstellung diskutiert werden. |
| interne Zustellung / Empfängerhinweis | kein Bestandteil der Adresse | teilweise unspezifisch in `extendedAddress` | `cbc:Department`, `cbc:MarkAttention`, `cbc:MarkCare`, `cbc:InhouseMail` | UBL trennt Adresse und postale Zustellhinweise nicht vollständig. Für Construct-X ist zu klären, ob diese Angaben zur Adresse oder zur Adressierung einer Sendung gehören. |
| Ort / Gemeinde | `vcard:locality` | `schema:addressLocality` | `cbc:CityName` | Nahe semantische Entsprechung. Der Begriff sollte nicht auf rechtlich definierte Städte beschränkt werden. |
| Stadtteil | kein eigenes Feld | kein eigenes Feld | `cbc:CitySubdivisionName` | Für große Baustellen, Quartiere und internationale Adressen potenziell relevant. |
| Bezirk | nur unscharf über `region` | nur unscharf über `addressRegion` | `cbc:District` | UBL bietet eine zusätzliche Verwaltungsebene. |
| Bundesland / Provinz / Verwaltungseinheit | `vcard:region` als Text, beispielhaft Staat oder Provinz | `schema:addressRegion` als `AdministrativeArea` oder Text | `cbc:CountrySubentity` als Text und `cbc:CountrySubentityCode` als Code | Dies ist die beste fachliche Entsprechung. UBL `Region` ist nicht automatisch dasselbe wie vCard/Schema.org `region`. |
| größere geografische oder wirtschaftliche Region | kein getrenntes Feld | kein getrenntes direktes Feld | `cbc:Region` | In UBL eine anerkannte geografische oder wirtschaftliche Region beziehungsweise Ländergruppe, nicht zwingend eine Verwaltungsebene. |
| Postleitzahl | `vcard:postal-code` | `schema:postalCode` | `cbc:PostalZone` | Direkte Entsprechung; als Text modellieren, damit führende Nullen und Buchstaben erhalten bleiben. |
| Land | `vcard:country-name` als Text | `schema:addressCountry` als `schema:Country` oder Text; Alpha-2 wird empfohlen | `cac:Country` mit `cbc:IdentificationCode` und `cbc:Name` | Construct-X sollte sowohl eine referenzierbare Länderressource als auch Code-/Textrepräsentationen abbilden können. |
| Grundstück / Flurstück | kein Feld | kein direktes Feld | `cbc:PlotIdentification` | Für Construction-X fachlich besonders interessant, semantisch aber eventuell besser als Beziehung zu einem Grundstücksobjekt statt als bloßer Adressliteral. |
| Geokoordinaten | `vcard:hasGeo` beziehungsweise GEO-Parameter außerhalb der fünf direkten Address-Komponenten; alte Latitude/Longitude-Datenfelder sind veraltet | nicht direkt in `PostalAddress`; üblicherweise über `Place` und `GeoCoordinates` | `cac:LocationCoordinate` 0..n mit Koordinatensystem, Grad/Minuten, Richtung und Höhe | Adresse und Geoposition sollten verknüpft, aber nicht gleichgesetzt werden. Das Koordinatenmodell sollte ein modernes CRS-fähiges Geomodell wiederverwenden. |
| Zeitzone | `vcard:tz` am beschriebenen Objekt oder als Parameter | kein direktes Adressfeld | `cbc:TimezoneOffset` | Ein momentaner UTC-Offset ist weniger stabil als eine benannte Zeitzone; UBL definiert ausdrücklich den Offset zum Austauschzeitpunkt. |
| Beschreibung | allgemein über andere Vokabulare; kein spezielles Address-Feld | geerbtes `schema:description` | `cbc:Description` 0..n | Generische Beschreibung nicht mit einer formatierten Adresszeile vermischen. |
| Mehrsprachigkeit | vCard-Parametermechanismus mit `language`; zusätzlich direkte und n-äre Eigenschaften | allgemeine RDF-Sprachliterale möglich, aber kein adressspezifischer Mechanismus | Wiederholung ausgewählter Felder ausdrücklich nur für denselben Inhalt in mehreren natürlichen Sprachen | Sprachvarianten brauchen eine klare Semantik und dürfen nicht als mehrere sachlich verschiedene Werte missverstanden werden. |
| Kontaktinformationen | E-Mail, Telefon und Adresse sind getrennte vCard-Eigenschaften | `PostalAddress` erbt wegen der Unterklasse `ContactPoint` unter anderem E-Mail, Telefon, Fax und Öffnungszeiten | `ElectronicAddress` ist ein separates UBL-Konzept; postalische Adresse enthält keine Telefon- oder E-Mail-Felder | Für Construct-X sollten physische Adresse und Kommunikationskanal getrennte Konzepte bleiben. |

## 5. Modellanalyse je Quelle

### vCard RDF

`vcard:Address` beschreibt die Bestandteile einer Zustelladresse. Der aktuelle direkte Kern besteht aus:

- `vcard:street-address`
- `vcard:locality`
- `vcard:region`
- `vcard:postal-code`
- `vcard:country-name`

Alle fünf Eigenschaften haben `xsd:string` als Wertebereich. `vcard:hasAddress` ist eine Objekteigenschaft mit `vcard:Address` als Wertebereich. Für die fünf Bestandteile existieren zusätzlich n-äre `has...`-Eigenschaften, über die vCard-Parameter wie Sprache oder Sortierinformation abgebildet werden können.

Die Ontologie zeigt Adressen im Beispiel zusätzlich als `vcard:Home` oder `vcard:Work`. Dies klassifiziert die Verwendung der Adresse, erweitert aber nicht ihre Bestandteile. Frühere Felder für Postfach, erweiterte Adresse und formatiertes Label sind in der aktuellen Ontologie ausdrücklich als veraltet markiert. Auch die früheren direkten Felder für Breiten- und Längengrad wurden zugunsten von `vcard:hasGeo` aufgegeben.

Die OWL-Klassendefinition enthält disjunktive Existenz- und Maximalitätsrestriktionen auf die fünf Kernfelder. Das ist keine geschlossene Validierungsregel: Unter der Open-World-Semantik prüft vCard weder eine vollständige Postanschrift noch eine bestimmte nationale Adressform.

### Schema.org PostalAddress

`schema:PostalAddress` ist eine Unterklasse von `schema:ContactPoint`, das wiederum von `schema:StructuredValue` erbt. Direkt für `PostalAddress` deklariert sind sieben Eigenschaften:

- `schema:addressCountry`: `schema:Country` oder Text
- `schema:addressLocality`: Text
- `schema:addressRegion`: `schema:AdministrativeArea` oder Text
- `schema:extendedAddress`: Text
- `schema:postOfficeBoxNumber`: Text
- `schema:postalCode`: Text
- `schema:streetAddress`: Text

Durch die Vererbung stehen außerdem allgemeine Kontakt- und `Thing`-Eigenschaften zur Verfügung, unter anderem `telephone`, `email`, `faxNumber`, `contactType`, `identifier`, `name` und `description`. Diese sind technisch auf `PostalAddress` anwendbar, bilden aber nicht automatisch Bestandteile einer physischen Adresse.

Schema.org legt standardmäßig keine Pflichtfelder fest und erlaubt jeder Eigenschaft mehrere Werte. Die angegebenen Domains und Ranges sind laut eigenem Datenmodell eher Nutzungsempfehlungen als strikte Regeln. Das macht das Modell robust für Webdaten, aber allein nicht ausreichend für eine verbindliche Construct-X-Validierung.

### UBL 2.5 AddressType

UBL modelliert `AddressType` als Aggregate Business Information Entity in einem XML Schema. Die Reihenfolge der folgenden Elemente ist durch `xsd:sequence` festgelegt. Auf Ebene von `AddressType` sind alle Elemente optional.

| UBL-Element | Kardinalität | Bedeutung |
| --- | --- | --- |
| `cbc:ID` | 0..1 | Adresse innerhalb eines vereinbarten Identifikationsschemas |
| `cbc:AddressTypeCode` | 0..1 | vereinbarter Code für die Adressart |
| `cbc:AddressFormatCode` | 0..1 | vereinbarter Code für das Adressformat |
| `cbc:Postbox` | 0..1 | Postfachnummer |
| `cbc:Floor` | 0..1 | Etage |
| `cbc:Room` | 0..1 | Raum, Suite oder Wohnung |
| `cbc:StreetName` | 0..n | Straßenname; Wiederholung nur für Sprachvarianten |
| `cbc:AdditionalStreetName` | 0..n | zusätzlicher Straßenname; Wiederholung nur für Sprachvarianten |
| `cbc:BlockName` | 0..1 | Name eines von Straßen umschlossenen Blocks |
| `cbc:BuildingName` | 0..1 | Gebäudename |
| `cbc:BuildingNumber` | 0..1 | Hausnummer innerhalb der Straße |
| `cbc:Description` | 0..n | erläuternde Beschreibung |
| `cbc:InhouseMail` | 0..1 | interne Zustellstelle in einem Gebäude |
| `cbc:Department` | 0..1 | Abteilung des Empfängers |
| `cbc:MarkAttention` | 0..1 | Empfängerhinweis im Sinn von „zu Händen“ |
| `cbc:MarkCare` | 0..1 | Empfängerhinweis im Sinn von „c/o“ |
| `cbc:PlotIdentification` | 0..1 | Kennung des zugehörigen Grundstücks, beispielsweise Parzellennummer |
| `cbc:CitySubdivisionName` | 0..1 | Stadtteil oder Ortsteil |
| `cbc:CityName` | 0..n | Stadt, Ort oder Dorf; Wiederholung nur für Sprachvarianten |
| `cbc:PostalZone` | 0..n | postalische Kennung wie Postleitzahl |
| `cbc:CountrySubentity` | 0..n | politische oder administrative Untereinheit als Text |
| `cbc:CountrySubentityCode` | 0..1 | politische oder administrative Untereinheit als Code |
| `cbc:Region` | 0..1 | anerkannte geografische oder wirtschaftliche Region beziehungsweise Ländergruppe |
| `cbc:District` | 0..1 | Bezirk oder geografische Unterteilung |
| `cbc:TimezoneOffset` | 0..1 | UTC-Abweichung zum Zeitpunkt des Austauschs |
| `cac:AddressLine` | 0..n | unstrukturierte Adresszeile; eine vorhandene AddressLine enthält `cbc:Line` 1..n |
| `cac:Country` | 0..1 | Land mit optionalem Identifikationscode und Namen |
| `cac:LocationCoordinate` | 0..n | geografische Koordinaten |

`LocationCoordinateType` unterstützt Koordinatensystemcode, Breiten- und Längengrad jeweils als Grad, Minuten und Richtung sowie eine Höhenangabe. Dieses Format ist detailliert, aber nicht identisch mit einer modernen Punktgeometrie aus einem Geovokabular.

UBL 2.5 verwendet denselben `AddressType` über zwölf unterschiedlich benannte globale Elemente: `Address`, `ApplicableAddress`, `ApplicableTerritoryAddress`, `DeliveryAddress`, `DespatchAddress`, `JurisdictionRegionAddress`, `LocationAddress`, `OriginAddress`, `PostalAddress`, `RegistrationAddress`, `ResidenceAddress` und `ReturnAddress`. Die fachliche Rolle entsteht damit am Verwendungsort, nicht durch zwölf verschiedene AddressType-Unterklassen.

Die UBL-2.5-Änderungshistorie hebt hervor, dass `StreetName`, `AdditionalStreetName` und `CityName` gegenüber UBL 2.4 von 0..1 auf 0..n erweitert wurden. Die Wiederholungen dienen laut Felddefinitionen den gleichen Inhalten in mehreren natürlichen Sprachen.

## 6. Kritische Mapping-Punkte

1. `region` ist kein eindeutiges gemeinsames Feld. vCard und Schema.org meinen typischerweise Staat, Provinz oder eine vergleichbare Verwaltungsebene. UBL bildet dies primär als `CountrySubentity` ab; UBL `Region` kann dagegen auch eine Wirtschaftsregion oder Ländergruppe bezeichnen.
2. `streetAddress` beziehungsweise `street-address` enthält üblicherweise Straße und Hausnummer gemeinsam. UBL `StreetName` enthält nur den Straßennamen. Ein ungeprüftes `owl:equivalentProperty` wäre deshalb falsch.
3. vCard `Home`/`Work`, Schema.org `billingAddress`/`deliveryAddress` und die UBL-Rollenelemente modellieren unterschiedliche Arten von Kontext. Ein einziges Feld „Adressart“ würde diese Bedeutungen vermischen.
4. Schema.orgs geerbte Telefon-, E-Mail- und Öffnungszeitenfelder sind Eigenschaften eines Kontaktpunkts, keine räumlichen Bestandteile der Adresse. Sie sollten nicht allein wegen der Vererbung in den Kern einer Adressontologie aufgenommen werden.
5. UBL mischt physische Ortsbestandteile mit Zustellanweisungen wie Abteilung, „zu Händen“ und „c/o“. Diese Angaben könnten in der Construct-X-Ontologie als eigene Adressierungs- oder Zustellinformation modelliert werden.
6. Eine Adresse kann zu einem Ort führen, ist aber weder mit einem Ort noch mit Koordinaten identisch. Das gilt besonders für Postfächer, Baustellenzufahrten, Grundstücke und temporäre Lieferpunkte.
7. Die drei Quellen liefern keine gemeinsame, belastbare Regel für nationale Pflichtbestandteile. Solche Regeln gehören eher in anwendungsspezifische SHACL-Profile als in die offene Kernontologie.

## 7. Ergebnisse der Fachabstimmung

Auf Grundlage der Gegenüberstellung wurden folgende Richtungsentscheidungen getroffen:

1. Die strukturierte Adresse ist die maßgebliche Repräsentation. Unstrukturierte oder geordnete Adresszeilen werden nicht als parallele Primärdaten vorgesehen.
2. Hausnummer, Gebäude, Gebäudeteil, Etage, Raum und interne Zustellstelle sollen einzeln abbildbar sein.
3. Länder und Verwaltungseinheiten werden ausschließlich als referenzierbare Ressourcen modelliert. Spätere A-Box-Graphen können diese Gebiete, ihre Codes, Namen und Hierarchien bereitstellen.
4. Die Nutzung einer Adresse wird über eine `AddressAssignment` mit einer referenzierbaren `AddressRole` modelliert. Konkrete Rollen werden als erweiterbares A-Box-Vokabular und nicht als fortlaufend zu ergänzende T-Box-Eigenschaften geführt.
5. Abteilung, „zu Händen“ und „c/o“ werden als optionale Eigenschaften der Adresszuordnung in den Kern aufgenommen. Profile können später strengere Regeln festlegen.
6. Georeferenzierung wird nicht vertieft. Die optionale Beziehung `hasGeographicPosition` wird als Erweiterungspunkt in Version 0.1.0 aufgenommen; ihr Wertebereich bleibt offen.
7. Eine formatierte Postdarstellung ist ausdrücklich keine primäre Datenquelle und wird im Konzept für Version 0.1.0 nicht als Address-Eigenschaft vorgesehen.
8. Anwendungsfallspezifische Mindestanforderungen werden erst nach Festlegung der Grundstruktur über Profile adressiert.

Die daraus abgeleiteten Klassen, Eigenschaften, Domains, Ranges und Beispiele stehen im [Konzeptmodell](concept-model.md).

## 8. Verständliches Übertragungsbeispiel

> vCard, Schema.org und UBL benennen Straße und Ort unterschiedlich. Im
> Construct-X-Modell werden diese Quellfelder auf dieselbe strukturierte
> Adresse abgebildet; Empfängerhinweise bleiben an der Adresszuordnung.
