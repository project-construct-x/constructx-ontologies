# Begriffskatalog des Address-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

## 1. Zweck

Der Katalog bietet einen kompakten Einstieg in die Begriffe der T-Box. Die
vollständigen Definitionen stehen in `ontology/conx-addr.ttl`.

## 2. Namensraum

```text
https://www.construct-x.org/ontology/address#
```

Das verwendete Präfix ist `conx-addr`.

## 3. Klassen

| Klasse | Verständliche Bedeutung |
| --- | --- |
| `Address` | strukturierte Anschrift |
| `AddressAssignment` | Zuordnung einer Adresse zu einer Ressource |
| `AddressRole` | Verwendungszweck einer Zuordnung |
| `AdministrativeTerritory` | administratives Gebiet |
| `Country` | Staat |
| `AdministrativeArea` | Verwaltungseinheit innerhalb eines Staates |

## 4. Beziehungen

`hasAddressAssignment` führt von einer beliebigen Ressource zur Zuordnung.
`assignedAddress` führt von der Zuordnung zur Adresse und `addressRole` zu den
Verwendungszwecken. `hasGeographicPosition` verbindet optional eine Adresse mit
einer extern beschriebenen Position.

## 5. Adresswerte

Zu den strukturierten Werten gehören unter anderem Straße, Hausnummer,
Postleitzahl, Ort, Postfach und Grundstückskennung. Der genaue Katalog steht im
[Konzeptmodell](concept-model.md).

## 6. Verständliches Beispiel

```turtle
ex:firma conx-addr:hasAddressAssignment ex:lieferadresse .
ex:lieferadresse
    conx-addr:assignedAddress ex:anschrift-bochum ;
    conx-addr:addressRole roles:DeliveryAddressRole .
```

In Worten: Die Firma besitzt eine Lieferadressenzuordnung; diese verweist auf
die eigentliche Anschrift in Bochum.

## 7. Nicht lokale Begriffe

Kennungen verwenden ADMS und SKOS. Konkrete Rollen und Gebiete stammen aus
separat versionierten Referenzdatensätzen.
