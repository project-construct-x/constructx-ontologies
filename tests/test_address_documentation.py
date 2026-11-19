from pathlib import Path
from urllib.parse import unquote, urlsplit

from documentation_checks import module_artifacts, rendered_document

from rdflib import Graph, Namespace, OWL, RDF, URIRef


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules/core/address"
ARTIFACTS = module_artifacts(MODULE_DIR)
TERM_CATALOG = MODULE_DIR / ARTIFACTS["term_catalog"]
ROLE_DOCUMENTATION = MODULE_DIR / ARTIFACTS["address_roles_documentation"]
INDEX_DOCUMENTATION = MODULE_DIR / ARTIFACTS["documentation"]
ONTOLOGY_FILE = MODULE_DIR / "ontology/conx-addr.ttl"
ROLES_FILE = ROOT / "datasets/reference/vocabularies/address-roles/address-roles.ttl"

CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")


def local_name(term: URIRef, namespace: Namespace) -> str:
    return str(term).removeprefix(str(namespace))


def test_term_catalog_documents_every_address_tbox_term() -> None:
    documentation = TERM_CATALOG.read_text(encoding="utf-8")
    ontology = Graph().parse(ONTOLOGY_FILE, format="turtle")

    for rdf_type in (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty):
        terms = {
            term
            for term in ontology.subjects(RDF.type, rdf_type)
            if isinstance(term, URIRef) and str(term).startswith(str(CONX_ADDR))
        }
        assert terms
        for term in terms:
            assert f"`{local_name(term, CONX_ADDR)}`" in documentation


def test_address_role_documentation_covers_every_controlled_role() -> None:
    documentation = ROLE_DOCUMENTATION.read_text(encoding="utf-8")
    roles = Graph().parse(ROLES_FILE, format="turtle")
    role_namespace = Namespace("https://www.construct-x.org/vocab/address-role#")

    role_resources = set(roles.subjects(RDF.type, CONX_ADDR.LocationRole))
    assert len(role_resources) == 11
    for role in role_resources:
        assert f"`roles:{local_name(role, role_namespace)}`" in documentation


def test_address_index_links_supplementary_documents() -> None:
    linked = {
        (INDEX_DOCUMENTATION.parent / unquote(urlsplit(link["href"]).path)).resolve()
        for link in rendered_document(INDEX_DOCUMENTATION).select("a[href]")
    }
    for key in ("address_roles_documentation", "administrative_territories"):
        assert (MODULE_DIR / ARTIFACTS[key]).resolve() in linked
