# Financial Modeling Standards & Computational Rules

## 1. Mathematical Standards
1. **Decimal-Safe Arithmetic:** All monetary amounts must use Python `Decimal` with `ROUND_HALF_UP` rounding. Standard float math is strictly forbidden for financial calculations.
2. **Tax Separation:** Taxes (e.g., 18% GST) are pass-through collections and must never be treated as revenue or commissionable revenue.
3. **Dynamic Formulas in Spreadsheets:** Generated Excel sheets must use uppercase Excel formulas (`=SUM()`, `=IF()`, `=B4*C4`) linking back to Assumptions.
4. **Three-Scenario Symmetry:** Every model must project Conservative (downside), Base Case (target), and Optimistic (high performance) scenarios.
