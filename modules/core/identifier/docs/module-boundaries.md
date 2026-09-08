# Modulgrenzen des Identifier-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Zweck

Die Grenze trennt die allgemeine Kennungsstruktur von fachlichen Regeln.

## 2. Zuständigkeiten

Identifier besitzt Typ, Notation und optionale Schema-Agentur. Person,
Organization und Document bestimmen selbst, ob und wie viele Kennungen erlaubt
oder verpflichtend sind.

## 3. Abhängigkeiten

Das Modul verwendet ADMS und SKOS. Konsumierende Core Shapes importieren den
versionierten Identifier-Shape-Graph.

## 4. Bewusste Ausschlüsse

Credential-Inhalte, kryptografische Prüfung, Vertrauensstatus und die stabile
IRI einer Ressource gehören nicht zum Identifier-Vertrag.

## 5. Verständliches Beispiel

> Der Identifier-Vertrag kann prüfen, dass „P-4711“ korrekt gespeichert ist.
> Ob jede Person eine Personalnummer benötigt, entscheidet dagegen ein
> Personen- oder Anwendungsprofil.

## 6. Integrationsregel

Core-Module referenzieren `conx-id-sh:ADMSIdentifierShape` und duplizieren die
Notation- und Schema-Agentur-Regeln nicht.
