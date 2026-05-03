# SuperPMM V1: Built with Claude Managed Agents

## Why This Approach

| Full Web App (Original Plan) | Claude Managed Agents |
|---|---|
| 6-8 weeks to build | Days to ship |
| Next.js + FastAPI + PostgreSQL + Redis | Claude Agent SDK handles everything |
| Custom auth, payments, hosting | Ship as CLI first, add web later |
| Need frontend engineer + backend engineer | One person can build the whole thing |
| LLM orchestration from scratch | Claude handles orchestration natively |
| Custom context management | Agent SDK has built-in context sharing |
| Website scraping infra | WebFetch/WebSearch tools built in |
| File parsing infra | Claude reads PDFs, XLSX, DOCX natively |

**The insight:** SuperPMM V1 is fundamentally a multi-step guided workflow where each step is an AI agent that reads context, generates structured output, and passes it to the next step. That's exactly what Claude managed agents do.

---

## Architecture: 5 Agents in a Chain

```
┌─────────────────────────────────────────────────────────┐
│                 SUPERPMM ORCHESTRATOR                     │
│           (Main agent — routes the workflow)               │
│                                                           │
│  Input: URL / PRD / PRFAQ / Call Notes / Existing Doc     │
│  Output: Complete GTM Document (markdown)                  │
│                                                           │
│  Step 0: Detect input type → route to right starting point│
│  Step 1: Spawn Research Agent                              │
│  Step 2: Spawn CI Agent (with Step 1 context)             │
│  Step 3: Spawn PRFAQ Agent (with Steps 1-2 context)       │
│  Step 4: Spawn Positioning Agent (with Steps 1-3 context) │
│  Step 5: Spawn GTM Plan Agent (with Steps 1-4 context)    │
│  Final: Compile all outputs → exportable GTM document     │
└─────────────────────────────────────────────────────────┘
```

Each agent is a Claude managed subagent with:
- A focused system prompt (the methodology + examples)
- Access to shared context (previous agents' outputs)
- Tool access (WebFetch, WebSearch for research/CI)
- Structured output format (markdown sections)

---

## Agent Definitions

### Agent 0: Orchestrator (Main Agent)

```
Role: Routes the GTM workflow, manages context passing between agents,
      compiles final output.

Trigger: User starts a new GTM project

Flow:
  1. Ask: "What are you building a GTM for?"
     → Accept: URL, file upload (PRD/PRFAQ/notes/doc), or text description
  2. Detect input type and pre-extract context
  3. Run agents 1-5 sequentially, passing accumulated context
  4. After each agent: show output, ask "Does this look right? Edit anything?"
  5. Compile final GTM document
  6. Export as markdown file

Tools: All (delegates to subagents)
```

### Agent 1: Research Agent

```
Role: Build ICP definition, persona sketches, TAM sizing, "current way" mapping

System prompt includes:
  - FletchPMM ICP Scorecard methodology (Retention, Access, Velocity, Activation)
  - FletchPMM "unit of work" + "current way" concepts
  - Winning by Design SPICED framework
  - TAM triangulation method (bottom-up + top-down + analogy)
  - Sample ICP one-pager (filled example shown to user)
  - Sample TAM calculation (with real numbers)

Tools needed:
  - WebFetch (scrape company website for product/audience signals)
  - WebSearch (market sizing data, industry reports, company info)

Input: Company URL + any uploaded context (PRD, notes, etc.)

Output (structured markdown):
  ## ICP Definition
  - Company type, industry, size
  - Buyer persona (title, pain, decision criteria)
  - End user persona
  - "Current way" (what they do today without the product)
  - Buying triggers

  ## TAM Sizing
  - Bottom-up: [X accounts × $Y ACV = $Z]
  - Top-down: [market size × addressable share]
  - Analogy: [comparable product/market]
  - SOM: [reachable segment NOW]

  ## ICP Scorecard
  - Retention: X/10
  - Access: X/10
  - Sales Velocity: X/10
  - Activation: X/10

Human review gate: "Does this ICP look right? Edit anything."
```

### Agent 2: Competitive Intelligence Agent

```
Role: Map competitive landscape, identify differentiation angles,
      determine market maturity phase

System prompt includes:
  - FletchPMM competitive vs contextual differentiation framework
  - 3 types of competition (direct, status quo, adjacent)
  - 3 phases of differentiation (early/growing/mature market)
  - How to extract strengths/weaknesses from G2 reviews
  - Sample competitive brief format

Tools needed:
  - WebSearch (competitor info, G2/Capterra data, pricing pages)
  - WebFetch (scrape competitor websites for positioning/pricing)

Input: ICP from Agent 1 + company URL + any competitor names user provided

Output (structured markdown):
  ## Competitive Landscape

  ### Direct Competitors
  For each (top 3):
  - Name + one-line description
  - Their positioning (H1/H2 from website)
  - Pricing model + price points
  - Strengths (from reviews/website)
  - Weaknesses (from reviews/website)

  ### Status Quo Competitor
  - What prospects do today without ANY product (from Agent 1 "current way")

  ### Market Maturity Assessment
  - Phase: [Early/Growing/Mature]
  - Implication: [Contextual/Competitive/Ecosystem differentiation]

  ### Differentiation Angles
  1. [Angle 1 — based on competitor weaknesses vs your strengths]
  2. [Angle 2]
  3. [Angle 3]

Human review gate: "Are these the right competitors? Anything to add or change?"
```

### Agent 3: PRFAQ Agent

```
Role: Generate internal press release + FAQ using Amazon working-backwards format

System prompt includes:
  - Amazon PRFAQ format and methodology
  - How to write a compelling problem paragraph
  - How to link solution to differentiation (from CI agent)
  - Sample PRFAQ (filled example)
  - "If the press release is hard to write, the product isn't clear enough"

Tools needed: None (works from accumulated context)

Input: All context from Agents 1-2

Output (structured markdown):
  ## Internal Press Release

  ### Headline
  [Company] Launches [Product] to Help [ICP] [Solve Problem]

  ### Sub-headline
  [One sentence — key benefit + differentiator]

  ### Opening Paragraph
  [City, Date] — [Company] today announced...

  ### Problem Paragraph
  "Today, [ICP] struggles with [problem]..."

  ### Solution Paragraph
  "[Product] solves this by [how]. Unlike [competitors/status quo]..."

  ### Customer Quote
  [Hypothetical or real — flagged if hypothetical]

  ### Getting Started
  [How to access/try/buy]

  ## FAQ
  ### Customer FAQs (auto-generated)
  ### Internal/Sales FAQs (auto-generated)

Human review gate: "This is your internal alignment doc. Edit the narrative until it feels right."
```

### Agent 4: Positioning Agent

```
Role: Generate positioning statement, message house, elevator pitches,
      persona-specific messaging, competitive messaging

System prompt includes:
  - FletchPMM Positioning Anchors (Market Elements × Product Elements)
  - FletchPMM MVP Positioning (4 common pairs)
  - Atlassian Message House structure (roof + 3 pillars + proof points)
  - "Only we can say this" test for each pillar
  - Capability vs feature vs benefit distinction (FletchPMM)
  - Sample positioning statement + message house (filled examples)
  - Persona-specific messaging matrix format (persona × pain × message × proof)

Tools needed: None (works from accumulated context)

Input: All context from Agents 1-3

Output (structured markdown):
  ## Positioning

  ### Positioning Anchors
  - Primary: [Market Element] + [Product Element]
  - Secondary: [...]

  ### Positioning Statement
  "For [ICP] who [problem], [Product] is a [category] that [key benefit].
   Unlike [competitive alternative], [Product] [key differentiator]."

  ### Positioning Line (one-liner)
  "[10-word version]"

  ## Message House
  ┌─── Roof: [Positioning statement] ───┐
  │ Pillar 1        │ Pillar 2        │ Pillar 3        │
  │ [Value prop]     │ [Value prop]     │ [Value prop]     │
  │ [Proof point]    │ [Proof point]    │ [Proof point]    │
  │ [Customer pain]  │ [Customer pain]  │ [Customer pain]  │

  ## Elevator Pitches
  - 10-word: [...]
  - 30-word: [...]
  - 100-word: [...]

  ## Persona-Specific Messaging
  | Persona | Pain Point | Message | Proof Point |
  |---------|-----------|---------|-------------|
  | [Buyer] | [...] | [...] | [...] |
  | [User]  | [...] | [...] | [...] |

  ## Competitive Messaging
  - vs [Competitor A]: "Unlike [A] which [weakness], we [strength]"
  - vs [Competitor B]: ...
  - vs Status Quo: "Instead of [current way], [Product] lets you..."

  ## Headline Variants (for A/B testing)
  1. [Category-anchor variant]
  2. [Problem-anchor variant]
  3. [Outcome-anchor variant]

Human review gate: "This is your external messaging. Refine until every line passes
                    the 'would I say this at a dinner party?' test."
```

### Agent 5: GTM Plan Agent

```
Role: Generate tiered launch plan with timeline, stakeholders, assets, metrics

System prompt includes:
  - Launch tiering methodology (Tier 1-4 with criteria)
  - DIN framework (Decide/Input/Notify) for stakeholder management
  - T-minus week timeline structure (from AWS template)
  - Tier-appropriate asset checklists
  - Leading vs lagging metrics (Rinita Datta/Splunk framework)
  - Anti-metrics to avoid (from Hattie's 6 anti-patterns)
  - Sample launch plan (filled example)

Tools needed: None (works from accumulated context)

Input: All context from Agents 1-4

Output (structured markdown):
  ## Launch Plan

  ### Launch Tier: [1/2/3/4]
  Reasoning: [why this tier based on product impact, audience, competitive context]

  ### Timeline
  T-6 weeks: Finalize positioning & messaging ✓ (done in Step 4)
  T-5 weeks: Brief sales team
  T-4 weeks: Create launch assets
  T-3 weeks: Internal enablement
  T-2 weeks: Seed with beta customers
  T-1 week: Final reviews
  T-0: LAUNCH
  T+1 week: Monitor metrics
  T+2 weeks: Retrospective

  ### Stakeholders (DIN)
  - Decide: [PMM — you]
  - Input: [PM, Sales lead, Content lead]
  - Notify: [Exec team, CS, Support, Partners]

  ### Asset Checklist (tier-appropriate)
  ☐ [Asset 1]
  ☐ [Asset 2]
  ...

  ### Not Needed for This Tier
  ✗ [Asset that's overkill for this tier]

  ### Success Metrics
  Leading (first 2 weeks): [...]
  Lagging (30-90 days): [...]
  Anti-metrics (don't track): [...]

Human review gate: "Your launch plan is ready. Adjust timeline or assets as needed."
```

---

## Implementation Plan

### Option A: Claude Code Skill (Fastest — Ship in 2-3 days)

Build SuperPMM as a Claude Code skill that runs in the terminal:

```
User types: /superpmm
→ Skill loads the orchestrator prompt
→ Asks for input (URL, file, or description)
→ Runs 5 agents sequentially with human review gates
→ Outputs complete GTM document as markdown file
→ User copies to Notion/Google Docs/wherever
```

**Pros:** Ship in 2-3 days. Zero infrastructure. Free to use.
**Cons:** Terminal-only UX. No web interface. Limited to Claude Code users.

### Option B: Claude Agent SDK Web App (Ship in 1-2 weeks)

Build a simple web app using the Claude Agent SDK:

```python
# Simplified architecture
from anthropic import Anthropic
from claude_agent_sdk import Agent, AgentOrchestrator

# Define agents
research_agent = Agent(
    name="research",
    system_prompt=RESEARCH_SYSTEM_PROMPT,  # FletchPMM ICP methodology
    tools=["web_search", "web_fetch"],
)

ci_agent = Agent(
    name="competitive_intelligence",
    system_prompt=CI_SYSTEM_PROMPT,  # FletchPMM differentiation framework
    tools=["web_search", "web_fetch"],
)

prfaq_agent = Agent(
    name="prfaq",
    system_prompt=PRFAQ_SYSTEM_PROMPT,  # Amazon working-backwards
    tools=[],
)

positioning_agent = Agent(
    name="positioning",
    system_prompt=POSITIONING_SYSTEM_PROMPT,  # FletchPMM anchors + Message House
    tools=[],
)

gtm_agent = Agent(
    name="gtm_plan",
    system_prompt=GTM_SYSTEM_PROMPT,  # Launch tiering + DIN + metrics
    tools=[],
)

# Orchestrator chains them
orchestrator = AgentOrchestrator(
    agents=[research_agent, ci_agent, prfaq_agent, positioning_agent, gtm_agent],
    context_sharing="sequential",  # each agent inherits all previous outputs
    human_review_gates=True,  # pause after each agent for user review
)

# Run
result = orchestrator.run(
    input=user_input,  # URL, uploaded file, or text
    output_format="markdown",
)
```

**Pros:** Web UI. Shareable. Can charge for it.
**Cons:** 1-2 weeks to build. Need hosting.

### Option C: Hybrid — Skill First, Web Later

1. **Week 1:** Ship as Claude Code skill (`/superpmm`). Validate with 50-100 PMMs.
2. **Week 2-3:** Based on feedback, build web wrapper with Claude Agent SDK.
3. **Week 4:** Launch on Product Hunt with web UI.

**This is the recommended approach.** Ship the skill in days, validate the workflow, then wrap it in a web UI.

---

## The Claude Code Skill: `/superpmm`

### Skill Definition

```yaml
name: superpmm
description: "Build your Go-To-Market in 60 minutes. Guided workflow: Research → CI → PRFAQ → Positioning → GTM Plan."
trigger: "/superpmm"
```

### What Happens When User Types `/superpmm`

```
SUPERPMM: Welcome to SuperPMM — the GTM Builder.

  Let's build your Go-To-Market strategy.
  What are you working with?

  1. Website URL (I'll analyze your company)
  2. Upload a PRD from your PM
  3. Upload a PRFAQ
  4. Paste call notes / meeting notes
  5. Upload existing positioning doc (for refresh)

USER: [pastes URL or uploads file]

SUPERPMM: Analyzing... [uses WebFetch to scrape site]

  Got it. Here's what I found:
  - Product: [extracted]
  - Category: [extracted]
  - Audience signals: [extracted]
  - Pricing: [extracted]

  ═══════════════════════════════════════
  STEP 1 of 5: RESEARCH & ICP
  ═══════════════════════════════════════

  Let me build your ICP. First, a few questions:

  Who is your ideal customer?
  (Here's an example of a strong ICP definition:)
  [shows sample]

  ...

  [Agent 1 runs, produces ICP + TAM output]

  Here's your ICP and market sizing:
  [structured output]

  Does this look right? (yes / edit / redo)

USER: Looks good, but change the buyer to "Head of Compliance"

SUPERPMM: Updated. Moving to competitive analysis.

  ═══════════════════════════════════════
  STEP 2 of 5: COMPETITIVE INTELLIGENCE
  ═══════════════════════════════════════

  Searching for competitors... [uses WebSearch]
  Analyzing competitor websites... [uses WebFetch]

  [Agent 2 runs, produces CI output]

  ...

  [Continue through all 5 steps]

  ═══════════════════════════════════════
  YOUR GTM DOCUMENT IS READY
  ═══════════════════════════════════════

  I've saved your complete GTM document to:
  → /Users/you/Documents/SuperPMM-[ProductName]-GTM.md

  It includes:
  ✓ ICP Definition + TAM Sizing
  ✓ Competitive Landscape
  ✓ Internal PRFAQ
  ✓ Positioning + Message House
  ✓ GTM Launch Plan

  Want me to export to Notion? (y/n)
```

---

## What We Need to Build

### For the Claude Code Skill (Option A — 2-3 days):

1. **Orchestrator skill file** (`/superpmm` SKILL.md)
   - Routes workflow, manages state between steps
   - Handles 5 input modes
   - Compiles final output

2. **5 agent system prompts** (the methodology + examples + output format)
   - `research-agent-prompt.md`
   - `ci-agent-prompt.md`
   - `prfaq-agent-prompt.md`
   - `positioning-agent-prompt.md`
   - `gtm-plan-agent-prompt.md`

3. **Template library** (reference examples embedded in prompts)
   - Sample ICP one-pager
   - Sample competitive brief
   - Sample PRFAQ
   - Sample message house
   - Sample launch plan

4. **Output compiler** (combines all 5 outputs into one clean markdown doc)

That's it. No database. No auth. No payments. No hosting. Just well-crafted prompts + tools.

### Lines of Code Estimate

| Component | Estimated Size |
|---|---|
| Orchestrator skill | ~200 lines of markdown |
| 5 agent prompts | ~500 lines each = ~2,500 total |
| Template examples | ~1,000 lines |
| Output compiler logic | ~100 lines |
| **Total** | **~3,800 lines of markdown + prompts** |

Compare to the full web app:
| Component | Estimated Size |
|---|---|
| Next.js frontend | ~5,000+ lines |
| FastAPI backend | ~3,000+ lines |
| Database schema + migrations | ~500 lines |
| Auth + payments | ~1,000 lines |
| LLM orchestration | ~2,000 lines |
| Deployment config | ~500 lines |
| **Total** | **~12,000+ lines of code** |

**Claude managed agents = 70% less to build, ships 80% faster.**
