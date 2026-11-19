from pathlib import Path

import yaml
from bs4 import BeautifulSoup
from rdflib import Graph, Literal, Namespace, RDF, RDFS, OWL

from scripts.generate_docs import (
    ontology_html_output_path,
    render_module_overview,
    render_profile_overview,
)


ROOT = Path(__file__).resolve().parents[1]
ADDRESS_MODULE_FILE = ROOT / "modules/core/address/module.yaml"
VSO_MODULE_FILE = ROOT / "modules/core/vso/module.yaml"
AGENT_MODULE_FILE = ROOT / "modules/core/agent/module.yaml"
PERSON_MODULE_FILE = ROOT / "modules/core/person/module.yaml"
CONTACT_MODULE_FILE = ROOT / "modules/core/contact/module.yaml"
ORGANIZATION_MODULE_FILE = ROOT / "modules/core/organization/module.yaml"
PARTICIPATION_MODULE_FILE = ROOT / "modules/core/participation/module.yaml"
DOCUMENT_MODULE_FILE = ROOT / "modules/core/document/module.yaml"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_ontology_html_output_paths_are_inside_module_docs() -> None:
    address_metadata = load_yaml(ADDRESS_MODULE_FILE)
    vso_metadata = load_yaml(VSO_MODULE_FILE)
    agent_metadata = load_yaml(AGENT_MODULE_FILE)
    person_metadata = load_yaml(PERSON_MODULE_FILE)
    contact_metadata = load_yaml(CONTACT_MODULE_FILE)
    organization_metadata = load_yaml(ORGANIZATION_MODULE_FILE)
    participation_metadata = load_yaml(PARTICIPATION_MODULE_FILE)
    document_metadata = load_yaml(DOCUMENT_MODULE_FILE)

    assert ontology_html_output_path(ADDRESS_MODULE_FILE, address_metadata) == (
        ROOT / "modules/core/address/docs/address.html"
    )
    assert ontology_html_output_path(VSO_MODULE_FILE, vso_metadata) == (
        ROOT / "modules/core/vso/docs/vso.html"
    )
    assert ontology_html_output_path(AGENT_MODULE_FILE, agent_metadata) == (
        ROOT / "modules/core/agent/docs/agent.html"
    )
    assert ontology_html_output_path(PERSON_MODULE_FILE, person_metadata) == (
        ROOT / "modules/core/person/docs/person.html"
    )
    assert ontology_html_output_path(CONTACT_MODULE_FILE, contact_metadata) == (
        ROOT / "modules/core/contact/docs/contact.html"
    )
    assert ontology_html_output_path(
        ORGANIZATION_MODULE_FILE, organization_metadata
    ) == (ROOT / "modules/core/organization/docs/organization.html")
    assert ontology_html_output_path(
        PARTICIPATION_MODULE_FILE, participation_metadata
    ) == (ROOT / "modules/core/participation/docs/participation.html")
    assert ontology_html_output_path(DOCUMENT_MODULE_FILE, document_metadata) == (
        ROOT / "modules/core/document/docs/document.html"
    )


def test_module_overview_points_to_module_local_html_docs() -> None:
    overview = render_module_overview(ROOT)

    assert "modules/core/address/docs/address.html" in overview
    assert "modules/core/vso/docs/vso.html" in overview
    assert "modules/core/agent/docs/agent.html" in overview
    assert "modules/core/person/docs/person.html" in overview
    assert "modules/core/contact/docs/contact.html" in overview
    assert "modules/core/organization/docs/organization.html" in overview
    assert "modules/core/participation/docs/participation.html" in overview
    assert "modules/core/document/docs/document.html" in overview
    assert "dist/docs" not in overview


def test_profile_overview_registers_the_vso_isoprops_profile() -> None:
    overview = render_profile_overview(ROOT)

    assert "vso-isoprops" in overview
    assert "https://www.construct-x.org/shapes/vso/isoprops" in overview
    assert (
        "profiles/construct-x/vso-isoprops/shapes/"
        "conx-vso-isoprops.shacl.ttl"
    ) in overview
    assert "profiles/construct-x/vso-isoprops/docs/00_index.md" in overview


def test_generated_organization_html_contains_the_implemented_terms() -> None:
    html_path = ROOT / "modules/core/organization/docs/organization.html"
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    text = soup.get_text(" ", strip=True)

    assert soup.title is not None
    assert "Construct-X Organization Ontology" in soup.title.get_text()
    for term in (
        "Organization",
        "LegalEntity",
        "OrganizationalUnit",
        "Membership",
        "LegalRepresentation",
        "registrationDate",
    ):
        assert term in text


def test_generated_participation_html_contains_the_implemented_terms() -> None:
    html_path = ROOT / "modules/core/participation/docs/participation.html"
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    text = soup.get_text(" ", strip=True)

    assert soup.title is not None
    assert "Construct-X Participation Ontology" in soup.title.get_text()
    for term in (
        "Participation",
        "Role",
        "participant",
        "role",
        "context",
        "startDate",
        "endDate",
    ):
        assert term in text


def test_generated_document_html_contains_the_implemented_terms() -> None:
    html_path = ROOT / "modules/core/document/docs/document.html"
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    text = soup.get_text(" ", strip=True)

    assert soup.title is not None
    assert "Construct-X Document Ontology" in soup.title.get_text()
    for term in (
        "Document",
        "DocumentReference",
        "DocumentDistribution",
        "DocumentType",
        "DocumentStatus",
        "validFrom",
        "validUntil",
    ):
        assert term in text




