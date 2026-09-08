# Abhaengigkeitsregeln

1. Core-Module duerfen andere Core-Module und externe Ontologien verwenden.
2. Domain-Module duerfen Core-Module verwenden.
3. Core-Module duerfen keine Domain-Module importieren.
4. Alignments bleiben optional.
5. Profile duerfen strengere Vorgaben als die allgemeinen Ontologien definieren.
6. T-Box und A-Box bleiben getrennt.
7. SHACL-Shapes bleiben von OWL-T-Boxen getrennt.
8. Fremdontologien werden nicht lokal neu definiert.
9. Externe Imports und getestete Versionen werden dokumentiert.
10. Jedes Ontologiemodul wird unabhaengig versioniert.

## Zweck

Die Regeln stellen sicher, dass das Ontologienetzwerk modular, nachvollziehbar und wartbar bleibt. Kernontologien sollen nicht von spaeteren Anwendungssichten oder fachlichen Spezialfaellen abhaengen.

## Imports

Externe Imports werden nur dokumentiert, wenn sie aus bereitgestellten Ontologien oder fachlich freigegebenen Entscheidungen belegbar sind. Versionen und getestete Staende werden in `network/imports.lock.yaml` gepflegt.

Die derzeit integrierte CX-VSO enthaelt keine `owl:imports`. Referenzierte externe Namespaces werden deshalb als `referenced-not-imported` dokumentiert.
