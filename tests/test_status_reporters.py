"""Integration with the actual Person and Organization Core classes."""
import shutil
import subprocess
import sys

import pytest
from pyshacl import validate
from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS

from scripts.status_bundle import build_status_bundle
from scripts.validate_status import (
    ROOT, load_status_data, load_status_ontology, load_status_shapes,
    load_status_vocabularies, validate_status,
)

MODULE = ROOT / "modules/core/status"
EXAMPLES = MODULE / "examples/reporting-actors"
S = Namespace("https://www.construct-x.org/ontology/status#")
AGENT = Namespace("https://www.construct-x.org/ontology/agent#")
PERSON = Namespace("https://www.construct-x.org/ontology/person#")
ORG = Namespace("https://www.construct-x.org/ontology/organization#")
ACTORS = {
    "person": {
        "class": PERSON.Person,
        "ontology": ROOT / "modules/core/person/ontology/conx-person.ttl",
        "shapes": ROOT / "modules/core/person/shapes/conx-person-core.shacl.ttl",
        "name": PERSON.fullName,
        "name_error": "PER-010",
    },
    "organization": {
        "class": ORG.Organization,
        "ontology": ROOT / "modules/core/organization/ontology/conx-org.ttl",
        "shapes": ROOT / "modules/core/organization/shapes/conx-org-core.shacl.ttl",
        "name": ORG.name,
        "name_error": "ORG-010",
    },
}


@pytest.fixture(params=ACTORS, ids=ACTORS)
def actor(request):
    return {**ACTORS[request.param], "example": EXAMPLES / f"{request.param}-reporter.ttl"}


@pytest.fixture(scope="module")
def reporter_bundle(tmp_path_factory):
    directory = tmp_path_factory.mktemp("reporter-bundle")
    build_status_bundle(ROOT, directory)
    return directory


def test_real_core_actor_requires_its_class_context_without_redundant_agent_type(actor):
    data = load_status_data(actor["example"])
    reporter = next(data.objects(None, S.reportedBy))
    assert set(data.objects(reporter, RDF.type)) == {actor["class"]}
    assert not list(data.triples((None, RDFS.subClassOf, None)))
    before = set(data)

    conforms, _, report = validate_status(data)
    assert not conforms and "STATUS-040" in report, report

    context = load_status_data(actor["ontology"])
    assert (actor["class"], RDFS.subClassOf, AGENT.Agent) in context
    context_before = set(context)
    conforms, _, report = validate_status(data, additional_ontology=context)
    assert conforms, report
    assert set(data) == before
    assert set(context) == context_before


@pytest.mark.parametrize("mutation", ["missing-type", "blank-node", "name-literal"])
def test_reporter_type_and_iri_rules_still_apply_with_core_context(actor, mutation):
    data = load_status_data(actor["example"])
    statement, reporter = next(data.subject_objects(S.reportedBy))
    if mutation == "missing-type":
        data.remove((reporter, RDF.type, None))
    elif mutation == "blank-node":
        replacement = BNode()
        data.add((replacement, RDF.type, actor["class"]))
        data.set((statement, S.reportedBy, replacement))
    else:
        data.set((statement, S.reportedBy, Literal("Reporter name")))
    conforms, _, report = validate_status(data, additional_ontology=load_status_data(actor["ontology"]))
    assert not conforms and "STATUS-040" in report, report


def test_person_and_organization_cannot_both_report_the_same_assignment():
    person_data = load_status_data(EXAMPLES / "person-reporter.ttl")
    organization_data = load_status_data(EXAMPLES / "organization-reporter.ttl")
    person_statement = next(person_data.subjects(S.reportedBy, None))
    organization = next(organization_data.objects(None, S.reportedBy))
    data = person_data + organization_data
    data.add((person_statement, S.reportedBy, organization))
    context = load_status_data(ACTORS["person"]["ontology"]) + load_status_data(ACTORS["organization"]["ontology"])
    conforms, _, report = validate_status(data, additional_ontology=context)
    assert not conforms and "STATUS-040" in report, report


def test_examples_also_satisfy_their_own_actor_core_contract(actor):
    data = load_status_data(actor["example"])
    context = load_status_data(actor["ontology"])
    ontology = load_status_ontology() + context
    shapes = load_status_shapes()
    shapes.parse(actor["shapes"])
    shapes.parse(ROOT / "modules/core/identifier/shapes/conx-id-core.shacl.ttl")
    data += load_status_vocabularies()
    conforms, _, report = validate(data, shacl_graph=shapes, ont_graph=ontology,
                                  inference="none", advanced=True, do_owl_imports=False)
    assert conforms, report

    # Loading a T-Box establishes Agent membership; applying the actor shapes
    # is the separate step that checks the actor's mandatory name fields.
    reporter = next(data.objects(None, S.reportedBy))
    data.remove((reporter, actor["name"], None))
    assert validate_status(data, additional_ontology=context)[0]
    conforms, _, report = validate(data, shacl_graph=shapes, ont_graph=ontology,
                                  inference="none", advanced=True, do_owl_imports=False)
    assert not conforms and actor["name_error"] in report, report


def test_documented_cli_loads_actual_core_ontology_as_extra_data(actor):
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/validate_status.py"),
         "--data", str(actor["example"]), "--data", str(actor["ontology"])],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Conforms: True" in result.stdout


def test_relocated_bundle_and_generic_shacl_accept_actual_core_context(actor, reporter_bundle, tmp_path):
    standalone = tmp_path / "package"
    shutil.copytree(reporter_bundle, standalone)
    data_file = tmp_path / "report.ttl"
    context_file = tmp_path / "actor-ontology.ttl"
    shutil.copy2(actor["example"], data_file)
    shutil.copy2(actor["ontology"], context_file)
    command = [sys.executable, "-B", str(standalone / "validate.py"), "--data", str(data_file)]
    missing_context = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, encoding="utf-8")
    assert missing_context.returncode == 1
    assert "STATUS-040" in missing_context.stdout
    result = subprocess.run(command + ["--data", str(context_file)], cwd=tmp_path,
                            capture_output=True, text=True, encoding="utf-8")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Conforms: True" in result.stdout

    # Use only the exported RDF components and the copied Core context.
    data = Graph().parse(data_file).parse(standalone / "vocabularies.ttl")
    ontology = Graph().parse(standalone / "ontology.ttl").parse(context_file)
    conforms, _, report = validate(
        data, shacl_graph=Graph().parse(standalone / "shapes.ttl"), ont_graph=ontology,
        inference="none", advanced=True, do_owl_imports=False,
    )
    assert conforms, report
