# Franchise Performance Analytics & KPI Framework

## 1. Purpose
This framework defines the formal measurement model, metric taxonomy, reporting frequencies, and analytical dashboard specifications for monitoring franchise network health, unit economics, commercial velocity, and operational risk.

---

## 2. Master KPI Specification Catalog (13 Core KPIs)

### KPI 1: Franchise Recruitment Velocity (FRV)
- **Definition:** The rate at which qualified franchise partners are signed and onboarded relative to target quotas.
- **Formula:** $FRV = \frac{\text{Signed Franchise Contracts in Period}}{\text{Target Quota for Period}} \times 100\%$
- **Required Data:** New signed contracts count, regional target expansion plan.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Head of Franchise Expansion.
- **Interpretation:** $> 100\%$ indicates strong market appeal; $< 75\%$ signals pricing resistance, weak pitch messaging, or inadequate lead generation.
- **Limitations:** Measures deal volume only; does not reflect partner quality or balance sheet strength.

### KPI 2: Franchise Activation Time (FAT)
- **Definition:** The number of calendar days elapsed between contract signing and the first customer demonstration conducted.
- **Formula:** $FAT = \text{Date of First Completed Customer Demo} - \text{Date of Agreement Execution}$
- **Required Data:** Agreement signing timestamp, central CRM demo completion log.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Onboarding & Operations Lead.
- **Interpretation:** Target $\le 30$ days. Prolonged FAT ($> 45$ days) indicates delays in office setup or lagging salesperson training.
- **Limitations:** Does not measure demo quality or likelihood of deal closure.

### KPI 3: Territory Penetration & Coverage Ratio (TPCR)
- **Definition:** Proportion of designated administrative territories (e.g., Talukas/Districts) with an active operating franchisee.
- **Formula:** $TPCR = \frac{\text{Count of Active Franchise Territories}}{\text{Total Qualified Addressable Territories}} \times 100\%$
- **Required Data:** Active territory registry, master territory database.
- **Reporting Frequency:** Quarterly.
- **Business Owner:** Strategy & Territory Architect.
- **Interpretation:** Measures expansion footprint and white-space opportunity remaining.
- **Limitations:** A territory is counted as covered even if the franchisee is under-indexing on market share.

### KPI 4: Product-Wise Sales Mix (PWSM)
- **Definition:** Breakdown of total sales volume and revenue contributed by each distinct product vertical.
- **Formula:** $PWSM_k = \frac{\text{Net Revenue from Product } k}{\text{Total Network Net Revenue}} \times 100\%$
- **Required Data:** Product-level invoice logs.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Product Practice Lead & Analyst 2.
- **Interpretation:** Identifies product dependency and cross-selling effectiveness.
- **Limitations:** Heavy concentration in one product may conceal weakness in the remaining product suite.

### KPI 5: Sales Conversion Efficiency (SCE)
- **Definition:** The percentage of qualified customer demonstrations that convert into paying contracts.
- **Formula:** $SCE = \frac{\text{Count of Paid Customer Invoices}}{\text{Count of Qualified Product Demonstrations Conducted}} \times 100\%$
- **Required Data:** CRM demonstration logs, central billing receipts.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Sales Enablement Lead.
- **Interpretation:** Industry benchmark for B2B software is $15\% - 25\%$. Lower values indicate poor sales presentation skills or product-price mismatch.
- **Limitations:** Can be artificially inflated if salespeople only log late-stage prospects as demos.

### KPI 6: Effective Revenue Sharing Yield (ERSY)
- **Definition:** The realized net revenue retained by the franchisor after all franchisee commissions, deductions, and tax pass-throughs.
- **Formula:** $ERSY = \frac{\text{Franchisor Retained Net Revenue}}{\text{Total Customer Invoiced Net Revenue}} \times 100\%$
- **Required Data:** Monthly commission settlement statements, net invoicing records.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Chief Financial Officer / Lead Financial Analyst.
- **Interpretation:** Verifies that contractual splits (e.g., 60%) are being achieved after discounts and implementation offsets.
- **Limitations:** Blended metric that may obscure individual contract concessions.

### KPI 7: Franchisee Unit Net Profit Margin (FNPM)
- **Definition:** Average net operating profit margin achieved by a local franchise office after deducting all local fixed and variable overhead.
- **Formula:** $FNPM = \frac{\text{Franchisee Net EBITDA}}{\text{Franchisee Gross Commission Revenue}} \times 100\%$
- **Required Data:** Monthly franchisee operational expense reports, commission statements.
- **Reporting Frequency:** Monthly / Quarterly.
- **Business Owner:** Franchise Performance Analyst (Analyst 2).
- **Interpretation:** Target $\ge 25\%$. Persistently low or negative margins indicate franchisee distress and churn risk.
- **Limitations:** Depends on honest reporting of local operational expenses by franchisees.

### KPI 8: Franchisor Central Gross Margin (FCGM)
- **Definition:** Franchisor gross profit margin from franchise operations after paying franchisee commissions, hosting costs, and customer onboarding expenses.
- **Formula:** $FCGM = \frac{\text{Franchisor Net Revenue} - (\text{Cloud Hosting} + \text{Central Support Delivery})}{\text{Franchisor Net Revenue}} \times 100\%$
- **Required Data:** Central cloud infrastructure bills, support staffing costs, franchisor revenue ledger.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Franchisor Finance Director.
- **Interpretation:** High gross margin ($> 70\%$) confirms asset-light leverage of the software franchise model.
- **Limitations:** Excludes core software R&D engineering overhead.

### KPI 9: Annual Subscription Renewal Rate (ASRR)
- **Definition:** Percentage of existing software subscription contracts successfully renewed at the end of their 12-month term.
- **Formula:** $ASRR = \frac{\text{Renewed Annual Contracts}}{\text{Contracts Expiring in Period}} \times 100\%$
- **Required Data:** Subscription renewal register, customer expiration dates.
- **Reporting Frequency:** Monthly / Annually.
- **Business Owner:** Customer Success & Renewal Operations Lead.
- **Interpretation:** Target $\ge 85\%$. Renewal health drives the long-term compounding enterprise value of the platform.
- **Limitations:** Lagging indicator; churn occurs months before formal expiration.

### KPI 10: Customer Logo Churn Rate (CLCR)
- **Definition:** Percentage of customers discontinuing service or failing to renew over a given period.
- **Formula:** $CLCR = \frac{\text{Cancelled or Non-Renewed Accounts in Period}}{\text{Active Accounts at Start of Period}} \times 100\%$
- **Required Data:** Cancellation tickets, uncollected renewal notices.
- **Reporting Frequency:** Monthly / Quarterly.
- **Business Owner:** Product Practice Lead.
- **Interpretation:** High churn ($> 15\%$ annually) indicates product usability issues, software bugs, or lack of local customer relationship maintenance.
- **Limitations:** Does not measure revenue expansion or contraction within continuing accounts.

### KPI 11: Franchisee Composite Performance Score (FCPS)
- **Definition:** Weighted multi-factor index rating an individual franchisee's overall commercial, operational, and compliance contribution.
- **Formula:** $FCPS = 0.40 \cdot \left(\frac{\text{Sales}}{\text{Quota}}\right) + 0.25 \cdot \text{Renewal Rate} + 0.20 \cdot \text{Audit Score} + 0.15 \cdot \text{CRM Compliance}$
- **Required Data:** Sales logs, renewal data, quarterly audit checklist, CRM logging activity.
- **Reporting Frequency:** Quarterly.
- **Business Owner:** Franchise Operations Manager.
- **Interpretation:** Tier 1 ($\ge 90$), Tier 2 ($75 - 89$), Tier 3 ($< 75$). Governs territory expansion eligibility or cure notices.
- **Limitations:** Subject to quarterly audit subjectivity.

### KPI 12: Network Risk Exposure Index (NREI)
- **Definition:** Aggregated financial and operational risk rating across the entire active franchise network.
- **Formula:** $NREI = \frac{\sum_{i=1}^{U} \text{Risk Exposure Score}_i}{U}$
- **Required Data:** Unit health indices, risk register scores.
- **Reporting Frequency:** Monthly.
- **Business Owner:** Risk Management Committee.
- **Interpretation:** An increasing trend indicates systemic vulnerability (e.g., widespread competitor discounting or salesperson attrition).
- **Limitations:** Can be distorted by a few severely distressed units in an otherwise healthy network.

### KPI 13: Territory White-Space Expansion Index (TWSEI)
- **Definition:** Quantitative ranking of unassigned territories showing high market potential relative to low competitive presence.
- **Formula:** $TWSEI_j = \frac{\text{Addressable Institution Density}_j \times \text{Regional Economic Wealth Index}_j}{\text{Incumbent Competitor Presence}_j + 1}$
- **Required Data:** Territory intelligence database, economic indices, competitor mapping.
- **Reporting Frequency:** Bi-Annually.
- **Business Owner:** Franchise Expansion Lead & Analyst 1.
- **Interpretation:** Directly dictates the target list for subsequent franchise recruitment campaigns.
- **Limitations:** High-scoring territories may still face unforeseen local cultural or regulatory barriers.

---

## 3. Executive Dashboard Mockup Specifications

### Dashboard 1: Executive Network Overview
- **Header:** Total Active Units, Network Net Revenue YTD, Average Franchisee EBITDA, Network Renewal Rate.
- **Charts:**
  1. *Territory Coverage Map:* Geographic density of active, in-onboarding, and open target talukas.
  2. *Monthly Billings Breakdown:* Stacked bar chart showing Franchisee Commission vs. Franchisor Retained Revenue vs. GST.
  3. *Product Mix Donut:* Percentage contribution of each of the 6 software products.

### Dashboard 2: Franchisee Unit Economics & Health
- **Header:** Units in Green ($UHI \ge 0.85$), Units on Watchlist ($0.60 \le UHI < 0.85$), Units in Remediation ($UHI < 0.60$).
- **Charts:**
  1. *Unit Payback Trajectory:* Cumulative cash flow curves across operating units compared against base model.
  2. *Sales Conversion Funnel:* Leads -> Qualified Demos -> Quotes -> Won Deals.
  3. *Unit P&L Scatter Plot:* Monthly Fixed Costs vs. Monthly Commission Revenue (identifying break-even frontier).
