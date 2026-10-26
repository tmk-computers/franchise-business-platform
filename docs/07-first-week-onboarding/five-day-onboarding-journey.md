# Five-Day Onboarding Journey: Fast-Track to Independent Productivity

Welcome to your first week on the **Franchise Business Modeling & Intelligence Platform**. 

This syllabus is engineered to take you from day-one orientation to submitting your first peer-reviewed pull request by the end of Friday. Every day is divided into clear learning objectives, structured reading materials, hands-on practical exercises, tangible outputs, completion criteria, and recommended time allocations.

---

## Weekly Schedule Overview

```text
Monday (Day 1)    → Platform Vision, Multi-Client Architecture & Repository Tour
Tuesday (Day 2)   → Franchise Economics, Archetypes, RACI & Statutory Tax Segregation
Wednesday (Day 3) → TMK IT Solutions Client Workspace, 6 Software Products & Commercial Terms
Thursday (Day 4)  → Role-Specific Playbook Mastery & First Practical Assignment Execution
Friday (Day 5)    → Pull Request Creation, Dual-Analyst Peer Review & Graduation Assessment
```

---

## Day 1: Platform & Repository Orientation

### Suggested Time Allocation: 7.5 Hours
- Morning (3.5h): Platform vision, multi-tenant architecture, and tenant isolation principles.
- Afternoon (4.0h): Local environment setup, directory exploration, and running test suites.

### 1. Learning Objectives
- Understand the core mission of the platform: transforming franchise expansion into an auditable, data-driven science.
- Master the **Client Independence Axiom**: `tmk-it-solutions` is the first client, NOT the platform itself.
- Verify your local Python development environment, install dependencies, and execute the automated test suite.
- Learn repository navigation and coding standards.

### 2. Reading Materials
1. [docs/START-HERE.md](file:///d:/company/products/franchise-business-platform/docs/START-HERE.md) (45 mins)
2. [platform/vision/platform-vision.md](file:///d:/company/products/franchise-business-platform/platform/vision/platform-vision.md) (30 mins)
3. [platform/architecture/system-architecture.md](file:///d:/company/products/franchise-business-platform/platform/architecture/system-architecture.md) (45 mins)
4. [platform/architecture/tenant-isolation.md](file:///d:/company/products/franchise-business-platform/platform/architecture/tenant-isolation.md) (30 mins)
5. [docs/standards/financial-modeling-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/financial-modeling-standards.md) (30 mins)
6. [Root AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md) (30 mins)

### 3. Practical Exercises
- **Exercise 1.1 — Environment Verification:**
  Open your shell and run:
  ```bash
  python --version  # Verify Python 3.10+
  python -m pytest tests/ -v
  python tools/validation/validate_repo.py
  ```
  Ensure all tests pass with zero warnings or errors.
- **Exercise 1.2 — Tenant Isolation Exploration:**
  Inspect `schemas/financial-assumptions.schema.json`. Verify that there are zero hardcoded references to "TMK" or "₹25,000".

### 4. Expected Outputs
- Verified local environment with 100% green test execution.
- Day 1 section marked in [onboarding-checklist.md](file:///d:/company/products/franchise-business-platform/docs/07-first-week-onboarding/onboarding-checklist.md).

### 5. Completion Criteria
- Analyst can explain why client data must never leak into `frameworks/` or `tools/`.
- Local test runner and validator output clean results.

---

## Day 2: Franchise Business Fundamentals

### Suggested Time Allocation: 7.5 Hours
- Morning (4.0h): Franchise archetypes (FOFO, FOCO, COCO, Master Franchise), RACI matrices, and unit economics.
- Afternoon (3.5h): Pass-through statutory tax handling, break-even math, and territory exclusivity rules.

### 1. Learning Objectives
- Master the operational and capital differences between FOFO, FOCO, COCO, and Master Franchises.
- Understand RACI governance matrices defining franchisor vs franchisee obligations.
- Master the statutory pass-through tax rule: 18% GST must be segregated before computing net revenue splits.
- Master unit break-even calculations and the 13 core franchise KPIs.

### 2. Reading Materials
1. [frameworks/franchise-model-design/franchise-archetypes-comparison.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-model-design/franchise-archetypes-comparison.md) (60 mins)
2. [frameworks/feasibility-analysis/financial-feasibility-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/feasibility-analysis/financial-feasibility-framework.md) (45 mins)
3. [frameworks/revenue-sharing/configurable-revenue-sharing-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/revenue-sharing/configurable-revenue-sharing-framework.md) (45 mins)
4. [frameworks/territory-intelligence/territory-intelligence-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/territory-intelligence/territory-intelligence-framework.md) (30 mins)
5. [frameworks/investor-protection/investor-protection-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/investor-protection/investor-protection-framework.md) (30 mins)
6. [docs/GLOSSARY.md](file:///d:/company/products/franchise-business-platform/docs/GLOSSARY.md) (30 mins)

### 3. Practical Exercises
- **Exercise 2.1 — Tax Segregation Math Exercise:**
  An enterprise client is invoiced ₹70,800 (tax inclusive at 18% GST) for a software license under a 40:60 split.
  In your scratch notes, compute:
  1. Net Realized Revenue: $70,800 / 1.18 = \text{₹}60,000$.
  2. Statutory GST Pass-Through: $70,800 - 60,000 = \text{₹}10,800$.
  3. Franchisee Share (40%): $60,000 \times 0.40 = \text{₹}24,000$.
  4. Franchisor Share (60%): $60,000 \times 0.60 = \text{₹}36,000$.
- **Exercise 2.2 — RACI Matrix Audit:**
  Inspect the RACI matrix in `frameworks/franchise-model-design/franchise-archetypes-comparison.md` and identify who is Accountable (A) for Core Software Bug Fixes vs Local Client Demos.

### 4. Expected Outputs
- Completed tax segregation calculation written in scratch notes.
- Summary of FOFO vs FOCO trade-offs logged in onboarding notebook.

### 5. Completion Criteria
- Perfect understanding that commission splits are NEVER computed on tax-inclusive gross billing.
- Ability to explain why earnings representations must be strictly labeled as illustrative scenarios.

---

## Day 3: TMK Client Workspace & Commercial Assumptions

### Suggested Time Allocation: 7.5 Hours
- Morning (4.0h): Deep-dive into TMK IT Solutions LLP workspace, profile, leadership, and 6 software products.
- Afternoon (3.5h): Financial assumptions inspection, commercial terms analysis, and approval matrix review.

### 1. Learning Objectives
- Understand TMK IT Solutions LLP as the platform's inaugural client.
- Master TMK's 6 software products: Enterprise ERP, School Management, Hospital ERP, Retail POS, DevOps Automation, and Cybersecurity Suite.
- Understand TMK's FOFO commercial terms:
  - Promotional joining fee: ₹25,000 (first 10 units).
  - Standard joining fee: ₹50,000.
  - Net revenue sharing split: 40% Franchisee : 60% TMK IT Solutions.
  - Working capital cushion: ₹50,000–₹1,00,000.
- Understand Indian administrative boundary mapping (Talukas / Tehsils) for territory strategy.

### 2. Reading Materials
1. [clients/tmk-it-solutions/profile/company-overview.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/profile/company-overview.md) (45 mins)
2. [clients/tmk-it-solutions/products/products-catalog.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json) (45 mins)
3. [clients/tmk-it-solutions/franchise-model/fofo-operating-model.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/franchise-model/fofo-operating-model.md) (45 mins)
4. [clients/tmk-it-solutions/financial-models/assumptions.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/financial-models/assumptions.json) (45 mins)
5. [clients/tmk-it-solutions/research/taluka-based-territory-strategy.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/research/taluka-based-territory-strategy.md) (30 mins)
6. [clients/tmk-it-solutions/approvals/approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md) (15 mins)

### 3. Practical Exercises
- **Exercise 3.1 — Product Catalog Inspection:**
  Open `clients/tmk-it-solutions/products/products-catalog.json`. Review each product's target industry vertical, annual base price, and delivery model.
- **Exercise 3.2 — Baseline Assumptions Audit:**
  Open `clients/tmk-it-solutions/financial-models/assumptions.json`. Locate the 3 scenarios (`conservative`, `base`, `optimistic`). Note the monthly sales velocity and renewal retention rate for each.

### 4. Expected Outputs
- Completed product comparison sheet comparing pricing across all 6 TMK products.
- Day 3 sign-off in [onboarding-checklist.md](file:///d:/company/products/franchise-business-platform/docs/07-first-week-onboarding/onboarding-checklist.md).

### 5. Completion Criteria
- Ability to articulate TMK's commercial value proposition to a prospective franchisee.
- Clear understanding of TMK's approval matrix status.

---

## Day 4: Role-Specific Execution & First Practical Assignment

### Suggested Time Allocation: 8.0 Hours
- Morning (2.5h): Role-specific playbook deep-dive (Analyst 1 or Analyst 2).
- Rest of Day (5.5h): Executing your first practical sprint assignment.

### 1. Learning Objectives
- Master your designated playbook:
  - If Analyst 1: [docs/05-analyst-playbooks/analyst-1-strategy-playbook.md](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md).
  - If Analyst 2: [docs/05-analyst-playbooks/analyst-2-finance-playbook.md](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md).
- Understand how your deliverables link with the evidence and assumptions registers.
- Complete your first assigned task independently.

### 2. Reading Materials
- **Analyst 1:** Read [Analyst 1 Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md) and [templates/market-research/market-research-report.template.md](file:///d:/company/products/franchise-business-platform/templates/market-research/market-research-report.template.md).
- **Analyst 2:** Read [Analyst 2 Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md) and [tools/financial-modeling/cli.py](file:///d:/company/products/franchise-business-platform/tools/financial-modeling/cli.py).

### 3. Practical Assignment by Role

#### For Analyst 1 (Business Strategy): Market Research Brief
1. Pick task `TASK-A1-04` from `analyst-workspace/task-tracker/task-board.md`.
2. Research hospital & healthcare clinic ERP adoption in Tier-2 Indian districts.
3. Add a verified empirical entry to `analyst-workspace/research-methodology/research-evidence-register.md` (`EVD-MKT-006`).
4. Draft `clients/tmk-it-solutions/research/healthcare-erp-market-brief.md` using the standard template.
5. Include TAM, SAM, SOM, and competitor positioning against legacy hospital software.

#### For Analyst 2 (Financial Modeling): Scenario Run & Excel Generation
1. Pick task `TASK-A2-05` from `analyst-workspace/task-tracker/task-board.md`.
2. Inspect `clients/tmk-it-solutions/financial-models/assumptions.json`.
3. Execute the CLI calculation engine for all 3 scenarios:
   ```bash
   python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario conservative
   python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario base
   python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario optimistic
   ```
4. Generate the dynamic Excel financial model:
   ```bash
   python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel
   ```
5. Inspect the generated Excel file in `clients/tmk-it-solutions/financial-models/` to verify uppercase formulas.

### 4. Expected Outputs
- **Analyst 1:** Completed draft `healthcare-erp-market-brief.md` with active `EVD-*` citations.
- **Analyst 2:** Generated Excel model and summary log of 36-month EBITDA and payback metrics.

### 5. Completion Criteria
- Deliverable is 100% complete with zero unfilled placeholders or unexplained `# TODO` items.

---

## Day 5: First Pull Request, Peer Review & Assessment

### Suggested Time Allocation: 7.0 Hours
- Morning (3.0h): Local quality checks, branch creation, and opening your first GitHub Pull Request.
- Afternoon (4.0h): Cross-disciplinary peer review, resolving review feedback, and completing the week-1 assessment.

### 1. Learning Objectives
- Master the platform's Git PR workflow: branch naming, PR descriptions, and CI check adherence.
- Conduct a rigorous peer review on your counterpart's deliverable using standardized acceptance checklists.
- Address peer review comments constructively and push clean revision commits.
- Complete the onboarding assessment and graduate to active sprint contributor.

### 2. Reading Materials
1. [docs/06-quality-and-approval/standard-work-journey.md](file:///d:/company/products/franchise-business-platform/docs/06-quality-and-approval/standard-work-journey.md) (45 mins)
2. [analyst-workspace/review-process/peer-review-workflow.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/review-process/peer-review-workflow.md) (30 mins)
3. [analyst-workspace/quality-checklists/pull-request-review-checklist.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/quality-checklists/pull-request-review-checklist.md) (20 mins)

### 3. Practical Exercises
- **Exercise 5.1 — Automated Self-Validation:**
  Before committing your work, run the automated validation suite:
  ```bash
  python -m pytest tests/ -v
  python tools/validation/validate_repo.py
  ```
  Confirm 0 errors.
- **Exercise 5.2 — Branch & PR Creation:**
  ```bash
  git checkout -b feat/<role>-onboarding-assignment
  git add .
  git commit -m "feat(onboarding): complete day-4 practical assignment"
  ```
  Open a pull request linking your assignment task ID.
- **Exercise 5.3 — Peer Review Simulation:**
  Swap PRs with your peer analyst:
  - Analyst 1 reviews Analyst 2's model for business logic and fee alignment.
  - Analyst 2 reviews Analyst 1's market brief for numerical claims and price consistency.
  - Leave at least 2 constructive comments and verify all checklist points.

### 4. Expected Outputs
- Merged or peer-approved pull request.
- Completed peer review feedback log.
- Signed-off [onboarding-checklist.md](file:///d:/company/products/franchise-business-platform/docs/07-first-week-onboarding/onboarding-checklist.md).

### 5. Completion Criteria & Graduation
- All 5 daily modules completed and signed off.
- Successful execution of automated quality checks.
- Formal graduation logged in `analyst-workspace/task-tracker/task-board.md` moving you to active project status!
