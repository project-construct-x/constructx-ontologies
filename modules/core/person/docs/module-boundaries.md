# Modulgrenzen der Personenontologie

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/person`

## 1. Ziel

Dieses Dokument ordnet Klassen und Beziehungen den zuständigen Construct-X-Modulen zu. Es verhindert, dass die Personenontologie zu einem Sammelmodell für Organisation, Kontakt, Adresse, Projekt und digitale Identität wird.

Die beschriebenen Core-Module sind in Version `0.1.0` umgesetzt. Aus einer modulübergreifenden Referenz folgt weiterhin kein automatischer OWL-Import.

## 2. Leitprinzipien

1. Ein Modul besitzt nur die Begriffe seines fachlichen Kerns.
2. Beziehungen werden möglichst von dem Modul definiert, das die Beziehung fachlich verantwortet.
3. Wiederverwendbare Querschnittskonzepte werden nicht in `person` versteckt.
4. Daten können modulübergreifend verbunden werden, ohne dass jedes verwendende Modul jedes andere importieren muss.
5. Abhängigkeiten sollen gerichtet und zyklusfrei bleiben.
6. Externe Ontologien werden nur importiert, wenn ihre Axiome für die lokale Semantik notwendig sind. Eine reine Ausrichtung über `rdfs:subClassOf`, `rdfs:subPropertyOf` oder Äquivalenzen ist gesondert zu bewerten.

## 3. Implementierte Core-Modulstruktur

```text
core/agent          minimale gemeinsame Oberklasse
   ├── core/person  natürliche Personen und intrinsische Personendaten
   └── core/organization  Organisationen, Mitgliedschaften und Vertretungen

core/identifier     gemeinsamer ADMS/SKOS-Kennungsvertrag
core/contact        domänenoffene Kontaktpunkte und Kontaktmethoden
core/address        Adress- und AddressAssignment-Modell
core/participation  qualifizierte Agentenrollen in fachlichen Kontexten
core/document       Dokumente, Referenzen und Distributionen
```

Ein mögliches Identitäts- oder Credential-Profil bleibt außerhalb des
Personenkerns. Geografische Positionen werden über den offenen Erweiterungspunkt
des Adressmoduls angebunden; die Personendokumentation plant kein eigenes
`core/location`.

## 4. Entscheidung zur Klasse `Agent`

Eine gemeinsame Oberklasse `Agent` ist sinnvoll, weil mehrere querschnittliche Beziehungen sowohl natürliche Personen als auch Organisationen betreffen:

- ausstellende oder verantwortliche Stellen,
- Mitgliedschaften und Rollen,
- potenziell Bevollmächtigung und Beteiligung.

Sie wird dennoch nicht in der Personenontologie definiert. Ein `conx-person:Agent` würde Organisationen dauerhaft von einem Personenmodul abhängig machen und die spätere Modulgrenze verzerren.

Das Zielbild ist daher eine minimale Klasse in `core/agent`:

```text
conx-agent:Agent
  ├── conx-person:Person
  └── conx-org:Organization
```

Für die externe Interoperabilität ist eine Ausrichtung auf `foaf:Agent` und für `Person` auf `foaf:Person` beziehungsweise `schema:Person` zu prüfen. Das lokale Modul bleibt Eigentümer seiner eigenen Begriffe und Qualitätsanforderungen.

Der konkrete Vorschlag sieht im ersten Agent-Release keine eigenen Agent-Properties und kein inhaltlich leeres Pflicht-Shape vor. Alle fachlichen Personenbegriffe sind im [Begriffskatalog](term-catalog.md) beschrieben.

## 5. Eigentümerschaft der Konzepte

| Modul | Besitzt | Besitzt ausdrücklich nicht |
| --- | --- | --- |
| `core/agent` | Minimale Oberklasse `Agent`; höchstens wirklich generische Agent-Beziehungen | Personenattribute, Organisationsstruktur, Kontaktwerte |
| `core/person` | `Person`, Namen, Geburtsdaten, `sex`, `gender`, Staatsangehörigkeit und Nachweisverknüpfungen | Mitgliedschaften, Rollen, Adressen, Kontaktpunktdetails, Credential- und Schlüsseldetails |
| `core/identifier` | gemeinsamer ADMS/SKOS-Vertrag und `ADMSIdentifierShape` | fachliche Pflichtkennungen und konkrete Kennungssysteme |
| `core/contact` | `ContactPoint`, `ContactMethod`, Kontaktkanal, Nutzungskontext, Kontaktzweck, E-Mail, Telefon und weitere Kanäle | Personennamen, Organisationsstruktur, postalische Adressbestandteile |
| `core/address` | `Address`, `AddressAssignment`, Adressrollen und postalische Struktur | Person und Organisation selbst |
| `core/organization` | `Organization`, `LegalEntity`, `OrganizationalUnit`, `Membership` und rechtliche Vertretung | Intrinsische Personendaten und allgemeine Kontextrollen |
| `core/participation` | allgemeine qualifizierte Rolle eines Agenten in einem fachlichen Kontext | Personenkern und Organisationsmitgliedschaft |
| zukünftiges Identitätsmodul | Identitätsdokumente, Credentials, Verifikationsmethoden, Status und Widerruf | Biografisches Personenprofil |

## 6. Implementierte Abhängigkeiten

### 6.1 Harte semantische Abhängigkeiten

Eine harte Abhängigkeit entsteht nur, wenn ein Modul Klassen oder Properties eines anderen Moduls in seinen eigenen Axiomen benötigt.

| Modul | Abhängigkeit | Grund |
| --- | --- | --- |
| `core/person` | `core/agent` | `Person` ist Unterklasse von `Agent` |
| `core/organization` | `core/agent` | `Organization` ist Agent; Mitglieder können Agenten sein |
| `person/core` Shape | `identifier/core` Shape | Personenkennungen verwenden den gemeinsamen ADMS/SKOS-Vertrag |

### 6.2 Komposition ohne zwingenden Import

Instanzdaten dürfen Begriffe verschiedener Module gemeinsam verwenden. Daraus folgt nicht automatisch ein Import vom Personenmodul zum jeweiligen Fachmodul.

Beispiel Adresse:

```turtle
ex:person-123 a conx-person:Person ;
    conx-addr:hasAddressAssignment ex:address-assignment-1 .
```

Da `conx-addr:hasAddressAssignment` dem Adressmodul gehört, kann eine Anwendung Person- und Adressmodul gemeinsam laden. Das Personenmodul muss die Property nicht erneut definieren.

Beispiel Kontakt:

```turtle
ex:person-123
    conx-contact:hasContactPoint ex:private-contact-point .

ex:private-contact-point
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:private-email .

ex:private-email
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "person@example.org" .
```

Das zweistufige Muster erlaubt Nutzungskontext, Zweck und später gegebenenfalls Gültigkeit, ohne diese Angaben an die Person oder an den einzelnen Kontaktwert selbst zu hängen.

## 7. Abgrenzung zu Organisationen

Das Personenmodul definiert keine Mitgliedschafts- oder Beschäftigungssemantik. Das vorhandene Organisationsmodul verwendet dafür ein am W3C-ORG-Muster orientiertes Beziehungsmodell:

```text
Person/Agent ── Membership ── Organization
                    │
                    ├── Role
                    └── Zeitraum
```

Direkte Beziehungen wie `isMemberOf` und `hasMember` können als einfache Sicht auf diese Struktur dienen. Definition, inverse Beziehung, Domain, Range und mögliche Ableitungsregeln müssen jedoch gemeinsam im Organisationsmodul liegen. Dadurch entsteht keine zyklische fachliche Eigentümerschaft zwischen `person` und `organization`.

Die Firmenadresse gehört zur Organisation oder zu einem Standort. Eine Person erhält sie nicht automatisch als eigene Adresse. Berufliche Kontaktpunkte können über das Kontaktmodul der Person, einer Stelle oder einer Organisation zugeordnet werden.

## 8. Abgrenzung zu Projekten

Eine Projektbeteiligung trägt typischerweise Rolle, Zeitraum, Auftrag oder Verantwortungsbereich. Sie gehört deshalb in das Projektmodul und sollte nicht auf eine einzelne direkte Person-Property reduziert werden.

Das Projektmodul darf Personen oder allgemeiner Agenten als Beteiligte referenzieren. Das Personenmodul benötigt dafür keine inverse Property. Falls eine inverse Navigationsbeziehung benötigt wird, wird sie zusammen mit der Beteiligungssemantik im Projektmodul festgelegt.

## 9. Abgrenzung zu Kontakt und Adresse

Kontakt und Adresse bleiben getrennt:

- Ein Kontaktpunkt beschreibt einen Kommunikationskanal, etwa E-Mail oder Telefon.
- Eine Adresse beschreibt einen postalischen beziehungsweise räumlichen Bezug.
- Ein Kontaktpunkt beschreibt, in welchem Nutzungskontext und für welche Zwecke ein Kontaktträger erreichbar ist. Der Kontaktträger verweist ausgehend über `hasContactPoint` auf diesen Kontaktpunkt.
- Eine Adresszuordnung beschreibt, für welche Ressource und in welcher Rolle eine Adresse gilt.

Das Kontaktmodul benötigt keine feste OWL-Domain auf `Agent`. `hasContactPoint` bleibt im offenen Kern ohne harte Domain, weil neben Personen und Organisationen auch Projekte, Stellen oder andere Ressourcen Kontaktträger sein können. Konkrete SHACL-Profile dürfen die Property gezielt für ihre jeweiligen Zielklassen zulassen.

## 10. Abgrenzung zu Identifikatoren und Identitätsnachweisen

Drei Ebenen sind auseinanderzuhalten:

| Ebene | Bedeutung | Zuständigkeit |
| --- | --- | --- |
| Ressourcen-IRI | Identität des RDF-Knotens im jeweiligen Datenraum | Datenhalter und Namespace-Konzept |
| Fachlicher Identifikator | Kennzeichen nach einem bekannten Schema | `core/identifier` und Identifier-Scheme-Vokabular |
| Identitätsnachweis | Behauptung oder Dokument, das Attribute an eine Person bindet | Externes beziehungsweise späteres Identitätsmodul |

Ein öffentlicher Schlüssel ist eine Verifikationsmethode und kein hinreichender natürlicher Personenidentifikator. Schlüsselmaterial, Controller, Verifikationsbeziehungen und Widerruf sollen sich an W3C Controlled Identifiers orientieren. Nachweisbare Aussagen über die Person können über ein Verifiable Credential angebunden werden.

Das Personenmodul darf eine generische Verknüpfung zum Nachweis definieren, soll aber dessen interne Struktur weder kopieren noch einschränken, bevor das Zielmodell feststeht.

## 11. Länder und geografische Begriffe

Das Construct-X-Ländervokabular verwendet stabile Länder-IRIs und typisiert sie
als `conx-addr:Country`. Das Personenmodul verwendet diese Ressourcen für
Staatsangehörigkeiten. Geografische Positionen bleiben über
`conx-addr:hasGeographicPosition` offen angebunden; ein eigenes Location-Modell
ist keine Voraussetzung des Personenkerns.

## 12. Import- und Alignment-Strategie

Für die Implementierung ist jede externe Quelle einer der folgenden Kategorien zuzuordnen:

| Kategorie | Bedeutung |
| --- | --- |
| Import | Die fremden Axiome sind für die lokale Semantik notwendig und werden versioniert aufgelöst |
| Referenz | Lokale Axiome verwenden externe Ressourcen, ohne die komplette Ontologie zu importieren |
| Alignment | Lokale Begriffe werden über Mapping-Axiome auf externe Begriffe ausgerichtet |
| Analysequelle | Die Quelle beeinflusst das Design, erscheint aber nicht zwingend im RDF-Modell |

Umgesetzte Einordnung:

| Quelle | Einordnung |
| --- | --- |
| ADMS und SKOS für Identifikatoren | Wiederverwendung über `core/identifier` |
| Construct-X ISO-3166-1-Ländervokabular | Referenz auf A-Box-Ressourcen |
| FOAF, Schema.org und SEMIC Core Person | konservative Alignments beziehungsweise dokumentierte Referenzen |
| vCard | Analyse- und Alignment-Quelle für Kontakt |
| W3C ORG | Alignment- und Wiederverwendungsquelle des Organisationsmoduls |
| W3C Controlled Identifiers und VC Data Model | Grundlage eines späteren Identitätsmoduls |

Die konkreten Referenzen sind in den jeweiligen `module.yaml`-Dateien als `referenced-not-imported` dokumentiert. Da keine T-Box `owl:imports` verwendet, entsteht kein neuer Eintrag in `network/imports.lock.yaml`.

## 13. Umsetzungsstand

`core/agent`, `core/person`, `core/contact`, `core/organization`,
`core/address`, `core/participation` und `core/identifier` sind umgesetzt und
fachlich abgegrenzt. Als nicht blockierende Folgeaufgabe bleibt die
Detaillierung von Identitätsnachweisen nach Auswahl eines Sicherheits- und
Vertrauensmodells.

## 14. Verständliches Beispiel

> Annas Geburtsdatum gehört zur Person. Ihre Büroanschrift gehört zu einer
> AddressAssignment und ihre Rolle im Büro zu Membership. Das Person-Modul
> speichert diese Informationen nicht noch einmal.
