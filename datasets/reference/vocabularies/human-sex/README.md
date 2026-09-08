# Construct-X Human Sex

Dieses Referenzvokabular stellt die vier sprachunabhängigen Codes aus ISO/IEC 5218:2022 als stabile SKOS-Konzepte für das Construct-X-Ontologienetzwerk bereit.

Die Codes werden als `skos:notation` mit dem Datentyp `human-sex:iso-iec-5218` geführt. Dadurch bleibt das zugrunde liegende Codesystem auch bei einer isolierten Notation maschinenlesbar.

## Öffentliche IRIs

```text
Vokabular-IRI: https://www.construct-x.org/vocab/human-sex
Versions-IRI:  https://www.construct-x.org/vocab/human-sex/0.1.0
Namespace:     https://www.construct-x.org/vocab/human-sex#
Prefix:        human-sex
```

## Werte

| IRI-Suffix | Code | Deutsch | Englisch |
| --- | --- | --- | --- |
| `notKnown` | `0` | Nicht bekannt | Not known |
| `male` | `1` | Männlich | Male |
| `female` | `2` | Weiblich | Female |
| `notApplicable` | `9` | Nicht anwendbar | Not applicable |

Das Fehlen einer `sex`-Aussage ist nicht gleichbedeutend mit `notKnown`. `notApplicable` ist keine Genderkategorie.

Quelle: [ISO/IEC 5218:2022](https://www.iso.org/standard/81682.html).
