"""
Unit & Integration Tests for Franchise Launch Readiness Framework
==================================================================
Validates:
1. JSON schema conformance for launch readiness checklists.
2. Uniqueness and pattern matching of all task IDs.
3. Complete coverage of the 12 management-mandated workstreams.
4. Representation of all 6 sequential launch gates.
5. Conformance of maturity statuses to the 7-stage hierarchy.
6. Resolution of all related document file paths on disk.
7. Structural integrity and formulas of the Excel tracker workbook.
"""

import os
import json
import re
import pytest
import openpyxl
from jsonschema import validate, ValidationError

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHECKLIST_PATH = os.path.join(REPO_ROOT, "clients", "tmk-it-solutions", "launch-readiness", "tmk-launch-readiness-checklist.json")
SCHEMA_PATH = os.path.join(REPO_ROOT, "schemas", "launch-readiness.schema.json")
EXCEL_PATH = os.path.join(REPO_ROOT, "clients", "tmk-it-solutions", "launch-readiness", "tmk_launch_readiness_tracker.xlsx")


@pytest.fixture(scope="module")
def checklist_data():
    with open(CHECKLIST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def launch_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_launch_readiness_schema_conformance(checklist_data, launch_schema):
    """Ensure TMK launch readiness checklist strictly validates against schemas/launch-readiness.schema.json."""
    validate(instance=checklist_data, schema=launch_schema)


def test_task_id_uniqueness_and_formatting(checklist_data):
    """Verify that every task ID is unique and follows the FLR-<DOM>-<NUM> convention."""
    items = checklist_data["items"]
    task_ids = [item["taskId"] for item in items]
    assert len(task_ids) == len(set(task_ids)), f"Duplicate task IDs found: {[tid for tid in task_ids if task_ids.count(tid) > 1]}"
    
    pattern = re.compile(r"^FLR-[A-Z]{3}-[0-9]{3}$")
    for tid in task_ids:
        assert pattern.match(tid), f"Task ID '{tid}' does not match required pattern ^FLR-[A-Z]{{3}}-[0-9]{{3}}$"


def test_all_12_management_workstreams_present(checklist_data):
    """Ensure all 12 original workstreams are represented without omission."""
    expected_workstreams = [
        "Business Model & Commercial Strategy",
        "Legal, Regulatory & Intellectual Property",
        "Six-Product Sales Readiness",
        "Finance, Banking & Accounting",
        "Franchise Operations & SOPs",
        "Franchise Management Technology",
        "Franchise Recruitment & Marketing",
        "Training & Certification",
        "Central Delivery & Customer Support",
        "Partner Onboarding Documents",
        "Governance & Performance Monitoring",
        "Pilot Launch & Final Approval"
    ]
    found_workstreams = set(item["workstream"] for item in checklist_data["items"])
    for ws in expected_workstreams:
        assert ws in found_workstreams, f"Missing required workstream: '{ws}'"


def test_all_6_launch_gates_represented(checklist_data):
    """Ensure all 6 launch gates are represented across checklist items."""
    expected_gates = [
        "Gate 1: Business Model Approved",
        "Gate 2: Legal & Financial Readiness",
        "Gate 3: Product & Delivery Readiness",
        "Gate 4: Franchise Recruitment Readiness",
        "Gate 5: Pilot Launch Readiness",
        "Gate 6: National Expansion Approval"
    ]
    found_gates = set(item["launchGate"] for item in checklist_data["items"])
    for gate in expected_gates:
        assert gate in found_gates, f"Missing launch gate mapping: '{gate}'"


def test_status_hierarchy_and_classifications(checklist_data):
    """Ensure tasks strictly adhere to the 7-stage maturity hierarchy and 8 classifications."""
    valid_statuses = {
        "Not Started", "In Progress", "Document Created", "Document Reviewed",
        "Document Approved", "Process Implemented", "Process Verified"
    }
    valid_classifications = {
        "Business research and modeling", "Documentation and presentation",
        "Legal and regulatory review", "Product engineering", "Finance and accounting",
        "Franchise operations", "Technology implementation", "Management approval"
    }

    for item in checklist_data["items"]:
        assert item["status"] in valid_statuses, f"Invalid status in task {item['taskId']}: {item['status']}"
        assert item["classification"] in valid_classifications, f"Invalid classification in task {item['taskId']}: {item['classification']}"
        assert isinstance(item["isBlocker"], bool), f"isBlocker must be boolean in task {item['taskId']}"


def test_related_documents_exist_on_disk(checklist_data):
    """Verify that every repository document referenced in relatedDocuments actually exists on disk."""
    for item in checklist_data["items"]:
        for doc_rel in item.get("relatedDocuments", []):
            doc_abs = os.path.join(REPO_ROOT, doc_rel.replace("/", os.sep))
            assert os.path.exists(doc_abs), f"Task {item['taskId']} references non-existent file: {doc_rel}"


def test_excel_tracker_workbook_structure():
    """Verify that the generated Excel launch readiness tracker exists, contains all 5 sheets and valid formulas."""
    assert os.path.exists(EXCEL_PATH), f"Excel tracker file not found at: {EXCEL_PATH}"
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=False)

    expected_sheets = [
        "Readiness Dashboard",
        "Workstream Summary",
        "Owner Summary",
        "Master Checklist",
        "Gates & Blockers"
    ]
    for sname in expected_sheets:
        assert sname in wb.sheetnames, f"Missing required sheet: '{sname}'"

    # Verify formula usage on Master Checklist
    ws_master = wb["Master Checklist"]
    assert ws_master.max_row >= 66  # Header + 65 items

    # Verify uppercase formulas in Workstream Summary
    ws_ws = wb["Workstream Summary"]
    c_formula = str(ws_ws["C5"].value)
    assert "COUNTIFS(" in c_formula or "COUNTIF(" in c_formula, f"Expected COUNTIF(S) formula in C5, got {c_formula}"

    # Verify uppercase formulas in Dashboard
    ws_dash = wb["Readiness Dashboard"]
    dash_total_formula = str(ws_dash["B6"].value)
    assert dash_total_formula.startswith("="), f"Expected formula in Dashboard total cell B6, got {dash_total_formula}"
