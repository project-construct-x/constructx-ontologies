# Fachliche SHACL-Anforderungen des Identifier-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Identifier Core Shapes

## 1. Zweck

Das Shape stellt einen einzigen wiederverwendbaren Minimalvertrag für
Identifier-Ressourcen bereit.

## 2. Shape-Set

`conx-id-sh:ADMSIdentifierShape` liegt im Shape-Graph
`https://www.construct-x.org/shapes/identifier/core`.

## 3. Kernanforderungen

- Typ `adms:Identifier`,
- Blank Node oder IRI,
- genau eine literale `skos:notation`,
- höchstens eine `adms:schemaAgency` als String.

## 4. Fehlerverhalten

Die stabilen Fehlercodes `ID-001` bis `ID-003` unterscheiden Typisierung,
Notation und Schema-Agentur.

## 5. Gültiges Beispiel

Eine korrekt typisierte Kennung mit genau einer Notation ist gültig; die
Schema-Agentur darf fehlen.

## 6. Ungültiges Beispiel

> Eine Identifier-Ressource mit zwei Notationen ist ungültig, weil nicht klar
> ist, welcher Wert die Kennung darstellt.

## 7. Bewusst nicht geprüft

Das Shape prüft weder fachliche Pflichtkennungen noch eine Positivliste von
Kennungssystemen.

## 8. Tests

Die Testgraphen unter `tests/valid` und `tests/invalid` decken alle drei
Regelgruppen ab.
