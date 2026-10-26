# Tools Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `tools/` directory contains the platform's automation software, calculation engines, spreadsheet generators, presentation compilers, and repository validation utilities:
- `tools/financial-modeling/`: Python `Decimal` calculation library (`calculator.py`), openpyxl workbook generator (`excel_generator.py`), and CLI runner (`cli.py`).
- `tools/document-generation/`: PowerPoint presentation compiler (`generate_pitch_deck.py`).
- `tools/validation/`: Standalone repository integrity and schema validation engine (`validate_repo.py`).

---

## 2. Specialized Agent Rules for `tools/`

1. **Strict Decimal Precision for Currency:**
   - Any financial calculation in Python must use `from decimal import Decimal, ROUND_HALF_UP`.
   - Never perform floating-point arithmetic (`float`) on currency amounts.
   - All monetary results must be quantized to 2 decimal places (`Decimal("0.01")`).
2. **Dynamic Uppercase Excel Formulas:**
   - When generating `.xlsx` workbooks via `openpyxl`:
     - NEVER hardcode calculated numerical values into cells that should be formula-driven.
     - Always use standard uppercase Excel formulas (`=SUM(...)`, `=IF(...)`, `=AVERAGE(...)`, `=ROUND(...)`).
     - Downstream sheets (P&L, Cash Flow, Break-Even) must link directly to the `Assumptions` and `Product Pricing` sheets.
3. **Cross-Platform Compatibility:**
   - Windows Console Safe: Ensure scripts handle Windows console stdout encoding safely (configure `sys.stdout.reconfigure(encoding="utf-8")` or avoid unencoded Unicode currency symbols on stdout).
   - Use `os.path.join` and cross-platform path resolution.
4. **100% Test Coverage Requirement:**
   - Any new calculation method added to `calculator.py` must have corresponding unit tests in `tests/test_financial_calculator.py`.
   - Any modification to spreadsheet structure must be validated in `tests/test_excel_generator.py`.
