# Welcome to the Franchise Business Modeling & Intelligence Platform
## START-HERE: The Primary Onboarding Guide for New Analysts

> [!IMPORTANT]
> **MANDATORY FIRST READ:** If you are a newly joined Data Analyst, Strategy Consultant, or Quantitative Modeler, start your journey here. This document explains the platform, your role, how our repository works, and exactly what you are expected to do during your first week.

---

## 1. What the Platform Is

The **Franchise Business Modeling & Intelligence Platform** is an enterprise-grade, data-driven analytical environment engineered to research, evaluate, architect, document, visualize, pitch, launch, and optimize franchise business models across multiple commercial industries.

Rather than relying on informal spreadsheets, unverified growth assumptions, and disconnected marketing slide decks, the platform treats franchise engineering as an auditable discipline combining:
- Decimal-safe financial modeling engines (`decimal.Decimal` in Python).
- Dynamic, linked-formula Excel models (openpyxl).
- Structured JSON Schema data contracts (Draft-07).
- Reusable, industry-agnostic business frameworks.
- Automated document and pitch presentation generators.
- A centralized analyst command workspace with evidence tracking registers.

---

## 2. Why the Platform Exists

Franchising powers trillions of dollars in global commerce across Quick Service Restaurants (QSR), retail, education, healthcare, and software. However, traditional franchise consulting suffers from chronic failure modes:
1. **Unsubstantiated Financial Promises:** Pitch decks frequently claim "guaranteed returns" or "instant payback" without sensitivity analysis or working capital modeling.
2. **Spreadsheet Fragility:** Broken formulas, hardcoded numbers, and circular references lead to severe capital shortfalls.
3. **Ambiguous Operating Boundaries:** Poorly defined franchisee vs. franchisor responsibilities cause service failure and legal disputes.
4. **Territory Cannibalization:** Unplanned sales territory allocation results in channel conflict and partner insolvency.

This platform replaces intuitive guesswork with a repeatable, institutional-grade engineering methodology.

---

## 3. Who Uses the Platform

| User Group | How They Use the Platform |
|---|---|
| **Data Analysts (You)** | Conduct secondary/primary market research, calibrate financial models, compute unit economics, configure schemas, and author client deliverables. |
| **Franchise Strategy Consultants** | Evaluate client business models, select optimal franchise archetypes (FOFO, FOCO, Master, etc.), design territory policies, and negotiate commercial splits. |
| **Corporate Enterprise Clients** | Review feasibility reports, approve commercial terms, inspect 36-month P&Ls, and sponsor regional franchise rollout campaigns. |
| **Prospective Franchise Partners** | Review transparent franchise prospectuses, inspect break-even requirements, and evaluate business viability before investing capital. |

---

## 4. The Critical Axiom: Platform Independence vs. TMK IT Solutions

> [!CAUTION]
> **NEVER CONFUSE THE PLATFORM WITH TMK IT SOLUTIONS LLP.**

- **The Platform is Client-Independent and Industry-Agnostic:**
  The core methodologies (`frameworks/`), document blueprints (`templates/`), calculation engines (`tools/`), schemas (`schemas/`), and industry models (`industry-models/`) are designed to serve **any industry**—from software and diagnostics to restaurants and retail.
- **TMK IT Solutions LLP is the Inaugural Client:**
  TMK IT Solutions LLP (`clients/tmk-it-solutions/`) is the first commercial enterprise being modeled on the platform. It is a client, **not the platform itself**.
- **Do Not Leak Client Rules into Generic Modules:**
  Never hardcode TMK's proposed 40:60 split, ₹25,000/₹50,000 joining fees, 6 software products, or specific Indian taluka boundaries into generic engines, templates, or schemas. Everything in reusable modules must be strictly parameterized.

---

## 5. What Analysts Are Expected to Produce

Depending on your assigned role, you will produce institutional-grade deliverables:

### Analyst 1: Strategy, Research & Documentation
- Empirical Market Research Briefs citing verifiable data sources.
- Franchise Model Design Documents & Operational RACI Matrices.
- Competitor Parity & Pricing Benchmarking Matrices.
- Slide-by-slide Franchise Pitch Deck Specifications.
- Commercial Brochures, Investor Prospectuses, and FAQs.
- Unit Operations Handbooks and Salesperson Training Curricula.
- Working Drafts of Franchise Agreements, Territory Policies, and NDAs.

### Analyst 2: Financial Modeling, Data Analytics & Intelligence
- Parameterized Financial Assumptions files (`assumptions.json`).
- Decimal-Safe Pro-Forma P&L Projections (36-month horizon).
- Operational Break-Even Unit Sales Calculations.
- Working Capital Decay, Solvency Runway, and Payback Analyses.
- Dynamic, Linked-Formula Excel Model Workbooks (`.xlsx`).
- Multi-Scenario Sensitivity Matrices (Conservative, Base, Optimistic).
- Territory Opportunity Scoring ($TOS$) and white-space prioritization models.
- KPI Specifications and Executive Dashboard Mockups.

---

## 6. How the Repository is Organized

```text
franchise-business-platform/
│
├── README.md                      # Platform overview & quickstart
├── AGENTS.md                      # Supreme instructions for AI agents and contributors
├── AGENT.md                       # Quick-reference card
├── CONTRIBUTING.md                # Git workflow, branch naming, Conventional Commits
├── CHANGELOG.md                   # Version release notes
│
├── docs/                          # Self-guided documentation and onboarding
│   ├── START-HERE.md              # <-- You are here! Primary analyst onboarding portal
│   ├── DOCUMENTATION-MAP.md       # Visual sitemap and asset directory index
│   ├── GLOSSARY.md                # Comprehensive terminology dictionary
│   ├── 01-platform-orientation/   # Module 1: Vision, architecture, and principles
│   ├── 02-franchise-fundamentals/ # Module 2: Archetypes, RACI, economics, protection
│   ├── 03-repository-guide/       # Module 3: Codebase anatomy, schemas, Git workflow
│   ├── 04-client-workspaces/      # Module 4: Client isolation & TMK workspace tour
│   ├── 05-analyst-playbooks/      # Module 5: Detailed Analyst 1 & Analyst 2 execution playbooks
│   ├── 06-quality-and-approval/   # Module 6: Standard work journey, peer review & CI
│   └── 07-first-week-onboarding/  # Module 7: Day-by-day 5-day onboarding journey & checklist
│
├── frameworks/                    # 12 Generic, reusable franchise business frameworks (incl. launch readiness)
├── templates/                     # 21 Reusable document, presentation, policy & checklist templates
├── industry-models/               # 8 Industry vertical economic profiles
├── clients/                       # Isolated client workspaces (e.g., tmk-it-solutions)
├── schemas/                       # 8 JSON Schema Draft-07 data contracts (incl. launch-readiness)
├── tools/                         # Python calculation engines, Excel generators, launch trackers, validator
├── analyst-workspace/             # Task board, evidence register, assumptions log, checklists
└── tests/                         # Automated pytest unit and integration test suite
```

---

## 7. Where to Find Frameworks, Templates and Launch Readiness

- **Generic Frameworks (`frameworks/`):**
  When designing a franchise model, evaluating financial feasibility, structuring a territory policy, or managing go-live readiness, consult [frameworks/](file:///d:/company/products/franchise-business-platform/frameworks/). Every framework follows a standardized 9-section structure. Key frameworks include:
  - [Franchise Launch Readiness Framework](file:///d:/company/products/franchise-business-platform/frameworks/franchise-launch-readiness/franchise-launch-readiness-framework.md): 12-workstream methodology, mathematical readiness scoring ($WRI$, $PLRI$), and 7-stage maturity model.
  - [Launch Gates & Critical Blockers](file:///d:/company/products/franchise-business-platform/frameworks/franchise-launch-readiness/launch-gates-and-blockers.md): Gates 1–6 entry/exit governance and Blocker ledger taxonomy (`BLK-001` to `BLK-007`).
- **Reusable Templates (`templates/`):**
  When authoring a business plan, pitch presentation, agreement draft, operations manual, or onboarding kit, start with a template in [templates/](file:///d:/company/products/franchise-business-platform/templates/). All templates use standardized `{{PLACEHOLDER}}` tags.
  - Due diligence: [franchise-due-diligence-questionnaire.template.md](file:///d:/company/products/franchise-business-platform/templates/checklists/franchise-due-diligence-questionnaire.template.md)
  - Curriculum: [franchisee-training-curriculum.template.md](file:///d:/company/products/franchise-business-platform/templates/training/franchisee-training-curriculum.template.md)
  - Governance: [franchise-advisory-council-charter.template.md](file:///d:/company/products/franchise-business-platform/templates/governance/franchise-advisory-council-charter.template.md)
  - Pilot launch: [pilot-launch-protocol.template.md](file:///d:/company/products/franchise-business-platform/templates/pilot-launch/pilot-launch-protocol.template.md)

---

## 8. How to Select a Client Workspace

Client workspaces live under `clients/<client-slug>/`.
- For the inaugural engagement, navigate to [clients/tmk-it-solutions/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/).
- To understand the client's commercial context, read:
  1. [Company Overview](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/profile/company-overview.md)
  2. [Commercial Assumptions](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/profile/commercial-assumptions.md)
  3. [Product Catalog](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json)
  4. [FOFO Operating Model](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/franchise-model/fofo-operating-model.md)
  5. [TMK Launch Readiness Checklist](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/launch-readiness/tmk-launch-readiness-checklist.md) & [Gates Assessment](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/launch-readiness/tmk-launch-gates-assessment.md)
  6. [Interactive Excel Launch Tracker](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/launch-readiness/tmk_launch_readiness_tracker.xlsx)

---

## 9. How to Find Assigned Tasks

Task management is centralized in the analyst command center:
1. Open the [Centralized Task Board](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md).
2. Check your role-specific backlog:
   - Analyst 1: [analyst-1-backlog.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/assignments/analyst-1-backlog.md)
   - Analyst 2: [analyst-2-backlog.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/assignments/analyst-2-backlog.md)
3. Every task has an assigned ID (e.g., `A1-01` or `A2-02`), owner, expected output path, status, and objective acceptance criteria.

---

## 10. How to Submit Completed Work & The Contribution Journey

We follow a strict 10-stage contribution lifecycle:
```text
Task Assigned ──> Research ──> Evidence Logging ──> Analysis ──> Draft Deliverable
      │
      v
Self-Validation ──> Pull Request ──> Peer Review ──> Management Approval ──> Release
```

1. **Create Feature Branch:** `feature/<client-or-framework>-<brief-description>`.
2. **Log Research & Assumptions:** Record citations in [research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md) and parameters in [assumptions-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/assumptions-register.md).
3. **Execute Self-Validation:**
   ```bash
   python -m pytest tests/ -v
   python tools/validation/validate_repo.py
   ```
4. **Submit PR:** Use [pull_request_template.md](file:///d:/company/products/franchise-business-platform/.github/pull_request_template.md).
5. **Peer Review Gate:** Analyst 1 deliverables are reviewed by Analyst 2; Analyst 2 deliverables are reviewed by Analyst 1.

---

## 11. How Approvals Work

Every document and model carries an explicit status header:
- `[DRAFT]`: Work in progress; internal to author.
- `[WORKING DISCUSSION DRAFT]`: Formulated for structural analysis; non-binding.
- `[PEER APPROVED]`: Validated and signed off by the cross-disciplinary peer analyst.
- `[MODELING APPROVED]`: Mathematical integrity and formulas certified by Analyst 2.
- `[CLIENT APPROVED]`: Formally ratified by client leadership in [approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md).

Never modify an approved document without explicit authorization.

---

## 12. Where to Go Next

Now that you understand the platform landscape, begin your guided learning journey:

1. **Inspect the Master Sitemap:** [DOCUMENTATION-MAP.md](file:///d:/company/products/franchise-business-platform/docs/DOCUMENTATION-MAP.md)
2. **Read the Terminology Glossary:** [GLOSSARY.md](file:///d:/company/products/franchise-business-platform/docs/GLOSSARY.md)
3. **Start Guided Module 01:** [01-platform-orientation/README.md](file:///d:/company/products/franchise-business-platform/docs/01-platform-orientation/README.md)
4. **Follow Your 5-Day Onboarding Schedule:** [07-first-week-onboarding/five-day-onboarding-journey.md](file:///d:/company/products/franchise-business-platform/docs/07-first-week-onboarding/five-day-onboarding-journey.md)
