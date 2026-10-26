# Templates Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `templates/` directory houses standardized, reusable document, presentation, policy, and dashboard templates. These templates serve as blueprints from which client-specific deliverables are instantiated.

---

## 2. Specialized Agent Rules for `templates/`

1. **Standardized Placeholder Conventions:**
   - All variable data points must use uppercase double-curly-brace placeholders: `{{PLACEHOLDER_NAME}}`.
   - Examples: `{{CLIENT_LEGAL_NAME}}`, `{{JOINING_FEE_NET}}`, `{{FRANCHISEE_COMMISSION_PERCENT}}`, `{{CURRENCY_SYMBOL}}`.
   - Never embed hardcoded client values inside files ending in `.template.md`.
2. **Template Usage Header:**
   - Every template must begin with a standardized usage callout:
     ```markdown
     > **Template Usage Instructions:**  
     > [Instructions explaining required inputs, schema mapping, and client deliverable destination]
     ```
3. **Template vs. Deliverable Separation:**
   - Templates reside in `templates/`.
   - Populated instances of templates belong exclusively in `clients/<client-name>/deliverables/` or respective client subdirectories. Never save client-specific output in `templates/`.
4. **Mandatory Risk Disclosures & Legal Caveats:**
   - Pitch deck, brochure, agreement, and prospectus templates must preserve standard legal disclaimers and risk disclosure callouts.
