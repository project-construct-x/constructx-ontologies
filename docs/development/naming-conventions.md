<a id="benennungsregeln"></a>

# Naming Conventions

<a id="dateien-und-ordner"></a>

## Files and Folders

- Folder names use lowercase letters and hyphens.
- Ontology files use Turtle as their primary format.
- Module metadata is stored in `module.yaml`.
- Documentation is maintained in Markdown.

<a id="oeffentliche-construct-x-iris"></a>

## Public Construct-X IRIs

Construct-X uses dereferenceable HTTPS IRIs under the provisional authority `https://www.construct-x.org`.

Public ontology IRIs follow this pattern:

```text
https://www.construct-x.org/ontology/{module}
```

Term namespace:

```text
https://www.construct-x.org/ontology/{module}#
```

Version IRI:

```text
https://www.construct-x.org/ontology/{module}/{semver}
```

SHACL graphs and their shapes use a named shape set:

```text
https://www.construct-x.org/shapes/{module}/{shape-set}
https://www.construct-x.org/shapes/{module}/{shape-set}/{semver}
https://www.construct-x.org/shapes/{module}/{shape-set}#{localName}
```

Examples of shape sets include `core`, `delivery`, and `construction-site`.

Reference vocabularies use:

```text
https://www.construct-x.org/vocab/{vocabulary}
```

Vocabulary terms use:

```text
https://www.construct-x.org/vocab/{vocabulary}#{localName}
```

Persistent reference objects use:

```text
https://www.construct-x.org/id/{type}/{guid}
```

Exact revisions use:

```text
https://www.construct-x.org/id/{type}/{guid}/revision/{revision}
```

Repository categories such as `core`, `domain`, and `alignments` must not be part of public ontology IRIs.

<a id="prefixe"></a>

## Prefixes

Construct-X prefixes use the pattern `conx-{module-abbreviation}`. The module abbreviation is short, unique, stable, and lowercase.

Example:

```turtle
@prefix conx-vso: <https://www.construct-x.org/ontology/vso#> .
```

<a id="ontologiebegriffe"></a>

## Ontology Terms

New Construct-X terms follow these local naming rules:

- Classes: `UpperCamelCase`
- ObjectProperties: `lowerCamelCase`, phrased as a relationship, for example `hasPropertyReference`
- DataProperties: `lowerCamelCase`, without a relationship prefix such as `has` or `is`
- SHACL shapes: class name followed by `Shape`

Namespaces, IRIs, classes, and properties are derived only from supplied ontologies or approved domain decisions.
