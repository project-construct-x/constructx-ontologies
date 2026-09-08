# VSO Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** VSO Core Shapes

## 1. Zweck

Der ausführbare Shape-Graph operationalisiert die Regeln aus den
[SHACL-Anforderungen](shacl-requirements.md).

## 2. Geprüfte Verträge

Geprüft werden Eigentümer, Merkmalsreferenz, Zustand, Wert und optionale
Einheit einer Zuweisung.

## 3. Referenzgraphen

OPM, QUDT und Schema.org werden referenziert. Die Validierung benötigt keine
OWL-Inferenz.

## 4. Gültiges Beispiel

`examples/measured-property.ttl` zeigt einen Dezimalwert mit Einheit;
`examples/text-property.ttl` zeigt einen Textwert ohne Einheit.

## 5. Ungültiges Beispiel

Die fokussierten Dateien unter `tests/invalid` zeigen fehlende Verknüpfungen,
mehrere Eigentümer und falsche Zustandswerte.

## 6. Tests

Automatisierte PySHACL-Tests prüfen gültige und ungültige Graphen.

## 7. Bewusst nicht geprüft

ISOProps-Regeln liegen im separaten Profil `vso-isoprops`.
