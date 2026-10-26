# Enterprise Client Onboarding Playbook

## 1. Onboarding Playbook Overview
This playbook provides a step-by-step operational checklist for onboarding a new corporate client onto the platform.

---

## 2. Five-Step Client Workspace Initialization

### Step 1: Create Client Workspace Directory
Create a dedicated workspace under `clients/<client-slug>/`:
```bash
mkdir -p clients/<client-slug>/{profile,products,research,franchise-model,financial-models,presentations,sales-marketing,legal-drafts,operations,risks,decisions,approvals,deliverables}
```

### Step 2: Define Client Profile (`profile/client.json`)
Populate `client.json` following `schemas/client.schema.json`.

### Step 3: Populate Product Catalog (`products/products-catalog.json`)
Define all client commercial products following `schemas/product.schema.json`.

### Step 4: Configure Assumptions & Revenue Sharing
Populate `financial-models/assumptions.json` and `franchise-model/revenue-sharing-config.json`.

### Step 5: Execute Automated Financial Model & Presentation Generation
```bash
python tools/financial-modeling/cli.py --client <client-slug> --generate-excel
python tools/document-generation/generate_pitch_deck.py --client <client-slug>
python tools/validation/validate_repo.py
```
