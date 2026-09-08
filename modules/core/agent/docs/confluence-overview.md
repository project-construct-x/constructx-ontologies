# Construct-X Agent Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Agent-Modul stellt einen gemeinsamen Oberbegriff für Akteure bereit.
Personen und Organisationen können dadurch in allgemeinen Beziehungen auf
dieselbe Weise angesprochen werden, ohne ihre Unterschiede aufzugeben.

## 2. Alltagsnahes Beispiel

> An einem Vertrag können Anna Müller und die Beispiel Bau GmbH beteiligt
> sein. Anna ist eine Person, die GmbH ist eine Organisation. Beide können in
> der gemeinsamen Beziehung als Agent referenziert werden.

Das Agent-Modul speichert dabei weder Annas Namen noch die Registerdaten der
GmbH. Diese Angaben bleiben in den jeweils zuständigen Modulen.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- die gemeinsame Klasse `Agent`,
- die semantische Grundlage für Beziehungen, die Personen und Organisationen
  gleichermaßen betreffen.

**Nicht im Modul enthalten:**

- eigene Properties,
- Namen, Kennungen, Adressen oder Kontaktwerte,
- Personen- und Organisationsuntertypen,
- allgemeine Pflichtangaben für Akteure.

Der kleine Umfang ist beabsichtigt. Neue generische Eigenschaften würden erst
bei einem nachgewiesenen fachlichen Bedarf ergänzt.

## 4. Modellübersicht

```text
                 Agent
                /     \
          Person       Organization

Participation -> participant -> Agent
```

`Agent` dient als gemeinsamer Anschluss. Die konkreten Informationen liegen
weiter an `Person` oder `Organization`.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Agent` | Entität, die handeln, Verantwortung tragen oder beteiligt sein kann |
| `Person` | konkrete natürliche Person aus `core/person` |
| `Organization` | konkrete Organisation aus `core/organization` |

Das Agent-Modul definiert selbst keine Beziehungen. Beispielsweise gehört die
Beziehung `participant` dem Participation-Modul, verweist aber auf `Agent`.

## 6. Validierung in verständlicher Sprache

Für das Agent-Modul gibt es bewusst kein eigenes Core Shape. Eine einzelne
Oberklasse besitzt noch keine sinnvollen Pflichtfelder. Die konkreten Module
prüfen ihre eigenen Datenverträge.

> **Beispiel:** Ob eine Person einen Namen benötigt, prüft das Person-Shape.
> Ob eine Organisation einen Namen benötigt, prüft das Organization-Shape.
> Ein zusätzliches Agent-Shape würde diese Regeln nur doppelt pflegen.

## 7. Abhängigkeiten

`Agent` ist konservativ an die verbreiteten Begriffe `foaf:Agent` und
`cv:Agent` angelehnt. Person und Organization spezialisieren den lokalen
Agentenbegriff; Participation verwendet ihn als Wertebereich für Beteiligte.
Das Modul übernimmt keine fachlichen Eigenschaften dieser konsumierenden
Module.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/agent` |
| Präfix | `conx-agent` |
| Core Shape | nicht erforderlich |

- [Ontologie](../ontology/conx-agent.ttl)
- [HTML-Dokumentation](agent.html)
- [Changelog](../CHANGELOG.md)

## 9. Weiterführende Dokumentation

- [Scope und Kompetenzfragen](scope-and-competency-questions.md)
- [Quellenanalyse](source-analysis.md)
- [Konzeptmodell](concept-model.md)
- [Modulgrenzen](module-boundaries.md)
- [Begriffskatalog](term-catalog.md)
- [SHACL-Anforderungen](shacl-requirements.md)
- [Erläuterung zu Core Shapes](core-shapes.md)
- [Konzeptdiagramm](diagrams/concept-model.md)

