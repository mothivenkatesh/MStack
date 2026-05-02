# AGENTS.md

Instructions for AI coding agents (Claude Code, Cursor, Codex, Gemini CLI, OpenHands, etc.) working in this repository.

## What this repo is

**One Person Billionaire** — a 22-lesson curriculum + 26 Claude skills + templates + workflow specs for solo agent operators chasing outlier outcomes. Read [README.md](./README.md) before changing anything.

## Repo structure

```
.
├── README.md                       Master index
├── 00-the-honest-premise/          Read this first
├── 01-04                           Part 1: Engineering
├── 04A                             Interlude: Boring stack first
├── 05-08                           Part 2: Productizing
├── 08A                             Interlude: Grand Slam Offer
├── 09-12                           Part 3: Distribution
├── 13-16                           Part 4: Monetization
├── 17-20                           Part 5: Leverage
├── skills/                         26 Claude skills (22 curriculum + 4 GTM)
│   ├── README.md                   Skill index + tier markers (🟢 v2 / 🟡 v1)
│   ├── CHECKLIST.md                v1 → v2 deepening tracker
│   └── <skill-name>/SKILL.md       Each skill
├── templates/                      4 fillable canvases (Hormozi-style)
├── code/                           Workflow specs (Inngest examples)
├── CONTRIBUTING.md                 Lesson + skill template
├── LICENSE                         MIT
└── Makefile                        Common commands
```

## Conventions

### When adding / editing a lesson

- Each lesson lives in `NN-kebab-case-name/README.md`
- Always end with one concrete exercise
- Cross-link to `[← prev]` and `[next →]` at bottom
- Keep opinions; "it depends" is not a lesson

### When adding / editing a skill

- Each skill lives in `skills/<kebab-case>/SKILL.md`
- Frontmatter required: `name`, `description` (rich, with trigger phrases)
- v2 standard: hard constraints first → workflow overview → step-by-step → required output format → worked example → common mistakes → notes on tooling → quick reference
- See `skills/wedge-finder/SKILL.md` or `skills/grand-slam-offer/SKILL.md` for the pattern
- Mark tier in `skills/README.md` index

### When deepening a v1 → v2

- Pull from the [`skills/CHECKLIST.md`](./skills/CHECKLIST.md) tracker
- Match the v2 standard (see exemplars in `skills/agent-builder/SKILL.md`, `skills/wedge-finder/SKILL.md`, `skills/icp-tam-research/SKILL.md`)
- Update `skills/README.md` tier marker after deepening

### When committing

- Use the GitHub no-reply email format for commit author (already configured per-repo)
- Honest, descriptive commit messages — no AI emojis, no "✨ Initial commit ✨"
- Commit messages explain the *why*, not just the *what*

### Things to NEVER do without explicit user request

- Push to remote (commit yes, push no — let the user decide when to push)
- Change git config global settings
- Modify the Premise lesson's honesty about realistic outcomes
- Add hype language ("revolutionary", "world-class", "10x")
- Add emojis to lesson bodies (only used in skill output formats)
- Inflate scope — small surgical edits beat sprawling rewrites

## How to test changes

```bash
make lint            # Validate skill frontmatter + cross-links
make new-skill name=<kebab-case>   # Scaffold a new skill from the v2 template
make check-tiers     # Print which skills are v1 vs v2 (vs CHECKLIST.md)
```

## When in doubt

- **For a lesson:** does it pass the "would I be embarrassed reading this in 5 years?" test
- **For a skill:** does it push back when the user gives vague input?
- **For a template:** does it produce a fillable artifact, not free-form prose?

## Honest scope guard

If asked to "improve everything" or "make the whole repo deeper," push back: identify the highest-leverage 3 files to change. Sprawling rewrites lose to small surgical edits.
