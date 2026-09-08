# Document Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Document Core Shapes

Die Document Core Shapes validieren die allgemeinen, fachübergreifenden
Datenverträge der Construct-X Dokumentontologie. Die T-Box bleibt unter der
Open-World-Annahme semantisch offen; das Core-Profil prüft konkrete
Datenlieferungen.

```text
Shape-Graph:  modules/core/document/shapes/conx-doc-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/document/core
Versions-IRI: https://www.construct-x.org/shapes/document/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/document/core#
Version:      0.1.0
```

Der Shape-Graph importiert den versionierten Vertrag
`https://www.construct-x.org/shapes/identifier/core/0.1.0`.

## 1. Target-Strategie

`Document`, `DocumentReference` und `DocumentDistribution` werden über ihre
Klassen sowie über eindeutige eingehende oder lokale Properties aktiviert.
Die gemeinsam verwendbaren Properties `documentType` und `hasDistribution`
aktivieren einen separaten `DocumentCarrierShape`. Dieser verlangt, dass das
Subjekt als `Document` oder `DocumentReference` typisiert ist, ohne eine
Dokumentreferenz zusätzlich zum Dokument zu machen.

Externe DCAT-Properties sind bewusst keine globalen Targets. Sie werden nur an
Ressourcen geprüft, die bereits als `DocumentDistribution` erkannt wurden.
Dadurch greift das Modul nicht in beliebige externe DCAT-Datengraphen ein.

## 2. Geprüfte Verträge

- Dokumente, Referenzen und Distributionen müssen Ressourcen und explizit mit
  der jeweils vorgesehenen Construct-X-Klasse typisiert sein.
- Werte von `hasDocumentReference` müssen typisierte
  `DocumentReference`-Ressourcen sein.
- Eine `DocumentReference` muss mindestens ein Ziel besitzen: ein modelliertes
  Dokument, eine externe IRI über `dcterms:references` oder eine Distribution.
- `referencesDocument` und `dcterms:references` dürfen jeweils höchstens
  einmal vorkommen.
- `documentType` und `documentStatus` verwenden ausschließlich die
  freigegebenen Referenzvokabulare; Status ist nur am Dokument vorgesehen.
- Titel und Beschreibung erlauben nicht leere `xsd:string`- oder
  `rdf:langString`-Werte.
- Sprache, Version und Dateiname müssen nicht leere `xsd:string`-Werte sein.
- `created`, `issued`, `modified`, `validFrom` und `validUntil` erlauben jeweils
  höchstens einen `xsd:date`- oder `xsd:dateTime`-Wert.
- `validFrom` darf nicht nach `validUntil` liegen. Werden beide Werte geliefert,
  sollten sie für eine eindeutige Vergleichbarkeit denselben Datentyp nutzen.
- `hasDistribution` verweist ausschließlich auf typisierte
  `DocumentDistribution`-Ressourcen.
- `dcat:accessURL` und `dcat:downloadURL` müssen IRIs sein.
- `dcat:mediaType` darf höchstens einmal als IANA-orientierte IRI vorkommen.
- ADMS-Identifier werden durch `identifier/core` validiert und benötigen den
  Typ `adms:Identifier`, genau eine literale `skos:notation` und höchstens
  eine `adms:schemaAgency` als `xsd:string`.

Zusatzproperties bleiben zulässig. Das Profil verwendet kein `sh:closed true`
und benötigt keine RDFS- oder OWL-Inferenz.

## 3. Referenzgraphen

Für die kontrollierten Werte werden gemeinsam mit den Daten geladen:

- `datasets/reference/vocabularies/document-type/document-type.ttl`,
- `datasets/reference/vocabularies/document-status/document-status.ttl`.

Die freigegebenen Werte sind zusätzlich als geschlossene `sh:in`-Listen im
Shape-Graph festgehalten. Erweiterungen der Wertemengen erfordern deshalb eine
bewusste Versionierung des Vokabulars und des Shape-Sets.

Der Integrationstest für Akteursrollen lädt zusätzlich:

- `modules/core/agent/ontology/conx-agent.ttl`,
- `modules/core/participation/ontology/conx-part.ttl`,
- `modules/core/participation/shapes/conx-part-core.shacl.ttl`,
- `datasets/reference/vocabularies/participation-role/participation-role.ttl`.

Damit wird belegt, dass Akteursrollen am Dokument über Participation und nicht
über direkte Document-Properties modelliert werden können.

## 4. Testdaten

Gültige Testgraphen:

- `minimal-document.ttl`: IRI und Blank Node als minimale Dokumente,
- `complete-document.ttl`: Metadaten, ADMS-Identifier, Gültigkeit und PDF,
- `multiple-distributions.ttl`: PDF, XML und technische Platzhalterdistribution,
- `document-references.ttl`: modelliertes, externes und distributionsbasiertes Ziel,
- `document-with-participation.ttl`: Integration mit Agent und Participation.

Ungültige Testgraphen:

- `invalid-document-typing.ttl`: fehlende oder falsche Ressourcentypisierung,
- `invalid-document-references.ttl`: fehlende, falsche oder zu viele Ziele,
- `invalid-distributions.ttl`: falsche URL-, Dateiname- und Medientypwerte,
- `invalid-controlled-values.ttl`: nicht freigegebene Typ- und Statuswerte,
- `invalid-metadata-and-identifiers.ttl`: Literal-, Datums-, Gültigkeits- und
  Identifierverstöße.

Die automatisierte Shape-Prüfung wird aus dem Repository-Stamm ausgeführt:

```text
uv run pytest tests/test_document_shapes.py
```

Die Suite validiert den Shape-Graph zusätzlich gegen SHACL-SHACL, prüft die
Versionsmetadaten und stellt sicher, dass jeder freigegebene Fehlercode durch
mindestens einen negativen Testgraphen abgedeckt ist.

## 5. Bewusst nicht geprüft

- UBL-Konformität oder UBL-Mappings,
- digitale Signaturen, Siegel oder Credential-Status,
- fachliche Evidence- oder Requirement-Erfüllung,
- Akteursrollen ohne geladenes Participation-Shape,
- Rechte, Zugriff, Vertraulichkeit und Workflowstatus,
- Erreichbarkeit einer URL oder Existenz einer Datei,
- Storage-, DMS-, Archivierungs- oder Aufbewahrungsregeln,
- fachliche Pflichtmetadaten einzelner Dokumenttypen.

Diese Anforderungen gehören in Profile oder spezialisierte Module.

## 6. Verständliches Beispiel

> Der Core prüft, dass eine Distribution technisch erreichbar beschrieben ist.
> Er entscheidet nicht, ob ein bestimmter Geschäftsprozess zwingend eine
> signierte PDF-Datei verlangt.
