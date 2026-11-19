# Construct-X Human Sex

This reference vocabulary provides the four language-independent codes from ISO/IEC 5218:2022 as stable SKOS concepts for the Construct-X ontology network.

The codes are stored as `skos:notation` with datatype `human-sex:iso-iec-5218`. This keeps the underlying code system machine-readable even when a notation is used in isolation.

<a id="öffentliche-iris"></a>

## Public IRIs

```text
Vocabulary IRI: https://www.construct-x.org/vocab/human-sex
Version IRI:    https://www.construct-x.org/vocab/human-sex/0.1.0
Namespace:      https://www.construct-x.org/vocab/human-sex#
Prefix:         human-sex
```

<a id="werte"></a>

## Values

| IRI suffix | Code | German | English |
| --- | --- | --- | --- |
| `notKnown` | `0` | Nicht bekannt | Not known |
| `male` | `1` | Männlich | Male |
| `female` | `2` | Weiblich | Female |
| `notApplicable` | `9` | Nicht anwendbar | Not applicable |

The absence of a `sex` statement is not equivalent to `notKnown`. `notApplicable` is not a gender category.

Source: [ISO/IEC 5218:2022](https://www.iso.org/standard/81682.html).
