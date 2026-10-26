# Authoritative Instructions for AI Coding Assistants and Autonomous Agents

Welcome to the **Franchise Business Modeling & Intelligence Platform** repository. This document serves as the **supreme, authoritative instruction set** governing all AI coding assistants, autonomous agents, and language model systems (including Google Antigravity, OpenAI Codex, Anthropic Claude, and GitHub Copilot), as well as human contributors.

---

## 1. Core Architectural Axiom: Client Independence

- **Platform vs. Client Segregation:** This repository maintains an uncompromising boundary between the generic, industry-agnostic franchise modeling platform (`frameworks/`, `templates/`, `tools/`, `schemas/`, `industry-models/`) and isolated client workspaces (`clients/<client-name>/`).
- **TMK IT Solutions LLP is a Client:** TMK IT Solutions LLP is the inaugural client (`clients/tmk-it-solutions/`), NOT the platform itself.
- **NEVER hardcode client-specific business rules into reusable frameworks.** 
  - Do NOT embed TMK's proposed 40:60 split, ₹25,000/₹50,000 joining fees, 6 software products, or specific taluka boundaries into generic calculation engines, schemas, or framework documents.
  - Reusable engines and frameworks must be strictly parameterized and driven by configuration files.

---

## 2. Cardinal Operating Rules

### Rule 1: Read Context and Contracts Before Writing
Before proposing code, modifying existing files, or authoring business documents:
1. Read relevant documentation in `docs/`, `frameworks/`, and `platform/`.
2. Inspect the active data contracts in `schemas/`.
3. Check the client configurations in `clients/<client-slug>/`.
4. Review directory-specific instructions in the local `AGENTS.md` of the target directory.

### Rule 2: Evidence-Based Research & Zero Fabrication
- **Strict Financial & Fact Integrity:** Do NOT invent financial metrics, market sizes, customer counts, adoption rates, or competitor quotes.
- **Empirical Grounding:** Every market sizing claim or competitor benchmark must be traceable to a verified entry in `analyst-workspace/research-methodology/research-evidence-register.md`.
- **Labeling Assumptions:** If an empirical value is unknown, record it explicitly as `[PROPOSED]`, `[WORKING HYPOTHESIS]`, or `[ESTIMATED]` in `analyst-workspace/research-methodology/assumptions-register.md` rather than assuming a value without disclosure.
- **No Deceptive Earnings Claims:** Never describe projected returns, scenario outputs, or cash flows as "guaranteed," "assured profit," or "risk-free."

### Rule 3: Decimal-Safe Arithmetic for Financial Calculations
- **No Floating-Point Math for Currency:** All financial calculations, fee splits, taxes, and margins in Python must strictly use the standard library `decimal.Decimal` module.
- **Rounding Conventions:** Currency values must be quantized to 2 decimal places using `ROUND_HALF_UP` (`0.01`).
- **Tax Segregation:** Statutory pass-through taxes (e.g., 18% GST in India) must be strictly isolated from distributable revenue pools. Never calculate commissions on tax-inclusive gross amounts unless explicitly configured.

### Rule 4: Clear Distinction Between Draft and Approved Documents
All files and deliverables must clearly indicate their review and approval status:
- `[DRAFT]`: Work in progress; subject to alteration.
- `[WORKING DISCUSSION DRAFT]`: Formulated for structural analysis; non-binding.
- `[PEER APPROVED]`: Reviewed and confirmed by peer analyst (Analyst 1 or Analyst 2).
- `[MODELING APPROVED]`: Mathematical integrity and formulas verified by quantitative lead.
- `[CLIENT APPROVED]` / `[APPROVED DELIVERABLE]`: Formally ratified by client leadership in `clients/<client>/approvals/approval-matrix.md`.

### Rule 5: Protection of Approved Deliverables and Version History
- **Zero Unauthorized Overwrites:** NEVER overwrite, delete, or modify approved deliverables located in `clients/<client-name>/deliverables/` or approved financial models without explicit authorization.
- **Preserve History:** Log changes systematically in `CHANGELOG.md` and document revision headers. Deprecated assets must be archived with timestamp tags.

### Rule 6: Independent Dual-Analyst Review
- Deliverables authored by **Analyst 1 (Strategy/Documentation)** must be reviewed by **Analyst 2 (Finance/Analytics)** for quantitative feasibility and pricing realism.
- Models and tools authored by **Analyst 2** must be reviewed by **Analyst 1** for contractual compliance and business model alignment.
- No PR or document release may bypass this cross-disciplinary review gate.

### Rule 7: Zero Secrets & Client Data Confidentiality
- Do not commit API tokens, private signing keys, passwords, database credentials, or customer Personally Identifiable Information (PII).
- Client-specific proprietary trade secrets, customer registries, and commercial terms must remain confined to `clients/<client-name>/`.
- Generic modules must never depend on non-public client data.

### Rule 8: Mandatory Automated Quality Checks
Before completing any turn or committing changes, execute the full automated verification suite:
```bash
python -m pytest tests/ -v
python tools/validation/validate_repo.py
```
Any failure in JSON schema validation, unit tests, broken relative links, or financial split balance checks must be resolved immediately before concluding work.

---

## 3. Directory Navigation & Specialized Agent Instructions

Specialized directory-level `AGENTS.md` files provide detailed constraints for specific subdomains. Agents working within those directories must comply with both this root document and the directory-specific instructions:

| Directory | Specialized AGENTS.md Path | Domain Focus & Primary Guidelines |
|---|---|---|
| `platform/` | [platform/AGENTS.md](file:///d:/company/products/franchise-business-platform/platform/AGENTS.md) | Multi-tenant SaaS architecture, PRDs, domain models, security, tenant isolation |
| `frameworks/` | [frameworks/AGENTS.md](file:///d:/company/products/franchise-business-platform/frameworks/AGENTS.md) | Reusable, client-agnostic franchise methodologies; mandatory 9-section structure |
| `templates/` | [templates/AGENTS.md](file:///d:/company/products/franchise-business-platform/templates/AGENTS.md) | Reusable document & presentation templates; strict placeholder standards (`{{...}}`) |
| `industry-models/` | [industry-models/AGENTS.md](file:///d:/company/products/franchise-business-platform/industry-models/AGENTS.md) | Vertical-specific economics (Software, F&B, Retail, Healthcare, Education, etc.) |
| `clients/` | [clients/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/AGENTS.md) | Client workspace isolation, confidentiality, tenant data segregation rules |
| `clients/tmk-it-solutions/` | [clients/tmk-it-solutions/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/AGENTS.md) | TMK IT Solutions workspace; FOFO model, 6 products, proposed fees, legal disclaimers |
| `schemas/` | [schemas/AGENTS.md](file:///d:/company/products/franchise-business-platform/schemas/AGENTS.md) | JSON Schema contracts (Draft-07), backward compatibility, strict validation |
| `tools/` | [tools/AGENTS.md](file:///d:/company/products/franchise-business-platform/tools/AGENTS.md) | Python calculation engine, Decimal precision, upper-case Excel formula generation |
| `analyst-workspace/` | [analyst-workspace/AGENTS.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/AGENTS.md) | Dual-analyst operational rules, evidence register, assumptions log, task board |
| `docs/` | [docs/AGENTS.md](file:///d:/company/products/franchise-business-platform/docs/AGENTS.md) | Global documentation, standards, terminology glossary, onboarding playbooks |
| `tests/` | [tests/AGENTS.md](file:///d:/company/products/franchise-business-platform/tests/AGENTS.md) | Pytest test suite, zero-superficial tests, regression prevention, edge case coverage |

---

## 4. Communication & Deliverable Quality Expectations

1. **Production-Grade Outputs:** Produce complete, actionable, professional markdown documents and code. Never leave empty stub files or unexplained `# TODO` placeholders.
2. **Clickable Links:** Always create clickable links for files and symbols using markdown syntax with the `file:///` scheme (e.g., [README.md](file:///d:/company/products/franchise-business-platform/README.md)).
3. **Transparent Financial Documentation:** Every financial figure produced must clearly state:
   - Base currency (e.g., INR ₹).
   - Taxation status (e.g., Exclusive of 18% GST).
   - Underlying driver assumptions and scenario tag (Conservative, Base, or Optimistic).
