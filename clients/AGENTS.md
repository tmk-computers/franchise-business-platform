# Clients Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `clients/` directory is the container for all tenant-specific workspaces. Each client has a dedicated, self-contained subfolder (`clients/<client-slug>/`) containing their confidential profile, product catalogs, commercial assumptions, financial models, research briefs, pitch decks, operations handbooks, legal drafts, and approved deliverables.

---

## 2. Specialized Agent Rules for `clients/`

1. **Strict Client Isolation (Zero Cross-Contamination):**
   - Each client workspace must remain completely self-contained.
   - Never reference or copy proprietary data, trade secrets, customer identities, or confidential commercial terms from one client directory into another.
   - When authoring tools or scripts, always parameterize the target client using `--client <client-slug>`.
2. **Schema Compliance:**
   - Every client workspace must provide valid JSON data contracts:
     - `profile/client.json` (validates against `schemas/client.schema.json`)
     - `products/products-catalog.json` (validates against `schemas/product.schema.json`)
     - `financial-models/assumptions.json` (validates against `schemas/financial-assumptions.schema.json`)
     - `franchise-model/revenue-sharing-config.json` (validates against `schemas/revenue-sharing.schema.json`)
3. **Protection of Approved Deliverables:**
   - Never overwrite, delete, or silently modify approved deliverables in `clients/<client-slug>/deliverables/`.
   - Modifying approved assets requires formal review and updates to `clients/<client-slug>/approvals/approval-matrix.md`.
4. **Draft vs. Approved Status Labeling:**
   - Clearly label commercial parameters as `[PROPOSED]` or `[WORKING HYPOTHESIS]` until formal client approval.
   - Legal documents must carry explicit non-final working draft disclaimers.
