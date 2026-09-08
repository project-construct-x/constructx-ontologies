from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/agent"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-agent.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/agent")
CONX_AGENT = Namespace("https://www.construct-x.org/ontology/agent#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
SEMIC_AGENT = URIRef("http://data.europa.eu/m8g/Agent")


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_AGENT))
    }


def test_agent_tbox_is_deliberately_minimal() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == {CONX_AGENT.Agent}
    assert not local_terms_of_type(graph, OWL.ObjectProperty)
    assert not local_terms_of_type(graph, OWL.DatatypeProperty)
    assert not local_terms_of_type(graph, OWL.NamedIndividual)
    assert (CONX_AGENT.Agent, RDFS.subClassOf, FOAF.Agent) in graph
    assert (CONX_AGENT.Agent, RDFS.seeAlso, SEMIC_AGENT) in graph
    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))


def test_agent_module_metadata_matches_the_tbox() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "agent"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.1.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.1.0"
    assert metadata["namespace"] == str(CONX_AGENT)
    assert metadata["artifacts"]["ontology"] == "ontology/conx-agent.ttl"
    assert metadata["artifacts"]["core_shapes"] is None
    assert metadata["artifacts"]["strict_shapes"] is None

