# Section 6: Quality Assurance, Review & Approval

## Purpose
This section establishes the quality standards, review gates, and formal sign-off procedures governing all work on the **Franchise Business Modeling & Intelligence Platform**. It provides an exhaustive guide to the 10-stage contribution lifecycle, details how dual-analyst peer reviews function, explains how automated quality gates protect repository integrity, and defines how deliverables transition from initial drafts to approved corporate assets.

---

## Prerequisites
- Completed [Section 1: Platform Orientation](file:///d:/company/products/franchise-business-platform/docs/01-platform-orientation/README.md) through [Section 5: Analyst Playbooks](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/README.md).
- Understanding of Git pull request mechanics and CI validation workflows.

---

## Reading Sequence

Follow this reading sequence:

1. [docs/06-quality-and-approval/standard-work-journey.md](file:///d:/company/products/franchise-business-platform/docs/06-quality-and-approval/standard-work-journey.md) — The 10-stage contribution lifecycle from task assignment to release, featuring concrete walkthroughs for Analyst 1 and Analyst 2.
2. [analyst-workspace/review-process/peer-review-workflow.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/review-process/peer-review-workflow.md) — Cross-disciplinary peer review protocols, criteria, and feedback loops between Analyst 1 and Analyst 2.
3. [analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md) — The 10-point acceptance criteria checklist required before PR merging.
4. [analyst-workspace/quality-checklists/pull-request-review-checklist.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/quality-checklists/pull-request-review-checklist.md) — Technical and formatting review criteria for code and documentation PRs.
5. [clients/tmk-it-solutions/approvals/approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md) — Formal approval matrix tracking client stakeholder sign-offs.

---

## Relevant Repository Links

| Quality Tool / Standard | Description |
|---|---|
| [Root AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md) | Authoritative operating rules, review mandates, and decimal math requirements |
| [docs/standards/financial-modeling-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/financial-modeling-standards.md) | Precision guidelines for financial calculations |
| [docs/standards/documentation-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/documentation-standards.md) | Formatting, link syntax, and deliverable status labeling |
| [tools/validation/validate_repo.py](file:///d:/company/products/franchise-business-platform/tools/validation/validate_repo.py) | Automated integrity verification tool |
| [tests/](file:///d:/company/products/franchise-business-platform/tests/) | Full automated test suite (Pytest) |

---

## Learning Outcomes

Upon completing this section, an analyst will be able to:
1. **Navigate the 10-Stage Lifecycle:** Execute any assignment through the full journey from backlog assignment to final approved release.
2. **Conduct Constructive Peer Reviews:** Review counterpart deliverables using objective checklists without personal friction.
3. **Execute Self-Validation:** Run automated tests and linting tools before opening pull requests to guarantee a 100% clean CI pipeline.
4. **Manage Document Status Tags:** Correctly apply status labels (`[DRAFT]`, `[WORKING DISCUSSION DRAFT]`, `[PEER APPROVED]`, `[MODELING APPROVED]`, `[CLIENT APPROVED]`).
5. **Feed Framework Enhancements:** Understand how client-specific discoveries are abstracted and backported into generic frameworks without violating tenant isolation.

---

## Practical Exercises

### Exercise 6.1: Run Repository Quality Validation
Execute the platform's automated quality validator in your terminal:
```bash
python tools/validation/validate_repo.py
```
Verify that all schema validations, file existence checks, and internal Markdown link checks complete with `0 errors`.

### Exercise 6.2: Inspect Deliverable Status Matrix
Open [clients/tmk-it-solutions/approvals/approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md). Review the current status of the 10 listed TMK deliverables. Identify which deliverables are in `Approved` status and which remain in `Draft` or `Pending Sign-off`.

---

## Completion Checklist

- [ ] Read `standard-work-journey.md` thoroughly.
- [ ] Studied `analyst-workspace/review-process/peer-review-workflow.md`.
- [ ] Ran `python tools/validation/validate_repo.py` with zero errors.
- [ ] Understand the 5 deliverable status levels and when each is applied.

---

## Next Recommended Section

Proceed to [Section 7: First-Week Onboarding Journey](file:///d:/company/products/franchise-business-platform/docs/07-first-week-onboarding/README.md) to begin your structured five-day onboarding curriculum.
