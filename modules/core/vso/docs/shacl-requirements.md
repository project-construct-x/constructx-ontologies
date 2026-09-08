# Fachliche SHACL-Anforderungen des VSO-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** VSO Core Shapes

## 1. Zweck

Die Core Shapes prüfen den systemneutralen Vertrag für Merkmalszuweisungen.

## 2. Shape-Set

Der Graph liegt unter `shapes/conx-vso-core.shacl.ttl` und besitzt die IRI
`https://www.construct-x.org/shapes/vso/core`.

## 3. Kernanforderungen

| ID | Anforderung |
| --- | --- |
| `VSO-LINK-001` | `hasProperty` verweist auf eine gültige Zuweisung |
| `VSO-ASSIGN-001` | jede Zuweisung gehört genau einer Ressource |
| `VSO-ASSIGN-010` | genau eine Merkmalsreferenz als IRI |
| `VSO-ASSIGN-020` | genau ein PropertyState |
| `VSO-STATE-010` | genau ein `schema:value` |
| `VSO-STATE-020` | höchstens eine QUDT-Einheit als IRI |

## 4. Fehlerverhalten

Jede Verletzung erzeugt den stabilen Code der betreffenden Regel.

## 5. Gültiges Beispiel

> Eine Wand besitzt genau eine Höhenzuweisung mit einem Zustand und dem Wert
> 2,80 Meter.

## 6. Ungültiges Beispiel

> Eine Merkmalszuweisung mit zwei Zuständen ist ungültig, weil der Core genau
> einen aktuellen Zustandsknoten erwartet.

## 7. Bewusst nicht geprüft

Ressourcenklasse, Merkmalsvokabular, Wertdatentyp und Pflicht einer Einheit
bleiben offen.

## 8. Tests

Die Testgraphen unter `tests/valid` und `tests/invalid` decken alle stabilen
Fehlercodes ab.
