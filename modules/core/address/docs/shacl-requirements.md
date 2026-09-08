# Fachliche SHACL-Anforderungen des Address-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Address Core Shapes

## 1. Zweck

Die Core Shapes prüfen, ob eine Adresszuordnung technisch vollständig und eine
Adresse strukturell korrekt beschrieben ist.

## 2. Shape-Set

Der ausführbare Graph liegt unter `shapes/conx-addr-core.shacl.ttl` und besitzt
die stabile IRI `https://www.construct-x.org/shapes/address/core`.

## 3. Kernanforderungen

- Eine `AddressAssignment` verweist auf genau eine `Address`.
- Eine `AddressAssignment` besitzt mindestens eine `AddressRole`.
- Datums- und Textwerte müssen die vorgesehenen Datentypen besitzen.
- referenzierte Gebietsressourcen müssen passend typisiert sein.

## 4. Fehlerverhalten

Eine verletzte Kernanforderung erzeugt eine `sh:Violation`. Zusätzliche
fachliche Pflichtfelder gehören in strengere Profile.

## 5. Gültiges Beispiel

> Eine Lieferadressenzuordnung besitzt eine Adresse und die Rolle
> „Lieferadresse“. Das ist im Core gültig, auch wenn ein Fachprofil später
> weitere Pflichtfelder verlangt.

## 6. Ungültiges Beispiel

> Eine Zuordnung ohne verknüpfte Adresse ist ungültig, weil nicht erkennbar ist,
> welche Anschrift verwendet werden soll.

## 7. Bewusst nicht geprüft

Der Core erzwingt keine universelle Postleitzahl, keine formatierte Anschrift
und keine länderspezifische Syntax.

## 8. Tests

Gültige und ungültige Testgraphen liegen unter `tests/valid` und
`tests/invalid`. Weitere Erläuterungen enthält die
[Core-Shape-Dokumentation](core-shapes.md).
