<a id="release-prozess"></a>

# Release Process

Automated publication is not configured in this Core repository. The Validate
workflow can be started manually; pushes and pull requests do not trigger it.

Before preparing a release:

1. Run `uv run python scripts/validate.py` and `uv run pytest`.
2. Review the module, shape and vocabulary versions and their changelogs.
3. Confirm source attribution and applicable licenses; see [NOTICE.md](../../NOTICE.md).
4. Run `uv run python scripts/build.py` and inspect the generated manifest and packages.
5. Agree on release approval, citation information, publication targets and namespace resolution.

The build recreates `dist/`; it does not commit, tag, push or publish anything.
Core modules and reference datasets are versioned independently according to
the [versioning rules](../architecture/versioning.md).
