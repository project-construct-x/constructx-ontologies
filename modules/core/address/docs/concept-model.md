# Konzeptmodell der Construct-X Address Ontology

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

## 1. Zweck

Dieses Dokument übersetzt die Ergebnisse der Quellenanalyse und der anschließenden Fachabstimmung in das freigegebene Konzeptmodell der Version 0.1.0. Die festgeschriebenen OWL-Begriffe stehen in `ontology/conx-addr.ttl`.

Der Namespace lautet:

```text
https://www.construct-x.org/ontology/address#
```

In den Beispielen wird dafür das Präfix `conx-addr:` verwendet.

## 2. Bestätigte Modellentscheidungen

| Thema | Entscheidung |
| --- | --- |
| Repräsentation | Die strukturierte Adresse ist die maßgebliche Datenquelle. |
| Freie Adresszeilen | Keine geordnete oder unstrukturierte Adresszeilenstruktur im Kernmodell. |
| Formatierte Postanschrift | Wird nicht als primäre Datenquelle und zunächst überhaupt nicht als Eigenschaft der Version 0.1.0 vorgesehen. |
| Gebäudedetails | Hausnummer, Block, Gebäude, Gebäudeteil, Etage, Raum und interne Zustellstelle werden einzeln abbildbar. |
| Gebiete | Länder und Verwaltungseinheiten werden als referenzierbare Ressourcen modelliert, nicht als bloße Textfelder an der Adresse. |
| Referenzdaten | Rollen, 249 aktuelle ISO-3166-1-Einträge, 16 deutsche Länder nach ISO 3166-2 und 271 Gaia-X-kompatible NUTS-2-Werte werden in getrennten A-Box-Referenzvokabularen bereitgestellt. |
| Adressrollen | Rollen werden über eine `AddressAssignment` modelliert. Neue Rollen erfordern dadurch keine Änderung der zentralen T-Box. |
| Zustellhinweise | Abteilung, „zu Händen“ und „c/o“ sind als optionale Eigenschaften der Adresszuordnung im Kern enthalten. |
| Georeferenzierung | Der Kern enthält den Erweiterungspunkt `hasGeographicPosition`. Koordinaten, Geometrien und ein fester Wertebereich werden nicht selbst modelliert. |
| Gebietskennungen | Die Address Ontology definiert kein eigenes Kennungsmodell. Gebiets-A-Boxen verwenden das netzwerkweite ADMS-Profil mit `adms:Identifier` und `skos:notation`. |
| Mindestanforderungen | Verbindliche Pflichtfelder für konkrete Anwendungsfälle werden später in SHACL-Profilen definiert. |
| Kernvalidierung | Allgemeine Kardinalitäten stehen als OWL-Restrictions in der T-Box und werden durch Core SHACL Shapes als konkrete Datenprüfungen gespiegelt. |

## 3. Modellüberblick

```text
beliebige Ressource
  └─ hasAddressAssignment → AddressAssignment
                               ├─ assignedAddress → Address
                               │                    ├─ hasCountry → Country
                               │                    ├─ hasAdministrativeArea → AdministrativeArea
                               │                    └─ hasGeographicPosition → externe Geo-Ressource
                               └─ addressRole → AddressRole

AdministrativeArea
  └─ broaderAdministrativeTerritory → AdministrativeTerritory

Country und AdministrativeArea
  └─ Unterklassen von AdministrativeTerritory
```

Die Trennung ist absichtlich: `Address` beschreibt die strukturierte Anschrift. `AddressAssignment` beschreibt, wer oder was diese Adresse in welcher Rolle verwendet. `AddressRole`, `Country` und `AdministrativeArea` definieren die Typen kontrollierter Referenzressourcen, deren konkrete Instanzen außerhalb der T-Box gepflegt werden können.

## 4. Klassen

| Klasse | Definition | Verwendung |
| --- | --- | --- |
| `conx-addr:Address` | Eine strukturierte Zusammenstellung von Angaben, mit denen ein postalischer oder physischer Adressbezug beschrieben wird. | Enthält ausschließlich stabile Adressbestandteile und Verweise auf Gebietsressourcen. |
| `conx-addr:AddressAssignment` | Eine kontextbezogene Zuordnung einer Adresse zu einer anderen Ressource. | Trägt Adresse, Rolle und gegebenenfalls empfänger- oder vorgangsbezogene Zustellhinweise. |
| `conx-addr:AddressRole` | Eine kontrolliert gepflegte Rolle, in der eine Adresse innerhalb einer Zuordnung verwendet wird. | T-Box-Klasse; konkrete Rollen sind A-Box-Ressourcen, etwa Liefer- oder Baustellenadresse. |
| `conx-addr:AdministrativeTerritory` | Ein politisch oder administrativ abgegrenztes Gebiet. | Gemeinsame Oberklasse für Länder und untergeordnete Verwaltungseinheiten. Sie ist nicht als direkte Instanzklasse gedacht. |
| `conx-addr:Country` | Ein souveränes oder im verwendeten Referenzsystem als Land geführtes Gebiet. | Referenzierbare Länderressourcen, beispielsweise eine Ressource für Deutschland. |
| `conx-addr:AdministrativeArea` | Eine Verwaltungseinheit unterhalb eines Landes oder einer anderen Verwaltungseinheit. | Beispielsweise Bundesland, Provinz, Regierungsbezirk, Landkreis oder Kommune. |

Klassenhierarchie:

```text
AdministrativeTerritory
├─ Country
└─ AdministrativeArea
```

`AddressRole`, `Country` und `AdministrativeArea` sind keine fest eingebauten Listen von Individuen. Die T-Box definiert ihre Bedeutung; versionierte A-Box-Graphen stellen konkrete Rollen und Gebiete bereit.

## 5. Objekteigenschaften

| Eigenschaft                           | Domain                         | Range                               | Definition                                                                                          | Core-Kardinalität                        |
| ------------------------------------- | ------------------------------ | ----------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `conx-addr:hasAddressAssignment`      | nicht fachlich eingeschränkt   | `conx-addr:AddressAssignment`       | Verknüpft eine beliebige identifizierbare Ressource mit einer kontextbezogenen Adresszuordnung.     | 0..n                                     |
| `conx-addr:assignedAddress`           | `conx-addr:AddressAssignment`  | `conx-addr:Address`                 | Bestimmt die Adresse einer Adresszuordnung.                                                         | genau 1 je Zuordnung                     |
| `conx-addr:addressRole`               | `conx-addr:AddressAssignment`  | `conx-addr:AddressRole`             | Bestimmt eine kontrollierte fachliche Rolle der Adresse in dieser Zuordnung.                        | 1..n                                     |
| `conx-addr:hasCountry`                | `conx-addr:Address`            | `conx-addr:Country`                 | Verweist auf das Land der Adresse.                                                                  | 0..1 im Kern; Profile dürfen 1 verlangen |
| `conx-addr:hasAdministrativeArea`     | `conx-addr:Address`            | `conx-addr:AdministrativeArea`      | Verweist auf eine für die Adresse relevante Verwaltungseinheit.                                     | 0..n                                     |
| `conx-addr:broaderAdministrativeTerritory` | `conx-addr:AdministrativeArea` | `conx-addr:AdministrativeTerritory` | Verknüpft eine Verwaltungseinheit mit dem direkt übergeordneten administrativen Gebiet oder Land. | 0..1 |
| `conx-addr:hasGeographicPosition`     | `conx-addr:Address`            | vorerst nicht festgelegt            | Verknüpft die Adresse optional mit einer Position aus einem später ausgewählten externen Geomodell. | 0..n                                     |

Für `hasAddressAssignment` wird keine enge RDFS-Domain empfohlen. Dadurch kann dieselbe Struktur für Unternehmen, Personen, Baustellen, Gebäude, Lieferstellen oder andere Ressourcen verwendet werden, ohne sie durch Inferenz unbeabsichtigt einer neuen Oberklasse zuzuordnen.

Für `hasGeographicPosition` werden in Version 0.1.0 weder Koordinateneigenschaften noch ein bestimmter Wertebereich erfunden. Sobald ein geeignetes Geo-/Location-Vokabular gewählt ist, kann die Range in einem Alignment oder einer späteren Ontologieversion präzisiert werden.

## 6. Dateneigenschaften der Adresse

| Eigenschaft                       | Domain              | Range                              | Definition                                                                            | Core-Kardinalität                             |
| --------------------------------- | ------------------- | ---------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| `conx-addr:streetName`            | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Name der Straße, des Weges oder eines vergleichbaren Verkehrsraums, ohne Hausnummer.  | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:additionalStreetName`  | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Zusätzliche Straßenbezeichnung zur genaueren Bestimmung der Adresse.                  | 0..n                                          |
| `conx-addr:houseNumber`           | `conx-addr:Address` | `xsd:string`                       | Haus-, Gebäude- oder Grundstücksnummer innerhalb der Straße.                          | 0..1                                          |
| `conx-addr:blockName`             | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Name eines räumlichen Blocks oder einer vergleichbaren adressbildenden Einheit.       | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:buildingName`          | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Eigenname oder gebräuchliche Bezeichnung eines Gebäudes.                              | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:buildingPart`          | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Bezeichnung eines Gebäudeteils, beispielsweise Bauteil, Trakt, Flügel oder Halle.     | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:floor`                 | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Bezeichnung einer Etage oder Ebene innerhalb eines Gebäudes.                          | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:room`                  | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Bezeichnung eines Raums, einer Suite oder einer vergleichbaren Einheit.               | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:internalDeliveryPoint` | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Stabile interne Zustellstelle innerhalb eines Gebäudes oder Betriebsgeländes.         | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:postOfficeBoxNumber`   | `conx-addr:Address` | `xsd:string`                       | Kennung eines Postfachs.                                                              | 0..1                                          |
| `conx-addr:localityName`          | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Name der Ortschaft, Stadt, Gemeinde oder eines vergleichbaren Siedlungsgebiets.       | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:citySubdivisionName`   | `conx-addr:Address` | `xsd:string` oder `rdf:langString` | Name eines Stadt-, Orts- oder Gemeindeteils.                                          | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:postalCode`            | `conx-addr:Address` | `xsd:string`                       | Postleitzahl oder vergleichbare postalische Gebietskennung.                           | 0..1                                          |
| `conx-addr:plotIdentifier`        | `conx-addr:Address` | `xsd:string`                       | Externe Kennung eines Grundstücks oder Flurstücks, das mit der Adresse verbunden ist. | 0..n                                          |

`xsd:string` wird auch für scheinbar numerische Bestandteile verwendet. Hausnummern, Postleitzahlen, Etagen, Räume und Gebietskennungen können Buchstaben, Trennzeichen oder führende Nullen enthalten.

Eine später vorhandene Grundstücks- oder Katasterontologie kann `plotIdentifier` durch eine Objekteigenschaft zu einer Grundstücksressource ergänzen oder ablösen. Für Version 0.1.0 bleibt die Kennung als pragmatischer strukturierter Bestandteil vorgesehen.

## 7. Dateneigenschaften der Adresszuordnung

| Eigenschaft                | Domain                        | Range                              | Definition                                                                                   | Core-Kardinalität                             |
| -------------------------- | ----------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `conx-addr:departmentName` | `conx-addr:AddressAssignment` | `xsd:string` oder `rdf:langString` | Abteilung oder Organisationseinheit, für die die Adresse in dieser Zuordnung verwendet wird. | 0..n; höchstens ein Wert je Sprache empfohlen |
| `conx-addr:attentionOf`    | `conx-addr:AddressAssignment` | `xsd:string`                       | Empfängerhinweis im Sinn von „zu Händen“.                                                    | 0..n                                          |
| `conx-addr:careOf`         | `conx-addr:AddressAssignment` | `xsd:string`                       | Empfängerhinweis im Sinn von „c/o“ oder „bei“.                                               | 0..1                                          |

Diese optionalen Kerneigenschaften liegen auf der Zuordnung und nicht auf `Address`, weil dieselbe physische Anschrift für verschiedene Empfänger, Abteilungen und Rollen verwendet werden kann. Profile können später strengere Kardinalitäten oder anwendungsfallspezifische Regeln festlegen.

`attentionOf` und `careOf` bleiben in Version 0.1.0 textuelle Übergangseigenschaften. Sobald im Ontologienetzwerk ein geeignetes allgemeines Modell für Personen und Organisationen verfügbar ist, sollen ergänzende Objekteigenschaften auf die jeweiligen Akteursressourcen verweisen. Insbesondere `careOf` darf dabei nicht auf Personen beschränkt werden, weil auch eine Organisation als c/o-Stelle auftreten kann.

Zeitliche Gültigkeit einer Zuordnung ist fachlich sinnvoll, wird aber nicht mit neuen Address-Eigenschaften modelliert. Dafür soll später ein netzwerkweit einheitliches Zeitmodell wiederverwendet werden.

## 8. OWL-Restrictions und Core SHACL Shapes

Die T-Box enthält alle anwendungsfallunabhängigen Kardinalitäten als
OWL-Restrictions. `AddressAssignment` besitzt genau eine `assignedAddress`,
mindestens eine `addressRole` und höchstens einen `careOf`-Wert. `Address`
besitzt höchstens je einen Wert für `hasCountry`, `houseNumber`,
`postOfficeBoxNumber` und `postalCode`. Eine `AdministrativeArea` besitzt
höchstens ein direktes `broaderAdministrativeTerritory`. `plotIdentifier`
bleibt dagegen bewusst mehrfach verwendbar.

Die [Core SHACL Shapes](core-shapes.md) spiegeln diese Kardinalitäten und prüfen
zusätzlich die bereits durch Domain und Range beschriebene Klassenzugehörigkeit,
IRIs für Referenzressourcen sowie die Datentypen der Literale. Wegen der
Open-World-Annahme ersetzt eine OWL-Restriction keine SHACL-Validierung:
Fehlende Werte oder mehrere Objektwerte müssen in OWL nicht unmittelbar zu
einem Widerspruch führen, werden im vorliegenden Datengraphen durch SHACL aber
direkt gemeldet.

Straße, Ort, Postleitzahl oder Land werden im Core nicht allgemein
verpflichtend. Solche Mindestanforderungen gehören weiterhin in getrennte
Anwendungsprofile.

## 9. Beschreibung von Gebietsressourcen

Konkrete `Country`- und `AdministrativeArea`-Ressourcen erhalten dauerhafte IRIs. Mehrsprachige bevorzugte und alternative Namen können mit `skos:prefLabel` und `skos:altLabel` beschrieben werden.

Kennungen wie ISO-Alpha-2, ISO-Alpha-3, ISO-numerisch oder nationale Gemeindeschlüssel benötigen neben ihrem Wert auch das jeweilige Kennungssystem. Diese allgemeine Anforderung wird nicht durch neue Address-Eigenschaften gelöst. Das [netzwerkweite Kennungsprofil](../../../../docs/architecture/identifier-model.md) verwendet `adms:Identifier`, den Kennungswert in `skos:notation`, dessen Datentyp als Kennungssystem und `adms:schemaAgency` für die herausgebende Stelle. Die Address Ontology selbst bleibt dadurch frei von systemspezifischen Kennungseigenschaften.

## 10. Kontrollierte Adressrollen

Die zentrale T-Box definiert nur `AddressRole` und `addressRole`. Konkrete Rollen werden als Individuen im getrennten kontrollierten Vokabular `https://www.construct-x.org/vocab/address-role` geführt. Version `0.2.0` enthält folgende Rollen:

| Rollenressource | Bedeutung |
| --- | --- |
| `roles:DeliveryAddressRole` | Adresse, an die Güter oder Materialien geliefert werden. |
| `roles:InvoiceAddressRole` | Adresse, die für Rechnungen verwendet wird. |
| `roles:PostalAddressRole` | Allgemeine postalische Korrespondenzadresse. |
| `roles:RegistrationAddressRole` | In einem Register geführte Adresse. |
| `roles:ReturnAddressRole` | Adresse für Rücksendungen. |
| `roles:ResidenceAddressRole` | Wohnadresse einer Person. Der englische Name folgt UBL `cac:ResidenceAddress`. |
| `roles:ConstructionSiteAddressRole` | Allgemeine Adresse einer Baustelle. |
| `roles:ConstructionSiteAccessRole` | Adresse oder Adressbezug einer bestimmten Baustellenzufahrt. |
| `roles:LegalAddressRole` | Rechtlich maßgebliche Adresse einer Person oder Organisation. |
| `roles:HeadquartersAddressRole` | Adresse des Hauptsitzes einer Organisation. |
| `roles:PhysicalLocationAddressRole` | Adresse des physischen Standorts einer Ressource. |

Die Liste ist ausdrücklich keine T-Box-Aufzählung. Eine neue Rolle wird als neue A-Box-Ressource ergänzt. Die zentrale Ontologie muss nur geändert werden, wenn eine neue Rolle zusätzliche Struktur oder neue allgemeine Semantik erfordert. Die vollständigen zweisprachigen Definitionen, Notationen und UBL-Herkunftshinweise stehen in der [Dokumentation des Adressrollen-Vokabulars](address-roles.md).

Eine `AddressAssignment` besitzt mindestens eine und darf mehrere Rollen enthalten. Alle weiteren Angaben der Zuordnung gelten gemeinsam für sämtliche verknüpften Rollen. Unterscheiden sich beispielsweise Abteilung, Zustellhinweis oder spätere Gültigkeit je Rolle, werden getrennte Zuordnungen für dieselbe Adresse angelegt.

## 11. Konzeptionelle Beispielinstanzen

Die folgenden Turtle-Ausschnitte erläutern das Modell. Eine ausführbare Beispielinstanz liegt zusätzlich in `examples/rub-address.ttl`. Die verwendeten `roles:`, `countries:`- und `areas:`-Ressourcen sind in getrennten Referenzdatensätzen umgesetzt.

### Lieferadresse eines Unternehmens

```turtle
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix ex: <https://example.org/id/> .
@prefix roles: <https://www.construct-x.org/vocab/address-role#> .
@prefix areas: <https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#> .

ex:company-17
    conx-addr:hasAddressAssignment ex:company-17-delivery-address .

ex:company-17-delivery-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:address-4711 ;
    conx-addr:addressRole roles:DeliveryAddressRole ;
    conx-addr:departmentName "Wareneingang"@de ;
    conx-addr:attentionOf "Schichtleitung" .

ex:address-4711
    a conx-addr:Address ;
    conx-addr:streetName "Musterstraße"@de ;
    conx-addr:houseNumber "12a" ;
    conx-addr:buildingName "Logistikzentrum West"@de ;
    conx-addr:buildingPart "Halle 3"@de ;
    conx-addr:floor "Erdgeschoss"@de ;
    conx-addr:room "Warenannahme"@de ;
    conx-addr:internalDeliveryPoint "Tor 4"@de ;
    conx-addr:postalCode "44137" ;
    conx-addr:localityName "Dortmund"@de ;
    conx-addr:hasAdministrativeArea areas:DE-NW-Dortmund ;
    conx-addr:hasCountry areas:DE .
```

Aus diesen strukturierten Angaben darf eine Anwendung eine Postdarstellung erzeugen. Eine solche Zeichenkette ist jedoch kein Bestandteil dieses Beispiels und keine alternative Quelle für die semantischen Werte.

### Dieselbe Adresse in mehreren Rollen

```turtle
ex:company-17
    conx-addr:hasAddressAssignment
        ex:company-17-general-address,
        ex:company-17-invoice-address .

ex:company-17-general-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:address-4711 ;
    conx-addr:addressRole roles:PostalAddressRole,
                          roles:RegistrationAddressRole .

ex:company-17-invoice-address
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:address-4711 ;
    conx-addr:addressRole roles:InvoiceAddressRole ;
    conx-addr:departmentName "Buchhaltung"@de .
```

Die allgemeine Zuordnung darf mehrere Rollen tragen, weil keine weiteren Angaben zwischen ihnen unterschieden werden müssen. Für die Rechnungsrolle wird eine getrennte Zuordnung verwendet, da `departmentName` nur für diese Rolle gilt. Die Adresse selbst wird nicht als `PostalAddress`, `RegistrationAddress` oder `InvoiceAddress` klassifiziert.

### Referenzierbare Gebiete als A-Box

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix areas: <https://www.construct-x.org/vocab/administrative-area/iso-3166-2-de#> .
@prefix countries: <https://www.construct-x.org/vocab/country#> .
@prefix id-scheme: <https://www.construct-x.org/vocab/identifier-scheme#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

countries:DEU
    a conx-addr:Country, skos:Concept ;
    skos:prefLabel "Deutschland"@de,
                   "Germany"@en ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2
    ] .

areas:DE-NW
    a conx-addr:AdministrativeArea, skos:Concept ;
    skos:prefLabel "Land Nordrhein-Westfalen"@de ;
    conx-addr:broaderAdministrativeTerritory countries:DEU ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DE-NW"^^id-scheme:iso-3166-2
    ] .
```

Städte werden bewusst nicht in dieser ersten Gebiets-A-Box geführt. Der strukturierte Ortsname steht weiterhin mit `localityName` an der Adresse. Hintergründe und ein vollständiges Verwendungsbeispiel stehen in der [Dokumentation der Gebietsreferenzen](administrative-territories.md).

### Rollen als A-Box-Vokabular

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://www.construct-x.org/vocab/address-role>
    a owl:Ontology, skos:ConceptScheme ;
    owl:versionIRI <https://www.construct-x.org/vocab/address-role/0.2.0> ;
    owl:versionInfo "0.1.0" ;
    skos:prefLabel "Construct-X address roles"@en,
                   "Construct-X Adressrollen"@de .

roles:DeliveryAddressRole
    a conx-addr:AddressRole, skos:Concept ;
    skos:inScheme <https://www.construct-x.org/vocab/address-role> ;
    skos:notation "delivery" ;
    skos:prefLabel "Lieferadresse"@de,
                   "Delivery address"@en .
```

## 12. Kompetenzfragen

Das Modell soll nach seiner Umsetzung mindestens folgende Fragen beantworten können:

1. Welche Adresszuordnungen besitzt eine bestimmte Ressource?
2. Welche strukturierte Adresse wird in einer bestimmten Zuordnung verwendet?
3. In welcher Rolle wird die Adresse verwendet?
4. Verwendet dieselbe Ressource dieselbe Adresse in mehreren Rollen?
5. Welche Abteilung, Person oder c/o-Stelle gehört zu einer konkreten Adresszuordnung?
6. Wie lauten Straße, Hausnummer, Gebäude, Gebäudeteil, Etage, Raum und interne Zustellstelle getrennt voneinander?
7. In welchem Land und in welcher Verwaltungseinheit liegt die Adresse?
8. Welche übergeordneten Verwaltungseinheiten gehören zu dieser Verwaltungseinheit?
9. Welche mehrsprachigen Bezeichnungen besitzt ein referenziertes Gebiet?
10. Ist eine externe geografische Position mit der Adresse verknüpft, ohne die Adresse mit der Position gleichzusetzen?

## 13. Bewusst ausgeschlossene Konzepte

Für Version 0.1.0 sind im aktuellen Entwurf nicht vorgesehen:

- `formattedAddress`, `addressLabel` oder eine vergleichbare formatierte Postanschrift,
- unstrukturierte oder geordnete Adresszeilen als alternative Primärrepräsentation,
- eigene Eigenschaften für Längen-, Breiten- oder Höhenkoordinaten,
- Telefon, E-Mail, Fax oder Öffnungszeiten als Bestandteile einer Adresse,
- fest in der T-Box codierte Liefer-, Rechnungs-, Baustellen- oder andere Rollenklassen,
- Text-Fallbacks für Land und Verwaltungseinheiten,
- nationale Pflichtfeldregeln in der offenen Kernontologie.

Alignments zu vCard, Schema.org und UBL dürfen später Transformationsregeln für unstrukturierte Quellfelder dokumentieren. Solche Quellfelder werden dadurch nicht zu gleichbedeutenden Eigenschaften des strukturierten Construct-X-Kerns.

## 14. Freigabestatus

Alle acht Modellpunkte wurden für Version 0.1.0 entschieden:

1. Die sechs Klassen einschließlich `AdministrativeTerritory` sind bestätigt.
2. Jede `AddressAssignment` besitzt genau eine Adresse und mindestens eine, gegebenenfalls mehrere Rollen.
3. `departmentName`, `attentionOf` und `careOf` sind optionale Eigenschaften des Kerns.
4. `blockName`, `additionalStreetName` und `plotIdentifier` sind Bestandteil der ersten T-Box.
5. `plotIdentifier` wird zunächst als Literal geführt und kann später durch eine Verknüpfung zu einem Grundstücksmodell ergänzt werden.
6. Die Address Ontology definiert kein eigenes Kennungsmodell; Gebiets-A-Boxen verwenden das netzwerkweite ADMS-Kennungsprofil.
7. `hasGeographicPosition` ist ohne festen Wertebereich Bestandteil der Version 0.1.0.
8. Die englischen lokalen Namen sind bestätigt; `broaderAdministrativeTerritory` ersetzt den vorläufigen Namen `broaderAdministrativeArea`.

Die T-Box 0.1.0 setzt diese Entscheidungen um. Rollen, ISO-3166-1-Länder, deutsche ISO-3166-2-Länder und NUTS-2-Regionen liegen als getrennte, eigenständig versionierte Referenzvokabulare vor. Das allgemeine Kennungsmuster ist als ADMS-Profil dokumentiert. Das Gaia-X-Alignment bleibt ein optionales Modul und erzeugt keine Abhängigkeit der Core-T-Box.
