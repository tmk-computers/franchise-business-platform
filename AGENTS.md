# Instructions for AI Coding Assistants and Autonomous Agents

Welcome to the **Franchise Business Modeling & Intelligence Platform** repository. This document sets strict operational rules, architectural guidelines, and behavioral requirements for AI assistants, language model agents, and autonomous contributors (including Google Antigravity, OpenAI Codex, Claude, and GitHub Copilot).

---

## 1. Core Architectural Axiom: Client Independence

- **Platform vs. Client Separation:** This repository contains both a generic, industry-agnostic franchise modeling platform (`frameworks/`, `templates/`, `tools/`, `schemas/`, `industry-models/`) and isolated client workspaces (`clients/<client-name>/`).
- **TMK IT Solutions LLP is a Client:** TMK IT Solutions LLP is the inaugural client (`clients/tmk-it-solutions/`), NOT the platform itself.
- **NEVER hardcode client-specific business rules into reusable frameworks.** For example, do not embed a 40:60 split or ₹25,000/₹50,000 joining fees into generic calculation engines or generic schemas. Always parameterize rules and pass them via configuration.

---

## 2. Cardinal Operating Rules

### Rule 1: Read Context Before Writing
Before modifying existing files or proposing architecture changes:
- Read relevant documentation in `docs/`, `frameworks/`, and `platform/`.
- Review the data contracts in `schemas/`.
- Verify the active configuration files in the appropriate client directory.

### Rule 2: Strict Financial Fact Integrity & Zero Fabrication
- **Do not invent financial numbers, customer counts, growth rates, or market sizes.**
- Clearly distinguish verified empirical data from modeled assumptions.
- If a parameter is unknown, record it explicitly in `analyst-workspace/research-methodology/assumptions-register.md` and request verification rather than assuming a value without labeling.
- Never label projected returns or model outputs as "guaranteed" or "assured profit."

### Rule 3: Decimal-Safe Arithmetic
- Always use `Decimal` for financial calculations in Python. Never use standard floating-point arithmetic for currency calculations to prevent rounding drift.
- Currency amounts must be rounded according to standard accounting conventions (e.g., standard half-up or half-even to 2 decimal places).

### Rule 4: Reuse and Maintain Generic Templates
- When creating client deliverables, inherit and instantiate templates from `templates/`.
- If a client requirement uncovers a missing structural element that is universally applicable, update the generic template first, then instantiate it for the client.

### Rule 5: Keep Client Data Isolated
- Never place client-specific trade secrets, proprietary software code, or client customer identities in `frameworks/`, `templates/`, or `platform/`.
- Each client's directory (`clients/<client-id>/`) must remain self-contained.

### Rule 6: Protect Version History and Approved Deliverables
- Never overwrite approved deliverables in `clients/<client-name>/deliverables/` without explicit authorization.
- Track changes systematically in `CHANGELOG.md` and document headers.

### Rule 7: Zero Secrets in Source Control
- Do not commit API tokens, passwords, database connection strings with credentials, or personal identity information.
- Use environment variables or configuration stubs (`.env.example`).

### Rule 8: Mandatory Quality Checks
- Before finishing any turn or delivering a feature, execute the test suite:
  ```bash
  pytest
  python tools/validation/validate_repo.py
  ```
- Any failure in JSON schema validation, unit tests, or broken relative links must be addressed immediately.

---

## 3. Directory Navigation Guide

| Directory | Purpose | Modifiability Guidelines |
|---|---|---|
| `platform/` | SaaS architecture, PRDs, roadmap | Platform team only; architectural changes require review |
| `frameworks/` | Reusable franchise methodology | Generic, client-agnostic only |
| `templates/` | Reusable document & deck templates | Add or refine template structures with placeholders |
| `industry-models/` | Vertical-specific economics (SaaS, QSR, Retail) | Industry research and generalized benchmarks |
| `schemas/` | JSON Schema data contracts | Keep backward compatible; validate with `jsonschema` |
| `tools/` | Calculation engine, Excel generator, validator | Maintain 100% test coverage; strictly decimal-safe |
| `clients/` | Client workspaces (e.g., `tmk-it-solutions`) | Client-specific configurations, drafts, and deliverables |
| `analyst-workspace/` | Onboarding, task tracking, registers | Update task statuses, assumption logs, and weekly reports |
| `docs/` | Standards, guides, glossary | Reference guides for human analysts and developers |
| `tests/` | Pytest test suite | Add unit tests for every new calculation or schema |

---

## 4. Communication & Output Expectations

- Produce actionable, production-grade files. Do not leave empty stub files or `# TODO` placeholders without explanatory context.
- Use GitHub Flavored Markdown with clickable file links (using `file:///` format or relative markdown links).
- When producing financial figures, always document:
  1. Base currency (e.g., INR ₹).
  2. Applicable taxation status (e.g., Exclusive of 18% GST).
  3. Cost/revenue driver assumptions.
