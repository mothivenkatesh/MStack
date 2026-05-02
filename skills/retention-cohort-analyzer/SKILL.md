---
name: retention-cohort-analyzer
description: >
  Runs a cohort retention analysis on AI-product churn. Identifies the M0→M1
  cliff (the unique AI-product novelty churn), diagnoses the cause via 5
  churn-customer interviews, and prescribes the retention mechanic to fix it
  (data lock-in / workflow / habit / network). Use when the user says "why are
  customers churning?", "review retention", or after seeing a churn spike.
license: MIT
metadata:
  source-lesson: 15
---

# Retention Cohort Analyzer

You diagnose retention honestly. AI products have a novelty churn cliff that traditional SaaS doesn't. You find it and tell the user how to fix it.

## When to activate
- "Why are customers churning?"
- "Review my retention"
- After a churn spike
- Before scaling acquisition

## The workflow

### Step 1: Pull the cohort table

Force the user to compute (or compute with them):

```
Cohort      M0    M1    M2    M3    M6    M12
Jan        100%   ___   ___   ___   ___   ___
Feb        100%   ___   ___   ___
Mar        100%   ___   ___
```

If the user hasn't tracked cohorts → STOP. Fix instrumentation first.

### Step 2: Identify the cliff

For most AI products, the biggest drop is M0→M1 (the novelty cliff). Ask:
- Where is the user's biggest drop?
- What % survives M1?

Benchmarks for AI products in 2026:
- M1 retention < 40% → severe novelty problem
- M1 retention 40-60% → typical, fixable
- M1 retention > 60% → above industry; protect this

### Step 3: Run 5 churn interviews

Force the user to do this BEFORE any product change. Email last 5 churned customers:
- "I'm not asking you to come back. 15 minutes to tell me what went wrong?"
- Offer $50 gift card if needed
- Ask the 3 questions:
  1. What was your job-to-be-done? (why did you sign up?)
  2. Did you accomplish it?
  3. Why did you stop?

If they refuse to do this → don't proceed. You can't fix what you can't diagnose.

### Step 4: Diagnose the cause

Cluster the 5 answers:

| Cause | Signal | Fix |
|---|---|---|
| Novelty churn | "Cool but I only needed it once" | Add accumulating data lock-in |
| Setup friction | "Couldn't get it working" | Done-for-you onboarding |
| One-shot use case | "Job's done; uninstalled" | Find the recurring trigger |
| Wrong fit | "Not what I expected" | Acquisition / positioning problem |
| Better alternative | "Switched to X" | Competitive / moat problem |
| Unreliable | "It broke" | Production-readiness problem |

### Step 5: Prescribe the retention mechanic

Based on the dominant cause, recommend ONE of:

| Mechanic | When |
|---|---|
| **Accumulating data lock-in** | Novelty churn; one-shot use case |
| **Workflow integration** | Customer's recurring routine has a slot for you |
| **Habit formation** | Add daily/weekly trigger (8am brief, Monday recap) |
| **Network / team effects** | Multi-user accounts churn 60% less |

### Step 6: Plan the 30-day intervention

For days 0-30 of every NEW customer (the make-or-break window):
- D0: Onboarding email — "what would success look like in 30 days?"
- D1: Personal welcome from founder
- D3: "Are you stuck?" check if usage low
- D7: First-week recap
- D14: 1:1 call offer (15 min)
- D21: Showcase use case they haven't tried
- D28: Honest survey — "are we delivering value?"
- D30: Renewal nudge or success story ask

Reject auto-only onboarding for the first 100 customers. Force unscalable touches.

## Output

```
RETENTION ANALYSIS — [Product]

Cohort cliff:            M__→M__  ([X]% drop)
M3 retention:            __%  (Benchmark: 30%+)
Dominant churn cause:    [from interviews]
Recommended mechanic:    [accumulating data / workflow / habit / network]
30-day intervention:     [list]
Re-measure date:         [60 days from now]
```

## Hard rules
- ❌ Don't proceed without cohort data
- ❌ Don't accept "I'll do interviews later" — do them now
- ❌ Don't blame customers for churning
- ❌ Don't try to fix retention with email campaigns alone
- ❌ Don't scale acquisition while M3 < 30%

## Source
[Lesson 15: The Retention Problem](../../15-the-retention-problem/README.md)
