<a id="construct-x-agent-core-module"></a>

# Construct-X Core-Modul Agent

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/agent`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Agent stellt eine gemeinsame Oberklasse für Akteure bereit. Personen und Organisationen können dadurch über denselben Typ an allgemeinen Beziehungen beteiligt sein, ohne ihre unterschiedliche Bedeutung zu verlieren.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Anna Müller und die Beispiel Bau GmbH können beide an einem Vertrag beteiligt sein. Anna ist eine Person, das Unternehmen eine Organisation. In der gemeinsamen Beziehung können beide als Agenten referenziert werden.

Namen und Registerdaten verbleiben in den dafür zuständigen Modulen Person und Organization.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst ausschließlich die gemeinsame Klasse `Agent` und die semantische Grundlage für Beziehungen, die Personen und Organisationen zulassen. Es definiert bewusst keine Eigenschaften, Stammdaten oder allgemeinen Pflichtfelder.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
                 Agent
                /     \
          Person       Organization

Participation -> participant -> Agent
```

`Agent` ist der gemeinsame Anknüpfungspunkt. Konkrete Angaben verbleiben an `Person` oder `Organization`.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Agent` | Entität, die handeln, Verantwortung tragen oder beteiligt sein kann |
| `Person` | Natürliche Person aus `core/person` |
| `Organization` | Organisation aus `core/organization` |

Das Modul Agent definiert selbst keine Beziehungen. Beispielsweise gehört `participant` zu Participation, verweist aber auf einen `Agent`.

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Das Modul Agent besitzt bewusst kein eigenes Core Shape. Für die reine Oberklasse gibt es keine sinnvollen Pflichtfelder; die konkreten Module prüfen ihre eigenen Datenanforderungen.

> Person prüft den erforderlichen Personennamen, während Organization den erforderlichen Organisationsnamen prüft. Ein Agent Shape würde diese Regeln verdoppeln.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

`Agent` wird zurückhaltend mit `foaf:Agent` und `cv:Agent` verknüpft. Person und Organization spezialisieren die lokale Klasse. Participation verwendet sie als Wertebereich für Beteiligte.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/agent` |
| Präfix | `conx-agent` |
| Core Shape | Nicht erforderlich |

- [Ontologie](../ontology/conx-agent.ttl)
- [HTML-Dokumentation](agent.html)
- [Änderungsprotokoll](../CHANGELOG.md)

<a id="9-further-documentation"></a>

## 9. Weiterführende Dokumentation

- [Umfang und Kompetenzfragen](02_scope-and-competency-questions.md)
- [Quellenanalyse](01_source-analysis.md)
- [Konzeptmodell](03_concept-model.md)
- [Modulabgrenzung](04_module-boundaries.md)
- [Begriffskatalog](05_term-catalog.md)
- [SHACL-Anforderungen](06_shacl-requirements.md)
- [Erläuterung zu den Core Shapes](07_core-shapes.md)
- [Konzeptdiagramm](08_concept-diagram.md)
- [Agent-Spezifikation](10_agent-specification.md)
