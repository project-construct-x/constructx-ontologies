<a id="construct-x-document-core-module"></a>

# Construct-X Core-Modul Document

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/document`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Document beschreibt dokumentartige Informationsobjekte, ihre Verwendung in einem fachlichen Kontext und ihre technische Bereitstellung. Es trennt das eigentliche Dokument von einem kontextbezogenen Verweis sowie von Dateien oder Downloads.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Ein Vertrag verweist auf einen Prüfbericht. Der Bericht ist das Dokument, seine PDF- und XML-Dateien sind zwei Bereitstellungen, und der Verweis im Vertrag ist eine Dokumentreferenz.

Ein neues Dateiformat erzeugt daher nicht automatisch ein neues fachliches Dokument.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst Dokumente, kontextbezogene Referenzen, technische Bereitstellungen, allgemeine Metadaten, kontrollierte Dokumenttypen und -status sowie strukturierte Kennungen. Es definiert keine akteursspezifischen Eigenschaften, Signaturen, digitalen Nachweise, Zugriffsrechte, Arbeitsabläufe, Herkunftsmodelle oder Speichersysteme.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Fachlicher Kontext -> DocumentReference -> Document
                            |                 |
                            +-----------------+-> DocumentDistribution
                                                    |
                                                    +-> PDF, XML oder URL
```

`Document` identifiziert den Inhalt, `DocumentReference` beschreibt den kontextbezogenen Verweis, und `DocumentDistribution` beschreibt die technische Bereitstellung.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Document` | Dokumentartiges Informationsobjekt |
| `DocumentReference` | Kontextbezogener Verweis auf ein Dokument |
| `DocumentDistribution` | Konkrete Datei oder technische Bereitstellung |
| `DocumentType` | Kontrollierter Typ, etwa Vertrag oder Rechnung |
| `DocumentStatus` | Kontrollierter Status, etwa Entwurf oder ausgestellt |
| `referencesDocument` | Verknüpft die Referenz mit dem Dokument |
| `hasDistribution` | Verknüpft ein Dokument oder eine Referenz mit einer Bereitstellung |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Dokumente, Referenzen und Bereitstellungen müssen explizit typisiert sein. Eine Dokumentreferenz benötigt mindestens ein Ziel: ein modelliertes Dokument, einen externen Verweis oder eine Bereitstellung. Datumsangaben müssen gültig und widerspruchsfrei sein; Typ und Status müssen aus den freigegebenen Vokabularen stammen.

> Eine Dokumentreferenz ohne Ziel ist unvollständig. Eine PDF-Bereitstellung mit Dateiname und Download-IRI kann gültig sein, obwohl der Core nicht prüft, ob die Datei verfügbar oder signiert ist.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

Das Core Shape importiert die versionierten Prüfregeln aus `core/identifier`. Dokumenttypen und -status stammen aus separaten Vokabularen. DCAT-Eigenschaften beschreiben technische Bereitstellungen; Dublin Core, Schema.org, FOAF und SKOS dienen als Referenz- oder Alignment-Quellen. Akteursrollen können über `core/participation` modelliert werden.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/document` |
| Präfix | `conx-doc` |

- [Ontologie](../ontology/conx-doc.ttl)
- [Core Shapes](../shapes/conx-doc-core.shacl.ttl)
- [HTML-Dokumentation](document.html)
- [Vollständiges Dokumentbeispiel](../tests/valid/complete-document.ttl)
- [Änderungsprotokoll](../CHANGELOG.md)

<a id="9-further-documentation"></a>

## 9. Weiterführende Dokumentation

- [Umfang und Kompetenzfragen](02_scope-and-competency-questions.md)
- [Quellenanalyse](01_source-analysis.md)
- [Konzeptmodell](03_concept-model.md)
- [Modulabgrenzung](04_module-boundaries.md)
- [Begriffskatalog](05_term-catalog.md)
- [SHACL-Anforderungen](06_shacl-requirements.md)
- [Core Shapes](07_core-shapes.md)
- [Konzeptdiagramm](08_concept-diagram.md)
