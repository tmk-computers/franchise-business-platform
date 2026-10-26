# Section 5: Analyst Playbooks & Execution Recipes

## Purpose
This section houses the role-specific execution playbooks for the two primary Data Analyst roles on the platform:
- **Analyst 1:** Business Strategy, Market Research & Commercial Documentation.
- **Analyst 2:** Financial Modeling, Quantitative Analytics & Intelligence.

Each playbook provides end-to-end, step-by-step workflows, deliverable templates, input/output paths, and validation recipes so an analyst can produce production-grade outputs autonomously.

---

## Prerequisites
- Completed [Section 1: Platform Orientation](file:///d:/company/products/franchise-business-platform/docs/01-platform-orientation/README.md) through [Section 4: Client Workspaces](file:///d:/company/products/franchise-business-platform/docs/04-client-workspaces/README.md).
- Python 3.10+ environment initialized.
- Understanding of the Dual-Analyst Review mechanism ([docs/GLOSSARY.md#dual-analyst-review](file:///d:/company/products/franchise-business-platform/docs/GLOSSARY.md#dual-analyst-review)).

---

## Playbook Navigation

Choose your assigned role to access your dedicated execution manual:

```text
docs/05-analyst-playbooks/
├── README.md                          # This orientation guide
├── analyst-1-strategy-playbook.md     # Strategy, Research & Documentation Playbook
└── analyst-2-finance-playbook.md      # Financial Modeling, Analytics & Intelligence Playbook
```

| Playbook | Core Domain & Focus | Key Deliverables Produced |
|---|---|---|
| [Analyst 1: Strategy Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md) | Business strategy, market sizing, competitive intelligence, legal drafts, brochures, pitch decks, and operations manuals. | Research briefs, evidence register, franchise agreements, SOP manuals, investor prospectuses, pitch decks. |
| [Analyst 2: Finance Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md) | Financial engineering, unit economics, Decimal-safe calculations, 36-month P&L forecasts, break-even, and Excel generation. | `assumptions.json`, financial projection summaries, dynamic Excel workbooks, sensitivity matrices, KPI dashboards. |

---

## Reading Sequence

1. Read this README to understand how the two analyst roles interface.
2. Open your specific role playbook:
   - If assigned to Business Strategy: [Analyst 1 Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-1-strategy-playbook.md).
   - If assigned to Financial Modeling: [Analyst 2 Playbook](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/analyst-2-finance-playbook.md).
3. Read the counterpart playbook to understand how your work will be peer-reviewed and integrated.
4. Review [analyst-workspace/task-tracker/task-board.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md) to inspect active sprint tasks.

---

## Relevant Repository Links

| Operational Tool / File | Purpose |
|---|---|
| [analyst-workspace/AGENTS.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/AGENTS.md) | Dual-analyst operational rules and governance constraints |
| [analyst-workspace/task-tracker/task-board.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md) | Active task assignments and backlog |
| [analyst-workspace/research-methodology/research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md) | Empirical evidence log for Analyst 1 & 2 |
| [analyst-workspace/research-methodology/assumptions-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/assumptions-register.md) | Numerical assumptions log for quantitative models |
| [analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md) | Formal acceptance criteria before PR submission |

---

## Learning Outcomes

Upon completing this section, an analyst will be able to:
1. **Execute Role Workflows End-to-End:** Follow step-by-step deliverable recipes without ambiguous gaps.
2. **Conduct Rigorous Dual-Analyst Peer Reviews:** Review counterpart deliverables for qualitative realism and quantitative integrity.
3. **Execute Automation Tools Correctly:** Run the Python financial calculator, Excel generator, and pitch deck builder using verified command-line invocations.
4. **Log Evidence and Assumptions:** Trace every business claim back to the evidence register and assumptions register.

---

## Practical Exercises

### Exercise 5.1: Review the Active Task Board
Open [analyst-workspace/task-tracker/task-board.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/task-tracker/task-board.md). Identify the current sprint tasks assigned to Analyst 1 and Analyst 2. Note how tasks transition between `Backlog`, `In Progress`, `Peer Review`, `Client Approval`, and `Done`.

---

## Completion Checklist

- [ ] Reviewed this section's overview and structure.
- [ ] Read your primary role playbook thoroughly.
- [ ] Skimmed your counterpart's playbook to understand cross-review obligations.
- [ ] Located your role's task assignments in the task tracker.

---

## Next Recommended Section

Proceed to [Section 6: Quality, Review & Approval](file:///d:/company/products/franchise-business-platform/docs/06-quality-and-approval/README.md) to master the 10-stage contribution lifecycle and quality gates.
