# Product Requirements Document (PRD) — Platform V0.1

## 1. Document Control
- **Product Name:** Franchise Business Modeling & Intelligence Platform
- **Version:** 0.1 (Bootstrap & Client Workspace Baseline)
- **Status:** Approved for Implementation
- **Authors:** Multidisciplinary Architecture & Engineering Team

---

## 2. Objective and Scope

Platform V0.1 establishes a production-grade, Git-based modeling and intelligence repository that empowers research and financial analysts to:
1. Conduct structured franchise market research across industries.
2. Formulate client-specific franchise strategies across FOFO, FOCO, COCO, and hybrid models.
3. Compute decimal-safe financial models with configurable revenue sharing, break-even analysis, and cash flow projections.
4. Automatically compile editable, linked-formula Excel workbooks and PowerPoint pitch decks.
5. Provide a fully structured, operational workspace for the inaugural client: **TMK IT Solutions LLP**.

---

## 3. User Personas

| Persona | Role | Primary Workflows |
|---|---|---|
| **Analyst 1 (Strategy & Documentation)** | Market & Business Strategy | Competitor research, territory strategy, legal drafting, pitch deck authoring, operations handbooks. |
| **Analyst 2 (Finance & Analytics)** | Financial & Quantitative Modeling | Unit economics, Decimal financial calculator, assumptions register, break-even & scenario analysis, Excel generator. |
| **Franchise Practice Lead** | Principal Consultant / Reviewer | Quality gating, review of management decisions, approval of commercial assumptions, client alignment. |
| **Enterprise Client Executive** | Client Sponsor (e.g., TMK Leadership) | Reviewing franchise prospectuses, approving revenue-sharing structures, signing off on unit rollout targets. |

---

## 4. Functional Requirements

### 4.1. Core Business Frameworks (`frameworks/`)
- **FR-01 Archetype Coverage:** Must document and provide RACI matrices for 10 franchise archetypes: FOFO, FOCO, COCO, COFO, Master Franchise, Area Development, Multi-Unit, Product Distribution, Sales Franchise, and Hybrid.
- **FR-02 Financial Feasibility:** Must specify calculation mechanics for capital expenditure (CapEx), working capital runway, monthly operating expenditure (OpEx), franchisee/franchisor P&L, unit economics, payback period, and internal rate of return (IRR).
- **FR-03 Revenue Sharing Flexibility:** Must support configurable splits across joining fees, license sales, implementation fees, recurring subscriptions, and infrastructure deductions.
- **FR-04 Territory Intelligence:** Must define territory prioritization heuristics based on customer density, taluka/district demographic scoring, and conflict mitigation.
- **FR-05 Investor Protection:** Must establish disclosure frameworks covering realistic earnings, operational risk disclosures, and fair exit mechanics.

### 4.2. Financial Modeling Engine (`tools/financial-modeling/`)
- **FR-06 Precision Math:** All currency calculations must execute via Python `decimal.Decimal` to avoid floating-point drift.
- **FR-07 Formula-Driven Spreadsheets:** The Excel generator must emit native upper-case Excel formulas (`=SUM()`, `=IF()`, `=B4*C4`) so non-technical analysts can inspect and manipulate assumptions dynamically.
- **FR-08 Scenario Analysis:** Must generate 3 distinct operating scenarios: Conservative, Base, and Optimistic.
- **FR-09 Recurring Economics:** Must model customer churn rate, subscription renewal commissions, and cumulative customer lifetime value.

### 4.3. Initial Client Workspace (`clients/tmk-it-solutions/`)
- **FR-10 Client Profile:** Complete overview of TMK IT Solutions LLP (Software & IT Services, FOFO model, India target market).
- **FR-11 Six Software Products:** Dedicated profiles for School/College ERP, Invoicing App+Web, OMR Software, Property Management ERP, DevOps Automation, and Sales CRM.
- **FR-12 Commercial Terms:** Proposed ₹25,000 promotional and ₹50,000 regular franchise joining fees; 40% franchisee / 60% franchisor split parameterized and modeled.
- **FR-13 Pitch & Marketing Package:** Presentation outline, generated PPTX deck, franchise brochure, prospectus, FAQ, and infographic specifications.
- **FR-14 Legal Drafts:** Non-final working drafts for Franchise Agreement, Revenue Sharing Policy, Territory Policy, Renewal Policy, Termination Policy, NDA, and Brand Usage Policy.

### 4.4. Analyst Operations (`analyst-workspace/`)
- **FR-15 Role Demarcation:** Distinct backlogs and responsibilities for Analyst 1 and Analyst 2.
- **FR-16 Registers:** Operational registers for Research Evidence, Assumptions, Risks, and Management Decisions.
- **FR-17 Task Tracking:** Centralized task board with task ID, description, owner, status, and acceptance criteria.

---

## 5. Non-Functional Requirements

- **NFR-01 Extensibility:** Adding a new client must require zero changes to `frameworks/`, `tools/`, or `schemas/`.
- **NFR-02 Auditability:** All financial parameters must be traceable to `assumptions-register.md`.
- **NFR-03 Test Coverage:** Calculation engine and schema compliance must maintain 100% automated test coverage in `tests/`.
- **NFR-04 Zero Data Leakage:** Client commercial secrets must remain strictly confined to `clients/<client-name>/`.
