# Developer & Analyst Quickstart Guide

## 1. Fast-Track Overview
This guide gets a new software engineer, data analyst, or franchise consultant productive within 15 minutes.

---

## 2. Prerequisites & Tooling
- **Git:** Version 2.40+
- **Python:** Version 3.11+
- **Dependencies:** `openpyxl`, `pandas`, `numpy`, `pydantic`, `jsonschema`, `pytest`, `python-pptx`

---

## 3. Running Financial Models
To simulate client financial scenarios and generate dynamic Excel workbooks:
```bash
# Run Base Scenario for TMK IT Solutions:
python tools/financial-modeling/cli.py --client tmk-it-solutions --scenario base

# Generate the live-formula Excel workbook:
python tools/financial-modeling/cli.py --client tmk-it-solutions --generate-excel

# Inspect the generated file at:
# clients/tmk-it-solutions/financial-models/tmk_it_solutions_franchise_financial_model.xlsx
```

---

## 4. Running Pitch Deck Generators
```bash
# Generate the 10-slide PowerPoint pitch deck:
python tools/document-generation/generate_pitch_deck.py --client tmk-it-solutions

# Inspect the generated file at:
# clients/tmk-it-solutions/presentations/franchise-opportunity-pitch-deck.pptx
```

---

## 5. Running Validation & Unit Tests
```bash
# Run automated quality checks:
python tools/validation/validate_repo.py

# Run unit tests:
pytest tests/
```
