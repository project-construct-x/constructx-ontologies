# Core-Module

Core-Module enthalten fachübergreifend wiederverwendbare Ontologien. Sie bilden gemeinsame Grundlagen, die von mehreren fachlichen Modulen verwendet werden können.

Die gemeinsame Form, die Pflichtdokumente und die Anforderungen an
verständliche Beispiele sind im
[Dokumentationsstandard](DOCUMENTATION.md) festgelegt.

Aktuelle Core-Module:

- `vso`: Construct-X Value Semantics Ontology
- `address`: Construct-X Address Ontology
- `agent`: minimale gemeinsame Oberklasse für Akteure
- `identifier`: gemeinsamer ADMS/SKOS-Vertrag für fachliche Kennungen
- `person`: Kerndaten realer natürlicher Personen
- `contact`: Kontaktpunkte und Kommunikationskanäle
- `organization`: Organisationen, rechtliche Einheiten, Organisationseinheiten, Mitgliedschaften und rechtliche Vertretungen
- `participation`: qualifizierte Rollen von Agenten in fachlichen Kontexten
- `document`: Dokumente, kontextbezogene Referenzen, technische Distributionen, Dokumenttypen und Dokumentstatus

Core-Module dürfen keine Domain-Module importieren. Externe Ontologien dürfen nur verwendet werden, wenn ihre Imports, Versionen und Rollen nachvollziehbar dokumentiert sind.
