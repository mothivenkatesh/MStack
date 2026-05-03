# PMM Agent OS — Product Vision

**Version:** 1.0
**Date:** April 9, 2026
**Author:** Mothi Venkatesh

---

## The One-Liner

**PMM Agent OS is the operating system for product marketing — 15 orchestrated AI agents that work together with persistent memory, so PMMs can shift from drowning in execution to orchestrating strategy.**

---

## The World Today (Problem)

Product marketing is broken. Not because PMMs lack talent — but because they lack systems.

### The Numbers

- **300,000+ PMMs globally.** 44% are teams of 1-2 people.
- **Product release cycles compressed from 6.4 weeks to 2.8 weeks.** Campaign timelines stayed at 8-12 weeks.
- **71% of PMMs** are expected to do more with less.
- **50%+** spend most of their time on execution, not strategy.
- **96% use AI tools.** But only **34%** use AI for strategic work.
- **72%** say AI output quality is inconsistent.
- The average PMM juggles **15+ disconnected tools** — Klue for CI, Jasper for content, Gong for call intel, Notion for docs, Confluence for launches, Highspot for enablement, spreadsheets for metrics — none of which talk to each other.

### What This Means

Every day, a solo PMM at a Series B startup wakes up and:

1. Manually checks 3 competitor websites for changes
2. Opens a stale battlecard in Google Docs and wonders if it's still accurate
3. Gets pinged by sales: "Can you hop on a call with a prospect comparing us to [competitor]?"
4. Opens ChatGPT, types "write me a LinkedIn post about our new feature," gets generic slop back
5. Spends 2 hours updating a launch tracker in a spreadsheet nobody reads
6. Misses a high-intent signal from a prospect who visited the pricing page 4 times this week
7. Gets asked by the VP of Sales: "What's the ROI of product marketing?" — and has no answer

**The tools exist. The system doesn't.**

AI made individual PMM tasks faster. But nobody built the connective tissue — the orchestration layer that links competitive intelligence to messaging to sales enablement to content to metrics in one persistent, context-aware system.

That's what we're building.

---

## The World We're Building (Vision)

### The Belief

> *"The PMM role is shifting from task execution to system design — 'orchestrating agents,' 'building systems.'"*
> — Fluvio 2025 PMM AI Trends Report (25% of PMMs independently arrived at this same insight)

We believe the future PMM doesn't write battlecards. They orchestrate a system that writes, updates, and distributes battlecards automatically — and measures whether sales actually uses them.

We believe the future PMM doesn't manually monitor competitors. They set up a signal network that detects changes, assesses impact, and triggers downstream updates across every asset that references that competitor.

We believe the future PMM doesn't spend Sunday night building a QBR deck. They review an auto-generated impact report that correlates their work to pipeline and win rates.

**PMM Agent OS makes this future real — today.**

### The Product

PMM Agent OS is an orchestrated multi-agent platform where **13 specialized AI agents share a persistent context graph** — your product knowledge, market intelligence, customer insights, brand voice, competitive landscape, and performance data.

Unlike ChatGPT or Claude (general-purpose, stateless, no workflow opinions), unlike Klue or Jasper (single-purpose, siloed), PMM Agent OS:

1. **Knows your world** — persistent memory of your product, market, competitors, personas, and brand voice that deepens over time
2. **Thinks in workflows, not prompts** — opinionated, methodology-driven flows (not "what do you want?" but "here's what great PMMs do, let me guide you through it")
3. **Chains actions across agents** — a competitor price change detected by the CI Agent automatically triggers the Positioning Agent to assess messaging impact, the Sales Enablement Agent to update battlecards, and the Alignment Agent to notify the sales team
4. **Learns what works for YOU** — tracks content performance, proposal win rates, and messaging effectiveness to continuously improve recommendations specific to your brand and audience
5. **Keeps humans in control** — configurable guardrails, confidence scoring, approval workflows, and escalation rules. PMMs are the "Head Coach," not passengers.

---

## The 14 Agents + Company Knowledge Base

> **Architecture:** Two foundation layers feed the Context Graph before any agent runs:
> - **Company KB** ("Agent Zero"): Company-level context — stage, GTM motion, brand, overall ICP, team structure. One per company.
> - **Product KB**: Per-product deep intelligence — features, architecture, pricing, use cases, product-specific ICP, competitive landscape, integration details, FAQs. One per product.
>
> Every specialized agent inherits both layers automatically. PMMs never re-explain their company or product — they go straight to strategy.
>
> See `pmm-agent-os-company-kb-spec.md` for the full onboarding and context-building spec.

### Embedded Methodology: The Frameworks That Power Every Agent

PMM Agent OS doesn't invent new methodology — it embeds the best frameworks from the practitioners who've proven them, making them executable at machine speed.

| Framework | Source | Where It's Embedded |
|---|---|---|
| **Positioning Anchors** (Market Elements x Product Elements) | FletchPMM (Pierri & Kaminski) | Positioning Agent |
| **Minimum Viable Positioning** (MVP Positioning pairs) | FletchPMM | Positioning Agent |
| **Four Positioning Questions** (What / Who / What it replaces / Why better) | FletchPMM | Positioning Agent |
| **Competitive vs. Contextual Differentiation** | FletchPMM | CI Agent, Positioning Agent |
| **3 Phases of Differentiation** (by market maturity) | FletchPMM | CI Agent, Positioning Agent |
| **ICP Scorecard** (Retention, Access, Sales Velocity, Activation) | FletchPMM | Research Agent, ICP workflows |
| **"Unit of Work" ICP methodology** (define ICP by what they DO, not demographics) | FletchPMM | Research Agent |
| **"Current Way" mapping** (what the customer does today before your product) | FletchPMM | Research Agent, CI Agent |
| **TAM Triangulation** ("TAM SAM SOM is broken" — go after reachable SOMs) | FletchPMM + bottom-up/top-down/analogy methods | Research Agent, Metrics Agent |
| **Value Proposition Messaging Canvas** | FletchPMM | Positioning Agent, Narrative Agent |
| **Capability-Market-Fit** (capabilities ≠ features ≠ benefits) | FletchPMM | Positioning Agent |
| **Obviously Awesome positioning framework** | April Dunford | Positioning Agent |
| **Content Playground** (depth x intent matrix) | Ashley Faus / Atlassian | Content Workflow Agent |
| **Launch Tiering** (Tier 1-4 with activity matrices) | Multiple (Spotify, Seismic, Superhuman) | Launch Planning Agent |
| **DACI decision framework** | Atlassian | Launch Agent, Alignment Agent |
| **Leading vs. Lagging indicators** | Rinita Datta / Splunk | Metrics Agent |
| **Hattie's 34 PMM OKRs + 6 anti-patterns** | productmarketers.com | Metrics Agent |
| **Message-market fit testing** | Rinita Datta, Wynter methodology | Positioning Agent |
| **"Right to Win" analysis** | Strategic consulting (BCG/McKinsey adapted for PMM) | Narrative Agent, Positioning Agent |
| **Narrative arc structures** (SCR, Minto Pyramid, StoryBrand) | Multiple | Narrative Agent |

---

### Core Strategic Agents

**1. Positioning & Messaging Agent**
*The strategist.*

The most methodology-dense agent in the system. Embeds multiple proven frameworks and guides PMMs through a structured process — not a blank prompt.

**Embedded Frameworks:**
- **FletchPMM's Positioning Anchors:** Maps your product across two dimensions — Market Elements (Persona, Company Type, Context, Problem) and Product Elements (Category, Capability, Feature, Benefit). Identifies which 1-3 elements to lead with as your primary and secondary anchors.
- **FletchPMM's Four Questions:** Forces clarity on: What is your product? Who is it for? What does it replace (the "current way")? Why is it better?
- **Minimum Viable Positioning:** For early-stage products, generates the minimum viable H1/H2 pairing — one market element + one product element — that can spread via word of mouth.
- **April Dunford's Obviously Awesome:** For more mature products, runs the full competitive alternatives → unique attributes → value → best-fit customers → market category flow.
- **FletchPMM's Value Proposition Messaging Canvas:** Documents capabilities against competitive weaknesses and maps benefits to specific blockers in customer use cases.
- **Competitive vs. Contextual Differentiation:** Auto-detects your market maturity phase and recommends the right differentiation mode. Early market = differentiate against the status quo ("current way"). Mature market = differentiate against named competitors.
- **Capability-Market-Fit:** Distinguishes between features, capabilities, and benefits. Tests whether the specific capability you're leading with is actually what the market cares about. Contrarian stance embedded: sometimes leading with capabilities/features is clearer than leading with abstract benefits.
- **"Right to Win" Analysis:** Evaluates your positioning against 5 dimensions — Do you have the product capability? The market credibility? The distribution access? The team expertise? The timing advantage? — to determine where your positioning is strongest and where it's aspirational.

**Messaging Pillars Generator:**
- Takes validated positioning and generates a structured messaging hierarchy:
  - **Level 1:** Brand-level message (overarching narrative)
  - **Level 2:** Product-level messages (by product/solution)
  - **Level 3:** Audience-level messages (by persona/segment)
  - **Level 4:** Channel-level messages (adapted for website, sales, social, events)
- Each pillar includes: the claim, the proof point, the customer language, and the competitive contrast
- Tests pillar resonance against synthetic ICP personas and recommends A/B variants

**"Framing the Need" Engine:**
- Before positioning your solution, you must frame WHY the prospect should care. This engine generates the "why change?" narrative that precedes any product pitch.
- Maps the prospect's current state (pain, inefficiency, risk) → the trigger event (what makes the status quo untenable NOW) → the desired future state → your product as the bridge.
- Uses FletchPMM's "current way" mapping to ground the need in what the prospect actually does today.

**"Spotting Insights" Module:**
- Surfaces non-obvious patterns from the Context Graph that can become positioning advantages:
  - "Your customers mention [specific pain] 4x more than your competitors' customers. This is an underexploited positioning angle."
  - "Competitor X is positioning around [theme], but their G2 reviews show customers actually care about [different theme]. Opportunity to counter-position."
  - "Three of your best customers came from [unexpected segment]. Your ICP may be wrong — here's the data."
- Generates weekly "Insight Briefing" that surfaces 3-5 actionable insights from across the Context Graph.

When the CI Agent detects a major competitive shift, this agent automatically reassesses: "Does our positioning still hold? Here's what changed, here's the FletchPMM differentiation phase we're in, and here's what I recommend."

Chained to: CI Agent (triggers on competitive shifts), Narrative Agent (feeds story arcs), Sales Enablement Agent (feeds messaging), Content Agent (feeds themes), Research Agent (receives customer language), Pricing Agent (aligned on value positioning)

**2. Competitive Intelligence Agent**
*The always-on radar.*

Continuously monitors competitor websites, G2/Capterra reviews, news sources, analyst reports, job postings, and pricing pages. Detects changes, assesses significance, and generates living battlecards that auto-update.

**Embedded Frameworks:**
- **FletchPMM's 3 Phases of Differentiation:** Classifies each competitor relationship by market maturity phase. Phase 1 (early market): your competitor is the status quo, not another product. Phase 2 (growing market): direct product-to-product differentiation. Phase 3 (mature market): ecosystem and trust differentiation.
- **"Current Way" Analysis:** For each competitor AND for the "do nothing" alternative, maps what the customer's workflow looks like today — because your real competitor is often the spreadsheet, not another SaaS product.

Doesn't just collect data — synthesizes it. "Competitor X just hired 12 enterprise AEs in EMEA and dropped their pricing by 15%. Here's what this likely means for your Q3 pipeline in that region. Based on our differentiation phase analysis, here's whether to respond on price or reframe on value."

**3. Launch Planning Agent**
*The project quarterback.*

Takes a product/feature brief and auto-tiers the launch (Tier 1-4, configurable to your framework — Spotify's "Headliner to Backstage," Seismic's "Go Big / Tell Sales / Tell CS," or your own). Generates the full activity plan, timeline, DACI assignments, and cross-functional checklist.

Knows the difference between a "release" and a "launch." Knows that Tier 1 needs press + social + newsletter + blog + events + paid + in-product, while Tier 4 needs a release note and a Slack message.

Pulls the Narrative Agent's story arc for each launch to ensure every launch tells a cohesive story, not just announces features.

**4. Sales Enablement Agent**
*The rep's secret weapon.*

Generates and maintains battlecards, one-pagers, talk tracks, objection handling guides, and demo scripts — all fed by real-time data from the CI Agent and Positioning Agent. When something changes upstream, assets update automatically.

Produces specific, concrete content — not fluffy marketing language. "When the prospect says they're evaluating [Competitor X], here's the exact question to ask that exposes their deployment limitation in multi-region setups." (Per Bhavika Thakkar/Microsoft: "specificity > fluffy language")

Tracks which assets reps actually use. Flags stale content before sales loses trust in it.

### Intelligence Agents

**5. Customer & Market Research Agent**
*The insight engine.*

The agent that makes ICP research, TAM sizing, and persona development data-driven and continuous — not a once-a-year exercise.

**ICP Research Module (Multi-Framework):**

The most methodology-rich ICP engine in any PMM tool — combines FletchPMM, Winning by Design, and practitioner methodologies into a guided, data-driven ICP process.

- **SPICED Diagnostic (Winning by Design):** For each customer segment, diagnoses across 5 dimensions:
  - **S**ituation: Facts, circumstances, and background details about the account type
  - **P**ain: The challenges they experience (functional + emotional)
  - **I**mpact: How your product impacts their business (quantified where possible)
  - **C**ritical Event: The trigger/deadline that drives them to buy NOW (funding round, compliance deadline, team growth, competitive threat)
  - **D**ecision: The process, committee, and criteria involved in purchasing
  - Agent auto-populates SPICED from Gong call data, CRM fields, and win/loss interviews. PMM reviews and refines.

- **ICP Scorecard (FletchPMM):** Rates every market segment across four dimensions — Retention (will they stick?), Access (can we reach them?), Sales Velocity (how fast do deals close?), Activation (how quickly do they get value?). Generates a prioritized segment ranking with risk/opportunity scores.

- **"Unit of Work" Analysis (FletchPMM):** Defines ICP not by demographics (company size, industry) but by whether the company actually DOES the work your product supports. "Similar-looking customers can have entirely different 'current ways,' making them different segments."

- **"Current Way" Mapping (FletchPMM):** For each ICP segment, maps the existing process/tool/workaround the customer uses today. This is the foundation for all positioning and competitive work.

- **Quantitative × Qualitative Triangulation (Winning by Design + Sonia Moaiery/Glassdoor):**
  - **Quantitative layer:** Cross-references firmographic traits (industry, revenue, employee size, growth rate) with lifetime revenue, retention, product usage, and technographic data to find which traits predict successful customers. Detects hidden attributes that matter (e.g., "distributed office environment" as a predictor, not just industry).
  - **Qualitative layer:** Guided listening-first research process:
    1. Start with 5-10 analyst/thought leader deep dives to understand category language
    2. Interview 5-10 most successful customers (deepest product usage)
    3. Run parallel conversations with Sales, CS, and prospects (80/20 prospect-to-customer ratio)
    4. Block 15 min after each conversation to capture top 2-3 takeaways
    5. Share real-time insights with a core team to reconcile conflicting signals
    6. Wait for themes to emerge (don't share with executives until you have pattern confidence)
    7. Validate initial hypotheses — which assumptions were confirmed vs. overturned?
  - Agent auto-generates interview guides, screener questions, and theme-tracking dashboards. Synthesizes across all conversations to surface patterns.

- **Segment-Level Persona Typing (Sonia Moaiery/Glassdoor):**
  - Beyond firmographics, identifies behavioral segmentation questions — "3 questions that can type someone into a segment." Example: maturity level in a specific domain (e.g., employer branding maturity at Glassdoor).
  - These typing questions can be embedded in onboarding flows, qualifying forms, or CS intake to auto-classify accounts as ICP match or non-match.
  - Agent recommends segment typing questions based on your product's value drivers.

- **ICP Output Architecture (Sonia Moaiery):**
  - Separates ICP research into two distinct deliverables:
    1. **Research & Insights Report:** How we got here, who we talked to, methodology, implications for the business. Shared with executives so they can make informed decisions across their functions.
    2. **ICP One-Pager:** Company-level profile (size, industry, titles of buyer/champion/end-user) + per-persona one-pagers. Shared with marketing, sales, CS, support, implementation, AND contractors (designers, copywriters) who represent your brand.
  - Agent auto-generates both deliverables and recommends distribution list (including often-forgotten teams: customer support, implementation, contractors).

- **Reverse-ICP from Value Prop (FletchPMM):** Uses your validated value proposition to reverse-engineer who your ICP actually is — working backwards from "who would care most about this specific capability?"

- **3-5 Segment Documentation (Winning by Design):** Produces a summary of 3-5 top segments within your ICP that have unique, differentiated pain points — making the ICP actionable for GTM teams while providing profiles around which to align content, discovery, and customer stories.

**TAM Sizing with Triangulation:**
- Rejects naive TAM/SAM/SOM (per FletchPMM: "TAM SAM SOM is broken"). Instead uses three-method triangulation:
  - **Bottom-up:** Count actual addressable accounts by segment × ACV × penetration rate
  - **Top-down:** Industry analyst data (Gartner, Forrester, MarketsandMarkets) → your category share → addressable slice
  - **Analogy:** Compare to similar products/markets at the same stage for reality-check sizing
- Generates a **"Reachable Greens" analysis** (FletchPMM concept): instead of chasing the full TAM, identifies the specific SOM segments where prospects are most willing to buy NOW, then sequences expansion from there.
- Auto-validates TAM estimates against real pipeline data, win rates, and market signals from the Signal Activation Agent.
- Visualizes the sequential GTM path: "Start here (SOM) → expand here (SAM) → eventually here (TAM)" with data backing each stage.

**Persona Development:**
- Not a standalone agent but a capability woven through the Research Agent. Every agent reads from and writes to living persona documents — updated continuously from call recordings, survey data, win/loss patterns, and content engagement data.
- Personas include FletchPMM's "unit of work" and "current way" for each segment.
- Personas are never stale because they're fed by real behavioral data, not annual research projects.

Ingests call recordings (Gong/Chorus), survey data, review sites, support tickets, and community discussions. Synthesizes themes, extracts pain points in the customer's own language, identifies patterns, and builds living persona updates.

"Across 47 sales calls this month, 'time to value' was mentioned 3.2x more than last month. Here are the 5 most common contexts and what this means for your onboarding messaging."

Chained to: Positioning Agent (feeds customer language + ICP data), CI Agent (feeds "current way" mapping), Pricing Agent (feeds willingness-to-pay signals), Narrative Agent (feeds customer stories + pain points)

**6. Signal Activation Agent**
*The intent radar.*

Captures and activates buyer intent signals across three layers:

- **1st Party:** Website behavior, product usage, CRM data, support tickets. Scores PQLs, detects expansion signals, flags churn risk.
- **2nd Party:** G2/Capterra comparison activity, partner ecosystem engagement, community sentiment shifts.
- **3rd Party:** Bombora intent data, LinkedIn signals, job postings (hiring signals), funding rounds, technographic changes.

Unifies all signals into account-level scores and routes to the right action: SDR outreach for high-intent unknowns, CS expansion play for existing customers showing new signals, marketing nurture for early-intent accounts.

### Content & Revenue Agents

**7. AI Content Workflow Agent**
*The content factory that actually knows what works.*

Not another AI writing tool. A system trained on high-performing content patterns across specific channels:

- **LinkedIn:** Hook structures, carousel formats, engagement patterns that drive reach for B2B
- **Reddit:** Subreddit-specific norms, authenticity-first tone, community-native framing
- **X/Twitter:** Thread mechanics, viral hooks, B2B thought leadership formats
- **Instagram:** Carousel best practices, Reels scripts, visual-first B2B storytelling
- **Landing Pages:** Above-the-fold conversion patterns, A/B test winner structures. Embeds FletchPMM's 7-step homepage messaging process (Hero → Problem → Solution Intro → Value Props → Proof → CTA).
- **Battlecards:** Competitive positioning patterns that actually close deals
- **Pitch Decks:** Narrative arcs by purpose (investor, customer, internal strategy)

Includes 8 specialized workflows — from LinkedIn Engine to Multi-Channel Campaign Orchestrator. Every piece of content is optimized for the specific platform AND your specific audience, learned from your own performance data over time.

Pulls messaging pillars from Positioning Agent and story arcs from Narrative Agent to ensure every piece of content ladders up to the same strategic narrative.

**8. Media Proposal Generator Agent**
*The deal accelerator.*

Turns 4-6 day manual proposal cycles into sub-24-hour personalized proposals. Codifies senior seller pricing/packaging wisdom so junior reps perform like veterans.

Ingests the buyer brief, pulls account context and competitive intelligence, recommends optimal pricing/packaging combinations (good/better/best), generates a personalized narrative that leads with the buyer's business problem, and assembles a presentation-ready proposal with ROI calculator.

Tracks proposal-to-close conversion rates by template, pricing structure, and narrative approach. Continuously improves.

Works in tandem with the Pricing Agent (pulls current pricing models and package structures) and Narrative Agent (uses the right story arc for the buyer's stage and persona).

### Narrative & Pricing Agents

**9. Narrative Agent** *(NEW)*
*The storyteller-in-chief.*

Every great PMM knows: **features tell, stories sell.** The Narrative Agent builds and maintains the overarching story that connects everything — from the company's "why" to each product's value to every piece of content and every sales conversation.

**What It Does:**

- **Company Narrative Architecture:** Builds a layered narrative structure:
  - **Origin Story:** Why your company exists — the founder insight, the market gap, the "aha moment" (per FletchPMM: "Nobody cares about your vision — they care about the problem you saw that nobody else did")
  - **Market Narrative:** The big shift happening in the world that makes your product necessary NOW. Not your product story — the MARKET story that your product rides. ("Framing the Need" — why should anyone care before you even mention your product?)
  - **Product Narrative:** How your product uniquely solves the problem created by the market shift
  - **Customer Narrative:** Stories of real customers whose world changed because of your product
  - **Future Narrative:** Where the market is going and why your company is best positioned to lead

- **"Framing the Need" Engine:**
  - Before you can sell a solution, you must sell the problem. This module generates the "why change?" story that precedes any product pitch.
  - Structure: Current State (what the world looks like today, with all its inefficiencies) → Trigger (what's changing that makes the status quo untenable) → Consequence (what happens if you don't adapt) → New Way (the category/approach that solves it) → Your Product (why you're the best version of the new way)
  - Uses data from the Research Agent (customer pain points), CI Agent (market shifts), and Signal Agent (trigger events) to keep the narrative grounded in reality, not aspirational fluff.

- **"Right to Win" Analysis:**
  - For every market you enter and every narrative you tell, validates whether you have the RIGHT to make that claim:
    - **Product Right:** Does your product actually deliver on the promise? (pulls from product analytics, NPS, adoption data)
    - **Credibility Right:** Do you have the customer proof, analyst recognition, and market presence to be believed? (pulls from case studies, G2 ratings, analyst mentions)
    - **Distribution Right:** Can you actually reach the audience you're claiming? (pulls from channel performance, pipeline data)
    - **Team Right:** Does your team have the domain expertise to be trusted? (founder background, team credentials)
    - **Timing Right:** Is the market ready for this narrative? Too early = no demand. Too late = commoditized.
  - Flags narratives where the "right to win" is weak: "You're positioning as the enterprise leader, but your largest customer is 200 employees. Recommend softening to 'built for growing teams' until you have 3+ enterprise logos."

- **"Spotting Insights" Module:**
  - Surfaces non-obvious narrative angles from across the Context Graph:
    - Customer language patterns that reveal untold stories
    - Market data that contradicts conventional wisdom
    - Competitor blind spots that create narrative openings
    - Emerging themes from sales calls that could become thought leadership
  - Weekly "Insight Briefing" with 3-5 narrative opportunities ranked by potential impact

- **Narrative Consistency Engine:**
  - Ensures every piece of content, every sales deck, every launch announcement, every social post tells a coherent story that ladders up to the same master narrative
  - Flags inconsistencies: "Your LinkedIn post is leading with 'ease of use' but your sales deck leads with 'enterprise security.' These are different narratives targeting different buyers. Intentional or misaligned?"
  - Adapts the narrative by audience without losing coherence — the CEO hears the market narrative, the practitioner hears the product narrative, the CFO hears the ROI narrative — but they all connect

- **Story Arc Library:**
  - Pre-built narrative structures for common PMM scenarios:
    - **Launch Story:** Problem → Solution → Proof → Excitement → CTA
    - **Competitive Displacement Story:** Status Quo Pain → Why Current Solution Fails → New Approach → Your Product → Customer Proof
    - **Category Creation Story:** Market Shift → New Category Definition → Why Now → Your Leadership Position
    - **Customer Success Story:** Before State → Challenge → Discovery → Implementation → Results → Future
    - **Investor/Board Story:** Market Opportunity → Unique Insight → Product → Traction → Vision
    - **Internal Rally Story:** Where We've Been → Where We Are → Where We're Going → What We Need From You
  - Each arc can be applied to any content format (deck, blog, email, video script, landing page)

Chained to: Positioning Agent (receives positioning anchors and messaging pillars), Research Agent (receives customer stories and market data), CI Agent (receives competitive landscape), Content Workflow Agent (feeds story arcs for every content piece), Launch Agent (provides launch narrative), Proposal Agent (provides deal narratives), Alignment Agent (ensures consistent storytelling across teams)

**10. Product Pricing Agent** *(NEW)*
*The value architect.*

Pricing and packaging is one of the highest-leverage PMM activities — yet most PMMs do it based on gut feel, a competitor comparison spreadsheet, and a prayer. This agent brings data, frameworks, and continuous optimization to pricing decisions.

**What It Does:**

- **Pricing Research & Analysis:**
  - **Willingness-to-Pay (WTP) Analysis:** Designs and analyzes Van Westendorp price sensitivity surveys, Gabor-Granger studies, and conjoint analyses. Pulls WTP signals from sales conversations (via Gong integration) — "when prospects push back on pricing, what specific objection do they raise? At what price point do deals stall?"
  - **Competitive Pricing Intelligence:** Continuously monitors competitor pricing pages, G2/Capterra mentions of pricing, and sales call recordings where competitors' pricing is discussed. Maintains a living competitive pricing matrix.
  - **Value Metric Identification:** Analyzes product usage data to identify the metric that best correlates with customer value (per-seat, per-usage, per-outcome, per-feature). "Your customers who use [Feature X] are 3.2x more likely to expand. This suggests [Feature X usage] is a better value metric than seat count."

- **Package Design & Optimization:**
  - **Good/Better/Best Packaging:** Generates tiered package recommendations based on: customer segment needs, feature usage patterns, competitive packaging, and willingness-to-pay data. Each tier is mapped to a specific persona and use case.
  - **Feature Gating Recommendations:** Analyzes which features drive conversion (should be in free/lower tiers) vs. which features drive expansion (should be gated to higher tiers). "Feature Y is used by 89% of customers who upgrade. Recommend keeping it in the Pro tier as the primary upgrade trigger."
  - **Add-on & Module Strategy:** Identifies opportunities for add-on products/modules that serve specific segments without complicating the core packaging.
  - **Freemium/Trial Optimization:** If PLG, recommends optimal free tier boundaries, trial lengths, and conversion triggers based on product usage data and industry benchmarks.

- **Pricing Scenario Modeling:**
  - **Impact Simulation:** "If we raise prices by 15%, here's the projected impact on conversion (based on WTP data), churn (based on price sensitivity by segment), and revenue (net effect)."
  - **Competitive Response Modeling:** "If Competitor X drops pricing by 20% (which the CI Agent just detected), here are 3 response scenarios with projected outcomes."
  - **Expansion Revenue Modeling:** Projects revenue from upsell/cross-sell based on current adoption patterns and pricing structure.
  - **New Market Pricing:** When entering a new segment or geography, models optimal pricing based on local competitive data, purchasing power, and willingness-to-pay benchmarks.

- **Pricing Enablement:**
  - Generates pricing talk tracks for sales: how to present pricing, handle objections, justify premium, and navigate discounting conversations.
  - Creates ROI calculators customized by persona and use case.
  - Builds pricing comparison pages (your product vs. competitors) with honest, data-backed positioning.
  - Generates internal pricing guides with discount authority levels and approval workflows.

- **Continuous Pricing Intelligence:**
  - Tracks pricing page conversion rates, trial-to-paid rates, expansion rates, and churn rates by pricing tier.
  - Detects pricing anomalies: "Churn in the Enterprise tier jumped 23% this month. 4 of 6 churned accounts cited 'not enough value for the price' in exit surveys. Recommend reviewing Enterprise packaging."
  - Quarterly "Pricing Health Report" with recommendations for optimization.

Chained to: CI Agent (competitive pricing data), Research Agent (WTP signals from customer conversations), Signal Activation Agent (pricing page behavior, expansion signals), Metrics Agent (pricing impact on revenue), Proposal Agent (pulls current pricing models for proposals), Positioning Agent (ensures pricing aligns with value positioning)

### Operational Agents

**11. Metrics & Attribution Agent**
*The proof machine.*

The agent that answers "What's the ROI of product marketing?" with data, not hand-waving.

**Embedded Frameworks:**
- **Hattie's 34 PMM OKRs** (productmarketers.com): Pre-loaded as selectable OKR templates. PMMs pick which ones they're tracking, and the agent auto-measures progress. Includes the 6 anti-patterns (vanity metrics to avoid).
- **Leading vs. Lagging Indicators** (Rinita Datta/Splunk): Every metric is classified as leading (predictive: sales confidence, enablement usage) or lagging (outcome: win rate, ARR). The agent prioritizes surfacing leading indicators so PMMs can course-correct before it's too late.
- **TAM Triangulation Tracking:** Validates market sizing assumptions against real pipeline and win rate data. "Your original TAM estimate was $50M. Based on 6 months of pipeline data, the addressable market for your current ICP is closer to $32M. Here's where the gap is and which segments to expand into."

Correlates PMM activities to business outcomes. Generates launch retrospectives, QBR slides, and impact dashboards.

"Your Tier 1 launch drove 847 landing page visits, 12% demo conversion (vs 8% baseline), and influenced $2.3M in pipeline across 23 accounts. Battlecard usage was 67% among reps who closed deals vs 31% among those who didn't."

**12. Cross-Functional Alignment Agent**
*The communication multiplier.*

Generates stakeholder-specific updates (the VP of Sales doesn't need the same update as the content team). Syncs priorities across PM, Sales, DemandGen, and CS. Manages information flow so the PMM doesn't spend half their calendar in alignment meetings.

Auto-generates weekly status updates, launch readiness summaries, and priority alignment briefs — each tailored to the recipient's role and information needs.

Uses the Narrative Agent's story arcs to ensure internal communications tell a coherent story, not just report status.

**13. Persona Intelligence Agent** *(Upgraded from embedded capability to standalone agent)*
*The living persona engine.*

Traditional personas are PDFs that rot in Google Drive. This agent builds, maintains, and activates **living personas** that auto-update from real data and feed every other agent in the system.

**What Makes This Different from GTMBuddy's Persona Intelligence:**

GTMBuddy's model is sales-rep-facing — it auto-surfaces persona cards during deals. PMMStudio's Persona Agent is **PMM-facing** — it helps PMMs BUILD the personas through research, then keeps them alive with real data, then activates them across every PMM workflow (positioning, content, launches, enablement, pricing, narrative).

| GTMBuddy Persona Intelligence | PMMStudio Persona Intelligence Agent |
|---|---|
| Maps job titles to pre-built persona profiles | Builds personas from scratch using research methodology |
| Surfaces persona cards to sales reps in CRM | Feeds persona context to ALL 14 other agents |
| Static persona pages (goals, challenges, pitches) | Living personas that auto-update from Gong, CRM, analytics, reviews |
| Identity defined by role/KPI/pain | Identity defined by unit of work + current way + buying triggers + identity transitions |
| Activated in sales workflow | Activated across positioning, content, launches, enablement, pricing, narrative |

**Core Capabilities:**

*Persona Research & Creation:*
- **Guided persona builder:** Walks PMMs through a structured process to build personas from scratch. Shows examples at every step. Uses FletchPMM's "unit of work" methodology — defines personas by what they DO, not just their title.
- **SPICED diagnostic per persona:** Maps each persona's Situation, Pain, Impact, Critical Event, and Decision criteria (Winning by Design).
- **"Current way" mapping:** For each persona, documents what they do TODAY without your product — their workflows, tools, workarounds, and pain points. This is the foundation for competitive positioning.
- **Identity transition mapping** (inspired by GTMBuddy's concept but adapted for PMM): Tracks not just who the persona IS but who they're BECOMING. Example: "The VP of Data Engineering is transitioning from 'pipeline builder' to 'data platform architect.' Our product accelerates this transition by eliminating manual ETL."
- **Buying committee mapping:** Maps the full buying committee — buyer (signs the check), champion (shepherds internally), end user (uses daily), blocker (can kill the deal), influencer (shapes opinion). Each gets their own persona profile.
- **Anti-persona definition:** Explicitly defines who is NOT your ICP — segments that look attractive but won't succeed with your product. Prevents wasted sales and marketing effort.
- **Developer persona framework:** For dev-tool companies — 13 developer archetypes mapped to awareness levels (Developer Marketing Alliance methodology), with channel preferences (Stack Overflow, HackerNews, GitHub, Discord) and content format preferences.

*Persona Enrichment (Living Data):*
- **Gong/Chorus integration:** Auto-extracts customer language, pain points, objection patterns, and buying signals from sales calls. Continuously updates persona profiles with real customer words — not marketing guesses.
- **CRM pattern analysis:** Identifies which persona types convert fastest, have highest ACV, expand most, and churn least. Updates persona priority scores.
- **Product analytics integration:** Maps persona types to product usage patterns — which personas activate fastest, use which features, and get the most value.
- **G2/Capterra review mining:** Extracts persona-specific sentiment from reviews — what each persona type loves and hates about your product vs competitors.
- **Support ticket analysis:** Identifies persona-specific pain points and confusion patterns from support data.
- **Community listening:** Monitors Reddit, LinkedIn, Slack communities for persona-relevant discussions and language patterns.

*Persona Activation (Feeding Every Agent):*
- **Positioning Agent:** Persona data informs messaging — which pain points to lead with, which language to use, which proof points matter per persona.
- **CI Agent:** Persona data determines which competitive angles matter — the CTO cares about security, the developer cares about DX, the CFO cares about ROI.
- **Content Agent:** Generates persona-specific content variants — same topic, different angle for each persona.
- **Sales Enablement Agent:** Creates persona-specific talk tracks, objection handling, and discovery questions.
- **Launch Agent:** Determines which personas to target at each launch tier.
- **Narrative Agent:** Adapts the story arc for each persona — the practitioner gets the product narrative, the executive gets the market narrative.
- **Pricing Agent:** Feeds willingness-to-pay signals per persona segment.
- **Signal Agent:** Persona typing applied to intent signals — high-intent CTO vs high-intent developer get different activation paths.
- **Proposal Agent:** Personalizes proposals based on the specific personas in the buying committee.
- **RFP Agent:** Adapts RFP response language to the expected reader persona.

*Persona Typing & Segmentation:*
- **Segment typing questions:** Generates 3-5 questions that can classify any prospect into a persona segment (Sonia Moaiery/Glassdoor methodology). These can be embedded in onboarding flows, qualification forms, or CS intake.
- **Title-to-persona mapping:** Maintains a database of job titles mapped to persona types (similar to GTMBuddy but PMM-managed, not pre-built). PMMs define the mapping; the system scales it.
- **Behavioral typing:** Beyond title/firmographic matching — uses product usage patterns, content engagement, and buying behavior to dynamically reclassify personas.

*Persona Health & Reporting:*
- **Persona freshness score:** Each persona profile shows when it was last updated and from which data sources. Flags stale personas (>90 days without enrichment).
- **Persona coverage dashboard:** Shows which personas have strong profiles and which have gaps. "Your 'Developer' persona is 92% complete. Your 'CFO Buyer' persona is only 34% — recommend 3 CFO customer interviews."
- **Persona performance report:** Correlates persona targeting with business outcomes. "Deals targeting the 'Platform Engineer' persona close 2.3x faster than 'IT Director' persona. Consider reallocating enablement focus."

Chained to: ALL agents. The Persona Agent is the second most connected agent after the Context Engine — every agent reads persona data, and several write back enrichment data.

---

## The Context Graph (The Moat)

All 15 agents share a persistent knowledge layer — the Context Graph — that accumulates and deepens over time:

```
Context Graph
|
+-- Product Knowledge
|   Features, roadmap, technical specs, value propositions,
|   pricing & packaging, rate cards
|
+-- Market Knowledge
|   Competitor profiles & changes, market trends, analyst reports,
|   win/loss patterns, competitor pricing intel, market maturity phase
|
+-- Customer Knowledge (FletchPMM methodology)
|   Living personas (unit of work + current way + ICP scorecard),
|   voice of customer (language, pain points), customer journey maps,
|   account-level intent scores, willingness-to-pay signals
|
+-- Brand Knowledge
|   Brand voice guidelines, messaging hierarchy, messaging pillars,
|   visual brand rules, channel-specific tone profiles
|
+-- Narrative Intelligence
|   Master narrative (market + product + customer stories),
|   "right to win" scores per market, story arc templates,
|   narrative consistency map, insight briefings
|
+-- Positioning Intelligence (FletchPMM methodology)
|   Positioning anchors (market elements x product elements),
|   MVP positioning pairs, competitive vs contextual differentiation mode,
|   value proposition canvas, capability-market-fit scores
|
+-- Pricing Intelligence
|   Willingness-to-pay data, competitive pricing matrix,
|   package structures (good/better/best), value metric analysis,
|   pricing scenario models, feature gating recommendations
|
+-- Signal Intelligence
|   1st/2nd/3rd party signals, unified account scores,
|   intent trends, trigger events
|
+-- Content Intelligence
|   High-performing patterns by channel, your performance history,
|   audience engagement patterns, format & timing optimization
|
+-- Deal Intelligence
|   Winning proposal patterns, pricing/packaging playbooks,
|   proposal-to-close data, buyer segment preferences
|
+-- ICP & TAM Intelligence (FletchPMM methodology)
|   ICP scorecard (retention, access, velocity, activation),
|   TAM triangulation (bottom-up, top-down, analogy),
|   "reachable greens" SOM analysis, GTM sequencing map,
|   segment prioritization with risk/opportunity scores
|
+-- Performance Knowledge
    Launch metrics, content performance by channel,
    enablement effectiveness, signal-to-pipeline conversion,
    proposal win rates, pricing health metrics, OKR tracking
```

### The Company Knowledge Base: How Every Agent Gets Context

A critical architectural question: **How does any agent think properly without knowing the context of the company?**

The answer is the **Company KB** — a structured onboarding layer that feeds the Context Graph before any agent runs. This is NOT a separate agent. It's the **foundation layer** that every agent reads from. Think of it as "Agent Zero" — the context that makes every other agent smart.

**Company KB Onboarding (First-Time Setup):**

When a new team onboards, they go through a guided setup that populates the Context Graph's foundational knowledge:

```
COMPANY KB ONBOARDING FLOW (30-60 minutes)
│
├── 1. COMPANY CONTEXT
│   ├── Company name, stage (seed/A/B/C/growth/enterprise)
│   ├── Industry/vertical
│   ├── Business model (SaaS, marketplace, PLG, sales-led, hybrid)
│   ├── GTM motion (self-serve, sales-assisted, enterprise, channel)
│   ├── Key metrics (ARR, users, growth rate, NDR, ACV)
│   ├── Team size and structure (PMM team, PM team, sales team)
│   └── Upload: pitch deck, about page URL, investor deck (optional)
│
├── 2. PRODUCT CONTEXT
│   ├── Product name(s) and descriptions
│   ├── Key features and capabilities
│   ├── Product category (existing or creating new)
│   ├── Pricing model and tiers (current)
│   ├── Product roadmap highlights (next 2-3 quarters)
│   └── Upload: product docs, feature specs, PRDs
│
├── 3. CUSTOMER CONTEXT
│   ├── Current ICP definition (or "we don't have one yet")
│   ├── Key personas (buyer, champion, end-user)
│   ├── Top 5-10 customer names and why they're great
│   ├── Top 3-5 use cases
│   ├── Customer language (how they describe the problem/solution)
│   └── Upload: existing persona docs, case studies, win/loss reports
│
├── 4. COMPETITIVE CONTEXT
│   ├── Top 3-5 competitors (names + URLs)
│   ├── How you typically win against each
│   ├── How you typically lose against each
│   ├── "Current way" — what do prospects do BEFORE your product?
│   └── Upload: existing battlecards, competitive analyses
│
├── 5. BRAND CONTEXT
│   ├── Brand voice (formal/casual, technical/accessible, etc.)
│   ├── Brand values and tone guidelines
│   ├── Visual brand guidelines (optional)
│   └── Upload: brand guide, style guide, existing messaging docs
│
├── 6. EXISTING ASSETS (optional but powerful)
│   ├── Current messaging/positioning docs
│   ├── Current sales deck
│   ├── Current website URL (auto-scraped for messaging analysis)
│   ├── Existing content library
│   └── CRM/Gong connection (if ready)
│
└── 7. GOALS & PRIORITIES
    ├── Top 3 company priorities this quarter
    ├── Top 3 PMM priorities this quarter
    ├── Key launches planned
    └── Biggest open questions / challenges
```

**How It Works:**

1. **PMM completes onboarding** (guided, can be done in stages — minimum viable setup takes 15 minutes)
2. **Company KB auto-populates the Context Graph** across all knowledge layers
3. **Every agent inherits this context automatically** — the Positioning Agent knows your ICP before you ask it to write positioning; the CI Agent knows your competitors before you ask it to monitor them; the Narrative Agent knows your brand voice before it writes a word
4. **Context deepens over time** — as agents run, they write back to the Context Graph. The CI Agent enriches competitive context. The Research Agent enriches customer context. The Metrics Agent enriches performance context. The Company KB is the seed; the Context Graph is the growing tree.

**Auto-Enrichment from Connections:**
- Connect your website → agent auto-extracts current messaging, positioning, and product descriptions
- Connect CRM → agent auto-identifies top customers, deal patterns, win/loss reasons, ICP characteristics
- Connect Gong → agent auto-extracts customer language, pain points, competitive mentions, objection patterns
- Connect product analytics → agent auto-identifies key usage patterns, activation metrics, expansion signals

**The "Cold Start" Problem Solved:**
Without the Company KB, every agent prompt would start with "tell me about your company, your product, your customers..." — that's ChatGPT. With the Company KB, every agent already knows who you are, what you sell, who you sell to, and what you're trying to achieve. The PMM goes straight to strategy, not setup.

**This is the moat.** The longer a PMM team uses the system, the smarter every agent becomes about their specific product, market, audience, and what works. Switching costs compound over time — not because we lock customers in, but because the system becomes genuinely irreplaceable.

---

## Embedded Template Library: Real Frameworks from Top PMMs

Every agent ships with battle-tested templates sourced from PMM leaders at the world's best companies. These aren't generic — they're the actual frameworks used at scale. PMMs can use them as-is, customize them, or let agents auto-populate them with data from the Context Graph.

### Positioning & Messaging Templates

| Template | Source | Embedded In |
|---|---|---|
| **Message House** (Roof + 3 Value Pillars + Pain Quotes + Proof Points) | Atlassian | Positioning Agent |
| **Persona-Driven Messaging Architecture** (Audience → Pain → Unique Focus → Value Pillars → Proof) | Algolia / Reshma Iyer | Positioning Agent |
| **Layered Messaging Framework** (L1 Product-Level + L2 Audience-Feature-Level) | Shopify / Stephanie Kelman | Positioning Agent |
| **Full-Stack Messaging Doc** (Market Insights → ICP → Personas → Competitive → Positioning Statement → External Messaging → Persona Messaging → Customer Stories → Production Deliverables) | SurveyMonkey / Mike Greenberg | Positioning Agent |
| **Positioning Canvas** (Vision → Audience → Insight/"Why Now" → Positioning Statement → 3 Key Messages → RTBs → Features) | Nikhil Balaraman / Pomerium | Positioning Agent |
| **Value Proposition Messaging Canvas** (Capabilities vs. Competitive Weaknesses, Benefits vs. Blockers) | FletchPMM / Pierri & Kaminski | Positioning Agent |
| **Minimum Viable Positioning** (4 Common Pairs: Market Element + Product Element) | FletchPMM | Positioning Agent |
| **Positioning Statement Framework** (Target + Category + Differentiator + Payoff) | PMA / Daniel Kuperman & Lara McCaskill | Positioning Agent |

### Narrative & Storytelling Templates

| Template | Source | Embedded In |
|---|---|---|
| **Hero's Journey for PMM** (Hero → Villain/Conflict → Impact → Adaptation → Victory → Theme → CTA) | BILL / Charles Tsang | Narrative Agent |
| **Story Inputs Canvas** (Audience + Functional Pain + Emotional Pain + Journey Stage + Market Context + Solution + Value Prop + Rational Hook + Emotional Hook + Proof Points) | BILL / Charles Tsang | Narrative Agent |
| **5-Layer Narrative Architecture** (Origin → Market → Product → Customer → Future) | PMM Agent OS native | Narrative Agent |
| **"Framing the Need" Arc** (Current State → Trigger → Consequence → New Way → Your Product) | PMM Agent OS + FletchPMM "Current Way" | Narrative Agent |
| **6 Story Arc Templates** (Launch, Competitive Displacement, Category Creation, Customer Success, Investor/Board, Internal Rally) | PMM Agent OS native | Narrative Agent |

### Launch Planning Templates

| Template | Source | Embedded In |
|---|---|---|
| **T-Minus Week SLA Tracker** (T-12 Positioning → T-10 Messaging → T-8 Marketing Plan → T-0 Launch) with embedded RACI | Amazon AWS / Kate Hodgins | Launch Planning Agent |
| **Tiered GTM Execution Plan** (Tier 1/2 × High/Med/Low Impact matrix with Gantt-chart activity trackers for Product Readiness + Customer Comms + Market Launch + Post-Launch Measurement) | SurveyMonkey / Morgan Lehman | Launch Planning Agent |
| **Product Launch Readiness Checklist** (Stakeholder Approval → Pricing → Legal → Metrics → Marketing → Support → Engineering → Data → Developer Experience) | Shopify / Stephanie Kelman | Launch Planning Agent |
| **Launch Tier Configurator** (Tier 1-4 with configurable activity matrices — supports Spotify "Headliner to Backstage," Seismic "Go Big/Tell Sales/Tell CS," or custom) | Multiple sources | Launch Planning Agent |

### Research & ICP Templates

| Template | Source | Embedded In |
|---|---|---|
| **Qualitative Research Planner** (Target Customer → Objective → Expected Actions → Approach → Screener → Questionnaire → Team Alignment) | Zoom / Sharon Markowitz | Research Agent |
| **ICP Scorecard** (Retention × Access × Sales Velocity × Activation per segment) | FletchPMM | Research Agent |
| **Developer Persona Framework** (13 Archetypes × Awareness Levels + Technical Role Taxonomy + Content Mapping + Community Platform Mapping) | Developer Marketing Alliance | Research Agent |
| **TAM Triangulation Worksheet** (Bottom-up + Top-down + Analogy methods with "Reachable Greens" SOM analysis) | FletchPMM + PMM Agent OS | Research Agent |
| **SPICED ICP Diagnostic** (Situation + Pain + Impact + Critical Event + Decision per segment, with quantitative × qualitative triangulation) | Winning by Design | Research Agent |
| **ICP Research Playbook** (Listening-first methodology: analysts → top customers → parallel Sales/CS/prospect interviews → theme validation → dual output: Insights Report + ICP One-Pager) | Sonia Moaiery / Glassdoor | Research Agent |

### Stakeholder Management Templates

| Template | Source | Embedded In |
|---|---|---|
| **DIN Framework** (Decide/Input/Notify stakeholder matrix + Workback Schedule + Weekly Forum Tracker) | Google / Pratik Gadamasetti (YouTube Shorts) | Alignment Agent |
| **Campaign RACI Matrix** (20+ functional roles × deliverables with stage-gated approval checkpoints) | Databricks / Kelley Sandoval | Alignment Agent, Launch Agent |
| **DACI Framework** (Driver/Approver/Contributor/Informed) | Atlassian | Alignment Agent |

### PMM Operations Templates

| Template | Source | Embedded In |
|---|---|---|
| **PMM Internal Roadmap** (Quarterly Gantt by workstream: Market Analysis → Persona Research → Positioning → GTM Plan → Collateral → Enablement → Launch → Feedback → Iterations) | DataDab | Alignment Agent |
| **PMM OKR Library** (34 OKRs across Core PMM + Sales Enablement + 6 Anti-Patterns) | Hattie the PMM / productmarketers.com | Metrics Agent |

### AI Assistant Configuration Templates

| Template | Source | Embedded In |
|---|---|---|
| **10 PMM GPT Templates** (Market Research, Competitive Analysis, Customer Insights, Persona Messaging, Industry Messaging, Thought Leadership, Product Knowledge, Content, Demo Script, Sales Enablement — each with JTBD, Instructions, Knowledge Base spec) | Claudia Michon / Automation Anywhere | Platform-level (for custom agent creation in Phase 4 marketplace) |

### How Templates Work in the Product

Templates are not static documents — they're **executable scaffolds** that agents auto-populate:

1. **PMM selects a template** (e.g., "Atlassian Message House") when starting a positioning project
2. **Agents auto-fill** what they can from the Context Graph (existing personas, competitive data, customer language, product info)
3. **PMM reviews, edits, and approves** the pre-populated template
4. **The completed template becomes a living document** — connected to the Context Graph, auto-updating when underlying data changes
5. **Templates are customizable** — PMMs can modify any template or create their own, which are saved to their team's library

This is the "opinionated but flexible" philosophy in action: the system guides you through proven frameworks, but never locks you in.

---

## Human-in-the-Loop: The "Head Coach" Architecture

PMM Agent OS is built on a foundational principle: **AI augments PMM judgment, it doesn't replace it.**

### Guardrails System

- **Budget limits:** Agents cannot commit spend beyond PMM-defined thresholds
- **Brand tone enforcement:** Content agents operate within brand voice parameters; deviations get flagged
- **Approval workflows:** Configurable per agent, per action type
  - Example: "Auto-publish internal Slack updates, but require my approval for any external-facing content"
  - Example: "Auto-update battlecard data points, but flag messaging changes for review"
- **Confidence scoring:** Every output includes a confidence score (0-100). Low-confidence outputs route to human review. Threshold is PMM-configurable.
- **Safe zone boundaries:** Each agent has a defined autonomy zone. Inside = auto-execute. Outside = escalate with context and a recommendation.

### What This Looks Like in Practice

The CI Agent detects that your #1 competitor just announced a major new feature:

1. CI Agent generates an impact assessment (confidence: 92%) → auto-published to the competitive Slack channel
2. Positioning Agent evaluates messaging impact → recommends 2 messaging updates (confidence: 78%) → routes to PMM for review with before/after comparison
3. Sales Enablement Agent drafts updated battlecard section (confidence: 85%) → queues for PMM approval with highlighted changes
4. Alignment Agent drafts a sales team notification → PMM reviews, edits one line, approves → sent to sales Slack channel
5. AI Content Workflow Agent drafts a LinkedIn response post → PMM reviews, adjusts the hook, approves → queued for optimal posting time

**Total PMM time: 15 minutes.** Without the system: 2-3 days of manual work across 5 different tools, if it happens at all.

---

## Who This Is For

### Primary: The Solo/Small-Team PMM (44% of all PMM teams)

**Sarah, Solo PMM at a Series B SaaS startup (60 employees)**

Sarah is the only PMM. She supports 4 PMs, a 15-person sales team, and a 3-person content team. She's expected to own positioning, competitive intel, launches, sales enablement, and content strategy. She uses ChatGPT for drafts but spends most of her time in spreadsheets and Google Docs trying to keep everything connected.

PMM Agent OS gives Sarah:
- A CI Agent that monitors her top 3 competitors while she sleeps
- A Launch Agent that auto-generates her launch plan when a PM drops a feature brief
- A Content Agent that produces channel-optimized posts trained on what actually works for her audience
- A Metrics Agent that generates her monthly impact report in 5 minutes instead of 5 hours

Sarah goes from **surviving** to **strategizing**.

### Secondary: PMM Teams at Scale (5-15 person teams)

**Marcus, Director of PMM at a growth-stage company (500 employees)**

Marcus manages 6 PMMs across 3 product lines. His challenge isn't individual productivity — it's consistency, knowledge sharing, and cross-team alignment. Every PMM has their own messaging doc, their own competitive notes, their own launch process.

PMM Agent OS gives Marcus:
- A shared Context Graph so every PMM works from the same source of truth
- Standardized workflows (launch tiering, messaging development, enablement creation) that enforce best practices
- Cross-team visibility into what every PMM is working on and how it connects
- Team-level metrics that prove the function's impact to leadership

Marcus goes from **managing chaos** to **running a machine**.

### Tertiary: Adjacent GTM Roles

Demand gen leaders, content strategists, growth marketers, and sales leaders who work closely with PMMs — all benefit from a system that keeps messaging consistent, content current, and intelligence flowing.

---

## Business Model

### Pricing

| Tier | Price | Target | What You Get |
|---|---|---|---|
| **Free** | $0 | Solo PMMs, job seekers | 1 project, 2 agents (Positioning + CI), 50 agent actions/month |
| **Pro** | $49/month | Solo PMMs, startup PMMs | All 11 agents, 5 projects, unlimited actions, integrations, export |
| **Team** | $29/user/month (min 3) | PMM teams | Everything in Pro + shared Context Graph, collaboration, brand voice, role-based permissions |
| **Enterprise** | Custom | PMM orgs at scale | Everything in Team + SSO, API access, custom agents, dedicated support, compliance (SOC2), on-premise option |

### Why This Pricing Works

- **Free tier** solves cold start (ChatPRD's 100K users started here)
- **$49/mo Pro** is a no-brainer vs. Klue ($20K+/yr) or Seismic ($30+/user/mo)
- **$29/user Team** aligns with enterprise procurement patterns
- **Future evolution:** Outcome-based pricing (per launch planned, per proposal generated, per battlecard updated) as the investor-favored model

### Revenue Trajectory

| Year | Free Users | Paid Users | ARR | Milestone |
|---|---|---|---|---|
| Y1 | 5,000 | 500 | ~$300K | PMF validated, community built |
| Y2 | 25,000 | 2,500 | ~$1.5M | Team tier traction, first enterprise deals |
| Y3 | 80,000 | 8,000 | $5-8M | Series A territory, category defined |

---

## Competitive Position

### What Exists Today

| Product | What It Does | What It Doesn't Do |
|---|---|---|
| **ChatGPT / Claude** | General-purpose AI | No PMM workflow, no persistent context, no agent chaining, no methodology |
| **Klue / Crayon** | Competitive intelligence | Single workflow. $20-47K/yr. No messaging, no launches, no content, no signals |
| **Jasper / Copy.ai** | AI content writing | Generic. No PMM context, no competitive awareness, no performance learning |
| **Seismic / Highspot** | Sales enablement (content management) | Content repository, not content intelligence. No CI, no positioning, no signals |
| **Kana** | Agentic marketing platform | Horizontal marketing, not PMM-specific. Media-buying focused proposal generator. $15M seed. |
| **aicofounder.com** | Startup validation agents | Founder-focused, not PMM. Proves the model works. |
| **ChatPRD** | PM copilot for PRDs | PM-focused, not PMM. Proves the model works. |

### Where We Win

```
                    PMM-Specific
                         |
                    [PMM Agent OS]  <-- WE ARE HERE
                         |
                         |
    Single Tool ---------|--------- Multi-Agent Orchestrated
                         |
      Klue, Crayon       |       Kana (broad marketing)
      Jasper, Copy.ai    |       Lindy (operations)
      Segment8           |       Salesforce Agentforce (CRM)
                         |
                    Horizontal/Generic
```

**Nobody occupies our quadrant: PMM-specific AND multi-agent orchestrated.**

---

## Why Now

1. **AI quality crossed the threshold.** Claude/GPT-4 class models can now produce PMM-grade positioning docs, battlecards, and launch plans that were impossible 18 months ago.

2. **PMMs are asking for this product.** 25% of PMMs independently said their role is shifting toward "orchestrating agents" and "building systems" (Fluvio 2025).

3. **The market window is open.** Gartner predicts 40% of enterprise apps will embed AI agents by end of 2026 (up from <5% in 2025). First-mover advantage matters.

4. **Budget pressure creates pull.** Marketing budgets at a decade-low 7.7% of revenue. PMMs need to do more with less — a $49/mo agent platform is the answer.

5. **The community is ready.** 300K+ PMMs across PMA (95K Slack), GoPMM, Sharebird, Reddit — a highly networked, community-driven audience primed for a purpose-built tool.

6. **The playbook is proven.** aicofounder.com (50K founders, bootstrapped) and ChatPRD (100K PMs, six-figure ARR) prove that role-specific AI agent platforms achieve rapid adoption.

---

## Principles

### 1. Opinionated > Flexible
We embed proven PMM methodologies (April Dunford positioning, launch tiering frameworks, Content Playground model) into the agents. The product guides PMMs through what great looks like — it doesn't ask "what do you want?" It says "here's how the best PMMs do this, let me walk you through it."

### 2. Connected > Comprehensive
A mediocre CI agent that feeds into positioning, which feeds into enablement, which feeds into metrics — is 10x more valuable than a best-in-class CI tool that lives in isolation. The power is in the connections between agents, not any individual agent.

### 3. Living > Static
Every document the system produces is a living artifact connected to the Context Graph. When the underlying data changes, the document updates. Battlecards don't go stale. Personas don't age out. Launch plans adapt to timeline changes.

### 4. Earned Autonomy > Blind Trust
Agents start with low autonomy and earn more as PMMs build trust. Day 1: everything requires approval. Month 3: routine updates auto-publish, novel outputs get reviewed. Month 12: the system runs 80% of execution autonomously while the PMM focuses on strategy.

### 5. Show the Work > Black Box
Every agent output includes: what data it used, what methodology it applied, its confidence level, and what alternatives it considered. PMMs should always understand why the system recommended what it recommended.

---

## Platform Roadmap: From Agent Platform to Full-Stack PMM Operating System

### The Strategic Arc

```
Phase 1 (M0-6)          Phase 2 (M6-18)           Phase 3 (M18-36)          Phase 4 (M36+)
STANDALONE AGENTS   →   CONNECTED PLATFORM    →   FULL-STACK PMM OS     →   ECOSYSTEM & API

2 core agents           11 agents + core          Deep integrations         Open platform
(Positioning + CI)      integrations              across entire             + marketplace
Free + Pro tiers        Team tier                 product/GTM stack         + partner agents
Community launch        First enterprise          System of record          Category leader
                                                  for GTM
```

### The Vision: PMM Agent OS as the Central Nervous System

Today, the PMM's world looks like this:

```
[Jira] [Confluence] [Productboard] [Amplitude] [Gong] [Slack] [HubSpot] [G2] [Highspot]
  |        |              |              |          |      |       |        |       |
  └────────┴──────────────┴──────────────┴──────────┴──────┴───────┴────────┴───────┘
                                         |
                                    [The PMM]  ← manually stitching everything together
                                         |
                              [Google Docs / Notion]  ← where the "work" lives
```

In the future, it looks like this:

```
[Jira] [Confluence] [Productboard] [Amplitude] [Gong] [Slack] [HubSpot] [G2] [Highspot]
  |        |              |              |          |      |       |        |       |
  └────────┴──────────────┴──────────────┴──────────┴──────┴───────┴────────┴───────┘
                                         |
                              ┌──────────┴──────────┐
                              │   PMM AGENT OS      │
                              │   Context Graph +   │  ← persistent intelligence layer
                              │   11 Orchestrated   │     that reads from and writes to
                              │   Agents            │     every tool in the stack
                              └──────────┬──────────┘
                                         |
                                    [The PMM]  ← orchestrating strategy, not stitching tools
```

**PMM Agent OS becomes the intelligence layer that sits on top of the entire product and GTM stack** — reading signals from every tool, enriching the Context Graph, and pushing actions back into the tools teams already use.

---

### Phase 2 Integrations (Months 6-18): Core Connectors

These are the integrations that make the Context Graph 10x more powerful by feeding it real data instead of manual input.

#### Product & Engineering Tools

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Jira** | Epics, stories, release dates, sprint status, feature descriptions, bug counts, velocity | Launch timeline auto-updates when sprints slip; auto-tag stories with GTM impact tier | Launch Planning Agent, Alignment Agent |
| **Confluence** | Product specs, PRDs, meeting notes, decision logs, retrospectives | Launch briefs, messaging docs, competitive analyses published as Confluence pages | All agents (read), Launch + Positioning (write) |
| **Productboard** | Feature requests ranked by customer impact, customer feedback, roadmap priorities, segment-level demand | Market insights, competitive gaps, win/loss themes pushed as insights | Research Agent, Positioning Agent, CI Agent |
| **Linear** | Issues, project status, release cycles | Similar to Jira — launch timeline sync, GTM tagging | Launch Planning Agent |
| **GitHub** | Release notes, changelog, public roadmap (if applicable) | Auto-generate customer-facing release notes from engineering changelogs | Content Workflow Agent, Sales Enablement Agent |

**Why this matters:** Today, PMMs manually translate Jira tickets into launch plans and Productboard insights into positioning docs. With these integrations, the Launch Planning Agent auto-detects when a Jira epic's release date slips and adjusts the launch timeline, notifies stakeholders, and recommends whether to decouple the marketing launch from the engineering release.

#### Product Analytics

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Mixpanel** | Feature adoption rates, user flows, conversion funnels, retention curves, cohort analysis | Segment definitions for signal activation; trigger events for in-app messaging | Metrics Agent, Signal Activation Agent, Research Agent |
| **Amplitude** | Same as Mixpanel + behavioral cohorts, experiment results, user journey maps | Same as Mixpanel | Metrics Agent, Signal Activation Agent, Research Agent |
| **Heap** | Auto-captured user interactions, session recordings, funnel analysis | User behavior patterns for persona enrichment | Research Agent, Signal Activation Agent |
| **Pendo** | Feature usage data, NPS/CSAT scores, in-app guide engagement, user segments | In-app guide content, feature announcement copy, onboarding flow recommendations | Content Workflow Agent, Metrics Agent |
| **PostHog** | Product analytics, session recordings, feature flags, A/B test results | Experiment recommendations based on content/messaging performance | Metrics Agent, Content Workflow Agent |

**Why this matters:** The Metrics Agent can finally answer "did our launch actually drive feature adoption?" by reading real product analytics — not relying on the PMM to manually pull Amplitude charts. The Signal Activation Agent detects when a free user hits an activation milestone and triggers a personalized upgrade nudge.

#### Revenue Intelligence & Sales

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Gong** | Call recordings, talk-to-listen ratios, competitor mentions, objection patterns, topic trends, deal risk scores | Talk track recommendations, competitive sound bites surfaced in Gong's flow | Research Agent, CI Agent, Sales Enablement Agent |
| **Chorus (ZoomInfo)** | Same as Gong | Same as Gong | Research Agent, CI Agent, Sales Enablement Agent |
| **Clari / Salesloft** | Pipeline data, forecast accuracy, deal velocity, stage progression | Launch impact on pipeline correlation data | Metrics Agent, Signal Activation Agent |
| **Salesforce / HubSpot CRM** | Opportunity data, win/loss reasons, competitor fields, account details, lead scores, campaign attribution | Auto-update competitor field from CI Agent detections; push signal scores to accounts; log PMM-influenced touchpoints | All agents — CRM is the connective tissue |
| **Outreach / Salesloft** | Email sequence performance, reply rates, meeting booked rates | Optimized email templates, personalized sequences based on signal + persona | Content Workflow Agent, Signal Activation Agent |
| **Highspot / Seismic** | Content usage by reps, content engagement by prospects, content-to-deal correlation | Auto-publish updated battlecards, one-pagers, talk tracks directly into the enablement platform | Sales Enablement Agent, CI Agent |

**Why this matters:** The Research Agent can synthesize themes across 500 Gong calls without the PMM listening to a single one. The Sales Enablement Agent knows which battlecard sections reps actually use (from Highspot data) and optimizes accordingly. The Metrics Agent can finally correlate "reps who used our new talk track had 23% higher win rates."

#### AI Notetakers & Meeting Intelligence

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Zoom** (native AI companion) | Meeting transcripts, AI summaries, action items | Nothing (read-only) | Research Agent, Alignment Agent |
| **Otter.ai** | Meeting transcripts, keyword highlights, action items | Nothing (read-only) | Research Agent |
| **Fireflies.ai** | Transcripts, topic tracking, sentiment analysis, action items | Nothing (read-only) | Research Agent, CI Agent |
| **Grain** | Video highlights, transcript clips, shared moments | Nothing (read-only) | Research Agent |
| **Fathom** | AI meeting summaries, action items, CRM sync data | Nothing (read-only) | Research Agent, Alignment Agent |
| **tl;dv** | Transcripts, AI notes, timestamps, CRM integration | Nothing (read-only) | Research Agent |
| **Granola** | Meeting notes, structured summaries | Nothing (read-only) | Research Agent |

**Why this matters:** Every customer call, sales meeting, product review, and internal planning session becomes fuel for the Context Graph. The Research Agent auto-extracts customer language patterns, pain points, and feature requests from meeting transcripts. The Alignment Agent generates post-meeting summaries with action items tagged to the right stakeholders.

#### Collaboration & Communication

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Slack** | Channel messages (competitive intel channel, deal room channels, product updates), reactions, thread activity | CI alerts, launch status updates, signal notifications, battlecard snippets — all delivered in Slack-native format | All agents — Slack is the distribution layer |
| **Microsoft Teams** | Same as Slack | Same as Slack | All agents |
| **Notion** | Product specs, launch docs, competitive wikis, team wikis, meeting notes | Publish positioning docs, launch briefs, personas, competitive analyses as Notion pages | All agents (read + write) |
| **Google Workspace** (Docs, Sheets, Slides, Drive) | Existing messaging docs, launch trackers, competitive analyses, sales decks, presentation templates | Export agent outputs as Google Docs/Sheets/Slides; auto-update shared docs when Context Graph changes | All agents |
| **Asana / Monday.com** | Project timelines, task status, dependencies, team workload | Launch task creation, milestone tracking, cross-functional assignments | Launch Planning Agent, Alignment Agent |
| **Figma / FigJam** | Design files, whiteboard content, positioning workshop outputs | Nothing (read-only) — but can generate Figma-compatible content briefs | Content Workflow Agent |
| **Loom** | Video transcripts, viewer engagement data | Nothing (read-only) | Research Agent |

**Why this matters:** PMM Agent OS doesn't force teams to leave their tools. Agents push outputs WHERE teams already work — battlecard updates appear in the sales Slack channel, launch status updates post to Asana, positioning docs publish to Notion. The system is invisible infrastructure, not another app to check.

#### Market Intelligence & Review Platforms

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **G2** | Reviews (yours and competitors), category rankings, buyer intent data, comparison traffic | Nothing (read-only) | CI Agent, Signal Activation Agent, Research Agent |
| **Capterra / TrustRadius** | Reviews, comparisons, ratings | Nothing (read-only) | CI Agent, Research Agent |
| **Gartner / Forrester** | Analyst report summaries (via API where available), MQ/Wave placement data | Nothing (read-only) | CI Agent, Positioning Agent |
| **Crayon / Klue** (for teams that already have them) | Competitive change data, battlecard content, win/loss data | Enriched competitive insights from our CI Agent's broader analysis | CI Agent (bi-directional enrichment) |
| **Bombora / 6sense** | Third-party intent data, topic-level research signals, account surge scores | Nothing (read-only) — intent signals feed directly into Signal Activation Agent | Signal Activation Agent |
| **LinkedIn Sales Navigator** | Account signals, job changes, company growth data | Nothing (read-only) | Signal Activation Agent, Research Agent |
| **SimilarWeb / SEMrush** | Competitor traffic data, keyword rankings, ad spend estimates | Nothing (read-only) | CI Agent, Content Workflow Agent |

#### Marketing Automation & Distribution

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **HubSpot Marketing** | Campaign performance, email metrics, landing page conversion, lead scoring | Campaign content (email copy, landing page copy), A/B test recommendations | Content Workflow Agent, Metrics Agent |
| **Marketo** | Same as HubSpot Marketing | Same as HubSpot Marketing | Content Workflow Agent, Metrics Agent |
| **Intercom** | In-app messages, product tours, help center articles, chatbot conversations | In-app announcement copy, product tour scripts, help center drafts | Content Workflow Agent, Sales Enablement Agent |
| **Braze / Customer.io** | Lifecycle campaign performance, push/email/in-app metrics, user segments | Personalized message content based on user behavior + persona | Content Workflow Agent, Signal Activation Agent |
| **Buffer / Hootsuite / Sprout Social** | Social media performance, engagement metrics, audience insights, competitor social tracking | Channel-optimized social content ready to schedule | Content Workflow Agent |
| **Webflow / WordPress** | Website content, page performance, conversion data | Landing page copy updates, A/B test variants | Content Workflow Agent, Positioning Agent |

#### Customer Success & Support

| Tool | What We Read | What We Write Back | Which Agent Benefits |
|---|---|---|---|
| **Gainsight / Totango** | Health scores, churn risk signals, expansion indicators, customer lifecycle stage | Nothing (read-only) — health signals feed Context Graph | Signal Activation Agent, Metrics Agent |
| **Zendesk / Intercom** | Support ticket themes, CSAT scores, common issues, feature requests | Help center content drafts, FAQ updates based on trending issues | Research Agent, Content Workflow Agent |
| **UserTesting / Maze** | Usability test results, user feedback, task completion rates | Nothing (read-only) — research insights feed personas | Research Agent |
| **Wynter** | Message testing results, B2B panel feedback | Nothing (read-only) — message performance feeds Positioning Agent | Positioning Agent, Research Agent |
| **Dovetail** | Research repository, tagged insights, interview themes | Nothing (read-only) — qualitative insights feed Context Graph | Research Agent |

---

### Phase 3 Integrations (Months 18-36): Deep Platform Capabilities

#### Bi-Directional Workflow Automation

Move from "read data and push content" to **trigger-based workflows that span the entire stack:**

**Example Workflow: "Competitor Launches New Feature"**
```
[G2 + Crayon + SimilarWeb]  ──detect──→  CI Agent
                                            │
                                  ┌─────────┼─────────┐
                                  ▼         ▼         ▼
                           Positioning   Sales      Alignment
                             Agent      Enable.      Agent
                               │        Agent         │
                               │          │           │
                               ▼          ▼           ▼
                         [Notion:      [Highspot:   [Slack:
                          Update       Update       Alert sales
                          messaging    battlecard]  team + PM]
                          doc]            │
                                          ▼
                                    [Gong: Surface
                                     new talk track
                                     in call flow]
```

**Example Workflow: "High-Intent Account Detected"**
```
[Bombora + G2 Intent + Website (Mixpanel)]  ──detect──→  Signal Activation Agent
                                                              │
                                               ┌──────────────┼──────────────┐
                                               ▼              ▼              ▼
                                         [Salesforce:    [Outreach:      [Slack:
                                          Update         Trigger         Alert AE
                                          account        personalized    in deal
                                          score]         sequence]       room]
                                                              │
                                                              ▼
                                                   Content Workflow Agent
                                                        │
                                                        ▼
                                                  [Generate account-
                                                   specific one-pager
                                                   based on intent
                                                   signals + persona]
```

**Example Workflow: "Jira Epic Delayed → Launch Timeline Shift"**
```
[Jira: Epic moved to next sprint]  ──detect──→  Launch Planning Agent
                                                       │
                                            ┌──────────┼──────────┐
                                            ▼          ▼          ▼
                                      [Asana:      [Slack:     [Google Slides:
                                       Shift all   Notify      Update launch
                                       dependent   stakeholders review deck
                                       tasks]      with new     with new
                                                   timeline]    dates]
                                                       │
                                                       ▼
                                                 Alignment Agent
                                                       │
                                                       ▼
                                                 [Generate "delay
                                                  turned positive"
                                                  memo — extra time
                                                  for these 3 items]
```

#### The Integration Moat

Here's why this integration strategy creates compounding defensibility:

| Moat Layer | How It Compounds |
|---|---|
| **Data network effects** | Every integration adds data to the Context Graph. More data = smarter agents = better outputs = more usage = more data. |
| **Workflow lock-in** | When agents trigger actions across 10+ tools automatically, ripping out PMM Agent OS means rebuilding all those automations manually. |
| **Cross-tool intelligence** | No single tool can correlate Gong call themes + Amplitude adoption data + G2 review sentiment + Jira release timelines. We can. |
| **Distribution advantage** | Agents push outputs into tools teams already use (Slack, Notion, Highspot). The value is felt everywhere, even by people who never log into PMM Agent OS directly. |

---

### Phase 4 (Months 36+): Open Platform & Ecosystem

#### Agent Marketplace
Allow PMMs and developers to build custom agents that plug into the orchestration layer and Context Graph:

- **Industry-specific agents:** "Healthcare Compliance Agent" that checks all messaging against FDA/HIPAA requirements
- **Channel-specific agents:** "Podcast Booking Agent" that identifies relevant podcasts, drafts pitches, and manages outreach
- **Regional agents:** "APAC Localization Agent" that adapts messaging for Japanese, Korean, and Southeast Asian markets
- **Vertical agents:** "Developer Marketing Agent" with dev-specific channel strategies (HackerNews, Stack Overflow, GitHub)
- **Partner-built agents:** Gong builds a "Deal Intelligence Agent," Klue builds an "Enterprise CI Agent," etc.

#### Public API
```
POST /api/v1/context-graph/query
{
  "query": "What is our current positioning against [Competitor X] for enterprise accounts?",
  "format": "structured",
  "include": ["positioning", "competitive", "win_loss", "talk_tracks"]
}
```

Let any tool in the GTM stack query the Context Graph — making PMM Agent OS the intelligence backbone that powers the entire revenue engine.

#### Webhook & Event System
```
POST /api/v1/webhooks/subscribe
{
  "event": "competitive.major_change",
  "competitor": "competitor-x",
  "callback_url": "https://your-app.com/webhook",
  "filters": { "significance": "high" }
}
```

Any tool can subscribe to events from the Context Graph — competitor changes, signal spikes, messaging updates, launch status changes.

---

### Integration Priority Matrix

For MVP and early phases, prioritize integrations by: (1) how much richer they make the Context Graph, and (2) how many PMMs already use the tool.

| Priority | Integrations | Why |
|---|---|---|
| **P0 — MVP** | Slack, Google Workspace, Notion | Distribution. Agents need to push outputs where PMMs already live. |
| **P1 — First 6 months** | Gong/Chorus, Salesforce/HubSpot CRM, Jira/Linear | Revenue intelligence + product timeline = the two richest data sources for PMMs. |
| **P2 — Months 6-12** | Amplitude/Mixpanel, Highspot/Seismic, G2, Asana | Product analytics + enablement platform + review data = next richest layer. |
| **P3 — Months 12-18** | Bombora/6sense, Outreach, Intercom/Braze, Productboard, AI notetakers | Signal data + marketing automation + product management = full stack. |
| **P4 — Months 18-24** | Crayon/Klue, Pendo, Gainsight, Dovetail, Wynter, SimilarWeb | Specialized tools for teams with mature stacks. |
| **P5 — Months 24+** | API + Webhook platform, Agent Marketplace | Open ecosystem play. |

---

### The Full Stack PMM OS: What It Looks Like When Everything Is Connected

**Monday morning for Sarah (Solo PMM, Series B startup), 18 months from now:**

She opens PMM Agent OS and sees her dashboard:

```
┌─────────────────────────────────────────────────────────────────────┐
│  GOOD MORNING, SARAH                                    April 2028 │
│                                                                     │
│  🔴 URGENT                                                          │
│  ├─ Competitor X dropped pricing 20% (detected 2h ago via G2 +     │
│  │  website monitor). Battlecard auto-updated. Sales notified.      │
│  │  → Review messaging impact assessment [85% confidence]           │
│  │                                                                   │
│  ├─ 3 high-intent accounts detected (Bombora surge + pricing page   │
│  │  visits). Personalized outreach sequences drafted in Outreach.   │
│  │  → Approve sequences [92% confidence]                            │
│  │                                                                   │
│  🟡 THIS WEEK                                                       │
│  ├─ Q2 feature launch: Jira epic on track, 12 days to release.     │
│  │  Launch plan auto-generated (Tier 2). Asana tasks created.       │
│  │  → Review launch brief [88% confidence]                          │
│  │                                                                   │
│  ├─ 4 LinkedIn posts queued (trained on your top performers).       │
│  │  Best predicted post: carousel on [topic] — 2.3x avg engagement  │
│  │  → Review & approve for scheduling                               │
│  │                                                                   │
│  🟢 INSIGHTS                                                        │
│  ├─ Gong analysis: "data security" mentioned 47% more in sales     │
│  │  calls this month. Recommend adding security proof points to     │
│  │  enterprise talk track.                                          │
│  │                                                                   │
│  ├─ Amplitude: New onboarding flow (launched 3 weeks ago) showing   │
│  │  18% better activation rate. Recommend Tier 3 announcement.      │
│  │                                                                   │
│  ├─ Win rate against Competitor Y improved from 34% → 41% since    │
│  │  battlecard refresh (6 weeks ago). Highspot shows 73% rep usage. │
│  │                                                                   │
│  📊 YOUR IMPACT THIS MONTH                                          │
│  ├─ Pipeline influenced: $4.2M (↑23% vs last month)                │
│  ├─ Battlecard usage: 71% of reps (↑12%)                           │
│  ├─ Content engagement: 34K impressions, 4.1% avg engagement       │
│  ├─ Launch on track: 2/3 Q2 launches completed                     │
│  └─ Signal-to-meeting conversion: 14% (↑3%)                        │
└─────────────────────────────────────────────────────────────────────┘
```

**Sarah's total time to review, adjust, and approve everything: 25 minutes.**

Without PMM Agent OS, this same set of activities would take Sarah **15-20 hours across 12 different tools**, and half of it simply wouldn't get done.

---

## The Endgame

In 5 years, "PMM Agent OS" becomes the category — the way Salesforce became synonymous with CRM, or Figma with collaborative design.

Every PMM team runs on an orchestrated agent platform. The best PMMs aren't the ones who write the best battlecards — they're the ones who build the best systems. The PMM role transforms from "marketing's most overworked generalist" to "GTM's strategic architect."

We're not building a tool. We're building the operating system for the future of product marketing.

---

*"AI isn't replacing PMMs. It's replacing the broken systems that PMMs have been forced to work within. We're building the system that should have existed all along."*

---

## Next Steps

1. **Validate** — 20 PMM interviews (GoPMM network, Sharebird contacts) to pressure-test the agent priorities and integration priorities
2. **Build MVP** — Positioning Agent + CI Agent + Slack/Notion/Google Workspace connectors, free tier, community launch
3. **Launch** — Product Hunt + PMA Slack + LinkedIn + GoPMM community
4. **Iterate** — Ship remaining agents and integrations based on user pull, not our assumptions
5. **Platform** — Open API + Agent Marketplace once core is proven
