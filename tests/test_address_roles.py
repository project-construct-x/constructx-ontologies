from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import DCTERMS, OWL, SKOS


ROOT = Path(__file__).resolve().parents[1]
VOCABULARY_DIR = ROOT / "datasets/reference/vocabularies/address-roles"
VOCABULARY_FILE = VOCABULARY_DIR / "address-roles.ttl"
METADATA_FILE = VOCABULARY_DIR / "dataset.yaml"
ONTOLOGY_FILE = ROOT / "modules/core/address/ontology/conx-addr.ttl"

CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
ROLES = Namespace("https://www.construct-x.org/vocab/address-role#")
SCHEMA = Namespace("https://schema.org/")
SCHEME = URIRef("https://www.construct-x.org/vocab/address-role")
UBL_SOURCE = URIRef(
    "https://docs.oasis-open.org/ubl/cs01-UBL-2.5/xsd/common/"
    "UBL-CommonAggregateComponents-2.5.xsd"
)

EXPECTED_ROLES = {
    ROLES.DeliveryAddressRole,
    ROLES.InvoiceAddressRole,
    ROLES.PostalAddressRole,
    ROLES.RegistrationAddressRole,
    ROLES.ReturnAddressRole,
    ROLES.ResidenceAddressRole,
    ROLES.ConstructionSiteAddressRole,
    ROLES.ConstructionSiteAccessRole,
    ROLES.LegalAddressRole,
    ROLES.HeadquartersAddressRole,
    ROLES.PhysicalLocationAddressRole,
}

UBL_ALIGNED_ROLES = {
    ROLES.DeliveryAddressRole,
    ROLES.PostalAddressRole,
    ROLES.RegistrationAddressRole,
    ROLES.ReturnAddressRole,
    ROLES.ResidenceAddressRole,
}
GAIA_X_ALIGNED_ROLES = {
    ROLES.LegalAddressRole,
    ROLES.HeadquartersAddressRole,
    ROLES.PhysicalLocationAddressRole,
}
GAIA_X_SOURCE = URIRef("https://docs.gaia-x.eu/ontology/development/classes/Address/")


def load_vocabulary() -> Graph:
    return Graph().parse(VOCABULARY_FILE, format="turtle")


def test_address_role_dataset_metadata_is_explicit() -> None:
    with METADATA_FILE.open(encoding="utf-8") as handle:
        metadata = yaml.safe_load(handle)

    assert metadata["id"] == "address-roles"
    assert metadata["type"] == "reference-vocabulary"
    assert metadata["status"] == "draft"
    assert metadata["version"] == "0.3.0"
    assert metadata["vocabulary_iri"] == str(SCHEME)
    assert metadata["version_iri"] == f"{SCHEME}/0.3.0"
    assert metadata["namespace"] == str(ROLES)
    assert metadata["dependencies"] == [
        {
            "id": "address",
            "version": "0.2.0",
            "ontology_iri": "https://www.construct-x.org/ontology/address",
            "version_iri": "https://www.construct-x.org/ontology/address/0.2.0",
        }
    ]


def test_vocabulary_contains_exactly_the_approved_address_roles() -> None:
    graph = load_vocabulary()
    roles = set(graph.subjects(RDF.type, CONX_ADDR.LocationRole))

    assert roles == EXPECTED_ROLES
    assert (SCHEME, RDF.type, SKOS.ConceptScheme) in graph
    assert (SCHEME, RDF.type, OWL.Ontology) in graph
    assert list(graph.objects(SCHEME, OWL.versionIRI)) == [
        URIRef(f"{SCHEME}/0.3.0")
    ]
    assert (SCHEME, SCHEMA.version, Literal("0.3.0")) in graph
    assert set(graph.objects(SCHEME, SKOS.hasTopConcept)) == EXPECTED_ROLES


def test_every_role_is_a_bilingual_skos_top_concept_with_a_unique_code() -> None:
    graph = load_vocabulary()
    notations = set()

    for role in EXPECTED_ROLES:
        assert (role, RDF.type, SKOS.Concept) in graph
        assert (role, SKOS.inScheme, SCHEME) in graph
        assert (role, SKOS.topConceptOf, SCHEME) in graph

        labels = list(graph.objects(role, SKOS.prefLabel))
        definitions = list(graph.objects(role, SKOS.definition))
        role_notations = list(graph.objects(role, SKOS.notation))

        assert len(labels) == 2
        assert {label.language for label in labels} == {"de", "en"}
        assert len(definitions) == 2
        assert {definition.language for definition in definitions} == {"de", "en"}
        assert len(role_notations) == 1
        assert role_notations[0] not in notations
        notations.add(role_notations[0])


def test_only_roles_with_direct_ubl_terms_claim_ubl_provenance() -> None:
    graph = load_vocabulary()

    for role in EXPECTED_ROLES:
        sources = set(graph.objects(role, DCTERMS.source))
        if role in UBL_ALIGNED_ROLES:
            assert sources == {UBL_SOURCE}
        elif role in GAIA_X_ALIGNED_ROLES:
            assert sources == {GAIA_X_SOURCE}
        else:
            assert not sources


def test_address_role_instances_remain_outside_the_tbox() -> None:
    ontology_graph = Graph().parse(ONTOLOGY_FILE, format="turtle")

    assert not set(ontology_graph.subjects(RDF.type, CONX_ADDR.LocationRole))
    assert not EXPECTED_ROLES.intersection(ontology_graph.all_nodes())

