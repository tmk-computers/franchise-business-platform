# Master Documentation Map & Repository Index

## 1. Visual Documentation Architecture

```mermaid
graph TD
    Root[Root: README.md / AGENTS.md / AGENT.md] --> StartHere[docs/START-HERE.md]
    StartHere --> DocMap[docs/DOCUMENTATION-MAP.md]
    StartHere --> Glossary[docs/GLOSSARY.md]

    StartHere --> M1[01-platform-orientation]
    StartHere --> M2[02-franchise-fundamentals]
    StartHere --> M3[03-repository-guide]
    StartHere --> M4[04-client-workspaces]
    StartHere --> M5[05-analyst-playbooks]
    StartHere --> M6[06-quality-and-approval]
    StartHere --> M7[07-first-week-onboarding]

    M1 --> PlatformDir[platform/*]
    M2 --> FrameworksDir[frameworks/*]
    M3 --> SchemasDir[schemas/* & tools/*]
    M4 --> ClientsDir[clients/tmk-it-solutions/*]
    M5 --> AnalystWs[analyst-workspace/* & templates/*]
    M6 --> ReviewGate[quality-checklists/* & tests/*]
    M7 --> OnboardingChecklist[07-first-week-onboarding/onboarding-checklist.md]
```

---

## 2. Master Navigation Index

### 2.1. Primary Entry Points
- [START-HERE.md](START-HERE.md): The primary onboarding portal for all incoming analysts.
- [DOCUMENTATION-MAP.md](DOCUMENTATION-MAP.md): This visual sitemap and asset directory.
- [GLOSSARY.md](GLOSSARY.md): Complete franchise business and financial modeling terminology dictionary.
- [DOCUMENTATION-AUDIT.md](DOCUMENTATION-AUDIT.md): Comprehensive inventory and audit of repository assets.

### 2.2. Seven-Module Guided Learning Paths
1. [01-platform-orientation/README.md](01-platform-orientation/README.md): Vision, multi-tenant architecture, and client-independence axiom.
2. [02-franchise-fundamentals/README.md](02-franchise-fundamentals/README.md): Archetypes (FOFO, FOCO, COCO, etc.), RACI matrices, unit economics, and investor protection.
3. [03-repository-guide/README.md](03-repository-guide/README.md): Codebase anatomy, Git branching workflow, Conventional Commits, and JSON schema data contracts.
4. [04-client-workspaces/README.md](04-client-workspaces/README.md): Client data isolation principles, client onboarding, and deep-dive tour of TMK IT Solutions LLP.
5. [05-analyst-playbooks/README.md](05-analyst-playbooks/README.md):
   - [Analyst 1 Playbook](05-analyst-playbooks/analyst-1-strategy-playbook.md): Strategy, market research, decks, agreements, operations.
   - [Analyst 2 Playbook](05-analyst-playbooks/analyst-2-finance-playbook.md): Financial engine, Excel models, break-even, sensitivity, dashboards.
6. [06-quality-and-approval/README.md](06-quality-and-approval/README.md):
   - [Standard Work Journey](06-quality-and-approval/standard-work-journey.md): 10-stage contribution lifecycle with concrete Analyst 1 and Analyst 2 walkthroughs.
7. [07-first-week-onboarding/README.md](07-first-week-onboarding/README.md):
   - [Five-Day Onboarding Journey](07-first-week-onboarding/five-day-onboarding-journey.md): Structured daily curriculum (Days 1–5).
   - [Onboarding Checklist](07-first-week-onboarding/onboarding-checklist.md): Interactive progress tracker.

---

### 2.3. Core Reusable Business Frameworks (`frameworks/`)
- [Franchise Archetypes Comparison & RACI](../frameworks/franchise-model-design/franchise-archetypes-comparison.md)
- [Financial Feasibility & Unit Economics](../frameworks/feasibility-analysis/financial-feasibility-framework.md)
- [Configurable Revenue Sharing & Settlement](../frameworks/revenue-sharing/configurable-revenue-sharing-framework.md)
- [Market Research Methodology (TAM/SAM/SOM)](../frameworks/market-research/market-research-methodology.md)
- [Territory Intelligence & Opportunity Scoring](../frameworks/territory-intelligence/territory-intelligence-framework.md)
- [Franchisee & Investor Protection](../frameworks/investor-protection/investor-protection-framework.md)
- [Risk Assessment & Mitigation Taxonomy](../frameworks/risk-assessment/risk-assessment-framework.md)
- [Operations Governance & Enablement](../frameworks/franchise-operations/operations-governance-framework.md)
- [Performance Analytics & 13 Core KPIs](../frameworks/performance-analytics/kpi-analytics-framework.md)
- [Network Expansion & Capacity Scaling](../frameworks/franchise-expansion/expansion-scaling-framework.md)
- [Financial Modeling Standards](../frameworks/financial-modeling/financial-modeling-standards.md)
- [Franchise Launch Readiness Framework](../frameworks/franchise-launch-readiness/franchise-launch-readiness-framework.md)
- [Launch Gates & Critical Blockers](../frameworks/franchise-launch-readiness/launch-gates-and-blockers.md)

---

### 2.4. Inaugural Client Workspace (`clients/tmk-it-solutions/`)
- [TMK Workspace Overview](../clients/tmk-it-solutions/README.md)
- Profile: [client.json](../clients/tmk-it-solutions/profile/client.json) | [Company Overview](../clients/tmk-it-solutions/profile/company-overview.md) | [Commercial Assumptions](../clients/tmk-it-solutions/profile/commercial-assumptions.md)
- Products: [Product Catalog JSON](../clients/tmk-it-solutions/products/products-catalog.json) | [School ERP](../clients/tmk-it-solutions/products/school-college-erp.md) | [Invoicing App](../clients/tmk-it-solutions/products/invoicing-app-web.md) | [OMR Software](../clients/tmk-it-solutions/products/omr-software.md) | [Property ERP](../clients/tmk-it-solutions/products/property-management-erp.md) | [DevOps Platform](../clients/tmk-it-solutions/products/devops-automation.md) | [Sales CRM](../clients/tmk-it-solutions/products/sales-crm.md)
- Franchise Model: [FOFO Model](../clients/tmk-it-solutions/franchise-model/fofo-operating-model.md) | [Fee Structure](../clients/tmk-it-solutions/franchise-model/fee-structure.md) | [Revenue Sharing Rules](../clients/tmk-it-solutions/franchise-model/revenue-sharing-rules.md) | [Territory Policy](../clients/tmk-it-solutions/franchise-model/territory-policy-draft.md)
- Financial Models: [Assumptions JSON](../clients/tmk-it-solutions/financial-models/assumptions.json) | [Projections Summary](../clients/tmk-it-solutions/financial-models/financial-projections-summary.md) | [Excel Workbook](../clients/tmk-it-solutions/financial-models/tmk_it_solutions_franchise_financial_model.xlsx)
- Pitch & Marketing: [Pitch Deck Spec](../clients/tmk-it-solutions/presentations/franchise-opportunity-pitch-deck.md) | [PowerPoint PPTX](../clients/tmk-it-solutions/presentations/franchise-opportunity-pitch-deck.pptx) | [Brochure](../clients/tmk-it-solutions/sales-marketing/franchise-brochure.md) | [Prospectus](../clients/tmk-it-solutions/sales-marketing/franchise-prospectus.md) | [FAQ](../clients/tmk-it-solutions/sales-marketing/franchise-faq.md)
- Working Legal Drafts: [Franchise Agreement](../clients/tmk-it-solutions/legal-drafts/franchise-agreement-draft.md) | [Revenue Policy](../clients/tmk-it-solutions/legal-drafts/revenue-sharing-policy-draft.md) | [Territory Policy](../clients/tmk-it-solutions/legal-drafts/territory-policy-draft.md) | [Renewal Policy](../clients/tmk-it-solutions/legal-drafts/franchise-renewal-policy-draft.md) | [Termination Policy](../clients/tmk-it-solutions/legal-drafts/franchise-termination-policy-draft.md) | [NDA](../clients/tmk-it-solutions/legal-drafts/confidentiality-agreement-draft.md) | [Brand Usage](../clients/tmk-it-solutions/legal-drafts/brand-usage-policy-draft.md)
- Launch Readiness: [Checklist JSON](../clients/tmk-it-solutions/launch-readiness/tmk-launch-readiness-checklist.json) | [Checklist Master Table](../clients/tmk-it-solutions/launch-readiness/tmk-launch-readiness-checklist.md) | [Gates Assessment](../clients/tmk-it-solutions/launch-readiness/tmk-launch-gates-assessment.md) | [Excel Tracker](../clients/tmk-it-solutions/launch-readiness/tmk_launch_readiness_tracker.xlsx) | [Coverage Report](../clients/tmk-it-solutions/launch-readiness/tmk-launch-coverage-report.md)

---

### 2.5. Analyst Workspace & Registers (`analyst-workspace/`)
- [Task Board](../analyst-workspace/task-tracker/task-board.md)
- [Analyst 1 Backlog](../analyst-workspace/assignments/analyst-1-backlog.md)
- [Analyst 2 Backlog](../analyst-workspace/assignments/analyst-2-backlog.md)
- [Research Evidence Register](../analyst-workspace/research-methodology/research-evidence-register.md)
- [Assumptions Register](../analyst-workspace/research-methodology/assumptions-register.md)
- [Pull Request Checklist](../analyst-workspace/quality-checklists/pull-request-review-checklist.md)
- [Deliverable Acceptance Checklist](../analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md)

---

### 2.6. Franchise Investor Academy (`education/franchise-investor-academy/`)
- [Academy Master Portal](../education/franchise-investor-academy/README.md)
- [Learning Paths & Curriculum](../education/franchise-investor-academy/LEARNING_PATHS.md)
- [100-Point Franchise Due Diligence Checklist](../education/franchise-investor-academy/DUE_DILIGENCE_CHECKLIST.md)
- [Investor Terminology Glossary](../education/franchise-investor-academy/GLOSSARY.md)
- [Editorial Standards & Review Gates](../education/franchise-investor-academy/EDITORIAL_STANDARDS.md)
- [Multi-Format Publishing Workflow](../education/franchise-investor-academy/PUBLISHING_WORKFLOW.md)
- **The 10-Volume Library:**
  - [Book 1: The First-Time Franchise Investor's Handbook](../education/franchise-investor-academy/book-01-first-time-investor-handbook/README.md) *(v1.0.0 Complete)*
  - [Book 2: Demystifying Business Models & Operating Archetypes](../education/franchise-investor-academy/book-02-business-models-and-archetypes/README.md) *(v0.1.0 Active Draft)*
  - [Book 3: Franchise Unit Economics & Financial Literacy](../education/franchise-investor-academy/book-03-unit-economics-and-financial-literacy/README.md) *(v0.1.0 Active Draft)*
  - [Book 4: The 100-Point Franchise Due Diligence Playbook](../education/franchise-investor-academy/book-04-due-diligence-playbook/README.md) *(v0.1.0 Active Draft)*
  - [Book 5: Unpacking the Franchise Agreement & Legal Rights](../education/franchise-investor-academy/book-05-franchise-agreements-and-legal-rights/README.md) *(v0.1.0 Active Draft)*
  - [Book 6: Sector-by-Sector Franchise Economics](../education/franchise-investor-academy/book-06-sector-by-sector-economics/README.md) *(v0.1.0 Active Draft)*
  - [Book 7: Site Selection, Territory Intelligence & Real Estate](../education/franchise-investor-academy/book-07-site-selection-and-territory-intelligence/README.md) *(v0.1.0 Active Draft)*
  - [Book 8: Working Capital Management & Cash Flow Survival](../education/franchise-investor-academy/book-08-working-capital-and-cash-flow/README.md) *(v0.1.0 Active Draft)*
  - [Book 9: Multi-Unit Franchising & Empire Building](../education/franchise-investor-academy/book-09-multi-unit-franchising/README.md) *(v0.1.0 Active Draft)*
  - [Book 10: Franchise Exits, Resales & Succession Planning](../education/franchise-investor-academy/book-10-franchise-exits-and-resales/README.md) *(v0.1.0 Active Draft)*

