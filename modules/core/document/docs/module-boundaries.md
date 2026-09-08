# Modulgrenzen des Document Core Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`  

## 1. Ziel

Dieses Dokument ordnet die Dokumentbegriffe den zuständigen Construct-X-
Modulen zu. Das Document Core Modul soll dokumentartige Ressourcen,
Dokumentreferenzen und technische Distributionen beschreiben, ohne
Agentenrollen, Provenienz, Evidence, Credentials, Signaturen, Rechte oder
Workflows zu übernehmen.

## 2. Leitprinzipien

1. `Document` beschreibt ein dokumentartiges Informationsobjekt.
2. `DocumentDistribution` beschreibt eine konkrete technische Ausprägung oder
   Bereitstellung.
3. `DocumentReference` beschreibt eine kontextbezogene Bezugnahme.
4. Fachliche Dokumenttypen und Dokumentstatus werden kontrollierte
   Referenzwerte, keine Klassenhierarchie.
5. Akteursrollen am Dokument laufen über `core/participation`.
6. Entstehung, Ableitung und Revision gehören in ein Provenienzprofil.
7. UBL ist Vergleichsquelle, aber keine Abhängigkeit und kein geplantes
   Mapping.

## 3. Zuständigkeit nach Modul

| Modul | Besitzt | Besitzt ausdrücklich nicht |
| --- | --- | --- |
| `core/document` | `Document`, `DocumentReference`, `DocumentDistribution`, Dokumenttyp, Dokumentstatus, allgemeine Dokumentmetadaten | Akteursrollen, Signaturen, Credentials, Evidence, Workflow, Rechte, Storage |
| `core/agent` | Allgemeiner Akteurbegriff | Dokumentmetadaten und Dokumentreferenzen |
| `core/participation` | Agent spielt Rolle in einem Kontext | Dokumentinhalt, Datei- oder Distributionsemantik |
| `core/person` | Intrinsische Personendaten | Autor-, Aussteller- oder Empfängerproperties am Dokument |
| `core/organization` | Organisationsstammdaten und Organisationsstruktur | Publisher-, Sender- oder Issuerproperties am Dokument |
| `core/contact` | Kontaktierbarkeit | Dokumentzustellung, Dokumentinhalt oder Dokumentstatus |
| `core/address` | Adressen und Adresszuordnungen | Dokumente, Dateien oder Distributionen |
| späteres Provenienzprofil | Erzeugung, Ableitung, Revision, Verarbeitung | Allgemeine Dokumentstammdaten |
| späteres Evidence-/Credential-Profil | Nachweissemantik, Credential-Prüfbarkeit, Widerruf | Allgemeiner Dokumentkern |
| späteres Rechte-/Policy-Profil | Zugriff, Lizenzbedingungen, Weitergaberegeln | Dokumentkern und technische Distribution |
| Domain-Module | Pflichtdokumente und fachliche Dokumentrollen je Prozess | Allgemeiner Document-Core-Begriff |

## 4. Abgrenzung zu `core/participation`

Akteursrollen am Dokument werden nicht im Document Core als eigene Properties
angelegt.

```text
Document
  <- Kontext einer Participation
Agent
  -> spielt Rolle issuer / recipient / author / publisher
```

Beispiele:

```text
Rechnung 4711
  Participation: Organisation A als issuer
  Participation: Organisation B als recipient
```

```text
Tragwerksplan Version 3
  Participation: Person X als author
  Participation: Organisation Y als publisher
```

Das verhindert Properties wie `documentIssuer`, `documentSender`,
`documentReceiver`, `documentAuthor` und `documentPublisher` im Kern.

## 5. Abgrenzung zu Provenienz

Provenienz beschreibt, wie ein Dokument entstanden ist, woraus es abgeleitet
wurde oder welche Aktivität es erzeugt hat.

```text
Dokumentversion 3
  wasDerivedFrom -> Dokumentversion 2
  wasGeneratedBy -> Exportlauf X
```

Solche Aussagen sind nicht dasselbe wie Dokumentmetadaten oder
Akteursrollen. Der Document Core kann später an PROV-O ausgerichtet werden,
kopiert aber keine Provenienzsemantik in den Kern.

## 6. Abgrenzung zu Evidence und Credentials

Ein Dokument kann als Nachweis verwendet werden. Das bedeutet aber nicht, dass
jedes Dokument eine Evidence- oder Credential-Ressource ist.

```text
Document: PDF eines Zertifikats
Evidence-Profil: Dieses Dokument belegt Requirement X
Credential-Profil: Dieses Credential wurde von Issuer Y für Subject Z ausgestellt
```

Requirement-Erfüllung, Credential-Status, Widerruf, kryptografische Proofs und
Verifikationsmethoden gehören nicht in `core/document`.

## 7. Abgrenzung zu Signatur und Vertrauen

Der Document Core modelliert keine elektronischen Signaturen, Siegel,
Zeitstempel, Trust Lists oder eIDAS-/ETSI-Prüflogik.

Eine signierte PDF-Datei kann als Distribution eines Dokuments beschrieben
werden. Die Signaturgültigkeit und rechtliche Beweiskraft gehören in ein
späteres Trust- oder Evidence-Profil.

## 8. Abgrenzung zu Rechte und Zugriff

Der Document Core besitzt keine Zugriffskontrolle. Eine Datei kann existieren,
ohne dass das Modell beschreibt, wer sie lesen, weitergeben, löschen oder
lizenzieren darf.

Lizenz- oder Rechtehinweise können später als einfache Metadaten oder in
einem Policy-Profil bewertet werden. ODRL bleibt dafür eine mögliche
Alignmentquelle.

## 9. Abgrenzung zu UBL

UBL bleibt für das Document Core Modul eine Vergleichsquelle. Insbesondere
`DocumentReference`, `Attachment` und `ExternalReference` zeigen, welche
fachlichen Informationen in Geschäftsprozessen auftreten können.

Für das MVP gilt:

- kein `owl:imports` auf UBL,
- keine lokalen UBL-Kopien,
- kein UBL-Mapping als Liefergegenstand,
- keine UBL-Pflichtstruktur im Core.

## 10. T-Box- und A-Box-Trennung

### T-Box-Begriffe

- `Document`
- `DocumentReference`
- `DocumentDistribution`
- `DocumentType`
- `DocumentStatus`
- `hasDocumentReference`
- `referencesDocument`
- `hasDistribution`
- `documentType`
- `documentStatus`
- lokale Metadatenproperties für Titel, Beschreibung, Sprache, Version,
  Datumsangaben und Dateiname,
- direkte Nutzung von `dcterms:references`, `dcat:accessURL`,
  `dcat:downloadURL` und `dcat:mediaType`

### A-Box beziehungsweise Referenzvokabulare

- `document-type`: kontrollierte Dokumenttypen,
- `document-status`: kontrollierte Dokumentstatus.

Konkrete Dokumente, Dokumentnummern, Dateien, URLs und Rollenbeziehungen sind
Instanzdaten der Datenhalter.

## 11. Import- und Alignment-Strategie

| Quelle | Einordnung |
| --- | --- |
| Dublin Core Terms | Alignment für lokale allgemeine Metadaten; `dcterms:references` für externe Referenzziele |
| DCAT 3 | Direkte Wiederverwendung von `accessURL`, `downloadURL` und `mediaType`; Alignment für Distributionen |
| ADMS/SKOS | Bestehendes Muster für Identifikatoren und kontrollierte Werte |
| Schema.org | Alignmentquelle für Web-Interoperabilität |
| FOAF | Einfaches Alignment für `foaf:Document`, nicht als Kernmodell |
| PROV-O | Späteres Provenienzprofil oder Alignment |
| UBL | Vergleichsquelle, keine Abhängigkeit |

Alle verwendeten externen Namespaces werden als `referenced-not-imported` in
`module.yaml` dokumentiert. Die T-Box setzt keine `owl:imports`.

## 12. Verständliches Beispiel

> Das Document-Modul kann festhalten, dass ein Prüfbericht existiert und als
> PDF verfügbar ist. Wer ihn signiert hat, ob die Signatur gültig ist und wer
> ihn lesen darf, bleibt bei Signatur-, Vertrauens- und Zugriffsmodellen.
