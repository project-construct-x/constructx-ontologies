from pathlib import Path

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef, XSD
from rdflib.collection import Collection


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_FILE = ROOT / "modules/core/address/ontology/conx-addr.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/address")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")

EXPECTED_CLASSES = {
    CONX_ADDR.Address,
    CONX_ADDR.AddressAssignment,
    CONX_ADDR.AddressRole,
    CONX_ADDR.AdministrativeTerritory,
    CONX_ADDR.Country,
    CONX_ADDR.AdministrativeArea,
}

EXPECTED_OBJECT_PROPERTIES = {
    CONX_ADDR.hasAddressAssignment,
    CONX_ADDR.assignedAddress,
    CONX_ADDR.addressRole,
    CONX_ADDR.hasCountry,
    CONX_ADDR.hasAdministrativeArea,
    CONX_ADDR.broaderAdministrativeTerritory,
    CONX_ADDR.hasGeographicPosition,
}

EXPECTED_DATATYPE_PROPERTIES = {
    CONX_ADDR.streetName,
    CONX_ADDR.additionalStreetName,
    CONX_ADDR.houseNumber,
    CONX_ADDR.blockName,
    CONX_ADDR.buildingName,
    CONX_ADDR.buildingPart,
    CONX_ADDR.floor,
    CONX_ADDR.room,
    CONX_ADDR.internalDeliveryPoint,
    CONX_ADDR.postOfficeBoxNumber,
    CONX_ADDR.localityName,
    CONX_ADDR.citySubdivisionName,
    CONX_ADDR.postalCode,
    CONX_ADDR.plotIdentifier,
    CONX_ADDR.departmentName,
    CONX_ADDR.attentionOf,
    CONX_ADDR.careOf,
}

LANGUAGE_AWARE_PROPERTIES = {
    CONX_ADDR.streetName,
    CONX_ADDR.additionalStreetName,
    CONX_ADDR.blockName,
    CONX_ADDR.buildingName,
    CONX_ADDR.buildingPart,
    CONX_ADDR.floor,
    CONX_ADDR.room,
    CONX_ADDR.internalDeliveryPoint,
    CONX_ADDR.localityName,
    CONX_ADDR.citySubdivisionName,
    CONX_ADDR.departmentName,
}

STRING_ONLY_PROPERTIES = {
    CONX_ADDR.houseNumber,
    CONX_ADDR.postOfficeBoxNumber,
    CONX_ADDR.postalCode,
    CONX_ADDR.plotIdentifier,
    CONX_ADDR.attentionOf,
    CONX_ADDR.careOf,
}


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def construct_x_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_ADDR))
    }


def test_address_tbox_contains_exactly_the_approved_terms() -> None:
    graph = load_graph()

    assert construct_x_terms_of_type(graph, OWL.Class) == EXPECTED_CLASSES
    assert construct_x_terms_of_type(graph, OWL.ObjectProperty) == EXPECTED_OBJECT_PROPERTIES
    assert construct_x_terms_of_type(graph, OWL.DatatypeProperty) == EXPECTED_DATATYPE_PROPERTIES


def test_natural_language_designations_allow_tagged_and_untagged_strings() -> None:
    graph = load_graph()

    for property_iri in LANGUAGE_AWARE_PROPERTIES:
        ranges = list(graph.objects(property_iri, RDFS.range))
        assert len(ranges) == 1
        union_heads = list(graph.objects(ranges[0], OWL.unionOf))
        assert len(union_heads) == 1
        assert set(Collection(graph, union_heads[0])) == {XSD.string, RDF.langString}


def test_codes_identifiers_and_recipient_literals_remain_plain_strings() -> None:
    graph = load_graph()

    for property_iri in STRING_ONLY_PROPERTIES:
        assert list(graph.objects(property_iri, RDFS.range)) == [XSD.string]


def test_address_assignment_requires_one_address_and_one_or_more_roles() -> None:
    graph = load_graph()
    restrictions = set(graph.objects(CONX_ADDR.AddressAssignment, RDFS.subClassOf))

    address_restrictions = {
        node for node in restrictions if (node, OWL.onProperty, CONX_ADDR.assignedAddress) in graph
    }
    role_restrictions = {
        node for node in restrictions if (node, OWL.onProperty, CONX_ADDR.addressRole) in graph
    }

    assert any(
        (node, OWL.cardinality, Literal(1, datatype=XSD.nonNegativeInteger)) in graph
        for node in address_restrictions
    )
    assert any(
        (node, OWL.minCardinality, Literal(1, datatype=XSD.nonNegativeInteger)) in graph
        for node in role_restrictions
    )
    assert not any((node, OWL.maxCardinality, None) in graph for node in role_restrictions)
    assert not any((node, OWL.cardinality, None) in graph for node in role_restrictions)


def test_address_object_property_contracts_are_explicit() -> None:
    graph = load_graph()

    assert (CONX_ADDR.hasAddressAssignment, RDFS.range, CONX_ADDR.AddressAssignment) in graph
    assert not list(graph.objects(CONX_ADDR.hasAddressAssignment, RDFS.domain))
    assert (CONX_ADDR.assignedAddress, RDFS.domain, CONX_ADDR.AddressAssignment) in graph
    assert (CONX_ADDR.assignedAddress, RDFS.range, CONX_ADDR.Address) in graph
    assert (CONX_ADDR.addressRole, RDFS.domain, CONX_ADDR.AddressAssignment) in graph
    assert (CONX_ADDR.addressRole, RDFS.range, CONX_ADDR.AddressRole) in graph
    assert (CONX_ADDR.hasGeographicPosition, RDFS.domain, CONX_ADDR.Address) in graph
    assert not list(graph.objects(CONX_ADDR.hasGeographicPosition, RDFS.range))


def test_administrative_territory_hierarchy_is_modeled() -> None:
    graph = load_graph()

    assert (CONX_ADDR.Country, RDFS.subClassOf, CONX_ADDR.AdministrativeTerritory) in graph
    assert (CONX_ADDR.AdministrativeArea, RDFS.subClassOf, CONX_ADDR.AdministrativeTerritory) in graph
    assert (
        CONX_ADDR.broaderAdministrativeTerritory,
        RDFS.domain,
        CONX_ADDR.AdministrativeArea,
    ) in graph
    assert (
        CONX_ADDR.broaderAdministrativeTerritory,
        RDFS.range,
        CONX_ADDR.AdministrativeTerritory,
    ) in graph


def test_tbox_has_no_imports_reference_data_or_excluded_address_fields() -> None:
    graph = load_graph()

    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))
    assert not construct_x_terms_of_type(graph, OWL.NamedIndividual)

    excluded_terms = {
        CONX_ADDR.formattedAddress,
        CONX_ADDR.addressLabel,
        CONX_ADDR.addressLine,
        CONX_ADDR.latitude,
        CONX_ADDR.longitude,
    }
    assert not any(term in graph.all_nodes() for term in excluded_terms)
