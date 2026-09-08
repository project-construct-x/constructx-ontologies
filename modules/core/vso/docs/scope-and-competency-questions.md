# Scope und Kompetenzfragen des VSO-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Zweck

VSO beschreibt, wie ein Merkmal mit einem konkreten Wert an eine Ressource
gebunden wird.

## 2. Bestätigter Scope

- Merkmalszuweisung zu genau einer Ressource,
- Referenz auf genau eine Merkmalsdefinition,
- genau ein Zustandsobjekt mit genau einem Wert,
- optionale Maßeinheit.

## 3. Nicht im Scope

VSO definiert keine fachlichen Merkmalskataloge und keine verpflichtenden
Datentypen. ISOProps-spezifische Regeln liegen in einem separaten Profil.

## 4. Kompetenzfragen

1. Welches Merkmal wurde einer Ressource zugewiesen?
2. Welchen aktuellen Wert besitzt es?
3. Welche Einheit wird verwendet?
4. Zu welcher Ressource gehört die Zuweisung?

## 5. Verständliches Beispiel

> Eine Wand besitzt das Merkmal „Höhe“. Der gespeicherte Wert ist 2,80 und die
> verwendete Einheit ist Meter.

```text
Wand -> Merkmalszuweisung „Höhe“ -> Zustand -> 2,80 m
```

## 6. Modellentscheidungen

Die Merkmalsdefinition und ihre konkrete Zuweisung bleiben getrennt. Dadurch
kann dieselbe Definition für viele Ressourcen verwendet werden.

## 7. Abnahmekriterien

Zuweisung, Referenz, Zustand und Wert sind eindeutig verbunden; eine Einheit
ist optional.
