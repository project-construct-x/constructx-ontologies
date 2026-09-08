# Fachliche SHACL-Anforderungen für den Personen-MVP

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Person Core Shapes

## 1. Zweck

Dieses Dokument legt die ausführbaren Qualitätsanforderungen für Personendaten fest. Es beschreibt Shape-Targets, Constraints, Schweregrade, Fehlermeldungen sowie gültige und ungültige Szenarien. Es ist die fachliche Grundlage der implementierten Core Shapes.

Der ausführbare Shape-Graph liegt unter `shapes/conx-person-core.shacl.ttl`. Kontaktanforderungen werden durch das eigenständige, implementierte `core/contact` abgedeckt und nicht im Person-Shape dupliziert.

## 2. Shape-Set

```text
Shape-Graph:  modules/core/person/shapes/conx-person-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/person/core
Versions-IRI: https://www.construct-x.org/shapes/person/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/person/core#
Prefix:       conx-person-sh
Version:      0.1.0
```

Die IRIs und die Version sind in `module.yaml` und im Shape-Graph festgelegt.

## 3. Validierungsprinzipien

### 3.1 Verhältnis von OWL und SHACL

- OWL beschreibt die Semantik unter der Open-World-Annahme.
- SHACL prüft den konkret gelieferten Datengraphen.
- Pflichtfelder und Maximalwerte werden im Core-Shape als geschlossene Datenanforderungen geprüft.
- Die Shapes bleiben für zusätzliche Properties offen; `sh:closed true` ist nicht vorgesehen.
- SHACL-Maximalwerte werden nicht automatisch als OWL-Kardinalitäten übernommen.

### 3.2 Schweregrade

Alle in diesem Dokument festgelegten Core-Verstöße verwenden `sh:Violation`. Empfehlungen wie die Angabe eines Familiennamens erzeugen im Core weder Fehler noch Warnung.

Anwendungsprofile dürfen später zusätzliche Regeln mit `sh:Warning` oder `sh:Info` ergänzen.

### 3.3 Fehlermeldungen

Jede fachliche Constraint-Komponente erhält mindestens:

- eine deutsche `sh:message`,
- eine englische `sh:message`,
- einen stabilen Anforderungsbezeichner aus diesem Dokument,
- einen präzisen Ergebnispfad, soweit SHACL ihn bestimmen kann.

### 3.4 Referenzdaten

Die Validierung muss gemeinsam mit den freigegebenen Referenzgraphen ausgeführt werden:

- Construct-X `human-sex`-Vokabular,
- Construct-X Gender-Vokabular,
- Construct-X ISO-3166-1-Ländervokabular.

Die kleinen `sex`- und Gender-Wertemengen können zusätzlich als geschlossene `sh:in`-Listen in das Personen-Shape aufgenommen werden. Die 249 Länder werden nicht in das Shape kopiert, sondern über Typ und `skos:inScheme` geprüft.

## 4. Verantwortungsgrenzen der Shape-Sets

| Anforderung | Zuständiges Shape-Set | Regel im Personen-Shape |
| --- | --- | --- |
| Intrinsische Personendaten | `person/core` | Vollständig validieren |
| Beziehung zu ADMS-Identifiern | `person/core` + `identifier/core` | Fachliche Zuordnung lokal, gemeinsame ADMS-Struktur zentral prüfen |
| Weitergehende Identifier-Regeln | spätere Fachprofile | Konkrete Schemata und Issuer-Semantik nicht im Personen-MVP erzwingen |
| Beziehung zu Identitätsnachweisen | `person/core` | Referenzierbarkeit prüfen |
| Inhalt von Dokumenten oder Credentials | späteres Identitäts-Shape | Nicht im Personen-Shape prüfen |
| Kontaktzuordnung | `contact/core` | Person darf Property verwenden; Kontakt-Shape validiert die Zuordnung |
| Adresse | vorhandenes `address/core` | Vorhandene Address Shapes wiederverwenden |
| Mitgliedschaft und Projektbeteiligung | spätere Fach-Shape-Sets | Nicht im Personen-Shape prüfen |

## 5. Shape-Katalog

### 5.1 Implementierte Shapes des Personenmoduls

| Shape-IRI | Typ | Target beziehungsweise Verwendung | Aufgabe |
| --- | --- | --- | --- |
| `conx-person-sh:StringOrLangStringShape` | wiederverwendbares Node Shape | von Property Shapes referenziert | Erlaubt `xsd:string` oder `rdf:langString` |
| `conx-person-sh:NonEmptyStringOrLangStringShape` | wiederverwendbares Node Shape | von Namens- und Ortswerten referenziert | Erlaubt String/LangString mit mindestens einem Nicht-Leerzeichen |
| `conx-person-sh:PersonShape` | Node Shape | `conx-person:Person` und Subjekte von Personen-Properties | Bündelt alle Person-Constraints |
| `conx-person-sh:HumanSexConceptShape` | Node Shape | Objekte von `conx-person:sex` | Prüft IRI und vier erlaubte ISO/IEC-5218-Konzepte |
| `conx-person-sh:GenderConceptShape` | Node Shape | Objekte von `conx-person:gender` | Prüft IRI und vier freigegebene Genderwerte |
| `conx-person-sh:CitizenshipCountryShape` | Node Shape | Objekte von `conx-person:citizenship` | Prüft Länderklasse und Country Concept Scheme |
| `conx-person-sh:IdentityEvidenceReferenceShape` | Node Shape | Objekte von `conx-person:hasIdentityEvidence` | Prüft eine externe IRI ohne Nachweisdetails zu validieren |

### 5.2 Wiederverwendete Shapes anderer Core-Module

| Shape-IRI | Eigentümer | Aufgabe |
| --- | --- | --- |
| `conx-contact-sh:ContactCarrierShape` | `contact/core` | Prüft Werte von `hasContactPoint` ohne harte Agent-Domain |
| `conx-contact-sh:ContactPointShape` | `contact/core` | Prüft Kontaktblock, Nutzung, Zweck und Kontaktmethoden |
| `conx-contact-sh:ContactMethodShape` | `contact/core` | Prüft Kontaktkanal und kanalspezifischen Payload |
| vorhandene Address Shapes | `address/core` | Prüfen Adresszuordnung, Adresse und Adressrollen |
| `conx-id-sh:ADMSIdentifierShape` | `identifier/core` | Prüft Typ, Notation und optionale Schema-Agentur einer Kennung |

## 6. Targets des `PersonShape`

Das implementierte `PersonShape` kombiniert folgende Targets:

1. `sh:targetClass conx-person:Person`,
2. `sh:targetSubjectsOf` für jede Property des Personenkerns.

Die zweite Target-Gruppe erkennt Ressourcen, die beispielsweise `birthDate` oder `gender` verwenden, aber nicht als `conx-person:Person` typisiert wurden. Das Shape verlangt dann den expliziten Personentyp. Eine bloße RDFS-Domain-Inferenz genügt für die Datenqualitätsprüfung nicht.

Folgende Properties lösen das Target aus:

- `fullName`,
- `givenName`,
- `familyName`,
- `additionalName`,
- `birthName`,
- `birthDate`,
- `birthPlaceName`,
- `sex`,
- `gender`,
- `citizenship`,
- `hasIdentityEvidence`.

`adms:identifier` ist eine generische Property und darf nicht jedes ihrer Subjekte automatisch zum Person-Target machen. Sie wird nur innerhalb bereits erkannter Personen geprüft.

## 7. Node-Constraints für Personen

| ID | Constraint | SHACL-Anforderung |
| --- | --- | --- |
| `PER-001` | Referenzierbare Person | Fokusressource muss `sh:nodeKind sh:IRI` erfüllen |
| `PER-002` | Expliziter Personentyp | Fokusressource muss `sh:class conx-person:Person` erfüllen |

Personen werden damit nicht als Blank Nodes ausgeliefert. Die stabile IRI bleibt unabhängig von fachlichen Identifikatoren, Ausweisen oder öffentlichen Schlüsseln.

## 8. Property-Constraints des `PersonShape`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `PER-010` | `fullName` | 1 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `PER-011` | `givenName` | 1 | offen | Nicht leerer `xsd:string` oder `rdf:langString` |
| `PER-012` | `familyName` | 0 | offen | Falls vorhanden: nicht leerer String/LangString |
| `PER-013` | `additionalName` | 0 | offen | Falls vorhanden: nicht leerer String/LangString |
| `PER-014` | `birthName` | 0 | offen | Falls vorhanden: nicht leerer String/LangString |
| `PER-020` | `birthDate` | 0 | 1 | Ausschließlich lexikalisch gültiges `xsd:date` |
| `PER-021` | `birthPlaceName` | 0 | 1 | Nicht leerer String/LangString |
| `PER-030` | `sex` | 0 | 1 | IRI aus der geschlossenen Human-Sex-Wertemenge |
| `PER-031` | `gender` | 0 | 1 | IRI aus der geschlossenen Gender-Startwertemenge |
| `PER-040` | `citizenship` | 0 | offen | IRI, Instanz von `conx-addr:Country`, im Country Concept Scheme |
| `PER-050` | `adms:identifier` | 0 | offen | Blank Node oder IRI, Instanz von `adms:Identifier`, genau eine literale `skos:notation`, optional höchstens eine `adms:schemaAgency` als String |
| `PER-060` | `hasIdentityEvidence` | 0 | offen | Externe IRI; keine Klassenfestlegung im Personenkern |

## 9. Literalregeln

### 9.1 Namen und Geburtsort

Zulässig sind:

- einfache Literale mit Datentyp `xsd:string`,
- sprachmarkierte Literale mit Datentyp `rdf:langString`.

Unzulässig sind:

- leere Werte,
- Werte, die ausschließlich aus Leerzeichen bestehen,
- numerische oder andere fachfremde Datentypen.

Für die Nicht-Leer-Prüfung ist eine Regel entsprechend `sh:pattern "\\S"` vorzusehen. `sh:uniqueLang` wird nicht verwendet, da mehrere Namen in derselben Sprache oder unterschiedlichen Schriftsystemen zulässig sein können.

### 9.2 Geburtsdatum

`birthDate` akzeptiert ausschließlich `xsd:date`. Nicht zugelassen sind:

- `xsd:gYear`,
- `xsd:gYearMonth`,
- untypisierte Datumsstrings,
- mehrere Geburtsdaten.

Eine Prüfung „Geburtsdatum darf nicht in der Zukunft liegen“ ist im Core nicht vorgesehen. Sie wäre zeitabhängig und kann in einem strengeren Anwendungsprofil ergänzt werden.

## 10. Kontrollierte Werte

### 10.1 `sex`

Die zulässige `sh:in`-Liste umfasst genau:

```text
human-sex:notKnown
human-sex:male
human-sex:female
human-sex:notApplicable
```

Zusätzlich gilt `sh:nodeKind sh:IRI` und `sh:maxCount 1`.

Das Fehlen der Property bedeutet, dass im Datensatz keine Aussage vorliegt. `human-sex:notKnown` ist dagegen eine ausdrückliche Aussage, dass der Wert nicht bekannt ist.

`human-sex:notApplicable` darf nicht als Ersatz für Genderdiversität verwendet werden. SHACL kann den fachlichen Grund seiner Verwendung nicht erkennen; dies bleibt eine Governance-Anforderung.

### 10.2 `gender`

Die zulässige `sh:in`-Liste umfasst zunächst genau:

```text
gender:man
gender:woman
gender:nonBinaryOrDiverse
gender:notDisclosed
```

Zusätzlich gilt `sh:nodeKind sh:IRI` und `sh:maxCount 1`.

Semantische Hinweise:

- `man` und `woman` sind Genderidentitäten; die englischen Labels lauten bewusst `Man` und `Woman`, nicht `Male` und `Female`.
- `nonBinaryOrDiverse` ist ein erweiterbarer Sammelbegriff. Präzisere Konzepte können in späteren Vokabularversionen ergänzt werden.
- `notDisclosed` ist keine Identität, sondern die ausdrückliche Nichtoffenlegung.
- Eine fehlende `gender`-Property bedeutet lediglich, dass keine Aussage im Datensatz vorliegt.

Eine Erweiterung der geschlossenen Liste erfordert eine neue Version des Shape-Sets. Dadurch akzeptiert ein älteres Profil nicht stillschweigend unbekannte neue Genderwerte.

### 10.3 Staatsangehörigkeit

Jeder Wert von `citizenship` muss:

1. eine IRI sein,
2. als `conx-addr:Country` typisiert sein,
3. `skos:inScheme <https://www.construct-x.org/vocab/country>` besitzen.

Ein Literal wie `"DE"`, eine ISO-3166-2-Unterteilung oder eine NUTS-2-Region ist nicht zulässig. Mehrere Staatsangehörigkeiten sind erlaubt. Eine Staatsangehörigkeit ist nicht verpflichtend.

## 11. Identifier-Anforderungen

Das Personen-Shape prüft für jeden Wert von `adms:identifier` mindestens:

- Ressourcenart `sh:BlankNodeOrIRI`,
- Klasse `adms:Identifier`,
- genau eine literale `skos:notation`,
- optional höchstens eine `adms:schemaAgency` als `xsd:string`.

Die fachliche Property `adms:identifier` bleibt im Personen-Shape. Ihre Werte
werden mit dem gemeinsamen `conx-id-sh:ADMSIdentifierShape` aus
`identifier/core` validiert:

| ID | Property | Anforderung |
| --- | --- | --- |
| `ID-001` | Ressourcentyp | `adms:Identifier` |
| `ID-002` | `skos:notation` | genau ein Literal |
| `ID-003` | `adms:schemaAgency` | optional, höchstens ein `xsd:string` |

Der Datentyp der Notation darf ein Construct-X-Identifier-Schema bezeichnen,
wird aber nicht gegen eine geschlossene Freigabeliste geprüft. Konkrete
Personen-Identifier-Schemata können deshalb in Fachprofilen ergänzt werden.

`issuedBy` und `issuedThrough` werden nicht verlangt, weil ihre endgültige
Property-Eigentümerschaft im Identifier- beziehungsweise Identitätsmodell nicht
festgelegt ist. `adms:schemaAgency` bleibt eine optionale textuelle Angabe und
wird nicht als vollständiges Issuer-Modell interpretiert.

## 12. Identity-Evidence-Anforderungen

`hasIdentityEvidence` besitzt:

- `sh:minCount 0`,
- kein Maximum,
- `sh:nodeKind sh:IRI`.

Das Personen-Shape verlangt absichtlich keine gemeinsame Klasse für die Zielressource. Zulässige externe Modelle können unter anderem Ausweisdokumentreferenzen, Führerscheinreferenzen, Verifiable Credentials, Registerauszüge oder andere digital prüfbare Nachweise bereitstellen.

Nicht im Personen-Shape geprüft werden:

- Herausgeber und Vertrauensstatus,
- Ausgabe- und Ablaufdatum,
- Credential Subject,
- Evidenzkette,
- Widerruf und Status,
- kryptografische Schlüssel und Proofs.

Diese Regeln gehören zum jeweiligen Dokument-, Credential- oder Identitäts-Shape.

## 13. Kontakt-Shape-Vertrag

Die folgenden Anforderungen werden nicht im Personen-Shape umgesetzt, sondern im eigenständigen `contact/core` Shape-Set beschrieben. Das aktuelle Anforderungsdokument liegt unter `modules/core/contact/docs/shacl-requirements.md`.

### 13.1 `ContactCarrierShape`

- Target: Subjekte von `conx-contact:hasContactPoint`.
- Keine `sh:class conx-agent:Agent`-Anforderung im offenen Core-Shape.
- Jeder Wert muss Blank Node oder IRI und `conx-contact:ContactPoint` sein.
- Das Shape macht keine Aussage darüber, ob das Subjekt Person, Organisation, Projekt, Stelle oder eine andere Ressource ist.

### 13.2 `ContactPointShape`

| ID | Property | Minimum | Maximum | Werteanforderung |
| --- | --- | ---: | ---: | --- |
| `CON-CP-010` | `hasContactMethod` | 1 | offen | Ressource vom Typ `ContactMethod` |
| `CON-CP-020` | `contactUsage` | 0 | 1 | IRI aus dem freigegebenen Contact-Usage-Scheme |
| `CON-CP-021` | `contactPurpose` | 0 | offen | IRI aus dem freigegebenen Contact-Purpose-Scheme |

`contactUsage` beschreibt den privaten, beruflichen oder offiziellen Verwendungskontext. `contactPurpose` beschreibt davon getrennt die fachliche Funktion, zum Beispiel allgemein, Lieferung, Rechnung, Support oder Notfall. `contact-usage:private` ist keine Zugriffs- oder Geheimhaltungsregel.

### 13.3 `ContactMethodShape`

Das minimale Shape verlangt:

- Blank Node oder IRI,
- expliziten Typ `conx-contact:ContactMethod`,
- genau einen freigegebenen `contactChannel`,
- genau einen zum Kanal passenden Payload: `contactValue`, `contactURI` oder `usesAddressAssignment`.

Postalische Kontaktmethoden verweisen ausschließlich mit `usesAddressAssignment` auf `conx-addr:AddressAssignment`. Der direkte Verweis auf `conx-addr:Address` ist im Kontakt-MVP nicht vorgesehen.

## 14. Fehlermeldungskatalog

### 14.1 Personenbezogene Meldungen

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `PER-001` | Eine Person muss durch eine IRI referenziert werden. | A Person must be referenced by an IRI. |
| `PER-002` | Eine Ressource mit Personeneigenschaften muss explizit als conx-person:Person typisiert sein. | A resource using Person properties must be explicitly typed as conx-person:Person. |
| `PER-010` | Eine Person muss mindestens einen nicht leeren vollständigen Namen besitzen. | A Person must have at least one non-empty full name. |
| `PER-011` | Eine Person muss mindestens einen nicht leeren Vornamen besitzen. | A Person must have at least one non-empty given name. |
| `PER-012` | Jeder Familienname muss ein nicht leerer String oder sprachmarkierter String sein. | Every family name must be a non-empty string or language-tagged string. |
| `PER-013` | Jeder zusätzliche Name muss ein nicht leerer String oder sprachmarkierter String sein. | Every additional name must be a non-empty string or language-tagged string. |
| `PER-014` | Jeder Geburtsname muss ein nicht leerer String oder sprachmarkierter String sein. | Every birth name must be a non-empty string or language-tagged string. |
| `PER-020` | Eine Person darf höchstens ein vollständiges Geburtsdatum mit dem Datentyp xsd:date besitzen. | A Person may have at most one complete birth date using datatype xsd:date. |
| `PER-021` | Der Geburtsortname muss ein nicht leerer String oder sprachmarkierter String sein und darf höchstens einmal vorkommen. | The birth place name must be a non-empty string or language-tagged string and may occur at most once. |
| `PER-030` | sex darf höchstens einmal vorkommen und muss auf einen freigegebenen ISO/IEC-5218-Wert verweisen. | sex may occur at most once and must reference an approved ISO/IEC 5218 value. |
| `PER-031` | gender darf höchstens einmal vorkommen und muss auf einen freigegebenen Genderwert verweisen. | gender may occur at most once and must reference an approved gender value. |
| `PER-040` | Jede Staatsangehörigkeit muss auf ein Land des freigegebenen Construct-X-Ländervokabulars verweisen. | Every citizenship value must reference a country from the approved Construct-X country vocabulary. |
| `PER-050` | Jeder Personenidentifikator muss eine ADMS-Identifier-Ressource mit genau einer literalen Notation sein. | Every Person identifier must be an ADMS Identifier resource with exactly one literal notation. |
| `PER-060` | Jeder Identitätsnachweis muss durch eine externe IRI referenziert werden. | Every identity evidence resource must be referenced by an external IRI. |

### 14.2 Identifier-Meldungen

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `ID-001` | Eine Identifikatorressource muss als adms:Identifier typisiert sein. | An identifier resource must be typed as adms:Identifier. |
| `ID-002` | Ein Identifikator muss genau eine skos:notation besitzen. | An identifier must have exactly one skos:notation. |
| `ID-003` | schemaAgency darf höchstens einmal als String angegeben werden. | schemaAgency may be provided at most once as a string. |

### 14.3 Kontaktmeldungen

| ID | Deutsch | Englisch |
| --- | --- | --- |
| `CON-CAR-001` | Jeder Wert von hasContactPoint muss eine ContactPoint-Ressource sein. | Every hasContactPoint value must be a ContactPoint resource. |
| `CON-CP-010` | Ein ContactPoint muss mindestens eine ContactMethod besitzen. | A ContactPoint must have at least one ContactMethod. |
| `CON-CP-020` | contactUsage darf höchstens einmal vorkommen und muss auf einen freigegebenen Usage-Wert verweisen. | contactUsage may occur at most once and must reference an approved usage value. |
| `CON-CP-021` | Jeder contactPurpose-Wert muss auf einen freigegebenen Purpose-Wert verweisen. | Every contactPurpose value must reference an approved purpose value. |
| `CON-CM-010` | Eine ContactMethod muss genau einen freigegebenen Kontaktkanal besitzen. | A ContactMethod must have exactly one approved contact channel. |
| `CON-CM-020` | Eine ContactMethod muss genau einen zum Kanal passenden Payload besitzen. | A ContactMethod must have exactly one payload matching its channel. |
| `CON-CM-032` | Eine postalische Kontaktmethode muss genau eine conx-addr:AddressAssignment referenzieren. | A postal contact method must reference exactly one conx-addr:AddressAssignment. |

## 15. Gültige Szenarien

### V-01: Minimale gültige Person

```turtle
ex:person-1 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" .
```

Erwartung: gültig. Alle optionalen Properties dürfen fehlen.

### V-02: Vollständige Person mit kontrollierten Werten

```turtle
ex:person-2 a conx-person:Person ;
    conx-person:fullName "Maria Anna Beispiel"@de ;
    conx-person:givenName "Maria" ;
    conx-person:additionalName "Anna" ;
    conx-person:familyName "Beispiel" ;
    conx-person:birthDate "1985-04-23"^^xsd:date ;
    conx-person:birthPlaceName "Bochum"@de ;
    conx-person:sex human-sex:female ;
    conx-person:gender gender:woman ;
    conx-person:citizenship country:DEU ;
    conx-person:hasIdentityEvidence ex:credential-789 .
```

Erwartung: gültig, wenn die referenzierten Vokabulare im Validierungsgraph geladen sind.

### V-03: Ausdrückliche Nichtoffenlegung von Gender

```turtle
ex:person-3 a conx-person:Person ;
    conx-person:fullName "Alex Beispiel" ;
    conx-person:givenName "Alex" ;
    conx-person:gender gender:notDisclosed .
```

Erwartung: gültig. Die Person hat ausdrücklich keine Genderangabe offengelegt.

### V-04: Privater Kontaktpunkt

```turtle
ex:person-4 a conx-person:Person ;
    conx-person:fullName "Sam Beispiel" ;
    conx-person:givenName "Sam" ;
    conx-contact:hasContactPoint ex:person-4-private-contact .

ex:person-4-private-contact
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private ;
    conx-contact:contactPurpose contact-purpose:general ;
    conx-contact:hasContactMethod ex:email-1 .

ex:email-1
    a conx-contact:ContactMethod ;
    conx-contact:contactChannel contact-channel:email ;
    conx-contact:contactValue "sam@example.org" .
```

Erwartung: für Person und Kontakt gültig, sobald das Contact-Core-Shape und das Kanalmodell implementiert sind.

### V-05: Mehrere Staatsangehörigkeiten und Identifikatoren

```turtle
ex:person-5 a conx-person:Person ;
    conx-person:fullName "Robin Beispiel" ;
    conx-person:givenName "Robin" ;
    conx-person:citizenship country:DEU,
                                country:FRA ;
    adms:identifier [
        a adms:Identifier ;
        skos:notation "P-4711"^^id-scheme:project-person-id ;
        adms:schemaAgency "Beispielorganisation"
    ] .
```

Erwartung: gültig, sofern das verwendete Identifikatorschema freigegeben ist.

## 16. Ungültige Szenarien

### I-01: `fullName` fehlt

```turtle
ex:invalid-1 a conx-person:Person ;
    conx-person:givenName "Kim" .
```

Erwarteter Verstoß: `PER-010`.

### I-02: `givenName` fehlt

```turtle
ex:invalid-2 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" .
```

Erwarteter Verstoß: `PER-011`.

### I-03: Leerer Name

```turtle
ex:invalid-3 a conx-person:Person ;
    conx-person:fullName "   " ;
    conx-person:givenName "Kim" .
```

Erwarteter Verstoß: `PER-010`.

### I-04: Unvollständiges Geburtsdatum

```turtle
ex:invalid-4 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:birthDate "1985"^^xsd:gYear .
```

Erwarteter Verstoß: `PER-020`.

### I-05: Mehrere Geburtsdaten

```turtle
ex:invalid-5 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:birthDate "1985-04-23"^^xsd:date,
                          "1985-04-24"^^xsd:date .
```

Erwarteter Verstoß: `PER-020`.

### I-06: `sex` als Literal

```turtle
ex:invalid-6 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:sex "female" .
```

Erwarteter Verstoß: `PER-030`.

### I-07: Unbekannter Genderwert

```turtle
ex:invalid-7 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:gender ex:unsupported-gender-value .
```

Erwarteter Verstoß: `PER-031`.

### I-08: Mehrere Genderwerte

```turtle
ex:invalid-8 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:gender gender:nonBinaryOrDiverse,
                       gender:notDisclosed .
```

Erwarteter Verstoß: `PER-031`.

### I-09: Länderkennzeichen als Literal

```turtle
ex:invalid-9 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:citizenship "DE" .
```

Erwarteter Verstoß: `PER-040`.

### I-10: Region statt Staat

```turtle
ex:invalid-10 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:citizenship ex:nuts-region-DEA1 .
```

Erwarteter Verstoß: `PER-040`.

### I-11: Identifikator als Literal

```turtle
ex:invalid-11 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    adms:identifier "P-4711" .
```

Erwarteter Verstoß: `PER-050`.

### I-12: Identitätsnachweis als Literal

```turtle
ex:invalid-12 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-person:hasIdentityEvidence "Personalausweis" .
```

Erwarteter Verstoß: `PER-060`.

### I-13: Kontaktpunkt ohne Kontaktmethode

```turtle
ex:person-13 a conx-person:Person ;
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" ;
    conx-contact:hasContactPoint ex:invalid-contact-point .

ex:invalid-contact-point
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private .
```

Erwarteter Verstoß im Contact Shape: `CON-CP-010`.

### I-14: Zwei Kontakt-Usage-Werte

```turtle
ex:invalid-contact-point-2
    a conx-contact:ContactPoint ;
    conx-contact:contactUsage contact-usage:private,
                              contact-usage:business ;
    conx-contact:hasContactMethod ex:email-2 .
```

Erwarteter Verstoß im Contact Shape: `CON-CP-020`.

### I-15: Personeneigenschaft ohne Personentyp

```turtle
ex:invalid-15
    conx-person:fullName "Kim Beispiel" ;
    conx-person:givenName "Kim" .
```

Erwarteter Verstoß: `PER-002`.

## 17. Bewusst nicht validiert

Das Core-Shape prüft nicht:

- ob `fullName` aus Vor-, Zusatz- und Familiennamen zusammengesetzt werden kann,
- ob eine Person einen Familiennamen besitzt,
- ob das Geburtsdatum in der Vergangenheit liegt,
- ob `sex` und `gender` vermeintlich zueinander passen,
- ob eine Staatsangehörigkeit fachlich oder rechtlich belegt ist,
- ob eine Person staatenlos ist,
- ob ein Identitätsnachweis vertrauenswürdig, gültig oder widerrufen ist,
- ob private Kontaktdaten veröffentlicht werden dürfen,
- ob ein Kontaktpunkt tatsächlich erreichbar ist,
- ob zusätzliche Properties anderer Construct-X-Module verwendet werden.

Diese Punkte sind entweder absichtlich offen, gehören in strengere Anwendungsprofile oder liegen in anderen fachlichen Modulen.

## 18. Testartefakte

Die Implementierung enthält mindestens folgende Dateien:

```text
modules/core/person/tests/valid/minimal-person.ttl
modules/core/person/tests/valid/complete-person.ttl
modules/core/person/tests/valid/gender-not-disclosed.ttl
modules/core/person/tests/invalid/missing-required-names.ttl
modules/core/person/tests/invalid/invalid-name-values.ttl
modules/core/person/tests/invalid/invalid-birth-values.ttl
modules/core/person/tests/invalid/invalid-controlled-values.ttl
modules/core/person/tests/invalid/invalid-identifier-and-evidence.ttl
```

Kontaktfälle gehören nach Anlage des Kontaktmoduls in dessen eigene Testverzeichnisse.

Automatisierte Tests prüfen:

1. alle gültigen Dateien sind konform,
2. jede ungültige Datei erzeugt mindestens den erwarteten Anforderungsbezeichner,
3. deutsche und englische Meldungen sind vorhanden,
4. jede beschlossene Maximal- oder Minimalkardinalität ist im Shape umgesetzt,
5. Referenzvokabulare werden in der Validierungsumgebung mitgeladen,
6. die Shapes funktionieren ohne RDFS- oder OWL-Inferenz, sofern explizite Typen verlangt werden.

## 19. Implementierungsreihenfolge

1. Gender- und Human-Sex-Referenzvokabulare versioniert anlegen. Erledigt.
2. `core/agent` und `core/person` T-Boxen implementieren. Erledigt.
3. Person Core Shapes aus diesem Dokument ableiten, einschließlich der minimalen ADMS-Constraints. Erledigt.
4. Gültige und ungültige Testgraphen anlegen. Erledigt.
5. Referenzgraphen in Build und Validierung integrieren. Erledigt.
6. Kontaktmodul separat spezifizieren und dessen Shapes implementieren.
7. HTML-Dokumentation erzeugen und Netzwerkmetadaten aktualisieren. Erledigt.

## 20. Abnahmekriterien der Core-Shape-Implementierung

Die Implementierung ist fachlich vollständig, wenn:

1. jede Anforderung `PER-*` in genau einem nachvollziehbaren Constraint umgesetzt ist,
2. die vier Sex- und vier Genderwerte geschlossen validiert werden,
3. Länder über den vorhandenen Referenzgraph geprüft werden,
4. Identifier nicht als Literale akzeptiert werden,
5. externe Identitätsnachweise als IRIs verlangt werden,
6. zusätzliche Properties anderer Module zulässig bleiben,
7. alle beschriebenen positiven und negativen Szenarien automatisiert geprüft werden,
8. keine Kontakt-, Credential- oder Organisationssemantik im Person Shape dupliziert wird.
