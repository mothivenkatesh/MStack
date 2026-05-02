# CLAUDE.md

This file is for Claude Code specifically. For other AI coding agents (Cursor, Codex, Gemini CLI, OpenHands), see [AGENTS.md](./AGENTS.md) — same instructions, AGENTS.md is the cross-tool standard.

> All conventions, repo structure, and contribution rules: see [AGENTS.md](./AGENTS.md).

## Claude Code specifics

### Skills auto-discovery

The `skills/` directory follows the agentskills.io spec. To make them auto-discover when running Claude Code in this repo:

```bash
cp -r skills/ .claude/skills/
```

Or symlink:

```bash
mkdir -p .claude
ln -s ../skills .claude/skills
```

After that, all 26 skills are available — Claude will activate them based on the `description` field in each frontmatter when your prompt matches.

### Recommended slash commands

The skills are designed to be invoked via natural language ("build me a wedge finder for X"), but for muscle memory you can wrap them as slash commands in `.claude/commands/`. See [`Makefile`](./Makefile) `make slash-commands` to scaffold.

### MCP integration

If you use MCPs in this repo, the recommended set:
- **Inngest MCP** — for the workflow specs in `code/`
- **GitHub MCP** — for repo operations
- **Stripe MCP** — for the pricing + margin skills' worked examples

None are required; the skills work without MCP.

## Conventions specific to Claude Code

When generating code or content for this repo:
- Default model: Claude Sonnet 4.6
- For skill `description` fields (which load at startup): keep under 200 tokens
- For SKILL.md bodies: target ≤ 5,000 tokens (enforced by spec for performance)
- For lesson READMEs: 800-1500 words for v2 lessons; 200-500 for short ones
