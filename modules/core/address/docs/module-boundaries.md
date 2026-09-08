# Modulgrenzen des Address-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

## 1. Zweck

Dieses Dokument erklärt, welche Aussagen das Address-Modul besitzt und wann
ein anderes Core-Modul zuständig ist.

## 2. Zuständigkeiten

| Thema | Zuständiges Modul |
| --- | --- |
| Straße, Postleitzahl, Ort und Land | `core/address` |
| E-Mail, Telefon und postalischer Kontaktkanal | `core/contact` |
| Person und Organisation | `core/person`, `core/organization` |
| Koordinaten und räumliche Referenzsysteme | externes Geo-/Location-Modell |
| fachliche Kennungsstruktur | `core/identifier` |

## 3. Abhängigkeiten

Das Address-Modul referenziert SKOS, ADMS und externe Adressquellen, übernimmt
deren Modelle aber nicht vollständig. Adressrollen und Gebietslisten werden als
getrennte Referenzdaten gepflegt.

## 4. Bewusste Ausschlüsse

Das Modul definiert keine Kontaktstelle, keine Organisation und kein eigenes
Koordinatensystem. `hasGeographicPosition` ist ausschließlich der Anschluss an
ein dafür zuständiges Modell.

## 5. Verständliches Beispiel

> Eine postalische Kontaktmethode verweist auf eine Adresszuordnung. Dadurch
> bleiben E-Mail und Telefon im Contact-Modul, während Straße und Ort im
> Address-Modul gepflegt werden.

```text
ContactMethod -> AddressAssignment -> Address
```

## 6. Integrationsregel

Andere Module verwenden `hasAddressAssignment`; sie kopieren keine lokalen
Properties für Straße, Ort oder Adressrolle.
