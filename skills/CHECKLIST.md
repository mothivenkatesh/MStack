# Skill Deepening Checklist

Track which skills are at v1 (lean, ~100 lines, activatable) vs v2 (Growton-structure, ~250+ lines, with worked example + output format + tooling notes).

Run `make check-tiers` to see actual line counts vs intended tier.

## v2 Deep ✅ (8 skills)

- [x] `wedge-finder` — Lesson 05
- [x] `grand-slam-offer` — Lesson 08A
- [x] `cold-outbound-drafter` — Lesson 10
- [x] `self-automation-mapper` — Lesson 17
- [x] `agent-role-designer` — Lesson 18
- [x] `weekly-cadence-designer` — Lesson 19
- [x] `ten-year-statement-writer` — Lesson 20
- [x] (Growton imports below also v2 by definition)

## GTM Toolkit ✅ (4 skills, imported from Growton)

- [x] `icp-tam-research`
- [x] `buying-triggers-signals`
- [x] `one-to-one-email-writing`
- [x] `email-waterfall-enrichment`

## v1 Lean → needs deepening (14 skills)

Ordered by priority (highest leverage first):

- [ ] `pricing-tripler` — Lesson 13 — **HIGHEST PRIORITY**: pricing decisions are highest-ROI lever
- [ ] `margin-auditor` — Lesson 14 — kills most "AI startups"; needs worked example
- [ ] `retention-cohort-analyzer` — Lesson 15 — cohort math + interview script needed
- [ ] `riskiest-assumption-tester` — Lesson 06 — Mom-Test interview templates
- [ ] `agent-builder` — Lesson 01 — needs runnable Python/TS scaffolds
- [ ] `production-readiness-audit` — Lesson 04 — needs concrete checklist examples
- [ ] `boring-stack-auditor` — Lesson 04A — needs Inngest/Temporal/n8n decision tree
- [ ] `bottleneck-identifier` — Lesson 16 — diagnostic flowchart needed
- [ ] `compounding-content-builder` — Lesson 11 — needs vs-page + data-report templates
- [ ] `harness-auditor` — Lesson 02 — needs scoring rubric for the 5 layers
- [ ] `multi-agent-decision` — Lesson 03 — needs cost-math worked example
- [ ] `business-shape-classifier` — Lesson 07 — needs trait-scoring worksheet
- [ ] `first-paid-thing-planner` — Lesson 08 — needs 7-day sprint plan template
- [ ] `build-in-public-drafter` — Lesson 09 — needs 4 archetype worked examples
- [ ] `community-engagement-planner` — Lesson 12 — needs platform-specific sub-flows

## v2 standard (the deepening target)

Each v2 skill must have:
1. **Frontmatter** — rich `description` with explicit trigger phrases
2. **Hard Constraints (Check First)** — max-N caps, required input fields, veto-list
3. **Workflow Overview** — ASCII / code block summary
4. **Step-by-step workflow** — numbered steps with sub-instructions
5. **Required Output Format** — exact tables, headings, emoji-tagged sections
6. **Worked Example** — one concrete walkthrough with placeholder data
7. **Common Mistakes to Avoid** — extensive bullet list
8. **Notes on Tooling** — what to use, in what order, with cost thresholds
9. **Quick Reference** — skim-readable summary at end
10. **Source** — link to source lesson

Reference exemplars:
- `skills/wedge-finder/SKILL.md` (v2)
- `skills/grand-slam-offer/SKILL.md` (v2)
- `skills/icp-tam-research/SKILL.md` (Growton-imported, v2 standard)
- `skills/one-to-one-email-writing/SKILL.md` (Growton-imported, v2 standard)

## How to claim a deepening

Pick a skill from the v1 list. Open a PR titled `Deepen <skill-name> v1 → v2`. Match the v2 standard above. Update this checklist by checking the box. Update `skills/README.md` to flip the tier marker from 🟡 to 🟢.

PRs welcome. The deepening is the harder half of the curriculum.
