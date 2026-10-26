# Franchise Network Expansion & Scaling Framework

## 1. Purpose
This framework provides strategic principles and phased rollout mechanisms to scale a franchise network from initial pilot units to regional and nationwide coverage. It defines expansion waves, criteria for transitioning from single-unit to multi-unit and master franchise models, and network capacity planning rules.

---

## 2. Business Questions Addressed
1. What phased rollout sequence (Wave 1, Wave 2, Wave 3) minimizes operational strain while establishing regional market density?
2. When is a franchise model ready to transition from direct franchisor management to regional Area Developers or Master Franchisees?
3. What central infrastructure (support engineers, servers, training personnel) is required for every 10 active franchise units added?
4. How do we prevent premature over-expansion that dilutes service quality and exhausts working capital?

---

## 3. Required Inputs
- **Market Prioritization Rankings:** Territory Opportunity Scores ($TOS$) from the Territory Intelligence framework.
- **Franchisor Operational Capacity:** Ratio of central support engineers and trainers to active operating franchise units.
- **Capital Reserves:** Expansion marketing and onboarding budget.

---

## 4. Methodology & Phased Rollout Waves

```mermaid
graph TD
    subgraph Wave 1: Pilot & Proof (Months 1 - 6)
        W1[3 - 5 Contiguous Pilot Territories: Close proximity, high oversight, direct franchisor support]
    end

    subgraph Wave 2: Regional Cluster (Months 7 - 18)
        W2[15 - 25 Regional Territories: Adjacent districts, proven sales playbook, standardized training]
    end

    subgraph Wave 3: National Scale (Months 19 - 36)
        W3[50 - 100+ Territories: Multi-state rollout, Area Developers, automated partner portal]
    end

    W1 --> W2
    W2 --> W3
```

---

## 5. Calculation Logic & Central Support Capacity Ratio

To preserve service quality and contract SLAs, franchisor central staffing scales according to defined capacity ratios:
$$\text{Required Central Support Engineers } (E_{sup}) = \left\lceil \frac{U_{active} \times \bar{N}_{cust\_per\_unit}}{C_{engineer\_load}} \right\rceil$$
Where:
- $U_{active}$ = Count of active franchise units.
- $\bar{N}_{cust\_per\_unit}$ = Average active customer software deployments per unit.
- $C_{engineer\_load}$ = Maximum customer accounts supported per central engineer (e.g., 50 accounts).

---

## 6. Expected Outputs
1. **Three-Year Network Expansion Roadmap.**
2. **Central Staffing & Infrastructure Capacity Plan.**
3. **Master Franchise Eligibility Evaluation Matrix.**

---

## 7. Risks and Limitations
- **Premature Scaling:** Launching Wave 2 before the core product sales playbook achieves reproducible unit economics in Wave 1 leads to widespread partner dissatisfaction.
- **Geographic Fragmentation:** Opening isolated units thousands of kilometers apart dramatically increases travel costs and dilutes local brand recognition.

---

## 8. Acceptance Criteria
- Wave 1 units must demonstrate at least 3 consecutive months of positive operating EBITDA before Wave 2 territory sales commence.
- Central support capacity must be funded and hired 60 days ahead of projected unit onboarding.

---

## 9. Example Application: TMK IT Solutions LLP
- **Wave 1 (Months 1–6):** 5 talukas in Western Maharashtra (Pune, Pimpri-Chinchwad, Baramati, Satara, Nashik).
- **Wave 2 (Months 7–18):** 20 talukas across Maharashtra and South Gujarat.
- **Wave 3 (Months 19–36):** 60+ talukas spanning major education and industrial districts across Western and Central India.
