# Financial Feasibility & Unit Economics Framework

## 1. Purpose
This framework establishes standardized, decimal-safe financial analysis standards to evaluate the economic sustainability of franchise ventures. It models capital outlays, monthly operational dynamics, unit economics, payback schedules, and sensitivity metrics for both the **Franchisee** and the **Franchisor**.

---

## 2. Business Questions Addressed
1. What is the total initial capital required for a franchisee to launch and survive to positive operating cash flow?
2. What are the franchisee's and franchisor's monthly operating margins, gross contributions, and net profit margins?
3. Exactly how many software licenses or product units must be sold each month to achieve operational break-even?
4. What is the projected payback period and 36-month Return on Investment (ROI) under conservative, base, and optimistic scenarios?
5. How does customer churn impact recurring subscription renewal revenues over a 3-year operating lifecycle?

---

## 3. Required Inputs

### 3.1. Franchisee Capital Expenditure & Setup Inputs
- **Franchise Joining Fee ($F_{join}$):** One-time or tiered fee per product line.
- **Office Setup & Infrastructure ($C_{setup}$):** Lease deposit, interior refurbishment, signage, computer hardware, internet, and office furniture.
- **Working Capital Reserve ($W_{reserve}$):** Mandatory contingency reserve covering a minimum of 4 to 6 months of fixed operating overhead.

### 3.2. Monthly Operational Inputs
- **Fixed Monthly Operating Expenses ($OpEx_{fixed}$):** Office rent, utility bills, internet/telecom, accounting/admin retainers.
- **Personnel Headcount Expenses ($OpEx_{staff}$):** Base salaries for required personnel (minimum 1 dedicated salesperson) plus statutory benefits.
- **Variable Sales Expenses ($OpEx_{var}$):** Local travel allowance, promotional collateral, lead generation, client demonstration expenses.

### 3.3. Commercial & Sales Drivers
- **Product Price ($P_k$):** Net selling price per product $k$ (excluding applicable GST/sales tax).
- **Sales Velocity ($V_{k,m}$):** Anticipated unit sales per product $k$ in month $m$.
- **Revenue Sharing Ratio:** Franchisee percentage share ($S_{fee}$) vs. Franchisor percentage share ($S_{sor}$), where $S_{fee} + S_{sor} = 1.0$.
- **Annual Subscription Renewal Rate ($R_{renewal}$):** Percent of customers renewing annual software licenses (e.g., $1.0 - \text{Churn}$).

---

## 4. Methodology & Analytical Principles

1. **Decimal Precision:** All computations must strictly use 28-digit decimal precision (`Decimal`), avoiding standard floating-point representation.
2. **Gross vs. Net Revenue Integrity:** Taxes (such as 18% Indian GST) are statutory pass-through liabilities collected from customers and remitted to the government. Revenue sharing is calculated strictly on **Net Revenue** (exclusive of GST).
3. **Dual P&L Modeling:** The financial health of both parties is interdependent. A model where the franchisor captures large profits while the franchisee operates at a persistent deficit is commercially unviable.

---

## 5. Calculation Logic & Formula Engine

### 5.1. Initial Capital Outlay & Total Investment
$$\text{Total Initial Investment } (I_{total}) = F_{join} + C_{setup} + W_{reserve}$$
Where:
$$W_{reserve} = N_{runway} \cdot (OpEx_{fixed} + OpEx_{staff})$$
($N_{runway} \ge 4\text{ months}$).

### 5.2. Monthly Franchisee P&L Dynamics
For month $m$:
$$\text{Gross Customer Billings } (B_m) = \sum_{k=1}^{K} (V_{k,m} \cdot P_k) + \text{Renewal Billings } (R_m)$$
$$\text{Net Revenue } (NR_m) = \frac{B_m}{1 + r_{tax}} \quad (\text{if billings are tax-inclusive})$$
$$\text{Franchisee Gross Revenue } (GR_{fee,m}) = NR_m \cdot S_{fee}$$
$$\text{Franchisee Total Monthly OpEx } (OpEx_{fee,m}) = OpEx_{fixed} + OpEx_{staff} + OpEx_{var,m}$$
$$\text{Franchisee Operating Profit / EBITDA } (EBITDA_{fee,m}) = GR_{fee,m} - OpEx_{fee,m}$$

### 5.3. Break-Even Unit Volume Analysis
Break-even occurs in month $m$ when Franchisee Gross Revenue equals total monthly OpEx:
$$\sum_{k=1}^{K} (V_{BE,k} \cdot P_k \cdot S_{fee}) = OpEx_{fixed} + OpEx_{staff}$$
For a blended average net product price $\bar{P}$:
$$V_{BE} = \frac{OpEx_{fixed} + OpEx_{staff}}{\bar{P} \cdot S_{fee}}$$

### 5.4. Cumulative Cash Flow & Payback Period
$$\text{Cumulative Cash Flow } (CCF_M) = -I_{total} + \sum_{m=1}^{M} EBITDA_{fee,m}$$
The **Payback Period** ($M_{payback}$) is the earliest month $M$ where $CCF_M \ge 0$:
$$M_{payback} = \min \{ M \in [1, 36] \mid CCF_M \ge 0 \}$$

### 5.5. Return on Investment (ROI - 36 Month Horizon)
$$ROI_{36} = \frac{\sum_{m=1}^{36} EBITDA_{fee,m} - I_{total}}{I_{total}} \times 100\%$$

---

## 6. Expected Outputs
1. **Franchisee 36-Month Pro-Forma P&L Statement.**
2. **Franchisor Central Royalty & Product P&L Statement.**
3. **Monthly Cash Flow & Working Capital Trajectory.**
4. **Break-Even Unit Sales Target Schedule.**
5. **Sensitivity Matrix:** Table demonstrating EBITDA impact across variance in sales velocity ($\pm 25\%$) and price elasticity ($\pm 15\%$).

---

## 7. Risks and Limitations
- **Overestimating Early Sales Velocity:** Inexperienced salespeople typically require a 60 to 90-day ramp period before reaching normalized conversion rates.
- **Working Capital Depletion:** Franchisees who fail to maintain $W_{reserve}$ face insolvency before reaching Month 6 break-even.

---

## 8. Acceptance Criteria
- Calculated break-even unit sales must reconcile with monthly fixed overhead.
- All monetary totals must balance across monthly cash flow tables to within ₹0.01 precision.
- Scenarios must include conservative (downside), base, and optimistic parameters.

---

## 9. Example Application: TMK IT Solutions LLP
- **Illustrative Product:** School/College ERP at net price of ₹60,000 / school.
- **Franchise Split:** 40% Franchisee share = ₹24,000 per sale; 60% Franchisor share = ₹36,000 per sale.
- **Franchisee Monthly Fixed Overhead:** Office Rent (₹12,000) + 1 Salesperson Salary (₹18,000) + Misc utilities (₹5,000) = ₹35,000 / month.
- **Monthly Break-Even Sales:**
  $$V_{BE} = \frac{₹35,000}{₹24,000} \approx 1.46 \text{ ERP sales per month}$$
  *(A franchise owner closing 2 ERP deals per month generates ₹48,000 gross commission, clearing break-even with ₹13,000 positive monthly operating cash flow).*
