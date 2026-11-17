# Status Core Shapes

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 11 November 2026  
**Scope:** `core/status`

## 1. Artifacts

- [Status Core graph](../shapes/conx-status-core.shacl.ttl)
- [Validation entry point](../../../../scripts/validate_status.py)
- [Standalone bundle exporter](../../../../scripts/status_bundle.py)
- [VSO Core graph](../../vso/shapes/conx-vso-core.shacl.ttl)
- [ISOProps graph](../../../../profiles/construct-x/vso-isoprops/shapes/conx-vso-isoprops.shacl.ttl)

The stable Status shape graph is
`https://www.construct-x.org/shapes/status/core`, version 0.1.0.

## 2. Shape Composition

StatusAssignmentShape targets typed assignments, subjects of assignment
properties and objects of hasStatus, hasCurrentStatus and previousStatus.
An omitted rdf:type therefore cannot bypass validation.
ResourceStatusShape checks navigation from the owner.
Its STATUS-064 and STATUS-065 constraints reject superseded or ambiguous
current selections. They compare only statuses of the same owner and kind,
using business instants and explicit predecessor paths. No current link is
required or generated.

RecordedAtShape combines datatype validation with an explicit lexical pattern
(STATUS-032), preventing permissive parser conversions from accepting malformed
timestamps. A regular timestamp uses sh:datatype xsd:dateTime. The alternative
RecordedAtEndOfDayShape supports the XSD 24:00:00 spelling even when a processor
cannot convert hour 24 to its native datetime type. Its SHACL-SPARQL constraint
checks the exact datatype, zero-valued smaller clock components and the
validity of the original calendar date. It temporarily substitutes hour 00
inside the calendar check; this checks the original date and does not compute
the equivalent next-day instant. The input graph and literal remain unchanged.

recordedAt remains optional, and a valid timestamp without a UTC offset remains
accepted. All these rules are included in the exported shape graph, so generic
SHACL-SPARQL processors use the same checks. For example, compare the
[valid recording without an offset](../tests/valid/recorded-at-without-offset.ttl)
with the rejected [space separator](../tests/invalid/recorded-at-space-separator.ttl)
and [excessive offset](../tests/invalid/recorded-at-invalid-offset.ttl) fixtures.
The [year-end midnight example](../tests/valid/recorded-at-midnight.ttl) and
[leap-day example without an offset](../tests/valid/recorded-at-midnight-without-offset.ttl)
show valid end-of-day spellings. An
[invalid calendar date at midnight](../tests/invalid/recorded-at-midnight-invalid-date.ttl)
still fails STATUS-032.

KindConceptShape, ValueConceptShape and ReasonConceptShape validate references.
ManagedMetadataPolicyShape applies the local publication requirements only to
the three Construct-X status vocabulary namespaces.

ConditionAssignmentShape invokes the existing VSO and ISOProps assignment
shapes. Additional paths invoke the VSO state and ISOProps definition shapes.
The loader copies shared definitions without their global targets and retains
their constraints and IRIs. Simply concatenating the unscoped source graphs
is not equivalent: it would also validate unrelated VSO data.

The source Status shape file references shared named shapes and therefore
requires the source loader or an assembled bundle. Repository builds now
publish a complete graph at `dist/modules/core/status/shapes/conx-status-core.shacl.ttl`,
including the scoped VSO/ISOProps definitions. The accompanying `validation/`
directory contains the complete offline package. This is generated from the
same composition used by the source validator, rather than maintained twice.

## 3. Running an Example

From the repository root:

```console
python scripts/validate_status.py --data modules/core/status/examples/status-with-condition.ttl
```

Expected output includes `Conforms: True`. Exit codes are 0 for valid data,
1 for a validation failure and 2 for a missing or mismatched local dependency.
Repeat `--data` to supply extra local vocabulary or context files.
`--no-reference-vocabularies` lets the caller supply all reference data.

For Person and Organization reporters, the
[reporting actor guide](../examples/reporting-actors/README.md) supplies two
worked examples and complete commands. Pass the relevant Person or
Organization Core ontology as another `--data` file. In the Python API, pass
the loaded ontology as `additional_ontology`. The same extra context works
with the standalone runner and with a generic SHACL processor. Without it,
a reporter typed only as Person or Organization fails STATUS-040.

The loader preserves literal lexical forms for validation, including offsets.
The Python API accepts an already constructed RDF graph; callers constructing
that graph must preserve information they expect the validator to check.
The command-line runner reports invalid values through SHACL and suppresses
RDFLib's native-conversion warnings, including its warning for valid hour 24.
Library callers retain control of their own logging configuration.

To export only the Status package without building any other modules:

```console
python scripts/status_bundle.py --output build/status-validation
python build/status-validation/validate.py --data modules/core/status/examples/status-with-condition.ttl
```

The resulting directory can be copied outside the repository. It contains:

| File | Use |
| --- | --- |
| shapes.ttl | Complete scoped SHACL-SPARQL graph |
| ontology.ttl | Status, Agent and VSO ontology context |
| vocabularies.ttl | The three initial reference vocabularies |
| validate.py | Standalone runner; requires Python 3.12+, RDFLib and pySHACL |
| bundle.json | Package version and checksums of the three RDF components |
| README.md | Standalone usage and integration instructions |

For another SHACL-SPARQL engine, merge vocabularies.ttl into the input data
and supply ontology.ttl as ontology context, alongside shapes.ttl. Preserve
literal lexical forms when parsing. No source checkout or remote imports are
needed. The runner rejects missing or altered components with exit code 2.

## 4. Test Mapping

| Test module | Responsibility |
| --- | --- |
| test_status_ontology.py | Public terms, metadata and module boundaries |
| test_status_shapes.py | Valid/invalid status fixtures, diagnostics, CLI and SHACL syntax |
| test_status_reference_vocabularies.py | Initial reference terms and managed publication rules |
| test_status_vso_isoprops.py | Measurements, dependency scoping and missing-dependency handling |
| test_status_regressions.py | Malformed literal contents, equal-time predecessors and microsecond ordering |
| test_status_current.py | Optional current links, latest business instants, unresolved ties, predecessor chains and object/kind isolation |
| test_status_reporters.py | Actual Person/Organization Core types, missing context, reporter cardinality, actor Core contracts, CLI and relocated bundle |
| test_status_bundle.py | Relocated standalone package, diagnostics and dependency integrity |
| test_status_integration.py | Documentation and validation with the actual published build graph |

Run these together with the existing Core documentation, namespace, metadata,
versioning and build tests. The general repository validator checks Turtle and
manifest integrity; these tests execute the semantic SHACL rules.

## 5. Invalid Example

[missing-offset.ttl](../tests/invalid/missing-offset.ttl) provides a local
clock time without its UTC offset. It must fail STATUS-031 even though all
other mandatory fields are present.
