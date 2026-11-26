from pathlib import Path

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef, XSD
from rdflib.collection import Collection


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_FILE = ROOT / "modules/core/address/ontology/conx-addr.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/address")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")

EXPECTED_CLASSES = {
    CONX_ADDR.Address,
    CONX_ADDR.LocationAssignment,
    CONX_ADDR.LocationRole,
    CONX_ADDR.AdministrativeTerritory,
    CONX_ADDR.Country,
    CONX_ADDR.AdministrativeArea,
}

EXPECTED_OBJECT_PROPERTIES = {
    CONX_ADDR.hasLocationAssignment,
    CONX_ADDR.hasAssignedAddress,
    CONX_ADDR.hasLocationRole,
    CONX_ADDR.hasCountry,
    CONX_ADDR.hasAdministrativeArea,
    CONX_ADDR.hasBroaderAdministrativeTerritory,
    CONX_ADDR.hasGeoReference,
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
}

STRING_ONLY_PROPERTIES = {
    CONX_ADDR.houseNumber,
    CONX_ADDR.postOfficeBoxNumber,
    CONX_ADDR.postalCode,
    CONX_ADDR.plotIdentifier,
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


def test_location_assignment_requires_address_or_geolocation_and_one_or_more_roles() -> None:
    graph = load_graph()
    restrictions = set(graph.objects(CONX_ADDR.LocationAssignment, RDFS.subClassOf))

    address_restrictions = {
        node for node in restrictions if (node, OWL.onProperty, CONX_ADDR.hasAssignedAddress) in graph
    }
    role_restrictions = {
        node for node in restrictions if (node, OWL.onProperty, CONX_ADDR.hasLocationRole) in graph
    }

    union, = (head for node in restrictions for head in graph.objects(node, OWL.unionOf))
    assert {(graph.value(r, OWL.onProperty), graph.value(r, OWL.someValuesFrom)) for r in Collection(graph, union)} == {
        (CONX_ADDR.hasAssignedAddress, CONX_ADDR.Address), (CONX_ADDR.hasGeoReference, OWL.Thing),
    }
    assert any(
        (node, OWL.maxCardinality, Literal(1, datatype=XSD.nonNegativeInteger)) in graph
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

    assert (CONX_ADDR.hasLocationAssignment, RDFS.range, CONX_ADDR.LocationAssignment) in graph
    assert not list(graph.objects(CONX_ADDR.hasLocationAssignment, RDFS.domain))
    assert (CONX_ADDR.hasAssignedAddress, RDFS.domain, CONX_ADDR.LocationAssignment) in graph
    assert (CONX_ADDR.hasAssignedAddress, RDFS.range, CONX_ADDR.Address) in graph
    assert (CONX_ADDR.hasLocationRole, RDFS.domain, CONX_ADDR.LocationAssignment) in graph
    assert (CONX_ADDR.hasLocationRole, RDFS.range, CONX_ADDR.LocationRole) in graph
    assert (CONX_ADDR.hasGeoReference, RDFS.domain, CONX_ADDR.LocationAssignment) in graph
    assert (CONX_ADDR.hasGeoReference, RDFS.range, None) not in graph
    assert CONX_ADDR.GeoLocation not in graph.all_nodes()


def test_administrative_territory_hierarchy_is_modeled() -> None:
    graph = load_graph()

    assert (CONX_ADDR.Country, RDFS.subClassOf, CONX_ADDR.AdministrativeTerritory) in graph
    assert (CONX_ADDR.AdministrativeArea, RDFS.subClassOf, CONX_ADDR.AdministrativeTerritory) in graph
    assert (
        CONX_ADDR.hasBroaderAdministrativeTerritory,
        RDFS.domain,
        CONX_ADDR.AdministrativeArea,
    ) in graph
    assert (
        CONX_ADDR.hasBroaderAdministrativeTerritory,
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
