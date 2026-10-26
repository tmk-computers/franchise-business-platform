# Contributing Guidelines

Thank you for contributing to the **Franchise Business Modeling & Intelligence Platform**. To maintain high business rigor, financial integrity, and software quality across all client workspaces and generic frameworks, all contributors (analysts, architects, engineers, and AI agents) must adhere to these guidelines.

---

## 1. Branch Strategy and Workflow

We follow a structured Git branching workflow based on trunk-based development with short-lived feature branches:

- `main` / `master`: Production-ready branch. Must always be deployable, pass all automated checks, and contain only peer-reviewed and validated deliverables.
- `feature/<client-or-framework>-<brief-description>`: For new capabilities, frameworks, or client work.
  - Example: `feature/tmk-financial-model-v1`
  - Example: `feature/framework-territory-scoring`
- `fix/<issue-description>`: For bug fixes or calculation corrections.
  - Example: `fix/churn-amortization-calc`
- `docs/<topic>`: For documentation updates, glossary expansions, or analyst guidelines.
  - Example: `docs/analyst-onboarding-refresh`

---

## 2. Commit Message Conventions

We enforce [Conventional Commits](https://www.conventionalcommits.org/):

Format:
```text
<type>(<scope>): <short description>

[optional body explaining motivation and context]

[optional footer(s)]
```

Allowed Types:
- `feat`: A new feature or analytical model (e.g., `feat(calc): add tiered royalty computation`)
- `fix`: A calculation bug fix or broken reference repair (e.g., `fix(tools): correct working capital runway formula`)
- `docs`: Documentation updates, template additions (e.g., `docs(templates): add franchise prospectus template`)
- `client`: Client workspace addition or modification (e.g., `client(tmk): add 6-product catalog profiles`)
- `refactor`: Refactoring code or restructuring documentation without changing output
- `test`: Adding or updating unit tests (e.g., `test(calc): add edge case tests for zero churn`)
- `chore`: Maintenance tasks, dependency updates, CI workflow updates

---

## 3. Pull Request Requirements

Every Pull Request must meet the following acceptance gates:

1. **Self-Contained & Descriptive:** Fill out the standardized Pull Request template (`.github/pull_request_template.md`).
2. **Automated Checks Pass:**
   - All pytest unit tests must pass (`pytest tests/`).
   - Repository validation script must pass with 0 errors (`python tools/validation/validate_repo.py`).
   - JSON schemas must validate all JSON configurations.
   - No broken relative links in markdown documentation.
3. **Dual Analyst Peer Review:**
   - Deliverables produced by **Analyst 1 (Strategy/Documentation)** must be reviewed by **Analyst 2 (Finance/Analytics)** for quantitative feasibility.
   - Models produced by **Analyst 2** must be reviewed by **Analyst 1** for alignment with business strategy and client contractual terms.
4. **No Financial Hallucinations:** Any assumption introduced must be linked to an entry in `analyst-workspace/research-methodology/assumptions-register.md`.
5. **Separation of Concerns:** Ensure client-specific business rules have not leaked into `frameworks/` or `tools/`.

---

## 4. Financial Modeling Review Standard

When modifying calculation engines or financial models:
- Always use `Decimal` for currency calculations in Python.
- Formulas in generated Excel workbooks must use upper-case Excel formula syntax (e.g., `=SUM(C4:C15)`, `=IF(D4>0, D4*0.4, 0)`).
- Provide unit tests in `tests/` covering:
  - Base case.
  - Conservative scenario.
  - Optimistic scenario.
  - Boundary cases (zero revenue, 100% churn, negative operating margins).

---

## 5. Security & Confidentiality Checklist

Before committing:
- Confirm no API credentials, passwords, or customer PII are present.
- Ensure files comply with `.gitignore`.
- Non-public client intellectual property must remain confined to `clients/<client-name>/`.
