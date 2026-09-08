# Konzeptmodell des Contact-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/contact`

## 1. Zweck

Das Modell trennt eine Kontaktstelle von den konkreten Wegen, über die sie
erreichbar ist.

## 2. Modell in einfachen Worten

Ein `ContactPoint` beschreibt den Nutzungskontext, beispielsweise „geschäftlich
für Rechnungen“. Eine `ContactMethod` enthält genau einen Kanal wie E-Mail,
Telefon oder Website.

## 3. Begriffe

| Begriff | Bedeutung |
| --- | --- |
| `ContactPoint` | gebündelte Kontaktstelle für einen Kontext |
| `ContactMethod` | einzelner Kontaktweg |
| `ContactChannel` | Art des Kontaktwegs |
| `ContactUsage` | privat, geschäftlich oder offiziell |
| `ContactPurpose` | beispielsweise Rechnung, Lieferung oder Support |

## 4. Beziehungen

Ein kontaktierbarer Träger verweist mit `hasContactPoint` auf einen
Kontaktpunkt. Dieser bündelt eine oder mehrere Kontaktmethoden.

## 5. Verständliches Beispiel

> Die Buchhaltung einer Firma ist geschäftlich für Rechnungen erreichbar. Sie
> besitzt eine E-Mail-Adresse und eine Telefonnummer.

```text
Firma -> ContactPoint „Buchhaltung“
           +-> E-Mail
           +-> Telefon
```

## 6. Abgrenzung

Postalische Adressbestandteile werden nicht kopiert. Eine postalische
Kontaktmethode verweist auf `core/address`.

## 7. Entscheidungen

Kontaktkanal, Nutzung und Zweck sind getrennte kontrollierte Werte. Strenge
Syntaxprüfungen bleiben Fachprofilen vorbehalten.

Das ausführliche Diagramm steht unter
[contact-concept-model.md](diagrams/contact-concept-model.md).
