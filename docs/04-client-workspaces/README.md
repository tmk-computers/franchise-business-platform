# Section 4: Client Workspaces & TMK Baseline

## Purpose
This section introduces the client workspace architecture and provides a comprehensive walkthrough of our inaugural client: **TMK IT Solutions LLP**. Analysts will learn how client workspaces are structured, how client confidentiality and data isolation are enforced, how TMK's 6 software products and commercial terms are configured, and how to replicate this structure when onboarding future corporate clients.

---

## Prerequisites
- Completed [Section 1: Platform Orientation](file:///d:/company/products/franchise-business-platform/docs/01-platform-orientation/README.md) through [Section 3: Repository Guide](file:///d:/company/products/franchise-business-platform/docs/03-repository-guide/README.md).
- Understand the distinction between generic frameworks and client-specific assets.

---

## Reading Sequence

Follow this reading sequence:

1. [clients/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/AGENTS.md) — Multi-tenant client isolation rules, data boundaries, and confidentiality standards.
2. [clients/tmk-it-solutions/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/AGENTS.md) — Operational guidelines specific to TMK IT Solutions LLP (FOFO model, 6 products, proposed commercial terms).
3. [clients/tmk-it-solutions/profile/company-overview.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/profile/company-overview.md) — Corporate background, executive leadership, vision, and commercial objectives.
4. [clients/tmk-it-solutions/products/products-catalog.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json) — Structural catalog detailing all 6 software products, licensing tiers, pricing, and target markets.
5. [clients/tmk-it-solutions/franchise-model/fofo-operating-model.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/franchise-model/fofo-operating-model.md) — Detailed specification of TMK's Franchise Owned, Franchise Operated (FOFO) commercial structure.
6. [clients/tmk-it-solutions/financial-models/assumptions.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/financial-models/assumptions.json) — Commercial parameters (promotional ₹25,000 / regular ₹50,000 joining fees; 40:60 net revenue sharing).
7. [clients/tmk-it-solutions/research/taluka-based-territory-strategy.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/research/taluka-based-territory-strategy.md) — Taluka and district expansion strategy across Indian Tier-2/Tier-3 markets.
8. [clients/tmk-it-solutions/approvals/approval-matrix.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/approvals/approval-matrix.md) — Status ledger tracking formal sign-offs for all TMK deliverables.
9. [docs/implementation-guides/client-onboarding-playbook.md](file:///d:/company/products/franchise-business-platform/docs/implementation-guides/client-onboarding-playbook.md) — Playbook for onboarding future client organizations.

---

## Relevant Repository Links

| Client Asset / Directory | Content Description |
|---|---|
| [clients/tmk-it-solutions/research/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/research/) | Market demand, competitor benchmarking, and territory research briefs |
| [clients/tmk-it-solutions/presentations/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/presentations/) | Master franchise opportunity pitch deck and presentation outlines |
| [clients/tmk-it-solutions/sales-marketing/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/sales-marketing/) | Franchise opportunity brochure, prospectus, and investor FAQ |
| [clients/tmk-it-solutions/operations/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/operations/) | Franchisee operations handbook, training curriculum, and support SLAs |
| [clients/tmk-it-solutions/legal-drafts/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/legal-drafts/) | Non-final draft franchise agreement, revenue policy, and territory guidelines |
| [clients/tmk-it-solutions/deliverables/](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/deliverables/) | Approved deliverables ratified by client leadership |

---

## Learning Outcomes

Upon completing this section, an analyst will be able to:
1. **Explain the TMK Client Baseline:** Articulate TMK's business model, leadership profile, and B2B software portfolio (Cloud ERP, School Management, Hospital ERP, Retail POS, DevOps Automation, Cybersecurity Suite).
2. **Interpret Commercial Assumptions:** Understand TMK's proposed commercial terms:
   - Early-mover promotional franchise joining fee: ₹25,000 (first 10 units).
   - Standard joining fee: ₹50,000.
   - Ongoing net revenue split: 40% Franchisee : 60% TMK IT Solutions.
   - Working capital requirement: ₹50,000–₹1,00,000.
3. **Execute Client Data Isolation:** Maintain strict confidentiality by keeping TMK client data strictly within `clients/tmk-it-solutions/`.
4. **Onboard a New Client:** Follow the step-by-step process in `client-onboarding-playbook.md` to establish a new client workspace (`clients/<new-client>/`).
5. **Trace Approval Status:** Inspect `clients/tmk-it-solutions/approvals/approval-matrix.md` to identify which documents are in Draft vs. Client Approved status.

---

## Practical Exercises

### Exercise 4.1: TMK Software Product Catalog Exploration
Open [clients/tmk-it-solutions/products/products-catalog.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/products/products-catalog.json).
1. List the 6 software products by `productId` and `name`.
2. For `prd-01-enterprise-erp`, identify its base license price (`indicativePriceNet`), target audience, and recurring renewal rate.

### Exercise 4.2: Inspecting Client Commercial Terms
Open [clients/tmk-it-solutions/financial-models/assumptions.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/financial-models/assumptions.json).
1. What is the configured `taxRatePercent`?
2. In `scenarios.base`, what is the `monthlyUnitSalesVelocity`?
3. What is the assumed monthly office rent under `franchiseeMonthlyOpEx.officeRent`?

---

## Completion Checklist

- [ ] Read `clients/AGENTS.md` and `clients/tmk-it-solutions/AGENTS.md`.
- [ ] Studied `clients/tmk-it-solutions/profile/company-overview.md`.
- [ ] Completed Practical Exercises 4.1 and 4.2.
- [ ] Reviewed `clients/tmk-it-solutions/research/taluka-based-territory-strategy.md`.
- [ ] Understood how the client approval matrix functions.

---

## Next Recommended Section

Proceed to [Section 5: Analyst Playbooks](file:///d:/company/products/franchise-business-platform/docs/05-analyst-playbooks/README.md) to access role-specific workflows and execution playbooks for Analyst 1 and Analyst 2.
