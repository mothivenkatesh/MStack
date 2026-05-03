# Funnel Discourse Scrape Pipeline

Bundled scrape + analysis pipeline that produced [`funnel-templates.md`](../references/funnel-templates.md) Section 0. Re-run quarterly to refresh the discourse data — template popularity shifts (e.g., GoHighLevel rising, ClickFunnels declining) are themselves a signal.

## What's in here

| File | Purpose |
|---|---|
| `targets-funnels.txt` | 20 funnel-related subreddits to scrape |
| `analyze-funnels.py` | Filter scraped posts by funnel keywords; rank by engagement; output top 200 thread URLs |
| `deep-analyze.py` | Re-process posts + full comment trees; tally template / anti-pattern / platform / guru mentions |
| `deep-analysis.json` | Last-run output: aggregated counts + top 10 hits per category, with permalinks + snippets |
| `funnel-pattern-summary.md` | Last-run output: per-topic post counts + top 5 thread URLs per topic |

## Pre-requisite

Clone [reddit-scraper](https://github.com/mothivenkatesh/reddit-scraper) (the user's own scraper — uses Reddit's public JSON endpoints, no auth needed):

```bash
git clone https://github.com/mothivenkatesh/reddit-scraper.git
cd reddit-scraper
pip install -r requirements.txt   # only `requests`
```

Copy these scripts into the cloned repo's root, then run.

## Pipeline (full re-run)

```bash
# 1) Scrape ~10K top posts across 20 funnel subreddits (~5-10 min)
python3 scrape.py --file targets-funnels.txt --sort top --max 1000

# 2) Filter for funnel-relevant posts; emit top 200 thread URLs (instant)
python3 analyze-funnels.py
#   -> top-funnel-threads.txt
#   -> funnel-pattern-summary.md

# 3) Pull full comment trees for those 200 threads (~5-10 min)
python3 scrape.py --file top-funnel-threads.txt

# 4) Tally template/anti-pattern/platform/guru mentions
python3 deep-analyze.py
#   -> deep-analysis.json (cited in funnel-templates.md Section 0)
```

Last run: 8,443 posts → 3,533 funnel-relevant → 200 top threads → 44,857 meaningful comments → **45,056 total conversations analyzed**.

## How to refresh `funnel-templates.md` Section 0

1. Re-run the pipeline above
2. Open `deep-analysis.json` — the structure is `{templates, anti_patterns, platforms, gurus}` each with top 10 hits sorted by Reddit score
3. Update Section 0 of [funnel-templates.md](../references/funnel-templates.md) with the refreshed counts and top thread URLs
4. Watch for shifts: a sudden jump in `gohighlevel` mentions, a collapse in `clickfunnels` mentions, a new platform appearing — each is a signal worth noting

## Caveats

- Reddit caps paginated results at ~500-1000 per subreddit (depends on sort)
- Polite delay is 1.5s between requests — full pipeline is ~15-20 min total
- Keyword filtering uses substring matching, which is noisy for short keywords (e.g., `cro` matches `macro`); the topic-level filtering compensates
- Two subreddits (r/Conversion, r/landingpages) returned empty in last run — likely private/restricted; OK to ignore
