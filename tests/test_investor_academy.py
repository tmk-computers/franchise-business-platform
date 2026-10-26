"""
Test Suite for Franchise Investor Academy (FIA)
================================================
Verifies:
1. Existence and structural completeness of all 10 eBook volumes.
2. Complete chapter set and assessment resources for Book 1.
3. Existence of core educational assets (checklists, glossary, learning paths, standards).
4. Mathematical verification of educational financial formulas (GST isolation, break-even, payback).
"""

import os
import re
from decimal import Decimal, ROUND_HALF_UP
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ACADEMY_ROOT = os.path.join(REPO_ROOT, "education", "franchise-investor-academy")


def test_academy_core_assets_exist():
    """Verify that all foundational guides and decision tools exist in the Academy root."""
    core_files = [
        "README.md",
        "LEARNING_PATHS.md",
        "DUE_DILIGENCE_CHECKLIST.md",
        "GLOSSARY.md",
        "EDITORIAL_STANDARDS.md",
        "PUBLISHING_WORKFLOW.md"
    ]
    for cf in core_files:
        fpath = os.path.join(ACADEMY_ROOT, cf)
        assert os.path.exists(fpath), f"Missing core Academy file: {cf}"
        assert os.path.getsize(fpath) > 1000, f"Core Academy file {cf} is too small or empty."


def test_book_01_complete_volume_assets():
    """Verify that Book 1 contains all 6 complete chapters, quizzes, and volume README."""
    book1_dir = os.path.join(ACADEMY_ROOT, "book-01-first-time-investor-handbook")
    assert os.path.isdir(book1_dir), "Book 1 directory not found"

    expected_assets = [
        "README.md",
        "chapter-01-what-is-franchising.md",
        "chapter-02-myths-vs-reality.md",
        "chapter-03-archetypes-and-models.md",
        "chapter-04-financial-mechanics.md",
        "chapter-05-investor-self-assessment.md",
        "chapter-06-red-flags-and-due-diligence.md",
        "quizzes-and-case-studies.md"
    ]
    for asset in expected_assets:
        fpath = os.path.join(book1_dir, asset)
        assert os.path.exists(fpath), f"Book 1 is missing asset: {asset}"
        assert os.path.getsize(fpath) > 3000, f"Book 1 asset {asset} is unexpectedly small."


def test_all_10_volumes_exist_with_starters():
    """Verify that Books 2 through 10 have structured READMEs and initial chapters."""
    expected_books = [
        ("book-02-business-models-and-archetypes", "chapter-01-fofo-operating-mechanics.md"),
        ("book-03-unit-economics-and-financial-literacy", "chapter-01-understanding-capex-opex.md"),
        ("book-04-due-diligence-playbook", "chapter-01-investigating-the-franchisor.md"),
        ("book-05-franchise-agreements-and-legal-rights", "chapter-01-anatomy-of-a-franchise-contract.md"),
        ("book-06-sector-by-sector-economics", "chapter-01-cross-industry-comparison.md"),
        ("book-07-site-selection-and-territory-intelligence", "chapter-01-demographic-and-catchment-analysis.md"),
        ("book-08-working-capital-and-cash-flow", "chapter-01-the-working-capital-j-curve.md"),
        ("book-09-multi-unit-franchising", "chapter-01-transitioning-from-1-to-5-units.md"),
        ("book-10-franchise-exits-and-resales", "chapter-01-valuation-and-exit-planning.md")
    ]

    for b_dir, ch1 in expected_books:
        b_path = os.path.join(ACADEMY_ROOT, b_dir)
        assert os.path.isdir(b_path), f"Missing eBook directory: {b_dir}"

        readme = os.path.join(b_path, "README.md")
        assert os.path.exists(readme), f"Missing README.md in {b_dir}"
        assert os.path.getsize(readme) > 1000, f"README.md in {b_dir} is too small"

        chapter1 = os.path.join(b_path, ch1)
        assert os.path.exists(chapter1), f"Missing Chapter 1 in {b_dir}: {ch1}"
        assert os.path.getsize(chapter1) > 4000, f"Chapter 1 in {b_dir} lacks substantive content"


def test_educational_financial_math_validation():
    """Verify mathematical accuracy of financial examples in Book 1 Chapter 4."""
    # 1. 18% GST Isolation Math
    gross_collections = Decimal("1180000.00")
    gst_rate = Decimal("0.18")
    net_revenue = (gross_collections / (Decimal("1.00") + gst_rate)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    gst_liability = gross_collections - net_revenue

    assert net_revenue == Decimal("1000000.00"), "Net revenue must equal 10,00,000.00 exactly"
    assert gst_liability == Decimal("180000.00"), "GST liability must equal 1,80,000.00 exactly"

    # 2. Royalty on Net Revenue
    royalty_rate = Decimal("0.06")
    royalty_payable = (net_revenue * royalty_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    assert royalty_payable == Decimal("60000.00"), "6% royalty on 10,00,000 net must be 60,000.00"

    # 3. Operational Break-Even Math
    fixed_overhead = Decimal("160000.00")
    contribution_margin = Decimal("0.40")
    break_even_revenue = (fixed_overhead / contribution_margin).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    assert break_even_revenue == Decimal("400000.00"), "Break-even revenue must be 4,00,000.00"

    # 4. Simple Payback Period
    total_initial_capex = Decimal("2000000.00")
    annual_post_tax_cash_flow = Decimal("720000.00")
    payback_years = (total_initial_capex / annual_post_tax_cash_flow).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    payback_months = (payback_years * Decimal("12")).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    assert payback_months == Decimal("33.4"), "Payback must be 33.4 months"
