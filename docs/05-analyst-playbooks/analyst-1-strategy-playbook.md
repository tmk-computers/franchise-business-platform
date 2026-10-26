# Analyst 1 Playbook: Business Strategy, Research & Documentation

Welcome to the operational execution manual for **Analyst 1 (Business Strategy, Market Research & Commercial Documentation)**. 

As Analyst 1, you own the qualitative, strategic, territorial, operational, and commercial deliverables of the platform. You transform enterprise products into viable franchise offerings, synthesize market intelligence, author institutional documentation, design governance policies, and ensure every empirical claim is grounded in verified evidence.

---

## Table of Contents
1. [Core Responsibilities & Role Boundaries](#1-core-responsibilities--role-boundaries)
2. [Research Evidence Management & Assumptions Tagging](#2-research-evidence-management--assumptions-tagging)
3. [Market Research & Opportunity Sizing Workflow](#3-market-research--opportunity-sizing-workflow)
4. [Franchise Business Model Design & RACI Architecture](#4-franchise-business-model-design--raci-architecture)
5. [Competitive Analysis & Benchmarking](#5-competitive-analysis--benchmarking)
6. [Territory Research & Geographic Scoring](#6-territory-research--geographic-scoring)
7. [Franchise Pitch Materials & Pitch Deck Generation](#7-franchise-pitch-materials--pitch-deck-generation)
8. [Product Demonstration Documentation & Sales Kits](#8-product-demonstration-documentation--sales-kits)
9. [Brochures, Prospectuses & Investor FAQs](#9-brochures-prospectuses--investor-faqs)
10. [Franchise Operations Manuals & Support SLAs](#10-franchise-operations-manuals--support-slas)
11. [Draft Policies & Franchise Agreements](#11-draft-policies--franchise-agreements)
12. [Management Presentations & Executive Decision Papers](#12-management-presentations--executive-decision-papers)
13. [Franchise Launch Readiness Execution & Workstream Governance](#13-franchise-launch-readiness-execution--workstream-governance)
14. [Analyst 1 Quality Checklist & Peer Review Hand-Off](#14-analyst-1-quality-checklist--peer-review-hand-off)

---

## 1. Core Responsibilities & Role Boundaries

### In-Scope for Analyst 1
- **Qualitative Strategy:** Industry research, competitor benchmarking, SWOT analyses, and archetype evaluations.
- **Commercial Documentation:** Franchise agreements, SOP handbooks, recruitment brochures, pitch decks, investor prospectuses, and sales playbooks.
- **Territory Intelligence:** Sub-district (taluka/tehsil) market potential analysis, exclusivity definitions, and anti-encroachment rules.
- **Evidence Integrity:** Maintaining [research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md).
- **Cross-Review:** Auditing Analyst 2's quantitative models for contractual and strategic feasibility.

### Out-of-Scope (Handled by Analyst 2)
- Authoring Python financial calculation engines (`calculator.py`).
- Calculating formulaic 36-month cash flows, break-even unit sales, or payback timelines.
- Generating openpyxl Excel workbooks.

---

## 2. Research Evidence Management & Assumptions Tagging

Every empirical number, competitor quote, pricing benchmark, or market statistic cited in Analyst 1 deliverables must be traceable to the centralized evidence ledger. Zero unverified claims are permitted.

### Step-by-Step Evidence Workflow
1. **Source Discovery:** Gather market reports, official government census data, trade publications, or direct competitor filings.
2. **Assign Evidence Identifier:** Open [analyst-workspace/research-methodology/research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md).
3. **Log the Entry:** Append a new record adhering to `schemas/research-source.schema.json`:
   ```markdown
   | Source ID | Claim / Fact | Primary Source | Date Verified | Credibility Tier |
   |---|---|---|---|---|
   | `EVD-MKT-004` | MSME SaaS adoption in Tier-2 Indian cities growing at 22% CAGR | Nasscom SME Tech Report 2025 | 2026-03-15 | Tier 1 (Institutional) |
   ```
4. **Label Assumptions:** If an exact figure is unavailable, log it in [analyst-workspace/research-methodology/assumptions-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/assumptions-register.md) and tag the text explicitly as `[PROPOSED]`, `[WORKING HYPOTHESIS]`, or `[ESTIMATED]`.

---

## 3. Market Research & Opportunity Sizing Workflow

### Purpose & Context
Quantify market demand, Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for the client's franchise offerings.

### Step-by-Step Deliverable Recipe
1. **Review Framework:** Read [frameworks/market-research/market-research-methodology.md](file:///d:/company/products/franchise-business-platform/frameworks/market-research/market-research-methodology.md).
2. **Select Template:** Copy [templates/market-research/market-research-report.template.md](file:///d:/company/products/franchise-business-platform/templates/market-research/market-research-report.template.md).
3. **Target Output Path:** Save draft as `clients/<client-slug>/research/market-demand-brief.md`.
4. **Execute Research Steps:**
   - Define customer segments (e.g., MSMEs, private schools, diagnostic clinics, mid-market retail).
   - Calculate TAM (top-down national spending) and SAM (regional addressable segment).
   - Formulate realistic SOM based on conservative 1%–3% territory market share.
5. **Cross-Check:** Ensure all market growth rates cite an `EVD-*` identifier.
6. **Peer Review:** Request Analyst 2 review for quantitative sizing consistency.

---

## 4. Franchise Business Model Design & RACI Architecture

### Purpose & Context
Structure the legal, operational, and commercial relationship between franchisor and franchisee.

### Step-by-Step Deliverable Recipe
1. **Review Framework:** Read [frameworks/franchise-model-design/franchise-archetypes-comparison.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-model-design/franchise-archetypes-comparison.md).
2. **Examine Archetypes:** Evaluate whether FOFO, FOCO, COCO, or Master Franchise fits the client's unit economics and operational capability.
3. **Author Specification:** Save draft as `clients/<client-slug>/franchise-model/<archetype>-model-specification.md`.
4. **Construct RACI Matrix:** Build an exhaustive 25+ row RACI table across:
   - Corporate identity, trademark licensing, software engineering, and cloud infrastructure.
   - Local facility leasing, hardware setup, local sales marketing, and client presentations.
   - Invoicing, tax withholding, collections, Tier-1 support, and Tier-2 engineering escalations.
5. **Review Gate:** Submit to Analyst 2 to verify that operational responsibilities align with the cost line items in `assumptions.json`.

---

## 5. Competitive Analysis & Benchmarking

### Purpose & Context
Benchmark the franchisor's offering against existing direct and indirect software competitors, franchised distribution networks, and local IT service agencies.

### Step-by-Step Deliverable Recipe
1. **Review Framework:** Consult Section 4 of `frameworks/market-research/market-research-methodology.md`.
2. **Gather Competitor Profiles:** Identify 3–5 key industry players (e.g., Tally, Marg ERP, Zoho, localized software agencies).
3. **Target Output Path:** Save draft as `clients/<client-slug>/research/competitive-analysis-brief.md`.
4. **Analyze Dimensions:**
   - Pricing models (upfront purchase vs. annual SaaS renewal).
   - Channel margins and partner commission percentages.
   - Implementation complexity and local deployment support.
   - Customer lock-in and switching costs.
5. **Construct Positioning Matrix:** Highlight the client's competitive differentiators (e.g., unified suite, local touchpoint, affordable entry tier).

---

## 6. Territory Research & Geographic Scoring

### Purpose & Context
Define territorial allocation methodology to prevent channel cannibalization and provide franchisees with viable commercial catchments.

### Step-by-Step Deliverable Recipe
1. **Review Framework:** Read [frameworks/territory-intelligence/territory-intelligence-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/territory-intelligence/territory-intelligence-framework.md).
2. **Select Boundary Unit:** For India, utilize official administrative Sub-Districts (Talukas / Tehsils) or District Municipalities.
3. **Target Output Path:** Save draft as `clients/<client-slug>/research/territory-strategy.md`.
4. **Implement Territory Scoring (0–100 scale):**
   - Commercial MSME establishment density (30% weight).
   - Educational & healthcare institution count (25% weight).
   - Banking & connectivity infrastructure (20% weight).
   - Competitive saturation / lack of direct competitors (25% weight).
5. **Codify Encroachment Rules:** Specify the 90-day Deal Registration Lock and minimum quarterly license benchmark targets.

---

## 7. Franchise Pitch Materials & Pitch Deck Generation

### Purpose & Context
Create compelling, institutional-grade investor presentation assets for prospective franchise partners.

### Step-by-Step Deliverable Recipe
1. **Review Template:** Inspect [templates/investor-presentations/pitch-deck-outline.template.md](file:///d:/company/products/franchise-business-platform/templates/investor-presentations/pitch-deck-outline.template.md).
2. **Author Narrative Outline:** Save as `clients/<client-slug>/presentations/franchise-pitch-deck-outline.md`.
3. **Execute Automated Presentation Generator:**
   Run the repository's verified python-pptx generation script:
   ```bash
   python tools/document-generation/generate_pitch_deck.py --client tmk-it-solutions
   ```
   *(Confirm generated `.pptx` file appears in `clients/<client-slug>/presentations/`)*.
4. **Mandatory Disclaimer Insertion:** Ensure Slide 2 or concluding slide contains the statutory non-guarantee earnings disclaimer:
   > "Illustrative scenarios only. Actual financial performance depends on local market execution, operational diligence, and economic conditions. No guaranteed earnings are represented."

---

## 8. Product Demonstration Documentation & Sales Kits

### Purpose & Context
Provide franchisees with standardized software demonstration scripts, client evaluation sheets, and technical objections handling guides.

### Step-by-Step Deliverable Recipe
1. **Review Template:** Inspect [templates/product-demonstrations/product-demo-guide.template.md](file:///d:/company/products/franchise-business-platform/templates/product-demonstrations/product-demo-guide.template.md).
2. **Target Output Path:** Save as `clients/<client-slug>/sales-marketing/product-demo-guide.md`.
3. **Structure 5-Step Demo Script:**
   - Step 1: Client Discovery & Pain Point Mapping (10 mins).
   - Step 2: Live System Navigation & High-Value Workflows (20 mins).
   - Step 3: ROI & Cost Savings Demonstration (10 mins).
   - Step 4: Objection Handling (Security, Data Migration, Pricing) (10 mins).
   - Step 5: Trial Onboarding & Next Steps (10 mins).

---

## 9. Brochures, Prospectuses & Investor FAQs

### Purpose & Context
Produce external marketing literature, comprehensive investment prospectuses, and candidate FAQs.

### Step-by-Step Deliverable Recipe
1. **Review Templates:** Inspect [templates/brochures/franchise-opportunity-brochure.template.md](file:///d:/company/products/franchise-business-platform/templates/brochures/franchise-opportunity-brochure.template.md).
2. **Target Output Paths:**
   - Brochure: `clients/<client-slug>/sales-marketing/franchise-opportunity-brochure.md`
   - Prospectus: `clients/<client-slug>/sales-marketing/franchise-prospectus.md`
   - FAQ: `clients/<client-slug>/sales-marketing/franchise-faq.md`
3. **Include Key Sections:**
   - Company background and product portfolio summary.
   - Franchisee partner profile (required competencies, educational background, capital readiness).
   - Upfront capital expenditure and working capital requirements.
   - Ongoing training, lead distribution, and technical escalation support.

---

## 10. Franchise Operations Manuals & Support SLAs

### Purpose & Context
Standardize daily franchise office operations, compliance checklists, customer onboarding, and service level escalations.

### Step-by-Step Deliverable Recipe
1. **Review Framework:** Read [frameworks/franchise-operations/operations-governance-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-operations/operations-governance-framework.md).
2. **Review Template:** Inspect [templates/operations-manuals/franchise-operations-manual.template.md](file:///d:/company/products/franchise-business-platform/templates/operations-manuals/franchise-operations-manual.template.md).
3. **Target Output Path:** Save as `clients/<client-slug>/operations/franchise-operations-manual.md`.
4. **Document Core Modules:**
   - Unit Launch Checklist (Facility setup, internet, branding, workstation configuration).
   - Daily & Weekly Operational Rhythm.
   - Customer Onboarding & Training SOPs.
   - Incident & SLA Escalation Matrix (P1: Critical bug < 2hr response; P2: Major bug < 8hr; P3: Query < 24hr).
   - Annual Audit & Compliance Checklist.

---

## 11. Draft Policies & Franchise Agreements

### Purpose & Context
Author formal contractual and policy drafts governing legal relationships, revenue distributions, and intellectual property.

> [!WARNING]
> All legal documents produced must carry the prominent header: `[WORKING DISCUSSION DRAFT - NON-BINDING - REQUIRES INDEPENDENT LEGAL COUNSEL REVIEW]`. Never represent drafts as binding legal advice.

### Step-by-Step Deliverable Recipe
1. **Review Templates:**
   - [templates/franchise-agreements/franchise-agreement.template.md](file:///d:/company/products/franchise-business-platform/templates/franchise-agreements/franchise-agreement.template.md)
   - [templates/legal-policies/revenue-sharing-policy.template.md](file:///d:/company/products/franchise-business-platform/templates/legal-policies/revenue-sharing-policy.template.md)
2. **Target Output Paths:**
   - Draft Agreement: `clients/<client-slug>/legal-drafts/draft-franchise-agreement.md`
   - Revenue Policy: `clients/<client-slug>/legal-drafts/revenue-sharing-policy.md`
   - Territory Policy: `clients/<client-slug>/legal-drafts/territory-protection-policy.md`
3. **Draft Core Clauses:** Trademark license scope, fee schedules, tax deduction (TDS/GST), non-compete covenants, audit rights, dispute resolution, and termination procedures.

---

## 12. Management Presentations & Executive Decision Papers

### Purpose & Context
Prepare structured executive summaries and decision memos for client C-level management to approve business model transitions and fee adjustments.

### Step-by-Step Deliverable Recipe
1. **Review Template:** Inspect [templates/management-reports/executive-management-report.template.md](file:///d:/company/products/franchise-business-platform/templates/management-reports/executive-management-report.template.md).
2. **Target Output Path:** Save as `clients/<client-slug>/decisions/decision-paper-<topic>.md`.
3. **Structure 4-Part Memo:**
   - Context & Strategic Problem Statement.
   - Comparative Options Evaluated with Pros/Cons.
   - Recommended Action & Commercial Rationale.
   - Financial Impact & Implementation Roadmap.

---

## 13. Franchise Launch Readiness Execution & Workstream Governance

### Purpose & Role Ownership
The platform mandates a rigorous 12-workstream launch readiness framework ([franchise-launch-readiness-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-launch-readiness/franchise-launch-readiness-framework.md)) to guide client go-live operations.

As Analyst 1, you own the qualitative, strategic, documentation, and operational items across the 12 workstreams.

### Workstream Ownership Breakdown for Analyst 1
1. **Workstream 1 (Business Model & Commercial Strategy):**
   - Author and calibrate franchise models, unit economics narratives, and territory exclusivity rules.
   - Example deliverable: [fofo-operating-model.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/franchise-model/fofo-operating-model.md).
2. **Workstream 2 (Legal, Regulatory & Intellectual Property):**
   - Draft non-binding commercial policy and contract blueprints for review by retained legal counsel.
   - Coordinate resolution of Blocker `BLK-001` (Retained Legal Counsel Review of Master Agreement).
3. **Workstream 3 (Six-Product Sales Readiness):**
   - Author product catalogs, sales qualification playbooks, and demonstration scripts.
   - Maintain client catalogs such as [products-catalog.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json).
4. **Workstream 5 (Franchise Operations & SOPs):**
   - Author franchisee onboarding handbooks, central support SLAs, and dispute resolution workflows.
   - Example deliverable: [support-sla-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/operations/support-sla-matrix.md).
5. **Workstream 7 (Franchise Recruitment & Marketing):**
   - Author prospectuses, investor brochures, FAQs, and web recruitment copy.
   - Example deliverable: [franchise-prospectus.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/sales-marketing/franchise-prospectus.md).
6. **Workstream 8 (Training & Certification):**
   - Author 5-day franchisee onboarding curricula, salesperson LMS modules, and certification exams.
   - Example deliverable: [franchise-training-curriculum.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/operations/franchise-training-curriculum.md).
7. **Workstream 10 (Partner Onboarding Documents):**
   - Author standardized application forms, due diligence questionnaires, and territory acceptance deeds.
   - Example deliverable: [franchise-application-form.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/sales-marketing/franchise-application-form.md).
8. **Workstream 11 (Governance & Performance Monitoring):**
   - Draft Franchise Advisory Council (FAC) charters, audit inspection checklists, and compliance scorecards.
9. **Workstream 12 (Pilot Launch & Final Approval):**
   - Structure pilot rollout protocols, define entry/exit milestone criteria, and monitor regional pilots.
   - Example deliverable: [pilot-launch-protocol.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/operations/pilot-launch-protocol.md).

### Task Maturity Progression
Never mark a task complete simply because a draft exists! Strictly adhere to the 7-stage maturity hierarchy:
`Not Started` ──> `In Progress` ──> `Document Created` ──> `Document Reviewed` ──> `Document Approved` ──> `Process Implemented` ──> `Process Verified`

---

## 14. Analyst 1 Quality Checklist & Peer Review Hand-Off

Before submitting any deliverable for peer review by Analyst 2, execute this mandatory self-audit:

```text
[ ] 1. Evidence Verification: Every empirical metric cites an active EVD-* ID in research-evidence-register.md.
[ ] 2. Assumptions Labeled: Any estimated figures carry [PROPOSED] or [WORKING HYPOTHESIS] tags.
[ ] 3. Status Tagged: Document header clearly states [DRAFT] or [WORKING DISCUSSION DRAFT].
[ ] 4. Legal Disclaimers: Financial risk and non-binding legal disclaimers are prominently displayed.
[ ] 5. Clickable Relative Links: All internal cross-references use verified file:/// markdown links.
[ ] 6. Tenant Isolation: Document is placed inside clients/<client-slug>/, not in generic platform directories.
[ ] 7. Launch Readiness Tagged: Deliverable is mapped to a specific Task ID in clients/<client-slug>/launch-readiness/.
[ ] 8. Dual-Analyst Review Assigned: Logged in analyst-workspace/task-tracker/task-board.md under "Peer Review".
```
