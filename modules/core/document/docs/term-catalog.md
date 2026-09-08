# Begriffskatalog für das Document Core Modul

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`  
**Umsetzungsstand:** T-Box, Referenzvokabulare und Core Shapes umgesetzt

## 1. Zweck

Dieser Katalog beschreibt die lokalen Begriffe der Document-T-Box 0.1.0 und die
zugehörigen Referenzvokabulare. Die genannten Kardinalitäten werden durch das
Core Shape geprüft und sind keine harten OWL-Restriktionen.

## 2. Namensräume

### Document Ontologie

```text
Ontologie-IRI: https://www.construct-x.org/ontology/document
Versions-IRI:  https://www.construct-x.org/ontology/document/0.1.0
Namespace:     https://www.construct-x.org/ontology/document#
Prefix:        conx-doc
```

### Dokumenttyp-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/document-type
Versions-IRI:  https://www.construct-x.org/vocab/document-type/0.1.0
Namespace:     https://www.construct-x.org/vocab/document-type#
Prefix:        document-type
```

### Dokumentstatus-Vokabular

```text
Vokabular-IRI: https://www.construct-x.org/vocab/document-status
Versions-IRI:  https://www.construct-x.org/vocab/document-status/0.1.0
Namespace:     https://www.construct-x.org/vocab/document-status#
Prefix:        document-status
```

## 3. Klassen

### 3.1 `conx-doc:Document`

| Punkt | Festlegung |
| --- | --- |
| Definition | Dokumentartiges Informationsobjekt, unabhängig von einer konkreten Datei |
| Modul | `core/document` |
| Verwendung | Rechungen, Verträge, Zertifikate, Berichte, Pläne und vergleichbare dokumentartige Ressourcen |
| Abgrenzung | Keine Datei, kein Ordner, kein DMS-Record, kein Credential-Modell |
| Externe Quellen | Dublin Core, Schema.org `DigitalDocument`, FOAF `Document` als Alignmentquellen |

### 3.2 `conx-doc:DocumentReference`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontextbezogene Bezugnahme auf ein Dokument, eine externe Dokumentressource oder eine Distribution |
| Modul | `core/document` |
| Verwendung | Erlaubt Referenzmetadaten, ohne den fachlichen Kontext direkt an eine Datei zu koppeln |
| Abgrenzung | Keine domain-spezifische Pflichtreferenz und kein UBL-Mapping |
| Externe Quellen | UBL `DocumentReference` als Vergleichsquelle |

### 3.3 `conx-doc:DocumentDistribution`

| Punkt | Festlegung |
| --- | --- |
| Definition | Konkrete technische Bereitstellung oder Ausprägung eines Dokuments |
| Modul | `core/document` |
| Verwendung | PDF-Datei, XML-Datei, Download-Link oder andere abrufbare Repräsentation |
| Abgrenzung | Kein Storage-, Upload-, Archiv- oder Repositorymodell |
| Externe Quellen | DCAT `Distribution` als primäre Alignmentquelle |

### 3.4 `conx-doc:DocumentType`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontrollierter Typ eines Dokuments |
| Modul | T-Box-Klasse in `core/document`, Werte im SKOS-Vokabular |
| Verwendung | Fachübergreifende Startwerte für Profile und Datenvalidierung |
| Abgrenzung | Dokumenttypen werden nicht als lokale Unterklassen von `Document` modelliert |
| Externe Quellen | SKOS, Dublin Core `type`, UBL `DocumentTypeCode` als Vergleich |

### 3.5 `conx-doc:DocumentStatus`

| Punkt | Festlegung |
| --- | --- |
| Definition | Kontrollierter dokumentbezogener Zustand |
| Modul | T-Box-Klasse in `core/document`, Werte im SKOS-Vokabular |
| Verwendung | Entwurf, ausgegeben, ersetzt, widerrufen, abgelaufen oder archiviert |
| Abgrenzung | Keine Workflowzustände wie "in Prüfung" oder "wartet auf Freigabe" |
| Externe Quellen | SKOS, ADMS `status`, Schema.org `creativeWorkStatus`, UBL `DocumentStatusCode` als Vergleich |

## 4. Objektproperties

### 4.1 `conx-doc:hasDocumentReference`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine beliebige fachliche Kontextressource mit einer Dokumentreferenz |
| Domain | Keine harte `rdfs:domain` |
| Range | `conx-doc:DocumentReference` |
| Kardinalität | `0..n` |
| Hinweis | Profile können für bestimmte Kontextklassen Pflichtreferenzen verlangen |

### 4.2 `conx-doc:referencesDocument`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft eine Dokumentreferenz mit einem im Graph modellierten Dokument |
| Domain | `conx-doc:DocumentReference` |
| Range | `conx-doc:Document` |
| Kardinalität | `0..1` im Core-Shape zu prüfen |
| Hinweis | Externe Dokumente können alternativ über URI-/Distribution-Bezüge beschrieben werden |

### 4.3 `conx-doc:hasDistribution`

| Punkt | Festlegung |
| --- | --- |
| Definition | Verknüpft ein Dokument oder eine Dokumentreferenz mit einer technischen Distribution |
| Domain | Keine harte Domain oder Union-Domain in der offenen T-Box |
| Range | `conx-doc:DocumentDistribution` |
| Kardinalität | `0..n` |
| Externe Quelle | DCAT `distribution` als Alignmentquelle |

### 4.4 `conx-doc:documentType`

| Punkt | Festlegung |
| --- | --- |
| Definition | Weist einem Dokument oder einer Dokumentreferenz einen kontrollierten Dokumenttyp zu |
| Domain | Keine harte Domain oder fachlich `Document`/`DocumentReference` |
| Range | `conx-doc:DocumentType` |
| Kardinalität | `0..1` im Core-Shape zu prüfen |
| Hinweis | Profile können strengere Pflichtangaben verlangen |

### 4.5 `conx-doc:documentStatus`

| Punkt | Festlegung |
| --- | --- |
| Definition | Weist einem Dokument einen kontrollierten dokumentbezogenen Status zu |
| Domain | Fachlich `conx-doc:Document` |
| Range | `conx-doc:DocumentStatus` |
| Kardinalität | `0..1` im Core-Shape zu prüfen |
| Hinweis | Workflowstatus bleibt ausserhalb des Document Core |

## 5. Datenproperties und externe Properties

Allgemeine Dokumentmetadaten werden lokal definiert und mit externen Begriffen
ausgerichtet. Die technischen DCAT-Properties werden direkt verwendet.

| Property | Bedeutung | Range | Alignment oder Wiederverwendung |
| --- | --- | --- | --- |
| `conx-doc:title` | Anzeigename oder fachlicher Titel | `xsd:string` oder `rdf:langString` | `dcterms:title`, `schema:name` |
| `conx-doc:description` | Freitextbeschreibung | `xsd:string` oder `rdf:langString` | `dcterms:description`, `schema:description` |
| `conx-doc:language` | Sprache des Inhalts | `xsd:string` | `dcterms:language`, `schema:inLanguage` |
| `conx-doc:version` | Dokumentversion oder Ausgabebezeichnung | `xsd:string` | `schema:version` |
| `conx-doc:created` | Erstellungsdatum oder -zeitpunkt | `xsd:date` oder `xsd:dateTime` | `dcterms:created`, `schema:dateCreated` |
| `conx-doc:issued` | fachliches Ausgabedatum oder -zeitpunkt | `xsd:date` oder `xsd:dateTime` | `dcterms:issued` |
| `conx-doc:modified` | letzte bekannte Änderung | `xsd:date` oder `xsd:dateTime` | `dcterms:modified`, `schema:dateModified` |
| `conx-doc:validFrom` | Beginn der fachlichen Gültigkeit | `xsd:date` oder `xsd:dateTime` | `schema:validFrom`, `dcterms:valid` |
| `conx-doc:validUntil` | Ende der fachlichen Gültigkeit | `xsd:date` oder `xsd:dateTime` | `schema:validThrough`, `dcterms:valid` |
| `conx-doc:fileName` | Name einer konkreten Datei | `xsd:string` | UBL `FileName` nur als Vergleich |
| `dcat:accessURL` | allgemeine Zugriffsadresse | IRI | direkte Wiederverwendung |
| `dcat:downloadURL` | direkte Download-Adresse | IRI | direkte Wiederverwendung |
| `dcat:mediaType` | IANA-orientierter Medientyp | IRI | direkte Wiederverwendung |

## 6. MVP-Werte

### 6.1 Dokumenttypen

Das Referenzvokabular 0.1.0 enthält:

```text
document-type:contract
document-type:invoice
document-type:deliveryNote
document-type:certificate
document-type:report
document-type:plan
document-type:evidenceDocument
document-type:other
```

### 6.2 Dokumentstatus

Das Referenzvokabular 0.1.0 enthält:

```text
document-status:draft
document-status:issued
document-status:superseded
document-status:withdrawn
document-status:expired
document-status:archived
```

## 7. Nicht als lokale Begriffe vorgesehen

- `issuer`, `sender`, `receiver`, `author`, `publisher` als direkte
  Document-Core-Properties,
- `Attachment` als lokale Kernklasse,
- UBL-spezifische Klassen oder Properties,
- Workflowstatus,
- Signatur-, Siegel-, Credential- oder Evidence-Klassen,
- Storage-, Repository-, Upload- oder Archivklassen.

## 8. Verständliches Beispiel

> Ein Prüfbericht wird als `Document` beschrieben. Die PDF-Datei ist eine
> `DocumentDistribution`; eine Referenz aus einem Vertrag ist eine
> `DocumentReference`. So wird nicht jede Datei zu einem neuen Dokument.
