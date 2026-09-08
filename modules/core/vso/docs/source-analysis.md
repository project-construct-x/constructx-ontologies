# Quellenanalyse des VSO-Moduls

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand der Recherche:** 1. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Ziel und Methode

Analysiert wurde ein systemneutrales Muster für Merkmalszuweisungen, Werte und
Einheiten.

## 2. Bewertete Quellen

| Quelle | Beitrag |
| --- | --- |
| OPM | Property und PropertyState |
| QUDT | wiederverwendbare Maßeinheiten |
| Schema.org | allgemeine Property `schema:value` |
| ISOProps | separates Interoperabilitätsprofil |

## 3. Bewertung

OPM bietet die passende Grundstruktur. QUDT und Schema.org decken Einheit und
Wert ab, ohne dass VSO parallele Begriffe einführen muss.

## 4. Ergebnis

VSO ergänzt die eindeutige Verknüpfung zwischen Ressource, Zuweisung,
Merkmalsreferenz und Zustand. Externe Ontologien werden referenziert, aber nicht
importiert.

## 5. Verständliches Beispiel

> „2,80“ allein ist nicht aussagekräftig. Zusammen mit der
> Merkmalsdefinition „Höhe“ und der Einheit „Meter“ wird daraus eine
> verständliche Eigenschaft einer Wand.

Technische Bestandsdetails stehen in der
[Integrationsanalyse](integration-analysis.md).
