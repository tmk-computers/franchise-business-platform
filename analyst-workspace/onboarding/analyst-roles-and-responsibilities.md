# Analyst Roles, Responsibilities & Accountability Matrix

## 1. Dual-Analyst Team Architecture

The platform operational model pairs two complementary analytical disciplines to ensure qualitative narrative excellence and quantitative mathematical integrity:

```mermaid
graph LR
    subgraph Analyst 1: Strategy & Documentation
        A1_1[Market Research & Sizing]
        A1_2[Franchise Model Design]
        A1_3[Pitch Decks & Brochures]
        A1_4[Agreements & Policies]
        A1_5[Operations Manuals]
    end

    subgraph Peer Review Bridge
        PR[Cross-Disciplinary Quality & Feasibility Review]
    end

    subgraph Analyst 2: Finance & Intelligence
        A2_1[Unit Economics & P&Ls]
        A2_2[Revenue-Sharing Logic]
        A2_3[Decimal Calculation Engine]
        A2_4[Break-Even & Sensitivity]
        A2_5[Dashboards & Risk Analytics]
    end

    Analyst 1: Strategy & Documentation --> PR
    Analyst 2: Finance & Intelligence --> PR
```

---

## 2. Analyst 1 — Strategy, Research & Documentation

### Core Mandate:
Owns the business narrative, market evidence, strategic positioning, competitive intelligence, legal policy drafting, and partner-facing communication materials.

### Primary Responsibilities:
1. **Market & Competitor Intelligence:** Conduct empirical research on target industries and competitor pricing models. Maintain `analyst-workspace/research-methodology/research-evidence-register.md`.
2. **Franchise Operating Model Design:** Formulate responsibility matrices (RACI), territory boundary definitions, and onboarding playbooks.
3. **Franchise Pitch & Marketing Collateral:** Author institutional pitch decks, franchise prospectuses, commercial brochures, and website copy.
4. **Legal & Policy Drafting:** Prepare non-final drafts of franchise agreements, territory exclusivity policies, and brand usage standards.
5. **Operations Documentation:** Build comprehensive franchisee operations manuals and salesperson training handbooks.

---

## 3. Analyst 2 — Finance, Analytics & Intelligence

### Core Mandate:
Owns the mathematical calculation engine, financial projections, unit economics, sensitivity models, KPI dashboards, and data schemas.

### Primary Responsibilities:
1. **Financial Modeling Engine:** Maintain and enhance `tools/financial-modeling/calculator.py` using strict `Decimal` precision.
2. **Dynamic Excel Generators:** Build and maintain formula-linked openpyxl workbooks (`tools/financial-modeling/excel_generator.py`).
3. **Unit Economics & Break-Even:** Compute exact break-even sales velocity, working capital runway, cash flow trajectories, and 3-year ROI.
4. **Assumptions & Risk Registers:** Own `analyst-workspace/research-methodology/assumptions-register.md` and client risk registers.
5. **Analytics & Dashboards:** Define KPI metrics, maintain JSON schemas, and design executive reporting dashboards.

---

## 4. Peer Review Covenants
- No deliverable produced by Analyst 1 is finalized without Analyst 2 reviewing for financial realism and pricing consistency.
- No model produced by Analyst 2 is released without Analyst 1 reviewing for strategic alignment and contractual feasibility.
