from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, OWL, RDF, SKOS, URIRef


ROOT = Path(__file__).resolve().parents[1]
VOCABULARY_ROOT = ROOT / "datasets/reference/vocabularies"
CONX_CONTACT = Namespace("https://www.construct-x.org/ontology/contact#")
CONTACT_CHANNEL = Namespace("https://www.construct-x.org/vocab/contact-channel#")
CONTACT_USAGE = Namespace("https://www.construct-x.org/vocab/contact-usage#")
CONTACT_PURPOSE = Namespace("https://www.construct-x.org/vocab/contact-purpose#")
CONTACT_PLATFORM = Namespace("https://www.construct-x.org/vocab/contact-platform#")

VOCABULARIES = {
    "contact-channel": (
        URIRef("https://www.construct-x.org/vocab/contact-channel"),
        CONX_CONTACT.ContactChannel,
        {
            CONTACT_CHANNEL.email: Literal("email"),
            CONTACT_CHANNEL.phone: Literal("phone"),
            CONTACT_CHANNEL.mobilePhone: Literal("mobile-phone"),
            CONTACT_CHANNEL.fax: Literal("fax"),
            CONTACT_CHANNEL.website: Literal("website"),
            CONTACT_CHANNEL.messenger: Literal("messenger"),
            CONTACT_CHANNEL.socialProfile: Literal("social-profile"),
            CONTACT_CHANNEL.postalAddress: Literal("postal-address"),
        },
    ),
    "contact-usage": (
        URIRef("https://www.construct-x.org/vocab/contact-usage"),
        CONX_CONTACT.ContactUsage,
        {
            CONTACT_USAGE.private: Literal("private"),
            CONTACT_USAGE.business: Literal("business"),
            CONTACT_USAGE.official: Literal("official"),
        },
    ),
    "contact-purpose": (
        URIRef("https://www.construct-x.org/vocab/contact-purpose"),
        CONX_CONTACT.ContactPurpose,
        {
            CONTACT_PURPOSE.general: Literal("general"),
            CONTACT_PURPOSE.delivery: Literal("delivery"),
            CONTACT_PURPOSE.billing: Literal("billing"),
            CONTACT_PURPOSE.support: Literal("support"),
            CONTACT_PURPOSE.sales: Literal("sales"),
            CONTACT_PURPOSE.technical: Literal("technical"),
            CONTACT_PURPOSE.emergency: Literal("emergency"),
        },
    ),
    "contact-platform": (
        URIRef("https://www.construct-x.org/vocab/contact-platform"),
        CONX_CONTACT.ContactPlatform,
        {
            CONTACT_PLATFORM.linkedin: Literal("linkedin"),
            CONTACT_PLATFORM.instagram: Literal("instagram"),
            CONTACT_PLATFORM.x: Literal("x"),
            CONTACT_PLATFORM.facebook: Literal("facebook"),
            CONTACT_PLATFORM.github: Literal("github"),
            CONTACT_PLATFORM.whatsapp: Literal("whatsapp"),
            CONTACT_PLATFORM.signal: Literal("signal"),
            CONTACT_PLATFORM.microsoftTeams: Literal("microsoft-teams"),
        },
    ),
}


def load_vocabulary(vocabulary_id: str) -> tuple[dict, Graph]:
    directory = VOCABULARY_ROOT / vocabulary_id
    metadata = yaml.safe_load((directory / "dataset.yaml").read_text(encoding="utf-8"))
    graph = Graph().parse(directory / metadata["artifacts"]["data"], format="turtle")
    return metadata, graph


def test_contact_reference_vocabularies_contain_the_approved_values() -> None:
    for vocabulary_id, (scheme, contact_type, expected_notations) in VOCABULARIES.items():
        metadata, graph = load_vocabulary(vocabulary_id)

        assert metadata["type"] == "reference-vocabulary"
        assert metadata["status"] == "draft"
        assert metadata["version"] == "0.1.0"
        assert (scheme, RDF.type, OWL.Ontology) in graph
        assert (scheme, RDF.type, SKOS.ConceptScheme) in graph
        assert list(graph.objects(scheme, OWL.versionIRI)) == [
            URIRef(f"{scheme}/0.1.0")
        ]
        assert list(graph.objects(scheme, OWL.versionInfo)) == [Literal("0.1.0")]

        concepts = set(graph.subjects(RDF.type, SKOS.Concept))
        assert concepts == set(expected_notations)
        assert set(graph.objects(scheme, SKOS.hasTopConcept)) == concepts

        for concept, notation in expected_notations.items():
            assert (concept, RDF.type, contact_type) in graph
            assert (concept, SKOS.inScheme, scheme) in graph
            assert (concept, SKOS.topConceptOf, scheme) in graph
            assert list(graph.objects(concept, SKOS.notation)) == [notation]
            assert {
                label.language for label in graph.objects(concept, SKOS.prefLabel)
            } == {"de", "en"}
            assert {
                definition.language
                for definition in graph.objects(concept, SKOS.definition)
            } == {"de", "en"}


def test_contact_reference_vocabularies_do_not_import_external_ontologies() -> None:
    for vocabulary_id, (scheme, _, _) in VOCABULARIES.items():
        _, graph = load_vocabulary(vocabulary_id)
        assert not list(graph.objects(scheme, OWL.imports))
