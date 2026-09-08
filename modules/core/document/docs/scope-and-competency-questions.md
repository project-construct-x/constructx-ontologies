# Scope und Kompetenzfragen des Document Core Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`  
**Umsetzungsstand:** T-Box, Referenzvokabulare und Core Shapes umgesetzt

## 1. Zweck

Das Document Core Modul beschreibt dokumentartige Ressourcen,
Dokumentreferenzen und technische Distributionen. Es soll Dokumente in
Construct-X eindeutig referenzierbar machen, ohne ein Dokumentenmanagement-,
Archiv-, Signatur-, Credential-, Rechte- oder Workflowmodell zu duplizieren.

Dieses Dokument legt den fachlichen Scope und die Kompetenzfragen des MVP fest.
Klassen, Properties, IRIs und Kardinalitäten sind in T-Box und Core Shapes
umgesetzt. Verwendete externe Begriffe sind als `referenced-not-imported`
dokumentiert.

Die fachliche Herleitung steht in der [Quellenanalyse](source-analysis.md).

## 2. Bestätigter Scope

| Bereich | Entscheidung für den MVP |
| --- | --- |
| Dokumentkern | Eigene Construct-X-Klasse `Document` für dokumentartige Informationsobjekte |
| Externe Alignments | Schema.org, FOAF und Dublin Core sind Alignmentziele, aber nicht der lokale Kernbegriff |
| Dokumentreferenz | Eigene Ressource `DocumentReference`, wenn eine Kontextressource auf ein Dokument verweist |
| Datei/Bereitstellung | DCAT-nahe Trennung als `DocumentDistribution`; `Attachment` bleibt nur UBL-Vergleichsbegriff |
| Metadaten | Titel, Beschreibung, Sprache, Version und zentrale Datumsangaben sind optional |
| Datumsangaben | Erstellt, ausgegeben, geändert und gültig sind optionale Kernangaben |
| Dokumenttyp | Kleines kontrolliertes MVP-Vokabular `DocumentType` |
| Dokumentstatus | Kleines kontrolliertes MVP-Vokabular `DocumentStatus` |
| Identifikatoren | Wiederverwendung von `core/identifier` und dessen ADMS-/SKOS-Vertrag |
| Akteursrollen | Aussteller, Sender, Empfänger, Autor, Publisher und ähnliche Rollen über `core/participation` modellieren |
| Provenienz | PROV-O nur für echte Erzeugung, Ableitung, Revision oder Verarbeitung nutzen |
| UBL | Nur Vergleichsquelle; keine Abhängigkeit und aktuell kein Mapping geplant |
| Signaturen und Credentials | Nicht Teil des Document Core; spätere Trust-/Evidence-Profile möglich |
| Rechte und Zugriff | Keine Policy- oder Zugriffskontrolle im Document Core |

## 3. Fachliches Zielbild

```text
fachlicher Kontext
  └── DocumentReference
        ├── referencesDocument -> Document
        ├── hasDistribution    -> DocumentDistribution
        └── Metadaten zur Referenz

Document
  ├── Titel / Beschreibung / Sprache
  ├── Identifikatoren
  ├── Dokumenttyp
  ├── Dokumentstatus
  ├── Datumsangaben
  └── Distributionen

DocumentDistribution
  ├── URI oder Download-/Access-Information
  ├── Dateiname
  └── Medientyp

Agentenrollen am Dokument
  └── core/participation

Entstehung, Ableitung, Revision
  └── späteres PROV-O-Alignment oder Provenienzprofil
```

Die Darstellung zeigt fachliche Verknüpfungen. Externe Vokabulare sind in
`module.yaml` als Referenzen ohne `owl:imports` dokumentiert.

## 4. Kompetenzfragen

### DCQ-01: Wie wird ein Dokument eindeutig referenziert?

Ein Dokument erhält eine stabile IRI im Namensraum des jeweiligen
Datenhalters. Diese IRI ist die technische RDF-Identität des Dokuments.
Fachliche Dokumentnummern, Registerkennungen, UUIDs oder externe Archivnummern
sind zusätzliche Identifikatoren und ersetzen die Dokument-IRI nicht.

Das Modell muss darstellen können:

- ein Dokument mit einer stabilen IRI,
- ein Dokument mit mehreren Identifikatoren,
- das jeweilige Identifikatorschema,
- die zuständige Schema-Agentur,
- die Trennung zwischen Ressourcen-IRI und fachlicher Kennung.

### DCQ-02: Was unterscheidet `Document`, `DocumentReference` und `DocumentDistribution`?

`Document` beschreibt das dokumentartige Informationsobjekt. Eine Rechnung, ein
Vertrag, ein Zertifikat oder ein Plan kann fachlich ein Dokument sein, ohne dass
damit bereits eine konkrete Datei gemeint ist.

`DocumentReference` beschreibt die kontextbezogene Bezugnahme auf ein Dokument.
Sie wird gebraucht, wenn eine andere Ressource auf ein Dokument verweist und die
Referenz eigene Angaben tragen kann, etwa Referenzart, Kontext, Sprache, Version
oder Gültigkeit.

`DocumentDistribution` beschreibt die konkrete technische Ausprägung oder
Bereitstellung, zum Beispiel eine PDF-Datei, einen Download-Link oder eine
andere abrufbare Datei.

Das Modell muss darstellen können:

- ein Dokument ohne bekannte Datei,
- ein Dokument mit mehreren Distributionen,
- eine Kontextressource mit einer oder mehreren Dokumentreferenzen,
- eine Dokumentreferenz, die auf ein lokal modelliertes Dokument oder eine
  externe Dokumentressource zeigt.

### DCQ-03: Wie verweist eine fachliche Kontextressource auf ein Dokument?

Eine fachliche Ressource soll nicht zwingend direkt auf eine Datei zeigen. Sie
verweist auf eine `DocumentReference`. Die Referenz kann anschliessend auf ein
modelliertes `Document`, eine externe Ressource oder eine Distribution zeigen.

Beispiel:

```text
Bestellung 123
  hasDocumentReference -> Referenz auf Vertragsanlage A

Referenz auf Vertragsanlage A
  referencesDocument -> Vertragsanlage A
  hasDistribution    -> PDF-Datei der Vertragsanlage
```

Dadurch können spätere Profile festlegen, welche Dokumentreferenzen für
welche fachlichen Kontexte verpflichtend sind, ohne diese Pflicht in den
Document Core selbst zu ziehen.

### DCQ-04: Welche allgemeinen Metadaten gehören in den Document Core?

Der Document Core soll allgemeine Metadaten vorsehen, die dokumentübergreifend
sinnvoll sind:

- Titel,
- Beschreibung,
- Sprache,
- Version,
- Erstellungsdatum,
- Ausgabedatum,
- Änderungsdatum,
- Gültigkeit.

Diese Angaben sind im offenen Core nicht pauschal verpflichtend. Ob ein
bestimmter Dokumenttyp einen Titel, eine Version oder ein Ausgabedatum braucht,
entscheidet ein späteres Profil.

### DCQ-05: Wie werden Dokumenttypen modelliert?

Dokumenttypen sind als kontrollierte Konzepte umgesetzt und nicht als
Unterklassen des Document Core. Dadurch bleibt der Kern klein und
erweiterbar.

Das getrennte MVP-Referenzvokabular enthält folgende Startwerte:

- Vertrag,
- Rechnung,
- Lieferschein,
- Zertifikat,
- Bericht,
- Plan oder Zeichnung,
- Nachweisdokument,
- sonstiges Dokument.

### DCQ-06: Wie werden Dokumentstatus modelliert?

Dokumentstatus beschreibt den Zustand eines Dokuments, nicht den Typ und nicht
den Prozessschritt.

Beispiele:

```text
Dokumenttyp:    Rechnung
Dokumentstatus: ausgegeben

Dokumenttyp:    Vertrag
Dokumentstatus: Entwurf

Dokumenttyp:    Zertifikat
Dokumentstatus: abgelaufen
```

Das getrennte MVP-Referenzvokabular enthält folgende dokumentbezogene
Statuswerte:

- Entwurf,
- ausgegeben oder freigegeben,
- ersetzt,
- widerrufen oder zurückgezogen,
- abgelaufen,
- archiviert.

Workflowzustände wie "in Prüfung", "wartet auf Freigabe" oder "zugewiesen an
Rechtsabteilung" gehören nicht in den Document Core.

### DCQ-07: Wie werden Datumsangaben abgegrenzt?

Der Document Core soll mehrere optionale Datumsbegriffe zulassen, weil ein
einziges allgemeines Dokumentdatum fachlich zu unscharf wäre.

| Datum | Bedeutung |
| --- | --- |
| Erstellt | Wann das Dokument erzeugt wurde |
| Ausgegeben | Wann das Dokument fachlich ausgestellt oder ausgegeben wurde |
| Geändert | Wann der Inhalt zuletzt geändert wurde |
| Gültig ab | Beginn der fachlichen Gültigkeit |
| Gültig bis | Ende der fachlichen Gültigkeit |

Gültigkeit ist nicht dasselbe wie Veröffentlichung, Ablauf eines Links oder
Archivierung. Der MVP verwendet zwei optionale Angaben `validFrom` und
`validUntil`; beide können als `xsd:date` oder `xsd:dateTime` angegeben werden.

### DCQ-08: Wie werden Dateien und technische Bereitstellungen beschrieben?

Eine Datei oder technische Bereitstellung wird als `DocumentDistribution`
modelliert. Sie ist nicht identisch mit dem Dokument selbst.

Das Modell muss darstellen können:

- eine Distribution mit URI,
- eine Distribution mit Dateiname,
- eine Distribution mit Medientyp,
- mehrere Distributionen für dasselbe Dokument, zum Beispiel PDF und XML,
- eine Distribution, die über eine Dokumentreferenz genutzt wird.

Medientypen sollen sich an IANA orientieren. Ein Storage-, Upload-, Repository-
oder Archivmodell gehört nicht in den Document Core.

### DCQ-09: Wie werden Aussteller, Sender, Empfänger, Autor und Publisher modelliert?

Diese Akteursrollen werden nicht als eigene direkte Properties im Document Core
angelegt. Sie werden über `core/participation` modelliert: Ein Agent spielt
eine kontrollierte Rolle im Kontext eines Dokuments oder einer
Dokumentreferenz.

Beispiel Rechnung:

```text
Rechnung 4711
  Participation: Organisation A als issuer
  Participation: Organisation B als recipient
```

Beispiel Bauzeichnung:

```text
Tragwerksplan Version 3
  Participation: Person X als author
  Participation: Organisation Y als publisher
  Participation: Organisation Z als recipient
```

Beispiel Genehmigungsbescheid:

```text
Baugenehmigung
  Participation: Behörde A als issuer
  Participation: Antragsteller B als recipient
```

Ein späteres Profil kann festlegen, dass ein bestimmter Dokumenttyp genau
einen Aussteller oder mindestens einen Empfänger besitzen muss. Diese
Kardinalitäten gehören nicht in den allgemeinen Document Core.

### DCQ-10: Wann ist PROV-O relevant?

PROV-O ist relevant, wenn die Entstehung, Ableitung, Revision oder Verarbeitung
eines Dokuments beschrieben wird.

Beispiele:

```text
PDF-Datei wurde aus Datensatz Y erzeugt
Dokumentversion 3 ersetzt Dokumentversion 2
Prüfbericht wurde durch Aktivität X generiert
```

Diese Aussagen sind Provenienz. Sie sind nicht dasselbe wie fachliche
Akteursrollen am Dokument. Autor, Aussteller, Sender und Empfänger laufen über
`core/participation`; Erzeugung, Ableitung und Revision können später gegen
PROV-O ausgerichtet werden.

### DCQ-11: Wie werden Evidence, Credentials und Signaturen abgegrenzt?

Ein Dokument kann als Nachweis verwendet werden, aber das macht das Document
Core Modul nicht zu einem Evidence- oder Credential-Modell.

Das Modell darf darstellen, dass ein Dokument existiert und referenziert wird.
Die Semantik "belegt Requirement X", "ist ein Verifiable Credential", "wurde
kryptografisch signiert" oder "ist rechtlich qualifiziert gültig" gehört in
spätere Profile oder spezialisierte Module.

### DCQ-12: Wie werden Rechte, Lizenzen und Zugriff behandelt?

Eine einfache Lizenz- oder Rechte-URI kann später als allgemeines Metadatum
bewertet werden. Zugriffskontrolle, Rollenrechte, Vertraulichkeit,
Einwilligungen, Weitergaberegeln und Policy-Auswertung sind nicht Teil des
Document Core.

ODRL bleibt eine mögliche spätere Alignmentquelle für Rechte- und
Policy-Profile.

### DCQ-13: Welche Validierungsfragen beantwortet das Core-SHACL-Profil?

Das implementierte Core-SHACL-Profil prüft:

- dass `Document`, `DocumentReference` und `DocumentDistribution` korrekt
  typisiert werden,
- dass Dokumenttypen nur Werte des freigegebenen Dokumenttyp-Vokabulars
  verwenden,
- dass Dokumentstatus nur Werte des freigegebenen Dokumentstatus-Vokabulars
  verwenden,
- dass Datumswerte passende Datentypen nutzen,
- dass Distributionen bei vorhandener URI eine gültige IRI verwenden,
- dass Medientypen konsistent als technische Formatangaben verwendet werden,
- dass Identifikatoren dem bestehenden ADMS-/SKOS-Muster folgen,
- dass keine direkten Document-Core-Properties für Aussteller, Autor,
  Publisher, Sender oder Empfänger erforderlich sind.

## 5. Ausdrücklich ausserhalb des Document Core

- Rechnungs-, Lieferschein-, Vertrags-, Zertifikats- oder Berichtsklassen,
- UBL-Abhängigkeiten und UBL-Mappings,
- Signatur-, Siegel-, Zeitstempel- und Trust-List-Modelle,
- Verifiable Credentials und Data-Integrity-Proofs,
- Evidence-/Requirement-Semantik,
- Workflowstatus, Freigabeprozesse und Aufgabensteuerung,
- Zugriffskontrolle, Berechtigungen, Datenschutz- und Policy-Auswertung,
- Archivierung, Aktenpläne, Retention und Records Management,
- Volltext, OCR, Seiten, Abschnitte und Annotationen,
- Storage-, Upload-, Repository- oder DMS-spezifische Konzepte,
- domain-spezifische Pflichtdokumente und Positivlisten.

Diese Ausschlüsse verhindern nicht die spätere Verknüpfung mit
entsprechenden Ressourcen. Sie legen nur fest, dass deren Semantik nicht vom
Document Core besessen wird.

## 6. Geklärte Modellentscheidungen

| Thema | Entscheidung | Grund |
| --- | --- | --- |
| Lokaler Dokumentbegriff | Eigene Klasse `Document` | Construct-X braucht einen stabilen Kernbegriff und kann externe Begriffe alignen |
| Datei vs. Dokument | Trennung über `DocumentDistribution` | Eine Datei ist nur eine Ausprägung oder Bereitstellung eines Dokuments |
| UBL | Nur Vergleichsquelle | Kein aktuelles Mapping und keine geplante Abhängigkeit |
| Dokumenttyp | Kleines MVP-Vokabular | Profile brauchen einen gemeinsamen Startpunkt ohne Klassenexplosion |
| Dokumentstatus | Kleines MVP-Vokabular | Dokumentzustand ist fachlich wiederkehrend, Workflowstatus bleibt draussen |
| Akteursrollen | Über `core/participation` | Verhindert direkte Properties für jede mögliche Rolle |
| Provenienz | Späteres PROV-O-Alignment oder Profil | Entstehung und Ableitung sind andere Semantik als Dokumentmetadaten |

## 7. Abgeschlossene Modellierungsentscheidungen

| Thema | Entscheidung |
| --- | --- |
| Externe Terms | Lokale Metadatenproperties mit Alignment; DCAT-Zugriffsproperties direkt wiederverwenden |
| Datumsmodell | Optionale `validFrom`- und `validUntil`-Werte |
| Typ-Vokabular | Acht freigegebene MVP-Werte im getrennten SKOS-Vokabular |
| Status-Vokabular | Sechs freigegebene MVP-Werte im getrennten SKOS-Vokabular |
| Distribution | Lokale `DocumentDistribution`, direkte Nutzung von `dcat:accessURL`, `dcat:downloadURL` und `dcat:mediaType` |
| Dokumentreferenz | Mindestens ein Ziel wird im Core Shape verlangt |

## 8. Abnahmekriterien der Shape-Phase

Die Shape-Phase ist abgeschlossen, weil:

1. T-Box und Referenzvokabulare syntaktisch validiert sind,
2. die abgestimmten Klassen und Properties vollständig umgesetzt sind,
3. die Referenzvokabulare getrennt versioniert vorliegen,
4. die SHACL-Anforderungen mit der implementierten T-Box übereinstimmen,
5. gültige und ungültige RDF-Testgraphen automatisiert geprüft werden,
6. alle freigegebenen Fehlercodes durch negative Testfälle abgedeckt sind,
7. die generierte HTML-Dokumentation und die repositoryweiten Tests das Modul
   enthalten.

## 9. Vorgemerkte Folgeaufgaben

Fachliche Pflichtmetadaten einzelner Dokumenttypen, strengere Rollenregeln und
weitere Integrationsvorgaben werden bei Bedarf in eigenen Profilen entwickelt.

## 10. Verständliches Beispiel

> Ein Lieferschein kann auf einen Vertrag verweisen. Der Document Core
> beschreibt Vertrag, Referenz und Datei, verlangt aber keine
> lieferscheinspezifische Pflichtrolle.
