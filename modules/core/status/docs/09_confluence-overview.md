# Überblick über das Status-Core-Modul

**Status:** Implementiert; Entwurfsversion  
**Version:** 0.1.0  
**Stand:** 17. November 2026  
**Geltungsbereich:** `core/status`

## 1. Zweck

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Moduldokumentation zusammen und
führt keine neuen fachlichen oder technischen Regeln ein.

Das Construct-X Core-Modul Status beschreibt, welchen Zustand ein Objekt zu
einem bestimmten fachlichen Datum und einer bestimmten Uhrzeit hatte.

## 2. Alltagsbeispiel

Eine Lieferung wird um 10:00 Uhr mit UTC-Offset +01:00 versendet. Um 10:05 Uhr
mit demselben UTC-Offset besteht sie die Temperaturprüfung nicht. Beide
Statusangaben können gleichzeitig aktuell sein, weil Transport und
Temperaturprüfung unterschiedliche Statusarten sind. Ein gemessener
Temperaturwert von 8,0 °C kann mit der Statusangabe zur Prüfung verknüpft werden.

## 3. Umfang und Abgrenzung

Das Modul umfasst Statusangaben, wiederverwendbare Statusarten, Statuswerte und
Statusgründe, optionale Verweise innerhalb der Statushistorie sowie die Anbindung
von Messwerten über VSO/ISOProps. Korrekturen, numerische Intervalle, Regeln für
Workflow-Übergänge und die Umstellung des bestehenden Document-Status gehören
nicht zum Umfang der Version 0.1.0.

## 4. Modellübersicht

Ein Objekt besitzt Statusangaben. Jede Statusangabe verweist auf genau eine
Statusart und einen Statuswert. Datum und Uhrzeit mit UTC-Offset sind
verpflichtend. Gründe, Beschreibungen, meldender Akteur, Erfassungszeitpunkt,
Vorgänger und Messwertverweise sind optional.

## 5. Zentrale Klassen und Beziehungen

| Element | Bedeutung in Alltagssprache |
| --- | --- |
| StatusAssignment | Eine Statusangabe zu einem Objekt mit Datum und Uhrzeit |
| StatusKind | Die beantwortete Frage, zum Beispiel nach dem Transportstatus |
| StatusValue | Der gemeldete Zustand, zum Beispiel „Versendet“ |
| StatusReason | Ein Grund für diesen Zustand |
| hasAllowedStatusValue | Welche Statuswerte zu einer Statusart gehören |
| hasAllowedStatusReason | Bekannte passende Gründe; die Liste ist nicht abschließend |
| hasCurrentStatus / previousStatus | Optionale Verweise auf die eindeutig neueste bekannte Statusangabe je Objekt und Statusart beziehungsweise auf den unmittelbaren Vorgänger |
| hasCondition | Ein Verweis auf eine VSO-Merkmalszuweisung mit ISOProps-Definition |
| reportedBy | Optional genau ein meldender Agent, zum Beispiel eine Person oder Organization |

Die Begriffe unserer Vokabulare besitzen Bezeichnungen, Definitionen, genau
einen Code und eine Zuordnung zu mindestens einem Begriffsschema. Pro Sprache
ist höchstens eine bevorzugte Bezeichnung vorgesehen. Statuswerte und Gründe
können wiederverwendet werden.

## 6. Validierung in Alltagssprache

Eine Statusangabe benötigt genau ein zugehöriges Objekt, eine Statusart, einen
Statuswert, ein Datum und eine Uhrzeit mit UTC-Offset. Der Statuswert muss zur
Statusart passen. Mehrere Gründe sind erlaubt, auch wenn sie der Statusart
nicht ausdrücklich zugeordnet sind.

Ein als aktuell ausgewählter Status muss zur Historie desselben Objekts gehören.
Je Objekt und Statusart darf höchstens eine Statusangabe als aktuell ausgewählt
sein. Der Verweis ist optional. Wird er gesetzt, muss er auf die eindeutig
neueste bekannte Statusangabe zeigen. Entscheidend sind das fachliche Datum
und die Uhrzeit einschließlich UTC-Offset, nicht der Erfassungszeitpunkt.
Bei gleichzeitigen neuesten Statusangaben muss die Reihenfolge ausdrücklich
durch Vorgängerverweise feststehen. Solange sie nicht eindeutig ist, darf kein
aktueller Status ausgewählt werden.

Beispiel: „Versendet“ (`Shipped`) um 09:00 Uhr, erst um 13:00 Uhr erfasst,
ersetzt nicht „Geliefert“ (`Delivered`) um 12:00 Uhr, erfasst um 12:05 Uhr
(alle Zeiten in UTC). Fachlich bleibt „Geliefert“ die neueste Statusangabe.
Die Anwendung pflegt den Verweis; die Validierung prüft lediglich, ob er korrekt ist.

Der optionale Erfassungszeitpunkt `recordedAt` muss ein gültiges Datums- und
Uhrzeitformat verwenden, wenn er angegeben wird. Beispielsweise ist
`2026-11-11T10:05:00` auch ohne UTC-Offset gültig. Ein Leerzeichen anstelle von
`T` oder ein UTC-Offset von +15:00 wird abgelehnt. Mitternacht darf auch als
`2026-12-31T24:00:00Z` geschrieben werden; das bezeichnet den Beginn des
1. Januar 2027. Bei Stunde 24 müssen Minuten, Sekunden und sämtliche
Nachkommastellen null sein. Die eingegebene Schreibweise bleibt erhalten.

Vorgängerverweise müssen beim selben Objekt und derselben Statusart bleiben.
Sie dürfen keine Kreise bilden und der bekannten fachlichen Reihenfolge nicht
widersprechen. Das gilt auch für ausdrücklich festgelegte Reihenfolgen bei
gleichen Zeitpunkten. Die fachliche Uhrzeit `referenceTime` unterstützt bis zu
sechs Nachkommastellen bei den Sekunden.

Über `hasCondition` verknüpfte Messwerte benötigen eine gültige
ISOProps-Definition, einen gültigen Wert des passenden Datentyps und eine
zulässige Einheit. Ein Wort wird beispielsweise auch dann abgelehnt, wenn es
technisch als Dezimalzahl gekennzeichnet wurde.

## 7. Abhängigkeiten

Das Modul nutzt Agent, VSO, das bestehende VSO/ISOProps-Profil und SKOS.
Die drei Startvokabulare werden als getrennte, versionierte Referenzdatensätze
bereitgestellt. Eine Domänenontologie wird nicht benötigt.

Wird eine Person oder Organisation als meldender Akteur verwendet, liefert die
jeweilige Core-Ontologie Person beziehungsweise Organization die benötigten
Klassendefinitionen. Die [Beispiele für meldende Akteure](../examples/reporting-actors/README.md)
zeigen beide Fälle mit ausführbaren Anleitungen zur Validierung.

## 8. Version, Status und Artefakte

Version 0.1.0 liegt als Entwurf vor. Die technischen Grundlagen sind die
[Ontologie](../ontology/conx-status.ttl), die [Core Shapes](07_core-shapes.md),
der [HTML-Katalog](status.html) und das [Änderungsprotokoll](../CHANGELOG.md).
Die Anwendung muss historische Messwerte aufbewahren. Eine Prüfung des
vorliegenden Datenstands kann nicht sicherstellen, dass gespeicherte Werte
über die Zeit unverändert bleiben.

Die [Anleitung zu den Core Shapes](07_core-shapes.md) erklärt außerdem, wie
das vollständige Validierungspaket exportiert und außerhalb des Repositorys
verwendet werden kann.

## 9. Weiterführende Dokumentation

- [Modulindex](00_index.md)
- [Konzeptmodell](03_concept-model.md)
- [Begriffskatalog](05_term-catalog.md)
- [Validierungsanforderungen](06_shacl-requirements.md)
- [Vollständiges Diagramm](08_concept-diagram.md)
- [Ausgearbeitetes Messwertbeispiel](../examples/status-with-condition.ttl)
