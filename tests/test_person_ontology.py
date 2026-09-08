from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD
from rdflib.collection import Collection


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/person"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-person.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/person")
CONX_PERSON = Namespace("https://www.construct-x.org/ontology/person#")
CONX_AGENT = Namespace("https://www.construct-x.org/ontology/agent#")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
SEMIC_PERSON = URIRef("http://www.w3.org/ns/person#Person")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

EXPECTED_CLASSES = {CONX_PERSON.Person}
EXPECTED_DATATYPE_PROPERTIES = {
    CONX_PERSON.fullName,
    CONX_PERSON.givenName,
    CONX_PERSON.familyName,
    CONX_PERSON.additionalName,
    CONX_PERSON.birthName,
    CONX_PERSON.birthDate,
    CONX_PERSON.birthPlaceName,
}
EXPECTED_OBJECT_PROPERTIES = {
    CONX_PERSON.sex,
    CONX_PERSON.gender,
    CONX_PERSON.citizenship,
    CONX_PERSON.hasIdentityEvidence,
}
LANGUAGE_AWARE_PROPERTIES = EXPECTED_DATATYPE_PROPERTIES - {CONX_PERSON.birthDate}


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_PERSON))
    }


def test_person_tbox_contains_exactly_the_approved_terms() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == EXPECTED_CLASSES
    assert local_terms_of_type(graph, OWL.DatatypeProperty) == EXPECTED_DATATYPE_PROPERTIES
    assert local_terms_of_type(graph, OWL.ObjectProperty) == EXPECTED_OBJECT_PROPERTIES
    assert not local_terms_of_type(graph, OWL.NamedIndividual)


def test_person_is_a_specialized_agent_and_natural_person() -> None:
    graph = load_graph()

    assert (CONX_PERSON.Person, RDFS.subClassOf, CONX_AGENT.Agent) in graph
    assert (CONX_PERSON.Person, RDFS.subClassOf, FOAF.Person) in graph
    assert (CONX_PERSON.Person, RDFS.subClassOf, SEMIC_PERSON) in graph


def test_person_literal_properties_have_the_approved_ranges() -> None:
    graph = load_graph()

    for property_iri in EXPECTED_DATATYPE_PROPERTIES:
        assert (property_iri, RDFS.domain, CONX_PERSON.Person) in graph

    assert list(graph.objects(CONX_PERSON.birthDate, RDFS.range)) == [XSD.date]

    for property_iri in LANGUAGE_AWARE_PROPERTIES:
        ranges = list(graph.objects(property_iri, RDFS.range))
        assert len(ranges) == 1
        union_heads = list(graph.objects(ranges[0], OWL.unionOf))
        assert len(union_heads) == 1
        assert set(Collection(graph, union_heads[0])) == {XSD.string, RDF.langString}


def test_person_object_property_contracts_are_explicit_but_open() -> None:
    graph = load_graph()

    for property_iri in EXPECTED_OBJECT_PROPERTIES:
        assert (property_iri, RDFS.domain, CONX_PERSON.Person) in graph

    assert (CONX_PERSON.sex, RDFS.range, SKOS.Concept) in graph
    assert (CONX_PERSON.gender, RDFS.range, SKOS.Concept) in graph
    assert (CONX_PERSON.citizenship, RDFS.range, CONX_ADDR.Country) in graph
    assert not list(graph.objects(CONX_PERSON.hasIdentityEvidence, RDFS.range))


def test_person_tbox_keeps_validation_and_other_modules_outside_owl() -> None:
    graph = load_graph()

    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))
    assert not set(graph.subjects(RDF.type, OWL.Restriction))

    excluded_terms = {
        CONX_PERSON.Agent,
        CONX_PERSON.ContactPoint,
        CONX_PERSON.hasContactAssignment,
        CONX_PERSON.Organization,
        CONX_PERSON.isMemberOf,
        CONX_PERSON.hasMember,
    }
    assert not any(term in graph.all_nodes() for term in excluded_terms)


def test_person_module_metadata_records_referenced_dependencies() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "person"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.1.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.1.0"
    assert metadata["namespace"] == str(CONX_PERSON)
    assert metadata["artifacts"]["ontology"] == "ontology/conx-person.ttl"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-person-core.shacl.ttl"
    assert metadata["artifacts"]["strict_shapes"] is None
    assert metadata["shape_sets"]["core"]["graph_iri"] == (
        "https://www.construct-x.org/shapes/person/core"
    )

    dependencies = {dependency["id"]: dependency for dependency in metadata["dependencies"]}
    assert {"identifier", "agent", "address", "human-sex", "gender", "foaf", "adms", "skos"} <= set(
        dependencies
    )
    assert all(
        dependency["relation"] == "referenced-not-imported"
        for dependency_id, dependency in dependencies.items()
        if dependency_id != "identifier"
    )
    assert dependencies["identifier"]["relation"] == "shape-imported"
