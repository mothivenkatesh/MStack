# Phase 3 — Funnel Mapping (User Journey Reverse-Engineering)

Goal: trace, with public evidence, how a stranger becomes aware of this product, tries it, sticks with it, pays, and refers others. Use the AARRR framework as a scaffold and adapt it to the actual business model.

## Pick the right funnel shape first

AARRR is the default but not universal. Confirm the model from Phase 1/2 evidence:

| Model | Funnel shape | Where to look |
|-------|--------------|---------------|
| Self-serve SaaS / PLG | AARRR — sign-up to activation in minutes | Free tier, in-product onboarding, usage-based pricing |
| Sales-led B2B | Lead → MQL → SQL → Opp → Won | "Book a demo" CTA, gated content, salesnav presence, AE hires |
| Marketplace (2-sided) | Two parallel funnels (supply + demand) | Separate landing pages, signup flows |
| Dev tool | Awareness → Star → Install → Build → Pay | GitHub stars, npm installs, docs traffic, paid plan signals |
| Consumer app | Install → Onboarding → Habit loop → Subscription | App store ranking, push perms, trial → paid conversion |
| Services/agency | Lead → Discovery call → Proposal → Engagement | Calendly links, contact forms, case study cadence |
| Community-led | Lurker → Joiner → Contributor → Champion | Discord/Slack, contribution patterns |

Pick the closest model and label your funnel stages accordingly. AARRR labels below are the fallback.

## AARRR — what to look for at each stage

### Acquisition — how strangers first encounter the product

For each channel found in Phase 1, classify as **owned**, **earned**, or **paid**, and estimate effort/spend tier.

Mechanisms to identify:
- **SEO** — what keyword clusters do they rank for? (use Google for "[topic] site:competitor.com")
- **Paid search** — Google Ads Transparency reveals keywords + ad copy
- **Paid social** — Meta/LinkedIn/TikTok ad libraries reveal targeting tells
- **Content / SEO blog** — topic clusters, publishing cadence, distribution
- **Earned media / PR** — TC/Verge mentions, founder podcast circuit
- **Community-driven** — Reddit/HN/Discord presence, organic mentions
- **Referral / affiliate** — program existence, payout, partner depth
- **Outbound** — sales team size on LinkedIn, "Outreach"/"Apollo" footprints in DNS
- **Partnerships** — co-marketing, integration listings, joint webinars
- **Events** — sponsorships, booth presence, speaking slots

For each, capture a concrete example: "Ranks #2 for 'invoice OCR India' (estimated 1.2K monthly searches)" beats "does SEO."

### Activation — what counts as "activated" and how do they get there

This is the hardest stage to reverse-engineer without internal data, but signals are visible:
- **Sign-up flow** — walk it (use a throwaway email; respect ToS). Note: required fields, magic link vs password, CC required, social login, time to first value
- **Onboarding pattern** — interactive tour? sample data? template gallery? Loom/email follow-up?
- **Time-to-value** — from sign-up click to first "wow" moment, in seconds. The lower, the more PLG-mature
- **Aha moment proxies** — what's the very first thing the empty state asks you to do?
- **Activation metric hypothesis** — what would they measure? (e.g., "first invoice scanned within 5 min", "first repo connected", "first contact added")

### Retention — what brings users back

Without analytics access, infer from:
- **Notification design** — email, push, Slack, in-app. What triggers them?
- **Habit loops** — daily/weekly digests? Streaks? Reports?
- **Network effects** — does the product get better with usage data or other users?
- **Switching cost** — data lock-in, integrations, team setup
- **Pricing structure** — usage-based pricing forces re-engagement; flat fees don't
- **Changelog cadence** — frequent shipping = retention bet
- **Status page / uptime** — reliability signals

### Revenue — how they monetize

- **Pricing tiers** — count, gap, anchor pricing, "popular" badge
- **Free vs paid wall** — what's gated, what's not
- **Sales model** — self-serve checkout, "contact sales", hybrid
- **Expansion levers** — per-seat, per-usage, add-ons, tiers
- **Discounts/promos** — annual discount, education, startups, lifetime deals
- **Pricing evolution** (via Wayback) — went up? went down? added a tier? removed one?

### Referral — how users bring users

- **Referral program** — incentive structure, share UX
- **Affiliate program** — public terms, commission, cookie window
- **Built-in virality** — invite flows, "powered by" badges, public artifacts (e.g., shareable reports)
- **Community advocacy** — UGC patterns, ambassador programs
- **Customer marketing** — case studies, logo wall, G2 review velocity

## Funnel mapping output template

```markdown
## User Funnel — [Product Name]

**Funnel shape:** [PLG / Sales-led / Marketplace / etc.]

### Acquisition
| Channel | Type | Evidence | Effort tier | Notes |
|---------|------|----------|-------------|-------|
| SEO — comparison pages | Owned | /vs/competitor/* (12 pages, ranked #1-3) | High | Built before launch |
| Paid Search — bottom-funnel | Paid | Google Ads "alternatives to X" | Medium | Started Q2 2023 |
| Founder Twitter | Owned | 18K followers, 4 posts/wk | High | Single largest demand source per podcast quote |
| Product Hunt | Earned | #1 of day, 1.2K upvotes | One-time | Launch lever |
| ... | | | | |

### Activation
- **Sign-up:** Email + magic link, no CC. ~14 sec from click to dashboard.
- **First-run UX:** 3-step tour with sample dataset pre-loaded. Empty state CTA: "Connect your first source."
- **Activation hypothesis:** "First report generated within 10 min of sign-up." Inferred from /how-it-works copy and onboarding email sequence (analyzed 4 emails received in 48h).

### Retention
- Weekly digest email (cadence inferred from public archives via inbox.com leaks)
- Slack-native bot — high stickiness; retention bet
- Status page shows 99.95% — reliability is a positioning asset
- Changelog: 3-4 ships/month for 18 straight months

### Revenue
- 4 tiers: Free / Pro $29 / Team $99/seat / Enterprise (contact)
- 2024 pricing change: Pro went $49 → $29 (Wayback diff). Hypothesis: activation lift bet.
- Expansion: per-seat + per-event usage caps
- Annual = 20% discount; startups = 50% off Year 1

### Referral
- Affiliate program: 30% lifetime commission, 90-day cookie (fairly aggressive)
- In-product: shareable public report links (built-in viral loop — every shared report is a backlink + brand impression)
- 47 G2 reviews in 18 months = ~2.6/month — moderate organic advocacy
```

## What "done" looks like

- All 5 AARRR stages covered (or model-specific equivalents)
- Each stage has 2+ specific mechanisms with evidence URLs
- Activation walked end-to-end (don't skip the sign-up flow)
- 3-5 explicit hypotheses called out (things you couldn't verify but suspect)
- Friction & open questions logged for Phase 4

## Common mistakes to avoid

- Listing channels without classifying paid/owned/earned
- "They have a blog" — useless. "They publish 8 SEO comparison pages targeting competitor branded terms" — useful.
- Skipping activation because you don't want to sign up. Sign up. It's the highest-signal step.
- Assuming a referral program = referral works. Often the in-product viral loop matters more.
- Confusing "what they sell" with "how they convert." Pricing page tells you the latter.
