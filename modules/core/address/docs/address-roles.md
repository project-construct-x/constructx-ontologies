# Kontrolliertes Adressrollen-Vokabular

Die Construct-X Address Ontology definiert mit `conx-addr:AddressRole` nur den Typ einer Adressrolle. Die konkreten Rollen werden getrennt als versioniertes SKOS-Referenzvokabular gepflegt:

```text
Vokabular-IRI: https://www.construct-x.org/vocab/address-role
Versions-IRI:  https://www.construct-x.org/vocab/address-role/0.2.0
Namespace:     https://www.construct-x.org/vocab/address-role#
Prefix:        roles
Version:       0.2.0
```

Quelldatei: [`datasets/reference/vocabularies/address-roles/address-roles.ttl`](../../../../datasets/reference/vocabularies/address-roles/address-roles.ttl)

## Rollen in Version 0.2.0

| Rollenressource | Deutsch | Englisch | Notation | Herkunft |
| --- | --- | --- | --- | --- |
| `roles:DeliveryAddressRole` | Lieferadresse | Delivery address | `delivery` | `cac:DeliveryAddress` |
| `roles:InvoiceAddressRole` | Rechnungsadresse | Invoice address | `invoice` | kein direkter CAC-Begriff |
| `roles:PostalAddressRole` | Postanschrift | Postal address | `postal` | `cac:PostalAddress` |
| `roles:RegistrationAddressRole` | Registrierungsadresse; alternativ Meldeadresse | Registration address | `registration` | `cac:RegistrationAddress` |
| `roles:ReturnAddressRole` | Rücksendeadresse | Return address | `return` | `cac:ReturnAddress` |
| `roles:ResidenceAddressRole` | Wohnadresse | Residence address | `residence` | `cac:ResidenceAddress` |
| `roles:ConstructionSiteAddressRole` | Baustellenadresse | Construction site address | `construction-site` | kein direkter CAC-Begriff |
| `roles:ConstructionSiteAccessRole` | Baustellenzufahrtsadresse | Construction site access address | `construction-site-access` | kein direkter CAC-Begriff |
| `roles:LegalAddressRole` | Rechtliche Adresse | Legal address | `legal` | Gaia-X `legalAddress` |
| `roles:HeadquartersAddressRole` | Hauptsitzadresse | Headquarters address | `headquarters` | Gaia-X `headquartersAddress` |
| `roles:PhysicalLocationAddressRole` | Physische Standortadresse | Physical location address | `physical-location` | Gaia-X `location` |

## UBL-Abgrenzung

Die englischen Bezeichnungen der fünf direkt zuordenbaren Rollen folgen der Terminologie von OASIS UBL 2.5 CS01. Der Bezug ist eine terminologische und fachliche Orientierung, keine formale Äquivalenzaussage zwischen einem SKOS-Konzept und einem XML-Schemaelement.

UBL verwendet `cac:RegistrationAddress` für die registrierte Adresse einer juristischen Person sowie für die steuerlich registrierte Adresse einer Partei. `roles:RegistrationAddressRole` fasst diese Kontexte als allgemeine Registrierungsrolle zusammen. Das deutsche alternative Label „Meldeadresse“ erleichtert die Verwendung für behördlich geführte Adressen, ohne Wohnadresse und registrierte Adresse gleichzusetzen.

UBL besitzt kein eigenständiges Element `cac:InvoiceAddress`. Rechnungsparteien und ihre Anschriften werden im UBL-Modell über ihren jeweiligen Kontext abgebildet. Deshalb bleibt `roles:InvoiceAddressRole` ein Construct-X-eigener Begriff. Gleiches gilt für die beiden bauspezifischen Rollen.

UBL 2.5 kennt außerdem `cac:DespatchAddress` als Adresse des Versands beziehungsweise der Abholung. Diese Rolle wurde nicht ungefragt in die freigegebene Startmenge aufgenommen und bleibt ein dokumentierter Erweiterungskandidat.

## Gaia-X-Orientierung

Die drei in Version `0.2.0` ergänzten Rollen bilden die Adressverwendungen aus
Gaia-X ab. `LegalAddressRole` bleibt bewusst von `RegistrationAddressRole`
getrennt, weil eine rechtlich maßgebliche Adresse nicht in jedem Rechts- und
Anwendungskontext mit einer Registeradresse identisch ist. Ein optionales
Gaia-X-Alignment gehört nicht zum Umfang dieses Core-only-Repositorys.

## Modellierungsregeln

Jede Rolle ist zugleich `conx-addr:AddressRole` und `skos:Concept`. Eine `AddressAssignment` kann mehrere Rollen tragen, wenn alle weiteren Angaben der Zuordnung gemeinsam für diese Rollen gelten. Unterscheiden sich Abteilung, Empfängerhinweis oder Gültigkeit, werden mehrere Zuordnungen zur selben Adresse angelegt.

Das offene Kernmodell erlaubt auch Rollen aus anderen kontrollierten Vokabularen. Ein strenges SHACL-Profil kann später verlangen, dass verwendete Rollen zum Construct-X-Konzeptschema `https://www.construct-x.org/vocab/address-role` gehören.
