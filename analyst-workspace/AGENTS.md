# Analyst Workspace: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `analyst-workspace/` directory is the operational headquarters for the two data analysts driving business research, modeling, and client delivery:
- **Analyst 1 (Strategy, Research & Documentation):** Owns market research, competitor benchmarking, RACI design, pitch materials, and legal drafts.
- **Analyst 2 (Finance, Analytics & Intelligence):** Owns unit economics, Decimal calculation engines, Excel models, KPI tracking, and scenario sensitivity.

---

## 2. Specialized Agent Rules for `analyst-workspace/`

1. **Evidence Logging Integrity:**
   - Every market sizing metric, competitor pricing point, or enterprise demographic claim must have a corresponding citation in `analyst-workspace/research-methodology/research-evidence-register.md`.
   - Record author/publisher, publication year, source type, and key findings.
2. **Assumptions Register Maintenance:**
   - Any financial or operational modeling assumption must be logged in `analyst-workspace/research-methodology/assumptions-register.md`.
   - Every assumption must state: Assumption ID (`ASM-xxx`), client scope, category, parameter name, modeled value, unit, evidence source reference, and status tag (`[PROPOSED]`, `[WORKING HYPOTHESIS]`, `[ESTIMATED]`, or `[VERIFIED]`).
3. **Task Tracking Discipline:**
   - Update `analyst-workspace/task-tracker/task-board.md` when tasks change state (Open -> In Progress -> Review -> Done).
   - Every task must have an assigned owner (Analyst 1 or Analyst 2), target deliverable, status, and clear acceptance criteria.
4. **Peer Review Protocol:**
   - Review all pull requests against `analyst-workspace/quality-checklists/pull-request-review-checklist.md`.
   - Verify deliverable readiness using `analyst-workspace/quality-checklists/deliverable-acceptance-checklist.md`.
