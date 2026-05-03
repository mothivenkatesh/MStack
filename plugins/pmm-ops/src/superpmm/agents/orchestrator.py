"""SuperPMM Orchestrator — chains 5 agents into a GTM workflow."""

import os
import datetime
import anthropic
from ..config import ANTHROPIC_API_KEY
from ..prompts import (
    ORCHESTRATOR_PROMPT,
    RESEARCH_PROMPT,
    CI_PROMPT,
    PRFAQ_PROMPT,
    POSITIONING_PROMPT,
    GTM_PLAN_PROMPT,
)
from ..prompts.discovery import DISCOVERY_PROMPT
from ..tools.web import web_fetch
from ..tools.file_reader import read_uploaded_file
from .runner import run_agent


STEPS = [
    {
        "number": 0,
        "name": "Discovery",
        "prompt": DISCOVERY_PROMPT,
        "use_tools": True,
        "description": "Understanding the product deeply before building any strategy — asking the right questions first",
    },
    {
        "number": 1,
        "name": "Research & ICP",
        "prompt": RESEARCH_PROMPT,
        "use_tools": True,
        "description": "Defining your ICP, personas, and market size",
    },
    {
        "number": 2,
        "name": "Competitive Intelligence",
        "prompt": CI_PROMPT,
        "use_tools": True,
        "description": "Mapping your competitive landscape",
    },
    {
        "number": 3,
        "name": "PRFAQ",
        "prompt": PRFAQ_PROMPT,
        "use_tools": False,
        "description": "Building your internal press release and FAQ",
    },
    {
        "number": 4,
        "name": "Positioning & Messaging",
        "prompt": POSITIONING_PROMPT,
        "use_tools": False,
        "description": "Crafting your positioning statement and message house",
    },
    {
        "number": 5,
        "name": "GTM Launch Plan",
        "prompt": GTM_PLAN_PROMPT,
        "use_tools": False,
        "description": "Building your tiered launch plan",
    },
]


class SuperPMMOrchestrator:
    """Orchestrates the 5-step GTM workflow."""

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self.sections = {}  # step_number -> markdown output
        self.product_name = ""
        self.initial_context = ""

    def run(self):
        """Run the full interactive GTM workflow."""
        self._print_welcome()
        self._collect_input()

        for step in STEPS:
            self._run_step(step)

        self._compile_and_save()

    def _print_welcome(self):
        print("\n" + "=" * 60)
        print("  SuperPMM — Build your GTM in 60 minutes")
        print("=" * 60)
        print("""
  What are you working with?

  1. A website URL
  2. A PRD from your PM (file path)
  3. A PRFAQ document (file path)
  4. Call notes / meeting notes (file path or paste)
  5. An existing positioning doc (file path)
  6. Just a text description
""")

    def _collect_input(self):
        choice = input("  Enter choice (1-6): ").strip()
        print()

        if choice == "1":
            url = input("  Website URL: ").strip()
            self.product_name = url.replace("https://", "").replace("http://", "").split("/")[0]
            print(f"\n  Analyzing {url}...")
            site_content = web_fetch(url)
            self.initial_context = f"## Website Analysis\nURL: {url}\n\n{site_content}"

        elif choice in ("2", "3", "4", "5"):
            labels = {"2": "PRD", "3": "PRFAQ", "4": "Call notes", "5": "Positioning doc"}
            file_path = input(f"  Path to {labels[choice]} file: ").strip()
            self.product_name = input("  Product/company name: ").strip()
            print(f"\n  Reading {file_path}...")
            content = read_uploaded_file(file_path)
            doc_type = labels[choice]
            self.initial_context = f"## Uploaded {doc_type}\nSource: {file_path}\n\n{content}"

        elif choice == "6":
            self.product_name = input("  Product/company name: ").strip()
            desc = input("  Describe your product (2-3 sentences): ").strip()
            self.initial_context = f"## Product Description\n\n{desc}"

        else:
            print("  Invalid choice. Starting with text description.")
            self.product_name = input("  Product/company name: ").strip()
            desc = input("  Describe your product: ").strip()
            self.initial_context = f"## Product Description\n\n{desc}"

        # Ask for additional context
        extra = input("\n  Any additional context? (competitors, audience, goals — or press Enter to skip): ").strip()
        if extra:
            self.initial_context += f"\n\n## Additional Context from User\n{extra}"

    def _run_step(self, step: dict):
        print("\n" + "=" * 60)
        print(f"  STEP {step['number']} of 5: {step['name'].upper()}")
        print(f"  {step['description']}")
        print("=" * 60 + "\n")

        # Build accumulated context from all previous steps
        context = self.initial_context
        for prev_num in range(1, step["number"]):
            if prev_num in self.sections:
                context += f"\n\n---\n\n{self.sections[prev_num]}"

        # Task message for this step
        task = f"Run Step {step['number']}: {step['name']} for the product described in the context. Follow your methodology and produce structured markdown output."

        print("  Working...\n")
        output = run_agent(
            client=self.client,
            system_prompt=step["prompt"],
            user_message=task,
            context=context,
            use_tools=step["use_tools"],
        )

        # Display output
        print(output)

        # Review gate
        print("\n" + "-" * 40)
        review = input("  Does this look right? (yes / edit / redo): ").strip().lower()

        if review == "redo":
            print("\n  Regenerating...\n")
            output = run_agent(
                client=self.client,
                system_prompt=step["prompt"],
                user_message=task + "\n\nThe user asked for a redo. Generate a different, improved version.",
                context=context,
                use_tools=step["use_tools"],
            )
            print(output)

        elif review == "edit":
            edits = input("  What should I change? ").strip()
            print("\n  Revising...\n")
            output = run_agent(
                client=self.client,
                system_prompt=step["prompt"],
                user_message=task + f"\n\nThe user wants these changes: {edits}\n\nHere is the previous output to revise:\n\n{output}",
                context=context,
                use_tools=step["use_tools"],
            )
            print(output)

        self.sections[step["number"]] = output
        print(f"\n  Step {step['number']} saved.\n")

    def _compile_and_save(self):
        """Compile all sections into one GTM document and save."""
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        safe_name = "".join(c if c.isalnum() or c in "-_ " else "" for c in self.product_name).strip().replace(" ", "-")

        doc = f"# GTM Document: {self.product_name}\n"
        doc += f"*Generated by SuperPMM — {date}*\n\n"
        doc += "---\n\n"

        for step_num in sorted(self.sections.keys()):
            doc += self.sections[step_num]
            doc += "\n\n---\n\n"

        # Save to file
        output_dir = os.path.expanduser("~/Documents")
        os.makedirs(output_dir, exist_ok=True)
        filename = f"SuperPMM-{safe_name}-GTM-{date}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(doc)

        print("\n" + "=" * 60)
        print("  YOUR GTM DOCUMENT IS READY")
        print("=" * 60)
        print(f"""
  Saved to: {filepath}

  It contains:
  1. ICP Definition + TAM Sizing
  2. Competitive Landscape
  3. Internal PRFAQ
  4. Positioning + Message House
  5. GTM Launch Plan

  Total sections: {len(self.sections)}
  """)
