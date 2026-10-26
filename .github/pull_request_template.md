## Pull Request Description

### Summary of Changes
<!-- Provide a concise summary of changes introduced in this PR -->

### Scope of Changes
- [ ] Platform Architecture / Core Frameworks (`platform/`, `frameworks/`)
- [ ] Financial Modeling Engine / Tools (`tools/`, `tests/`)
- [ ] Schemas / Data Contracts (`schemas/`)
- [ ] Client Workspace: TMK IT Solutions (`clients/tmk-it-solutions/`)
- [ ] Other Client Workspace (`clients/...`)
- [ ] Analyst Workspace / Task Registers (`analyst-workspace/`)
- [ ] Templates / Documentation (`templates/`, `docs/`)

---

## Quality Gate Checklist

- [ ] **No Client Leaks:** No client-specific commercial terms or confidential data leaked into generic frameworks or tools.
- [ ] **Financial Precision:** Currency calculations use `Decimal` arithmetic; no invented financial facts.
- [ ] **Assumptions Documented:** Any new modeling parameter is registered in `assumptions-register.md`.
- [ ] **Schema Compliance:** Any modified JSON configuration validates against its schema in `schemas/`.
- [ ] **Unit Tests:** Pytest passes (`pytest tests/`) and new unit tests cover edge cases.
- [ ] **Integrity Checks:** `python tools/validation/validate_repo.py` passes with zero errors.
- [ ] **Markdown Links:** All internal relative links are valid and resolve.

---

## Peer Review Sign-Off

- **Analyst 1 (Strategy/Documentation):** [ ] Approved / [ ] Not Applicable  
- **Analyst 2 (Finance/Analytics):** [ ] Approved / [ ] Not Applicable  
- **Notes / Review Comments:**
