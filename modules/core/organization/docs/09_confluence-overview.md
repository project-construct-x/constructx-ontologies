<a id="construct-x-organization-core-module"></a>

# Construct-X Core-Modul Organization

**Status:** Freigegebene Confluence-Kurzfassung<br>
**Version:** 0.1.0<br>
**Stand:** 3. September 2026<br>
**Geltungsbereich:** `core/organization`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte
Confluence-Modulseite. Es fasst die ausführliche Repository-Dokumentation
zusammen und führt keine neuen fachlichen oder technischen Regeln ein.

<a id="1-purpose"></a>

## 1. Zweck

Das Modul Organization beschreibt Organisationen, rechtliche Einheiten, interne Organisationseinheiten, Mitgliedschaften und rechtliche Vertretungen. Der Schwerpunkt liegt auf Organisationsstammdaten und -strukturen.

<a id="2-everyday-example"></a>

## 2. Alltagsbeispiel

> Die Beispiel Bau GmbH ist eine rechtliche Einheit mit einer internen Logistikeinheit. Anna Müller ist Mitglied und darf das Unternehmen rechtlich vertreten. Organisation, Einheit, Mitgliedschaft und Vertretung sind getrennte, miteinander verknüpfte Ressourcen.

Annas persönliche Daten werden nicht in die Mitgliedschaft oder Vertretung kopiert.

<a id="3-scope-and-boundaries"></a>

## 3. Umfang und Abgrenzung

Das Modul umfasst Organisationen, rechtliche Einheiten, Organisationseinheiten, Namen, Rechtsform, Registrierungsdaten, Hierarchien, Mitgliedschaften und rechtliche Vertretungen. Es definiert keine intrinsischen Personendaten, Adress- und Kontaktstrukturen, allgemeinen Projektrollen, Bankkonten, digitalen Nachweise, Versicherungen oder Projektstammdaten.

<a id="4-model-overview"></a>

## 4. Modellübersicht

```text
Agent
  +-> Organization
        +-> LegalEntity
        +-> OrganizationalUnit

Membership:          Agent -> Organization
LegalRepresentation: Person -> LegalEntity
```

Adressen, Kontakte und Kennungen werden aus den jeweils zuständigen Core-Modulen wiederverwendet.

<a id="5-key-classes-and-relationships"></a>

## 5. Zentrale Klassen und Beziehungen

| Begriff | Bedeutung in Alltagssprache |
| --- | --- |
| `Organization` | Allgemeine Organisation |
| `LegalEntity` | Rechtlich registrierte Organisation |
| `OrganizationalUnit` | Interne Einheit einer Organisation |
| `Membership` | Mitgliedschaft eines Agenten in einer Organisation |
| `LegalRepresentation` | Rechtliche Vertretung durch eine Person |
| `subOrganizationOf` | Allgemeine Organisationshierarchie |
| `unitOf` | Ordnet eine Einheit ihrer Organisation zu |

<a id="6-validation-in-plain-language"></a>

## 6. Validierung in Alltagssprache

Jede Organisation benötigt einen Namen. Eine rechtliche Einheit benötigt zusätzlich einen rechtlichen Namen, genau ein Registrierungsdatum, mindestens eine strukturierte Kennung und eine Standortzuordnung mit rechtlicher Rolle und genau einer Adresse. Einheiten benötigen ihre Organisation; Mitgliedschaften und Vertretungen benötigen jeweils beide beteiligten Ressourcen.

> Eine rechtliche Einheit ohne Registrierungsdatum verletzt die Core-Anforderungen. Eine allgemeine Organisation, die keine rechtliche Einheit ist, benötigt kein solches Datum.

<a id="7-dependencies"></a>

## 7. Abhängigkeiten

Organization spezialisiert `core/agent` und verwendet Personen aus `core/person`. Kennungen werden über `core/identifier` geprüft; Adressen und Kontakte stammen aus `core/address` und `core/contact`. W3C ORG, ADMS, SKOS und Schema.org dienen als externe Referenz- und Alignment-Quellen.

<a id="8-version-status-and-artifacts"></a>

## 8. Version, Status und Artefakte

| Eigenschaft | Wert |
| --- | --- |
| Repository-Status | Entwurf; fachlich geprüft und umgesetzt |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/organization` |
| Präfix | `conx-org` |

- [Ontologie](../ontology/conx-org.ttl)
- [Core Shapes](../shapes/conx-org-core.shacl.ttl)
- [HTML-Dokumentation](organization.html)
- [Vollständiges Beispiel einer rechtlichen Einheit](../tests/valid/complete-legal-entity.ttl)
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
