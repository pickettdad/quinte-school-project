"""Quinte school operating model — Phase 2 (2026 prices; ×1.0609 for 2028).
Run: python3 finance/model.py > finance/outputs.md
Every input is in finance/assumptions.md with its source. Capital is donor-funded (no debt) per founder decision 2026-10-15.
"""
S = {  # scenario: students -> inputs (CAD, 2026)
  30: dict(people=1_405_600, m2=1_000),
  50: dict(people=1_969_900, m2=1_400),
  75: dict(people=2_734_900, m2=2_000),
}
# premises per m2 (research/premises.md §9): utilities 33, maintenance 25; insurance ~$18/m2 equiv; reserve 1.5% of replacement value ($3,500/m2)
UTIL, MAINT, INS, REPL_VAL, RESERVE = 33, 25, 18, 3_500, 0.015
TRANSPORT = {30: 95_000, 50: 95_000, 75: 170_000}      # research/transportation.md: one sponsored bus (two runs); second bus at 75
OUTINGS = {30: 15_000, 50: 22_000, 75: 30_000}
MEAL_DAY, DAYS = 6.25, 194                             # v1 premises note §8 (no Ontario benchmark; CONFIRM)
SUPPLIES_PER_STUDENT, ADMIN_FIXED = 1_800, 60_000      # supplies/AT/PD/checks; audit/insurance/IT/legal
FUNDRAISING_PROGRAM = {30: 30_000, 50: 40_000, 75: 50_000}  # dev lead salary already in people
CONTINGENCY = 0.05
# Offsets (research/public-services-partners.md consolidated table; staffing-volunteers.md §9) — conservative / moderate
INKIND = {30: (45_000, 110_000), 50: (70_000, 165_000), 75: (90_000, 220_000)}       # OHaH avoided cost + volunteer-replaced hours + donated food
RESTRICTED = {30: (35_000, 95_000), 50: (55_000, 155_000), 75: (75_000, 210_000)}   # Passport, OAP, SSAH, SNP — netted only against the programs they fund
UNRESTRICTED = {30: (0, 15_000), 50: (0, 20_000), 75: (0, 25_000)}                   # CSJ, City (non-recurring), enterprise; nothing committed

print("# Model outputs (generated — do not edit)\n")
print("All figures CAD, 2026 prices. Capital excluded (donor-funded assumption). Conservative / moderate offsets.\n")
print("| Line | 30 students | 50 students (base) | 75 students |\n|---|---:|---:|---:|")
rows = {}
for n, i in S.items():
    prem = i["m2"] * (UTIL + MAINT + INS) + i["m2"] * REPL_VAL * RESERVE
    meals = n * MEAL_DAY * DAYS * 1.12
    supplies = n * SUPPLIES_PER_STUDENT + ADMIN_FIXED
    sub = i["people"] + prem + TRANSPORT[n] + OUTINGS[n] + meals + supplies + FUNDRAISING_PROGRAM[n]
    gross = sub * (1 + CONTINGENCY)
    cash_c, cash_m = gross - INKIND[n][0], gross - INKIND[n][1]
    need_c = cash_c - RESTRICTED[n][0] - UNRESTRICTED[n][0]
    need_m = cash_m - RESTRICTED[n][1] - UNRESTRICTED[n][1]
    rows[n] = dict(people=i["people"], prem=prem, trans=TRANSPORT[n] + OUTINGS[n], meals=meals, supp=supplies,
                   fr=FUNDRAISING_PROGRAM[n], cont=gross - sub, gross=gross, cash_c=cash_c, cash_m=cash_m,
                   need_c=need_c, need_m=need_m, per=gross / n, reserve6=gross / 2)
L = [("People (staffing-volunteers.md §9)", "people"), ("Premises: utilities, maintenance, insurance, replacement reserve", "prem"),
     ("Transportation incl. outings", "trans"), ("Meals and kitchen consumables", "meals"), ("Supplies, AT, PD, checks, audit, admin", "supp"),
     ("Fundraising program (excl. salary)", "fr"), ("Contingency 5%", "cont"), ("**Gross annual cost**", "gross"), ("Per student", "per"),
     ("Cash cost after in-kind (conservative)", "cash_c"), ("Cash cost after in-kind (moderate)", "cash_m"),
     ("**Remaining fundraising requirement (conservative)**", "need_c"), ("**Remaining fundraising requirement (moderate)**", "need_m"),
     ("Six-month operating reserve (cash)", "reserve6")]
for label, k in L:
    print(f"| {label} | " + " | ".join(f"{rows[n][k]:,.0f}" for n in S) + " |")
print("\nGross raise if fundraising cost ratio is 12% on top of the lines above: need ÷ 0.88. "
      "Restricted funding is shown net of nothing — it may only pay for the specific services it funds (see public-services-partners.md).")
