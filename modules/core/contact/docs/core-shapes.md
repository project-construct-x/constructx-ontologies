# Contact Core Shapes

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** Contact Core Shapes

Die Contact Core Shapes validieren die allgemeinen, anwendungsfallunabhängigen Datenverträge der Construct-X Kontaktontologie. Die T-Box bleibt unter der Open-World-Annahme semantisch offen; das Core-Profil prüft dagegen konkrete Datenlieferungen.

```text
Shape-Graph:  modules/core/contact/shapes/conx-contact-core.shacl.ttl
Shape-IRI:    https://www.construct-x.org/shapes/contact/core
Versions-IRI: https://www.construct-x.org/shapes/contact/core/0.1.0
Namespace:    https://www.construct-x.org/shapes/contact/core#
Version:      0.1.0
```

## 1. Geprüfte Verträge

- Werte von `hasContactPoint` müssen als `conx-contact:ContactPoint` typisiert sein.
- `hasContactPoint` typisiert das Subjekt nicht hart als `conx-agent:Agent`.
- Jeder `ContactPoint` muss Blank Node oder IRI sein, explizit als `conx-contact:ContactPoint` typisiert sein und mindestens eine `ContactMethod` besitzen.
- `contactUsage` darf höchstens einmal vorkommen und muss auf das freigegebene `contact-usage`-Vokabular verweisen.
- `contactPurpose` verweist auf das freigegebene `contact-purpose`-Vokabular.
- Beschreibende Textwerte wie `contactName`, `departmentName`, `functionTitle` und `availabilityNote` dürfen nicht leer sein.
- Jede `ContactMethod` muss Blank Node oder IRI sein, explizit als `conx-contact:ContactMethod` typisiert sein und genau einen freigegebenen `contactChannel` besitzen.
- E-Mail, Telefon, Mobiltelefon und Fax verwenden genau einen nicht-leeren `contactValue` als `xsd:string`.
- Website und Social Profile verwenden genau eine IRI über `contactURI`.
- Messenger verwendet genau einen nicht-leeren `contactValue` oder genau eine IRI über `contactURI`.
- Postalische Kontaktmethoden verwenden genau ein `usesAddressAssignment` auf eine `conx-addr:AddressAssignment`.
- `contactPlatform` darf höchstens einmal vorkommen und muss auf das freigegebene `contact-platform`-Vokabular verweisen.

Zusatzproperties bleiben zulässig. Das Profil verwendet kein `sh:closed true` und benötigt keine RDFS- oder OWL-Inferenz.

## 2. Referenzgraphen

Für die Prüfung kontrollierter Werte werden gemeinsam mit den Daten geladen:

- `datasets/reference/vocabularies/contact-channel/contact-channel.ttl`,
- `datasets/reference/vocabularies/contact-usage/contact-usage.ttl`,
- `datasets/reference/vocabularies/contact-purpose/contact-purpose.ttl`,
- `datasets/reference/vocabularies/contact-platform/contact-platform.ttl`,
- `modules/core/address/ontology/conx-addr.ttl`,
- `datasets/reference/vocabularies/address-roles/address-roles.ttl`, wenn postalische Adresszuordnungen vollständig validiert werden.

Die kleinen Kontaktwertemengen sind zusätzlich als geschlossene `sh:in`-Listen im Shape-Graph festgehalten. Neue Kanäle, Nutzungen, Zwecke oder Plattformen sollen daher bewusst versioniert werden.

## 3. Testdaten

Gültige Testgraphen liegen unter `modules/core/contact/tests/valid`. Gezielte Fehlerfälle liegen unter `modules/core/contact/tests/invalid`. Die automatisierten Tests laden die erforderlichen Referenzgraphen, führen PySHACL ohne Inferenz aus und prüfen Fehlermeldungs-IDs.

Die automatisierte Shape-Prüfung kann aus dem Repository-Stamm so ausgeführt werden:

```text
uv run pytest tests/test_contact_shapes.py
```

Direkte `pyshacl`-Aufrufe müssen die genannten Referenzgraphen ebenfalls in den Validierungsdatengraph laden. Dies übernimmt die automatisierte Testsuite.

## 4. Bewusst nicht geprüft

- ob eine Telefonnummer tatsächlich erreichbar ist,
- ob eine E-Mail-Adresse existiert,
- strenge E-Mail- oder Telefonnummernsyntax,
- ob eine Social-Profile-URL wirklich zur angegebenen Plattform gehört,
- wer private Kontaktdaten sehen oder verwenden darf,
- Öffnungszeiten, Servicegebiete, Prioritäten und Zustellbarkeit,
- Personen-, Organisations-, Rollen- oder Adressdetails jenseits der `AddressAssignment`-Referenz.

Diese Bereiche gehören in spätere Fachprofile oder eigenständige Module.

## 5. Verständliches Beispiel

> Ein Kontaktpunkt ohne Kontaktmethode ist ungültig, weil niemand darüber
> erreicht werden kann. Ein geschäftlicher Kontaktpunkt mit einer korrekt
> typisierten E-Mail-Methode erfüllt dagegen den Core-Vertrag.
