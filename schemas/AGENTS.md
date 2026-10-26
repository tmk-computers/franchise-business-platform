# Schemas Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `schemas/` directory defines formal JSON Schema (Draft-07) data contracts governing client configurations, product catalogs, financial assumptions, revenue-sharing rules, research evidence, and deliverable tracking across the platform.

---

## 2. Specialized Agent Rules for `schemas/`

1. **Schema Standard & Syntax:**
   - All schemas must use JSON Schema Draft-07 specification (`"$schema": "http://json-schema.org/draft-07/schema#"`).
   - Filenames must strictly follow `<entity-name>.schema.json`.
   - Schemas must enforce `"additionalProperties": false` on root and complex object types to prevent configuration drift.
2. **Client-Agnostic Purity:**
   - NEVER embed client-specific enumerations, product names, or fee defaults in schemas.
   - For example, do not hardcode TMK product IDs into `product.schema.json`. Use generalized regex patterns (e.g., `"pattern": "^[a-z0-9-]+$"`).
3. **Backward Compatibility:**
   - Any modification to an existing schema must remain backward compatible with existing client JSON files in `clients/`.
   - If a breaking schema change is necessary, update all client JSON instances across all active client workspaces simultaneously.
4. **Mandatory Validation Gate:**
   - Always run `python tools/validation/validate_repo.py` after editing any schema to ensure all client data files validate with 0 errors.
