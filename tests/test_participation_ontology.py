from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/participation"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-part.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/participation")
CONX_PART = Namespace("https://www.construct-x.org/ontology/participation#")
CONX_AGENT = Namespace("https://www.construct-x.org/ontology/agent#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_PART))
    }


def test_participation_tbox_contains_exactly_the_approved_terms() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == {
        CONX_PART.Participation,
        CONX_PART.Role,
    }
    assert local_terms_of_type(graph, OWL.ObjectProperty) == {
        CONX_PART.participant,
        CONX_PART.role,
        CONX_PART.context,
        CONX_PART.hasParticipation,
    }
    assert local_terms_of_type(graph, OWL.DatatypeProperty) == {
        CONX_PART.startDate,
        CONX_PART.endDate,
    }
    assert not local_terms_of_type(graph, OWL.NamedIndividual)


def test_participation_class_and_property_contracts_match_the_model() -> None:
    graph = load_graph()

    assert (CONX_PART.Role, RDFS.subClassOf, SKOS.Concept) in graph
    assert (CONX_PART.Participant, RDF.type, OWL.Class) not in graph
    assert (CONX_PART.Context, RDF.type, OWL.Class) not in graph

    assert (CONX_PART.participant, RDFS.domain, CONX_PART.Participation) in graph
    assert (CONX_PART.participant, RDFS.range, CONX_AGENT.Agent) in graph
    assert (CONX_PART.role, RDFS.domain, CONX_PART.Participation) in graph
    assert (CONX_PART.role, RDFS.range, CONX_PART.Role) in graph
    assert (CONX_PART.context, RDFS.domain, CONX_PART.Participation) in graph
    assert not list(graph.objects(CONX_PART.context, RDFS.range))

    for property_iri in (CONX_PART.startDate, CONX_PART.endDate):
        assert (property_iri, RDFS.domain, CONX_PART.Participation) in graph
        assert list(graph.objects(property_iri, RDFS.range)) == [XSD.date]


def test_participation_tbox_keeps_validation_and_deferred_terms_outside_owl() -> None:
    graph = load_graph()

    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))
    assert not set(graph.subjects(RDF.type, OWL.Restriction))
    assert set(graph.triples((None, OWL.inverseOf, None))) == {
        (CONX_PART.hasParticipation, OWL.inverseOf, CONX_PART.context)
    }
    assert (CONX_PART.hasParticipation, RDFS.range, CONX_PART.Participation) in graph
    assert not list(graph.objects(CONX_PART.hasParticipation, RDFS.domain))

    deferred_terms = {
        CONX_PART.AgentRoleAssignment,
        CONX_PART.AgentInRole,
        CONX_PART.Context,
        CONX_PART.ParticipationStatus,
        CONX_PART.ParticipationEvidence,
        CONX_PART.isParticipationOf,
    }
    assert not any(term in graph.all_nodes() for term in deferred_terms)


def test_participation_module_metadata_matches_the_implementation() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "participation"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.2.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.2.0"
    assert metadata["namespace"] == str(CONX_PART)
    assert metadata["preferred_namespace_prefix"] == "conx-part"
    assert metadata["artifacts"]["ontology"] == "ontology/conx-part.ttl"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-part-core.shacl.ttl"
    assert metadata["artifacts"]["strict_shapes"] is None
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/participation/core",
        "version_iri": "https://www.construct-x.org/shapes/participation/core/0.2.0",
        "namespace": "https://www.construct-x.org/shapes/participation/core#",
        "version": "0.2.0",
        "artifact": "shapes/conx-part-core.shacl.ttl",
    }

    dependencies = {dependency["id"]: dependency for dependency in metadata["dependencies"]}
    assert set(dependencies) == {"agent", "participation-role", "skos"}
    assert all(
        dependency["relation"] == "referenced-not-imported"
        for dependency in dependencies.values()
    )


def test_participation_skos_dependency_is_registered_in_network_lock() -> None:
    lock = yaml.safe_load(
        (ROOT / "network/imports.lock.yaml").read_text(encoding="utf-8")
    )
    skos_dependency = lock["dependencies"]["skos"]

    assert "modules/core/participation" in skos_dependency["used_by"]
    assert (
        "datasets/reference/vocabularies/participation-role"
        in skos_dependency["used_by"]
    )
    assert "skos:Concept" in skos_dependency["used_terms"]
