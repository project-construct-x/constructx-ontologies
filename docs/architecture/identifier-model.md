<a id="kennungsmodell-im-construction-x-ontologienetzwerk"></a>

# Identifier Model in the Construction-X Ontology Network

<a id="entscheidung"></a>

## Decision

The ontology network uses the W3C ADMS vocabulary for business identifiers.
No parallel Construction-X class for identifiers is introduced.
A resource uses `adms:identifier` to reference an instance of
`adms:Identifier`. The identifier value is stored in `skos:notation`; the
literal's datatype identifies the identifier scheme being used.

The shared semantic and validation contract is versioned in the Core module
[`identifier`](../../modules/core/identifier/README.md). The executable
`conx-id-sh:ADMSIdentifierShape` is reused by the relevant Core shape graphs.

```turtle
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix id-scheme: <https://www.construct-x.org/vocab/identifier-scheme#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://www.construct-x.org/vocab/country#DEU>
    adms:identifier [
        a adms:Identifier ;
        skos:notation "DE"^^id-scheme:iso-3166-1-alpha-2 ;
        adms:schemaAgency "International Organization for Standardization (ISO)"
    ] .
```

<a id="verwendete-kennungssysteme"></a>

## Identifier Schemes in Use

| Datatype IRI | Meaning |
| --- | --- |
| `id-scheme:iso-3166-1-alpha-2` | Two-letter ISO 3166-1 code |
| `id-scheme:iso-3166-1-alpha-3` | Three-letter ISO 3166-1 code |
| `id-scheme:iso-3166-1-numeric` | Three-digit numeric ISO 3166-1 code |
| `id-scheme:iso-3166-2` | ISO 3166-2 code of an administrative subdivision |
| `id-scheme:nuts-2` | Code of a NUTS level 2 region |

The datatype IRIs are stable identifiers for the identifier schemes used in
the network. They do not introduce new identifier logic. The semantics of
identifiers, identifier values, and issuing agencies come from ADMS and SKOS.
The corresponding graph is published as a reference vocabulary under the
stable IRI `https://www.construct-x.org/vocab/identifier-scheme`, with version
`0.2.0` published at
`https://www.construct-x.org/vocab/identifier-scheme/0.2.0`.

<a id="modellierungsregeln"></a>

## Modeling Rules

1. Domain resources do not receive system-specific properties such as
   `isoAlpha2Code` or `isoSubdivisionCode`.
2. Each identifier is modeled as a separate `adms:Identifier` resource.
3. The value is specified exactly once using `skos:notation`.
4. The identifier scheme is identified by the notation's datatype.
5. The issuing agency can be documented using `adms:schemaAgency`.
6. A resource may have multiple identifiers from different schemes.

The same pattern is reused for person, organization, membership, document,
and document-reference identifiers. Additional domain modules can use it
without defining their own identifier structure.

<a id="abgrenzung"></a>

## Boundaries

The identifier model does not determine which identifier makes a resource
addressable in the Construction-X network. The stable resource IRI and its
business identifiers are separate concepts. An A-Box containing ISO identifiers
does not replace general master-data or history-management logic either.

<a id="normative-grundlage"></a>

## Normative References

- [Asset Description Metadata Schema (ADMS) 2.0](https://semiceu.github.io/ADMS/releases/2.00/)
- [SKOS Simple Knowledge Organization System](https://www.w3.org/TR/skos-reference/)
- [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.html)


