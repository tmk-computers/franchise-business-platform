# Section 3: Repository Guide & Engineering Standards

## Purpose
This section provides an architectural tour of the repository. It details directory responsibilities, explains how JSON Schema data contracts govern client configurations, demonstrates the mathematical standards for financial modeling, and outlines engineering best practices for Python automation, openpyxl Excel generation, and Git collaboration.

---

## Prerequisites
- Completed [Section 1: Platform Orientation](file:///d:/company/products/franchise-business-platform/docs/01-platform-orientation/README.md) and [Section 2: Franchise Fundamentals](file:///d:/company/products/franchise-business-platform/docs/02-franchise-fundamentals/README.md).
- Python 3.10+ installed locally with a verified virtual environment (`.venv`).

---

## Reading Sequence

Follow this reading sequence:

1. [docs/DOCUMENTATION-MAP.md](file:///d:/company/products/franchise-business-platform/docs/DOCUMENTATION-MAP.md) — Structural map and file index of the entire repository.
2. [docs/standards/financial-modeling-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/financial-modeling-standards.md) — Mandatory Decimal arithmetic standards, rounding rules, and tax handling.
3. [docs/standards/documentation-standards.md](file:///d:/company/products/franchise-business-platform/docs/standards/documentation-standards.md) — Markdown formatting, header hierarchy, and deliverable status labeling.
4. [schemas/AGENTS.md](file:///d:/company/products/franchise-business-platform/schemas/AGENTS.md) — JSON Schema (Draft-07) specifications, contracts, and validation rules.
5. [tools/AGENTS.md](file:///d:/company/products/franchise-business-platform/tools/AGENTS.md) — Standards for Python automation engines and Excel formula generators.
6. [CONTRIBUTING.md](file:///d:/company/products/franchise-business-platform/CONTRIBUTING.md) — Git branching workflow, commit message standards, and PR guidelines.
7. [tests/AGENTS.md](file:///d:/company/products/franchise-business-platform/tests/AGENTS.md) — Test suite architecture, coverage requirements, and regression prevention.

---

## Relevant Repository Links

| Directory / File | Description |
|---|---|
| [schemas/](file:///d:/company/products/franchise-business-platform/schemas/) | JSON Schema contracts (`client`, `product`, `financial-assumptions`, `revenue-sharing`, etc.) |
| [templates/](file:///d:/company/products/franchise-business-platform/templates/) | 15+ standardized deliverable templates with `{{...}}` placeholders |
| [tools/financial-modeling/](file:///d:/company/products/franchise-business-platform/tools/financial-modeling/) | Python calculation engine (`calculator.py`) and Excel builder (`excel_generator.py`) |
| [tools/validation/validate_repo.py](file:///d:/company/products/franchise-business-platform/tools/validation/validate_repo.py) | Central repository validation script enforcing schema and link integrity |
| [tests/](file:///d:/company/products/franchise-business-platform/tests/) | Pytest test suite validating calculator math, schemas, and repo structure |

---

## Learning Outcomes

Upon completing this section, an analyst will be able to:
1. **Navigate the Repository Confidently:** Locate any framework, template, schema, tool, or client asset instantly.
2. **Apply Decimal-Safe Math:** Implement financial calculations in Python using `decimal.Decimal` and `quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)` without binary floating-point drift.
3. **Validate Data Contracts:** Run and interpret JSON Schema validation to verify that client configuration files meet platform contracts.
4. **Utilize Reusable Templates:** Populate document templates from `templates/` using standard placeholder conventions (`{{CLIENT_NAME}}`, `{{PRODUCT_NAME}}`) without breaking layout structures.
5. **Execute Quality Checks:** Run automated test suites (`pytest tests/`) and repository validators before committing changes.

---

## Practical Exercises

### Exercise 3.1: JSON Schema Validation Run
Open your terminal in the repository root and execute the schema test:
```bash
python -m pytest tests/test_schemas.py -v
```
Inspect the output. Confirm that `clients/tmk-it-solutions/` configurations pass all JSON Schema contracts.

### Exercise 3.2: Inspecting Data Contracts
Open [schemas/financial-assumptions.schema.json](file:///d:/company/products/franchise-business-platform/schemas/financial-assumptions.schema.json) and compare it against [clients/tmk-it-solutions/financial-models/assumptions.json](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/financial-models/assumptions.json). Identify the required top-level keys (`franchiseFees`, `revenueSharing`, `operationalCosts`, `taxAndCompliance`, `projectionsHorizonMonths`).

---

## Completion Checklist

- [ ] Studied `docs/DOCUMENTATION-MAP.md` and repository directory structure.
- [ ] Read `docs/standards/financial-modeling-standards.md` and committed Decimal arithmetic rules to memory.
- [ ] Reviewed `schemas/AGENTS.md` and examined schema definitions.
- [ ] Ran `pytest tests/test_schemas.py -v` successfully in terminal.
- [ ] Reviewed `CONTRIBUTING.md` Git workflows.

---

## Next Recommended Section

Proceed to [Section 4: Client Workspaces & TMK Baseline](file:///d:/company/products/franchise-business-platform/docs/04-client-workspaces/README.md) to inspect the isolated workspace of our inaugural client, TMK IT Solutions LLP.
