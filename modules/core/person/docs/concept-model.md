# Konzeptmodell des Person-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

## 1. Zweck

Das Modell beschreibt intrinsische Kerndaten einer realen natürlichen Person.

## 2. Modell in einfachen Worten

Eine Person besitzt Namen und kann Angaben zu Geburt, Staatsangehörigkeit,
menschlichem Geschlecht, Gender, Kennungen und Identitätsnachweisen tragen.

## 3. Begriffe

Der zentrale Begriff ist `Person`. Kontrollierte Werte für `sex` und `gender`
werden in getrennten Referenzvokabularen gepflegt.

## 4. Beziehungen

`Person` ist eine Unterklasse von `Agent`. Kontakte, Adressen und
Organisationsbeziehungen werden über ihre zuständigen Module angebunden.

## 5. Verständliches Beispiel

> Anna Müller wird einmal als Person beschrieben. Ihre geschäftliche
> Telefonnummer liegt an einem Kontaktpunkt; ihre Mitgliedschaft in einem Büro
> liegt an einer Membership. Beides wird nicht in die Person kopiert.

```text
Person Anna Müller
  +-> ContactPoint    über core/contact
  +-> Membership      über core/organization
  +-> Identifier      über core/identifier
```

## 6. Abgrenzung

Das Modul beschreibt weder Organisationen noch die interne Struktur von
Credentials oder Ausweisdokumenten.

## 7. Entscheidungen

`sex` und `gender` bleiben getrennt. Personenkennungen verwenden den
gemeinsamen Identifier-Vertrag.

Das ausführliche Diagramm steht unter
[person-concept-model.md](diagrams/person-concept-model.md).
