# Phase 1 — Discovery: Source Matrix

Goal: build an exhaustive inventory of every place the target product/service has a digital footprint. Skipping categories causes blind spots in later phases — work the full matrix.

## How to work this phase

1. Start with the **canonical URL** and pull domain-level intel (WHOIS, DNS, hosting).
2. Walk the **on-site footprint** (sitemap, robots.txt, /blog, /changelog, /pricing, /customers, /careers).
3. Then walk the **off-site categories** below in parallel — spawn sub-agents for independent categories when scope is large.
4. For every footprint, capture: **URL, type, first-seen date, last-seen date, raw notes**.
5. Save the running inventory as a markdown table; you'll feed it directly into Phase 2.

## Source matrix

### A. Owned web properties
- Primary domain + subdomains (`docs.`, `blog.`, `app.`, `help.`, `status.`, `careers.`)
- Sitemap.xml (reveals content structure + dates)
- Robots.txt (reveals what they hide)
- /changelog, /releases, /whats-new
- /pricing (current + via Wayback for evolution)
- /customers, /case-studies, /logos
- /careers, /jobs (signals team size, hiring focus, tech stack)
- Help center / knowledge base (article publish dates show feature timeline)
- API docs, developer portal
- Open-source repos, public SDKs

### B. Search & SEO footprint
- `site:domain.com` Google search — total indexed pages
- Top organic keywords (use any free tier of SEMrush, Ahrefs, Ubersuggest, SimilarWeb, or just Google)
- Backlink profile (referring domains, anchor text patterns)
- Featured snippets, "People also ask" appearances
- Schema markup (review counts, FAQ, Organization)

### C. Paid acquisition footprint
- **Google Ads Transparency Center** — every ad they've run with dates
- **Meta Ad Library** — Facebook/Instagram ads with run dates and spend bands
- **LinkedIn Ad Library** — B2B ads, targeting tells
- **TikTok Ad Library**, Pinterest, Snap (if consumer)
- Landing-page variants (often `/lp/`, `/get/`, `/try/` paths)
- UTM patterns in shared links (reveals channel attribution model)

### D. Social media — owned accounts
For each: profile URL, follower count, account creation date, post #1 date, current cadence, top-performing posts.
- Twitter/X
- LinkedIn (Company + Founders/CEO personal)
- Instagram
- YouTube (channel start date, view counts, video dates)
- TikTok
- Threads, Bluesky, Mastodon (if applicable)
- Pinterest (B2C, ecommerce)
- Facebook page

### E. Community & forum footprint
Where do users talk about this product (organic), and where does the company show up?
- Reddit — `site:reddit.com [product]`, relevant subreddits, official AMA history
- Hacker News — Algolia HN search for company name + URL
- Indie Hackers, Lenny's Newsletter community, Demand Curve, Superpath
- Quora answers (official + organic)
- Stack Overflow / Stack Exchange (dev tools)
- Discord servers (own + adjacent)
- Slack communities
- Telegram, WhatsApp groups (regional)
- Industry-specific forums (e.g., r/SaaS, r/Entrepreneur, GrowthHackers)

### F. Launch platforms & directories
- **Product Hunt** — launch date, upvotes, comments, hunter, makers
- BetaList, Launching Next, Uneed, Peerlist
- AppSumo / lifetime deal sites
- G2, Capterra, TrustRadius, GetApp, Software Advice (review velocity = adoption proxy)
- Trustpilot, SiteJabber (consumer)
- Industry-specific directories (e.g., Stackshare for dev tools, Toolify for AI, There's An AI For That)

### G. App stores (if applicable)
- iOS App Store — release date, version history, review velocity
- Google Play Store — first published date, install bands, recent updates
- Chrome Web Store, Firefox Add-ons (extensions)
- Shopify App Store, Slack App Directory, etc. (vertical stores)

### H. Code & developer footprint
- GitHub org — repos, commit history, contributors, star history (use star-history.com)
- GitLab, Bitbucket
- npm, PyPI, RubyGems, Crates packages — first publish date, download trends
- Postman / public API collections
- Devpost (hackathon entries)

### I. Press, PR, and earned media
- TechCrunch, The Verge, VentureBeat, Bloomberg, Forbes, etc. — `site:techcrunch.com [company]`
- Crunchbase — funding rounds, investors, dates
- PitchBook, Tracxn (paid, but free previews)
- Press releases on PR Newswire, Business Wire
- Local/regional press (esp. for India: ET, Inc42, YourStory, MoneyControl, MediaNama)
- Podcasts — founder/exec appearances (search Listen Notes, Apple Podcasts, Spotify)

### J. Video & long-form content
- YouTube — owned channel + mentions ("[product] review", "[product] tutorial")
- Webinars, conference talks (own + sponsored)
- Loom, Wistia public links

### K. Email & newsletter footprint
- Newsletter sign-up flow on site (what they ask for, double opt-in or not)
- Substack / Beehiiv newsletters they run
- Million Dollar Newsletter / SparkLoop / newsletter directories
- Newsletter sponsorships they've done — search "sponsored by [product]" in newsletter archives

### L. Partnership & integration footprint
- Integration marketplaces — Zapier, Make, n8n, Salesforce AppExchange, HubSpot Marketplace
- "Partners" page on own site
- Co-marketing case studies (their logo on partners' sites + vice versa)
- Affiliate program existence, terms, payout structure

### M. Hiring, team & talent footprint
- LinkedIn employee count over time (use LinkedIn directly + archive snapshots)
- Founders' / key execs' personal LinkedIn, Twitter, blogs, podcasts
- Glassdoor, Blind, AmbitionBox (India) — culture + hiring volume signals
- Conference speaker pages — where do execs show up

### N. Domain & infrastructure intel
- WHOIS — domain registration date, registrar
- DNS records — MX (email provider), TXT (verification trails reveal SaaS stack: HubSpot, Marketo, Intercom, Segment, etc.)
- SSL cert history (crt.sh)
- BuiltWith, Wappalyzer — analytics, marketing, payment, hosting stack
- SimilarWeb traffic estimates + top referrers
- Wayback Machine — earliest snapshot date, design evolution, copy evolution

### O. Vernacular / regional footprint (don't skip for India/SEA/LATAM/MENA)
- Hindi/Tamil/Bengali Twitter & YouTube
- Regional language blogs, newsletters
- WhatsApp/Telegram groups (search "[product] WhatsApp group")
- Regional press in Indian languages
- Local Reddit alternatives (e.g., r/IndiaSpeaks, r/developersIndia)

## Footprint inventory output template

```markdown
| # | Source | URL | Type | First seen | Last seen | Notes |
|---|--------|-----|------|-----------|-----------|-------|
| 1 | Domain WHOIS | — | Infra | 2022-03-14 | — | Registered via Namecheap, NS on Cloudflare |
| 2 | Product Hunt launch | https://... | Launch | 2022-09-08 | — | 1,247 upvotes, hunted by [name] |
| 3 | Twitter @company | https://... | Owned social | 2022-08-22 | 2026-04-30 | Created 2 weeks pre-launch; cadence ~3/wk |
| ... | | | | | | |
```

## What "done" looks like

- 25+ footprints catalogued (fewer is OK for very young or stealthy companies — note why)
- Every category above either populated or explicitly marked "no footprint found"
- Every entry has at minimum a URL and a first-seen date (or "undated" with reason)
- A 3-5 sentence "Discovery summary" noting which categories were richest, which were sparse, what surprised you
