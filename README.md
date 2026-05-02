# One Person Billionaire

**An honest 22-lesson curriculum + 66 Claude skills + 7 chained commands for engineers who want to build, ship, and monetize agent-powered products as a solo (or near-solo) operator.**

## One objective

Everything in this repo serves **one** goal:

> **Build, ship, and monetize an agent-powered product as a solo operator targeting outlier outcomes ($5M-$50M ARR over 5-7 years).**

The curriculum is the theory. The skills are the activatable workflows. The commands chain skills into end-to-end actions. The templates are the fillable artifacts. The workflow specs are the runnable infrastructure.

## Start Here (don't read — type)

```
/find-wedge        Discover a profitable wedge end-to-end (wedge → ICP → validation)
/build-offer       Construct the Hormozi Grand Slam offer + price it for max margin
/start-outbound    Run a 100-prospect cold campaign (signals → emails → drafts)
/audit-product     5-dimensional audit (harness, production, boring-stack, margin, retention)
/diagnose-stall    Why you're stuck at $X MRR — pick the ONE bottleneck
/plan-week         Design your 4-day operator's week
/annual-review     Annual scorecard + update your 10-year statement
```

These 7 slash commands chain the 66 skills into end-to-end workflows. **Type one to start.** No need to read the lessons first — the skills walk you through.

If you prefer reading first → start with [Lesson 00: The Honest Premise](./00-the-honest-premise/README.md). It tells you what's actually achievable (spoiler: not a billion in solo revenue, but $5M-$50M is) so you don't quit when the math hits.

## Install

### Claude Code (recommended)

```bash
claude plugin marketplace add mothivenkatesh/one-person-billionaire
claude plugin install one-person-billionaire@one-person-billionaire
```

All 66 skills + 7 commands install automatically. Type `/find-wedge` (or any other) to start.

### Manual install (any tool)

```bash
git clone https://github.com/mothivenkatesh/one-person-billionaire.git
# Skills auto-load in Claude Code from .claude/skills/ — symlink:
ln -s $(pwd)/one-person-billionaire/skills .claude/skills
# For Cursor: cp -r one-person-billionaire/skills .cursor/skills
# For Gemini CLI: cp -r one-person-billionaire/skills .gemini/skills
# For Codex: cp -r one-person-billionaire/skills .codex/skills
```

## Read this first

The phrase **"one-person billionaire"** is mostly fan-fiction in 2026. Zero have been confirmed. The honest ladder:

| Stage | ARR | Solo? | Known cases |
|---|---|---|---|
| Side project | $0 – $10K | ✅ | Most attempts |
| Ramen profitable | $10K – $100K | ✅ | Thousands of indie hackers |
| Sustainable solo | $100K – $1M | ✅ | Hundreds globally |
| Mid solo | $1M – $10M | ✅ with agents | ~50–200 globally |
| Outlier solo | $10M – $100M | Possible with agents + automation | ~5–20 globally |
| Solo $100M+ ARR | $100M+ | Hypothetically possible 2030+ | None proven |
| Solo $1B exit / $1B founder net worth | — | Possible at high multiples + held equity | None proven *as solo* |

This curriculum trains you for the realistic ladder. **Read [Lesson 00](./00-the-honest-premise/README.md) before anything else** — it does the math so you don't quit when the math hits.

---

## What this is — and is not

| ✅ This is | ❌ This is not |
|---|---|
| A 22-lesson opinionated path from `while True:` to monetized agent product | A get-rich-quick framework |
| Honest about distribution being the harder half | A "just code well" engineering deep-dive |
| Calibrated for 2026: post-MCP, post-Claude 4.7, post-Skills spec | A theoretical AI textbook |
| Each lesson ends with one concrete exercise | A motivational manifesto |
| Built to compound — short reads, durable principles | A library you'll reference once and forget |

---

## Who this is for

- You can already code (Python or TypeScript)
- You've shipped at least one thing to real users (or you're about to)
- You've used Claude Code / Cursor / Codex enough to feel what an agent *is*
- You don't need hand-holding on `git`
- You're tempted by the indie-hacker leg but realize engineering alone won't get you there

---

## The 5 Parts

```
PART 1   ENGINEERING       L01 → L04   The 100x agent engineer (compressed)
[INTERLUDE]                L04A        The boring stack first — when NOT to use AI
PART 2   PRODUCTIZING      L05 → L08   Engineering chops → a thing people pay for
[INTERLUDE]                L08A        The Grand Slam Offer — fix the offer before scaling distribution
PART 3   DISTRIBUTION      L09 → L12   The half engineers always skip
PART 4   MONETIZATION      L13 → L16   Pricing, margin, retention, scaling
PART 5   LEVERAGE          L17 → L20   Compounding into outlier outcomes

PRACTICAL HARNESS (use alongside the lessons)
- skills/                        66 Claude skills (22 curriculum + 4 GTM toolkit + 40 GTM analytics)
- skills/grand-slam-offer/       Hormozi $100M Offers framework
- skills/gtm-analytics/          Enterprise GTM analytics for $1M+ ARR scale
- commands/                      7 chained slash commands
- templates/                     4 fillable canvases
- code/offer-workshop/           Inngest workflow spec for automated weekly offer review
```

---

## Lessons

### Part 0 — Premise
- **00** [The Honest Premise](./00-the-honest-premise/README.md) — Read first. The math behind the meme.

### Part 1 — Engineering
- **01** [The Minimum Viable Agent](./01-the-minimum-viable-agent/README.md)
- **02** [The Harness Is the Moat](./02-the-harness-is-the-moat/README.md)
- **03** [Multi-Agent and When to Actually Use It](./03-multi-agent-when-to-use-it/README.md)
- **04** [Production-Ready](./04-production-ready/README.md)

### Interlude (mandatory before Part 2)
- **04A** [The Boring Stack First — When NOT to Use AI](./04A-the-boring-stack-first/README.md)

### Part 2 — Productizing
- **05** [Find a Profitable Wedge](./05-find-a-profitable-wedge/README.md)
- **06** [The Riskiest Assumption Test](./06-riskiest-assumption-test/README.md)
- **07** [Wrapper, Product, or Platform](./07-wrapper-product-or-platform/README.md)
- **08** [The Smallest Paid Thing](./08-the-smallest-paid-thing/README.md)

### Interlude (mandatory before Part 3)
- **08A** [The Grand Slam Offer](./08A-the-grand-slam-offer/README.md) — Hormozi's Value Equation, problem→solution stack, bonuses, scarcity, urgency, the 4 guarantees, MAGIC naming.

### Part 3 — Distribution
- **09** [Build in Public as Distribution](./09-build-in-public/README.md)
- **10** [Cold Outbound for AI Products](./10-cold-outbound/README.md)
- **11** [Content That Compounds in the AI-Search Era](./11-content-that-compounds/README.md)
- **12** [Communities, Partnerships, and Affiliates](./12-communities-and-affiliates/README.md)

### Part 4 — Monetization
- **13** [Pricing AI Products](./13-pricing-ai-products/README.md)
- **14** [Margin Engineering](./14-margin-engineering/README.md)
- **15** [The Retention Problem Unique to AI Products](./15-the-retention-problem/README.md)
- **16** [The Scaling Cliff](./16-the-scaling-cliff/README.md)

### Part 5 — Leverage
- **17** [Automate Yourself First](./17-automate-yourself-first/README.md)
- **18** [Hiring Agents Instead of Humans](./18-hiring-agents-not-humans/README.md)
- **19** [The 1-Person Operating System](./19-the-one-person-operating-system/README.md)
- **20** [The 10-Year Compound](./20-the-10-year-compound/README.md)

---

## How to use

- **Read in order** if you're new to either side
- **Skip Part 1** if you already understand the agent loop
- **Skip Parts 1–2** if you're a senior PM/founder who needs the engineer's mental model
- **Each lesson** = ~15-min read + 1 actionable exercise. Most exercises are *"stop reading, go do this for an hour, come back"*

---

## The 8 Principles

1. **Distribution is the harder half.** Engineering excellence is necessary but not sufficient. Most failed indie attempts had the better product.
2. **Margin is destiny.** Per-token pricing kills you. Value-based pricing on durable problems wins.
3. **Compound or die.** One-time wins make great Twitter posts. Recurring wins make great businesses.
4. **The boring stack ships.** Anthropic SDK + a `while` loop + Postgres + Stripe will outship the latest agent framework every time.
5. **The model is not the moat.** Your moat is data, distribution, retention, and trust.
6. **Honest >> impressive.** Lying to yourself about your numbers is the most expensive thing you'll do.
7. **Time-in-market beats market-timing.** The 5-year operator beats the 12-month sprinter every time.
8. **AI is not always the answer.** Most production "AI products" are a workflow engine + 1-2 LLM steps. The agent loop is for the fuzzy 20%, not the structured 80%.

---

## Further reading (educational sources cited throughout)

- Alex Hormozi — *$100M Offers* and *$100M Leads* (offer construction)
- Patrick McKenzie — bootstrapped SaaS economics, cold email, "Don't Call Yourself a Programmer"
- Jason Cohen — A Smart Bear blog (bootstrapped SaaS)
- Tyler Tringas — Calm Company Fund (alternative to VC)
- Pieter Levels — bootstrapped multi-product solo operator (the "boring stack" example)
- Rob Fitzpatrick — *The Mom Test* (customer interview method)
- Madhavan Ramanujam — *Monetizing Innovation* (pricing framework)
- Anthropic — Claude API docs, prompt caching docs, Skills specification
- OWASP — MCP Top 10 (agent security)

---

## License

MIT. Fork it, ship it, sell it.
