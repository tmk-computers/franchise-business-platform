# Platform Domain: AI Agent Operating Instructions

> **Parent Authority:** This document inherits all cardinal rules from the root [AGENTS.md](file:///d:/company/products/franchise-business-platform/AGENTS.md).

---

## 1. Domain Purpose & Scope
The `platform/` directory houses the core SaaS architecture, Product Requirements Documents (PRDs), domain entity definitions, security policies, and long-term technical roadmap. It defines how the franchise modeling platform transitions from an analyst-driven Git repository into an enterprise multi-tenant cloud application.

---

## 2. Specialized Agent Rules for `platform/`

1. **Multi-Tenant Architectural Purity:**
   - All domain designs and architectural blueprints must maintain strict tenant isolation.
   - Do NOT introduce architecture that couples the core SaaS engine to a specific client, database schema, or cloud vendor proprietary API.
   - Target stack standards: React 19 + TypeScript frontend, ASP.NET Core 8 Web API backend, PostgreSQL 16 with Row-Level Security (RLS), and Python 3.12+ analytical microservices.
2. **Domain Entity Integrity:**
   - Any modifications to domain entities (`Client`, `Product`, `FranchiseModel`, `FinancialAssumption`, `Territory`, `RevenueSharingRule`) in `platform/data-models/domain-model.md` must maintain backward compatibility with JSON schemas in `schemas/`.
3. **Security & Zero Secrets Policy:**
   - Guidelines in `platform/security/security-policy.md` and `platform/security/confidentiality-guidelines.md` must be respected. Never document actual private production credentials or API keys.
4. **Roadmap Governance:**
   - Maintain the phased release structure (V0.1 Bootstrap -> V1.0 Multi-Client Automation -> V2.0 Cloud Platform -> V3.0 Enterprise SaaS Portal).
