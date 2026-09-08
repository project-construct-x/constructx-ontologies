# Construct-X Organization Core-Modul

**Status:** Für Confluence freigegebene Kurzfassung  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/organization`

Dieses Dokument ist die Veröffentlichungsquelle für die kompakte Modulseite in
Confluence. Es verdichtet die vorhandene Repository-Dokumentation und führt
keine neuen fachlichen oder technischen Regeln ein.

## 1. Zweck

Das Organization-Modul beschreibt Organisationen, rechtliche Einheiten,
interne Organisationseinheiten, Mitgliedschaften und rechtliche Vertretungen.
Es konzentriert sich auf Organisationsstammdaten und Organisationsstruktur.

## 2. Alltagsnahes Beispiel

> Die Beispiel Bau GmbH ist eine rechtliche Einheit. Sie besitzt die Abteilung
> „Logistik“. Anna Müller ist Mitglied der GmbH und darf sie rechtlich
> vertreten. Organisation, Abteilung, Mitgliedschaft und Vertretung sind
> unterschiedliche, miteinander verbundene Ressourcen.

Annas persönliche Daten werden dabei nicht in der Mitgliedschaft oder
Vertretung wiederholt.

## 3. Umfang und Abgrenzung

**Im Modul enthalten:**

- Organisationen, rechtliche Einheiten und Organisationseinheiten,
- Namen, rechtlicher Name, Registerdatum, Rechtsform und Tätigkeit,
- allgemeine Organisationshierarchien,
- Mitgliedschaften und rechtliche Vertretungen.

**Nicht im Modul enthalten:**

- intrinsische Personendaten,
- Adress- und Kontaktstrukturen,
- allgemeine Rollen in Projekten, Verträgen oder Dokumenten,
- Bankkonten, Credentials, Versicherungen und Projektstammdaten.

## 4. Modellübersicht

```text
Agent
  +-> Organization
        +-> LegalEntity
        +-> OrganizationalUnit

Membership:          Agent -> Organization
LegalRepresentation: Person -> LegalEntity
```

Adressen, Kontakte und Kennungen werden aus ihren zuständigen Core-Modulen
eingebunden und nicht im Organization-Namensraum neu definiert.

## 5. Zentrale Klassen und Beziehungen

| Begriff | Verständliche Bedeutung |
| --- | --- |
| `Organization` | allgemeine Organisation |
| `LegalEntity` | rechtlich registrierte Organisation |
| `OrganizationalUnit` | interne Einheit einer Organisation |
| `Membership` | Mitgliedschaft eines Agenten in einer Organisation |
| `LegalRepresentation` | rechtliche Vertretung durch eine Person |
| `subOrganizationOf` | allgemeine Organisationshierarchie |
| `unitOf` | ordnet eine Einheit ihrer Organisation zu |
| `member` / `membershipOrganization` | Bestandteile einer Mitgliedschaft |
| `representative` / `representedOrganization` | Bestandteile einer Vertretung |

## 6. Validierung in verständlicher Sprache

Jede Organisation benötigt mindestens einen Namen. Eine rechtliche Einheit
benötigt zusätzlich einen rechtlichen Namen, genau ein Registerdatum,
mindestens eine strukturierte Kennung und eine rechtliche Adresszuordnung.
Organisationseinheiten müssen ihrer Organisation zugeordnet sein;
Mitgliedschaft und Vertretung benötigen jeweils genau die beiden beteiligten
Ressourcen.

> **Beispiel:** Eine GmbH ohne Registerdatum erfüllt den Core-Vertrag nicht.
> Eine normale Organisation, die keine rechtliche Einheit ist, muss dagegen
> kein Registerdatum besitzen.

## 7. Abhängigkeiten

Organization spezialisiert `core/agent` und verwendet Personen aus
`core/person`. Kennungen werden durch das importierte Shape aus
`core/identifier` geprüft. Adressen und Kontaktpunkte stammen aus
`core/address` und `core/contact`. W3C ORG, ADMS, SKOS und Schema.org dienen als
externe Referenz- und Alignmentquellen.

## 8. Version, Status und Artefakte

| Merkmal | Wert |
| --- | --- |
| Repository-Status | Draft; fachlich bestätigt und implementiert |
| Version | `0.1.0` |
| Ontologie-IRI | `https://www.construct-x.org/ontology/organization` |
| Präfix | `conx-org` |

- [Ontologie](../ontology/conx-org.ttl)
- [Core Shapes](../shapes/conx-org-core.shacl.ttl)
- [HTML-Dokumentation](organization.html)
- [Beispiel einer Legal Entity](../tests/valid/complete-legal-entity.ttl)
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

