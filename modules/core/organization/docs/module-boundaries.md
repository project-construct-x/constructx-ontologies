# Modulgrenzen des Organization-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`

## 1. Zweck

Die Modulgrenzen trennen Organisationsstammdaten von Kontakten, Adressen,
Personen, Prozessrollen und externen Nachweisen.

## 2. Zuständigkeiten

| Thema | Zuständiges Modul |
| --- | --- |
| Organisation, Legal Entity und Organisationseinheit | `core/organization` |
| natürliche Person | `core/person` |
| allgemeiner Akteur | `core/agent` |
| Adresse und Adressrolle | `core/address` |
| Kontaktpunkt und Kontaktmethode | `core/contact` |
| fachübergreifende Prozessrolle | `core/participation` |
| Struktur einer Kennung | `core/identifier` |

## 3. Abhängigkeiten

Organization spezialisiert Agent und verwendet die Verträge aus Person,
Address, Contact und Identifier. Die externen Begriffe werden referenziert und
nicht in der Organisationsontologie neu definiert.

## 4. Bewusste Ausschlüsse

Standorte, Bankkonten, Credentials, Versicherungen und fachliche Projektrollen
gehören nicht in den Organization Core.

## 5. Verständliches Beispiel

> Eine GmbH hat einen rechtlichen Namen, eine Registerkennung, eine
> Geschäftsadresse und einen Rechnungskontakt. Nur Name, Registerdatum und
> Organisationsstruktur gehören unmittelbar zum Organization-Modul.

```text
LegalEntity
  +-> Identifier      aus core/identifier
  +-> Address         über core/address
  +-> ContactPoint    über core/contact
```

## 6. Integrationsregel

Neue Beziehungen werden dort definiert, wo ihre fachliche Bedeutung liegt.
Organization kopiert keine Properties anderer Core-Module.
