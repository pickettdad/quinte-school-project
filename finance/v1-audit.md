# Audit of the v1 financial model (report of 2026-10-14)

**Status:** Phase 2 desk audit, 2026-10-15. Audits the calculations and conclusions in `reports/2026-10-14-feasibility-report-v1.md` (section 9 and the figures it carries from sections 3, 5 and 7) and the underlying notes `reports/2026-10-14-v1-research-notes/premises_staffing_costs.md` (Q5–Q10), `funding_and_financing.md` (KQ7) and `educational_design_and_comparables.md` (section 8). Nothing in the v1 files has been edited; this file records where they are right, where they are wrong, and what the Phase 2 model (`finance/model.py`) should take from them.

**Labels:** VERIFIED (from the v1 files, with file and section, or a primary source read today) / SECONDARY (reputable commentary) / ESTIMATE (formula shown) / PROPOSAL (recommendation, not approved) / ASSUMPTION (planning assumption) / CONFIRM (needs a named authority) / FOUNDER DECISION (from `docs/decision-log.md`).

**Price year:** all v1 figures are stated as "2028-29 prices" but are built from 2026 wage and rate benchmarks with no escalation applied (premises note Q10.B header says "escalate ~3%/yr" but the table does not). Treat every v1 figure as **2026 prices** unless the model builder escalates them explicitly. ESTIMATE.

---

## 1. Reconciliation of the "People" line (12 / 20 / 30 students)

### 1.1 What the v1 report says

Section 9 of the v1 report states the people line as $631,400 / $945,300 / $1,314,400 and lists its contents in one cell: "2/3/4 special-ed teachers at $82.6K loaded; 4/6/8 EAs at $45.4K; 0.5/0.75/1.0 principal; admin; cook; custodian; contracted SLP, OT, BCBA, psychologist; 4% relief; development staff" (VERIFIED, v1 report §9 operating table). Teachers plus EAs at 30 students are 4 × $82,600 + 8 × $45,400 = $330,400 + $363,200 = **$693,600**, leaving **$620,800** unexplained in the report itself. The premises note (Q6, "Inferences — staffing cost tables") carries the full table.

### 1.2 Line-by-line reconciliation, 30 students

Every unit cost below is VERIFIED from premises note Q6 ("Unit costs chosen" paragraph and the table). Hours × rates are recomputed here.

| # | Line | Basis (premises note Q6) | Arithmetic | $ | Classification of the choice |
|---|---|---|---|---|---|
| 1 | Special-education teachers | 4 × $82,600 loaded ($70,000 base × 1.18) | 4 × 82,600 | 330,400 | Ratio: PROPOSAL (one teacher per "band"); rate: ASSUMPTION (set below public grid) |
| 2 | Educational assistants | 8 × $45,400 loaded ($26.00/h × 7.5 h × 194 d × 1.20) | 8 × 45,400 | 363,200 | Ratio: PROPOSAL (2 EAs per class, from comparators); rate: ASSUMPTION |
| | **Sub-total teachers + EAs** | | | **693,600** | |
| 3 | Principal / coordinator | 1.0 FTE × $100,000 × 1.18 | 1.0 × 118,000 | 118,000 | Statutory in substance: Ministry validation requires "a principal in charge" (v1 report §8, VERIFIED); salary level ASSUMPTION |
| 4 | Admin / bookkeeper | 1.0 FTE × $23.45 × 2,080 h = $48,776 × 1.20 | 1.0 × 58,500 | 58,500 | Planning assumption; a charity with audit obligations (revenue ≥ $500K, v1 §8 VERIFIED) needs bookkeeping; 1.0 FTE at 30 students is a v1 researcher choice |
| 5 | Cook / food coordinator | 1.0 FTE × $20.75 × 2,080 h = $43,160 × 1.20 | 1.0 × 51,800 | 51,800 | v1 researcher choice (12-month FTE for a 194-day program; see §3.4 below) |
| 6 | Custodian | 1.0 FTE × $45,635 × 1.20 | 1.0 × 54,800 | 54,800 | v1 researcher choice; **contradicts the note's own benchmark** (Q5: ~14 h/week for 10,000 sf ≈ 0.35 FTE) |
| 7 | SLP (contract) | 16 h/wk × 40 wk × $120/h | 640 h × 120 | 76,800 | Professional recommendation (comparators employ SLP); hours and rate ASSUMPTION |
| 8 | OT (contract) | 12 h/wk × 40 wk × $100/h | 480 h × 100 | 48,000 | Professional recommendation; hours and rate ASSUMPTION |
| 9 | Behaviour consultant / BCBA (contract) | 16 h/wk × 40 wk × $125/h | 640 h × 125 | 80,000 | Professional recommendation (behaviour plans "implementable without restraint", v1 §2); hours ASSUMPTION |
| 10 | Psychologist (contract) | 120 h/yr × $210/h | 120 × 210 | 25,200 | Professional recommendation (assessments by 16 for DSO/Passport, v1 §1); hours ASSUMPTION |
| | **Staffing subtotal (note's figure $1,206,700)** | | 693,600 + 513,100 | **1,206,700** | reconciles exactly |
| 11 | Supply / relief allowance | 4% × (teachers + EAs) = 0.04 × 693,600 = 27,744, shown as 27,700 | | 27,700 | Planning assumption; thin (see §3.3) |
| 12 | Fundraising / development staff | 1.0 FTE at $80,000 loaded | | 80,000 | v1 researcher choice; **moved out of the people line in the Phase 2 treatment (§7)** |
| | **Total people (note's figure $1,314,400)** | | 1,206,700 + 27,700 + 80,000 | **1,314,400** | reconciles exactly |

**The $620,800 is therefore:** principal 118,000 + admin 58,500 + cook 51,800 + custodian 54,800 + SLP 76,800 + OT 48,000 + BCBA 80,000 + psychologist 25,200 + relief 27,700 + development 80,000 = **620,800** (VERIFIED, sums exactly to the note's figures; the only rounding is relief 27,744 → 27,700). Nothing is missing and nothing is unexplained; the report's section 9 simply compressed ten lines into one cell.

What each component buys: lines 3–4 are the legal minimum of running a validated private school that is also a registered charity (a principal; books that can be audited). Lines 5–6 are the operating consequence of the v1 design choices "meals included" and "own the building". Lines 7–10 are the clinical layer that comparators (Summit, Renfrew) employ in-house at 500+ students and that v1 proposed to contract (educational note §8, PROPOSAL, VERIFIED as the note's recommendation). Line 11 is absence cover. Line 12 is fundraising capacity.

### 1.3 Reconciliation, 12 students ($631,400)

| Line | Arithmetic | $ |
|---|---|---|
| Teachers | 2 × 82,600 | 165,200 |
| EAs | 4 × 45,400 | 181,600 |
| Principal | 0.5 × 118,000 | 59,000 |
| Admin | 0.4 × 58,500 | 23,400 |
| Cook | 0.5 × 51,800 | 25,900 |
| Custodian | 0.5 × 54,800 | 27,400 |
| SLP | 8 × 40 × 120 | 38,400 |
| OT | 6 × 40 × 100 | 24,000 |
| BCBA | 8 × 40 × 125 | 40,000 |
| Psychologist | 60 × 210 | 12,600 |
| **Staffing subtotal** | | **597,500** (matches note) |
| Relief | 0.04 × 346,800 = 13,872 → 13,900 | 13,900 |
| Development | 0.25 FTE | 20,000 |
| **Total people** | 597,500 + 13,900 + 20,000 | **631,400** (matches note) |

Non-teacher/EA remainder = 631,400 − 346,800 = $284,600. VERIFIED.

### 1.4 Reconciliation, 20 students ($945,300)

| Line | Arithmetic | $ |
|---|---|---|
| Teachers | 3 × 82,600 | 247,800 |
| EAs | 6 × 45,400 | 272,400 |
| Principal | 0.75 × 118,000 | 88,500 |
| Admin | 0.6 × 58,500 | 35,100 |
| Cook | 0.6 × 51,800 = 31,080 → 31,100 | 31,100 |
| Custodian | 0.75 × 54,800 | 41,100 |
| SLP | 12 × 40 × 120 | 57,600 |
| OT | 8 × 40 × 100 | 32,000 |
| BCBA | 12 × 40 × 125 | 60,000 |
| Psychologist | 90 × 210 | 18,900 |
| **Staffing subtotal** | | **884,500** (note: 884,500; exact sum is 884,480, rounded) |
| Relief | 0.04 × 520,200 = 20,808 → 20,800 | 20,800 |
| Development | 0.5 FTE | 40,000 |
| **Total people** | 884,500 + 20,800 + 40,000 | **945,300** (matches note) |

Non-teacher/EA remainder = 945,300 − 520,200 = $425,100. VERIFIED (rounding of $20 inside the cook line).

### 1.5 Observations on the reconciliation

- **Group sizes implied.** 12 students / 2 classes = 6.0; 20 / 3 = 6.7; 30 / 4 = 7.5 per class — all at the bottom of the comparator range (6–12) the v1 educational note itself documents (§8, VERIFIED). The v1 model is therefore a *high-intensity* staffing model even before relief or supervision are considered. ESTIMATE.
- **Adult:student ratio implied** (teachers + EAs only): 30 students, 12 adults → 1:2.5, denser than DDSB (6:1:2 = 1:2), OCDSB DD (10:1:2.4 = 1:2.9), Oak Bridge (1:3.3) and Summit (10–12 with ≥2 staff ≈ 1:5–6). ESTIMATE from VERIFIED ratios in educational note §8.
- **Therapy as a share.** Contracted clinicians are $115,000 at 12 students (19.2% of the staffing subtotal), $168,500 at 20 (19.1%) and $230,000 at 30 (19.1%): the v1 researcher scaled therapy hours in proportion to enrolment, which is a choice, not evidence. ESTIMATE.

---

## 2. Loaded-cost factors

### 2.1 Recomputation of the v1 factors (2026 statutory rates, VERIFIED in premises note Q6 "Statutory employer costs")

Inputs: CPP employer 5.95% on (earnings − $3,500) up to YMPE $74,600; CPP2 4% on earnings between $74,600 and $85,000; EI employer 2.282% up to MIE $68,900; WSIB Class D1 Educational Services $0.33 per $100; EHT nil (registered-charity exemption on the first $1M of payroll — note this requires the school to *be* a registered charity; before registration, EHT at 0.98–1.95% would apply above the ordinary exemption, CONFIRM with the Ministry of Finance); vacation pay 4% (ESA, <5 years); group benefits 8% (v1 PROPOSAL, no survey).

**Teacher, $70,000 base (10-month, salaried):**

| Item | Formula | $ |
|---|---|---|
| CPP | 0.0595 × (70,000 − 3,500) | 3,956.75 |
| CPP2 | 70,000 < 74,600 → 0 | 0.00 |
| EI | 0.02282 × min(70,000; 68,900) | 1,572.30 |
| WSIB | 0.0033 × 70,000 | 231.00 |
| EHT | charity exemption | 0.00 |
| Vacation | salaried; taken as paid time within salary | 0.00 |
| Benefits | 0.08 × 70,000 | 5,600.00 |
| **Total on-costs** | | **11,360.05 = 16.23%** |
| v1 working factor | 1.18 × 70,000 | **82,600** (cushion of $1,240 per teacher over the computed 16.2%) |

**EA, $26.00/h × 7.5 h × 194 days = $37,830 base (hourly):**

| Item | Formula | $ |
|---|---|---|
| CPP | 0.0595 × (37,830 − 3,500) | 2,042.64 |
| EI | 0.02282 × 37,830 | 863.28 |
| WSIB | 0.0033 × 37,830 | 124.84 |
| Vacation | 0.04 × 37,830 | 1,513.20 |
| Benefits | 0.08 × 37,830 | 3,026.40 |
| **Total on-costs** | | **7,570.36 = 20.01%** |
| v1 working factor | 1.20 × 37,830 = 45,396 | **45,400** |

Both v1 factors are arithmetically sound (VERIFIED by recomputation). Two statutory items are missing from the hourly factor:

- **Public-holiday pay (ESA).** The 194 paid days are days worked; Ontario's public holidays falling in the school year (Labour Day, Thanksgiving, Christmas, Boxing Day, New Year's, Family Day, Good Friday, Victoria Day — about seven inside a September–June contract) are paid days *not* worked for hourly staff. ESTIMATE: 7 × 7.5 h × $26 = **$1,365 per EA (+3.6%)**, ≈ $10,900 for 8 EAs. Statutory, omitted.
- **Sick leave.** ESA sick leave is unpaid (3 days), so nothing is statutorily missing; but a school that offers no paid sick days to EAs will not retain them against HPEDSB (11 days at 100%). Any paid sick days are a cost *on top of* the relief allowance, because the absent employee and the supply are both paid. Professional recommendation; not costed in v1.

No pension is included (v1 says so explicitly: "add 3–5% if a group RRSP match is offered"). Professional recommendation for retention; ASSUMPTION either way.

### 2.2 Why HPEDSB's $138K/teacher and $55K/EA are so much higher

The HPEDSB figures are budget-book divisions (classroom-teacher expense $117,385K ÷ 847.8 FTE; teacher-assistant expense $15,816K ÷ 286.7 FTE), VERIFIED inputs, ESTIMATE division (premises note Q6). The gap to v1's $82.6K is $55.4K per teacher. An indicative bridge, all ESTIMATE/SECONDARY:

| Component | HPEDSB (public board) | v1 private model | Gap |
|---|---|---|---|
| Base salary | Ontario grid runs from ≈ $52,800 (A0 step 0) to ≈ $107,500 (A4 step 10+) under the 2024–26 central agreements (SECONDARY, [bremo.io illustrative grid, 2026](https://bremo.io/teacher-salary-ontario-2026); CONFIRM against the ETFO/OSSTF central agreements). A board with a mature workforce averages roughly $95–100K. | $70,000 (≈ A3 step 0 / A1 step 5) | ≈ $25–30K |
| Pension | OTPP: employer-matched contributions of roughly 10–12% of salary (SECONDARY; OTPP contribution rate 10.4% to the CPP limit and 12% above, employer matched; CONFIRM current rate) ≈ $10–12K | none | ≈ $10–12K |
| Health/dental/LTD benefits | Board-funded ELHT plans ≈ $8–10K per FTE (SECONDARY; no plan document read) | 8% = $5,600 | ≈ $3–4K |
| Statutory (CPP/CPP2/EI/WSIB) | on ≈ $97K: CPP 4,230 + CPP2 416 + EI 1,572 + WSIB 320 ≈ $6.5K | $5.8K | ≈ $0.7K |
| Occasional-teacher cover, allowances, preparation time | "Classroom teacher" expense in board budgets includes occasional (supply) teachers, department/positions-of-responsibility allowances and the FTE that delivers contractual preparation time (ETFO: 240 min/week elementary). In a 4-teacher school, prep time means someone else must be with the class. | 4% relief only; no prep cover | ≈ $8–12K |
| **Total** | **≈ $138K** | **$82.6K** | **≈ $55K** |

The bridge is indicative (ESTIMATE); the components to CONFIRM are the current grid, OTPP employer rate and ELHT cost per FTE. The point for Phase 2 is not that $70K is wrong — Indeed's Belleville special-education average is $82,877 and the Bayfield Treatment Centres proxy is $58,504 (VERIFIED, premises note Q6) — but that a $70K flat salary buys a *junior* teacher (grid step 0–5) or an experienced teacher taking a 25–35% cut, with no pension. The 50-student model should carry a salary *distribution* (e.g., one lead teacher at $90–95K, others at $65–75K) and a pension decision, with the sensitivity v1 already quantified (+$222K at 30 students if paid at the public loaded rate, VERIFIED premises note Q10.C).

For EAs the gap ($55.2K − $45.4K = $9.8K) decomposes as: hourly rate (HPEDSB ≈ $51.8K ÷ (7 h × 194 d) ≈ $38/h on an annualised basis versus $26/h — but board EAs are paid for roughly 194–200 days at 6.5–7 h, so the rate gap is nearer $5–7/h ≈ $7–10K); OMERS pension (employer ≈ 9%, SECONDARY) ≈ $4K; benefits; partly offset by the v1 7.5-h day. ESTIMATE; CONFIRM against the CUPE/OSSTF educational-worker local agreement if a ceiling is needed.

---

## 3. Staffing ratios against the proposed student profile

### 3.1 Status of "two EAs per class"

- **Statutory:** none. O. Reg. 298 s.31 sets *class-size maxima* for boards (DD 10; autism/multiple 6; MID 12–16) and does not bind a private school (VERIFIED via Ministry summary, v1 report §1; regulation text not read). No Ontario regulation prescribes an EA ratio for any school, public or private. Ontario provides no staffing standard for private schools at all ("does not inspect or approve … staffing", VERIFIED v1 report §8).
- **Professional recommendation:** the comparator pattern is one teacher plus two assistants for *developmental-disability* groups of 6–10 (DDSB minimum 2 EAs for ≤6; OCDSB 2.4 EAs per DD class of ≤10; Oak Bridge 10:1:2; Project SEARCH 10:1:2), but one EA per class for *MID* groups (OCDSB GLP) and one job coach per 12 for independent transition students (Storefront) — all VERIFIED in educational note §8. The EEF guidance that assistants "supplement, not replace" the teacher is a quality argument, not a ratio (VERIFIED v1 §1).
- **Planning assumption (v1):** uniform 1:2 for every class regardless of profile, and classes of 6–7.5 rather than 8–12. That is the v1 researcher's choice and is the single largest driver of the per-student cost.

### 3.2 Mixed group sizes for a 50-student school (PROPOSAL)

The Phase 2 brief defines the opening population as students who can "take part in small-group instruction and shared activities with the resources available", excludes continuous 1:1 and nursing-delegated needs at opening, and asks for small groups "matched to actual skills and learning needs; groupings may differ by subject" (FOUNDER DECISION, brief §Students). The v1 admission domains (group of 4–6 with adult support; toileting with prompts; ambulatory) describe the same population (v1 §2, PROPOSAL). For that population:

| Group type | Students per teacher | EAs | Adults : students | Comparator anchor |
|---|---|---|---|---|
| Higher-support DD group (communication/regulation needs) | 6–8 | 2.0 | 1 : 2.3 | DDSB, OCDSB DD |
| Standard DD/mixed group | 8–10 | 1.5 (one full-time, one shared) | 1 : 3.6 | Oak Bridge, Summit |
| MID / independent secondary & transition group | 10–12 | 1.0 | 1 : 5.5 | OCDSB GLP, Storefront, BC 1:6 floor |

Fifty students arranged as, say, 2 higher-support groups (14), 2 standard groups (18) and 2 MID/transition groups (18) need **6 teachers and 9 EAs** (2+2+1.5+1.5+1+1), an overall ratio of 15 adults : 50 students = 1:3.3 — inside the comparator band (1:3 to 1:4 for DD, up to 1:6 for MID; VERIFIED range, educational note §8). ESTIMATE: 6 × $82,600 + 9 × $45,400 = $495,600 + $408,600 = **$904,200** for 50 students versus v1's $693,600 for 30. The homeroom staffing stays reliable because every group keeps one teacher and at least one EA when volunteers are absent (brief §Staffing). Subject regrouping for literacy blocks (Allor's 1–4 per instructor, VERIFIED v1 §1) is achieved by pooling the 15 paid adults plus trained volunteers across two adjacent groups for 45 minutes, not by hiring more staff. This is a PROPOSAL for `research/educational-design.md` and `research/staffing-volunteers.md` to test; it is not adequate for a cohort that turns out to need 1:1.

### 3.3 What v1 did not include

| Omission | Status | Indicative cost at 30 students (ESTIMATE) |
|---|---|---|
| Relief beyond 4% | 4% = 7.8 days per FTE per year. Ontario education-worker absence commonly runs 10–15 days/yr (SECONDARY, widely reported board sick-leave data; CONFIRM with HPEDSB's own absence rate). A supply EA at $26/h × 7.5 h = $195/day; a supply teacher $250–300/day. | Raising relief to 6% of teacher+EA cost: +$13,900; to 8%: +$27,700 |
| Paid sick days (if offered) | Professional recommendation (retention); not statutory | 5 paid days × 12 staff × ≈ $220 = ≈ $13,000 |
| Public-holiday pay for hourly staff | Statutory (ESA) | ≈ $10,900 (§2.1) |
| Lunch, arrival and dismissal supervision | The 7.5-h EA day (8:00–4:00 less a 30-minute unpaid lunch) covers a 8:30–3:30 student day only if lunches are staggered inside each class's three adults; with 1.5 EAs per class this needs a schedule, not more money. Staggered start/end times (brief §Transportation) stretch the *building* day to ≈ 8:00–4:30; staff shifts stagger with the cohorts, so total hours do not rise if designed together. | $0 if scheduled; +6.7% on the EA line (+$24,300) if every EA is paid 8 h |
| Teacher preparation time | No cover for teacher prep in v1; in a one-teacher class an EA alone with students for 200–240 min/week. Professional recommendation: cover prep with the principal/lead teacher or a 0.2 FTE float teacher. | 0.2 FTE teacher ≈ $16,500 |
| EA ride-along time on buses | v1 assumes it "within the EA day" (premises note Q7), which conflicts with a 7.5-h day that already covers the school day; the note's own figure if paid: $10,100 per bus per year. Moot in the Phase 2 base case (no door-to-door transport). | $0 base; +$10,100 per bus in the transport module |
| Volunteer coordination, screening, training | Required by the brief ("coordination, screening, training, supervision, semester gaps and backups costed"). Not in v1 at all. | 0.5–1.0 FTE coordinator ≈ $30–60K loaded; vulnerable-sector checks (Belleville Police fee, CONFIRM) and training ≈ $2–5K/yr |
| Executive director distinct from principal | Brief requires paid executive *and* educational leadership; v1 had one $118K "principal/coordinator". | +1.0 FTE ED ≈ $100–120K loaded, or a principal + 0.5 ED |
| Bus driver as employee | Only if the school owns a (donated) bus; v1 put the driver inside the $46.5–51K per-bus owned cost (premises note Q7, VERIFIED), so it is not an omission there, but it moves to the people line with WSIB class F2 ($1.43/$100) if the school employs the driver. | $20,500 per bus (inside transport module) |
| Nursing / PSW | Not in v1 (assumed OHaH; v1 §5). Correct for the opening profile; becomes a cost if the admitted profile widens. | $0 at opening; CONFIRM OHaH scope (OQ-3) |

### 3.4 What v1 may have over-counted

- **Custodian 1.0 FTE at 30 students** against the note's own ratio (≈ 14 h/week ≈ 0.35 FTE for 10,000 sf; premises note Q5, ESTIMATE). A school with a teaching kitchen and toileting support justifies more than the board ratio, but 0.5–0.6 FTE is defensible: ≈ **−$22–27K**. ESTIMATE.
- **Cook 1.0 FTE (2,080 h) at 30 students** for a 194-day program; 194 × 7.5 h = 1,455 h is the service need unless summer programming is offered: ≈ **−$15K** at a 0.7 FTE. ESTIMATE.
- **Layered buffers.** Relief 4% + contingency 5% + capital reserve + an 18–24-month operating reserve are four separate cushions on the same cost base. Not a double count in accounting terms, but the model should state which risk each one covers so that donors are not asked to fund the same risk twice (see §8).
- **Working capital counted twice.** The start-up budget contains "Working capital (3 months of operating cost) $250–300K" (premises note Q10.A, VERIFIED), and the funding gate adds an "18–24-month operating reserve … on top of ≈ $2.1–2.8M of start-up" (v1 report §9, VERIFIED). The three months inside start-up *is* the first three months of that reserve: **$250–300K is double-counted** in the headline gate. ESTIMATE.
- **Therapy scaled linearly with enrolment** (§1.5): consultation models (BCBA, SLP program-level coaching) do not scale 1:1 with students.

---

## 4. Therapy costs and the overlap with public and insured services

### 4.1 What v1 carries (VERIFIED, premises note Q6 table)

| Service | 12 students | 20 | 30 |
|---|---|---|---|
| SLP | 38,400 | 57,600 | 76,800 |
| OT | 24,000 | 32,000 | 48,000 |
| BCBA / behaviour consultant | 40,000 | 60,000 | 80,000 |
| Psychologist | 12,600 | 18,900 | 25,200 |
| **Total** | **115,000** | **168,500** | **230,000** |

The report's "$115K of contracted SLP/OT/BCBA/psychology" at 12 students (v1 §9) reconciles exactly.

### 4.2 Overlap (flagged for `research/public-services-partners.md`; eligibility is being researched by another agent)

- **Ontario Health atHome School Health Support Services** are stated to be available to students in "a publicly funded school, private school, or home-school program", including nursing, dietitian and — for private-school students, because Children's Treatment Centres serve only public schools — PT, OT and SLP, on the principal's referral (VERIFIED from the fact sheet as cited in v1 §5; OQ-3 open). This overlaps v1 lines SLP and OT directly and nursing (not costed) entirely. It does **not** overlap BCBA (not a health service OHaH delivers) or psychology (OHaH does not provide psychological assessment).
- **Family health benefits** (brief §Public and insured services): typical employer plans cap paramedical categories at a few hundred to ~$1,500 per practitioner per year (ASSUMPTION; no plan read) — material for psychology (assessments $2,500–4,000 privately, ASSUMPTION) and marginal for SLP/OT at the hours v1 assumed. Use is voluntary, never an admission factor and never school revenue (FOUNDER DECISION).
- **OAP** core clinical funding can pay for BCBA-supervised ABA, SLP and OT for autistic students only when delivered or supervised by college-registered professionals (VERIFIED v1 §5) — a family-directed purchase, not a school revenue line.

### 4.3 Conditions under which the contracted line could fall (PROPOSAL)

| Condition | Effect on the 30-student line |
|---|---|
| OHaH South East confirms private-school eligibility *and* assesses direct SLP/OT for referred students (student-by-student, assessed hours — not a school-wide block) | Drop OT (−$48,000); halve SLP, retaining 8 h/week of *program-level* consultation for AAC systems and staff coaching, which OHaH's direct-therapy model does not provide (−$38,400). Keep BCBA and psychologist. **Revised total $143,600 (−$86,400).** |
| OHaH eligible but local availability or assessed hours are thin (the brief's distinction between eligibility and delivery) | Keep SLP at 12 h/wk, OT at 6 h/wk: $57,600 + $24,000 + $80,000 + $25,200 = **$186,800 (−$43,200)** |
| OHaH not available to the school's students | v1 figure stands: **$230,000** |
| Psychology at intake | Psychologist hours should be driven by intake volume, not enrolment: most applicants already hold a recent psycho-educational assessment (an IPRC prerequisite); re-assessment by 16 is needed for DSO/Passport (v1 §1). 120 h/yr ≈ 30 file reviews and 6–8 assessments. Keep. |

Record the with/without pair as two scenarios in `finance/assumptions.md`; do not net any OHaH value as revenue (avoided cost only, v1's own rule, VERIFIED §5).

---

## 5. Transportation: audit of the hybrid 45-minute figures

### 5.1 Reconstruction (premises note Q7 "Inferences — cost model", all ESTIMATE in v1; arithmetic VERIFIED here)

**Owned used accessible bus, per year:** driver $22/h × 4 h × 194 d = $17,072 × 1.20 = $20,486 (≈ $20,500); fuel at 25 L/100 km × $1.55/L: 40 km/day → $3,007; 70 km → $5,264; 100 km → $7,517; insurance $7,500; maintenance $7,000; inspections/licensing $1,500; depreciation $35,000 ÷ 5 = $7,000. Totals: **$46,500 (40 km, "30-min")**, $48,750 (70 km), **$51,000 (100 km, "60-min")**. Recomputed exactly.

**Contracted small accessible bus, per day:** (driver 5 h × $22 × 1.20 = $132) + (vehicle $35,000 ÷ 194 = $180.4) + fuel/licensing $40 = $352.4 × 1.25 overhead/margin = **$440.5/day**; × 194 = **$85,460 ≈ $85,400/yr**. Recomputed exactly.

**Hybrid:** 1/2/3 owned buses at $51,000 + 1 contracted bus at $85,400 = **$136,400 / $187,400 / $238,400**; per student $11,367 / $9,370 / $7,947 (report: $11,400 / $9,400 / $7,900). Recomputed exactly.

### 5.2 Assumptions embedded (ASSUMPTION unless stated)

1. Every student rides every day (100% take-up).
2. One contracted bus serves the satellite hubs at *every* enrolment level (12 → 30), while owned buses scale 1 → 3: the model assumes hub demand never exceeds one bus.
3. The hybrid uses the **60-minute** owned-bus cost ($51,000, 100 km/day) even though the hybrid is described as shortening routes to ≤ 20 km one way (premises note Q7); the internally consistent figure is the 40–70 km rate ($46,500–48,750), overstating by ≈ $2,250–4,500 per owned bus. Minor.
4. EA ride-along uncosted (see §3.3); +$10,100 per bus if paid.
5. Vehicle capital ($30–45K per used bus) is in the start-up budget, not operating; depreciation at $7,000/bus/yr is in operating. Not a double count, but the model must not also carry a replacement reserve for the same vehicle.
6. No rate card was obtained from any operator (CONFIRM: Sharp, Switzer-CARTY, Voyago).
7. Load factor: at 30 students the hybrid runs four vehicles — 7.5 students per vehicle — which is why the per-student cost is four times the public benchmark ($1,965, VERIFIED inputs). The economics only improve with concentrated pickup points or successive runs.

### 5.3 Phase 2 treatment (FOUNDER DECISION, brief §Transportation)

Comprehensive door-to-door transport is **not** an opening requirement. Transport leaves the operating base and becomes an optional module with the brief's four options to be costed in `research/transportation.md`:

| Option | Starting point from v1 inputs (ESTIMATE) |
|---|---|
| Family transport + chartered outings | $0 daily transport; chartered accessible outings for community experiences, e.g. 2 half-day charters/week × 38 weeks × ≈ $350 ≈ **$26,600** (rate ASSUMPTION; CONFIRM with a local operator) |
| Sponsored local operator serving concentrated pickup points | 1 contracted bus ≈ $85,400/yr per bus-day equivalent; sponsorship is a restricted gift offsetting this line, never counted twice (v1 §5 rule, VERIFIED) |
| One donated/sponsored bus making successive runs (two staggered start times) | 1 owned bus, 2 runs each way: driver 6 h × $22 × 194 × 1.2 = $30,700; fuel 140 km/day ≈ $10,500; insurance, maintenance, inspections $16,000; depreciation $0 if donated (but a replacement reserve ≈ $7,000) → ≈ **$57–64K/yr** for up to ≈ 2 × 18 = 36 seats |
| Second bus as later expansion | + same again |

"The McDougall Insurance bus" is an illustration, not a prospect (FOUNDER DECISION).

---

## 6. Property debt and what remains of the premises line

### 6.1 v1 premises line, reconciled (VERIFIED, premises note Q10.B and Q5)

| Component | 12 | 20 | 30 |
|---|---|---|---|
| Debt service, $712,500 at 6%/25 yr | 54,700 | 54,700 | 54,700 |
| Addition financing (30 only, "add ~$20K") | — | — | 20,000 |
| Utilities ($2.25/sf × 4,557 sf ≈ 10,300; 8,000 sf at 30) | 10,300 | 10,300 | 18,000 |
| Maintenance, custodial supplies, snow, grounds | 15,000 | 17,000 | 25,000 |
| Capital/maintenance reserve (1.5% of building value) | 15,000 | 15,000 | 20,000 |
| **Premises line, report §9** | **95,000** | **97,000** | **137,700** |

Sums exactly. **Rent is not included anywhere in the base case** — leasing appears only as a sensitivity ("Leasing 10,000 sq ft … $230K/yr vs ~$75K debt service + tax", premises note Q10.C). VERIFIED: no rent/debt double count.

Mortgage arithmetic check: $712,500 at 6% nominal, 25-year amortisation, Canadian semi-annual compounding (monthly factor (1.03)^(1/6) − 1 = 0.49386%) gives $4,558.6/month = **$54,703/yr** — v1's $4,560 / $54,700 is exact. (Monthly compounding would give $4,590.6 / $55,088; v1 used the Canadian convention.) ESTIMATE, VERIFIED formula.

### 6.2 Phase 2 basis (FOUNDER DECISION: capital donor-funded, no debt — a planning assumption, not secured funding)

Remove $54,700 (+$20,000 at 30). What remains, and how it should be sized in the 50-student model:

| Item | v1 at 30 | Phase 2 guidance |
|---|---|---|
| Utilities | 18,000 ($2.25/sf) | Keep the $/sf method; the sf comes from `research/premises.md` (a surplus-school wing or a 12,000–15,000 sf building at 250–300 sf/student is a very different number: 15,000 sf × $2.25 = $33,750) |
| Maintenance, grounds, snow | 25,000 | Keep; re-base per sf ($1.50–2.50/sf, v1 Q5 PROPOSAL) |
| Insurance (property, CGL with abuse extension, D&O, auto) | 22,000 (separate line) | Keep; CONFIRM with a broker; drop owned-auto if no owned vehicle |
| Replacement reserve | 20,000 (1.5% of a $950K *purchase price*) | Re-base on **insured replacement cost**, not purchase price: a donated building is still consumed. PROPOSAL: 1.5–2% of replacement cost, or a component schedule (roof, HVAC, elevator, kitchen) |
| Property tax | 0–18,000 | Owned by a charity "seminary of learning" exemption is the stronger case (v1 §4, SECONDARY); CONFIRM MPAC (OQ-5) |
| Debt service | 74,700 | **0** |

Capital-campaign fundraising costs and the acquisition itself belong in a separate capital schedule, never in operating, and a naming sponsorship for the building is counted once (brief §Capital).

---

## 7. Fundraising expenses: the double count and a single treatment

### 7.1 What v1 does (VERIFIED)

1. People line: "development staff" $20,000 / $40,000 / $80,000 (0.25 / 0.5 / 1.0 FTE), premises note Q6.
2. Supplies/admin line: "Fundraising program costs (events, materials; excl. staff)" $15,000 / $25,000 / $35,000, premises note Q10.B.
3. Start-up: "Fundraising set-up (CRM, website, case for support, launch)" $15–30K, Q10.A — legitimately one-off.
4. Sensitivity (v1 §5 and §9): "If fundraising actually costs 20–25 percent of what it raises … the gross amount that must be raised rises … by a further ~$200–280K at 12 students, ~$265–375K at 20 and ~$325–475K at 30."

Items 1 + 2 total $35K / $65K / $115K. At 30 students, against a net need of ≈ $1.86–1.91M, that is an implied cost-of-raising of 115 ÷ (1,860 + 115) ≈ **5.8%** — yet the sensitivity applies 20–25% to the *whole* gross. The base budget therefore assumes a 6% fundraising cost while the text argues 20–25% is "realistic". Check of the sensitivity: at 12 students, N ≈ $0.96–0.99M; G = N ÷ (1 − 0.20) = $1.20–1.24M (+$240–248K), less the $35K already budgeted ≈ +$205–213K; at 25%: G = $1.28–1.32M (+$320–330K) less $35K ≈ +$285–295K. The v1 "$200–280K" is consistent with netting the $35K at the low end, so the arithmetic is *not* a strict double count — but the presentation is: the headline tables carry 6% while the narrative treats 20–25% as the expected case, and a reader adding the sensitivity to the table without the netting would double count $35–115K. ESTIMATE.

### 7.2 Single consistent treatment (PROPOSAL)

Define, for any scenario:

- **C** = operating cost *excluding* all fundraising cost (no development staff, no program costs).
- **O** = non-philanthropic offsets (purchased services, CSJ, City grants) — cash only; OHaH, SNP and donated services are avoided costs already netted out of C.
- **N = C − O** = net philanthropic need.
- **c** = cost-of-raising ratio (fundraising cost ÷ gross raised).
- **G = N ÷ (1 − c)** = gross philanthropic raise required.
- **F = G − N = c × G** = the fundraising budget, which *is* the development staff plus program costs (one line, in the operating budget, so the T3010 ratio can be computed).

Choose c from the planned *mix*, not from one comparator. Greenfield's reasonable-cost guidelines (SECONDARY, [OneOC/Greenfield summary](https://oneoc.org/wp-content/uploads/2019/10/fundraising-reasonable-costs-jim-greenfield.pdf), accessed 2026-10-15): direct-mail acquisition $1.25–1.50 per $1; direct-mail renewal $0.20–0.25; special events $0.50 (direct costs only); corporations and foundations $0.20; capital campaigns $0.10–0.20; planned giving $0.20–0.30; major gifts are commonly cited at $0.05–0.15 (SECONDARY, sector lore; CONFIRM against the AFP Fundraising Effectiveness Project). Hospice Quinte's 24.5% ($216,277 ÷ $882K, VERIFIED v1 §5) reflects an events-heavy mature mix. A school whose plan is anchored by a few multi-year major and foundation gifts (brief §Funding) should model **c = 12% base, 20% stress, 25% for an events-led mix**, and must keep the ratio inside CRA's 35% comfort line (CG-013, VERIFIED v1 §5).

Applied to the Phase 2 30-student baseline (§10): C = $1,523,340 (no OHaH) and O = $85,000 (mid-point of v1's $60–110K, ESTIMATE) give N = $1,438,340 and:

| c | G (gross raise) | F (fundraising budget) |
|---|---|---|
| 7.4% (v1's implied) | 1,553,283 | 114,943 |
| 12% (proposed base) | 1,634,477 | 196,137 |
| 20% (stress) | 1,797,925 | 359,585 |
| 25% (events-led) | 1,917,787 | 479,447 |

At c = 12%, F ≈ $196K buys a 1.0 FTE development lead ($80K loaded, v1 rate), ≈ $35K program/events, CRM and materials, and part-time grant-writing — a plausible staffing of the ratio. Capital-campaign costs are charged to the capital schedule at $0.10–0.20 per dollar and never to F.

---

## 8. Reserves

### 8.1 What v1 proposed (VERIFIED, v1 §9 and funding note KQ7)

An 18–24-month operating reserve "in cash or irrevocable pledges" plus signed pledges covering 60–70% of Year-1 cash need, before any lease or hire. v1 itself labels 18–24 months "the researcher's proposal, not a published standard" (funding note KQ7) and cites "3–6 months as a *minimum* reserve for established charities". At the v1 cost base this gate was $1.5–2.0M (12 students) to $2.2–2.9M (20); at the v1 30-student cost it would be ≈ $3.0–3.9M — in addition to $2.1–2.8M of start-up (which, per §3.4, already holds three months' working capital).

### 8.2 Assessment

- Sector guidance: the US Nonprofit Operating Reserves Initiative's commonly cited floor is 25% of annual operating expenses (three months), with 3–6 months typical and larger reserves expected to be justified (SECONDARY; no primary document read today). CRA CG-013 Appendix C expects a charity to be able to justify its reserve level against a written policy (VERIFIED v1 funding note KQ7). A reserve above what the policy justifies invites the question why donated funds are not being spent on charitable activities; a large cash reserve may also count as property not used directly in charitable activities for disbursement-quota purposes (CONFIRM with charity counsel — not asserted here).
- The ethical argument v1 makes is sound — a school must not close mid-year on students who cannot easily be moved — but a static 18–24 months is the wrong instrument for it. The duty is to *finish the year and transition students*, which is a rolling test, not a fixed multiple of annual cost. 18–24 months of a $1.5–2.0M budget is itself a reason the school never opens.

### 8.3 Tiered reserve (PROPOSAL, for `docs/open-questions.md` and a founder decision)

| Tier | Form | Size (30-student Phase 2 baseline ≈ $1.52M/yr) | Purpose |
|---|---|---|---|
| 1. Operating reserve | Unrestricted cash, board-designated | **6 months of operating cost ≈ $760K** | Timing of pledge receipts, grant holdbacks, an anchor donor's late payment |
| 2. Continuity backstop | Irrevocable multi-year pledge agreements or a written donor standby commitment (not cash) covering a further 12 months | **≈ $1.5M in signed instruments** | Replaces v1's second 12–18 months of cash with enforceable promises; released or renewed annually |
| 3. Wind-down / transition reserve | Restricted cash | **≈ one term (4 months) ≈ $500K plus ESA termination/severance for ≈ 15 staff ≈ $150K** | Guarantees an orderly finish of the school year and transition of every student if Tiers 1–2 fail; this is the ethical duty made explicit |
| Rolling test | Policy rule | At every board meeting: cash + confirmed receivables ≥ cost to the end of the current school year + Tier 3 | The operative go/no-go, replacing a one-time 18–24-month gate |

Tier 1 plus Tier 3 ≈ $1.4M of cash at 30 students — close to v1's 12-student gate but covering a 30-student school — with Tier 2 carried as instruments rather than cash. At 50 students the amounts scale with the model's cost base. The three-month working capital in start-up is the first half of Tier 1, not an addition to it.

---

## 9. Unsupported assumptions and absolute claims

| # | Claim (v1 location) | Status | What would settle it |
|---|---|---|---|
| 1 | "not financially feasible on the base case … unless a transformational funder is in hand" (bottom line; §9 verdict) | **Partially supported.** The cost side is a high-intensity design (1:2.5, door-to-door transport, debt, 12-month cook/custodian); the revenue side infers a ceiling from four T3010s. On the Phase 2 basis the 30-student need falls from ≈ $1.97M to ≈ $1.43–1.52M (§10) before any volunteer substitution. | A corrected cost base (this audit + the 50-student model) and a prospect register with capacity ratings (`funding/prospect-register.md`); a campaign feasibility study once the founder authorises outreach |
| 2 | "exceeds what any Belleville-area charity raises from the community (Hospice Quinte … ~$0.88M)" and "equals roughly 43 percent of the entire United Way … campaign" used as a ceiling (bottom line; §5) | **Unsupported as a ceiling.** Both are real data points (VERIFIED) but neither measures community capacity: UWHPE is one federated workplace campaign among many vehicles, and Hospice Quinte's *operating* giving excludes its capital campaign. Larger local vehicles (Belleville General Hospital Foundation, Quinte Humane Society's shelter campaign, Loyalist College foundation, Three Oaks) were "not researched — search budget exhausted" (v1 item 25, VERIFIED). The brief rejects inferring a ceiling from a few charities (FOUNDER DECISION). | T3010s for BGHF, QHS, Loyalist Foundation, Three Oaks, Community Visions; StatCan T1 charitable-donations data for the Belleville CA (total receipted donations claimed by residents); results of the prospect register |
| 3 | "confirmed non-philanthropic sources can cover at most 3–5 percent" (bottom line) | **Partially supported** for cash; understated as a share once OHaH-delivered therapy, SNP food and donated services are treated as avoided cost (§4). | OQ-3 (OHaH scope); HPELF decision on an SNP site; partner agreements |
| 4 | "no Ontario or federal operating stream for private schools" (bottom line) | **Supported** (VERIFIED, Ontario.ca). | — |
| 5 | "No source offers a brand-new charity … an interest-free institutional loan" → heading "no interest-free institution exists" (§7) | **Unsupported as an absolute**; supported as "none found in a truncated search" (v1 states the search budget was exhausted). Religious-order and foundation program-related investments, credit-union community loans and Infrastructure Ontario's eligible-borrower list were not examined. Largely moot under the no-debt planning assumption, but the brief says keep exploring. | A targeted review in `funding/` of PRI lenders (foundations), religious-community loan funds and IO eligibility; the question of whether forgiven donor loans are receiptable (CONFIRM CRA/counsel) |
| 6 | "Opening earlier than 2028 is not credible" (bottom line; §9 milestones) | **Partially supported.** CRA registration (6–12 months) is not a legal precondition to operate or to receive donations through an existing charity acting as agent; the binding constraints are a building, five compulsory-age pupils and a principal by September. Sept 2028 is the adopted target (FOUNDER DECISION, decision log 2026-10-14), so the claim is not operative, but it should be recorded as a judgment, not a fact. | A premises decision date from `research/premises.md`; whether a qualified donee will host the project pre-registration (CONFIRM with counsel) |
| 7 | Family propensity "15–30 percent would seriously consider; 5–12 percent would enrol at opening" (§2) | **Unsupported** — v1 says so ("no desk source pins down"). It drives the entire demand funnel. | The anonymous intermediary-distributed survey and EOI list v1 proposes (PROPOSAL; requires founder authorisation for outreach) |
| 8 | "$1.0 million a year at 12 students, $1.4 million at 20 and $2.0 million at 30" presented as point estimates (bottom line) | **Partially supported.** The arithmetic is exact (§1, §6) but the inputs carry unstated ranges: renovation $75–150/sf, insurance "unsourced", transport "no rate card", benefits 8% "no survey", therapy hours chosen. A ±15% band is the honest presentation. | Quotes listed in v1 items 17–19; the Phase 2 model should publish low/base/high |
| 9 | "four bands" at 30 students, 1 teacher + 2 EAs each (§1, §9) | **PROPOSAL presented as cost fact.** Comparators support 6–12 per class with 1–2.4 EAs by profile (§3). | `research/educational-design.md` grouping design against the admitted profile |
| 10 | "250–300 sq ft/student" so Property A "fits 8–16" and 30 needs an addition (§4) | **Unsupported** (v1: "researcher's assumption"); HPEDSB elementary average is 85–130 sf gross per pupil (VERIFIED). A special-purpose school needs more, but 250–300 is unanchored and sets the premises size for 50 students (12,500–15,000 sf). | An architect's programme of spaces; comparator floor areas (Summit, Oak Bridge) |
| 11 | "The surplus schools are a mirage on this timeline"; "None of the three fits a 12–30-student school" (§4) | **Partially supported** on timeline (VERIFIED precedents of 2.5–6 years) ; the "fit" claim is moot for a 50-student school with partial occupancy, which the brief directs to be tested (FOUNDER DECISION). | `research/premises.md` (OQ-2) |
| 12 | "a mature local program … itself takes three to five years to build" (§9 verdict) | **Unsupported** generalisation; plausible sector lore. | Prospect register progress; comparable start-up charities' first-three-year T3010s |
| 13 | "Staffing is 55–65% of operating cost" (premises note Q10) | **Arithmetic error, minor:** 631.4/1,009.9 = 62.5%; 945.3/1,437.0 = 65.8%; 1,314.4/1,971.9 = 66.7% → 62–67%. | — |
| 14 | "fixed core ≈ $230K at 12 students … every student below plan adds ~$1,600" (§9) | **Supported as arithmetic** (principal + admin + cook + custodian + premises + insurance = $245,700; ÷12 = $20.5K; ÷11 = $22.3K → +$1.9K). Slightly understated. | — |
| 15 | "Fully endowing the school would take roughly $25M at 12 students … 'endow a seat' needs ~$2.1M" (§5) | **Supported arithmetic at a 4% draw on the v1 cost**; on the Phase 2 30-student base ($1.52M, $50.8K/seat) the figures are ≈ $38M and ≈ $1.27M per seat; at 50 students lower again. | The 50-student model |
| 16 | "18–24-month operating reserve" as a condition of viability (§9) | **PROPOSAL** (v1 labels it so) elevated to a condition in the headline. See §8. | Founder decision on a reserve policy |
| 17 | "Transportation is a school operating cost line, not a public service the school can assume" (§3) | **Supported** (Tri-Board policy, VERIFIED). | — |
| 18 | "JK–12 private schools … are not eligible partners" for space in operating schools (§4) | **Supported** (Guideline text quoted, VERIFIED). | — |
| 19 | "Ontario comparators without public funding plateau at 10–100 students after 10–20 years" (§8) | **Partially supported** (OurKids-listed sizes, school-reported); survivorship and selection not addressed. | — |
| 20 | "the model works if, and only if, the money is anchored by one or two very large recurring commitments" (bottom line) | **Unsupported "only if".** It follows from claims 1–2; on a corrected cost base and an investigated (not inferred) donor market, a broader base of mid-level multi-year commitments plus one anchor is an alternative structure that v1 did not model. | Prospect register tiers; the fundraising mix in §7 |

Unsupported *optimism* to challenge equally: (a) a $70K flat teacher salary with no pension retaining qualified special-education teachers (§2.2); (b) 4% relief (§3.3); (c) 8% benefits with no quote; (d) "contracted clinicians at 1.8× employee hourly" — private-practice SLP/psychology rates in eastern Ontario may exceed $120/$210 (CONFIRM); (e) utilities at $2.25/sf for a 1950s–90s church (ESTIMATE from 2015-16 school data +40%); (f) $0 property tax; (g) OHaH delivering school-based therapy at the hours assumed, which the brief warns is an eligibility-versus-delivery question.

---

## 10. Corrected 30-student baseline on the Phase 2 basis, and inputs the 50-student model needs

### 10.1 Baseline table (2026 prices; ESTIMATE throughout, built only from v1 inputs with the four Phase 2 corrections applied)

| Line | v1 (report §9) | Phase 2 baseline, therapy without OHaH | Phase 2 baseline, therapy with OHaH | Change and label |
|---|---|---|---|---|
| Teachers 4 × 82,600 | 330,400 | 330,400 | 330,400 | unchanged (ratio PROPOSAL to be re-set at 50 students) |
| EAs 8 × 45,400 | 363,200 | 363,200 | 363,200 | unchanged |
| Principal 1.0 | 118,000 | 118,000 | 118,000 | unchanged (ED decision pending, §3.3) |
| Admin 1.0 | 58,500 | 58,500 | 58,500 | unchanged |
| Cook 1.0 | 51,800 | 51,800 | 51,800 | unchanged (over-count flagged §3.4) |
| Custodian 1.0 | 54,800 | 54,800 | 54,800 | unchanged (over-count flagged §3.4) |
| Contracted SLP / OT / BCBA / psychologist | 230,000 | 230,000 | 143,600 | with-OHaH: OT dropped, SLP halved (§4.3) |
| Relief 4% | 27,700 | 27,700 | 27,700 | unchanged (thin; §3.3) |
| Development staff | 80,000 | **0** | **0** | moved to fundraising treatment (§7) |
| **People** | **1,314,400** | **1,234,400** | **1,148,000** | |
| Debt service (incl. addition) | 74,700 | **0** | **0** | FOUNDER DECISION (no-debt planning assumption) |
| Utilities | 18,000 | 18,000 | 18,000 | re-base on actual sf |
| Maintenance, grounds, snow | 25,000 | 25,000 | 25,000 | |
| Replacement reserve | 20,000 | 20,000 | 20,000 | re-base on replacement cost (§6.2) |
| Property tax | 0 (–18,000) | 0 (–18,000) | 0 (–18,000) | CONFIRM MPAC |
| Insurance | 22,000 | 22,000 | 22,000 | CONFIRM broker |
| Transportation | 238,400 | **0** (module) | **0** (module) | FOUNDER DECISION; module options §5.3 |
| Meals and kitchen consumables | 41,400 | 41,400 | 41,400 | SNP eligibility may reduce (CONFIRM HPELF) |
| Supplies, AT upkeep, PD, admin/audit | 90,000 | 90,000 | 90,000 | |
| Fundraising program costs | 35,000 | **0** | **0** | moved to fundraising treatment (§7) |
| Student enterprise (net) | 0 | 0 | 0 | |
| **Subtotal before contingency** | 1,878,900 | **1,450,800** | **1,364,400** | |
| Contingency 5% | 93,000 | 72,540 | 68,220 | |
| **Operating cost C** | **1,971,900** | **1,523,340** | **1,432,620** | −$448,560 / −$539,280 |
| Per student | 65,730 | **50,778** | **47,754** | |
| Non-philanthropic offsets O (v1 $60–110K, mid) | | 85,000 | 85,000 | ESTIMATE |
| Net need N = C − O | | 1,438,340 | 1,347,620 | |
| Gross raise G at c = 12% | | **1,634,477** | **1,531,386** | fundraising budget F = 196,137 / 183,766 |
| Gross raise G at c = 20% (stress) | | 1,797,925 | 1,684,525 | F = 359,585 / 336,905 |
| Transport module, if adopted (one sponsored bus, two runs) | | + ≈ 57–64K | + ≈ 57–64K | §5.3; sponsorship offsets this line only |

Check of the reduction from v1: 74,700 (debt) + 238,400 (transport) + 80,000 (development staff) + 35,000 (fundraising program) + 20,460 (contingency on the removed amounts) = **448,560**. Exact.

Adjustments **not** applied above, for the model builder to decide and document in `finance/assumptions.md`: public-holiday pay +$10,900 (statutory); relief to 6% +$13,900; prep-time cover +$16,500; volunteer coordinator +$30–60K; executive director +$100–120K or a split role; custodian to 0.5 FTE −$27,400; cook to 0.7 FTE −$15,500; pension 3–5% of payroll +$30–50K; salary distribution for teachers (lead teacher premium). Net of these the 30-student baseline moves by roughly +$150–230K (ESTIMATE), i.e. to ≈ $1.6–1.75M without OHaH — still ≈ $220–370K below v1 because debt and door-to-door transport are gone.

### 10.2 Indicative check only — 50 students (PROPOSAL; not a model)

Using the §3.2 grouping (6 teachers, 9 EAs): teachers + EAs = $904,200; relief 4% = $36,200; principal + ED ≈ $230K; admin 1.0 $58,500; cook 1.0 $51,800; custodian 1.0 $54,800; therapy at the §4.3 with-OHaH level scaled to intake rather than enrolment ≈ $180–220K; volunteer coordinator ≈ $45K → people ≈ $1.56–1.60M; premises on 14,000 sf ≈ $85–100K; insurance ≈ $28K; meals ≈ $69K; supplies/admin ≈ $130K; contingency 5% → **≈ $1.95–2.05M, ≈ $39–41K per student** before volunteer substitution. This is the order of magnitude the 50-student model should land near if its inputs resemble v1's; a material departure needs an explanation in `finance/assumptions.md`.

### 10.3 Inputs the 50-student model must obtain from the Phase 2 topic files

| From | Inputs required |
|---|---|
| `research/educational-design.md` | Number and size of instructional groups by profile; EAs per group by profile; instructional minutes per cohort under staggered schedules; subjects regrouped and the adult count needed in literacy/numeracy blocks; age bands; the admitted-profile boundary (what 1:1 or nursing would add) |
| `research/staffing-volunteers.md` | Paid FTE by role (teachers, EAs, principal, ED, admin, cook, custodian, coordinator) with base pay, pension decision and benefits rate; relief % and paid sick days; which paid hours volunteers replace versus enhance (hours/week, by activity, with a reliability discount); coordinator FTE; screening, training and supervision costs; shared payroll/bookkeeping/facilities options and their cost |
| `research/transportation.md` | Module chosen for the base case; number of vehicles and runs; driver employed or contracted; daily km; sponsorship (restricted gift) treatment; charter allowance for outings; EA ride-along hours |
| `research/public-services-partners.md` | OHaH: eligibility confirmation, services, assessed hours per referred student and local delivery capacity; insured-services share and the uninsured-family provision; SNP site eligibility and value; partner payer/recipient/eligible activities for developmental-service and health organisations |
| `research/premises.md` | Building and site chosen (surplus school wing, church, other); gross sf; utilities $/sf with the building's own data; maintenance $/sf; insurance quote; property-tax status; replacement-cost basis for the reserve; whether partial-occupancy costs can truly be separated; capital schedule (acquisition, renovation, equipment) and the donated-capital assumption as a separate schedule |
| `funding/prospect-register.md` | Committed / plausible / speculative tiers; non-philanthropic offsets O; the fundraising mix that sets c |

---

## Summary of findings

1. The $620,800 gap in the 30-student people line is fully explained by ten lines in the premises note (principal $118,000; admin $58,500; cook $51,800; custodian $54,800; SLP $76,800; OT $48,000; BCBA $80,000; psychologist $25,200; relief $27,700; development $80,000) and the 12- and 20-student columns reconcile to the dollar.
2. The loaded factors (1.18 teacher, 1.20 EA) are arithmetically correct on the 2026 statutory rates; public-holiday pay for hourly staff (~$1,365 per EA) is the one statutory omission; no pension is carried.
3. The $55K-per-teacher gap to HPEDSB is pay-grid position (~$25–30K), OTPP (~$10–12K), richer benefits, and the supply/prep/allowance costs inside a board's "classroom teacher" line.
4. Two EAs per class is a planning assumption drawn from DD-class comparators, not a statute; a 50-student school can run 6–12 per group with 1–2 EAs by profile (6 teachers, 9 EAs) at a 1:3.3 overall ratio.
5. v1 omits relief beyond 4%, prep cover, volunteer coordination, an executive director and holiday pay, and over-counts a 12-month cook and custodian and three months of working capital inside both start-up and the reserve gate.
6. Therapy ($115K at 12, $230K at 30) overlaps OHaH only for SLP/OT; with OHaH delivering, the 30-student line falls to ≈ $143,600.
7. The hybrid transport figures reconstruct exactly; the Phase 2 base case removes them and costs transport as a module ($0 to ≈ $64K for one sponsored bus with two runs).
8. Debt service ($54,700 + $20,000) is removed; rent was never in the base case; utilities, maintenance, insurance and a replacement reserve re-based on replacement cost remain.
9. Fundraising was carried at an implied 6–7% in the tables and 20–25% in the narrative; the single treatment is G = N ÷ (1 − c) with c = 12% base, 20% stress, and F = c × G as the one fundraising line.
10. On the Phase 2 basis the 30-student operating cost is ≈ $1.52M (≈ $1.43M with OHaH), ≈ $50.8K per student, versus v1's $1.97M; the 18–24-month reserve should become a tiered policy (6 months cash + 12-month pledged backstop + a one-term wind-down reserve with a rolling finish-the-year test).
