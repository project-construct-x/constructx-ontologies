# Quellenanalyse des Agent-Moduls

**Status:** Konsolidierte Analysegrundlage  
**Version:** 0.1.0  
**Stand der Recherche:** 27. August 2026  
**Geltungsbereich:** `core/agent`

## 1. Ziel und Methode

Untersucht wurde, welcher gemeinsame Akteursbegriff Personen und Organisationen
verbinden kann, ohne ihre Stammdaten zusammenzuführen.

## 2. Bewertete Quellen

| Quelle | Beitrag |
| --- | --- |
| FOAF | allgemeiner Begriff `foaf:Agent` |
| SEMIC Core Vocabularies | europäische Agenten- und Personenmodelle |
| W3C ORG | Agenten in Mitgliedschaften und Organisationen |

## 3. Bewertung

`foaf:Agent` ist breit interoperabel. Ein lokaler Construct-X-Begriff bleibt
trotzdem sinnvoll, damit interne Module auf eine kontrollierte gemeinsame
Oberklasse verweisen können.

## 4. Ergebnis

`conx-agent:Agent` ist als Unterklasse von `foaf:Agent` umgesetzt. Eine
Äquivalenz wurde vermieden, weil Construct-X den verwendeten Ausschnitt enger
kontrolliert.

## 5. Verständliches Beispiel

> Bei einer Beteiligung wird ein Akteur referenziert. Dieselbe Struktur kann
> dadurch sowohl „Anna Müller“ als auch „Beispiel Bau GmbH“ aufnehmen.

Die ausführliche Herleitung steht in der
[Agent-Spezifikation](agent-specification.md).
