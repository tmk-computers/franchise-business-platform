# License Decision and Intellectual Property Policy

## 1. Proprietary Status

**Repository Status:** Private & Proprietary  
**Current Classification:** Commercial Confidential — Internal Development & Client Advisory

The **Franchise Business Modeling & Intelligence Platform** code, financial models, architecture documentation, analytical frameworks, schemas, and automation tools are proprietary commercial assets. Unauthorized copying, distribution, reverse engineering, or public publishing of this repository or any portion thereof is strictly prohibited.

---

## 2. Rationale for Private & Proprietary Licensing

1. **Client Confidentiality & Commercial Sensitivity:**
   The platform repository houses working client workspaces (such as `clients/tmk-it-solutions/`), commercial revenue-sharing configurations, financial projections, business strategy frameworks, and competitive positioning research. Public release would compromise proprietary business intelligence and client data.

2. **Core Competitive Advantage:**
   The financial calculation engine, territory scoring heuristics, and revenue-sharing logic represent strategic intellectual property developed for multi-industry franchise modeling and advisory engagements.

3. **Multi-Tenant SaaS Evolution:**
   As the platform evolves toward a software-as-a-service (SaaS) architecture (React + TypeScript frontend, ASP.NET Core Web API backend, PostgreSQL database, and Python analytical microservices), core engine modules and schemas will form the proprietary foundation of a commercial SaaS product.

---

## 3. Client IP Separation and Co-Existence

To ensure clear legal and intellectual boundaries between the platform framework and client deliverables:

- **Platform Frameworks, Tools, and Schemas:**
  All generic frameworks (`frameworks/*`), calculation engines (`tools/*`), JSON schemas (`schemas/*`), and reusable templates (`templates/*`) remain the exclusive intellectual property of the platform maintainers.
- **Client-Specific Deliverables:**
  Materials generated within client directories (e.g., `clients/<client-name>/deliverables/`), signed commercial contracts, finalized pitch decks, and client customer data are owned or licensed in accordance with individual client service agreements.
- **Client Anonymization:**
  No client-specific trademarks, confidential product roadmaps, or non-public financial metrics may be promoted into the generic `frameworks/`, `templates/`, or `schemas/` directories without thorough sanitization and anonymization.

---

## 4. Third-Party Open Source Components

This repository utilizes standard open source libraries under permissive licenses:
- Python packages: `openpyxl` (MIT), `pandas` (BSD-3-Clause), `numpy` (BSD), `pydantic` (MIT), `jsonschema` (MIT), `python-pptx` (MIT), `pytest` (MIT).

All third-party dependencies are linked dynamically or used via standardized interfaces, maintaining compliance with their respective licenses.

---

## 5. Future Open Core Considerations

In future phases (Roadmap V2.0+), the platform steering committee may evaluate releasing selected foundational components (such as generic franchise schemas or basic financial utility functions) under a permissive open-source license (such as Apache 2.0 or MIT) to foster community contributions, while maintaining advanced intelligence models, multi-tenant engines, and proprietary advisory frameworks under commercial licensing.
