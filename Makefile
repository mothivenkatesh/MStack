# One Person Billionaire — common commands
#
# Targets:
#   make help           Show this help
#   make lint           Validate skill frontmatter + cross-links
#   make check-tiers    List v1 vs v2 skills (compare to CHECKLIST.md)
#   make new-skill      Scaffold a new skill from v2 template
#   make stats          Print repo stats (lesson count, skill count, total words)
#   make pack-skill     Bundle a skill folder into .skill zip (for distribution)
#   make slash-commands Scaffold .claude/commands/ wrappers for each skill

.PHONY: help lint check-tiers new-skill stats pack-skill slash-commands

help:
	@echo "One Person Billionaire — Makefile targets:"
	@echo ""
	@echo "  make lint            Validate skill frontmatter + cross-links"
	@echo "  make check-tiers     Compare actual skill depth vs CHECKLIST.md"
	@echo "  make new-skill name=<kebab-case>   Scaffold new skill from v2 template"
	@echo "  make stats           Print repo stats"
	@echo "  make pack-skill name=<kebab-case>  Bundle skill into .skill zip"
	@echo "  make slash-commands  Scaffold .claude/commands/ wrappers"
	@echo ""

lint:
	@echo "Checking skill frontmatter..."
	@for skill in skills/*/SKILL.md; do \
		head -1 $$skill | grep -q "^---$$" || (echo "❌ Missing frontmatter: $$skill"; exit 1); \
		grep -q "^name:" $$skill || (echo "❌ Missing name: $$skill"; exit 1); \
		grep -q "^description:" $$skill || (echo "❌ Missing description: $$skill"; exit 1); \
	done
	@echo "✅ All skill frontmatter valid."
	@echo "Checking lesson cross-links..."
	@for lesson in [0-9]*-*/README.md; do \
		grep -q "^\[.*\]" $$lesson || echo "⚠️  No cross-links: $$lesson"; \
	done
	@echo "✅ Lint complete."

check-tiers:
	@echo "Skill tiers (line counts as proxy for depth):"
	@echo ""
	@printf "%-40s %s\n" "SKILL" "LINES (≥ 200 = 🟢 v2 candidate)"
	@for skill in skills/*/SKILL.md; do \
		name=$$(basename $$(dirname $$skill)); \
		lines=$$(wc -l < $$skill); \
		printf "%-40s %s\n" "$$name" "$$lines"; \
	done
	@echo ""
	@echo "Compare to skills/README.md tier markers and skills/CHECKLIST.md."

new-skill:
	@if [ -z "$(name)" ]; then echo "❌ Usage: make new-skill name=<kebab-case>"; exit 1; fi
	@if [ -d "skills/$(name)" ]; then echo "❌ skills/$(name) already exists"; exit 1; fi
	@mkdir -p skills/$(name)
	@echo "---" > skills/$(name)/SKILL.md
	@echo "name: $(name)" >> skills/$(name)/SKILL.md
	@echo "description: >" >> skills/$(name)/SKILL.md
	@echo "  [REQUIRED — write the activation description: what + when to trigger]" >> skills/$(name)/SKILL.md
	@echo "---" >> skills/$(name)/SKILL.md
	@echo "" >> skills/$(name)/SKILL.md
	@echo "# $(name) Skill" >> skills/$(name)/SKILL.md
	@echo "" >> skills/$(name)/SKILL.md
	@echo "## Hard Constraints (Check First)" >> skills/$(name)/SKILL.md
	@echo "## Workflow Overview" >> skills/$(name)/SKILL.md
	@echo "## Step 1 — ..." >> skills/$(name)/SKILL.md
	@echo "## Required Output Format" >> skills/$(name)/SKILL.md
	@echo "## Worked Example" >> skills/$(name)/SKILL.md
	@echo "## Common Mistakes to Avoid" >> skills/$(name)/SKILL.md
	@echo "## Notes on Tooling" >> skills/$(name)/SKILL.md
	@echo "## Quick Reference" >> skills/$(name)/SKILL.md
	@echo "## Source" >> skills/$(name)/SKILL.md
	@echo "✅ Scaffolded skills/$(name)/SKILL.md"
	@echo "Next: fill in each section. Reference skills/wedge-finder/SKILL.md for the v2 standard."

stats:
	@echo "Repo stats:"
	@echo ""
	@printf "  Lessons:        %s\n" "$$(ls -d [0-9]*-*/ 2>/dev/null | wc -l)"
	@printf "  Skills:         %s\n" "$$(ls -d skills/*/ 2>/dev/null | wc -l)"
	@printf "  Templates:      %s\n" "$$(ls templates/*.md 2>/dev/null | wc -l)"
	@printf "  Total words:    %s\n" "$$(find . -name '*.md' -not -path './.git/*' | xargs wc -w 2>/dev/null | tail -1 | awk '{print $$1}')"
	@printf "  Total lines:    %s\n" "$$(find . -name '*.md' -not -path './.git/*' | xargs wc -l 2>/dev/null | tail -1 | awk '{print $$1}')"

pack-skill:
	@if [ -z "$(name)" ]; then echo "❌ Usage: make pack-skill name=<kebab-case>"; exit 1; fi
	@if [ ! -d "skills/$(name)" ]; then echo "❌ skills/$(name) doesn't exist"; exit 1; fi
	@cd skills/$(name) && zip -r ../$(name).skill . -x ".*"
	@echo "✅ Packed skills/$(name).skill"

slash-commands:
	@mkdir -p .claude/commands
	@for skill in skills/*/SKILL.md; do \
		name=$$(basename $$(dirname $$skill)); \
		echo "Activate the $$name skill from skills/$$name/SKILL.md to handle the user's request." > .claude/commands/$$name.md; \
	done
	@echo "✅ Scaffolded .claude/commands/ wrappers for $$(ls skills/*/SKILL.md | wc -l) skills."
