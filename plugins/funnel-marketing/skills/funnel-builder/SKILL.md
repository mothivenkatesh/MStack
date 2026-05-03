---
name: funnel-builder
description: >
  Use this skill whenever the user provides a product URL, company name, or competitor
  and wants to reverse-engineer their launch and distribution strategy. Trigger this skill
  when the user mentions phrases like "reverse engineer this funnel", "decode their funnel",
  "teardown of [company]", "competitor teardown", "how did X launch", "how are they getting
  users", "what's their distribution", "what's their playbook", "show me their digital
  footprint", "audit their funnel", "deconstruct their GTM", "how do they sell", "what funnel
  template are they using", or shares a competitor URL and asks how it was built into market.
  Also trigger when the user asks for a launch timeline, channel-mix analysis, or "copy this
  in 90 days" plan based on a competitor. Always use this skill before attempting funnel or
  distribution reverse-engineering from scratch — it enforces the four-phase workflow
  (Discovery → Timeline → Funnel Mapping → Distribution Synthesis), citation discipline,
  confirmation gates, and the standardized intelligence-report output format.
user-invocable: true
argument-hint: "[product URL or company name] [optional: focus = full | launch | funnel | distribution | discovery-only]"
---

# Reverse-Engineer-Funnel Skill

This skill defines the end-to-end workflow for turning a single product URL or company name into a complete **Launch & Distribution Teardown** — an intelligence report another team could use to replicate (or counter) the strategy.

The skill enforces:
- A **four-phase sequence** that must run in order — synthesis quality depends on discovery completeness
- **Citation discipline** — every claim ties back to a public URL with a date
- **Confirmation gates** before expensive phases (Phase 1 → Phase 2, Phase 3 → Phase 4)
- A standardized 7-section report with TL;DR, footprint inventory, timeline, AARRR funnel, distribution playbook, 90-day copy plan, and open questions
- A funnel-template lookup against the canonical 12 templates (see `references/funnel-templates.md`)

---

## Workflow Overview

```
Phase 0: Intake → confirm target + focus + use case (skip if URL is clear)
Phase 1: Discovery → exhaustive footprint inventory (table)
        ↓ confirmation gate: "Discovery complete — proceed to Timeline?"
Phase 2: Timeline → chronological events + phases of growth
Phase 3: Funnel Mapping → AARRR with evidence + funnel-template match
        ↓ confirmation gate: "Funnel mapped — proceed to Synthesis?"
Phase 4: Synthesis → playbook + 90-day copy plan + what NOT to copy
Final: Present full intelligence report in the standard format
```

**Critical rule**: Never skip ahead to Phase 4 when the user asks "what's their playbook" — the playbook only holds up if Phases 1-3 were done. If the user wants a quick read, run an explicit `discovery-only` or `launch-only` focus, but say so.

---

## Phase 0 — Intake

### Step 0.1 — Extract target and confirm focus

Take the product URL, company name, or description provided by the user. If only a name is given, find the canonical homepage URL first via WebSearch.

If the user did not specify a focus, ask **one** clarifying question:

> "Quick check before I go deep:
> • **Target confirmed:** [URL or name]
> • **Focus:** full report (Discovery → Timeline → Funnel → Synthesis), or just one phase?
> • **Use case:** are you trying to **replicate**, **compete against**, **learn from**, or **invest in** this company? (Shapes the synthesis lens.)
> • **Constraints:** any markets to limit (India only, US only, EU only) or sources off-limits?"

Skip this step entirely if the user gave a URL and explicitly said "full teardown" or "do it all."

### Step 0.2 — Set scope expectations

State up front:
- The four phases that will run
- That all claims will be cited to public URLs
- That you will pause at the gates between phases for confirmation if the focus is `full`

---

## Phase 1 — Discovery: Map Every Digital Footprint

Goal: produce an exhaustive inventory of where this product/service exists online, with raw URLs and timestamps. Skipping categories causes blind spots in later phases.

### Step 1.1 — Walk the source matrix

Read [references/phase-1-discovery.md](references/phase-1-discovery.md) for the full 15-category source matrix (web, blogs, socials, forums, communities, app stores, review sites, podcasts, video, code repos, launch platforms, press, ad libraries, SEO/backlink intel, employee/team footprints, vernacular/regional sources).

Walk the matrix in this order:
1. **On-site footprint** first — domain, sitemap, robots.txt, /blog, /changelog, /pricing, /customers, /careers
2. **Off-site categories** in parallel — spawn sub-agents (subagent_type: researcher or general-purpose) for independent categories when scope is large
3. **Domain & infrastructure intel** — WHOIS, BuiltWith, SimilarWeb, Wayback first-snapshot
4. **Vernacular/regional** last — but never skip if the company operates in India/SEA/LATAM/MENA

For every footprint, capture: **URL, type, first-seen date, last-seen date, raw notes**.

### Step 1.2 — Present the footprint inventory in this exact format

---

### 🔍 Footprint Inventory — [Product Name]

| # | Source | URL | Type | First Seen | Last Seen | Notes |
|---|--------|-----|------|-----------|-----------|-------|
| 1 | Domain WHOIS | — | Infra | 2022-03-14 | — | Registered via Namecheap, NS on Cloudflare |
| 2 | Product Hunt launch | https://... | Launch | 2022-09-08 | — | 1,247 upvotes, hunted by [name] |
| 3 | Twitter @company | https://... | Owned social | 2022-08-22 | 2026-04-30 | Created 2 weeks pre-launch; cadence ~3/wk |
| 4 | r/SaaS thread | https://... | Community | 2023-02-11 | — | Founder AMA, 312 comments |
| ... | | | | | | |

**Discovery summary** (3-5 sentences): which categories were richest, which were sparse, what surprised you, and what each absence tells us.

---

### Step 1.3 — Confirmation gate

After presenting the inventory, always say:

> "Discovery complete — **[N] footprints** catalogued across [M] categories.
> Want me to proceed to **Phase 2 (Timeline Reconstruction)**, or should I dig deeper into any specific category first?
> Reply **yes** / **proceed** to continue, or name the category to expand."

Wait for explicit confirmation if focus is `full`. Skip the gate if focus is `discovery-only`.

---

## Phase 2 — Timeline Reconstruction

Goal: turn the unordered footprint inventory into a dated, ordered launch timeline. Order reveals priority — what they bet on first, second, third.

### Step 2.1 — Date every footprint

Read [references/phase-2-timeline.md](references/phase-2-timeline.md) for the full dating-techniques playbook (Wayback, WHOIS, schema.org, RSS pubDates, platform-native timestamps, GitHub commit history, crt.sh, Crunchbase, conflict resolution).

Apply techniques in order of reliability:
1. Hard-coded publish metadata (schema.org, `<meta>`, RSS)
2. Platform-native timestamps (X, LinkedIn, YouTube, GitHub, PH, App Store)
3. Wayback Machine (earliest snapshot, copy-evolution diffs)
4. Domain & infra (WHOIS, crt.sh, BuiltWith first-detected)
5. Press & funding (Crunchbase rounds, TC articles)
6. Inferred / triangulated (founder tweets, first customer logo, first job posting)

Resolve conflicts using "earliest credible = exists by; latest = publicly active by." Flag conflicts in notes — they're often informative ("operated in stealth for 18 months").

### Step 2.2 — Present the master chronological timeline

---

### 📅 Launch Timeline — [Product Name]

| Date | Event | Channel/Surface | Evidence URL | Inferred Intent |
|------|-------|-----------------|--------------|-----------------|
| 2021-03-14 | Domain registered | Infra | [whois] | Stealth begins |
| 2021-11-02 | First public GitHub commit | Code | [github] | MVP open-sourced |
| 2022-08-22 | Twitter @company created | Social | [x.com] | Owning channel pre-launch |
| 2022-09-08 | Product Hunt launch (#1 of day) | Launch | [PH] | Public v1 |
| 2022-09-09 | TechCrunch coverage | Press | [TC] | PR was pre-arranged |
| 2023-02 | Pricing dropped $49 → $29 | Monetization | [wayback] | Activation issue → lower price |
| 2023-04-19 | Series A announced ($12M) | Press | [TC] | Capital for distribution |
| 2024-01 | Affiliate program launched | Partner | [/affiliates] | Begin compounding distribution |
| ... | | | | |

### Step 2.3 — Segment into phases of growth

Most companies fall into 4-6 phases. Name each phase, give a one-line characterization, and note the dominant bet:

```markdown
## Phase A — Stealth (2021-03 → 2022-08, 17 months)
Building period. Two founders, one engineer. No public marketing function.
Dominant bet: Product depth.

## Phase B — Public Launch (2022-08 → 2022-12, 4 months)
Coordinated multi-channel launch over ~2 weeks. PH + TechCrunch + founder Twitter + cold outbound.
Dominant bet: Concentrated noise window.

## Phase C — Content Moat (2023-01 → 2023-08, 8 months)
Single dominant bet: SEO content. 47 articles at 2/wk cadence. No paid spend yet.
Dominant bet: Compounding organic.

## Phase D — Paid + Scale (2023-09 → 2024-06, 10 months)
Series A enabled paid bets. YouTube + Google Ads + LinkedIn Ads start within 60 days.
Dominant bet: Channel diversification.

## Phase E — Loops (2024-07 → present)
Affiliate program, integration marketplace presence, customer-led growth.
Dominant bet: Compounding distribution.
```

### Step 2.4 — Optional: ASCII timeline visualization

Include a simple ASCII timeline if it sharpens the story. Optional.

---

## Phase 3 — Funnel Mapping

Goal: trace, with public evidence, how a stranger becomes a user → customer → advocate. Map AARRR (or the model-specific equivalent) and **explicitly match against the canonical 12 funnel templates**.

### Step 3.1 — Pick the right funnel shape

Read [references/phase-3-funnel.md](references/phase-3-funnel.md) for funnel-shape selection (PLG / sales-led / marketplace / dev tool / consumer app / services / community-led).

State the funnel shape explicitly before proceeding.

### Step 3.2 — Match against the canonical 12 funnel templates

Read [references/funnel-templates.md](references/funnel-templates.md) for the 12 templates mined from real marketing-community discourse:

1. Tripwire / low-ticket → upsell stack (Brunson)
2. VSL → application → call (Hormozi / Cole Gordon)
3. Webinar funnel (live + evergreen)
4. PLG free trial → paid
5. Freemium → premium upgrade
6. Lead magnet → email nurture → offer
7. Challenge funnel (5-day / 7-day)
8. Book funnel (low-ticket book + upsell stack)
9. High-ticket coaching application funnel
10. E-commerce cold-ad → PDP → checkout → upsell
11. Affiliate / 2-step opt-in
12. Marketplace 2-sided funnel

For each match, cite the URL pattern, page structure, ad copy pattern, or pricing pattern that gave it away. If the funnel is a hybrid or doesn't match cleanly, say so and describe the variant.

### Step 3.3 — Walk the AARRR layer with evidence

For each stage — **Acquisition, Activation, Retention, Revenue, Referral** — present specific mechanisms with evidence URLs. Sign up to the product to walk activation end-to-end (use a throwaway email; respect ToS).

Present in this format:

---

### 🛒 User Funnel — [Product Name]

**Funnel shape:** [PLG / Sales-led / Marketplace / Hybrid]
**Closest canonical template match:** [#X — name] | confidence: [High/Medium/Low]
**Why this match:** [1-2 lines tied to specific evidence]

**Acquisition**

| Channel | Paid/Organic | Evidence | Effort Tier | Notes |
|---------|--------------|----------|-------------|-------|
| SEO comparison pages | Organic | /vs/competitor/* (12 pages, ranked #1-3) | High | Built before launch |
| Paid Search | Paid | [Google Ads Transparency] | Medium | Started Q2 2023 |
| Founder Twitter | Owned | 18K followers, 4 posts/wk | High | Largest demand source per [podcast] |
| ... | | | | |

**Activation**
- **Sign-up flow:** [email + magic link / SSO / CC required] — [time to first value]
- **First-run UX:** [tour / sample data / template gallery / Loom follow-up]
- **Activation hypothesis:** [the metric they likely measure, with evidence]

**Retention**
- [Mechanism 1 with evidence]
- [Mechanism 2 with evidence]
- [Switching cost / network effect / habit loop]

**Revenue**
- **Tiers:** [count and gaps]
- **Pricing evolution:** [Wayback diff if any]
- **Expansion lever:** [per-seat / per-usage / add-on]
- **Sales motion:** [self-serve / contact-sales / hybrid]

**Referral**
- **Affiliate program:** [terms, commission, cookie window]
- **In-product virality:** [shareable artifacts / public links / "powered by" badges]
- **Customer marketing:** [G2 review velocity, case-study cadence, logo wall]

**Friction & open questions**
- [Things you couldn't verify but suspect]

---

### Step 3.4 — Confirmation gate

After presenting the funnel, always say:

> "Funnel mapped — closest template match is **#[X] — [name]** with [High/Medium/Low] confidence.
> Want me to proceed to **Phase 4 (Distribution Strategy Synthesis)**, or should I tighten any stage first?
> Reply **yes** / **proceed** to continue."

---

## Phase 4 — Distribution Strategy Synthesis

Goal: compress everything into a **replicable playbook** — the deliverable a PMM, founder, or growth lead would actually use.

### Step 4.1 — Synthesize using the playbook structure

Read [references/phase-4-synthesis.md](references/phase-4-synthesis.md) for the synthesis structure (one-line strategy, channel-mix matrix, messaging-evolution analysis, compounding loops, non-obvious lever, "Copy This in 90 Days" plan, what NOT to copy).

### Step 4.2 — Present the final intelligence report in this exact format

This is the final deliverable. Always use this 7-section structure:

---

# [Product Name] — Launch & Distribution Teardown

## TL;DR (5 bullets)
- The thing they did
- The order they did it in
- The 1-2 channels that actually worked
- The non-obvious lever
- What you'd copy / what you wouldn't

## 1. Footprint Inventory
[Table from Phase 1, condensed to top 25 if longer]

## 2. Launch Timeline
[Chronological table + phases of growth from Phase 2]

## 3. User Funnel (AARRR + Template Match)
**Closest canonical template:** #[X] — [name]
[Stage-by-stage breakdown from Phase 3 with evidence URLs]

## 4. Distribution Playbook
- **One-line strategy:** [≤25 words]
- **Channel mix matrix:** [table — channel | % effort | paid/organic | when activated | why it works]
- **Content cadence:** [posting frequency, formats, themes]
- **Messaging evolution:** [Wayback diff table at 3-5 inflection points]
- **Partnership pattern:** [who, when, why]
- **Community plays:** [communities seeded/built and how]
- **Compounding loops:** [what compounds without ongoing input]

## 5. The "Copy This in 90 Days" Plan

| # | Move | Effort (1-5) | Impact (1-5) | Leading Indicator |
|---|------|--------------|--------------|-------------------|
| 1 | Build 12 SEO comparison pages targeting top competitor brand terms | 3 | 5 | 100+ organic clicks/wk by day 60 |
| 2 | Stand up founder Twitter, 4 posts/wk, technical depth | 2 | 4 | 500 followers in 60 days, 3 inbound demos |
| 3 | Coordinate Product Hunt launch with pre-warmed list of 200 emails | 4 | 3 | Top 5 of day; 800 signups in 48h |
| ... | | | | |

5-10 ranked moves, opinionated. Drop anything weak.

## 6. What I Wouldn't Copy
- [Move 1] — why it worked for them but won't for you (founder advantage / capital / market timing)
- [Move 2] — ...

## 7. Open Questions / Gaps
- [Specific thing you couldn't verify, with what would unlock it]

## 8. Sources
[All URLs cited, organized by section]

---

## Operating Principles

These principles bind every phase. Violations make the report unusable.

- **Cite everything.** Every claim has a URL. If you can't find evidence, mark it as a hypothesis. Do not fabricate URLs.
- **Dates are non-negotiable.** A footprint without a date is half-useless. Use Phase 2 techniques aggressively.
- **Public data only.** No scraping behind logins, no paywall bypassing, no facial-image gathering. Respect robots.txt.
- **Triangulate.** Don't trust a single source for a key claim — confirm via at least two independent footprints.
- **Look for what's missing.** Absence is signal. No Twitter? No SEO blog? No paid ads? Each absence narrows their actual strategy.
- **Distinguish stated strategy from revealed strategy.** Their "About" page says one thing; their footprint pattern shows another. Trust the pattern.
- **Use sub-agents for parallelism.** Phase 1 source categories are independent — spawn researchers in parallel when scope is large.
- **Report on what you found, not what you wished you'd found.** If a phase is sparse, say so and explain why (private company, recent launch, regional focus).
- **Confirmation gates are non-optional in `full` mode.** Don't blast through to synthesis without checking in.

---

## Common Mistakes to Avoid

- **Do not skip Phase 1.** Tempting to jump to "what's their playbook" — but the playbook is only credible if discovery is complete.
- **Do not over-index on the website.** The website is one footprint among ~30. Don't stop at the homepage.
- **Do not confuse chronology with causation.** X happening before Y doesn't mean X caused Y. Note correlation; flag causation as hypothesis.
- **Do not assume SaaS-style funnels.** Adapt AARRR for the actual model — marketplace, B2B sales-led, dev tool, info product, services.
- **Do not produce generic playbook output.** "They use content marketing" is useless. "They published 47 SEO articles in 6 months targeting [specific cluster] of long-tail terms, ranking on 31" is a playbook.
- **Do not forget the funnel-template match.** Naming the template (e.g., "VSL → application → call") compresses 1000 words of explanation into 5.
- **Do not pad the 90-day plan.** 5-10 ranked moves beats 20. Force prioritization.
- **Do not skip "What I wouldn't copy."** This is the section that distinguishes serious analysis from cargo-culting.
- **Do not fabricate dates or URLs.** If Wayback has no snapshot, say "first snapshot: 2023-04 (lower bound)." Never invent.
- **Do not bypass the confirmation gates** unless the user explicitly opted into a fast lane.

---

## Notes on Tools & Sources

When researching for a teardown, prioritize these sources:

- **Wayback Machine (archive.org)** — single most powerful tool. Earliest snapshot, copy evolution, pricing changes
- **WHOIS + crt.sh** — domain/cert history reveals subdomain launches
- **Google Ads Transparency Center, Meta Ad Library, LinkedIn Ad Library** — full ad history with run dates
- **Product Hunt, BetaList, AppSumo** — launch-platform footprints with dates
- **G2, Capterra, TrustPilot** — review velocity = adoption proxy
- **GitHub + star-history.com** — commit history, star trajectory
- **Crunchbase + LinkedIn** — funding timeline + headcount/hiring trajectory
- **BuiltWith + Wappalyzer** — analytics, marketing, payment, hosting stack
- **SimilarWeb** — traffic estimates + top referring domains
- **Reddit / HN / IndieHackers / Lenny's** — organic conversation, AMAs, founder commentary
- **Listen Notes + Apple Podcasts** — exec/founder podcast circuit
- **Indian context** — Inc42, YourStory, MoneyControl, MediaNama for Indian press; r/developersIndia, r/IndiaSpeaks for community
- **Uploaded documents** — always prioritize over generic web research; they carry the company's own framing
