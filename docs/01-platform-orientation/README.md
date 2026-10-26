# Section 1: Platform Orientation & Architecture

## Purpose
This section establishes foundational understanding of the **Franchise Business Modeling & Intelligence Platform**. It clarifies the core architectural axiom of the repository: **client independence**. New analysts will understand why the platform exists, who uses it, how reusable analytical frameworks operate across multiple industries, and why TMK IT Solutions LLP is the inaugural client workspace rather than the platform itself.

---

## Prerequisites
- Basic familiarity with repository navigation and Git version control.
- Read the root [START-HERE.md](file:///d:/company/products/franchise-business-platform/docs/START-HERE.md) document.

---

## Reading Sequence

Follow this reading order to build systematic understanding:

1. [docs/START-HERE.md](file:///d:/company/products/franchise-business-platform/docs/START-HERE.md) — The centralized executive gateway for onboarding analysts.
2. [platform/vision/platform-vision.md](file:///d:/company/products/franchise-business-platform/platform/vision/platform-vision.md) — The strategic vision, business rationale, and platform value proposition.
3. [platform/product-requirements/prd-v0.1.md](file:///d:/company/products/franchise-business-platform/platform/product-requirements/prd-v0.1.md) — Product Requirements Document (PRD) detailing functional capabilities and user personas.
4. [platform/architecture/system-architecture.md](file:///d:/company/products/franchise-business-platform/platform/architecture/system-architecture.md) — Multi-tenant architecture, component layers, and system data flows.
5. [platform/architecture/tenant-isolation.md](file:///d:/company/products/franchise-business-platform/platform/architecture/tenant-isolation.md) — Strict security boundaries, data segregation, and client confidentiality rules.
6. [platform/roadmap/roadmap-v1-to-v3.md](file:///d:/company/products/franchise-business-platform/platform/roadmap/roadmap-v1-to-v3.md) — Evolution timeline from V0.1 analytical engine to V3.0 full SaaS portal.

---

## Relevant Repository Links

| Document / Asset | Description |
|---|---|
| [Root README.md](file:///d:/company/products/franchise-business-platform/README.md) | High-level repository overview and directory architecture |
| [Root AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md) | Authoritative operating rules and client independence axioms |
| [platform/AGENTS.md](file:///d:/company/products/franchise-business-platform/platform/AGENTS.md) | Instructions governing platform architecture modifications |
| [docs/DOCUMENTATION-MAP.md](file:///d:/company/products/franchise-business-platform/docs/DOCUMENTATION-MAP.md) | Complete directory tree and file index |
| [docs/GLOSSARY.md](file:///d:/company/products/franchise-business-platform/docs/GLOSSARY.md) | Centralized franchise, financial, and technical glossary |

---

## Learning Outcomes

Upon completing this section, an analyst will be able to:
1. **Explain the Platform's Raison d'Être:** Articulate why traditional spreadsheet-based franchising fails and how data-driven modeling de-risks expansion for franchisors and franchisees.
2. **Defend Client Independence:** Clearly separate generic platform engines (`frameworks/`, `schemas/`, `tools/`) from client workspaces (`clients/tmk-it-solutions/`).
3. **Identify Target Personas:** Detail the needs of Corporate Strategy Executives, Franchise Advisors, Financial Analysts, and Prospective Franchisees.
4. **Enforce Tenant Isolation:** Ensure no client-specific financial figures (such as TMK's 40:60 revenue share or ₹25,000 joining fee) are ever hardcoded into platform tools.
5. **Navigate the Platform Roadmap:** Understand current V0.1 file-driven capabilities versus future V1.0–V3.0 web API and SaaS milestones.

---

## Practical Exercises

### Exercise 1.1: Tenant Isolation Audit
Open [platform/architecture/system-architecture.md](file:///d:/company/products/franchise-business-platform/platform/architecture/system-architecture.md) and [platform/architecture/tenant-isolation.md](file:///d:/company/products/franchise-business-platform/platform/architecture/tenant-isolation.md). In your local scratchpad, list the three layers of isolation enforced between reusable modules and client workspaces. Verify that `schemas/financial-assumptions.schema.json` does not contain any hardcoded company names.

### Exercise 1.2: Architectural Boundary Verification
Inspect `tools/financial-modeling/financial_calculator.py`. Locate where client configuration parameters are accepted. Confirm that the calculator takes pure generic parameters (such as `assumptions: Dict[str, Any]`) rather than reading from a hardcoded client path.

---

## Completion Checklist

- [ ] Read `docs/START-HERE.md` completely.
- [ ] Studied `platform/vision/platform-vision.md` and summarized the 3 core platform pillars.
- [ ] Read `platform/product-requirements/prd-v0.1.md` and identified the primary deliverables required from your role.
- [ ] Reviewed `platform/architecture/system-architecture.md` and `platform/architecture/tenant-isolation.md`.
- [ ] Completed Practical Exercises 1.1 and 1.2.
- [ ] Understood that `tmk-it-solutions` is a client and not the platform.

---

## Next Recommended Section

Proceed to [Section 2: Franchise Fundamentals & Archetypes](file:///d:/company/products/franchise-business-platform/docs/02-franchise-fundamentals/README.md) to master commercial franchise structures, RACI governance, and revenue distribution models.
