# Financial assumptions (Phase 2, first pass — 2026-10-15)

Price year: **2026** (escalate ×1.0609 to 2028-29). Capital (acquisition, renovation, equipment, bus) is **donor-funded without debt** — FOUNDER DECISION (planning assumption). Model: `finance/model.py` → `finance/outputs.md`.

| Input | Value | Label | Source |
|---|---|---|---|
| People cost 30/50/75 | $1,405,600 / $1,969,900 / $2,734,900 | ESTIMATE | research/staffing-volunteers.md §9 (27.2 FTE at 50: 7 teachers, 13 EAs, educational leader, ED, admin, development lead, 0.6 volunteer coordinator, cook, custodian, 0.6 bus driver; EHT; 5% relief; contracted clinicians $245,900) |
| Alternative FTE design | 23.75 FTE (no rotation teacher, 11 EAs, clinicians lighter) | PROPOSAL | research/educational-design.md — **unreconciled with staffing file; founder decision needed** |
| Floor area | 1,000 / 1,400 / 2,000 m² | ASSUMPTION | ~28 m²/student; premises.md |
| Utilities / maintenance / insurance | $33 / $25 / $18 per m² | ESTIMATE | premises.md §9 (QSS 2015-16 $12.53/m² escalated to $14.20–16.30 for a large efficient building; small old buildings higher) |
| Replacement reserve | 1.5% × $3,500/m² replacement value | PROPOSAL | premises.md §9 (1–2% band) |
| Transportation | One sponsored lift bus, two runs: $95K/yr; second bus at 75 students +$75K; outings $15–30K | ESTIMATE | transportation.md (config 3; $69K if attendant absorbed into EA shifts) |
| Meals | $6.25/student/day × 194 days × 1.12 consumables | ESTIMATE | v1 premises note §8; no Ontario benchmark — CONFIRM |
| Supplies/AT/PD/checks + fixed admin | $1,800/student + $60,000 | ESTIMATE | v1 operating table scaled |
| Fundraising program (non-salary) | $30–50K | ESTIMATE | financing.md; development lead salary sits in People |
| Contingency | 5% | ASSUMPTION | v1 |
| In-kind avoided cost (cons./mod.) at 50 | $70K / $165K | ESTIMATE | OHaH $31K/$123K (public-services-partners.md) + volunteer-replaced hours ~$37K (staffing-volunteers.md §9) + donated food $2–10K |
| Restricted service funding at 50 | $55K / $155K | ESTIMATE | Passport $15–40K, OAP $15–60K, SSAH $10–30K, SNP $14–24K — each only pays for the service it funds |
| Unrestricted revenue at 50 | $0 / $20K | ESTIMATE | nothing committed; CSJ, City (non-recurring), enterprise $0–5K |
| Property tax | $0–18K | CONFIRM | MPAC/City — not in model |
| Capital (not in operating model) | Church + modular: $2.9–4.6M, ~$5.3M with soft costs; QSS wing isolation alone $0.5–1.5M; used bus $35–45K | ESTIMATE | premises.md, transportation.md |

Not yet modelled (next pass): monthly cash flow; tiered reserve (audit proposal: 6 months cash + 12-month pledged backstop + one-term wind-down); partnership-shortfall scenario; 2028 escalation; founder decision between the two FTE designs.
