# Versionierung

Jedes Ontologiemodul und jedes Referenzdatenartefakt wird nachvollziehbar versioniert. Construct-X unterscheidet dabei drei Modelle.

## 1. Ontologien und SHACL-Graphen

Ontologien und SHACL-Graphen werden als vollstaendige Graphen mit SemVer versioniert.

Regeln:

- Die stabile Graph-IRI bleibt unveraendert.
- Jede Veroeffentlichung erhaelt eine SemVer-Versions-IRI.
- Begriffs-IRIs enthalten keine Versionsnummer.
- Veroeffentlichte Versionen sind unveraenderlich.
- Die unversionierte Graph-IRI verweist auf die aktuelle empfohlene Version.
- Aeltere Versionen bleiben ueber ihre Versions-IRIs erreichbar.
- Entfernte IRIs duerfen niemals fuer andere Begriffe wiederverwendet werden.

SHACL-Graphen werden pro Modul in benannte Shape-Sets gegliedert. Dadurch
koennen allgemeine Core-Regeln und spaetere Anwendungsprofile unabhaengig
versioniert werden:

```text
Stabiler Core-Shape-Graph: https://www.construct-x.org/shapes/address/core
Core-Shape-Version:       https://www.construct-x.org/shapes/address/core/0.1.0
Shape-Namespace:          https://www.construct-x.org/shapes/address/core#
```

Beispiel Address Ontology:

```text
Ontologie-IRI: https://www.construct-x.org/ontology/address
Versions-IRI:  https://www.construct-x.org/ontology/address/0.1.0
Namespace:     https://www.construct-x.org/ontology/address#
```

## 2. Referenzvokabulare

Referenzvokabulare werden ebenfalls als vollstaendige Graphen mit SemVer versioniert.

Regeln:

- Die stabile Vokabular-IRI bleibt unveraendert.
- Jede Veroeffentlichung erhaelt eine SemVer-Versions-IRI.
- Vokabularbegriffe enthalten keine Versionsnummer.
- Veroeffentlichte Versionen sind unveraenderlich.
- Begriffe werden moeglichst nicht geloescht, sondern als veraltet gekennzeichnet.

Beispiel:

```text
Vokabular:        https://www.construct-x.org/vocab/wall-type
Vokabularversion: https://www.construct-x.org/vocab/wall-type/1.2.0
Begriff:          https://www.construct-x.org/vocab/wall-type#ExternalWall
```

Eine neue Vokabularversion erzeugt nicht automatisch neue IRIs fuer unveraendert fortbestehende Begriffe.

## 3. Referenzobjekte

Referenzobjekte unter `/id/` werden individuell versioniert und verwenden kein SemVer.

Regeln:

- Eine fachliche Version besitzt eine GUID.
- Eine Revision behaelt die GUID und erhoeht die Revisionsnummer.
- Eine neue fachliche Version erhaelt eine neue GUID.
- Veroeffentlichte Revisionen sind unveraenderlich.
- Normative und reproduzierbare Referenzen verwenden GUID und Revisionsnummer.

Beispiel:

```text
Aktuelle Revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000

Exakte Revision:
https://www.construct-x.org/id/property/550e8400-e29b-41d4-a716-446655440000/revision/2
```

Die SemVer-Version eines veroeffentlichten Graphen und die Revision eines darin beschriebenen Referenzobjekts sind voneinander unabhaengige Angaben.

Die ausfuehrliche Regelung steht in `docs/architecture/construct-x-namespace-konzept.md`.
