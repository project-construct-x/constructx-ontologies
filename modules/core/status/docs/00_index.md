# Status Module Index

**Status:** Implemented; draft release  
**Version:** 0.1.0  
**As of:** 17 November 2026  
**Scope:** `core/status`

## 1. Overview

The module is implemented as draft version 0.1.0. The ontology defines the
vocabulary; the SHACL graph defines validation requirements. The complete
runtime bundle is assembled by [validate_status.py](../../../../scripts/validate_status.py).
It can also be exported as a complete standalone package using
[status_bundle.py](../../../../scripts/status_bundle.py); see
[Core Shapes](07_core-shapes.md) for the commands and package contents.

## 2. Introduction for Nontechnical Readers

Think of a status assignment as a dated note attached to an object:
"At 10:00 +01:00, this delivery was shipped." A second note may describe a
different question, such as whether its temperature inspection passed.

The status **kind** identifies the question, the **value** is the answer,
and optional **reasons** explain the answer. A vocabulary groups reusable terms;
a status refers directly to a term, not to the whole vocabulary.

The optional hasCurrentStatus link identifies the uniquely latest known
statement for an object and kind. If the latest statements have equal times
and no known order, the link must be omitted until the ambiguity is resolved.

## 3. Documentation Package

- [source analysis](01_source-analysis.md)
- [scope and competency questions](02_scope-and-competency-questions.md)
- [concept model](03_concept-model.md)
- [module boundaries](04_module-boundaries.md)
- [term catalog](05_term-catalog.md)
- [shacl requirements](06_shacl-requirements.md)
- [core shapes](07_core-shapes.md)
- [concept diagram](08_concept-diagram.md)
- [Confluence Overview (German)](09_confluence-overview.md)

The Confluence overview uses German as the agreed publication language.
The detailed repository documentation remains in English.

## 4. Technical Artifacts

- [Module metadata](../module.yaml)
- [Ontology](../ontology/conx-status.ttl)
- [Core shapes](../shapes/conx-status-core.shacl.ttl)
- [Generated HTML](status.html)
- [Status kinds](../../../../datasets/reference/vocabularies/status-kind/README.md)
- [Status values](../../../../datasets/reference/vocabularies/status-value/README.md)
- [Status reasons](../../../../datasets/reference/vocabularies/status-reason/README.md)

## 5. Examples and Tests

| Scenario | Runnable example |
| --- | --- |
| Smallest complete statement | [Minimal status](../examples/minimal-status.ttl) |
| Three stages and a selected current status | [History](../examples/status-history.ttl) |
| Late recording does not change which status is current | [Current status](../examples/current-status-selection.ttl) |
| Independent transport and inspection states | [Multiple kinds](../examples/multiple-status-kinds.ttl) |
| More than one explanation | [Multiple reasons](../examples/multiple-status-reasons.ttl) |
| A failed inspection with a measurement | [Condition](../examples/status-with-condition.ttl) |
| A Person reporting delivery | [Person reporter](../examples/reporting-actors/person-reporter.ttl) |
| An Organization reporting dispatch | [Organization reporter](../examples/reporting-actors/organization-reporter.ttl) |

Positive and negative Turtle fixtures are in `tests/valid/` and `tests/invalid/`.
The repository's `tests/test_status_*.py` files exercise the full contracts.
See [Core Shapes](07_core-shapes.md) for commands and dependency composition.
The [reporting actor guide](../examples/reporting-actors/README.md) provides
the extra Core ontology context required by the two reporter examples.

## 6. Additional Documents

The existing `# Fragen.md` in the module directory is a historical,
non-normative working note. It is retained unchanged. The current specification
is the numbered package above. See also the [changelog](../CHANGELOG.md).
