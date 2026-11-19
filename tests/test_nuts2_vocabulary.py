from pathlib import Path

import yaml
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import OWL, SKOS


ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "datasets/reference/administrative-territories/nuts-2"
DATA_FILE = DATASET_DIR / "data/nuts-2-regions.ttl"
METADATA_FILE = DATASET_DIR / "dataset.yaml"

ADMS = Namespace("http://www.w3.org/ns/adms#")
CONX_ADDR = Namespace("https://www.construct-x.org/ontology/address#")
COUNTRIES = Namespace("https://www.construct-x.org/vocab/country#")
ID_SCHEME = Namespace("https://www.construct-x.org/vocab/identifier-scheme#")
NUTS = Namespace("https://www.construct-x.org/vocab/administrative-area/nuts-2#")
SCHEME = URIRef("https://www.construct-x.org/vocab/administrative-area/nuts-2")


def test_nuts2_dataset_is_versioned_and_pins_gaia_x_source() -> None:
    metadata = yaml.safe_load(METADATA_FILE.read_text(encoding="utf-8"))

    assert metadata["version"] == "0.1.0"
    assert metadata["version_iri"] == f"{SCHEME}/0.1.0"
    assert metadata["source"]["extraction_release"] == "v2.3.0"
    assert metadata["source"]["extraction_commit"] == (
        "57131b2cec747de8a08a4115bea198369778aef6"
    )


def test_nuts2_vocabulary_contains_the_complete_gaia_x_release_set() -> None:
    graph = Graph().parse(DATA_FILE, format="turtle")
    regions = set(graph.subjects(RDF.type, CONX_ADDR.AdministrativeArea))

    assert len(regions) == 271
    assert (SCHEME, RDF.type, OWL.Ontology) in graph
    assert (SCHEME, RDF.type, SKOS.ConceptScheme) in graph
    assert set(graph.objects(SCHEME, SKOS.hasTopConcept)) == regions
    assert {NUTS.DEA1, NUTS.DEA5, NUTS.DEZZ, NUTS.EL30, NUTS.SEZZ} <= regions

    for region in regions:
        assert (region, RDF.type, SKOS.Concept) in graph
        assert (region, SKOS.inScheme, SCHEME) in graph
        assert len(list(graph.objects(region, SKOS.prefLabel))) == 1
        assert len(list(graph.objects(region, CONX_ADDR.broaderAdministrativeTerritory))) == 1
        identifiers = list(graph.objects(region, ADMS.identifier))
        assert len(identifiers) == 1
        notations = list(graph.objects(identifiers[0], SKOS.notation))
        assert len(notations) == 1
        assert notations[0].datatype == ID_SCHEME["nuts-2"]


def test_nuts2_regions_link_to_the_correct_iso_country_resources() -> None:
    graph = Graph().parse(DATA_FILE, format="turtle")

    assert (
        NUTS.DEA5,
        CONX_ADDR.broaderAdministrativeTerritory,
        COUNTRIES.DEU,
    ) in graph
    assert (
        NUTS.EL30,
        CONX_ADDR.broaderAdministrativeTerritory,
        COUNTRIES.GRC,
    ) in graph
    identifier = next(graph.objects(NUTS.DEA5, ADMS.identifier))
    assert list(graph.objects(identifier, SKOS.notation)) == [
        Literal("DEA5", datatype=ID_SCHEME["nuts-2"])
    ]
