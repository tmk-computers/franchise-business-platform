# Tests Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `tests/` directory maintains the platform's automated unit, integration, and regression test suites executed via pytest. It verifies financial calculation precision, Excel workbook structure, JSON schema compliance, and repository integrity.

---

## 2. Specialized Agent Rules for `tests/`

1. **Zero Superficial Tests:**
   - Tests must validate actual business logic, mathematical formulas, and schema boundaries.
   - Never write trivial tests that pass unconditionally without asserting real business rules.
2. **Boundary & Stress Testing:**
   - Financial calculator tests (`tests/test_financial_calculator.py`) must cover edge cases:
     - Zero sales velocity (working capital drawdown).
     - 0% and 100% renewal retention (churn extremes).
     - Negative operating margins.
     - Tax-inclusive vs. tax-exclusive calculations.
3. **Automated Schema Verification:**
   - `tests/test_schemas.py` must test that valid client JSON files pass and intentionally malformed JSON files fail with expected `ValidationError` exceptions.
4. **Excel Structure Verification:**
   - `tests/test_excel_generator.py` must inspect generated `.xlsx` workbooks to verify that all 10 required sheets exist and formula cells contain valid Excel formula strings starting with `=`.
5. **Execution Command Standard:**
   - Tests must run cleanly via `python -m pytest tests/ -v`.
