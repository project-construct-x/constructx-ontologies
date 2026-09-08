# Modulgrenzen des VSO-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Zweck

Die Grenzen halten den VSO-Core unabhängig von Fachdomänen und konkreten
Merkmalsstandards.

## 2. Zuständigkeiten

VSO besitzt die Struktur der Merkmalszuweisung. Fachmodule bestimmen, welche
Ressourcen welche Merkmale tragen dürfen.

## 3. Abhängigkeiten

OPM liefert die Grundklassen, QUDT die Einheiten und Schema.org die
Wertproperty. Diese Ontologien werden referenziert und nicht importiert.

## 4. Bewusste Ausschlüsse

ISOProps-Identifikatoren, domänenspezifische Wertebereiche und Pflichtangaben zu
Einheiten sind keine VSO-Core-Regeln.

## 5. Verständliches Beispiel

> VSO kann ausdrücken, dass eine Tür eine Breite von 1,01 Metern besitzt. Ob
> Türen zwingend eine Breite benötigen, entscheidet ein Tür- oder Bauprofil.

## 6. Integrationsregel

Spezifische Standards verschärfen VSO über Profile, ohne den offenen
Core-Vertrag zu verändern.
