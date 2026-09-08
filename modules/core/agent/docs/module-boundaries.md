# Modulgrenzen des Agent-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Der Agent-Kern verhindert zyklische Abhängigkeiten zwischen Person und
Organization.

## 2. Zuständigkeiten

`core/agent` besitzt nur den gemeinsamen Typ `Agent`. Personendaten liegen in
`core/person`, Organisationsdaten in `core/organization`.

## 3. Abhängigkeiten

Person, Organization und Participation referenzieren Agent. Agent selbst hängt
nicht von diesen Modulen ab.

## 4. Bewusste Ausschlüsse

Keine Namen, Kennungen, Kontakte, Adressen, Rollen oder Berechtigungen werden
im Agent-Modul definiert.

## 5. Verständliches Beispiel

> Eine Telefonnummer gehört zu einem Kontaktpunkt. Auch wenn der Kontaktpunkt
> von einem Agenten genutzt wird, wird die Telefonnummer nicht zu einer
> Agent-Property.

## 6. Integrationsregel

Neue Core-Module dürfen Agent verwenden, wenn sowohl Personen als auch
Organisationen sinnvolle Werte derselben Beziehung sein können.
