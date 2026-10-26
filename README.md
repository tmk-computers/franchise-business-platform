# Franchise Business Modeling & Intelligence Platform (V0.1)

A systematic, client-independent, and industry-agnostic platform engineered to research, design, evaluate, document, visualize, pitch, launch, and optimize franchise business models.

---

## 1. Executive Overview & Platform Vision

Franchising is one of the most effective scaling mechanisms for modern enterprises. However, traditional franchise modeling is plagued by fragmented spreadsheets, unverified commercial assumptions, unrealistic earnings claims, poorly defined unit economics, and lack of operational standardization. 

The **Franchise Business Modeling & Intelligence Platform** transforms franchise expansion from intuitive guesswork into an auditable, data-driven discipline. By combining rigorous financial engineering, standardized operational frameworks, structured market intelligence, and automated document generation, the platform enables enterprises and franchise advisory teams to rapidly evaluate feasibility, design sustainable revenue-sharing models, and deploy franchise networks with confidence.

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

## 5. Repository Organization

```text
franchise-business-platform/
│
├── README.md                          # Repository overview & quickstart
├── AGENTS.md                          # Operational instructions for AI assistants
├── CONTRIBUTING.md                    # Contribution guidelines & branch workflows
├── CHANGELOG.md                       # Release notes and version history
├── LICENSE-DECISION.md                # IP, licensing, and proprietary classification
├── .gitignore                         # Git exclusion rules
├── .editorconfig                      # Coding and formatting standards
├── .github/                           # CI workflows and PR templates
│
├── platform/                          # Platform vision, PRDs, SaaS architecture & roadmap
│   ├── vision/                        # Strategic objectives and core capabilities
│   ├── product-requirements/          # Product requirement documents (PRD V0.1)
│   ├── architecture/                  # Multi-tenant SaaS architecture & system design
│   ├── data-models/                   # Domain entities and relationship documentation
│   ├── security/                      # Confidentiality guidelines & access controls
│   └── roadmap/                       # Roadmap for V1.0, V2.0, and V3.0
│
├── frameworks/                        # Reusable, client-agnostic business frameworks
│   ├── franchise-model-design/        # Archetype comparisons, RACI matrices & selection
│   ├── feasibility-analysis/          # Financial feasibility, unit economics, payback
│   ├── market-research/               # Market sizing, competitive benchmarking methodology
│   ├── financial-modeling/            # Mathematical standards & modeling conventions
│   ├── revenue-sharing/               # Parameterized commission, fee splits & tiering
│   ├── territory-intelligence/        # Territory segmentation, density & conflict prevention
│   ├── investor-protection/           # Transparency, risk disclosure & fair exit policies
│   ├── risk-assessment/               # Franchise risk taxonomy & mitigation playbooks
│   ├── franchise-operations/          # Operations manual architecture & quality standards
│   ├── performance-analytics/         # 13 core KPIs, metrics taxonomy & benchmarking
│   └── franchise-expansion/           # Phased rollout waves & scaling strategy
│
├── templates/                         # Standardized document and presentation templates
│   ├── business-plans/                # Franchise business plan templates
│   ├── market-research/               # Market analysis & territory report templates
│   ├── financial-models/              # Feasibility & P&L narrative templates
│   ├── franchise-agreements/          # Master franchise agreement legal templates
│   ├── legal-policies/                # Revenue-sharing, territory & IP policy templates
│   ├── investor-presentations/        # Pitch deck outlines & investor risk disclosures
│   ├── brochures/                     # Franchise opportunity brochure templates
│   ├── product-demonstrations/        # Demo scripts & presentation kits
│   ├── sales-playbooks/               # Sales training & franchise recruitment playbooks
│   ├── operations-manuals/            # Unit operations handbooks
│   ├── dashboards/                    # Executive KPI dashboard specifications
│   ├── checklists/                    # Onboarding, due diligence & review checklists
│   └── management-reports/            # Weekly & executive reporting templates
│
├── industry-models/                   # Vertical-specific franchise economics & benchmarks
│   ├── software/                      # SaaS & IT services recurring revenue models
│   ├── food-beverage/                 # QSR, café, kitchen supply-chain models
│   ├── retail/                        # Store inventory, footfall & merchandise models
│   ├── education/                     # K-12, coaching, test prep institution models
│   ├── healthcare/                    # Clinics, diagnostic labs & pharmacy models
│   ├── real-estate/                   # Brokerage & property management networks
│   ├── manufacturing/                 # Contract manufacturing & fabrication models
│   └── professional-services/         # Staffing, accounting & consulting agencies
│
├── clients/                           # Client-specific workspaces (strictly isolated)
│   └── tmk-it-solutions/              # Initial client: TMK IT Solutions LLP
│       ├── profile/                   # Client overview & commercial assumptions
│       ├── products/                  # 6 software product profiles & catalog
│       ├── research/                  # Market demand, competitive & territory briefs
│       ├── franchise-model/           # FOFO architecture, RACI & revenue rules
│       ├── financial-models/          # Projections & live-formula Excel workbook
│       ├── territory-analysis/        # Indian taluka & district expansion strategy
│       ├── presentations/             # Franchise opportunity pitch deck & PowerPoint
│       ├── sales-marketing/           # Brochure, prospectus, FAQ & infographics
│       ├── legal-drafts/              # Non-final agreement and policy drafts
│       ├── operations/                # Operating handbook & support SLA matrix
│       ├── risks/                     # Client-specific risk register
│       ├── decisions/                 # Management decision log
│       ├── approvals/                 # Commercial sign-off matrix
│       └── deliverables/              # Finalized and approved client assets
│
├── schemas/                           # JSON Schema data contracts
│   ├── client.schema.json             # Client profile data contract
│   ├── product.schema.json            # Product catalog contract
│   ├── franchise-model.schema.json    # Franchise structure contract
│   ├── financial-assumptions.schema.json # Modeling parameters contract
│   ├── revenue-sharing.schema.json    # Revenue sharing logic contract
│   ├── research-source.schema.json    # Research evidence tracking contract
│   └── deliverable.schema.json        # Client deliverable tracking contract
│
├── tools/                             # Automation tools and calculation engines
│   ├── financial-modeling/            # Python Decimal engine & openpyxl workbook generator
│   ├── validation/                    # Repository integrity & schema validation scripts
│   ├── document-generation/           # Automated presentation & document generators
│   └── reporting/                     # Summary & metrics reporting tools
│
├── analyst-workspace/                 # Dual-analyst operational command center
│   ├── onboarding/                    # Analyst onboarding guides & 6-week plan
│   ├── assignments/                   # Analyst 1 & Analyst 2 backlogs
│   ├── task-tracker/                  # Centralized operational task board
│   ├── research-methodology/          # Evidence standards & assumptions register
│   ├── quality-checklists/            # PR review & deliverable acceptance checklists
│   ├── weekly-reports/                # Progress reports & weekly templates
│   └── review-process/                # Peer-review & sign-off workflow
│
├── docs/                              # Global documentation & standards
│   ├── getting-started/               # Quickstart guide for new engineers/analysts
│   ├── standards/                     # Mathematical & documentation standards
│   ├── glossary/                      # Standardized franchise terminology
│   └── implementation-guides/         # Client onboarding playbook
│
└── tests/                             # Comprehensive automated test suite
    ├── test_financial_calculator.py   # Unit tests for Decimal math & revenue sharing
    ├── test_excel_generator.py        # Validation of generated Excel workbook formulas
    ├── test_schemas.py                # Schema validation for all JSON configurations
    └── test_repo_integrity.py         # Structural, file, and link integrity tests
```

---

## 6. How to Onboard a New Client

To onboard a new corporate client:
1. **Create Client Workspace:**
   Create a new directory under `clients/<client-identifier>/` mirroring the standard client workspace layout.
2. **Populate Client Profile:**
   Create `profile/client.json` adhering to `schemas/client.schema.json`.
3. **Define Product Catalog:**
   Document products in `products/` and configure `products/products-catalog.json` adhering to `schemas/product.schema.json`.
4. **Configure Commercial & Financial Assumptions:**
   Define franchise fees, fee waivers, revenue splits, operating costs, and tax treatments in `financial-models/assumptions.json` adhering to `schemas/financial-assumptions.schema.json`.
5. **Generate Financial Model:**
   Run the financial modeling toolkit to generate projections and the editable Excel workbook:
   ```bash
   python tools/financial-modeling/cli.py --client <client-identifier> --output-dir clients/<client-identifier>/financial-models/
   ```
6. **Execute Validation Checks:**
   Verify client configuration using `python tools/validation/validate_repo.py`.

---

## 7. How to Create a Financial Model

1. **Review and Update Assumptions:** Edit `clients/<client-name>/financial-models/assumptions.json`.
2. **Execute the Python Engine:**
   ```bash
   # Run model calculations and output JSON projection summary:
   python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario base

   # Generate the comprehensive Excel workbook with dynamic formulas:
   python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel
   ```
3. **Inspect the Generated Workbook:**
   The output workbook (`clients/<client-name>/financial-models/<client-name>_franchise_financial_model.xlsx`) contains dynamic Excel formulas for:
   - Assumptions & Product Pricing
   - Franchisee Initial Investment & Working Capital
   - Monthly Sales & Renewal Projections (36-month horizon)
   - Franchisee P&L & Cash Flow
   - Franchisor Central P&L & Royalty Settlement
   - Break-Even Analysis & Sensitivity Scenarios

---

## 8. How to Create a Franchise Pitch Package

1. **Synthesize Research & Value Proposition:** Review research briefs in `clients/<client-name>/research/`.
2. **Instantiate Document Templates:** Use `templates/investor-presentations/` and `templates/brochures/`.
3. **Generate PowerPoint Pitch Deck:**
   ```bash
   python tools/document-generation/generate_pitch_deck.py --client tmk-it-solutions
   ```
4. **Draft Franchise Prospectus and FAQ:** Complete the narrative documents in `clients/<client-name>/sales-marketing/`.

---

## 9. How Analysts Should Contribute

The workspace supports two dedicated data analysts working concurrently:
- **Analyst 1 (Strategy, Research & Documentation):** Drives market research briefs, competitor benchmarking, franchise agreements, operational handbooks, and pitch materials. Tracks research in `analyst-workspace/research-methodology/research-evidence-register.md`.
- **Analyst 2 (Finance, Analytics & Intelligence):** Builds unit economics, refines assumptions in `assumptions.json`, validates break-even calculations, models sensitivity scenarios, and monitors KPI benchmarks.

Both analysts collaborate through `analyst-workspace/task-tracker/task-board.md` and execute peer reviews before submitting pull requests.

---

## 10. Document Review & Quality Gates

Every document and model must pass through the four-stage review pipeline:
1. **Draft:** Initial creation by assigned analyst with assumption tags.
2. **Peer Review:** Cross-functional review between Analyst 1 and Analyst 2.
3. **Validation Gate:** Automated CI test suite passes with zero errors.
4. **Client Approval:** Final sign-off logged in `clients/<client-name>/approvals/approval-matrix.md`.

---

## 11. Automated Validation Tools

Run the full automated test suite locally:
```bash
# Run pytest unit tests:
pytest tests/

# Run repository integrity and schema validation:
python tools/validation/validate_repo.py
```

The validation suite enforces:
- Strict JSON Schema validation across all client datasets.
- Decimal arithmetic precision and consistency across scenarios.
- Existence of mandatory client files and deliverable structures.
- Integrity of all internal Markdown relative links.

---

## 12. Implementation Status & Future Roadmap

### Current Status (V0.1 Bootstrap)
- [x] Repository foundation, licensing, and CI workflows established.
- [x] Complete generic franchise frameworks documented across 11 core domains.
- [x] Reusable Python financial modeling engine with dynamic Excel workbook generator.
- [x] Complete workspace for inaugural client: **TMK IT Solutions LLP**.
- [x] Profiles for all 6 TMK software products with target customer analysis.
- [x] Configurable FOFO commercial terms (Promotional ₹25,000 / Regular ₹50,000 fees; 40:60 revenue sharing).
- [x] Automated PowerPoint deck generator and editable Excel financial model.
- [x] Operational workspace for two Data Analysts with 6-week roadmap and task trackers.
- [x] 15+ institutional document and presentation templates.

### Roadmap Outlook
- **V1.0 (Q1 2027):** Multi-client support, interactive territory mapping CLI, automated PDF deliverable compiler.
- **V2.0 (Q3 2027):** Cloud-native backend (ASP.NET Core Web API + PostgreSQL), real-time financial simulation engine, multi-tenant RBAC.
- **V3.0 (Q1 2028):** Full SaaS portal (React + TypeScript), automated franchise lead portal, predictive territory scoring AI.
