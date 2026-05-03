"""Tool definitions for Claude API tool_use."""

TOOL_DEFINITIONS = [
    {
        "name": "web_search",
        "description": "Search the web for information. Use for market research, competitor analysis, TAM data, industry reports, G2/Capterra reviews, and company information.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query. Be specific — include company names, product categories, and what you're looking for."
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "web_fetch",
        "description": "Fetch and extract content from a specific URL. Use to scrape company websites, competitor pages, pricing pages, and G2 review pages.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to fetch content from."
                },
                "extract": {
                    "type": "string",
                    "description": "What to extract from the page: 'all', 'pricing', 'positioning', 'features', 'about'.",
                    "enum": ["all", "pricing", "positioning", "features", "about"]
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "save_section",
        "description": "Save a completed GTM section to the document. Called after each step is reviewed and approved by the user.",
        "input_schema": {
            "type": "object",
            "properties": {
                "section_number": {
                    "type": "integer",
                    "description": "Section number (1-5)"
                },
                "section_title": {
                    "type": "string",
                    "description": "Section title"
                },
                "content": {
                    "type": "string",
                    "description": "The full markdown content for this section"
                }
            },
            "required": ["section_number", "section_title", "content"]
        }
    }
]
