# Franchise Business Modeling & Intelligence Platform (V0.1)

A systematic, client-independent, and industry-agnostic platform engineered to research, design, evaluate, document, visualize, pitch, launch, and optimize franchise business models.

---

> [!IMPORTANT]
> ### 🚀 New to the Platform? Start Here!
> If you are a new Data Analyst, Engineer, or Contributor, your primary orientation gateway is:
> 👉 **[docs/START-HERE.md](docs/START-HERE.md)**
>
> | Quick Navigation Link | Target Content |
> |---|---|
> | **[docs/START-HERE.md](docs/START-HERE.md)** | Executive welcome, platform vs client distinction, and onboarding guide |
> | **[docs/DOCUMENTATION-MAP.md](docs/DOCUMENTATION-MAP.md)** | Complete directory tree and file index across the entire repository |
> | **[docs/GLOSSARY.md](docs/GLOSSARY.md)** | Alphabetized glossary of franchise, financial, regulatory, and platform terms |
> | **[Analyst 1 Playbook](docs/05-analyst-playbooks/analyst-1-strategy-playbook.md)** | Execution manual for Business Strategy, Market Research & Documentation |
> | **[Analyst 2 Playbook](docs/05-analyst-playbooks/analyst-2-finance-playbook.md)** | Execution manual for Financial Modeling, Analytics & Python/Excel Engines |
> | **[First-Week Onboarding Program](docs/07-first-week-onboarding/README.md)** | 5-Day structured onboarding curriculum and interactive checklist |
> | **[Franchise Investor Academy](education/franchise-investor-academy/README.md)** | 10-Volume educational eBook library, learning paths & 100-point checklist |
> | **[Launch Readiness Framework](frameworks/franchise-launch-readiness/franchise-launch-readiness-framework.md)** | 12-workstream methodology, launch gates, and blocker resolution |
> | **[TMK Launch Checklist & Tracker](clients/tmk-it-solutions/launch-readiness/tmk-launch-readiness-checklist.md)** | Master 65-task readiness matrix, gates assessment, and Excel tracker |


---

## Table of Contents
1. [Executive Overview & Platform Vision](#1-executive-overview--platform-vision)
2. [Business Problems Solved](#2-business-problems-solved)
3. [Target Users](#3-target-users)
4. [Supported Franchise Business Models](#4-supported-franchise-business-models)
5. [Guided Learning Paths for Analysts](#5-guided-learning-paths-for-analysts)
6. [Repository Organization & Directory Map](#6-repository-organization--directory-map)
7. [Client Workspaces & Inaugural Client (TMK IT Solutions)](#7-client-workspaces--inaugural-client-tmk-it-solutions)
8. [Decimal-Safe Financial Modeling & Projections Engine](#8-decimal-safe-financial-modeling--projections-engine)
9. [Institutional Document & Presentation Templates](#9-institutional-document--presentation-templates)
10. [Contribution Guidelines & Standard Work Journey](#10-contribution-guidelines--standard-work-journey)
11. [Quality Gates & Automated Validation Suite](#11-quality-gates--automated-validation-suite)
12. [Current Roadmap & Implementation Status](#12-current-roadmap--implementation-status)
13. [Next Steps & Navigation](#13-next-steps--navigation)

---

## 1. Executive Overview & Platform Vision

Franchising is one of the most effective scaling mechanisms for modern enterprises. However, traditional franchise modeling is plagued by fragmented spreadsheets, unverified commercial assumptions, unrealistic earnings claims, poorly defined unit economics, and lack of operational standardization. 

The **Franchise Business Modeling & Intelligence Platform** transforms franchise expansion from intuitive guesswork into an auditable, data-driven discipline. By combining rigorous financial engineering, standardized operational frameworks, structured market intelligence, and automated document generation, the platform enables enterprises and franchise advisory teams to rapidly evaluate feasibility, design sustainable revenue-sharing models, and deploy franchise networks with confidence.

**Core Architectural Axiom:** This platform is strictly **client-independent and industry-agnostic**. Reusable frameworks (`frameworks/`), schemas (`schemas/`), calculation engines (`tools/`), and templates (`templates/`) are strictly isolated from client workspaces (`clients/`). **TMK IT Solutions LLP** is the platform's inaugural client workspace (`clients/tmk-it-solutions/`), NOT the platform itself.

---

## 2. Business Problems Solved

| Problem in Traditional Franchising | Platform Solution |
|---|---|
| **Unrealistic Financial Claims & Investor Risk** | Decimal-safe financial modeling engine with transparent break-even, payback, cash flow analysis, and sensitivity testing across conservative, base, and optimistic scenarios. |
| **Ambiguous Franchisee-Franchisor Roles** | Standardized responsibility matrices (RACI) across operational, technical, sales, billing, and regulatory domains for all major franchise formats. |
| **Rigid, Hardcoded Revenue Splits** | Parameterized revenue-sharing engine supporting multi-tier product lines, recurring subscription renewals, implementation fees, and infrastructure offsets. |
| **Territory Conflicts & Cannibalization** | Structured territory intelligence methodology incorporating demographic density, market opportunity scoring, and taluka/district-level boundary rules. |
| **Fragmented Documentation & Inconsistent Pitching** | Reusable document and presentation templates generating cohesive franchise prospectuses, business plans, pitch decks, and legal agreements. |
| **Knowledge Silos Among Analysts** | Centralized analyst workspace with standardized evidence registers, assumption tracking, risk scoring, and peer review gates. |

---

## 3. Target Users

1. **Franchise Advisory & Consulting Teams:** Senior consultants and business analysts evaluating expansion models for corporate clients.
2. **Corporate Strategy & Expansion Executives:** Enterprise leaders seeking to franchise internal software products, retail concepts, or service networks.
3. **Data & Financial Analysts:** Quantitative analysts developing unit economics, financial forecasts, and KPI tracking dashboards.
4. **Prospective Franchise Investors:** Commercial partners reviewing institutional-grade franchise disclosure documents, P&L projections, and unit economics.

---

## 4. Supported Franchise Business Models

The platform provides dedicated comparative frameworks and economic models for all primary franchise archetypes:

- **FOFO (Franchise Owned, Franchise Operated):** Franchisee funds capital and manages daily operations; franchisor provides branding, product development, training, and central support. (First client TMK IT Solutions LLP utilizes this model).
- **FOCO (Franchise Owned, Company Operated):** Franchisee provides capital/real estate; franchisor operates the unit directly, sharing operational profits.
- **COCO (Company Owned, Company Operated):** Fully centralized flagship model used for benchmarking and market proof.
- **COFO (Company Owned, Franchise Operated):** Franchisor owns the asset or lease; an experienced operator runs the business.
- **Master Franchise:** Master franchisee holds exclusive development rights for a major region, sub-franchising and sharing royalties.
- **Area Development Franchise:** Developer commits to opening a predetermined number of units within a geographic territory.
- **Multi-Unit Franchise:** Single franchisee operates multiple locations across defined territories.
- **Product Distribution & Sales Franchise:** Focused on distribution rights, channel sales enablement, and localized customer relationship management.
- **Hybrid Models:** Custom blended models tailored to multi-tiered digital and physical ecosystems.

---

## 5. Guided Learning Paths for Analysts

To guide new contributors through systematic onboarding, the platform provides 7 numbered learning paths in `docs/`:

1. **[01-Platform Orientation](docs/01-platform-orientation/README.md):** Strategic vision, SaaS architecture, tenant isolation, and client independence.
2. **[02-Franchise Fundamentals](docs/02-franchise-fundamentals/README.md):** Archetypes (FOFO/FOCO/COCO), RACI governance, pass-through GST segregation, and territory rules.
3. **[03-Repository Guide](docs/03-repository-guide/README.md):** Directory tour, JSON Schema contracts, mathematical standards, and testing conventions.
4. **[04-Client Workspaces](docs/04-client-workspaces/README.md):** Multi-tenant isolation and deep-dive into the TMK IT Solutions baseline.
5. **[05-Analyst Playbooks](docs/05-analyst-playbooks/README.md):** Role manuals for [Analyst 1 (Strategy)](docs/05-analyst-playbooks/analyst-1-strategy-playbook.md) and [Analyst 2 (Finance)](docs/05-analyst-playbooks/analyst-2-finance-playbook.md).
6. **[06-Quality and Approval](docs/06-quality-and-approval/README.md):** 10-stage contribution lifecycle, peer review gates, and deliverable sign-offs.
7. **[07-First-Week Onboarding](docs/07-first-week-onboarding/README.md):** 5-day structured syllabus and interactive onboarding checklist.

---

## 6. Repository Organization & Directory Map

```text
franchise-business-platform/
│
├── README.md                          # Repository overview & quickstart
├── AGENTS.md                          # Authoritative operational rules for AI assistants
├── CONTRIBUTING.md                    # Contribution guidelines & branch workflows
├── CHANGELOG.md                       # Release notes and version history
├── LICENSE-DECISION.md                # IP, licensing, and proprietary classification
│
├── docs/                              # Centralized documentation system
│   ├── START-HERE.md                  # Primary onboarding entry point for all analysts
│   ├── DOCUMENTATION-MAP.md           # Master directory tree and file index
│   ├── GLOSSARY.md                    # Comprehensive terminology reference
│   ├── DOCUMENTATION-AUDIT.md         # Audit of repository structure and gaps
│   ├── 01-platform-orientation/       # Module 1: Architecture & vision
│   ├── 02-franchise-fundamentals/     # Module 2: Franchise models & RACI
│   ├── 03-repository-guide/           # Module 3: Directories & standards
│   ├── 04-client-workspaces/          # Module 4: Tenant isolation & TMK baseline
│   ├── 05-analyst-playbooks/          # Module 5: Role-specific playbooks
│   ├── 06-quality-and-approval/       # Module 6: Review gates & 10-stage lifecycle
│   └── 07-first-week-onboarding/      # Module 7: 5-Day onboarding syllabus
│
├── platform/                          # Platform vision, PRDs, SaaS architecture & roadmap
├── frameworks/                        # Reusable, client-agnostic business frameworks (11 domains)
├── templates/                         # Standardized document and presentation templates
├── industry-models/                   # Vertical-specific economics (software, retail, etc.)
├── education/                         # Educational academies & curricula
│   └── franchise-investor-academy/    # 10-Volume Franchise Investor eBook Library & Checklists
│
├── clients/                           # Client-specific workspaces (strictly isolated)
│   └── tmk-it-solutions/              # Inaugural client: TMK IT Solutions LLP
│       ├── profile/                   # Corporate overview & leadership
│       ├── products/                  # 6 software product profiles & catalog
│       ├── research/                  # Market demand, competitive & territory briefs
│       ├── franchise-model/           # FOFO architecture, RACI & revenue rules
│       ├── financial-models/          # Projections & live-formula Excel workbook
│       ├── territory-analysis/        # Indian taluka & district expansion strategy
│       ├── presentations/             # Franchise opportunity pitch deck & PowerPoint
│       ├── sales-marketing/           # Brochure, prospectus, FAQ & infographics
│       ├── legal-drafts/              # Non-final agreement and policy drafts
│       ├── operations/                # Operating handbook & support SLA matrix
│       ├── decisions/                 # Management decision log
│       ├── approvals/                 # Commercial sign-off matrix
│       └── deliverables/              # Finalized and approved client assets
│
├── schemas/                           # JSON Schema data contracts (Draft-07)
├── tools/                             # Automation tools and calculation engines
├── analyst-workspace/                 # Dual-analyst operational command center
└── tests/                             # Automated test suite (pytest)
```

---

## 7. Client Workspaces & Inaugural Client (TMK IT Solutions)

Client workspaces reside in `clients/<client-slug>/`. The inaugural client is **TMK IT Solutions LLP** (`clients/tmk-it-solutions/`).

### TMK IT Solutions Overview
- **Business Model:** FOFO (Franchise Owned, Franchise Operated).
- **Product Portfolio:** 6 enterprise B2B software solutions (Cloud ERP, School Management, Hospital ERP, Retail POS, DevOps Automation, Cybersecurity Suite).
- **Commercial Terms:**
  - Promotional joining fee: ₹25,000 (first 10 units).
  - Standard joining fee: ₹50,000.
  - Net revenue sharing split: 40% Franchisee : 60% TMK IT Solutions.
  - Mandatory statutory tax handling: 18% GST pass-through strictly isolated from distributable revenue.
  - Working capital cushion: ₹50,000–₹1,00,000.
- **Territory Strategy:** Sub-district administrative boundaries (Talukas / Tehsils) with a 90-day Deal Registration Lock.

To onboard a future client, follow the [Client Onboarding Playbook](docs/implementation-guides/client-onboarding-playbook.md).

---

## 8. Decimal-Safe Financial Modeling & Projections Engine

All financial calculations in Python strictly utilize `decimal.Decimal` with `ROUND_HALF_UP` quantization (`0.01`) to eliminate binary floating-point drift.

### Running Projections & Generating Excel Workbooks
Execute the command-line interface in `tools/financial-modeling/`:
```bash
# 1. Run simulation for base scenario:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario base

# 2. Run simulation for conservative (stress-test) scenario:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario conservative

# 3. Generate comprehensive, formula-linked Excel workbook:
python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel
```
Output workbook: `clients/tmk-it-solutions/financial-models/tmk_it_solutions_franchise_financial_model.xlsx`.

---

## 9. Institutional Document & Presentation Templates

The `templates/` directory provides production-grade templates featuring standardized `{{...}}` placeholders:
- **Business Plans:** `templates/business-plans/franchise-business-plan-template.md`
- **Market Research:** `templates/market-research/market-analysis-template.md`
- **Franchise Agreements:** `templates/franchise-agreements/master-franchise-agreement-template.md`
- **Legal Policies:** `templates/legal-policies/revenue-sharing-policy-template.md`
- **Investor Pitch Decks:** `templates/investor-presentations/pitch-deck-outline.md`
- **Brochures & Prospectuses:** `templates/brochures/franchise-brochure-template.md`
- **Operations Manuals:** `templates/operations-manuals/operations-manual-template.md`

Generate PowerPoint presentations automatically:
```bash
python tools/document-generation/generate_pitch_deck.py --client tmk-it-solutions
```

---

## 10. Contribution Guidelines & Standard Work Journey

Contributors follow the **10-Stage Contribution Lifecycle** detailed in [docs/06-quality-and-approval/standard-work-journey.md](docs/06-quality-and-approval/standard-work-journey.md):
$$\text{Task Assigned} \to \text{Research} \to \text{Evidence Collection} \to \text{Analysis} \to \text{Draft Deliverable} \to \text{Self-Validation} \to \text{Pull Request} \to \text{Peer Review} \to \text{Management Approval} \to \text{Release}$$

- Deliverables authored by **Analyst 1 (Strategy)** must be peer-reviewed by **Analyst 2 (Finance)**.
- Models developed by **Analyst 2 (Finance)** must be peer-reviewed by **Analyst 1 (Strategy)**.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for Git branch conventions.

---

## 11. Quality Gates & Automated Validation Suite

Before committing code or opening pull requests, execute the automated verification suite:
```bash
# Run pytest unit test suite:
python -m pytest tests/ -v

# Run repository integrity, schema, and markdown link validation:
python tools/validation/validate_repo.py
```

The validation suite enforces:
- Strict JSON Schema validation against `schemas/*.schema.json`.
- Decimal arithmetic consistency across scenarios.
- Existence of mandatory client files.
- Zero broken relative Markdown links across documentation.

---

## 12. Current Roadmap & Implementation Status

### Current Status (V0.1 Bootstrap)
- [x] Complete documentation navigation system with `START-HERE.md`, `DOCUMENTATION-MAP.md`, and `GLOSSARY.md`.
- [x] 7 guided learning paths covering platform orientation, franchise fundamentals, playbooks, and onboarding.
- [x] Dedicated execution playbooks for Analyst 1 (Strategy) and Analyst 2 (Finance).
- [x] Reusable Python financial engine with dynamic Excel workbook generator.
- [x] Complete isolated workspace for inaugural client: **TMK IT Solutions LLP**.
- [x] Automated test suite and repository validator passing 100% green.

### Roadmap Outlook
- **V1.0 (Q1 2027):** Multi-client support, interactive territory mapping CLI, automated PDF deliverable compiler.
- **V2.0 (Q3 2027):** Cloud-native backend (ASP.NET Core Web API + PostgreSQL), real-time financial simulation engine, multi-tenant RBAC.
- **V3.0 (Q1 2028):** Full SaaS portal (React + TypeScript), automated franchise lead portal, predictive territory scoring AI.

---

## 13. Next Steps & Navigation

Ready to dive in? Choose your next destination:

- **New Analyst?** Head straight to 👉 **[docs/START-HERE.md](docs/START-HERE.md)**.
- **Ready for Day 1?** Open 👉 **[Section 7: First-Week Onboarding](docs/07-first-week-onboarding/README.md)**.
- **Looking for Tasks?** Check the 👉 **[Analyst Task Board](analyst-workspace/task-tracker/task-board.md)**.
- **Need Terminology?** Consult the 👉 **[Glossary](docs/GLOSSARY.md)**.
