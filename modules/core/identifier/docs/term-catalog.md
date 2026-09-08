# Begriffskatalog des Identifier-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Zweck

Der Katalog dokumentiert die direkt wiederverwendeten Begriffe.

## 2. Namensräume

Der Shape-Namensraum lautet
`https://www.construct-x.org/shapes/identifier/core#`. Die fachlichen Begriffe
stammen aus ADMS und SKOS.

## 3. Klassen

Das Modul verwendet `adms:Identifier` und definiert keine lokale Klasse.

## 4. Properties

| Property | Bedeutung |
| --- | --- |
| `adms:identifier` | verbindet eine Ressource mit einer Kennung |
| `skos:notation` | enthält den Kennungswert |
| `adms:schemaAgency` | nennt optional die herausgebende Stelle |

## 5. Kontrollierte Werte

Kennungssysteme können durch Datentyp-IRIs aus dem getrennten
Identifier-Scheme-Vokabular bezeichnet werden.

## 6. Verständliches Beispiel

`"DE"^^id-scheme:iso-3166-1-alpha-2` bedeutet nicht nur den Text „DE“, sondern
ausdrücklich einen Alpha-2-Ländercode.

## 7. Ausschlüsse

Das Modul besitzt keine lokalen fachlichen Kennungstypen und keine Liste
zulässiger Kennungen je Fachklasse.
