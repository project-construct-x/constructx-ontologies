# Document Core Shapes

**Status:** Implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** Document Core Shapes

The Document Core Shapes validate the general, cross-domain data contracts of the Construct-X Document Ontology. The T-Box remains semantically open under the open-world assumption; the core profile checks concrete data submissions.

```text
Shape graph: modules/core/document/shapes/conx-doc-core.shacl.ttl
Shape IRI:   https://www.construct-x.org/shapes/document/core
Version IRI: https://www.construct-x.org/shapes/document/core/0.1.0
Namespace:   https://www.construct-x.org/shapes/document/core#
Version:     0.1.0
```

The shape graph imports the versioned contract `https://www.construct-x.org/shapes/identifier/core/0.1.0`.

## 1. Target Strategy

`Document`, `DocumentReference`, and `DocumentDistribution` are targeted through their classes and through unambiguous incoming or local properties. The shared properties `documentType` and `hasDistribution` activate a separate `DocumentCarrierShape`. This requires the subject to be typed as `Document` or `DocumentReference` without additionally turning a document reference into a document.

External DCAT properties are deliberately not global targets. They are checked only on resources already recognized as `DocumentDistribution`. This prevents the module from affecting arbitrary external DCAT data graphs.

## 2. Validated Contracts

- Documents, references, and distributions must be resources and explicitly typed with the respective Construct-X class.
- Values of `hasDocumentReference` must be typed `DocumentReference` resources.
- A `DocumentReference` must have at least one target: a modeled document, an external IRI through `dcterms:references`, or a distribution.
- `referencesDocument` and `dcterms:references` may each occur at most once.
- `documentType` and `documentStatus` use only approved reference vocabularies; status is intended only for documents.
- Title and description allow non-empty `xsd:string` or `rdf:langString` values.
- Language, version, and filename must be non-empty `xsd:string` values.
- `created`, `issued`, `modified`, `validFrom`, and `validUntil` each allow at most one `xsd:date` or `xsd:dateTime` value.
- `validFrom` must not be later than `validUntil`. If both values are supplied, they should use the same datatype for unambiguous comparison.
- `hasDistribution` references only typed `DocumentDistribution` resources.
- `dcat:accessURL` and `dcat:downloadURL` must be IRIs.
- `dcat:mediaType` may occur at most once as an IANA-oriented IRI.
- ADMS identifiers are validated by `identifier/core` and require type `adms:Identifier`, exactly one literal `skos:notation`, and at most one `adms:schemaAgency` as `xsd:string`.

Additional properties remain permitted. The profile does not use `sh:closed true` and requires no RDFS or OWL inference.

## 3. Reference Graphs

For controlled values, the following graphs are loaded together with the data:

- `datasets/reference/vocabularies/document-type/document-type.ttl`,
- `datasets/reference/vocabularies/document-status/document-status.ttl`.

The approved values are additionally recorded as closed `sh:in` lists in the shape graph. Extensions to the value sets therefore require deliberate versioning of both the vocabulary and the shape set.

The integration test for actor roles additionally loads:

- `modules/core/agent/ontology/conx-agent.ttl`,
- `modules/core/participation/ontology/conx-part.ttl`,
- `modules/core/participation/shapes/conx-part-core.shacl.ttl`,
- `datasets/reference/vocabularies/participation-role/participation-role.ttl`.

This demonstrates that actor roles associated with documents can be modeled through Participation rather than direct Document properties.

## 4. Test Data

Valid test graphs:

- `minimal-document.ttl`: IRI and blank node as minimal documents,
- `complete-document.ttl`: metadata, ADMS identifier, validity, and PDF,
- `multiple-distributions.ttl`: PDF, XML, and a technical placeholder distribution,
- `document-references.ttl`: modeled, external, and distribution-based targets,
- `document-with-participation.ttl`: integration with Agent and Participation.

Invalid test graphs:

- `invalid-document-typing.ttl`: missing or incorrect resource typing,
- `invalid-document-references.ttl`: missing, incorrect, or excessive targets,
- `invalid-distributions.ttl`: incorrect URL, filename, and media type values,
- `invalid-controlled-values.ttl`: unapproved type and status values,
- `invalid-metadata-and-identifiers.ttl`: literal, date, validity, and identifier violations.

The automated shape tests are run from the repository root:

```text
uv run pytest tests/test_document_shapes.py
```

The suite additionally validates the shape graph against SHACL-SHACL, checks version metadata, and ensures that every approved error code is covered by at least one negative test graph.

## 5. Deliberately Excluded Checks

- UBL conformance or UBL mappings,
- digital signatures, seals, or credential status,
- domain-specific Evidence or Requirement satisfaction,
- actor roles without a loaded Participation Shape,
- rights, access, confidentiality, and workflow status,
- URL reachability or file existence,
- storage, DMS, archiving, or retention rules,
- mandatory domain-specific metadata for individual document types.

These requirements belong in profiles or specialized modules.

## 6. Illustrative Example

> The core checks that a distribution is described in terms of technical access. It does not decide whether a particular business process requires a signed PDF file.