# Agent Operational Reference Card

> **CRITICAL NOTICE:**  
> This file is a quick reference pointer. The comprehensive, authoritative instruction document for all AI assistants, autonomous agents, and human contributors is located in:  
> **[AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md)**.
> 
> You MUST read and strictly adhere to [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md) before performing any changes in this repository.

---

## Quick Reference: 8 Golden Rules

1. **Client Independence:** Never hardcode client-specific commercial terms (e.g., TMK's 40:60 split or ₹25k/₹50k fees) into generic frameworks (`frameworks/`, `tools/`, `schemas/`).
2. **Fact Integrity & Zero Fabrication:** Never invent market data or financial figures. Trace all research to [research-evidence-register.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/research-methodology/research-evidence-register.md).
3. **Decimal Precision:** Use Python `decimal.Decimal` with `ROUND_HALF_UP` for all monetary arithmetic. Standard floats are forbidden.
4. **Draft vs. Approved Status:** Explicitly tag all documents (`[DRAFT]`, `[WORKING DISCUSSION DRAFT]`, `[PEER APPROVED]`, `[CLIENT APPROVED]`).
5. **Protect Approved Deliverables:** Never overwrite or modify approved client deliverables without authorization.
6. **Dual-Analyst Review:** Strategy documents (Analyst 1) require financial review (Analyst 2); financial models require strategy review.
7. **Zero Secrets in Git:** Never commit API keys, passwords, credentials, or client customer PII.
8. **Mandatory Automated Checks:** Run tests and validation before completing work:
   ```bash
   python -m pytest tests/ -v
   python tools/validation/validate_repo.py
   ```

---

## Directory-Specific Instruction Index

- Platform Architecture & PRDs: [platform/AGENTS.md](file:///d:/company/products/franchise-business-platform/platform/AGENTS.md)
- Reusable Business Frameworks: [frameworks/AGENTS.md](file:///d:/company/products/franchise-business-platform/frameworks/AGENTS.md)
- Reusable Document Templates: [templates/AGENTS.md](file:///d:/company/products/franchise-business-platform/templates/AGENTS.md)
- Industry Vertical Models: [industry-models/AGENTS.md](file:///d:/company/products/franchise-business-platform/industry-models/AGENTS.md)
- Client Workspaces & Isolation: [clients/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/AGENTS.md)
- TMK IT Solutions Client Workspace: [clients/tmk-it-solutions/AGENTS.md](file:///d:/company/products/franchise-business-platform/clients/tmk-it-solutions/AGENTS.md)
- JSON Schemas & Data Contracts: [schemas/AGENTS.md](file:///d:/company/products/franchise-business-platform/schemas/AGENTS.md)
- Financial Modeling Tools & Engines: [tools/AGENTS.md](file:///d:/company/products/franchise-business-platform/tools/AGENTS.md)
- Analyst Operational Workspace: [analyst-workspace/AGENTS.md](file:///d:/company/products/franchise-business-platform/analyst-workspace/AGENTS.md)
- Documentation & Standards: [docs/AGENTS.md](file:///d:/company/products/franchise-business-platform/docs/AGENTS.md)
- Testing & Quality Assurance: [tests/AGENTS.md](file:///d:/company/products/franchise-business-platform/tests/AGENTS.md)
