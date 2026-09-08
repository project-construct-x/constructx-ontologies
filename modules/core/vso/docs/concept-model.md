# Konzeptmodell des VSO-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Zweck

Das Konzeptmodell beschreibt die systemneutrale Zuweisung eines Merkmals und
seines Wertes zu einer Ressource.

## 2. Modell in einfachen Worten

Eine `AssignedProperty` ist nicht die allgemeine Merkmalsdefinition, sondern
deren konkrete Zuweisung zu genau einer Ressource.

## 3. Begriffe

| Begriff | Bedeutung |
| --- | --- |
| `AssignedProperty` | konkrete Merkmalszuweisung |
| `PropertyState` | Zustand mit dem gespeicherten Wert |
| `hasPropertyReference` | Verweis auf die Merkmalsdefinition |
| `hasUsedUnit` | optionale QUDT-Einheit |

## 4. Beziehungen

```text
Ressource
  -> hasProperty
       -> AssignedProperty
            -> hasPropertyReference: genau eine Definition
            -> hasPropertyState: genau ein PropertyState
                 -> schema:value: genau ein Wert
                 -> hasUsedUnit: optional eine Einheit
```

## 5. Verständliches Beispiel

> Zwei Wände können dieselbe Definition „Höhe“ verwenden, besitzen aber je
> eine eigene Zuweisung und dadurch unterschiedliche Werte.

## 6. Abgrenzung

Der Core lässt Ressourcentyp, Merkmalsvokabular und Wertdatentyp offen.

## 7. Entscheidungen

OPM-, QUDT- und Schema.org-Begriffe werden wiederverwendet. ISOProps-Regeln
gehören ausschließlich in das separate Profil.
