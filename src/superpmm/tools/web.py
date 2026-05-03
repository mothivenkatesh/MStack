"""Web tools for research and competitive intelligence."""

import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import re


def web_search(query: str) -> str:
    """Search the web using a simple search API.

    In production, replace with:
    - Tavily API (best for AI agents — tavily.com)
    - SerpAPI
    - Brave Search API
    - Google Custom Search API
    """
    try:
        # Using DuckDuckGo instant answer API as a free fallback
        encoded = urllib.parse.quote_plus(query)
        url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1"
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers={"User-Agent": "SuperPMM/0.1"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        results = []
        if data.get("Abstract"):
            results.append(f"Summary: {data['Abstract']}")
        if data.get("RelatedTopics"):
            for topic in data["RelatedTopics"][:5]:
                if isinstance(topic, dict) and topic.get("Text"):
                    results.append(f"- {topic['Text']}")

        if results:
            return "\n".join(results)
        return f"No instant results for '{query}'. Try a more specific query or use web_fetch on a specific URL."

    except Exception as e:
        return f"Search error: {str(e)}. Try web_fetch with a specific URL instead."


def web_fetch(url: str, extract: str = "all") -> str:
    """Fetch and extract content from a URL.

    In production, replace with:
    - Firecrawl (firecrawl.dev) — best for structured extraction
    - Jina Reader API (r.jina.ai) — simple, free
    - Playwright for JS-heavy sites
    """
    try:
        # Use Jina Reader for clean extraction (free, no API key needed)
        jina_url = f"https://r.jina.ai/{url}"
        req = urllib.request.Request(
            jina_url,
            headers={
                "User-Agent": "SuperPMM/0.1",
                "Accept": "text/plain"
            }
        )
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="replace")

        # Truncate to avoid token limits
        max_chars = 8000
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n[... truncated for length]"

        if extract == "pricing":
            return _extract_section(content, ["pricing", "price", "plan", "tier", "cost", "per month", "per year"])
        elif extract == "positioning":
            return _extract_section(content, ["hero", "tagline", "value prop", "why", "solution"])
        elif extract == "features":
            return _extract_section(content, ["feature", "capability", "what you get", "included"])
        elif extract == "about":
            return _extract_section(content, ["about", "mission", "story", "founded", "team"])

        return content

    except Exception as e:
        return f"Fetch error for {url}: {str(e)}"


def _extract_section(content: str, keywords: list) -> str:
    """Extract relevant sections from content based on keywords."""
    lines = content.split("\n")
    relevant = []
    capture = False
    for line in lines:
        lower = line.lower()
        if any(kw in lower for kw in keywords):
            capture = True
        if capture:
            relevant.append(line)
            if len(relevant) > 50:
                break
        if capture and line.strip() == "" and len(relevant) > 5:
            capture = False
    return "\n".join(relevant) if relevant else content[:3000]
