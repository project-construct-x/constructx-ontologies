# Agent Core Shapes

**Status:** Kein eigenes Shape erforderlich  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Der Agent-Kern definiert ausschließlich eine gemeinsame Oberklasse.

## 2. Geprüfte Verträge

Es existiert kein eigener Shape-Graph und damit kein Agent-spezifischer
Validierungsvertrag.

## 3. Referenzgraphen

Nicht anwendbar.

## 4. Gültiges Beispiel

Eine Person kann als Agent verwendet werden, weil die T-Box die
Unterklassenbeziehung festlegt.

## 5. Ungültiges Beispiel

Nicht anwendbar; konkrete Unterklassen werden durch ihre eigenen Shapes geprüft.

## 6. Tests

Die OWL-Tests prüfen die T-Box-Struktur.

## 7. Bewusst nicht geprüft

Alle fachlichen Eigenschaften bleiben bei den zuständigen Modulen.
