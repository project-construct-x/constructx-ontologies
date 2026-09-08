# Fachliche SHACL-Anforderungen für das Document Core Modul

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Document Core Shapes  
**Umsetzungsstand:** Core-Shape-Graph und automatisierte Testfälle vorhanden

## 1. Zweck

Dieses Dokument beschreibt die verbindlichen Datenqualitätsanforderungen des
Document Core Moduls. Die ausführbare Umsetzung liegt in
`modules/core/document/shapes/conx-doc-core.shacl.ttl`.

## 2. Shape-Set

```text
Shape-Graph:  modules/core/document/shapes/conx-doc-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/document/core
Versions-IRI: https://www.construct-x.org/shapes/document/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/document/core#
Prefix:       conx-doc-sh
Version:      0.1.0
```

## 3. Validierungsprinzipien

- OWL beschreibt die offene Bedeutung der Begriffe; SHACL prüft konkrete
  Datenlieferungen im Core-Profil.
- Pflichtfelder und Maximalwerte werden nicht als harte OWL-Kardinalitäten in
  die offene T-Box geschrieben.
- Zusatzproperties bleiben erlaubt; das Shape-Set verwendet kein
  `sh:closed true`.
- Alle Core-Verstöße sind `sh:Violation`.
- Jede benannte Property Shape besitzt eine deutsche und eine englische
  Meldung mit stabilem Anforderungsbezeichner.
- Die Validierung benötigt keine RDFS- oder OWL-Inferenz.

## 4. Verantwortungsgrenzen

| Anforderung | Zuständiges Shape-Set | Regel im Document-Core-Shape |
| --- | --- | --- |
| Dokumente, Referenzen und Distributionen | `document/core` | Typisierung und Kernstruktur prüfen |
| Dokumenttypen und Dokumentstatus | `document/core` plus Referenzvokabulare | Werte gegen freigegebene Wertemengen prüfen |
| Identifikatoren | ADMS-/SKOS-Vertrag im `document/core` | Bestehende Identifier-Struktur wiederverwenden |
| Akteursrollen | `participation/core` oder Profil | Keine direkten Rollenproperties im Document Core |
| Provenienz | Provenienzprofil | Nicht im Document-Core-Shape |
| Evidence, Credentials und Signaturen | Trust-/Evidence-Profile | Nicht im Document-Core-Shape |
| Rechte und Zugriff | Policy-Profil | Nicht im Document-Core-Shape |
| UBL-Strukturen | Aktuell kein Mapping | Nur Vergleichsquelle, keine Validierungsabhängigkeit |

## 5. Shape-Katalog

| Shape-IRI | Typ | Target beziehungsweise Verwendung | Aufgabe |
| --- | --- | --- | --- |
| `conx-doc-sh:DocumentContextShape` | Node Shape | Subjekte von `hasDocumentReference` | Prüft kontextuelle Referenzwerte |
| `conx-doc-sh:DocumentCarrierShape` | Node Shape | Subjekte von `documentType` oder `hasDistribution` | Verlangt Typ `Document` oder `DocumentReference` |
| `conx-doc-sh:DocumentShape` | Node Shape | Dokumenttargets | Prüft Dokumentkern und Metadaten |
| `conx-doc-sh:DocumentReferenceShape` | Node Shape | Referenztargets | Prüft Dokumentreferenzen und Referenzziele |
| `conx-doc-sh:DocumentDistributionShape` | Node Shape | Distributionstargets | Prüft technische Distributionen |
| `conx-doc-sh:DocumentTypeConceptShape` | Node Shape | Werte von `documentType` | Prüft freigegebene Dokumenttypen |
| `conx-doc-sh:DocumentStatusConceptShape` | Node Shape | Werte von `documentStatus` | Prüft freigegebene Dokumentstatus |
| `conx-id-sh:ADMSIdentifierShape` | Node Shape aus `identifier/core` | Werte von `adms:identifier` | Prüft den gemeinsamen ADMS/SKOS-Identifier-Vertrag |
| `conx-doc-sh:StringOrLangStringShape` | wiederverwendbares Node Shape | Textwerte | Erlaubt `xsd:string` oder `rdf:langString` |
| `conx-doc-sh:NonEmptyStringOrLangStringShape` | wiederverwendbares Node Shape | Fachtexte | Verlangt nicht leere Textwerte |
| `conx-doc-sh:NonEmptyStringShape` | wiederverwendbares Node Shape | technische Textwerte | Verlangt nicht leere `xsd:string`-Werte |
| `conx-doc-sh:DateOrDateTimeShape` | wiederverwendbares Node Shape | Datumswerte | Erlaubt `xsd:date` oder `xsd:dateTime` |

## 6. Targets

### 6.1 Kontext und gemeinsam verwendete Properties

`DocumentContextShape` verwendet `sh:targetSubjectsOf
conx-doc:hasDocumentReference`. Jeder Wert muss eine explizit typisierte
`DocumentReference`-Ressource sein (`DOC-CTX-001`).

`DocumentCarrierShape` verwendet `sh:targetSubjectsOf conx-doc:documentType`
und `sh:targetSubjectsOf conx-doc:hasDistribution`. Das Subjekt muss explizit
als `Document` oder `DocumentReference` typisiert sein (`DOC-CAR-001`). Dadurch
werden gemeinsam verwendete Properties geprüft, ohne Referenzen zu Dokumenten
umzutypisieren.

### 6.2 Dokumente

`DocumentShape` verwendet:

- `sh:targetClass conx-doc:Document`,
- `sh:targetObjectsOf conx-doc:referencesDocument`,
- `sh:targetSubjectsOf conx-doc:documentStatus`.

### 6.3 Dokumentreferenzen

`DocumentReferenceShape` verwendet:

- `sh:targetClass conx-doc:DocumentReference`,
- `sh:targetObjectsOf conx-doc:hasDocumentReference`,
- `sh:targetSubjectsOf conx-doc:referencesDocument`.

### 6.4 Distributionen

`DocumentDistributionShape` verwendet:

- `sh:targetClass conx-doc:DocumentDistribution`,
- `sh:targetObjectsOf conx-doc:hasDistribution`,
- `sh:targetSubjectsOf conx-doc:fileName`.

Externe DCAT-Properties sind bewusst keine globalen Targets. Sie werden erst
an bereits erkannten `DocumentDistribution`-Ressourcen geprüft.

## 7. Node-Constraints

| ID | Fokus | Anforderung |
| --- | --- | --- |
| `DOC-CTX-001` | Kontextressource | `hasDocumentReference` verweist auf eine typisierte `DocumentReference` |
| `DOC-CAR-001` | Dokumentträger | Subjekt gemeinsamer Properties ist `Document` oder `DocumentReference` |
| `DOC-DOC-001` | `Document` | Fokuswert ist IRI oder Blank Node |
| `DOC-DOC-002` | `Document` | Expliziter Typ `conx-doc:Document` |
| `DOC-REF-001` | `DocumentReference` | Fokuswert ist IRI oder Blank Node |
| `DOC-REF-002` | `DocumentReference` | Expliziter Typ `conx-doc:DocumentReference` |
| `DOC-DIST-001` | `DocumentDistribution` | Fokuswert ist IRI oder Blank Node |
| `DOC-DIST-002` | `DocumentDistribution` | Expliziter Typ `conx-doc:DocumentDistribution` |

## 8. Property-Constraints für `Document`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `DOC-DOC-010` | `title` | 0 | offen | Nicht leerer String oder sprachmarkiertes Literal |
| `DOC-DOC-011` | `description` | 0 | offen | Nicht leerer String oder sprachmarkiertes Literal |
| `DOC-DOC-012` | `language` | 0 | offen | Nicht leerer `xsd:string` |
| `DOC-DOC-020` | `documentType` | 0 | 1 | IRI aus dem freigegebenen Dokumenttyp-Vokabular |
| `DOC-DOC-021` | `documentStatus` | 0 | 1 | IRI aus dem freigegebenen Dokumentstatus-Vokabular |
| `DOC-DOC-030` | `version` | 0 | 1 | Nicht leerer `xsd:string` |
| `DOC-DOC-040` | `created` | 0 | 1 | `xsd:date` oder `xsd:dateTime` |
| `DOC-DOC-041` | `issued` | 0 | 1 | `xsd:date` oder `xsd:dateTime` |
| `DOC-DOC-042` | `modified` | 0 | 1 | `xsd:date` oder `xsd:dateTime` |
| `DOC-DOC-043` | `validFrom` | 0 | 1 | `xsd:date` oder `xsd:dateTime` |
| `DOC-DOC-044` | `validUntil` | 0 | 1 | `xsd:date` oder `xsd:dateTime` |
| `DOC-DOC-045` | Gültigkeitsreihenfolge | - | - | `validFrom` liegt nicht nach `validUntil` |
| `DOC-DOC-050` | `hasDistribution` | 0 | offen | Typisierte `DocumentDistribution`-Ressource |
| `DOC-DOC-060` | `adms:identifier` | 0 | offen | Gültig strukturierte ADMS-Identifier-Ressource |

Für eine eindeutige Vergleichbarkeit sollten `validFrom` und `validUntil`
denselben Datentyp verwenden.

## 9. Property-Constraints für `DocumentReference`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `DOC-REF-010` | `referencesDocument` | 0 | 1 | Explizit typisierte `Document`-Ressource |
| `DOC-REF-011` | `dcterms:references` | 0 | 1 | IRI einer externen Dokumentressource |
| `DOC-REF-012` | `hasDistribution` | 0 | offen | Typisierte `DocumentDistribution`-Ressource |
| `DOC-REF-013` | Referenzziel | 1 Alternative | - | Dokument, externe IRI oder Distribution |
| `DOC-REF-020` | `documentType` | 0 | 1 | IRI aus dem freigegebenen Dokumenttyp-Vokabular |
| `DOC-REF-030` | `adms:identifier` | 0 | offen | Gültig strukturierte ADMS-Identifier-Ressource |

## 10. Property-Constraints für `DocumentDistribution`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `DOC-DIST-010` | `dcat:accessURL` | 0 | offen | IRI |
| `DOC-DIST-011` | `dcat:downloadURL` | 0 | offen | IRI |
| `DOC-DIST-020` | `fileName` | 0 | 1 | Nicht leerer `xsd:string` |
| `DOC-DIST-030` | `dcat:mediaType` | 0 | 1 | IANA-orientierte IRI |

Eine Distribution darf ohne Zugriffs-URL als technischer Platzhalter
existieren. Das Core-Shape erzwingt kein Storage- oder Archivmodell.

## 11. Identifier-Constraints

Die Fehlercodes dieses Abschnitts werden vom importierten Shape-Graph
`identifier/core` bereitgestellt. Das Document Shape definiert nur, an welchen
Dokument- und Referenzressourcen `adms:identifier` verwendet wird.

| ID | Anforderung |
| --- | --- |
| `ID-001` | Identifier-Ressource ist explizit als `adms:Identifier` typisiert |
| `ID-002` | Genau eine literale `skos:notation` |
| `ID-003` | Höchstens eine `adms:schemaAgency` als `xsd:string` |

## 12. Kontrollierte Werte

Das Document-Type-Vokabular umfasst `contract`, `invoice`, `deliveryNote`,
`certificate`, `report`, `plan`, `evidenceDocument` und `other`.

Das Document-Status-Vokabular umfasst `draft`, `issued`, `superseded`,
`withdrawn`, `expired` und `archived`.

Die Shapes prüfen IRI, `skos:Concept`, den lokalen Klassentyp und eine
geschlossene `sh:in`-Liste. Vokabularerweiterungen erfordern daher eine
bewusste Versionierung von Referenzvokabular und Shape-Set.

## 13. Testfälle

Gültige Testgraphen:

- `minimal-document.ttl`,
- `complete-document.ttl`,
- `multiple-distributions.ttl`,
- `document-references.ttl`,
- `document-with-participation.ttl`.

Ungültige Testgraphen:

- `invalid-document-typing.ttl`,
- `invalid-document-references.ttl`,
- `invalid-distributions.ttl`,
- `invalid-controlled-values.ttl`,
- `invalid-metadata-and-identifiers.ttl`.

Die automatisierte Suite prüft alle gültigen und ungültigen Graphen, die
SHACL-SHACL-Konformität, die Shape-Metadaten, zweisprachige Meldungen und die
Abdeckung aller freigegebenen Anforderungsbezeichner.

## 14. Nicht zu validieren im Document-Core-Shape

- UBL-Konformität oder UBL-Mappings,
- digitale Signaturgültigkeit und Credential-Status,
- Evidence- oder Requirement-Erfüllung,
- direkte Aussteller-, Autor-, Publisher-, Sender- oder Empfängerrollen,
- Rechte, Zugriff, Vertraulichkeit und Workflowstatus,
- URL-Erreichbarkeit oder Dateiexistenz,
- DMS-, Archiv-, Storage- und Aufbewahrungsregeln,
- fachliche Pflichtmetadaten einzelner Dokumenttypen.

Diese Anforderungen gehören in spezialisierte Module oder Profile.

## 15. Verständliches Beispiel

> Ein Dokument mit Titel und Typ sowie einer PDF-Distribution ist im Core
> gültig. Verweist die Distribution weder auf einen Download noch auf eine
> Zugriffsadresse, meldet das Shape einen Strukturfehler.
