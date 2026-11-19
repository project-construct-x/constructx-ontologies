<a id="ontologienetzwerk"></a>

# Core Dependency Registry

The [dependency registry](imports.lock.yaml) records external namespaces,
reference vocabularies and validation components used by this distribution.
Its `used_by` entries point only to included Core modules, datasets or the
VSO/ISOProps validation profile.

Each module's `module.yaml` is authoritative for that module's dependencies,
versions, shape sets and registered artifacts. Referencing an external IRI
does not automatically import or redistribute the external ontology.

For example, Status refers to Agent and VSO and validates against the Status
vocabularies, VSO Core shapes and the ISOProps profile. The manual
[Status validator](../scripts/validate_status.py) loads those dependencies
locally. The [bundle exporter](../scripts/status_bundle.py) packages them for
validation outside this repository.
