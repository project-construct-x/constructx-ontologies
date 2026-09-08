# Fachliches Konzeptmodell des Document Core Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`  
**Umsetzungsstand:** T-Box, Referenzvokabulare und Core Shapes umgesetzt

## 1. Ziel

Das Konzeptmodell beschreibt den implementierten dokumentbezogenen Kern des
Construct-X-Ontologienetzwerks. Es führt die Quellenanalyse, die bestätigten
Scope-Entscheidungen und den Begriffskatalog in einem konsistenten fachlichen
Modell zusammen.

Die vollständigen Mermaid-Diagramme stehen im
[fachlichen Document-Konzeptdiagramm](diagrams/document-concept-model.md).
Klassen und Properties sind im [Begriffskatalog](term-catalog.md)
dokumentiert. Die Modulgrenzen stehen in [module-boundaries.md](module-boundaries.md).

## 2. Modellkern

Der MVP definiert fünf lokale Kernbegriffe:

```text
Document
DocumentReference
DocumentDistribution
DocumentType
DocumentStatus
```

Diese Begriffe bilden drei unterschiedliche Ebenen ab:

1. dokumentartiger Inhalt,
2. kontextbezogene Bezugnahme auf ein Dokument,
3. technische Bereitstellung als Datei, Download oder vergleichbare
   Distribution.

Akteursrollen, Signaturen, Credentials, Evidence, Rechte, Workflows,
Archivierung und Storage werden nicht im Document Core definiert.

## 3. Grundmodell

```text
fachlicher Kontext
  └── DocumentReference
        ├── referencesDocument -> Document
        └── hasDistribution    -> DocumentDistribution

Document
  ├── documentType
  ├── documentStatus
  ├── Identifikatoren
  ├── Metadaten
  └── hasDistribution -> DocumentDistribution
```

Eine fachliche Ressource verweist nicht zwingend direkt auf eine Datei. Sie
verweist auf eine Dokumentreferenz. Die Dokumentreferenz kann auf ein im Graph
modelliertes Dokument, eine externe Dokumentressource oder eine konkrete
Distribution zeigen.

## 4. Klassen

### 4.1 `Document`

`Document` ist eine eigene Construct-X-Klasse für ein dokumentartiges
Informationsobjekt. Der Begriff ist unabhängig von einer konkreten Datei.

Ein Dokument kann sein:

- eine Rechnung,
- ein Vertrag,
- ein Zertifikat,
- ein Bericht,
- ein Plan oder eine Zeichnung,
- ein Nachweisdokument.

Ein Dokument ist nicht automatisch:

- eine PDF-Datei,
- ein Download-Link,
- ein DMS-Record,
- ein Credential,
- eine Evidence,
- ein signiertes Artefakt,
- ein Workflowobjekt.

Externe Begriffe wie `schema:DigitalDocument`, `foaf:Document` oder Dublin-
Core-Ressourcenbegriffe können später als Alignmentziele dienen. Sie ersetzen
nicht den lokalen Construct-X-Kernbegriff.

### 4.2 `DocumentReference`

`DocumentReference` ist eine eigenständige Ressource für eine
kontextbezogene Bezugnahme auf ein Dokument.

Sie ist erforderlich, wenn die Referenz selbst fachliche Informationen tragen
kann, zum Beispiel:

- welcher Kontext das Dokument referenziert,
- welche Art von Dokument erwartet wird,
- welche Version oder Sprache referenziert wird,
- ob die Referenz auf ein modelliertes Dokument oder nur auf eine externe
  Ressource zeigt,
- welche Distribution im Kontext verwendet wird.

Eine direkte Property vom fachlichen Kontext auf eine Datei reicht dafür nicht
aus.

### 4.3 `DocumentDistribution`

`DocumentDistribution` beschreibt eine konkrete technische Ausprägung oder
Bereitstellung eines Dokuments. Der Begriff ist DCAT-nah gedacht.

Beispiele:

- eine PDF-Datei,
- eine XML-Datei,
- eine HTML-Ansicht,
- ein Download-Link,
- eine abrufbare externe Datei.

Mehrere Distributionen können dasselbe Dokument repräsentieren:

```text
Prüfbericht
  ├── PDF-Distribution
  ├── XML-Distribution
  └── HTML-Distribution
```

Eine Distribution ist kein Storage-, Upload-, Archiv- oder Repositorymodell.

### 4.4 `DocumentType`

`DocumentType` ist ein kontrollierter Dokumenttyp. Dokumenttypen werden als
Werte eines Referenzvokabulars vorgesehen und nicht als lokale Unterklassen von
`Document` modelliert.

Dadurch bleibt der Core stabil:

```text
Document
  documentType -> document-type:invoice
```

statt:

```text
InvoiceDocument rdfs:subClassOf Document
```

Fachliche Profile können später strengere Regeln für bestimmte
Dokumenttypen festlegen.

### 4.5 `DocumentStatus`

`DocumentStatus` ist ein kontrollierter dokumentbezogener Zustand.

Der Status beschreibt nicht den Dokumenttyp und nicht den Prozessschritt.

```text
Dokumenttyp:    Zertifikat
Dokumentstatus: abgelaufen
```

Workflowzustände wie "in Prüfung", "wartet auf Freigabe" oder "zugewiesen an
Rechtsabteilung" gehören nicht in den Document Core.

## 5. Dokument, Referenz und Distribution

Die drei Begriffe dürfen nicht vermischt werden.

| Frage | Modellbegriff |
| --- | --- |
| Was ist der dokumentartige Inhalt? | `Document` |
| Warum oder wo wird darauf verwiesen? | `DocumentReference` |
| Welche konkrete Datei oder technische Bereitstellung gibt es? | `DocumentDistribution` |

Beispiel:

```text
Bestellung 123
  hasDocumentReference -> Vertragsanlage-Referenz

Vertragsanlage-Referenz
  referencesDocument -> Vertragsanlage A
  hasDistribution    -> vertragsanlage-a.pdf

Vertragsanlage A
  documentType   -> contract
  documentStatus -> issued
```

Diese Trennung erlaubt, dass ein Dokument ohne Datei bekannt ist, mehrere
Dateien besitzt oder nur extern referenziert wird.

## 6. Metadaten

Der Document Core soll allgemeine Metadaten vorsehen. Sie sind im offenen Core
nicht pauschal verpflichtend.

| Metadatum | Bedeutung |
| --- | --- |
| Titel | Anzeigename oder fachlicher Dokumenttitel |
| Beschreibung | Freitextbeschreibung |
| Sprache | Sprache des Dokumentinhalts |
| Version | Dokumentversion oder Ausgabebezeichnung |
| Erstellt | Zeitpunkt oder Datum der Erzeugung |
| Ausgegeben | fachliches Ausstellungs- oder Ausgabedatum |
| Geändert | letzte bekannte Änderung |
| Gültig ab | Beginn der fachlichen Gültigkeit |
| Gültig bis | Ende der fachlichen Gültigkeit |

Allgemeine Metadaten werden als lokale `conx-doc`-Properties geführt und über
`rdfs:seeAlso` mit passenden Dublin-Core- und Schema.org-Begriffen verbunden.
Für technische Distributionen werden `dcat:accessURL`, `dcat:downloadURL` und
`dcat:mediaType` direkt verwendet.

## 7. Identifikatoren

Dokumentkennungen folgen dem bestehenden Construct-X-ADMS-/SKOS-Muster:

```text
Document
  └── adms:identifier
        └── adms:Identifier
              ├── skos:notation
              └── adms:schemaAgency
```

Die Ressourcen-IRI und fachliche Kennungen bleiben getrennt. Der Document Core
führt keine eigenen Nummernproperties wie `documentNumber`, `invoiceNumber`,
`contractNumber`, `uuidValue` oder `archiveId` ein.

## 8. Akteursrollen

Akteursrollen am Dokument werden über `core/participation` modelliert.

```text
Agent
  └── spielt Rolle im Kontext Document oder DocumentReference
```

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
```

Der Document Core führt deshalb keine direkten Properties für Aussteller,
Sender, Empfänger, Autor oder Publisher ein. Profile können später
festlegen, dass bestimmte Rollen für bestimmte Dokumenttypen verpflichtend
sind.

## 9. Provenienz

Provenienz beschreibt Entstehung, Ableitung, Revision oder Verarbeitung eines
Dokuments.

Beispiele:

```text
PDF wurde aus Datensatz Y erzeugt
Dokumentversion 3 ersetzt Dokumentversion 2
Prüfbericht wurde durch Aktivität X generiert
```

Diese Semantik gehört nicht in den Document Core. PROV-O bleibt dafür eine
spätere Alignment- oder Profilquelle.

## 10. UBL als Vergleichsquelle

UBL zeigt, dass Dokumentreferenzen und technische Anhänge in
Geschäftsprozessen eigene Metadaten tragen können. Diese Beobachtung stützt
die Trennung von `DocumentReference` und `DocumentDistribution`.

Für den MVP gilt aber:

- kein UBL-Import,
- keine UBL-Kopien,
- kein UBL-Mapping als Liefergegenstand,
- keine UBL-Pflichtstruktur im Document Core.

## 11. Nicht im Document Core

Folgende Themen gehören nicht in den Document Core:

- Rechnungs-, Lieferschein-, Vertrags-, Zertifikats- oder Berichtsklassen,
- direkte Akteursproperties wie Aussteller, Sender, Empfänger, Autor oder
  Publisher,
- Signatur-, Siegel-, Zeitstempel- und Trust-List-Modelle,
- Verifiable Credentials und Data-Integrity-Proofs,
- Evidence-/Requirement-Semantik,
- Workflowstatus, Freigabeprozesse und Aufgabensteuerung,
- Zugriffskontrolle, Berechtigungen und Policy-Auswertung,
- Archivierung, Aktenpläne, Retention und Records Management,
- Volltext, OCR, Seiten, Abschnitte und Annotationen,
- Storage-, Upload-, Repository- oder DMS-spezifische Konzepte,
- UBL-Abhängigkeiten oder UBL-Mappings.

## 12. Modellentscheidungen

| Thema | Entscheidung |
| --- | --- |
| Lokaler Dokumentbegriff | Eigene Klasse `Document` |
| Referenzen | Eigene Klasse `DocumentReference` |
| Dateien | DCAT-nahe Klasse `DocumentDistribution` |
| Dokumenttypen | Kontrolliertes MVP-Vokabular |
| Dokumentstatus | Kontrolliertes MVP-Vokabular |
| Identifikatoren | ADMS-/SKOS-Muster wiederverwenden |
| Akteursrollen | Über `core/participation` modellieren |
| Provenienz | Nicht im Kern; später PROV-O-Alignment oder Profil |
| UBL | Nur Vergleichsquelle |

## 13. Abgeschlossene Detailentscheidungen

| Thema | Entscheidung |
| --- | --- |
| Externe Properties | Lokale `conx-doc`-Metadatenproperties mit Alignment; technische DCAT-Properties direkt verwenden |
| Gültigkeit | Optionale Angaben `validFrom` und `validUntil` |
| Typ-Vokabular | `contract`, `invoice`, `deliveryNote`, `certificate`, `report`, `plan`, `evidenceDocument`, `other` |
| Status-Vokabular | `draft`, `issued`, `superseded`, `withdrawn`, `expired`, `archived` |
| Distribution | `dcat:accessURL`, `dcat:downloadURL` und `dcat:mediaType`; lokales `fileName` |
| DocumentReference | Mindestens ein Ziel im Core Shape: Dokument, externe Ressource oder Distribution |

## 14. Implementierungsstand

`module.yaml`, `ontology/conx-doc.ttl`, die Referenzvokabulare,
`shapes/conx-doc-core.shacl.ttl`, Beispiele und Tests setzen die bestätigten
[SHACL-Anforderungen](shacl-requirements.md) um.

## 15. Verständliches Beispiel

> Ein Prüfbericht ist ein Document. Seine PDF-Datei ist eine Distribution.
> Verweist ein Vertrag auf den Bericht, wird dafür eine DocumentReference
> verwendet und nicht eine zweite Kopie des Dokuments angelegt.
