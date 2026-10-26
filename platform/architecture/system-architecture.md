# System Architecture: Target Multi-Tenant SaaS & V0.1 Git Baseline

## 1. Architectural Strategy

The platform architecture follows an evolutionary path:
- **Phase 0 (Current - V0.1):** File-based, Git-governed analytical workspace with Python CLI calculation tools, JSON schemas, dynamic Excel generation, and automated validation.
- **Phase 1 (Target - V2.0+):** Enterprise Multi-Tenant SaaS platform hosting corporate clients, franchise consultants, and prospective franchisees.

---

## 2. Target Cloud-Native Multi-Tenant Architecture

```mermaid
graph TD
    subgraph Client Layer
        Web[Web Application: React + TypeScript + TailwindCSS / AntD]
        Mobile[Mobile Dashboard: Progressive Web App / Flutter]
    end

    subgraph API Gateway & Security
        Gateway[API Gateway / YARP Reverse Proxy]
        Auth[OAuth2 / OIDC Auth0 / Keycloak - RBAC & Tenant Context]
    end

    subgraph Application Backend
        API[Core API Service: ASP.NET Core 8 Web API]
        DocService[Document Generation Service: Python / Aspose / Weasyprint]
        AnalyticsEngine[Quantitative Analytics Service: Python FastAPI + Celery]
    end

    subgraph Data & Storage Layer
        Postgres[(Multi-Tenant PostgreSQL: Row-Level Security RLS)]
        Redis[(Redis Cache: Distributed Session & Rate Limiting)]
        S3[(Encrypted Object Storage: AWS S3 / Azure Blob)]
    end

    Client Layer --> Gateway
    Gateway --> Auth
    Gateway --> API
    API --> Postgres
    API --> Redis
    API --> DocService
    API --> AnalyticsEngine
    DocService --> S3
    AnalyticsEngine --> Postgres
```

---

## 3. Technology Stack Specification

| Component Layer | Technology Choice | Architectural Rationale |
|---|---|---|
| **Frontend Web App** | React 19 + TypeScript + Vite | Rich interactive modeling, type safety, dynamic data visualization (ECharts/Recharts), responsive design. |
| **Backend API Service** | ASP.NET Core 8 Web API | High-throughput asynchronous performance, enterprise security, native dependency injection, clean architecture. |
| **Analytical Engine** | Python 3.12+ (FastAPI + NumPy / Pandas) | Advanced financial math, Monte Carlo simulation, statistical territory scoring, openpyxl/python-pptx integration. |
| **Primary Database** | PostgreSQL 16 with Row-Level Security (RLS) | Relational integrity for contracts/P&Ls, native JSONB support for configurable parameters, proven multi-tenant RLS. |
| **Caching & Messaging** | Redis 7 + Celery / RabbitMQ | Asynchronous execution of heavy Excel generation, report rendering, and caching of client configuration schemas. |
| **Object Storage** | S3-Compatible Encrypted Object Store | Secure, versioned storage of generated PDF deliverables, signed franchise contracts, and raw pitch decks. |

---

## 4. Logical Separation in V0.1 Git Baseline

In the current V0.1 repository, logical separation directly mirrors the future multi-tenant database boundary:
1. **Shared Platform Kernel (`platform/`, `frameworks/`, `tools/`, `schemas/`):** Corresponds to the future multi-tenant backend code, generic business logic, and standard domain entity models.
2. **Tenant Workspaces (`clients/<tenant-slug>/`):** Corresponds to tenant-isolated database rows and secure object containers in the cloud database.
3. **Configuration Contracts (`schemas/*.schema.json`):** Corresponds to the future database DDL and API request validation schemas.
