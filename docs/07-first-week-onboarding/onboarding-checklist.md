# Data Analyst First-Week Onboarding Checklist

This interactive checklist tracks the onboarding progress of a new Data Analyst joining the **Franchise Business Modeling & Intelligence Platform**.

Each item must be completed and marked `[x]` sequentially across the five-day onboarding program.

---

## Analyst Profile
- **Analyst Name:** `[Your Name]`
- **Assigned Role:** `[Analyst 1: Strategy, Research & Documentation / Analyst 2: Financial Modeling & Intelligence]`
- **Onboarding Start Date:** `[YYYY-MM-DD]`
- **Peer Review Partner:** `[Peer Analyst Name]`
- **Onboarding Mentor / Lead:** `[Lead Name]`

---

## Day 1: Platform & Repository Orientation
- [ ] Read [docs/START-HERE.md](file:///d:/company/products/franchise-business-platform/docs/START-HERE.md).
- [ ] Read [platform/vision/platform-vision.md](file:///d:/company/products/franchise-business-platform/platform/vision/platform-vision.md).
- [ ] Studied [platform/architecture/system-architecture.md](file:///d:/company/products/franchise-business-platform/platform/architecture/system-architecture.md) and [platform/architecture/tenant-isolation.md](file:///d:/company/products/franchise-business-platform/platform/architecture/tenant-isolation.md).
- [ ] Read root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md) and memorized the 8 Cardinal Operating Rules.
- [ ] Verified local Python 3.10+ installation and activated virtual environment.
- [ ] Executed automated test suite: `python -m pytest tests/ -v` (100% passing).
- [ ] Executed repository validator: `python tools/validation/validate_repo.py` (0 errors).
- [ ] Confirmed understanding: `tmk-it-solutions` is a client, NOT the platform.

*Day 1 Sign-Off Date:* `____________` | *Analyst Initials:* `______`

---

## Day 2: Franchise Business Fundamentals
- [ ] Read [frameworks/franchise-model-design/franchise-archetypes-comparison.md](file:///d:/company/products/franchise-business-platform/frameworks/franchise-model-design/franchise-archetypes-comparison.md).
- [ ] Studied [frameworks/feasibility-analysis/financial-feasibility-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/feasibility-analysis/financial-feasibility-framework.md).
- [ ] Read [frameworks/revenue-sharing/configurable-revenue-sharing-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/revenue-sharing/configurable-revenue-sharing-framework.md).
- [ ] Read [frameworks/territory-intelligence/territory-intelligence-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/territory-intelligence/territory-intelligence-framework.md).
- [ ] Read [frameworks/investor-protection/investor-protection-framework.md](file:///d:/company/products/franchise-business-platform/frameworks/investor-protection/investor-protection-framework.md).
- [ ] Reviewed [docs/GLOSSARY.md](file:///d:/company/products/franchise-business-platform/docs/GLOSSARY.md).
- [ ] Completed Practical Exercise 2.1 (FOFO vs FOCO comparison).
- [ ] Completed Practical Exercise 2.2 (Pass-through statutory GST tax segregation math).
- [ ] Understood zero-deceptive earnings representations rule (Item 19 compliance).

*Day 2 Sign-Off Date:* `____________` | *Analyst Initials:* `______`

---

## Day 3: TMK Client Workspace & Commercial Assumptions
- [ ] Read [clients/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/AGENTS.md) and [clients/tmk-it-solutions/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/AGENTS.md).
- [ ] Read [clients/tmk-it-solutions/profile/company-overview.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/profile/company-overview.md).
- [ ] Inspected all 6 software products in [clients/tmk-it-solutions/products/products-catalog.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json).
- [ ] Read [clients/tmk-it-solutions/franchise-model/fofo-operating-model.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/franchise-model/fofo-operating-model.md).
- [ ] Audited commercial assumptions in [clients/tmk-it-solutions/financial-models/assumptions.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/financial-models/assumptions.json).
- [ ] Reviewed taluka/district expansion strategy in [clients/tmk-it-solutions/research/taluka-based-territory-strategy.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/research/taluka-based-territory-strategy.md).
- [ ] Inspected current deliverable approval status in [clients/tmk-it-solutions/approvals/approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md).

*Day 3 Sign-Off Date:* `____________` | *Analyst Initials:* `______`

---

## Day 4: Role-Specific Workflows & Practical Assignment

### For Analyst 1 (Business Strategy & Documentation)
- [ ] Studied [docs/05-analyst-playbooks/analyst-1-strategy-playbook.md](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md).
- [ ] Reviewed [analyst-workspace/research-methodology/research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md).
- [ ] Assigned sprint task card in [analyst-workspace/task-tracker/task-board.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md).
- [ ] Conducted market research and added an `EVD-*` verified empirical entry to the evidence register.
- [ ] Drafted assigned market research brief using standardized markdown template.
- [ ] Tagged document status as `[DRAFT]`.

### For Analyst 2 (Financial Modeling & Intelligence)
- [ ] Studied [docs/05-analyst-playbooks/analyst-2-finance-playbook.md](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md).
- [ ] Reviewed Decimal arithmetic guidelines in [docs/standards/financial-modeling-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/financial-modeling-standards.md).
- [ ] Assigned sprint task card in [analyst-workspace/task-tracker/task-board.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md).
- [ ] Executed Python CLI calculation engine across conservative, base, and optimistic scenarios.
- [ ] Generated dynamic Excel model using `python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel`.
- [ ] Verified that all generated formulas use valid uppercase syntax with zero hardcoded math.

*Day 4 Sign-Off Date:* `____________` | *Analyst Initials:* `______`

---

## Day 5: First Pull Request, Peer Review & Graduation
- [ ] Executed local automated test suite: `python -m pytest tests/ -v`.
- [ ] Executed local repository validator: `python tools/validation/validate_repo.py`.
- [ ] Created feature branch (`feat/<role>-<task-name>`).
- [ ] Pushed branch and opened GitHub Pull Request with completed PR description.
- [ ] Assigned counterpart peer analyst as reviewer.
- [ ] Conducted reciprocal peer review on counterpart's PR using [analyst-workspace/quality-checklists/pull-request-review-checklist.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/quality-checklists/pull-request-review-checklist.md).
- [ ] Resolved review feedback comments and achieved `[PEER APPROVED]` status.
- [ ] Updated task card in `analyst-workspace/task-tracker/task-board.md` to *Done*.
- [ ] Completed Onboarding Debrief with Project Lead.

*Day 5 Sign-Off Date:* `____________` | *Analyst Initials:* `______`

---

## Final Onboarding Graduation Sign-Off

The undersigned certify that the Analyst has successfully executed the complete five-day curriculum, demonstrated proficiency in platform architecture, adhered to data isolation and decimal arithmetic rules, and is fully qualified for autonomous project contribution.

- **Analyst Signature:** `___________________________` | **Date:** `____________`
- **Peer Reviewer Signature:** `______________________` | **Date:** `____________`
- **Lead / Mentor Signature:** `______________________` | **Date:** `____________`
