# Phase 2 — Timeline Reconstruction

Goal: turn the unordered footprint inventory from Phase 1 into a dated, ordered narrative of *what happened when*. Order reveals priority, and priority reveals strategy.

## Why dates matter more than they look

Without dates, you have a list. With dates, you have a story. The story shows:
- What they bet on **first** (signal of true conviction)
- What they bet on **second** (signal of what worked)
- What they **abandoned** (gap in cadence = pivot or kill)
- How **long** each phase lasted before scaling
- What was **simultaneous** vs **sequenced** (resource discipline)

## Dating techniques (in order of reliability)

### 1. Hard-coded publish metadata
- Blog post `<meta property="article:published_time">` and `<meta property="article:modified_time">`
- Schema.org JSON-LD `datePublished` / `dateModified` fields
- RSS feed `<pubDate>` tags
- Sitemap.xml `<lastmod>` entries
- HTTP `Last-Modified` headers (sometimes accurate, often cache-driven)

### 2. Platform-native timestamps
- Twitter/X — exact post timestamp on each tweet (use Twitter advanced search: `from:handle since:YYYY-MM-DD until:YYYY-MM-DD`)
- LinkedIn — relative timestamps; mouse over to get exact, or scroll to find
- YouTube — "Published on" date on every video; "Joined" date on channel About tab
- Reddit — exact post and comment timestamps; sort `top` `all-time` to find inflection points
- Hacker News — every submission and comment is dated
- Product Hunt — launch date is the canonical "v1.0 to public" date
- App Store — "Released" date + per-version "What's New" dates
- GitHub — commit dates, repo creation date, release tags, star history (star-history.com)

### 3. Wayback Machine (archive.org)
The single most powerful tool. For every key page:
- Earliest snapshot = lower bound on when page existed
- Snapshot frequency = signal of activity
- Compare snapshots N months apart to see copy evolution, pricing changes, positioning shifts
- Use Wayback's CDX API for programmatic access if you need many dates

Other archives: archive.today (often catches what Wayback misses), Google cache (short-lived), Bing cache.

### 4. Domain & infrastructure
- WHOIS — domain creation date (lower bound on company age; sometimes domain pre-dates company)
- crt.sh — every SSL cert issued for the domain, with dates (catches subdomain launches)
- DNS history (SecurityTrails free tier, ViewDNS) — when MX/NS/A records changed
- BuiltWith — "first detected" date for each tech in their stack

### 5. Press & funding
- Crunchbase — funding round dates, often the most reliable corporate-history dates
- TechCrunch / Bloomberg / sector press — launch articles, funding announcements, exec changes
- LinkedIn company "Founded" date (often inaccurate; cross-check)
- Government registries (SEC EDGAR, MCA for India, Companies House for UK) — incorporation date

### 6. Inferred / triangulated dates
When no hard date exists, infer from:
- Founder's tweet announcing it
- First customer logo appearance on website (use Wayback to find when the logo was added)
- First mention in a podcast (transcript search)
- First Glassdoor review (proxy for ~6 months post-incorporation)
- First job posting (signals when they started hiring for that function)

## Handling conflicting dates

You will find conflicts (e.g., domain registered 2021-03, but Wayback's first snapshot is 2022-09, and Crunchbase says founded 2020). Resolve by:
- **Use the earliest credible date as "exists by"** and the latest as "publicly active by"
- **Flag the conflict** in your timeline notes — it's often informative ("operated in stealth for 18 months")
- **Prefer hard timestamps over self-reported dates** (LinkedIn "Founded" is often vibes)

## Timeline output format

### Master chronological table

```markdown
| Date | Event | Channel/Surface | Evidence URL | Inferred intent |
|------|-------|-----------------|--------------|-----------------|
| 2021-03-14 | Domain registered | Infra | whois | Stealth begins |
| 2021-11-02 | First GitHub commit (private→public) | Code | github.com/... | Building MVP |
| 2022-06-08 | Founder hired first marketer (LinkedIn) | Team | linkedin.com/in/... | Prep for launch |
| 2022-08-22 | Twitter @company created | Social | x.com/company | Owning channel pre-launch |
| 2022-09-08 | Product Hunt launch (#1 of day) | Launch | producthunt.com/... | Public v1 |
| 2022-09-09 | TechCrunch coverage | Press | techcrunch.com/... | PR was pre-arranged |
| 2022-09-12 | First SEO blog published | Content | /blog/... | Begin organic moat |
| 2022-11 | Cadence: 2 blogs/wk for 8 wks | Content | /blog | Content sprint |
| 2023-02 | Pricing page changes from $49 → $29 | Monetization | wayback | Activation issue → lower price |
| 2023-04-19 | Series A announced ($12M) | Press | techcrunch | Capital for distribution |
| 2023-05 | First Google Ads campaign | Paid | adstransparency | Begin paid acquisition |
| 2023-09 | YouTube channel kicks off (12 vids) | Content | youtube.com/@... | Long-form content bet |
| 2024-01 | Affiliate program launches | Partner | /affiliates | Begin compounding distribution |
| ... | | | | |
```

### Phase segmentation

Group the timeline into **phases of growth**. Most companies fall into 4-6:

```markdown
## Phase A — Stealth (2021-03 → 2022-08)
- 17 months of building, no public footprint
- Signal: 2 founders, 1 engineer hired, no marketing function
- Key artifacts: domain reg, GitHub repos (private), first hires

## Phase B — Public Launch (2022-08 → 2022-12)
- Coordinated multi-channel launch over ~2 weeks
- PH + TechCrunch + founder Twitter + cold outbound
- Signal: ~30 footprints created in 90 days

## Phase C — Content Moat (2023-01 → 2023-08)
- Single dominant bet: SEO content (47 articles, 2/wk cadence)
- Began ranking for 31 long-tail terms by month 6
- No paid spend yet

## Phase D — Paid + Scale (2023-09 → 2024-06)
- Series A enabled paid bets
- YouTube + Google Ads + LinkedIn Ads start within same 60-day window
- Sales team hired (LinkedIn shows 4 AEs joined Q4 2023)

## Phase E — Compounding Loops (2024-07 → present)
- Affiliate program, integration marketplace presence, customer-led growth
- Content cadence drops (efficient frontier reached)
- Focus shifts to community + events
```

### Optional: ASCII visualization

```
2021 ─── 2022 ─── 2023 ─── 2024 ─── 2025 ─── 2026
 │        │        │        │        │
 │ STEALTH│ LAUNCH │CONTENT │ PAID + │ LOOPS
 │  ▓▓▓▓▓▓│ ▓▓     │ ▓▓▓▓▓▓ │ SCALE  │ ▓▓▓▓
 │        │        │        │ ▓▓▓▓▓▓▓│
 │        │        │        │        │
   17 mo    4 mo     8 mo     10 mo    ongoing
```

## What "done" looks like

- Every Phase 1 footprint either has a date or is explicitly marked "undated, reason: X"
- Master timeline covers from earliest detectable date to today
- 4-6 named phases, each with a one-line characterization
- A "what surprised you" 3-bullet observation about the order/cadence
