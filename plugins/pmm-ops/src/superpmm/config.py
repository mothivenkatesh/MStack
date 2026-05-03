"""Configuration for SuperPMM agents."""

import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-20250514"
MODEL_DEEP = "claude-opus-4-0-20250514"
MAX_TOKENS = 8192
