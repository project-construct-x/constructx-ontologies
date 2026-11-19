# Contributing

Please remember and follow our [Code of Conduct](./CODE_OF_CONDUCT.md).

## How to Contribute

- Report bugs, suggest features, and discuss tasks via GitHub **Issues**
    - Please use and fill in the existing Issue templates
- Create GitHub **Pull Requests** to the `main` branch for all repository changes
    - It is highly recommended to link every pull request to at least one issue

## Best Practices

- Add a license header to your files
- Use [Conventional Commits](https://www.conventionalcommits.org/en) (preferred)
- [Sign your commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) (preferred)

## Ontology Contributions

- Keep T-Box ontologies, SHACL Shapes, examples and reference data separated.
- Update the module documentation and changelog together with semantic changes.
- Keep this distribution limited to Core ontologies and their supporting data and validation dependencies. The included VSO/ISOProps profile supports the Status contract; Domain ontologies, unrelated application profiles and optional Alignments remain outside this repository.
- Validate the repository with `uv run python scripts/validate.py`.
- Run the Core test suite with `uv run pytest` before opening a pull request.
