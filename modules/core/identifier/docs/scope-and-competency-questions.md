# Scope und Kompetenzfragen des Identifier-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Zweck

Das Modul definiert einen gemeinsamen Minimalvertrag für fachliche Kennungen.

## 2. Bestätigter Scope

- Kennung als `adms:Identifier`,
- genau ein Kennungswert über `skos:notation`,
- optionale Angabe der herausgebenden Stelle,
- wiederverwendbares Core Shape.

## 3. Nicht im Scope

Das Modul entscheidet nicht, welche Kennung ein Fachobjekt zwingend benötigt.
Es definiert auch keine parallele Construct-X-Identifier-Klasse.

## 4. Kompetenzfragen

1. Welchen Wert besitzt eine Kennung?
2. Welches Kennungssystem bezeichnet den Wert?
3. Welche Stelle hat das Schema herausgegeben?
4. Kann derselbe Vertrag für Person, Organisation und Dokument gelten?

## 5. Verständliches Beispiel

> Eine Organisation besitzt die Registernummer „HRB 1234“. Die Organisation
> verweist auf eine eigene Identifier-Ressource, die den Wert und optional die
> herausgebende Stelle enthält.

```text
Organisation -> Identifier -> „HRB 1234“
                               Amtsgericht Bochum
```

## 6. Modellentscheidungen

ADMS und SKOS werden direkt wiederverwendet. Fachmodule behalten die
Zuständigkeit für Pflichtkennungen und zulässige Kennungssysteme.

## 7. Abnahmekriterien

Der Vertrag ist erfüllt, wenn jede Identifier-Ressource korrekt typisiert ist
und genau eine literale Notation besitzt.
