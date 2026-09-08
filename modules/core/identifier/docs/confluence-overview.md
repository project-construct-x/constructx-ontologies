# Construct-X Identifier Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Identifier-Modul stellt einen gemeinsamen Datenvertrag für fachliche
Kennungen bereit. Person, Organization und Document können dadurch dasselbe
ADMS/SKOS-Muster verwenden, ohne die Regeln für Kennungswerte mehrfach zu
definieren.

## 2. Alltagsnahes Beispiel

> Die Registernummer „HRB 1234“ gehört zu einer Organisation. Neben dem Wert
> kann gespeichert werden, welche Stelle oder welches Schema die Kennung
> herausgibt. Zusammen bilden diese Angaben eine eigene Identifier-Ressource.

Die Webadresse der Organisation und ihre Registernummer sind damit nicht
dasselbe: Die IRI identifiziert die RDF-Ressource, der Identifier bildet eine
fachliche Kennung ab.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- der wiederverwendbare Vertrag für `adms:Identifier`,
- genau eine Kennungsnotation über `skos:notation`,
- eine optionale textuelle Schema-Agentur,
- ein versionierter Core-Shape-Graph für konsumierende Module.

**Nicht im Modul enthalten:**

- eine parallele Construct-X-Identifier-Klasse,
- die Pflicht, dass eine bestimmte Fachressource eine Kennung besitzt,
- geschlossene Listen konkreter Kennungssysteme,
- Credentials, kryptografische Prüfung oder Vertrauensstatus.

## 4. Modellübersicht

```text
Fachressource -> adms:identifier -> adms:Identifier
                                      |
                                      +-> skos:notation „HRB 1234"
                                      +-> adms:schemaAgency „Registerstelle"
```

Das Identifier-Modul prüft die rechte Seite. Das jeweilige Fachmodul
entscheidet, ob und wie viele Kennungen eine Ressource benötigt.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `adms:Identifier` | strukturierte fachliche Kennung |
| `adms:identifier` | verbindet eine Fachressource mit ihrer Kennung |
| `skos:notation` | eigentlicher Kennungswert |
| `adms:schemaAgency` | optionale Bezeichnung der verantwortlichen Stelle |
| `ADMSIdentifierShape` | gemeinsam wiederverwendete Validierungsregel |

Die genannten RDF-Begriffe stammen aus ADMS und SKOS. Das Construct-X-Modul
besitzt den gemeinsamen Shape-Vertrag und seine Versionierung.

## 6. Validierung in verständlicher Sprache

Eine Kennung muss ausdrücklich ein `adms:Identifier` sein und genau einen
literalen Kennungswert besitzen. Die Schema-Agentur ist optional, darf aber
höchstens einmal und nur als Text angegeben werden.

> **Beispiel:** Ein Identifier mit den beiden Notationen „HRB 1234“ und
> „1234“ ist im Core ungültig, weil nicht eindeutig ist, welcher Wert die
> Kennung darstellt. Zwei unterschiedliche Kennungen werden stattdessen als
> zwei Identifier-Ressourcen modelliert.

## 7. Abhängigkeiten

Das Modul verwendet die Standards ADMS und SKOS. Person, Organization und
Document importieren den versionierten Shape-Graph und wenden ihn innerhalb
ihrer eigenen Regeln an. Die fachliche Kardinalität bleibt dabei beim
konsumierenden Modul.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/identifier` |
| Präfix | `conx-id` |
| Shape-Präfix | `conx-id-sh` |

- [Ontologie-Metadaten](../ontology/conx-id.ttl)
- [Core Shapes](../shapes/conx-id-core.shacl.ttl)
- [HTML-Dokumentation](identifier.html)
- [Minimales Kennungsbeispiel](../tests/valid/minimal-identifier.ttl)
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

