<a id="abhaengigkeitsregeln"></a>

# Dependency Rules

1. Core modules may use other Core modules and external ontologies.
2. Domain modules may use Core modules.
3. Core modules must not import Domain modules.
4. Alignments remain optional.
5. Profiles may define stricter requirements than the general ontologies.
6. T-Boxes and A-Boxes remain separate.
7. SHACL shapes remain separate from OWL T-Boxes.
8. External ontologies are not redefined locally.
9. External imports and tested versions are documented.
10. Each ontology module is versioned independently.

<a id="zweck"></a>

## Purpose

These rules ensure that the ontology network remains modular, traceable, and maintainable. Core ontologies should not depend on later application views or specialized domain cases.

## Imports

External imports are documented only when they can be substantiated from supplied ontologies or approved domain decisions. Versions and tested releases are maintained in `network/imports.lock.yaml`.

The currently integrated CX-VSO contains no `owl:imports`. Referenced external namespaces are therefore documented as `referenced-not-imported`.
