# Gap verification: funding and philanthropy questions (Quinte IDD school)

Status note (2026-10-14): This run was cut short by a session limit after ~35 tool calls. The web-search budget was already exhausted when the run began, so everything below came from direct fetches of known URLs. Item 1 is substantially resolved via the CRA open-data CKAN API (a working alternative to the JavaScript-only CRA charity listings). Items 2–7 were attempted but every target host either blocked the fetcher (robots.txt), returned fetch errors, or the session limit hit before a response arrived. Each item states exactly what was tried so the next researcher does not repeat it.

Method that works for T3010 data (reusable): `https://open.canada.ca/data/api/3/action/datastore_search?resource_id=0b9b4b01-5cb6-4981-b007-ae88f48cc799&q=<BN>` returns the full Schedule 6 / Section D row for any charity in the CRA "2023 List of charities" dataset (dataset id 05b3abd0-e70f-4b3b-a9c5-acc436bd15b6, resource "financial_d_and_schedule_6_2023_updated.csv"). It is rate-limited (HTTP 429 after ~5 calls in quick succession); space the calls out. Direct CSV download via curl is blocked by the egress proxy (open.canada.ca and opencanada.blob.core.windows.net both 403 on CONNECT), and the resulting signed blob URL is too long for WebFetch. The 2024 dataset was not located (a CKAN search for "List of charities 2023" returned only the 2023 dataset; a sorted search for newer years was refused by robots).

## 1. T3010 financial snapshots (Belleville comparables and model schools)

### Takeaway
Four of the five requested Belleville charities were retrieved from CRA's 2023 open-data T3010 file (fiscal periods ending 2023). The pattern is stark: the developmental-services agency (Community Living Belleville) is 97% provincial funding with negligible donations; the hospice is ~63% government / ~38% donations and fundraising; the two Christian school charities run on receipted gifts (which, for religious schools, include the CRA-permitted receipted portion of tuition) plus fees, with essentially zero government revenue. No Belleville charity in this set raises more than roughly $0.9M a year in donations plus fundraising from the community.

### Cited Findings
Line-code key used (CRA Form T3010 Schedule 6): 4500 tax-receipted gifts; 4510 gifts from other registered charities; 4530 other non-receipted gifts; 4540/4550/4560 federal/provincial/municipal revenue; 4575 revenue from outside Canada; 4580 interest/investment; 4600 net proceeds of asset dispositions; 4610 rental; 4620 memberships; 4630 non-receipted fundraising revenue; 4640 sale of goods and services (tuition/fees); 4650 other revenue (4655 specifies); 4700 total revenue; 4880 total compensation; 4950 total expenditures before gifts to qualified donees; 5000 charitable programs; 5010 management and administration; 5020 fundraising; 5050 gifts to qualified donees; 5100 total expenditures; 4155 land and buildings; 4200 total assets; 4310 deferred revenue; 4350 total liabilities. Line sums were checked against 4700 for each record and reconcile exactly.

- VERIFIED — **Community Living Belleville and Area (815280201RR0001), FPE 2023-03-31**: total revenue $16,573,394; tax-receipted gifts $10,986 (0.07%); gifts from other charities $34,000; federal $116,106; provincial $15,972,906 (government combined $16,089,012 = 97.1%); sale of goods/services $196,723; interest $60,810; rental $69,144; other $112,719. Total expenditures $16,580,555: charitable $14,547,249, management/admin $1,861,517, fundraising not reported (nil), total compensation $12,511,955 (75% of spend). Land and buildings $7,868,365; total assets $7,480,929; total liabilities $4,568,024. — [CRA open data, datastore_search BN 815280201RR0001](https://open.canada.ca/data/api/3/action/datastore_search?resource_id=0b9b4b01-5cb6-4981-b007-ae88f48cc799&q=815280201RR0001) (fetched 2026-10-14; dataset "2023 List of charities").
- VERIFIED — **Hospice Quinte (119114452RR0001), FPE 2023-03-31**: total revenue $2,347,048; tax-receipted gifts $742,246 (31.6%); from other charities $22,898; non-receipted gifts $35,117; non-receipted fundraising $82,106 (all donations/fundraising combined $882,367 = 37.6%); federal $52,805; provincial $1,193,471; municipal $230,000 (government combined $1,476,276 = 62.9%); interest $22,862; net asset-disposition proceeds $9,304; rental $320; other -$44,081 (unrealized investment loss). Total expenditures $2,232,992: charitable $1,613,466, management/admin $403,249, fundraising $216,277 (9.7% of spend; about 25 cents per dollar of donations and fundraising revenue), compensation $1,398,764. Land/buildings $6,642,737; total assets $8,717,444; liabilities $7,199,434 (of which deferred revenue $7,052,258 — consistent with a capital campaign/building funded by deferred contributions). — [CRA open data, BN 119114452RR0001](https://open.canada.ca/data/api/3/action/datastore_search?resource_id=0b9b4b01-5cb6-4981-b007-ae88f48cc799&q=119114452RR0001) (fetched 2026-10-14).
- VERIFIED — **Quinte Region Christian Schools (119108033RR0001), FPE 2023-07-31**: total revenue $2,619,221; tax-receipted gifts $1,248,721 (47.7%; a sub-line 5610 of $657,254 is reported only by the two school charities and is probably the receipted portion of tuition — interpretation unverified); from other charities $190,646 (7.3%); non-receipted gifts $3,339; provincial $890 (government 0.03%); revenue from outside Canada $74,500 (likely international students); interest $5,600; rental $29,702; non-receipted fundraising $60,404; sale of goods/services (tuition/fees) $938,286 (35.8%); other $67,133. Total expenditures $2,586,784: charitable $2,390,042, management/admin $173,963, fundraising $21,729, gifts to qualified donees $1,050, compensation $1,396,740 (54%), occupancy $146,429, travel/vehicle $369,675 (busing), scholarships $8,000. Land/buildings $5,024,210; total assets $4,129,280; liabilities $2,202,920 (deferred revenue $1,732,549). — [CRA open data, BN 119108033RR0001](https://open.canada.ca/data/api/3/action/datastore_search?resource_id=0b9b4b01-5cb6-4981-b007-ae88f48cc799&q=119108033RR0001) (fetched 2026-10-14). Caution: the busing cost and scholarship line suggest this charity may operate Quinte Christian High School rather than Belleville Christian School; the CRA name is as shown, and which campus each BN runs was not verified.
- VERIFIED — **Belleville District Christian School Society (106782972RR0001), FPE 2023-07-31**: total revenue reported $1,720,906, but this is after a -$2,743,598 "DEFERRED CONTRIBUTIONS" adjustment on line 4650; gross receipts before that adjustment were about $4,464,504, comprising tax-receipted gifts $3,086,318 (69% of gross; again includes receipted tuition portion), from other charities $63,378, non-receipted gifts $8,106, provincial $4,659 (government 0.1%), rental $460, non-receipted fundraising $14,916, sale of goods/services (fees) $1,286,667 (29% of gross). Total expenditures $1,901,249: charitable $1,765,331, management/admin $121,193, fundraising $4,731, gifts to qualified donees $9,994, compensation $1,329,425 (70%), occupancy $163,581, travel/vehicle $175,071. Land/buildings $5,519,798; total assets $5,661,994; liabilities $4,427,724 (deferred revenue $3,872,236; other liabilities $540,000). — [CRA open data, BN 106782972RR0001](https://open.canada.ca/data/api/3/action/datastore_search?resource_id=0b9b4b01-5cb6-4981-b007-ae88f48cc799&q=106782972RR0001) (fetched 2026-10-14). The large deferred-contribution swing suggests a building campaign in FY2023; treat the single year with care.
- SECONDARY — Community Living Belleville's website lists annual reports for 2020-21, 2022-23, 2023-24, 2024-25 and 2025-26 but the fetched page exposed no PDF links or figures. — [communitylivingbelleville.org/resources/annual-reports/](https://communitylivingbelleville.org/resources/annual-reports/) (fetched 2026-10-14).
- SECONDARY — CanadaHelps profile for Community Living Belleville and Area shows no financial data, only the BN and description. — [CanadaHelps](https://www.canadahelps.org/en/charities/community-living-belleville-and-area/) (fetched 2026-10-14).

### Inferences
- A Belleville-area charity of $1–2.5M in total revenue with a meaningful philanthropic base (Hospice Quinte) raises roughly $0.75M receipted plus ~$0.1M event/fundraising revenue a year, and spends about $0.2M to do so. That is the best local benchmark for what a new, free-to-families school could plausibly sustain from community giving once mature — and Hospice Quinte had a decades-long presence and a capital campaign behind those numbers.
- The two Christian school charities show that Belleville families already sustain two independent schools of roughly $2–2.6M in annual spend with near-zero government money, but their "donations" are dominated by receipted tuition under CRA's religious-school rules, a mechanism not available to a secular free school.
- Community Living Belleville's 97% provincial funding illustrates the scale of MCCSS developmental-services funding in the area but also that it does not spill into donations; the agency reports no fundraising expense at all.

### Gaps
- UNRESOLVED — **Community Visions (107980336RR0001)**: the datastore query was refused with HTTP 429 (rate limit) on the fifth consecutive call; not retried. Use the same URL pattern with that BN after a pause.
- UNRESOLVED — Three Oaks Foundation, Quinte Humane Society, Belleville General Hospital Foundation, United Way Hastings & Prince Edward, Bridge Street United Church, Quinte Christian High School: not attempted (BNs unknown and web search unavailable; the datastore API supports `q=<name text>` full-text search, which could be tried next).
- UNRESOLVED — Model comparables (Summit School Montreal, Oak Bridge Academy, Monarch House-type schools, Brighton School, Kohai Educational Centre): not attempted for the same reason. Note that Oak Bridge Academy and Monarch House are, to the researcher's knowledge, for-profit operators and would not appear in T3010 data; this was not verified.
- The CRA 2024 List of charities dataset (FPEs in 2024) was not located; figures above are FY2023 and may be one to two years stale.
- charitydata.ca (both name and `/charity/x/<BN>/` URL forms) returned only page metadata to the fetcher — it appears to render client-side; Blumbergs and Charity Intelligence were not tried.

## 2. Ontario Trillium Foundation eligibility of schools and operating-history requirement

### Takeaway
UNRESOLVED. otf.ca disallows automated fetching (robots.txt), and the alternates tried (Wayback Machine, ontario.ca OTF page, GrantWatch) were blocked, errored, or hit the session limit.

### Cited Findings
- None retrieved.

### Inferences
- None.

### Gaps
- Tried and failed: `otf.ca/our-grants/eligibility` (ROBOTS_DISALLOWED), `otf.ca/our-grants/community-investments-grants` and `/seed-grant` (ROBOTS_DISALLOWED), `otf.ca/resources/forms-and-documents` (ROBOTS_DISALLOWED), `web.archive.org/web/2026/https://otf.ca/our-grants/eligibility` (SITE_BLOCKED), `ontario.ca/page/ontario-trillium-foundation` (fetch error), `grantwatch.com/cat/41/ontario-trillium-foundation.html` (session limit). Still needed: eligible applicant types (whether schools/educational institutions are eligible), the one-year-of-financial-statements rule for Seed/Grow/Capital in the 2026–29 program, and deadlines for the next 12 months. A human can read otf.ca directly; the fetcher cannot.

## 3. Service clubs and local/community foundations

### Takeaway
UNRESOLVED (not reached, apart from two inconclusive fetches). No service-club grant pages or local-news gift examples were retrieved.

### Cited Findings
- Community Foundations of Canada's "Find a community foundation" page contains only an embedded ArcGIS map (no text list of Ontario foundations), with the note "Community foundations may have additional assets or supports to community that are not listed on the map." — [communityfoundations.ca](https://communityfoundations.ca/find-a-community-foundation/) (fetched 2026-10-14).

### Inferences
- None.

### Gaps
- Tried and failed: `cfka.org/about-us/` (fetch error). Not attempted: Rotary Club of Belleville, Rotary Club of Quinte Sunrise, Belleville Lions, Kinsmen Club of Belleville, Knights of Columbus councils, Belleville Shrine Club, 100 Men/100 Women Who Care Quinte, Kiwanis Club of Belleville, Trenton Rotary/Kinsmen, and the "Quinte/Hastings/Belleville community foundation" existence check. All require web search, which was exhausted before this run started.

## 4. National/provincial foundations accepting unsolicited applications

### Takeaway
UNRESOLVED. Every foundation site attempted (Azrieli, Slaight, Rick Hansen) failed to fetch; the remainder were not reached.

### Cited Findings
- None retrieved.

### Inferences
- None.

### Gaps
- Tried and failed: `azrielifoundation.org/education/` (server error), `/grants/` (fetch error), home page (session limit); `theslaightfamilyfoundation.org` (ROBOTS_DISALLOWED); `rickhansen.com/become-accessible/accessibility-funding` (fetch error). Not attempted: Lions Foundation of Canada, McConnell, Lawson, Laidlaw, TD Friends of the Environment, Home Depot Canada Foundation, RBC Foundation/Future Launch, Scotiabank ScotiaRISE, Mackenzie Investments Charitable Foundation, Hydro One/OPG community investment, Enbridge Fueling Futures, CIBC Foundation, Ontario Community Building Fund successors, Inclusion Canada/Community Living Ontario funds. Open/closed/invitation-only status for all of these remains to be labelled.

## 5. Lenders for Ontario nonprofits

### Takeaway
UNRESOLVED. Community Forward Fund and Infrastructure Ontario pages did not load; credit unions, VCIB, Realize Capital Partners and the Social Finance Fund were not reached.

### Cited Findings
- None retrieved.

### Inferences
- None.

### Gaps
- Tried and failed: `communityforwardfund.ca` (session limit); `infrastructureontario.ca/en/what-we-do/loans/`, `/loans/eligible-borrowers/`, `/lending/` (fetch errors — the URL paths were guessed and may be wrong), IO home page (session limit). Not attempted: Kawartha CU, Alterna, Desjardins Ontario, Northern CU, Your Neighbourhood CU, FirstOntario, Vancity Community Investment Bank, Realize Capital Partners / Social Finance Fund Ontario intermediaries, SFF wholesaler terms, and the question of personal guarantees for founders.

## 6. Employment Ontario / Youth Job Connection wage subsidies

### Takeaway
UNRESOLVED. The single fetch of ontario.ca/page/youth-job-connection returned a fetch error.

### Cited Findings
- None retrieved.

### Inferences
- None.

### Gaps
- Still needed: whether a nonprofit school can act as a Youth Job Connection employer (hiring incentive for 15–29-year-olds facing barriers, paid pre-employment training hours) and whether placements can be for students in the school's own pre-employment programming, plus any Employment Ontario wage-subsidy route for hiring staff.

## 7. Ontario Autism Program provider status and Entry to School relevance

### Takeaway
UNRESOLVED. Both ontario.ca OAP pages were requested but the session limit interrupted before any content was returned.

### Cited Findings
- None retrieved.

### Inferences
- None.

### Gaps
- Tried: `ontario.ca/page/ontario-autism-program` and `ontario.ca/page/ontario-autism-program-entry-school-program` (session limit on both). Still needed: OAP Provider List requirements for core clinical services (regulated clinician / clinical supervisor criteria), caregiver-mediated and Entry to School delivery model (lead-agency delivered, ages 3–6, whether the "school" the child is entering can be a private school), and whether any of this creates a revenue or partnership path for an independent school.
