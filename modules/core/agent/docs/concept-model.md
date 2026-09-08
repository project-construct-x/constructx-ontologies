# Konzeptmodell des Agent-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Das Konzeptmodell zeigt den kleinsten gemeinsamen Nenner für handelnde oder
verantwortliche Entitäten.

## 2. Modell in einfachen Worten

Ein Agent ist ein allgemeiner Akteur. Person und Organization sind genauere
Arten dieses Akteurs.

## 3. Begriffe

| Begriff | Bedeutung |
| --- | --- |
| `Agent` | allgemeiner Akteur |
| `Person` | natürlicher Mensch aus `core/person` |
| `Organization` | kollektiver Akteur aus `core/organization` |

## 4. Beziehungen

Das Agent-Modul besitzt keine eigenen fachlichen Beziehungen. Andere Module
dürfen `Agent` als Wertebereich verwenden.

## 5. Verständliches Beispiel

```text
Participation -> participant -> Agent
                                /   \
                          Person     Organization
```

Eine Projektrolle kann damit von einer Person oder Organisation wahrgenommen
werden, ohne die Rollenbeziehung doppelt zu definieren.

## 6. Abgrenzung

Stammdaten bleiben bei Person und Organization. Kontakt- und Adressbeziehungen
bleiben ebenfalls in ihren Fachmodulen.

## 7. Entscheidungen

Der Agent-Kern bleibt propertyfrei und benötigt deshalb kein eigenes Core
Shape.
