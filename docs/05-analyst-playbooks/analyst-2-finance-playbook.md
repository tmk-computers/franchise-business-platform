# Analyst 2 Playbook: Financial Modeling, Data Analytics & Intelligence

Welcome to the operational execution manual for **Analyst 2 (Financial Modeling, Quantitative Analytics & Intelligence)**.

As Analyst 2, you own the mathematical, quantitative, computational, and financial deliverables of the platform. You build unit economics models, maintain client assumptions, calculate cash flows, evaluate break-even and payback timelines, generate formula-linked Excel models using Python, and audit strategic claims for quantitative feasibility.

---

## Table of Contents
1. [Core Responsibilities & Technical Mandates](#1-core-responsibilities--technical-mandates)
2. [Decimal-Safe Arithmetic & Mathematical Standards](#2-decimal-safe-arithmetic--mathematical-standards)
3. [Financial Assumptions Management & Schema Validation](#3-financial-assumptions-management--schema-validation)
4. [Franchise Investment & CapEx Modeling](#4-franchise-investment--capex-modeling)
5. [Revenue-Sharing & Tax Segregation Calculations](#5-revenue-sharing--tax-segregation-calculations)
6. [Franchisee 36-Month P&L & Cash Flow Projections](#6-franchisee-36-month-pl--cash-flow-projections)
7. [Franchisor Central P&L & Royalty Settlement](#7-franchisor-central-pl--royalty-settlement)
8. [Break-Even & Payback Analysis](#8-break-even--payback-analysis)
9. [Product Unit Economics & Basket Modeling](#9-product-unit-economics--basket-modeling)
10. [Territory Scoring & Quantitative Demographic Indexing](#10-territory-scoring--quantitative-demographic-indexing)
11. [KPI Architecture & Dashboard Design](#11-kpi-architecture--dashboard-design)
12. [Multi-Scenario Sensitivity Modeling](#12-multi-scenario-sensitivity-modeling)
13. [CLI Commands, Excel Generation & Model Validation](#13-cli-commands-excel-generation--model-validation)
14. [Franchise Launch Readiness Quantitative Analytics & Tracker Generation](#14-franchise-launch-readiness-quantitative-analytics--tracker-generation)
15. [Analyst 2 Quality Checklist & Cross-Review Hand-Off](#15-analyst-2-quality-checklist--cross-review-hand-off)

---

## 1. Core Responsibilities & Technical Mandates

### In-Scope for Analyst 2
- **Quantitative Modeling:** Building and maintaining `assumptions.json` and scenario definitions.
- **Python Calculation Engine:** Executing and extending `tools/financial-modeling/calculator.py` and `cli.py`.
- **Dynamic Excel Generation:** Maintaining and enhancing `tools/financial-modeling/excel_generator.py`.
- **Unit Economics & Sensitivity:** Quantifying break-even, payback, NPV/IRR, and 36-month P&L statements.
- **Quantitative Territory Indexing:** Developing demographic scoring algorithms for taluka and district rankings.
- **Cross-Review:** Auditing Analyst 1's qualitative strategies and pitch decks for numerical consistency.

### Out-of-Scope (Handled by Analyst 1)
- Authoring qualitative market narrative briefs or customer interview summaries.
- Drafting legal agreements or operations manual text.
- Writing commercial marketing copy for brochures and pitch presentations.

---

## 2. Decimal-Safe Arithmetic & Mathematical Standards

Floating-point operations (`float` in Python) are strictly prohibited for financial calculations due to binary approximation errors.

### Mandatory Python Pattern
```python
from decimal import Decimal, ROUND_HALF_UP

# Define financial values as string-based Decimals:
price_net = Decimal("45000.00")
gst_rate = Decimal("0.18")
tax_amount = (price_net * gst_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
total_gross = (price_net + tax_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

### Rounding & Tax Conventions
- Currency figures must be quantized to two decimal places: `.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`.
- **Statutory Taxes (GST 18% in India):** Must be isolated from distributable revenue. Never calculate franchisee or franchisor shares on tax-inclusive gross amounts.

---

## 3. Financial Assumptions Management & Schema Validation

Every financial parameter for a client workspace resides in `clients/<client-slug>/financial-models/assumptions.json`.

### Structure of `assumptions.json`
The file is strictly validated against `schemas/financial-assumptions.schema.json` and contains:
- `franchiseFees`: Promotional joining fee (₹25,000 for early units), standard joining fee (₹50,000), renewal fee rates.
- `revenueSharing`: Default split percentages for new software licenses and annual renewals (e.g., 40% Franchisee : 60% Franchisor).
- `franchiseeCapEx`: Office lease deposit, interior/signage, computer hardware, networking.
- `franchiseeMonthlyOpEx`: Office rent, sales staff salary, internet, utilities, local marketing, admin.
- `scenarios`: Multi-case assumptions (`conservative`, `base`, `optimistic`) for monthly unit sales velocity, annual client renewal retention, and ramp-up periods.

### Validation Command
Whenever modifying `assumptions.json`, validate immediately:
```bash
python -m pytest tests/test_schemas.py -v
```

---

## 4. Franchise Investment & CapEx Modeling

### CapEx Line Items
The franchisee's initial capital outlay covers:
1. **Office Rental Deposit:** (e.g., ₹20,000–₹30,000 refundable commercial lease security).
2. **Branding & Signage:** (e.g., ₹15,000 corporate acrylic fascia board and internal posters).
3. **IT Hardware & Networking:** (e.g., ₹30,000 workstation, printer, UPS, router).
4. **Initial Franchise Joining Fee:** (e.g., ₹25,000 promotional tier or ₹50,000 standard tier).
5. **Mandatory Working Capital Reserve:** (e.g., ₹50,000–₹1,00,000 covering 4–6 months of fixed overhead).

### Mathematical Formula
$$\text{Total Initial Outlay} = \text{CapEx} + \text{Joining Fee} + \text{Working Capital Reserve}$$

---

## 5. Revenue-Sharing & Tax Segregation Calculations

### Flow of Funds Logic
1. **Gross Customer Billing ($G$):** Total invoiced to end client, inclusive of 18% GST.
2. **Net Realized Revenue ($R$):**
   $$R = \frac{G}{1 + \text{GST Rate}} = \frac{G}{1.18}$$
3. **Statutory Tax ($T$):** Remitted directly to tax authorities:
   $$T = G - R$$
4. **Franchisee Share ($S_F$):**
   $$S_F = R \times \text{Franchisee Split \%} \quad (\text{e.g., } R \times 0.40)$$
5. **Franchisor Share ($S_M$):**
   $$S_M = R \times \text{Franchisor Split \%} \quad (\text{e.g., } R \times 0.60)$$

---

## 6. Franchisee 36-Month P&L & Cash Flow Projections

The Python calculator generates a complete month-by-month financial projection across a 36-month horizon.

### Month-by-Month Statement Structure
- **Gross Monthly Revenue:** Blended license sales + recognized recurring renewals.
- **Direct Costs / Splits:** Net revenue retained by franchisee (e.g., 40%).
- **Fixed Monthly Operating Overhead (OpEx):** Office rent + staff salaries + telecom/utilities + local marketing.
- **Monthly EBITDA:** Franchisee Retained Revenue minus Total Monthly OpEx.
- **TDS / Net Profit:** EBITDA adjusted for applicable corporate/individual tax withholding.
- **Cumulative Cash Flow:** Starting from $(-\text{Total Initial Investment})$ and accumulating monthly EBITDA until positive cash inflection.

---

## 7. Franchisor Central P&L & Royalty Settlement

The central franchisor P&L aggregates revenue across all active franchise territories:
- **Central Revenue Streams:**
  - Upfront Joining Fees (collected once per unit).
  - Central Net Revenue Share (e.g., 60% of all software license billings).
  - Annual Software Maintenance / Renewal Share.
- **Central Costs:**
  - Cloud server hosting & database scaling.
  - Core software development & bug patching.
  - Central marketing campaigns and lead qualification.
  - Regional franchise manager auditing & field support.

---

## 8. Break-Even & Payback Analysis

### Unit Break-Even Formulation
Let $C_{\text{fixed}}$ be the franchisee's monthly fixed operating overhead (e.g., ₹27,000).
Let $M_{\text{unit}}$ be the franchisee's average retained margin per software product sale (e.g., 40% of blended ₹45,000 net license price = ₹18,000).

$$\text{Break-Even Units / Month} = \left\lceil \frac{C_{\text{fixed}}}{M_{\text{unit}}} \right\rceil = \left\lceil \frac{27,000}{18,000} \right\rceil = 2 \text{ units/month}$$

### Payback Timeline Formulation
$$\text{Payback Month} = \min \left\{ t \;\middle|\; \sum_{m=1}^{t} \text{Monthly Operating Cash Flow}_m \ge \text{Total Initial Investment} \right\}$$
Under TMK Base Case assumptions, payback occurs at **Month 8–10** post-launch.

---

## 9. Product Unit Economics & Basket Modeling

Software products feature varying price points, delivery models, and margins. For TMK IT Solutions, the product catalog in `products-catalog.json` defines 6 distinct products:

| Product ID | Name | Net Price (INR) | Impl. Fee (INR) | Est. Annual Renewal |
|---|---|---|---|---|
| `prd-01-enterprise-erp` | Cloud Enterprise ERP | ₹45,000 | ₹10,000 | ₹15,000 |
| `prd-02-school-management` | School & College Management | ₹30,000 | ₹5,000 | ₹10,000 |
| `prd-03-hospital-clinic-erp`| Hospital & Diagnostic ERP | ₹55,000 | ₹12,000 | ₹18,000 |
| `prd-04-retail-pos-inventory`| Retail POS & Multi-Store | ₹25,000 | ₹3,000 | ₹8,000 |
| `prd-05-devops-automation`  | Cloud Infrastructure & DevOps| ₹60,000 | ₹15,000 | ₹20,000 |
| `prd-06-cybersecurity-audit`| Cyber & Compliance Suite | ₹40,000 | ₹8,000 | ₹12,000 |

**Blended Basket Net Price:** ₹42,500. Average franchisee commission per sale at 40%: **₹17,000**.

---

## 10. Territory Scoring & Quantitative Demographic Indexing

Analyst 2 models territorial potential using a normalized multi-criteria weighting index:

$$\text{Territory Score} = (0.30 \times M) + (0.25 \times I) + (0.20 \times B) + (0.25 \times C)$$

Where:
- $M$: Normalized commercial MSME establishment density (0–100).
- $I$: Normalized institutional count (schools, colleges, hospitals) (0–100).
- $B$: Banking, internet connectivity, and commercial infrastructure index (0–100).
- $C$: Competitive whitespace index (absence of direct incumbents) (0–100).

---

## 11. KPI Architecture & Dashboard Design

Analyst 2 designs and monitors the 13 core platform KPIs defined in `frameworks/performance-analytics/performance-framework.md`:
1. Monthly License Sales Velocity (Units/month).
2. Net Realized Revenue per Territory (₹/month).
3. Annual Renewal Retention Rate (% active clients renewing).
4. Franchisee Operating Margin (EBITDA / Net Revenue).
5. Unit Break-Even Achievement Month.
6. Lead-to-Conversion Ratio (Closed deals / Qualified leads).
7. Deal Registration Velocity (Days from lock to contract).
8. Average Deal Size (₹ ACV).
9. Franchisee Payback Progress (% initial capital recovered).
10. Support SLA Adherence Rate (% P1 issues resolved < 2h).
11. Audit Compliance Score (% compliance on bi-annual review).
12. Customer Churn Rate (% client attrition/month).
13. Network Health Index (Composite territory rating).

---

## 12. Multi-Scenario Sensitivity Modeling

Analyst 2 evaluates three standardized cases to guarantee transparent risk assessment:

| Dimension | Conservative (Stress-Test) | Base (Target Case) | Optimistic (High-Growth) |
|---|---|---|---|
| Monthly Sales Velocity | 1.5 units / month | 3.0 units / month | 5.5 units / month |
| Annual Renewal Rate | 60% | 80% | 90% |
| Ramp-Up Period | 6 months | 3 months | 1 month |
| Payback Timeline | Month 14–16 | Month 8–10 | Month 5–6 |
| 36-Month Net EBITDA | Lower baseline | Empirically grounded | Rapid network expansion |

---

## 13. CLI Commands, Excel Generation & Model Validation

Analyst 2 must execute only verified, production-tested command-line tools. Do not invent arguments.

### 1. Run Financial Projection Simulation
Run the calculation engine for a specific scenario:
```bash
# Base scenario:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario base

# Conservative scenario:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario conservative

# Optimistic scenario:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario optimistic
```

### 2. Generate Formula-Linked Excel Workbook
Generate the dynamic openpyxl workbook containing 10 interlinked sheets with uppercase formulas:
```bash
python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel
```
Output workbook location:
`clients/tmk-it-solutions/financial-models/tmk_it_solutions_franchise_financial_model.xlsx`

### 3. Run Automated Unit Tests
Verify mathematical calculations, Excel formula syntax, and schema integrity:
```bash
# Test financial calculator Decimal math:
python -m pytest tests/test_financial_calculator.py -v

# Test Excel generator and formula integrity:
python -m pytest tests/test_excel_generator.py -v

# Run the complete test suite:
python -m pytest tests/ -v
```

### 4. Run Repository Validation
```bash
python tools/validation/validate_repo.py
```

---

## 14. Franchise Launch Readiness Quantitative Analytics & Tracker Generation

### Purpose & Role Ownership
Under the 12-workstream launch readiness framework ([franchise-launch-readiness-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-launch-readiness/franchise-launch-readiness-framework.md)), Analyst 2 is accountable for quantitative verification, data schema compliance, automated Excel tracker generation, and financial readiness indicators.

### Workstream Ownership Breakdown for Analyst 2
1. **Workstream 4 (Finance, Banking & Accounting):**
   - Verify commercial split mechanics, tax segregation routines (e.g. 18% GST passthrough), and escrow account settlement workflows.
   - Monitor clearance of Blocker `BLK-002` (Dedicated Escrow/Settlement Bank Account Configuration).
2. **Workstream 6 (Franchise Management Technology):**
   - Audit client JSON data contracts against schemas (e.g., `schemas/launch-readiness.schema.json`).
   - Monitor technical blockers including `BLK-003` (Demonstration Sandbox Cloud Deployment) and `BLK-007` (90-Day CRM Deal Lock Engine).
3. **Workstream 1 (Commercial Modeling Verification):**
   - Calibrate unit economics, operational break-even unit sales, and working capital drawdowns.

### Generating the Interactive Excel Launch Tracker
Analyst 2 generates and validates the client launch readiness workbook using the platform tool:

```bash
# Generate interactive launch readiness tracker:
python tools/launch-readiness/generate_readiness_tracker.py --client tmk-it-solutions
```

Output workbook location:
`clients/tmk-it-solutions/launch-readiness/tmk_launch_readiness_tracker.xlsx`

**Workbook Structure & Formula Standards:**
- **5 Interlinked Sheets:** `Readiness Dashboard`, `Workstream Summary`, `Owner Summary`, `Master Checklist`, `Gates & Blockers`.
- **Formulas:** All formulas must be strictly uppercase (`COUNTIF`, `COUNTIFS`, `COUNTA`, `IF`, `ROUND`, `SUM`).
- **Data Validation:** Dynamic dropdowns for Status and Priority columns.

### Mathematical Readiness Indexing
Analyst 2 computes the quantitative progress metrics defined in the framework:
- **Workstream Readiness Index:**
  $$WRI_w = \frac{\sum_{i=1}^{N_w} (w_i \cdot S_i)}{\sum_{i=1}^{N_w} w_i}$$
- **Platform Launch Readiness Index:**
  $$PLRI = \sum_{w=1}^{12} (\Omega_w \cdot WRI_w)$$

---

## 15. Analyst 2 Quality Checklist & Cross-Review Hand-Off

Before submitting any financial model or data analysis for peer review by Analyst 1:

```text
[ ] 1. Decimal Precision: All Python math uses decimal.Decimal with quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).
[ ] 2. Zero Float Math: No floating-point division or rounding drift in currency calculations.
[ ] 3. Tax Isolation: Statutory pass-through taxes (18% GST) are segregated before split calculations.
[ ] 4. Schema Compliance: assumptions.json passes schemas/financial-assumptions.schema.json validation.
[ ] 5. Dynamic Excel Formulas: Excel sheets use valid uppercase formulas (SUM, AVERAGE, ROUND, IF, MAX) with zero hardcoded numbers in formula cells.
[ ] 6. Multi-Scenario Validation: Projections tested across conservative, base, and optimistic scenarios.
[ ] 7. Launch Tracker Validated: tmk_launch_readiness_tracker.xlsx generated cleanly with openpyxl and formulas verified.
[ ] 8. Automated Test Suite Passes: pytest tests/ returns 100% green.
[ ] 9. Cross-Review Hand-Off: Model logged in analyst-workspace/task-tracker/task-board.md for Analyst 1 sign-off.
```
