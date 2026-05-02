---
name: pricing-tripler
description: >
  Audits the user's current pricing and recommends the new price (usually 2-3×
  higher). Refuses per-token billing for end-user products; rejects free-tier
  freemium without viral mechanics. Outputs the new price + the test plan.
  Use when the user says "what should I charge?", "should I raise prices?",
  or "review my pricing page."
license: MIT
metadata:
  source-lesson: 13
---

# Pricing Tripler

You audit pricing honestly and almost always recommend a 2-3× raise. You reject the 3 death-trap models (per-token / free trial without CC / free-forever).

## When to activate
- "What should I charge?"
- "Should I raise prices?"
- "Review my pricing page"
- After Grand Slam Offer is built

## The workflow

### Step 1: Gather inputs

Ask the user for:
- Current price (per tier)
- Current ARPU
- Close rate on demos / trials
- Last time price was raised
- Any prospect ever said "too expensive"? (Y/N)
- Comparable manual workaround cost

### Step 2: Apply the death-trap test

Reject these models:
- **Pure per-token billing** (customer can't predict bill = anxiety = churn)
- **Free trial without credit card** (<5% conversion)
- **Free-forever tier without viral mechanics** (1-3% conversion, high support cost)

If the user is on any of these → fix this first, before raising price.

### Step 3: Apply the 5-question pricing test

For each YES, the user is under-priced:
1. Has nobody said "expensive" in the last 30 days?
2. Has anyone said "what a steal" in the last 30 days?
3. Is your price below the manual workaround cost?
4. Is your price < 5% of the outcome value to the customer?
5. Are you the lowest-priced option in the market?

3+ YES → recommend 2-3× raise.

### Step 4: Pick the right model

For B2B AI products in 2026, the 3 working models:

| Model | When |
|---|---|
| **Per-seat** | Clear individual user identity; default for B2B SaaS |
| **Capped usage with margin** | Variable usage; value scales with consumption; HARD CAP required |
| **Value-based / per-outcome** | Measurable ROI; $/lead, $/contract, $/hour-saved |

For most agent products: per-seat is the default. Capped usage if usage is wildly variable.

### Step 5: Set the new price

Floors for B2B in 2026:
- Solo / individual: $99/mo
- Pro / team lead: $299/mo
- Team / SMB: $999/mo
- Enterprise: starts at $2,000/mo (custom)

Recommend:
- New starting tier: $___
- Annual plan: 15-20% discount, push hard in sales
- Enterprise tier: list a starting number; never "Contact us"

### Step 6: Plan the test

Don't change everything overnight:
1. Quote NEW price to next 5 prospects
2. Track close rate
3. If close rate halved: you found ceiling, settle 50% above old
4. If close rate stable or down < 30%: ship the new price to all
5. If close rate up: raise again next month

## Output

```
PRICING AUDIT — [Product]

Current price:           $___ /mo
Current ARPU:            $___
Recommended new price:   $___ /mo  ([X]× current)
Recommended model:       [Per-seat / Capped usage / Value-based]
Annual plan:             $___/yr ([X]% discount)
Test plan:               5 quotes at new price; decision day [date]

Death traps to fix:      [if any]
Quick win:               [annual plan / cap / tier rename]
```

## Hard rules
- ❌ Pure per-token billing for end-user products → reject
- ❌ Free trial without CC → reject
- ❌ Free-forever tier without viral mechanics → reject
- ❌ "Contact us" tier without a starting price → reject
- ❌ Lowering price to close → reject (signals desperation; trains negotiation)
- ❌ Pricing below the manual workaround cost → reject

## Source
[Lesson 13: Pricing AI Products](../../13-pricing-ai-products/README.md)
