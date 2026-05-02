---
name: agent-builder
description: >
  Builds the minimum viable agent — model + tools + the 30-line loop + 20 evals.
  Use when starting a new agent project, when the user says "build me an agent for X",
  or when an existing agent has gotten too complex and needs a rewrite from primitives.
license: MIT
metadata:
  source-lesson: 01
---

# Agent Builder

You build the smallest correct agent for the user's task — and refuse to add complexity until evals demand it.

## When to activate
- "Build an agent that ___"
- "I want to make an agent for ___"
- "How do I start an agent for ___"
- "Replace my LangGraph stack with the bare loop"

## The workflow

### Step 1: Force task specificity
Reject vague tasks. Push for one specific, recurring, measurable workflow.
- Bad: "An agent for content"
- Good: "Daily 8am: read my Twitter inbox, draft 3 reply candidates per DM from prospects, queue for my approval"

### Step 2: Pick the model
Default to Claude Sonnet 4.6. Push back if user wants Opus before evals justify it.
- Cheap/routing → Haiku 4.5
- Default → Sonnet 4.6
- Hard reasoning only → Opus 4.7

### Step 3: Define ≤ 5 tools
For each tool: name (verb_object), description (when AND why to use it), schema. Refuse > 5 tools at v0.

```python
{
  "name": "fetch_url",
  "description": "Fetch the raw HTML of a URL. Use when you need page content past the model's training data.",
  "input_schema": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}
}
```

### Step 4: Write the loop (30 lines, no framework)
```python
def agent(user_msg, tools):
    messages = [{"role": "user", "content": user_msg}]
    for _ in range(20):  # max iterations
        r = llm.create(messages=messages, tools=tools)
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason == "end_turn": return r.content
        for tc in r.tool_uses:
            result = execute(tc)
            messages.append({"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": tc.id, "content": result}
            ]})
    raise Exception("Max iterations exceeded")
```

### Step 5: Write 20 hand-graded evals BEFORE first user touches it
Mix: 15 happy paths, 3 edge cases, 2 adversarial. Each eval = (input, expected_tool, expected_pattern).

### Step 6: Add the bounds
- Max iterations (default 20)
- Per-session token budget (default 50K)
- Tool execution timeout (default 30s)

## Output

A runnable Python or TypeScript file with:
1. Tool definitions
2. The loop
3. 20 evals in `evals.yaml`
4. A `make run` and `make eval` command

## Hard rules
- ❌ No framework before the bare loop is shipped
- ❌ No vector DB at v0
- ❌ No multi-agent at v0 (use [`multi-agent-decision`](../multi-agent-decision/SKILL.md))
- ❌ No streaming, auth, or UI at v0
- ❌ No deployment until evals pass

## Source
[Lesson 01: The Minimum Viable Agent](../../01-the-minimum-viable-agent/README.md)
