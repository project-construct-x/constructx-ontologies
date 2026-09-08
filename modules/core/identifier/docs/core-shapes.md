# Identifier Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Identifier Core Shapes

## 1. Zweck

Der Shape-Graph `https://www.construct-x.org/shapes/identifier/core` stellt das
wiederverwendbare `conx-id-sh:ADMSIdentifierShape` bereit.

## 2. Geprüfter Vertrag

Das Shape verlangt eine `adms:Identifier`-Ressource mit genau einer literalen
`skos:notation`. `adms:schemaAgency` bleibt optional und ist auf höchstens
einen `xsd:string` begrenzt.

## 3. Wiederverwendung

Konsumierende Core-Module importieren den versionierten Shape-Graph und binden
`conx-id-sh:ADMSIdentifierShape` über ihre lokalen `adms:identifier`-
Property-Shapes ein. Dadurch bleiben fachliche Kardinalitäten lokal, während
die Struktur einer Kennung nur einmal definiert wird.

## 4. Verständliches Beispiel

> Die Kennung „HRB 1234“ ist gültig, wenn sie als `adms:Identifier` genau eine
> `skos:notation` besitzt. Ob eine Organisation eine solche Registerkennung
> haben muss, entscheidet das Organization-Shape.

## 5. Tests

Gültige und ungültige Beispiele liegen unter `tests/valid` und
`tests/invalid`.

## 6. Bewusst nicht geprüft

Das Core Shape erzwingt weder ein konkretes Kennungssystem noch eine
Pflichtkennung für eine bestimmte Fachklasse.
