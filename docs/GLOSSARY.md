# Comprehensive Franchise & Platform Glossary

Welcome to the centralized terminology reference for the **Franchise Business Modeling & Intelligence Platform**. This glossary establishes precise, unambiguous definitions across franchise business models, financial mathematics, legal & regulatory compliance, territorial governance, and platform architecture.

All analysts, agents, and contributors must use these terms consistently across documentation, financial models, client proposals, and code implementations.

---

## Table of Contents
- [A](#a)
- [B](#b)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
- [H](#h)
- [I](#i)
- [J](#j)
- [K](#k)
- [L](#l)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [Q](#q)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)
- [W](#w)

---

## A

### Annual Contract Value (ACV)
The annualized revenue generated from a customer contract, excluding one-time onboarding, hardware, or implementation fees. In subscription software modeling, ACV drives recurring commission pools.

### Annual Recurring Revenue (ARR)
The predictable recurring revenue component generated from software subscriptions, maintenance retainers, or annual service renewals normalized over a 12-month period.

### Area Development Agreement
A franchising agreement granting an operator the exclusive right and contractual obligation to establish multiple franchise units within a defined geographic territory over a scheduled development timeframe.

### Assumptions Register
A centralized repository document ([assumptions-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/assumptions-register.md)) cataloging every empirical parameter, financial rate, driver, and growth hypothesis. Every assumption must be categorized as `[EMPIRICAL]`, `[WORKING HYPOTHESIS]`, `[PROPOSED]`, or `[CLIENT MANDATED]`.

---

## B

### Benchmark Target
A defined minimum operational or sales threshold (e.g., minimum software license billings per quarter) required of a franchisee to maintain active territory exclusivity or renewal eligibility.

### Billable Rate
The standard commercial price charged to enterprise clients for professional software customization, deployment consulting, or support labor.

### Break-Even (Unit / Revenue)
- **Unit Break-Even:** The exact quantity of product or service sales required in a given time period to generate a total gross margin equal to all fixed operating overheads.
- **Revenue Break-Even:** The monetary sales volume required to yield zero operating profit/loss:
  $$\text{Break-Even Revenue} = \frac{\text{Fixed Costs}}{\text{Contribution Margin Ratio}}$$

---

## C

### Cannibalization
A condition where opening a new franchise territory reduces sales, customer traffic, or margins of an adjacent existing franchise unit.

### Capital Expenditure (CapEx)
Upfront capital invested by a franchisee to establish an operational facility. Includes lease security deposits, office furniture, IT hardware, corporate branding/signage, and initial statutory registrations.

### Client Workspace
An isolated directory located in `clients/<client-slug>/` housing confidential corporate data, product catalogs, customized financial assumptions, contracts, and deliverables for an individual tenant.

### COCO (Company Owned, Company Operated)
A franchise model where the franchisor provides 100% of the initial capital and directly operates the unit via corporate staff. Primarily used for flagship innovation centers and pilot validation.

### Contribution Margin
Revenue minus variable direct costs associated with delivering that specific product or contract. Represents the incremental cash contributed toward covering fixed operating expenses.

### Customer Acquisition Cost (CAC)
The cumulative marketing, lead generation, sales travel, and demonstration expenditure incurred to acquire a single paying client.

---

## D

### Data Contract
A formal specification codified as a JSON Schema (located in `schemas/`) defining mandatory fields, data types, and structural constraints for business entities such as client profiles, products, territories, and financial parameters.

### Deal Registration Lock
A governance mechanism in multi-partner channels where a franchisee logs an enterprise lead in the franchisor's CRM. If validated, the franchisee receives exclusive sales protection on that prospect for a designated period (standard: 90 days), preventing franchisor direct encroachment or multi-franchisee bid wars.

### Decimal-Safe Arithmetic
The mandatory software practice of executing all currency calculations using arbitrary-precision fixed-point math (`decimal.Decimal` in Python, quantizing to 2 decimal places with `ROUND_HALF_UP`) to prevent floating-point rounding discrepancies.

### Dual-Analyst Review
The mandatory governance gate where deliverables authored by **Analyst 1 (Strategy/Documentation)** must be vetted by **Analyst 2 (Finance/Analytics)**, and mathematical models developed by Analyst 2 must be audited by Analyst 1 prior to management sign-off.

---

## E

### Earnings Claim (Item 19 / Representation)
Any explicit or implied statement regarding historical or prospective financial performance, sales revenue, gross margin, or net profit made to prospective franchisees. Deceptive or unsubstantiated earnings claims violate consumer protection regulations.

### Encroachment
The unauthorized or contractually disputed infringement by a franchisor or neighboring franchisee on an existing franchisee's defined protected territory.

### Evidence Register
The empirical audit ledger ([research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md)) tracing every market size, competitor quote, pricing point, and economic metric back to verified citations, interviews, and official documents.

---

## F

### Fee Segregation
The architectural separation between one-time franchise onboarding/joining fees and ongoing recurring royalties/revenue distributions.

### FICO (Franchise Invested, Company Operated)
A hybrid franchise model where an investor provides upfront capital expenditure, while the franchisor manages daily operational execution, sharing operating profits after corporate management fees.

### Financial Scenario Modeling
The process of evaluating economic feasibility across three standardized operational baselines:
- **Conservative (Stress-Test):** Depressed volumes (-30%), extended sales cycles (+50%), higher operating costs.
- **Base (Most Likely):** Empirically justified adoption rates and verified pricing.
- **Optimistic (High-Growth):** Accelerated market penetration and rapid cross-sell expansion.

### FOCO (Franchise Owned, Company Operated)
A model where the franchisee provides the physical facility, lease, and setup capital, while the franchisor's centralized operational team directs staff, sales, and service delivery, distributing net earnings per contract.

### FOFO (Franchise Owned, Franchise Operated)
The predominant decentralized franchise model where the franchisee funds 100% of the setup capital and manages daily operations, customer acquisition, and local support under franchisor guidelines, brand standards, and software licensing frameworks.

### Franchise Disclosure Document (FDD)
A comprehensive pre-sale disclosure instrument detailing franchisor leadership history, litigation, fees, territory boundaries, audited financial statements, and operating requirements provided to prospective franchisees prior to contract execution.

---

## G

### Goods and Services Tax (GST)
A comprehensive indirect consumption tax levied in India. In franchise operations, standard business-to-business (B2B) software licenses, joining fees, and royalty fees carry 18% GST. GST is a pass-through tax and must be segregated from distributable net revenue.

### Gross Margin
Gross revenue minus direct cost of goods or services sold (COGS), expressed as a monetary figure or percentage.

### Gross Revenue
The total invoiced billing amount to end customers before any deduction of taxes, vendor fees, or partner splits.

---

## H

### Hurdles / High-Water Mark
Pre-agreed financial milestones (such as cumulative sales volume or revenue thresholds) that trigger increased commission tiers or performance bonuses.

---

## I

### Internal Rate of Return (IRR)
The discount rate that equates the net present value (NPV) of all future operating cash inflows to the initial capital outlay of establishing the franchise unit.

### Item 19
The standardized section within a Franchise Disclosure Document governing financial performance representations and earnings claims.

---

## J

### Joining Fee (Initial Franchise Fee)
A non-refundable upfront fee paid by the franchisee upon signing the franchise agreement. Covers territorial reservation, initial training, onboarding collateral, software enablement, and brand onboarding.

---

## K

### Key Performance Indicator (KPI)
A quantifiable metric utilized to monitor franchise unit health (e.g., Lead Conversion Rate, Monthly Recurring Revenue, Average Resolution Time, Audit Compliance Score).

---

## L

### Lead Pipeline Velocity
A commercial sales velocity metric measuring how rapidly enterprise prospects move through sales stages from initial lead qualification to signed contract.

### Liquid Capital Requirement
The minimum unencumbered cash balance a prospective franchisee must possess to cover setup CapEx plus 6 months of operating cash burn without relying on immediate customer revenues.

---

## M

### Master Franchise Agreement
A contract conferring exclusive territorial rights across a major regional territory (state or country), authorizing the master franchisee to recruit sub-franchisees, collect fees, and share royalties with the primary franchisor.

### Monthly Recurring Revenue (MRR)
The normalized monthly subscription revenue recognized from active SaaS software clients.

---

## N

### Net Present Value (NPV)
The present value of anticipated future net cash inflows discounted at the franchisee's cost of capital, minus the initial capital expenditure.

### Net Realized Revenue
The net distributable commercial revenue pool computed as Gross Billing minus pass-through statutory taxes (e.g., GST), third-party transaction fees, or direct client hardware disbursements.

---

## O

### Operating Expenditure (OpEx)
Ongoing recurring expenses incurred to maintain franchise operations, including office rent, staff salaries, internet/telecom, utilities, marketing campaigns, and travel.

### Operations Manual (SOP Manual)
The comprehensive operational playbook provided to franchisees detailing standard operating procedures, sales methodologies, brand identity compliance, customer support escalation, and governance protocols.

---

## P

### Parametric Modeling Engine
A computational system (such as the Python calculation engine in `tools/financial-modeling/`) driven purely by parameter files (`assumptions.json`), ensuring zero hardcoded business logic or client-specific numbers in reusable codebase modules.

### Payback Period (Simple / Discounted)
The timeframe (in months or years) required for cumulative operational cash inflows to fully recoup the initial setup CapEx and joining fees.

---

## Q

### Quality Assurance (QA) Gate
An enforced verification checkpoint ensuring deliverables meet JSON Schema specifications, mathematical balance checks, relative link validity, and peer approval before release.

---

## R

### Return on Investment (ROI)
The net financial gain generated by a franchise unit relative to the initial capital invested, expressed as an annualized percentage:
$$\text{ROI} = \left(\frac{\text{Cumulative Net Profit}}{\text{Total Initial Investment}}\right) \times 100$$

### Revenue Sharing Split
The contractual percentage breakdown determining how Net Realized Revenue from client billings is partitioned between the Franchisee and Franchisor (e.g., 40% Franchisee : 60% Franchisor).

### Royalty Fee
An ongoing periodic payment (percentage of revenue or fixed monthly fee) paid by the franchisee to the franchisor for continuous brand usage, software updates, centralized infrastructure, and ongoing coaching.

---

## S

### Service Level Agreement (SLA)
Contractually defined performance commitments governing support response times, software uptime, and resolution escalations between franchisor, franchisee, and end clients.

### Software as a Service (SaaS)
A software licensing and delivery model in which software is centrally hosted and accessed via web interfaces on a subscription or recurring retainer basis.

---

## T

### Taluka / Tehsil
The primary sub-district administrative division in India, utilized by the platform as the foundational geographic boundary unit for territorial modeling, demographic scoring, and exclusivity mapping.

### Tax Deduction at Source (TDS)
A statutory direct tax withholding requirement under Indian tax law whereby the payer deducts tax before remitting commissions or professional fees to the recipient.

### Tenant Isolation
The foundational architectural principle ensuring that client-specific business rules, financial figures, customer names, and proprietary documents remain strictly encapsulated within `clients/<client-slug>/` without contaminating the generic platform modules.

### Tier-2 / Tier-3 / Tier-4 Cities
Indian urban and commercial classification hierarchy based on population density, commercial activity, and municipal infrastructure, heavily informing territory market potential and operating cost assumptions.

---

## U

### Unit Economics
The direct revenues and costs associated with delivering a single unit of software product or service contract, highlighting gross margin viability prior to overhead absorption.

### Unit Franchise
A single-location franchise agreement granting an operator rights to own and operate one specific franchise office within a delineated territory.

---

## V

### Variable Costs
Operational and delivery costs that fluctuate directly in proportion to sales or service volume (e.g., sales commissions, cloud compute scaling costs, third-party payment gateway fees).

---

## W

### Working Capital Reserve
The mandatory liquid cash contingency fund set aside by a franchisee to cover payroll, rent, and overhead during the initial operational ramp-up phase before monthly cash collections reach break-even.

---

## Quick Reference Summary Table

| Term | Category | Brief Definition |
|---|---|---|
| **FOFO** | Franchise Model | Franchise Owned, Franchise Operated; decentralized capital and operations. |
| **FOCO** | Franchise Model | Franchise Owned, Company Operated; investor funds CapEx, franchisor runs ops. |
| **COCO** | Franchise Model | Company Owned, Company Operated; corporate flagship unit. |
| **Net Realized Revenue** | Financial | Gross customer billing minus pass-through statutory taxes (GST). |
| **Revenue Split** | Financial | Contractual partition of Net Realized Revenue (e.g., 40:60). |
| **CapEx** | Financial | Upfront setup expenditure (office deposit, computers, signage). |
| **OpEx** | Financial | Recurring monthly operational costs (salaries, rent, utilities). |
| **Taluka** | Territorial | Official Indian sub-district administrative territory unit. |
| **Deal Registration Lock**| Commercial | 90-day exclusive sales hold on validated enterprise prospects in CRM. |
| **Tenant Isolation** | Platform | Strict segregation between reusable engines and individual client workspaces. |
| **Dual-Analyst Review** | Quality | Peer review cross-check between Strategy (Analyst 1) and Finance (Analyst 2). |

---

> [!TIP]
> For detailed instructions on how to use these terms within role workflows, refer to the [Analyst 1 Strategy Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md) and the [Analyst 2 Finance Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md).
