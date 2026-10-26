# Multi-Tenant Isolation and Data Segregation Architecture

## 1. Tenancy Model Overview

The Franchise Business Modeling & Intelligence Platform serves multiple corporate clients, each with proprietary commercial terms, unique product catalogs, private financial assumptions, and confidential partner negotiations. Strict tenant isolation is a core non-functional requirement.

---

## 2. Tenancy Isolation Across Platform Evolutionary Stages

```mermaid
graph LR
    subgraph V0.1 Git Baseline
        Dir[Directory-Level Boundary: clients/client-id/]
        Schema[JSON Schema Contracts: schemas/*.json]
        Tools[Isolated CLI Runner: --client parameter]
    end

    subgraph V2.0 Cloud Architecture
        RLS[PostgreSQL Row-Level Security RLS]
        JWT[JWT Tenant Claims & RBAC Middleware]
        Storage[Isolated S3 Buckets / Tenant Prefixes]
    end

    V0.1 Git Baseline -->|Seamless Migration Path| V2.0 Cloud Architecture
```

---

## 3. Database Isolation Strategy (PostgreSQL RLS)

In the target cloud architecture, we adopt a **Shared Database, Isolated Schema / Row-Level Security (RLS)** model:

1. **Tenant Identification:**
   Every primary entity (`Product`, `FranchiseFee`, `FinancialAssumption`, `Territory`, `ContractDraft`) includes a mandatory `tenant_id` (UUID) foreign key referencing the `Tenants` table.
2. **PostgreSQL RLS Policies:**
   ```sql
   ALTER TABLE client_financial_assumptions ENABLE ROW LEVEL SECURITY;

   CREATE POLICY tenant_isolation_policy ON client_financial_assumptions
       FOR ALL
       TO application_role
       USING (tenant_id = current_setting('app.current_tenant_id')::uuid);
   ```
3. **Session Context Injection:**
   ASP.NET Core middleware extracts `tenant_id` from the authenticated JWT token and sets the PostgreSQL connection variable `app.current_tenant_id` before query execution.

---

## 4. Role-Based Access Control (RBAC) Matrix

| User Role | Tenant Scope | Frameworks Scope | Client Deliverables Scope |
|---|---|---|---|
| **Platform Administrator** | All Tenants (Admin Only) | Full Read/Write | Audit Read Only |
| **Principal Consultant** | Assigned Client Tenants | Read/Write | Full Approval & Release |
| **Data Analyst 1 & 2** | Assigned Client Tenants | Read/Write | Draft & Edit |
| **Client Corporate Sponsor** | Own Tenant Only | Read Only | View & Sign-Off |
| **Prospective Franchisee** | Own Candidate Sandbox | View Public Frameworks | View Approved Prospectus Only |

---

## 5. Migration Strategy from V0.1 to SaaS

1. All client JSON files in `clients/<client-slug>/` adhere strictly to standard JSON schemas.
2. An automated ingestion pipeline will read `client.json`, `products-catalog.json`, and `assumptions.json` directly into PostgreSQL tenant tables without data loss or reformatting.
