# Construct-X Document Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/document`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Document-Modul beschreibt dokumentartige Informationsobjekte, ihre
Verwendung in einem fachlichen Kontext und ihre technische Bereitstellung. Es
trennt damit das Dokument selbst von einer Referenz darauf und von Dateien oder
Downloads.

## 2. Alltagsnahes Beispiel

> Ein Vertrag verweist auf einen Prüfbericht. Der Prüfbericht ist das
> Dokument. Seine PDF- und XML-Dateien sind zwei Distributionen. Die Stelle im
> Vertrag, die auf den Bericht zeigt, wird als Dokumentreferenz beschrieben.

Eine neue Dateiform erzeugt so nicht automatisch ein neues fachliches
Dokument.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- Dokumente, Dokumentreferenzen und technische Distributionen,
- allgemeine Metadaten wie Titel, Sprache, Version und Gültigkeit,
- kontrollierte Dokumenttypen und Dokumentstatus,
- strukturierte Kennungen über den gemeinsamen Identifier-Vertrag.

**Nicht im Modul enthalten:**

- Autor-, Aussteller- oder Empfängerproperties,
- Signaturen, Credentials und Nachweisprüfung,
- Rechte, Zugriff, Workflows und Provenienz,
- Speicher-, DMS-, Upload- oder Archivierungsmodelle.

## 4. Modellübersicht

```text
fachlicher Kontext -> DocumentReference -> Document
                            |                 |
                            +-----------------+-> DocumentDistribution
                                                    |
                                                    +-> PDF, XML oder URL
```

`Document` beantwortet „Welcher Inhalt?“, `DocumentReference` beantwortet
„Warum wird darauf verwiesen?“ und `DocumentDistribution` beantwortet „In
welcher technischen Form ist er verfügbar?“.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Document` | dokumentartiges Informationsobjekt |
| `DocumentReference` | kontextbezogene Bezugnahme auf ein Dokument |
| `DocumentDistribution` | konkrete Datei oder technische Bereitstellung |
| `DocumentType` | kontrollierter Typ, etwa Vertrag oder Rechnung |
| `DocumentStatus` | kontrollierter Zustand, etwa Entwurf oder ausgegeben |
| `hasDocumentReference` | verbindet einen Kontext mit einer Referenz |
| `referencesDocument` | verbindet die Referenz mit dem Dokument |
| `hasDistribution` | verbindet Dokument oder Referenz mit einer Bereitstellung |
| `documentType` / `documentStatus` | ordnen Typ und Zustand zu |

## 6. Validierung in verständlicher Sprache

Dokumente, Referenzen und Distributionen müssen eindeutig als solche
gekennzeichnet sein. Eine Dokumentreferenz benötigt mindestens ein Ziel:
ein modelliertes Dokument, eine externe Referenz oder eine Distribution.
Datumswerte müssen gültig und zeitlich widerspruchsfrei sein; Typ und Status
stammen aus den freigegebenen Wertelisten.

> **Beispiel:** Eine Dokumentreferenz ohne Ziel ist unvollständig. Eine PDF-
> Distribution mit Dateiname und Download-IRI kann gültig sein; ob die Datei
> tatsächlich abrufbar und signiert ist, prüft der Core nicht.

## 7. Abhängigkeiten

Das Core Shape importiert den versionierten Vertrag aus `core/identifier`.
Dokumenttypen und Dokumentstatus stammen aus separaten Referenzvokabularen.
DCAT-Properties werden für technische Distributionen wiederverwendet; Dublin
Core, Schema.org, FOAF und SKOS dienen als Referenz- oder Alignmentquellen.
Akteursrollen werden bei Bedarf über `core/participation` modelliert.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/document` |
| Präfix | `conx-doc` |

- [Ontologie](../ontology/conx-doc.ttl)
- [Core Shapes](../shapes/conx-doc-core.shacl.ttl)
- [HTML-Dokumentation](document.html)
- [Vollständiges Dokumentbeispiel](../tests/valid/complete-document.ttl)
- [Changelog](../CHANGELOG.md)

## 9. Weiterführende Dokumentation

- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Quellenanalyse](source-analysis.md)
- [Konzeptmodell](concept-model.md)
- [Modulgrenzen](module-boundaries.md)
- [Begriffskatalog](term-catalog.md)
- [SHACL-Anforderungen](shacl-requirements.md)
- [Core-Shape-Referenz](core-shapes.md)
- [Konzeptdiagramm](diagrams/concept-model.md)

