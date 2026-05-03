"""Agent runner — executes a single agent step with tool use."""

import json
import anthropic
from ..config import MODEL, MAX_TOKENS
from ..tools.web import web_search, web_fetch
from ..tools.definitions import TOOL_DEFINITIONS


def run_agent(
    client: anthropic.Anthropic,
    system_prompt: str,
    user_message: str,
    context: str = "",
    use_tools: bool = True,
    model: str = None,
) -> str:
    """Run a single agent step with optional tool use.

    Args:
        client: Anthropic client
        system_prompt: The agent's system prompt (methodology + output format)
        user_message: The user's input for this step
        context: Accumulated context from previous steps
        use_tools: Whether to enable web_search and web_fetch tools
        model: Override model (default from config)

    Returns:
        The agent's final response text
    """
    model = model or MODEL
    messages = []

    # Build the user message with accumulated context
    full_message = ""
    if context:
        full_message += f"## Context from Previous Steps\n\n{context}\n\n---\n\n"
    full_message += f"## Current Task\n\n{user_message}"

    messages.append({"role": "user", "content": full_message})

    # Tools for research/CI steps, none for PRFAQ/positioning/GTM
    tools = TOOL_DEFINITIONS if use_tools else []

    # Agentic loop — keep running until the agent stops calling tools
    while True:
        response = client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            messages=messages,
            tools=tools if tools else anthropic.NOT_GIVEN,
        )

        # Check if the agent wants to use tools
        tool_calls = [b for b in response.content if b.type == "tool_use"]

        if not tool_calls:
            # No tool calls — agent is done, extract text response
            text_blocks = [b.text for b in response.content if b.type == "text"]
            return "\n".join(text_blocks)

        # Process tool calls
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for tool_call in tool_calls:
            result = _execute_tool(tool_call.name, tool_call.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_call.id,
                "content": result,
            })

        messages.append({"role": "user", "content": tool_results})


def _execute_tool(name: str, inputs: dict) -> str:
    """Execute a tool call and return the result."""
    if name == "web_search":
        return web_search(inputs["query"])
    elif name == "web_fetch":
        return web_fetch(inputs["url"], inputs.get("extract", "all"))
    elif name == "save_section":
        # save_section is handled by the orchestrator, not here
        return json.dumps({"status": "saved", "section": inputs["section_number"]})
    else:
        return f"Unknown tool: {name}"
