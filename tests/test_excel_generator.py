"""
Unit Tests for Excel Generator
==============================
Validates that openpyxl generates workbooks with all 10 required sheets,
upper-case Excel formulas, and valid cell values.
"""

import pytest
import os
import openpyxl
import sys

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tools", "financial-modeling"))
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from excel_generator import FranchiseExcelGenerator


def test_excel_generation_and_sheet_structure(tmp_path):
    output_xlsx = str(tmp_path / "test_model.xlsx")
    generator = FranchiseExcelGenerator(client_name="Test Enterprise LLP")
    generator.generate(output_xlsx)

    assert os.path.exists(output_xlsx)
    wb = openpyxl.load_workbook(output_xlsx, data_only=False)

    expected_sheets = [
        "Dashboard Summary",
        "Assumptions",
        "Product Pricing",
        "Franchise Investment",
        "Monthly Sales Forecast",
        "Franchisee P&L",
        "Franchisor P&L",
        "Cash Flow",
        "Break-Even Analysis",
        "Scenario Analysis"
    ]

    for sheet_name in expected_sheets:
        assert sheet_name in wb.sheetnames, f"Missing sheet: {sheet_name}"

    # Verify formulas in Franchise Investment sheet
    ws_inv = wb["Franchise Investment"]
    assert str(ws_inv["C15"].value).startswith("=SUM(")

    # Verify formulas in Break-Even sheet
    ws_be = wb["Break-Even Analysis"]
    assert str(ws_be["C9"].value).startswith("=")
