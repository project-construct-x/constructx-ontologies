# Fachliche SHACL-Anforderungen des Agent-Moduls

**Status:** Kein eigenes Shape erforderlich  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Das Dokument erklärt, warum das Agent-Modul trotz einheitlicher
Dokumentationsstruktur keinen ausführbaren Shape-Graph besitzt.

## 2. Shape-Set

Für Version 0.1.0 ist kein Agent Core Shape definiert.

## 3. Validierungsanforderungen

`Agent` besitzt keine eigenen Pflichtproperties. Eine pauschale Validierung
würde deshalb keinen zusätzlichen Datenvertrag ausdrücken.

## 4. Fehlerverhalten

Es gibt keine Agent-spezifischen Fehlercodes. Konkrete Fehler entstehen in den
Modulen, die eine Beziehung oder Unterklasse besitzen.

## 5. Gültiges Beispiel

Eine Ressource mit dem Typ `conx-agent:Agent` ist ohne weitere Angaben gültig.

## 6. Ungültiges Beispiel

Ein allgemeines ungültiges Agent-Beispiel existiert nicht, weil der Agent-Core
keine Pflichtangaben festlegt.

## 7. Bewusst nicht geprüft

Namen, Kontakte, Adressen und Rollen werden durch ihre Fachmodule geprüft.

## 8. Tests

Ontologietests prüfen die Klasse und ihre Einordnung unter `foaf:Agent`.
