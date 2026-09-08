# Begriffskatalog des VSO-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/vso`

## 1. Zweck

Der Katalog erklärt die öffentlichen VSO-Begriffe kompakt.

## 2. Namensraum

`https://www.construct-x.org/ontology/vso#` mit dem Präfix `conx-vso`.

## 3. Klassen

| Klasse | Bedeutung |
| --- | --- |
| `AssignedProperty` | konkrete Zuweisung einer Merkmalsdefinition |
| `PropertyState` | Zustand, der den konkreten Wert trägt |

## 4. Properties

| Property | Bedeutung |
| --- | --- |
| `hasProperty` | verbindet eine Ressource mit einer Zuweisung |
| `hasPropertyReference` | verweist auf die Merkmalsdefinition |
| `hasPropertyState` | verbindet Zuweisung und Zustand |
| `hasUsedUnit` | verweist optional auf eine QUDT-Einheit |
| `schema:value` | enthält den konkreten Wert |

## 5. Kontrollierte Werte

Einheiten stammen aus QUDT. VSO besitzt kein eigenes Einheitenvokabular.

## 6. Verständliches Beispiel

Eine Zuweisung verweist auf „Höhe“, ihr Zustand enthält `2.80` und verweist auf
die QUDT-Einheit Meter.

## 7. Ausschlüsse

Fachliche Merkmalsdefinitionen und ISOProps-Metadaten sind keine lokalen
VSO-Begriffe.
