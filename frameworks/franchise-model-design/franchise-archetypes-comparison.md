# Franchise Archetypes & Operating Model Design Framework

## 1. Purpose
This framework provides a systematic, objective methodology for evaluating, selecting, and designing franchise business models across commercial industries. It establishes structural boundaries, capital allocation rules, and operational responsibility matrices for ten distinct franchise archetypes.

---

## 2. Business Questions Addressed
1. What franchise archetype (FOFO, FOCO, COCO, COFO, Master, Area Dev, Multi-Unit, Sales, Distribution, Hybrid) aligns with our capital structure, operational capabilities, and expansion velocity?
2. Who owns the physical or digital assets, who funds working capital, and who manages daily sales and delivery?
3. What are the legal, commercial, and operational failure modes of each archetype?
4. How should responsibilities be divided across marketing, customer acquisition, delivery, technical support, billing, and compliance?

---

## 3. Required Inputs
- **Capital Intensity:** Real estate, inventory, equipment, or software setup costs.
- **Operational Complexity:** Skill level required for local operations (sales-only vs. complex technical delivery vs. retail supply chain).
- **Brand & Quality Sensitivity:** Risk to brand equity if a local operator underperforms.
- **Regulatory Environment:** Local licensing, tax compliance, labor laws, and consumer protection mandates.
- **Scalability Velocity Goals:** Required number of operating nodes over a 12, 24, and 36-month horizon.

---

## 4. Methodology & Archetype Taxonomy

### 4.1. Comparative Taxonomy of 10 Franchise Archetypes

| Archetype | Name | CapEx Ownership | Daily Operations | Revenue & Profit Model | Primary Advantages | Critical Limitations / Failure Modes | Best Suited For |
|---|---|---|---|---|---|---|---|
| **FOFO** | Franchise Owned, Franchise Operated | Franchisee | Franchisee | Franchisee retains local operating margin; pays joining fee + royalty or shares revenue (e.g., 40:60 split). | Rapid asset-light scaling; highly motivated local entrepreneur; zero franchisor real estate risk. | Inconsistent service quality; franchisee may under-invest in local sales; territory disputes. | Software products, specialized consulting, education, service agencies. (Used by TMK IT Solutions). |
| **FOCO** | Franchise Owned, Company Operated | Franchisee | Franchisor | Franchisee receives fixed minimum guarantee or percentage of top-line revenue; franchisor manages staff and P&L. | High brand consistency; attracts pure financial investors who lack operating skills. | Franchisor carries operational headcount burden; high management overhead across distributed units. | QSR chains, boutique retail, healthcare clinics, hospitality. |
| **COCO** | Company Owned, Company Operated | Franchisor | Franchisor | Franchisor retains 100% of top-line and net profit. | Total quality control; rapid experimentation; uncompromised customer experience. | Extremely capital intensive; slower geographical expansion; high fixed administrative overhead. | Flagship pilot units, high-security manufacturing, luxury brands. |
| **COFO** | Company Owned, Franchise Operated | Franchisor | Franchisee | Franchisor leases or owns asset; franchisee pays operational lease and retains operational profit. | Fast turnaround of underperforming corporate assets; leverages experienced local operators. | Franchisee may neglect franchisor-owned physical assets; complex lease agreements. | Highway service stations, railway retail kiosks, government concessions. |
| **Master Franchise** | Master Franchise Agreement | Master Franchisee | Sub-Franchisees & Master Unit | Master franchisee pays substantial territory fee; sub-franchises territory and splits royalties with franchisor. | Immediate regional scaling; local market adaptation; franchisor deals with single point of regional contact. | Loss of direct relationship with end franchisees; franchisor dependent on master franchisee competency. | National or international brand expansion across states or countries. |
| **Area Development** | Area Developer Model | Area Developer | Area Developer | Developer commits to opening N units directly within territory over T years; pays discounted upfront fees. | Faster unit rollout with fewer distinct partners; institutional capital backing. | If developer faces financial distress, expansion halts across the entire territory. | Fast-casual dining, fitness centers, regional supermarket chains. |
| **Multi-Unit** | Multi-Unit Franchisee | Franchisee | Franchisee (Multi-Unit Management) | Economies of scale across 3-10 units; single corporate franchisee entity. | Lower support cost per unit for franchisor; more professional management and governance. | Concentration risk; multi-unit franchisee can exert disproportionate bargaining power. | Established franchise brands expanding with high-net-worth operators. |
| **Product Distribution** | Product Distribution Franchise | Dealer / Franchisee | Dealer / Franchisee | Margin spread between wholesale purchasing price and authorized retail price. | Simple legal structure; focused purely on inventory turnover and channel logistics. | Low customer engagement; risk of gray-market discounting or brand dilution. | Automotive dealerships, industrial machinery, packaged consumer goods. |
| **Sales Franchise** | Sales & Commission Franchise | Franchisee (Sales Office) | Franchisee (Local Sales Team) | Franchisee earns commission on deal closure; franchisor handles 100% of delivery and billing. | Minimal inventory risk; rapid sales force deployment; low capital barrier for franchisee. | Low switching cost for franchisee; high sales churn if product adoption stalls. | B2B enterprise software, corporate insurance, financial services. |
| **Hybrid Franchise** | Blended Digital / Physical Franchise | Shared | Shared (Split by Function) | Tiered split (e.g., local sales share + central subscription delivery share). | Optimizes core competencies: local relationship selling combined with central technical delivery. | Requires sophisticated multi-party billing and clear operational RACI matrices. | Cloud software ecosystems, omnichannel retail, telemedicine. |

---

### 4.2. Comprehensive Master RACI Matrix

The following RACI matrix (*Responsible, Accountable, Consulted, Informed*) defines operational boundaries for standard **FOFO & Hybrid Software/Service Franchise Models**:

| Functional Domain | Key Operational Task | Franchisee | Franchisor Central Team | Customer |
|---|---|---|---|---|
| **Setup & Facilities** | Office Lease, Interior, Local Hardware Setup | **A / R** | C | I |
| **Setup & Facilities** | Brand Standards & Signage Compliance | R | **A** | I |
| **Talent & Staffing** | Hiring & Payroll of Local Sales Personnel | **A / R** | C | - |
| **Talent & Staffing** | Sales Training & Product Certification | R | **A** | - |
| **Marketing & Leads** | Local Field Marketing, Local Networking, Cold Outreach | **A / R** | C | - |
| **Marketing & Leads** | National Brand Advertising & Digital Campaign Collateral | I | **A / R** | - |
| **Sales Process** | Customer Discovery & Preliminary Product Pitch | **A / R** | C | R |
| **Sales Process** | Complex Technical Demonstration & Architecture Review | C / R | **A / R** | R |
| **Sales Process** | Proposal Generation & Standard Contract Pricing | R | **A** | I |
| **Billing & Finance** | Customer Invoicing & GST Tax Remittance | I | **A / R** | R |
| **Billing & Finance** | Franchise Commission Settlement & Reconciliation | R | **A / R** | - |
| **Delivery & Implementation**| Software Deployment, Cloud Provisioning, Data Migration | I | **A / R** | C |
| **Support & Operations** | Level-1 Initial Triage & Relationship Management | **A / R** | C | I |
| **Support & Operations** | Level-2 / Level-3 Bug Fixes, Code Updates, Cloud Uptime | I | **A / R** | I |
| **Renewals & Growth** | Annual License Renewal Follow-up & Commercial Extension | **A / R** | C | R |

---

## 5. Calculation Logic & Decision Heuristics

To determine the optimal archetype score $S_m$ for a candidate model $m$:
$$S_m = \sum_{i=1}^{n} w_i \cdot C_{i,m}$$
Where:
- $w_i$ = Strategic priority weight ($\sum w_i = 1.0$) across criteria: Capital Availability ($w_1$), Speed to Market ($w_2$), Quality Control Sensitivity ($w_3$), Local Market Nuance ($w_4$).
- $C_{i,m}$ = Fit score (1 to 5) of model $m$ against criterion $i$.

---

## 6. Expected Outputs
1. Completed Archetype Suitability Scorecard.
2. Formalized Client Responsibility Matrix (RACI).
3. Contractual Term Sheet boundaries defining asset ownership, termination rights, and audit covenants.

---

## 7. Risks and Limitations
- **Model Inversion:** Attempting to force a FOFO model when the product requires complex engineering delivery creates customer churn if the franchisee lacks technical depth.
- **RACI Friction:** Misunderstandings regarding Level-1 vs. Level-2 customer support will lead to customer abandonment.

---

## 8. Acceptance Criteria
- Every task in the RACI matrix has exactly one party Accountable (**A**).
- Archetype selection is supported by a documented evaluation against minimum capital requirements and operational capability.

---

## 9. Example Application: TMK IT Solutions LLP
- **Selected Archetype:** FOFO (Franchise Owned, Franchise Operated) Hybrid.
- **Rationale:** TMK IT Solutions develops complex software products. Software development, hosting, and implementation must remain centralized (Franchisor Accountable) to protect IP and ensure uptime. Conversely, local sales, school/business customer relationship management, and demo coordination are best performed by local entrepreneurs with regional market presence (Franchisee Accountable).
