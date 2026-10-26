# Changelog

All notable changes to the Franchise Business Modeling & Intelligence Platform will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-10-26

### Added
- **Repository Architecture & Bootstrap:**
  - Initial repository structure supporting client-agnostic franchise modeling.
  - Comprehensive `.editorconfig`, `.gitignore`, and `LICENSE-DECISION.md`.
  - Continuous integration workflows for automated testing and schema validation.
- **Generic Franchise Business Frameworks:**
  - Comprehensive model comparison framework (FOFO, FOCO, COCO, COFO, Master, Area Dev, Multi-Unit, Sales, Hybrid).
  - Financial feasibility and unit economics framework with decimal-precision arithmetic standards.
  - Market research, territory intelligence, investor protection, risk assessment, operations, and expansion frameworks.
- **Python-based Financial Modeling Toolkit (`tools/financial-modeling/`):**
  - Decimal-safe calculation engine (`calculator.py`) supporting joining fees, product sales, configurable revenue shares, expense modeling, break-even, ROI, and scenario projections.
  - Automated openpyxl Excel generator (`excel_generator.py`) building live-formula financial model workbooks.
  - CLI utility (`cli.py`) for automated model runs, scenario analysis, and Excel exports.
- **Validation Engine & Automated Quality Checks (`tools/validation/`):**
  - Schema validator for JSON data contracts (`schemas/`).
  - Markdown relative link checker and structure verification scripts.
  - Unit test suite (`tests/`) covering financial calculation accuracy, Excel generator output, and schema compliance.
- **First Client Workspace (`clients/tmk-it-solutions/`):**
  - Client profile for TMK IT Solutions LLP with FOFO operational architecture.
  - Six comprehensive product profiles: School/College ERP, Invoicing App+Web, OMR Software, Property Management ERP, DevOps Automation, Sales CRM.
  - Configurable commercial assumptions (Promotional ₹25,000 / Regular ₹50,000 joining fee; 40% franchisee / 60% franchisor revenue split).
  - Pre-generated editable financial workbook (`tmk_franchise_financial_model.xlsx`).
  - 6 market research briefs, starter slide-by-slide pitch deck specification and generated PowerPoint (`franchise-opportunity-pitch-deck.pptx`), franchise prospectus, brochure, FAQ, and non-final working legal drafts.
- **Analyst Workspace (`analyst-workspace/`):**
  - Onboarding guide, role demarcation (Analyst 1: Strategy/Research vs. Analyst 2: Finance/Analytics).
  - 6-week operational work plan, centralized task board, assumptions register, research evidence register, risk register, and management decision log.
- **Reusable Templates & Standards (`templates/`, `docs/`):**
  - 15+ comprehensive reusable templates across business plans, feasibility reports, legal agreements, pitch decks, operations manuals, and checklists.
  - Architectural roadmap for future SaaS implementation (React + TypeScript, ASP.NET Core, PostgreSQL, Python analytics).
