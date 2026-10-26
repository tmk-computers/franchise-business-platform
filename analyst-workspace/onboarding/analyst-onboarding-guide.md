# Analyst Onboarding & Operational Command Guide

## 1. Welcome to the Platform
Welcome to the **Franchise Business Modeling & Intelligence Platform**. As a data analyst, business analyst, or strategy consultant on this project, your work directly informs multi-million rupee commercial investments by enterprise franchisors and independent franchise business owners.

This repository is your primary working environment. Everything—from market sizing research to financial calculations, presentation decks, and legal drafts—is version-controlled, auditable, and automated.

---

## 2. Environment Setup (First 60 Minutes)
1. **Clone & Inspect Workspace:**
   ```bash
   git status
   git branch
   ```
2. **Verify Python Environment:**
   ```bash
   python --version  # Requires Python 3.11+
   pip install -r requirements.txt  # Or verify openpyxl, pandas, jsonschema, pytest, python-pptx
   ```
3. **Execute the Baseline Quality Suite:**
   ```bash
   # Run validation suite:
   python tools/validation/validate_repo.py

   # Run automated test suite:
   pytest tests/
   ```
4. **Read Cardinal Documentation:**
   - [README.md](file:///d:/company/products/franchise-business-platform/README.md)
   - [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md)
   - [CONTRIBUTING.md](file:///d:/company/products/franchise-business-platform/CONTRIBUTING.md)
   - [Analyst Roles](file:///d:/company/products/franchise-business-platform/analyst-workspace/onboarding/analyst-roles-and-responsibilities.md)

---

## 3. Daily Operational Cadence
- **09:30 AM — Standup & Task Board Review:** Inspect `analyst-workspace/task-tracker/task-board.md` for active assignments.
- **10:00 AM to 04:30 PM — Focus Work:** Research, financial modeling, or documentation drafting.
- **04:30 PM — Peer Review Exchange:** Analyst 1 and Analyst 2 review each other's open pull requests.
- **05:30 PM — Git Commit & Push:** Commit clean conventional commits; verify automated checks pass.
