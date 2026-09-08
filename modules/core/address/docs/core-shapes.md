# Core SHACL Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Address Core Shapes

Die Address Core Shapes validieren die allgemeinen Verträge der Address
Ontology unabhängig von einem konkreten Anwendungsfall. Sie spiegeln die
OWL-Kardinalitäten und machen die in der T-Box beschriebenen Wertebereiche als
geschlossene Datenprüfungen ausführbar.

```text
Shape-Graph: modules/core/address/shapes/conx-addr-core.shacl.ttl
Shape-IRI:   https://www.construct-x.org/shapes/address/core
Versions-IRI: https://www.construct-x.org/shapes/address/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/address/core#
Version:     0.1.0
```

`core` ist der Name des Shape-Sets. Weitere anwendungsfallspezifische
Shape-Sets können unter demselben Modulpfad unabhängig versioniert werden.

## 1. OWL und SHACL erfüllen unterschiedliche Aufgaben

OWL beschreibt die Semantik zulässiger Modelle unter der Open-World-Annahme.
Eine fehlende Rolle ist dort nicht automatisch falsch, weil sie noch unbekannt
sein kann. Zwei über `hasCountry` verknüpfte Ressourcen können bei einer
Maximalrestriktion außerdem als dieselbe Ressource interpretiert werden.

SHACL prüft dagegen den jeweils vorliegenden Datengraphen. Fehlt eine
verpflichtende Rolle oder sind zwei Länder angegeben, entsteht unmittelbar ein
Validierungsfehler. Die parallelen Regeln sind deshalb keine unnötige
Dopplung:

- OWL macht die Modellsemantik für Reasoner und Ontologienutzer sichtbar.
- SHACL prüft konkrete Datenlieferungen und erzeugt verständliche Fehlerpfade.

## 2. Parallel in OWL und SHACL abgebildete Kardinalitäten

| Klasse | Eigenschaft | Kardinalität |
| --- | --- | --- |
| `AddressAssignment` | `assignedAddress` | genau 1 |
| `AddressAssignment` | `addressRole` | mindestens 1 |
| `AddressAssignment` | `careOf` | höchstens 1 |
| `Address` | `hasCountry` | höchstens 1 |
| `Address` | `houseNumber` | höchstens 1 |
| `Address` | `postOfficeBoxNumber` | höchstens 1 |
| `Address` | `postalCode` | höchstens 1 |
| `AdministrativeArea` | `broaderAdministrativeTerritory` | höchstens 1 |

`assignedAddress` und `addressRole` waren bereits als OWL-Restrictions in der
T-Box enthalten. Die übrigen sechs Maximalrestriktionen wurden mit den Core
Shapes ergänzt.

`plotIdentifier` bleibt bewusst bei `0..n`: Eine Adresse kann mit mehreren
Grundstücken oder Flurstücken verbunden sein.

## 3. Zusätzlich geprüfte T-Box-Verträge

Die Shapes führen die vorhandenen OWL-/RDFS-Verträge als Datenprüfung aus:

- Werte von Objektbeziehungen müssen Instanzen der angegebenen Range-Klasse
  sein.
- Rollen, Länder und Verwaltungseinheiten müssen über IRIs referenziert werden.
- `hasGeographicPosition` muss auf eine Ressource und darf nicht auf ein
  Literal verweisen.
- Textuelle Bezeichnungen akzeptieren `xsd:string` oder `rdf:langString`.
- Codes und empfängerbezogene Textwerte akzeptieren ausschließlich
  `xsd:string`.
- Ressourcen, die Address-Eigenschaften verwenden, müssen explizit dem
  passenden Address-Typ entsprechen.

Die letzte Regel ist in SHACL strenger sichtbar als eine RDFS-Domain. Eine
RDFS-Domain inferiert den Typ, während SHACL einen fehlenden oder falschen Typ
als Datenproblem melden kann.

## 4. Bewusst nicht im Core erzwungen

- Straße, Hausnummer, Ort, Postleitzahl oder Land als allgemeine Pflichtfelder
- Zugehörigkeit zu genau einem bestimmten Rollen- oder ISO-Referenzdatensatz
- höchstens ein sprachmarkierter Wert je Sprache
- länderspezifische Postleitzahlenmuster
- Abhängigkeiten wie „Postfachnummer oder Straßenanschrift erforderlich“
- Übereinstimmung zwischen Land und vollständiger Verwaltungshierarchie

Diese Regeln hängen vom Anwendungsfall oder Profil ab. Sie werden später in
Shapes für Liefer-, Rechnungs-, Baustellen- oder Postfachadressen ergänzt.

## 5. Testdaten

Der vollständige gültige Graph liegt unter:

```text
modules/core/address/tests/valid/complete-address.ttl
```

Gezielte Fehlerfälle liegen unter:

```text
modules/core/address/tests/invalid/assignment-missing-required-values.ttl
modules/core/address/tests/invalid/invalid-core-values.ttl
```

Eine einzelne Datei kann beispielsweise so validiert werden:

```text
uv run pyshacl -s modules/core/address/shapes/conx-addr-core.shacl.ttl -e modules/core/address/ontology/conx-addr.ttl -i none modules/core/address/tests/valid/complete-address.ttl
```

Die automatisierten Tests prüfen zusätzlich, dass jede allgemeine
OWL-Kardinalität im Shape-Graph gespiegelt wird.

## 6. Verständliches Beispiel

> Eine AddressAssignment ohne Adresse ist unvollständig. Die Core Shapes
> melden diesen Fehler, weil sonst nicht erkennbar ist, welche Anschrift der
> Ressource zugeordnet wurde.
