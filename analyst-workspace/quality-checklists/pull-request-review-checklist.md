# Pull Request Quality & Peer Review Checklist

## Reviewer Instructions
Before approving any Pull Request, the assigned peer reviewer (Analyst 1 or Analyst 2) must complete this checklist:

### 1. Architectural & Privacy Boundaries
- [ ] No client-specific commercial terms or confidential data leaked into `frameworks/`, `templates/`, or `tools/`.
- [ ] Client files reside strictly in `clients/<client-slug>/`.

### 2. Quantitative & Modeling Integrity
- [ ] Calculations use `Decimal` arithmetic; no floating-point currency calculations.
- [ ] Taxes (18% GST) are segregated and not treated as distributable revenue.
- [ ] Any new numerical assumption is logged in `assumptions-register.md`.
- [ ] Formulas in generated Excel sheets are standard uppercase (`=SUM()`, `=IF()`).

### 3. Verification & CI Checks
- [ ] `pytest tests/` passes with 100% test success.
- [ ] `python tools/validation/validate_repo.py` passes with 0 errors.
- [ ] JSON files validate against their corresponding schema in `schemas/`.
- [ ] All internal relative markdown links resolve correctly.
