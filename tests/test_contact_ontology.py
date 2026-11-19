from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD
from rdflib.collection import Collection


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/contact"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-contact.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/contact")
CONX_CONTACT = Namespace("https://www.construct-x.org/ontology/contact#")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

EXPECTED_CLASSES = {
    CONX_CONTACT.ContactPoint,
    CONX_CONTACT.ContactMethod,
    CONX_CONTACT.ContactChannel,
    CONX_CONTACT.ContactUsage,
    CONX_CONTACT.ContactPurpose,
    CONX_CONTACT.ContactPlatform,
}
EXPECTED_OBJECT_PROPERTIES = {
    CONX_CONTACT.hasContactPoint,
    CONX_CONTACT.isContactPointFor,
    CONX_CONTACT.hasContactMethod,
    CONX_CONTACT.contactChannel,
    CONX_CONTACT.contactUsage,
    CONX_CONTACT.contactPurpose,
    CONX_CONTACT.contactPlatform,
    CONX_CONTACT.contactURI,
    CONX_CONTACT.usesLocationAssignment,
}
EXPECTED_DATATYPE_PROPERTIES = {
    CONX_CONTACT.contactValue,
    CONX_CONTACT.contactName,
    CONX_CONTACT.departmentName,
    CONX_CONTACT.functionTitle,
    CONX_CONTACT.availableLanguage,
    CONX_CONTACT.availabilityNote,
}
LANGUAGE_AWARE_PROPERTIES = {
    CONX_CONTACT.contactName,
    CONX_CONTACT.departmentName,
    CONX_CONTACT.functionTitle,
    CONX_CONTACT.availabilityNote,
}


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_CONTACT))
    }


def test_contact_tbox_contains_the_approved_terms() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == EXPECTED_CLASSES
    assert local_terms_of_type(graph, OWL.ObjectProperty) == EXPECTED_OBJECT_PROPERTIES
    assert local_terms_of_type(graph, OWL.DatatypeProperty) == (
        EXPECTED_DATATYPE_PROPERTIES
    )
    assert not local_terms_of_type(graph, OWL.NamedIndividual)
    assert CONX_CONTACT.ContactAssignment not in graph.all_nodes()


def test_contact_controlled_value_classes_are_skos_concepts() -> None:
    graph = load_graph()

    for class_iri in (
        CONX_CONTACT.ContactChannel,
        CONX_CONTACT.ContactUsage,
        CONX_CONTACT.ContactPurpose,
        CONX_CONTACT.ContactPlatform,
    ):
        assert (class_iri, RDFS.subClassOf, SKOS.Concept) in graph


def test_has_contact_point_keeps_domain_open_but_sets_range_and_inverse() -> None:
    graph = load_graph()

    assert not list(graph.objects(CONX_CONTACT.hasContactPoint, RDFS.domain))
    assert (CONX_CONTACT.hasContactPoint, RDFS.range, CONX_CONTACT.ContactPoint) in graph
    assert (
        CONX_CONTACT.hasContactPoint,
        OWL.inverseOf,
        CONX_CONTACT.isContactPointFor,
    ) in graph


def test_contact_object_property_contracts_are_explicit() -> None:
    graph = load_graph()

    assert (CONX_CONTACT.hasContactMethod, RDFS.domain, CONX_CONTACT.ContactPoint) in graph
    assert (CONX_CONTACT.hasContactMethod, RDFS.range, CONX_CONTACT.ContactMethod) in graph
    assert (CONX_CONTACT.contactChannel, RDFS.range, CONX_CONTACT.ContactChannel) in graph
    assert (CONX_CONTACT.contactUsage, RDFS.range, CONX_CONTACT.ContactUsage) in graph
    assert (CONX_CONTACT.contactPurpose, RDFS.range, CONX_CONTACT.ContactPurpose) in graph
    assert (CONX_CONTACT.contactPlatform, RDFS.range, CONX_CONTACT.ContactPlatform) in graph
    assert (
        CONX_CONTACT.usesLocationAssignment,
        RDFS.range,
        CONX_ADDR.LocationAssignment,
    ) in graph
    assert (CONX_CONTACT.contactURI, RDF.type, OWL.ObjectProperty) in graph


def test_contact_literal_properties_have_the_approved_ranges() -> None:
    graph = load_graph()

    assert list(graph.objects(CONX_CONTACT.contactValue, RDFS.range)) == [XSD.string]
    assert list(graph.objects(CONX_CONTACT.availableLanguage, RDFS.range)) == [
        XSD.string
    ]

    for property_iri in LANGUAGE_AWARE_PROPERTIES:
        ranges = list(graph.objects(property_iri, RDFS.range))
        assert len(ranges) == 1
        union_heads = list(graph.objects(ranges[0], OWL.unionOf))
        assert len(union_heads) == 1
        assert set(Collection(graph, union_heads[0])) == {XSD.string, RDF.langString}


def test_contact_module_metadata_registers_core_shapes_and_dependencies() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "contact"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.2.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.2.0"
    assert metadata["namespace"] == str(CONX_CONTACT)
    assert metadata["artifacts"]["ontology"] == "ontology/conx-contact.ttl"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-contact-core.shacl.ttl"
    assert metadata["artifacts"]["strict_shapes"] is None
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/contact/core",
        "version_iri": "https://www.construct-x.org/shapes/contact/core/0.2.0",
        "namespace": "https://www.construct-x.org/shapes/contact/core#",
        "version": "0.2.0",
        "artifact": "shapes/conx-contact-core.shacl.ttl",
    }

    dependencies = {dependency["id"]: dependency for dependency in metadata["dependencies"]}
    assert {
        "address",
        "contact-channel",
        "contact-usage",
        "contact-purpose",
        "contact-platform",
        "skos",
    } <= set(dependencies)
    assert all(
        dependency["relation"] == "referenced-not-imported"
        for dependency in dependencies.values()
    )
