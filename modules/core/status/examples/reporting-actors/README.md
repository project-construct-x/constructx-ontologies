# Persons and Organizations Reporting a Status

Alex reports that an object was delivered. Example Logistics reports that an
object was shipped. Each status has one reporting actor through reportedBy.
These examples use only Core classes; the delivery is an ordinary example
resource and does not require a domain ontology.

| Example | Reporter type | Required extra ontology context |
| --- | --- | --- |
| [Person](person-reporter.ttl) | conx-person:Person | [Person Core](../../../person/ontology/conx-person.ttl) |
| [Organization](organization-reporter.ttl) | conx-org:Organization | [Organization Core](../../../organization/ontology/conx-org.ttl) |

Both classes are subclasses of conx-agent:Agent in their existing Core
ontologies. The examples assert only Person or Organization. They neither
duplicate the class hierarchy nor add an extra Agent type to the reporter.

From the repository root, run:

```console
python scripts/validate_status.py --data modules/core/status/examples/reporting-actors/person-reporter.ttl --data modules/core/person/ontology/conx-person.ttl
python scripts/validate_status.py --data modules/core/status/examples/reporting-actors/organization-reporter.ttl --data modules/core/organization/ontology/conx-org.ttl
```

Both commands return `Conforms: True`. Omitting the extra ontology produces
STATUS-040 because the default Status bundle does not know these subclass
relationships. That is a missing-context error, not a prohibition of persons
or organizations. The Python API accepts the same Core graph through
`additional_ontology`.

For the exported bundle, use the same two `--data` arguments with
`python build/status-validation/validate.py`. Outside the repository, copy
the example and the corresponding ontology alongside the bundle, then use
their local paths. No remote import or change to the bundle is needed.

reportedBy remains optional and permits at most one IRI-valued Agent per
status assignment. A name string, an untyped resource, or two reporters on
the same assignment does not satisfy the contract. The reporting actor is
not automatically the driver, owner, recipient or person who took a measurement.

The additional ontology provides class relationships; it does not activate
the full Person or Organization validation rules. The tests also validate
these examples with the respective Core shapes and their local Identifier
dependency, so the example actor records satisfy those contracts too.

See [Core Shapes](../../docs/07_core-shapes.md) for the complete Status
validation package and [Module Boundaries](../../docs/04_module-boundaries.md)
for the division of responsibilities.
