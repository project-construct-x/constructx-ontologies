# Quellenanalyse des Identifier-Moduls

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand der Recherche:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Ziel und Methode

Die Analyse prüft, ob Construct-X eigene Kennungsbegriffe benötigt oder einen
bestehenden Standardvertrag wiederverwenden kann.

## 2. Bewertete Quellen

| Quelle | Verwendeter Beitrag |
| --- | --- |
| ADMS | `Identifier`, `identifier`, `schemaAgency` |
| SKOS | `notation` für den maschinenlesbaren Kennungswert |
| Construct-X Identifier-Scheme-Vokabular | Datentypen für Kennungssysteme |

## 3. Bewertung

ADMS und SKOS decken die benötigte Grundstruktur bereits ab. Eine lokale
Identifier-Klasse würde dieselbe Bedeutung ein zweites Mal modellieren.

## 4. Ergebnis

Construct-X besitzt nur den gemeinsamen Validierungsvertrag. Die semantischen
Begriffe bleiben bei ADMS und SKOS.

## 5. Verständliches Beispiel

> „DE“ ist erst zusammen mit dem Kennungssystem eindeutig. Als typisierte
> `skos:notation` kann erkennbar gemacht werden, dass es sich um einen
> ISO-3166-1-Alpha-2-Code handelt.

Die ausführliche Architekturentscheidung steht im
[netzwerkweiten Kennungsmodell](../../../../docs/architecture/identifier-model.md).
