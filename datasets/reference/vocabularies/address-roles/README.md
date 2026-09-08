# Construct-X Address Roles

Dieses Verzeichnis enthält das kontrollierte Adressrollen-Vokabular für die Construct-X Address Ontology. Es ist als A-Box-Referenzdatensatz von der T-Box unter `modules/core/address/ontology/conx-addr.ttl` getrennt.

## Kennung und Version

```text
Vokabular-IRI: https://www.construct-x.org/vocab/address-role
Versions-IRI:  https://www.construct-x.org/vocab/address-role/0.2.0
Namespace:     https://www.construct-x.org/vocab/address-role#
Prefix:        roles
Version:       0.2.0
Status:        draft
```

Die stabile Vokabular-IRI identifiziert das `skos:ConceptScheme`. Jede konkrete Rolle besitzt eine dauerhafte IRI im Rollen-Namespace und ist zugleich Instanz von `conx-addr:AddressRole` und `skos:Concept`.

## Inhalt

Version `0.2.0` enthält elf Rollen:

- Lieferadresse
- Rechnungsadresse
- Postanschrift
- Registrierungsadresse mit dem alternativen Label Meldeadresse
- Rücksendeadresse
- Wohnadresse
- Baustellenadresse
- Baustellenzufahrtsadresse
- rechtliche Adresse
- Hauptsitzadresse
- physische Standortadresse

Bezeichnungen, Definitionen und stabile Notationen stehen direkt in `address-roles.ttl`. Neue Rollen werden in diesem Referenzvokabular ergänzt und erfordern keine Änderung der Address-T-Box.

## UBL-Orientierung

Die englischen Vorzugsbezeichnungen für Delivery, Postal, Registration, Residence und Return sind an die gleichnamigen Address-Elemente aus OASIS UBL 2.5 CS01 angelehnt. UBL beschreibt `cac:RegistrationAddress` sowohl im Kontext der Unternehmensregistrierung als auch der steuerlichen Registrierung; das Construct-X-Konzept fasst diese Verwendungen als allgemeine Registrierungsrolle zusammen.

Für `InvoiceAddressRole`, `ConstructionSiteAddressRole` und `ConstructionSiteAccessRole` wurde in UBL 2.5 kein direkter CAC-Adressbegriff identifiziert. Diese Rollen sind daher als Construct-X-eigene Begriffe dokumentiert. Die Rollen `LegalAddressRole`, `HeadquartersAddressRole` und `PhysicalLocationAddressRole` orientieren sich an Gaia-X. Insbesondere wird keine Gleichheit zu einem lediglich ähnlich verwendeten UBL-Element behauptet.

UBL 2.5 enthält zusätzlich `cac:DespatchAddress` mit der Definition einer Versand- beziehungsweise Abholadresse. Eine entsprechende Construct-X-Rolle ist nicht Bestandteil von Version `0.1.0` und kann nach fachlicher Entscheidung additiv ergänzt werden.

Quelle: [OASIS UBL 2.5 CS01 Common Aggregate Components](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/xsd/common/UBL-CommonAggregateComponents-2.5.xsd)

## Verwendung

```turtle
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix ex: <https://example.org/id/> .
@prefix roles: <https://www.construct-x.org/vocab/address-role#> .

ex:site-access-assignment
    a conx-addr:AddressAssignment ;
    conx-addr:assignedAddress ex:gate-3-address ;
    conx-addr:addressRole roles:ConstructionSiteAccessRole,
                          roles:DeliveryAddressRole .
```

Alle weiteren Angaben einer `AddressAssignment` gelten gemeinsam für sämtliche mit ihr verknüpften Rollen. Sobald sich beispielsweise Abteilung, Zustellhinweis oder Gültigkeit je Rolle unterscheiden, werden getrennte Zuordnungen zur selben Adresse verwendet.

## Pflege

- Notationen und IRIs werden nicht für andere Bedeutungen wiederverwendet.
- Entfernte Rollen werden als veraltet gekennzeichnet, nicht stillschweigend gelöscht.
- Neue Rollen benötigen deutsche und englische Vorzugsbezeichnungen und Definitionen.
- Direkte UBL-Bezüge werden nur dokumentiert, wenn ein entsprechender UBL-Begriff tatsächlich vorhanden ist.

