"""System prompts for each SuperPMM agent."""

from .orchestrator import ORCHESTRATOR_PROMPT
from .discovery import DISCOVERY_PROMPT
from .research import RESEARCH_PROMPT
from .ci import CI_PROMPT
from .prfaq import PRFAQ_PROMPT
from .positioning import POSITIONING_PROMPT
from .gtm_plan import GTM_PLAN_PROMPT

__all__ = [
    "ORCHESTRATOR_PROMPT",
    "DISCOVERY_PROMPT",
    "RESEARCH_PROMPT",
    "CI_PROMPT",
    "PRFAQ_PROMPT",
    "POSITIONING_PROMPT",
    "GTM_PLAN_PROMPT",
]
