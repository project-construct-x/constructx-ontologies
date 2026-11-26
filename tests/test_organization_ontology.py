from pathlib import Path

import yaml
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD
from rdflib.collection import Collection


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules/core/organization"
ONTOLOGY_FILE = MODULE_ROOT / "ontology/conx-org.ttl"
ONTOLOGY_IRI = URIRef("https://www.construct-x.org/ontology/organization")
CONX_ORG = Namespace("https://www.construct-x.org/ontology/organization#")
CONX_AGENT = Namespace("https://www.construct-x.org/ontology/agent#")
CONX_PERSON = Namespace("https://www.construct-x.org/ontology/person#")
ORG = Namespace("http://www.w3.org/ns/org#")
SCHEMA = Namespace("https://schema.org/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

EXPECTED_CLASSES = {
    CONX_ORG.Organization,
    CONX_ORG.LegalEntity,
    CONX_ORG.OrganizationalUnit,
    CONX_ORG.Membership,
    CONX_ORG.LegalRepresentation,
}
EXPECTED_DATATYPE_PROPERTIES = {
    CONX_ORG.name,
    CONX_ORG.legalName,
    CONX_ORG.alternativeName,
    CONX_ORG.registrationDate,
}
EXPECTED_OBJECT_PROPERTIES = {
    CONX_ORG.legalForm,
    CONX_ORG.activity,
    CONX_ORG.subOrganizationOf,
    CONX_ORG.hasSubOrganization,
    CONX_ORG.unitOf,
    CONX_ORG.hasUnit,
    CONX_ORG.member,
    CONX_ORG.membershipOrganization,
    CONX_ORG.representedOrganization,
    CONX_ORG.representative,
}


def load_graph() -> Graph:
    return Graph().parse(ONTOLOGY_FILE, format="turtle")


def local_terms_of_type(graph: Graph, rdf_type: URIRef) -> set[URIRef]:
    return {
        term
        for term in graph.subjects(RDF.type, rdf_type)
        if isinstance(term, URIRef) and str(term).startswith(str(CONX_ORG))
    }


def test_organization_tbox_contains_exactly_the_approved_terms() -> None:
    graph = load_graph()

    assert local_terms_of_type(graph, OWL.Class) == EXPECTED_CLASSES
    assert local_terms_of_type(graph, OWL.DatatypeProperty) == (
        EXPECTED_DATATYPE_PROPERTIES
    )
    assert local_terms_of_type(graph, OWL.ObjectProperty) == EXPECTED_OBJECT_PROPERTIES
    assert not local_terms_of_type(graph, OWL.NamedIndividual)


def test_organization_class_hierarchy_matches_the_approved_model() -> None:
    graph = load_graph()

    assert (CONX_ORG.Organization, RDFS.subClassOf, CONX_AGENT.Agent) in graph
    assert (CONX_ORG.Organization, RDFS.subClassOf, ORG.Organization) in graph
    assert (CONX_ORG.LegalEntity, RDFS.subClassOf, CONX_ORG.Organization) in graph
    assert (
        CONX_ORG.OrganizationalUnit,
        RDFS.subClassOf,
        CONX_ORG.Organization,
    ) in graph
    assert (
        CONX_ORG.OrganizationalUnit,
        RDFS.subClassOf,
        ORG.OrganizationalUnit,
    ) in graph
    assert (CONX_ORG.Membership, RDFS.subClassOf, ORG.Membership) in graph
    assert (CONX_ORG.LegalEntity, RDFS.subClassOf, ORG.FormalOrganization) not in graph


def test_organization_literal_properties_have_approved_domains_and_ranges() -> None:
    graph = load_graph()

    for property_iri in (
        CONX_ORG.name,
        CONX_ORG.alternativeName,
    ):
        assert (property_iri, RDFS.domain, CONX_ORG.Organization) in graph

    assert (CONX_ORG.legalName, RDFS.domain, CONX_ORG.LegalEntity) in graph
    assert (CONX_ORG.registrationDate, RDFS.domain, CONX_ORG.LegalEntity) in graph
    assert list(graph.objects(CONX_ORG.registrationDate, RDFS.range)) == [XSD.date]

    for property_iri in (
        CONX_ORG.name,
        CONX_ORG.legalName,
        CONX_ORG.alternativeName,
    ):
        ranges = list(graph.objects(property_iri, RDFS.range))
        assert len(ranges) == 1
        union_heads = list(graph.objects(ranges[0], OWL.unionOf))
        assert len(union_heads) == 1
        assert set(Collection(graph, union_heads[0])) == {XSD.string, RDF.langString}

    assert (CONX_ORG.name, RDFS.subPropertyOf, SCHEMA.name) in graph
    assert (CONX_ORG.legalName, RDFS.subPropertyOf, SCHEMA.legalName) in graph
    assert (
        CONX_ORG.alternativeName,
        RDFS.subPropertyOf,
        SCHEMA.alternateName,
    ) in graph


def test_organization_object_property_contracts_and_inverses_are_explicit() -> None:
    graph = load_graph()

    expected_contracts = {
        CONX_ORG.legalForm: (CONX_ORG.LegalEntity, SKOS.Concept),
        CONX_ORG.activity: (CONX_ORG.Organization, SKOS.Concept),
        CONX_ORG.subOrganizationOf: (
            CONX_ORG.Organization,
            CONX_ORG.Organization,
        ),
        CONX_ORG.hasSubOrganization: (
            CONX_ORG.Organization,
            CONX_ORG.Organization,
        ),
        CONX_ORG.unitOf: (CONX_ORG.OrganizationalUnit, CONX_ORG.Organization),
        CONX_ORG.hasUnit: (CONX_ORG.Organization, CONX_ORG.OrganizationalUnit),
        CONX_ORG.member: (CONX_ORG.Membership, CONX_AGENT.Agent),
        CONX_ORG.membershipOrganization: (
            CONX_ORG.Membership,
            CONX_ORG.Organization,
        ),
        CONX_ORG.representedOrganization: (
            CONX_ORG.LegalRepresentation,
            CONX_ORG.LegalEntity,
        ),
        CONX_ORG.representative: (
            CONX_ORG.LegalRepresentation,
            CONX_PERSON.Person,
        ),
    }

    for property_iri, (domain, range_) in expected_contracts.items():
        assert (property_iri, RDFS.domain, domain) in graph
        assert (property_iri, RDFS.range, range_) in graph

    assert (
        CONX_ORG.subOrganizationOf,
        OWL.inverseOf,
        CONX_ORG.hasSubOrganization,
    ) in graph
    assert (CONX_ORG.unitOf, OWL.inverseOf, CONX_ORG.hasUnit) in graph


def test_organization_tbox_keeps_validation_and_deferred_terms_outside_owl() -> None:
    graph = load_graph()

    assert not list(graph.objects(ONTOLOGY_IRI, OWL.imports))
    assert not set(graph.subjects(RDF.type, OWL.Restriction))

    deferred_terms = {
        CONX_ORG.EconomicActor,
        CONX_ORG.Enterprise,
        CONX_ORG.EconomicOperator,
        CONX_ORG.FormalOrganization,
        CONX_ORG.Post,
        CONX_ORG.Credential,
        CONX_ORG.homepage,
        CONX_ORG.hasMember,
        CONX_ORG.memberOf,
        CONX_ORG.foundingDate,
        CONX_ORG.activityStartDate,
    }
    assert not any(term in graph.all_nodes() for term in deferred_terms)


def test_organization_module_metadata_matches_the_implementation() -> None:
    metadata = yaml.safe_load((MODULE_ROOT / "module.yaml").read_text(encoding="utf-8"))

    assert metadata["id"] == "organization"
    assert metadata["type"] == "core"
    assert metadata["version"] == "0.1.0"
    assert metadata["ontology_iri"] == str(ONTOLOGY_IRI)
    assert metadata["version_iri"] == f"{ONTOLOGY_IRI}/0.1.0"
    assert metadata["namespace"] == str(CONX_ORG)
    assert metadata["artifacts"]["ontology"] == "ontology/conx-org.ttl"
    assert metadata["artifacts"]["core_shapes"] == "shapes/conx-org-core.shacl.ttl"
    assert metadata["artifacts"]["strict_shapes"] is None
    assert metadata["shape_sets"]["core"] == {
        "graph_iri": "https://www.construct-x.org/shapes/organization/core",
        "version_iri": "https://www.construct-x.org/shapes/organization/core/0.3.0",
        "namespace": "https://www.construct-x.org/shapes/organization/core#",
        "version": "0.3.0",
        "artifact": "shapes/conx-org-core.shacl.ttl",
    }

    dependencies = {dependency["id"]: dependency for dependency in metadata["dependencies"]}
    assert {
        "agent",
        "identifier",
        "person",
        "address",
        "contact",
        "address-roles",
        "adms",
        "skos",
        "org",
        "schema-org",
    } <= set(dependencies)
    assert all(
        dependency["relation"] == "referenced-not-imported"
        for dependency_id, dependency in dependencies.items()
        if dependency_id != "identifier"
    )
    assert dependencies["identifier"]["relation"] == "shape-imported"


def test_organization_external_dependencies_are_registered_in_network_lock() -> None:
    lock = yaml.safe_load(
        (ROOT / "network/imports.lock.yaml").read_text(encoding="utf-8")
    )
    dependencies = lock["dependencies"]
    module_path = "modules/core/organization"

    for dependency_id in ("adms", "schema_org", "skos", "org"):
        assert module_path in dependencies[dependency_id]["used_by"]

    assert {
        "org:Organization",
        "org:OrganizationalUnit",
        "org:Membership",
        "org:subOrganizationOf",
        "org:hasSubOrganization",
        "org:unitOf",
        "org:hasUnit",
        "org:member",
        "org:organization",
    } <= set(dependencies["org"]["used_terms"])
