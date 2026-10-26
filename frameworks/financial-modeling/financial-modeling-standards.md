# Financial Modeling Standards & Computational Principles

## 1. Purpose
This document establishes strict mathematical standards, precision requirements, currency handling rules, and spreadsheet formatting conventions for all quantitative models across the platform.

---

## 2. Cardinal Modeling Standards

### Standard 1: Decimal Precision vs. Float
All quantitative calculations in Python scripts and analytical tools must strictly use the standard library `decimal.Decimal` module:
```python
# Prohibited:
price = 60000.0 * 0.40  # Can result in 24000.000000000004

# Mandatory:
from decimal import Decimal, ROUND_HALF_UP
price = (Decimal("60000") * Decimal("0.40")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

### Standard 2: Statutory Tax Segregation
- Models must clearly designate whether prices are **Tax-Exclusive** or **Tax-Inclusive**.
- Unless explicitly indicated otherwise, baseline modeled prices are **Tax-Exclusive**.
- Statutory pass-through taxes (e.g., 18% GST in India) must never be treated as revenue or included in commission split distributions.

### Standard 3: Native Dynamic Formulas in Generated Spreadsheets
When tools generate Microsoft Excel (`.xlsx`) workbooks:
- **Never hardcode calculated results** into cells that should be formula-driven.
- Use uppercase standard Excel formulas:
  - Totaling ranges: `=SUM(C4:C15)`
  - Multiplication: `=B12*C12`
  - Conditional logic: `=IF(D4>0, D4*0.4, 0)`
  - Net Profit / EBITDA: `=C10-C25`
  - Cumulative balance: `=F29+C30`
- Keep assumptions in a dedicated `Assumptions` worksheet so that modifying an assumption in one cell dynamically updates all linked downstream sheets (P&L, Cash Flow, Break-Even, Dashboard).

### Standard 4: Scenario Symmetry
Every financial forecast must generate three balanced scenarios:
1. **Conservative (Downside):** 60–70% of base sales velocity; higher sales cycle length (+30%); 20% annual churn.
2. **Base Case (Realistic Target):** Expected sales velocity based on validated market research; 12% annual churn.
3. **Optimistic (High Performance):** 130–140% of base sales velocity; shorter sales cycle (-20%); 8% annual churn.

### Standard 5: Working Capital Solvency Check
Every model must calculate the **Maximum Drawdown** and verify that the proposed Franchisee Initial Investment includes an adequate working capital reserve covering at least 4 to 6 months of fixed overhead under a zero-sales stress scenario.
