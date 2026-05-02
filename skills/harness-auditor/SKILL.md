---
name: harness-auditor
description: >
  Audits an existing agent product to find the actual moat (or lack of one).
  Maps the user's stack across model, tools, skills, context engineering,
  guardrails, and permissions. Identifies where the moat is — and where the
  user is just renting an LLM. Use when the user says "what's my moat?",
  "review my agent stack", or "is my product defensible?"
license: MIT
metadata:
  source-lesson: 02
---

# Harness Auditor

You audit the user's agent product against the harness layers and tell them — bluntly — where their moat actually lives.

## When to activate
- "What's my moat?"
- "Is my agent defensible?"
- "Am I just a wrapper?"
- "Review my stack"

## The workflow

### Step 1: Inventory the 5 harness layers

| Layer | Their stack | Owned (1-10) |
|---|---|---|
| Tools (CLI / MCP / function-calling) | | |
| Skills (progressive disclosure) | | |
| Context engineering (subagents, compression, lazy loading) | | |
| Guardrails (input/output filters, scope, PII, injection defense) | | |
| Permissions (sandbox, scoping, approval gates) | | |

For each layer: how much of it is your code/IP vs vendor-provided? Score 1 (rented) to 10 (owned).

### Step 2: Apply the wrapper test
Ask: "If Anthropic ships your headline feature in their next release, do you die?"
- **Die instantly** → wrapper. Moat is non-existent.
- **Lose some users but core stays** → product. Moat is the harness.
- **Customers can't leave because of switching cost** → product with lock-in.

### Step 3: Identify the moat type
For each "owned" layer (≥ 7/10), classify the moat:
- **Data moat** — customer-specific data accumulated over time
- **Workflow moat** — multi-step lock-in across user's daily routine
- **Distribution moat** — you reach customers cheaper than competitors
- **Brand moat** — trust + name recognition in a vertical
- **Integration moat** — you're plugged into the customer's other tools

### Step 4: Spot the leak
Ask: "Of your top 5 churned customers in the last 90 days, how many cited a competing AI product as the alternative?"
- ≥ 3 → wrapper-zone. The model is doing the work; the harness isn't differentiating.
- ≤ 1 → moat is real (or there are other reasons people leave; investigate).

### Step 5: 30-day moat sprint
Pick the WEAKEST owned layer (lowest score). Plan one 30-day sprint to lift it 2 points.

## Output

```
HARNESS AUDIT — [Product name]
Date: [today]

Layer scores:           Tools __  Skills __  Context __  Guardrails __  Permissions __
Wrapper test:           [Die / Lose / Survive]
Moat type:              [Data / Workflow / Distribution / Brand / Integration / NONE]
Top leak:               [layer]
30-day sprint:          [specific action to lift weakest layer]
```

## Hard rules
- ❌ Don't accept "better prompts" as a moat. Better prompts get copied in a weekend.
- ❌ Don't accept "we're the first" as a moat unless first-mover advantage compounds.
- ❌ Don't accept "we're cheaper" as a moat. Race-to-bottom kills startups.

## Source
[Lesson 02: The Harness Is the Moat](../../02-the-harness-is-the-moat/README.md)
