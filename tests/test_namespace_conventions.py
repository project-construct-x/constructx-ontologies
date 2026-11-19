import re
from pathlib import Path

from rdflib import Graph, RDF, OWL, URIRef


ROOT = Path(__file__).resolve().parents[1]
CONX_AUTHORITY = "https://www.construct-x.org"
SEMVER_RE = re.compile(r"^https://www\.construct-x\.org/ontology/[a-z][a-z0-9-]*/\d+\.\d+\.\d+$")
CLASS_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
OBJECT_PROPERTY_RE = re.compile(r"^(has|is|belongsTo|contains|classifiedAs)[A-Z]?[A-Za-z0-9]*$")
DATA_PROPERTY_RE = re.compile(r"^[a-z][A-Za-z0-9]*$")

MODULES = [
    {
        "path": ROOT / "modules/core/status/ontology/conx-status.ttl",
        "ontology_iri": URIRef("https://www.construct-x.org/ontology/status"),
        "version_iri": URIRef("https://www.construct-x.org/ontology/status/0.1.0"),
        "namespace": "https://www.construct-x.org/ontology/status#",
        "prefix": "conx-status",
        "known_object_property_deviations": {"previousStatus", "reportedBy"},
        "known_data_property_deviations": set(),
    },
    {
        "path": ROOT / "modules/core/vso/ontology/conx-vso.ttl",
        "ontology_iri": URIRef("https://www.construct-x.org/ontology/vso"),
        "version_iri": URIRef("https://www.construct-x.org/ontology/vso/0.1.0"),
        "namespace": "https://www.construct-x.org/ontology/vso#",
        "prefix": "conx-vso",
        "known_object_property_deviations": set(),
        "known_data_property_deviations": set(),
    },
    {
        "path": ROOT / "modules/core/address/ontology/conx-addr.ttl",
        "ontology_iri": URIRef("https://www.construct-x.org/ontology/address"),
        "version_iri": URIRef("https://www.construct-x.org/ontology/address/0.2.0"),
        "namespace": "https://www.construct-x.org/ontology/address#",
        "prefix": "conx-addr",
        "known_object_property_deviations": {
            "locationRole",
            "assignedAddress",
            "broaderAdministrativeTerritory",
        },
        "known_data_property_deviations": set(),
    },
    {
        "path": ROOT / "modules/core/participation/ontology/conx-part.ttl",
        "ontology_iri": URIRef("https://www.construct-x.org/ontology/participation"),
        "version_iri": URIRef("https://www.construct-x.org/ontology/participation/0.3.0"),
        "namespace": "https://www.construct-x.org/ontology/participation#",
        "prefix": "conx-part",
        "known_object_property_deviations": set(),
        "known_data_property_deviations": set(),
    },
]


def load_graph(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def local_name(uri: URIRef) -> str:
    return str(uri).split("#", 1)[1]


def test_construct_x_ontology_iri_namespace_version_and_prefix() -> None:
    for module in MODULES:
        graph = load_graph(module["path"])

        assert list(graph.subjects(RDF.type, OWL.Ontology)) == [module["ontology_iri"]]
        assert list(graph.objects(module["ontology_iri"], OWL.versionIRI)) == [module["version_iri"]]
        assert SEMVER_RE.match(str(module["version_iri"]))
        assert dict(graph.namespaces())[module["prefix"]] == URIRef(module["namespace"])


def test_construct_x_terms_do_not_include_repository_categories_or_old_segments() -> None:
    forbidden_segments = [
        "/ontology/core/",
        "/ontology/domain/",
        "/ontology/alignments/",
        "/ontology/value-semantics",
        "/1lieferschein/",
    ]

    for module in MODULES:
        graph = load_graph(module["path"])
        construct_terms = {
            str(node)
            for triple in graph
            for node in triple
            if isinstance(node, URIRef) and str(node).startswith(CONX_AUTHORITY)
        }

        assert construct_terms
        for segment in forbidden_segments:
            assert not any(segment in term for term in construct_terms)


def test_construct_x_class_and_property_local_names_follow_or_document_convention() -> None:
    for module in MODULES:
        graph = load_graph(module["path"])
        namespace = module["namespace"]

        classes = [uri for uri in graph.subjects(RDF.type, OWL.Class) if str(uri).startswith(namespace)]
        object_properties = [
            uri for uri in graph.subjects(RDF.type, OWL.ObjectProperty) if str(uri).startswith(namespace)
        ]
        data_properties = [
            uri for uri in graph.subjects(RDF.type, OWL.DatatypeProperty) if str(uri).startswith(namespace)
        ]

        bad_classes = {local_name(uri) for uri in classes if not CLASS_RE.match(local_name(uri))}
        bad_object_properties = {
            local_name(uri) for uri in object_properties if not OBJECT_PROPERTY_RE.match(local_name(uri))
        }
        bad_data_properties = {
            local_name(uri) for uri in data_properties if not DATA_PROPERTY_RE.match(local_name(uri))
        }

        assert classes
        assert object_properties
        assert bad_classes == set()
        assert bad_object_properties == module["known_object_property_deviations"]
        assert bad_data_properties == module["known_data_property_deviations"]


