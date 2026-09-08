# Construct-X Core Ontologies

Dieses Repository stellt die fachübergreifend wiederverwendbaren
Core-Ontologien von Construct-X bereit. Es enthält bewusst keine Domain-
Ontologien, anwendungsspezifischen Profile oder optionalen Alignments.

**Status:** Draft
**Aktueller Modulstand:** `0.1.0`

## Core-Module

| Modul | Inhalt |
| --- | --- |
| [Address](modules/core/address/README.md) | strukturierte Adressen und Adresszuordnungen |
| [Agent](modules/core/agent/README.md) | gemeinsame Oberklasse für handelnde Akteure |
| [Contact](modules/core/contact/README.md) | Kontaktpunkte und Kontaktmethoden |
| [Document](modules/core/document/README.md) | Dokumente, Referenzen und technische Distributionen |
| [Identifier](modules/core/identifier/README.md) | gemeinsamer ADMS/SKOS-Kennungsvertrag |
| [Organization](modules/core/organization/README.md) | Organisationen, Einheiten, Mitgliedschaften und Vertretungen |
| [Participation](modules/core/participation/README.md) | Rollen von Agenten in fachlichen Kontexten |
| [Person](modules/core/person/README.md) | intrinsische Kerndaten natürlicher Personen |
| [VSO](modules/core/vso/README.md) | Zuweisung von Merkmalen, Werten und Einheiten |

## Repository-Struktur

```text
modules/core/       Ontologien, Shapes, Dokumentation und Testdaten
datasets/reference/ kontrollierte Werte und administrative Referenzdaten
docs/               Architektur- und Einstiegshilfen
network/            dokumentierte externe Abhängigkeiten
scripts/            Validierung und Build
tests/              automatisierte Core-Prüfungen
```

## Einstieg

Vorausgesetzt werden Python 3.12 oder neuer und
[uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/project-construct-x/constructx-ontologies.git
cd constructx-ontologies
uv sync --locked
```

Repository validieren und Tests ausführen:

```bash
uv run python scripts/validate.py
uv run pytest
```

Ein auslieferbares Paket wird unter `dist/` erzeugt:

```bash
uv run python scripts/build.py
```

## Dokumentation

Der Einstieg liegt unter [docs/README.md](docs/README.md). Jedes Core-Modul
enthält zusätzlich eine kompakte `docs/confluence-overview.md` sowie die
ausführlichen fachlichen und technischen Dokumente.

## Lizenz

Code steht unter Apache License 2.0, siehe [LICENSE](LICENSE). Ontologien,
Dokumentation und weitere Nicht-Code-Inhalte stehen unter CC BY 4.0, siehe
[LICENSE_non-code](LICENSE_non-code). Quellen und abweichende Hinweise stehen
in den jeweiligen Metadaten und in [NOTICE.md](NOTICE.md).
