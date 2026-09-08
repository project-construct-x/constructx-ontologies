# Scope und Kompetenzfragen des Address-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/address`

## 1. Zweck

Das Modul beschreibt strukturierte Adressen und die Zuordnung einer Adresse zu
einer Ressource. Es trennt den Ort von der fachlichen Verwendung, beispielsweise
als Liefer- oder Rechnungsadresse.

## 2. Bestätigter Scope

- strukturierte Bestandteile einer Adresse,
- Adresszuordnungen mit mindestens einer Rolle,
- Länder und administrative Gebiete als referenzierbare Ressourcen,
- optionale Verknüpfung mit einer geografischen Position.

## 3. Nicht im Scope

Kontaktkanäle, Personen, Organisationen, Koordinatenmodelle und formatierte
Postanschriften werden nicht im Address-Modul definiert.

## 4. Kompetenzfragen

1. Welche Adresse ist einer Ressource zugeordnet?
2. Welche Rolle besitzt diese Zuordnung?
3. In welchem Land und Verwaltungsgebiet liegt die Adresse?
4. Ist eine geografische Position mit der Adresse verknüpft?

## 5. Verständliches Beispiel

> Eine Firma nutzt dieselbe Anschrift für Rechnungen und Lieferungen. Die
> Straße wird nur einmal gespeichert; die beiden Verwendungszwecke stehen an
> der Adresszuordnung.

```text
Firma -> Adresszuordnung -> Adresse in Bochum
             |
             +-> Rechnungsadresse
             +-> Lieferadresse
```

## 6. Modellentscheidungen

Die Adresse selbst bleibt frei von Empfänger- und Verwendungsdaten. Rollen und
empfängerspezifische Hinweise liegen an `AddressAssignment`. Die vollständigen
Entscheidungen stehen im [Konzeptmodell](concept-model.md).

## 7. Abnahmekriterien

Der Scope ist erfüllt, wenn Adresse, Zuordnung und Rolle getrennt bleiben und
die Core Shapes die erforderlichen Beziehungen prüfen.
