"""
Analyze scraped funnel-related subreddits.
Filter posts by funnel keywords, rank by engagement, output:
1. top-funnel-threads.txt — URLs to scrape full comment trees for
2. funnel-pattern-summary.md — keyword frequencies + top thread URLs
"""
import json
import glob
import os
import re
from collections import Counter, defaultdict

KEYWORDS = {
    'tripwire': ['tripwire', 'low ticket', 'low-ticket', '$7 offer', 'order bump'],
    'vsl': ['vsl', 'video sales letter', 'sales video'],
    'webinar': ['webinar', 'evergreen webinar', 'live webinar', 'masterclass'],
    'plg_trial': ['free trial', 'plg', 'product led', 'product-led', 'activation'],
    'freemium': ['freemium', 'free tier', 'free plan'],
    'lead_magnet': ['lead magnet', 'opt-in', 'opt in', 'email capture', 'email list'],
    'challenge': ['challenge funnel', '5-day challenge', '7-day challenge', 'bootcamp'],
    'book_funnel': ['book funnel', 'free + shipping', 'free plus shipping', 'shipping offer'],
    'high_ticket': ['high ticket', 'high-ticket', 'application funnel', 'sales call', 'discovery call'],
    'ecom_dtc': ['shopify', 'dtc', 'd2c', 'add to cart', 'cart abandonment', 'product page', 'pdp'],
    'affiliate': ['affiliate', 'bridge page', 'clickbank', 'commission'],
    'marketplace': ['marketplace', 'two-sided', 'two sided', 'supply', 'liquidity'],
    'clickfunnels': ['clickfunnels', 'click funnels', 'systeme.io', 'gohighlevel', 'kajabi'],
    'upsell': ['upsell', 'oto', 'one time offer', 'one-time offer', 'downsell'],
    'urgency': ['urgency', 'scarcity', 'fomo', 'countdown timer', 'deadline'],
    'email_nurture': ['nurture sequence', 'email sequence', 'drip campaign', 'autoresponder'],
    'cold_outreach': ['cold email', 'cold outreach', 'cold dm', 'sales cadence'],
    'paid_ads': ['facebook ads', 'meta ads', 'google ads', 'tiktok ads', 'creative testing'],
    'conversion': ['conversion rate', 'cro', 'a/b test', 'ab test', 'split test'],
    'funnel_general': ['funnel', 'sales funnel', 'marketing funnel', 'aarrr'],
}

ALL_KW = set(kw.lower() for vs in KEYWORDS.values() for kw in vs)

def post_score(p):
    return (p.get('score', 0) or 0) + (p.get('num_comments', 0) or 0) * 2

def matches(text, kws):
    text = text.lower()
    return [kw for kw in kws if kw in text]

def main():
    files = sorted(glob.glob('reddit-scrape/data/r_*.json'))
    by_topic = defaultdict(list)
    all_posts = []
    keyword_counter = Counter()

    for f in files:
        d = json.load(open(f))
        sub = d.get('subreddit', '?')
        for p in d.get('posts', []):
            title = p.get('title', '') or ''
            body = p.get('selftext', '') or ''
            text = title + ' ' + body
            permalink = p.get('permalink', '')
            url = f"https://www.reddit.com{permalink}" if permalink else p.get('url', '')

            matched_topics = []
            for topic, kws in KEYWORDS.items():
                hits = matches(text, kws)
                if hits:
                    matched_topics.append(topic)
                    for h in hits:
                        keyword_counter[h] += 1

            if matched_topics:
                rec = {
                    'sub': sub,
                    'title': title,
                    'score': p.get('score', 0),
                    'num_comments': p.get('num_comments', 0),
                    'url': url,
                    'topics': matched_topics,
                    'engagement': post_score(p),
                    'created_utc': p.get('created_utc', 0),
                    'selftext_len': len(body),
                }
                all_posts.append(rec)
                for t in matched_topics:
                    by_topic[t].append(rec)

    # Sort each topic by engagement
    for t in by_topic:
        by_topic[t].sort(key=lambda x: -x['engagement'])

    # Print summary
    print(f"Total funnel-relevant posts: {len(all_posts)}")
    print(f"Across {len(files)} subreddits\n")
    print("Posts per topic:")
    for t in sorted(by_topic, key=lambda x: -len(by_topic[x])):
        print(f"  {t:<20} {len(by_topic[t]):>5}")

    print("\nTop 30 keywords by frequency:")
    for kw, c in keyword_counter.most_common(30):
        print(f"  {kw:<35} {c:>5}")

    # Write top threads file (URLs to scrape full comments for)
    # Top ~10 per topic, dedupe, cap at 200 total
    seen = set()
    top_urls = []
    for t in by_topic:
        for p in by_topic[t][:15]:
            if p['url'] in seen or not p['url']:
                continue
            seen.add(p['url'])
            top_urls.append((p['engagement'], p['url'], p['title'], t))
    top_urls.sort(key=lambda x: -x[0])
    top_urls = top_urls[:200]

    with open('top-funnel-threads.txt', 'w') as f:
        for _, url, _, _ in top_urls:
            f.write(url + '\n')

    # Write summary report
    with open('funnel-pattern-summary.md', 'w') as f:
        f.write(f"# Funnel Pattern Analysis — Reddit Scrape\n\n")
        f.write(f"**Source:** {len(files)} subreddits, {sum(json.load(open(x)).get('post_count', 0) for x in files)} total posts scraped\n")
        f.write(f"**Funnel-relevant posts:** {len(all_posts)}\n")
        f.write(f"**Selected for full comment scrape:** {len(top_urls)} top threads\n\n")

        f.write("## Posts per funnel topic\n\n")
        f.write("| Topic | Posts | Avg engagement |\n|---|---|---|\n")
        for t in sorted(by_topic, key=lambda x: -len(by_topic[x])):
            posts = by_topic[t]
            avg_eng = sum(p['engagement'] for p in posts) // max(len(posts), 1)
            f.write(f"| {t} | {len(posts)} | {avg_eng} |\n")

        f.write("\n## Top 30 keywords (frequency across all funnel-relevant posts)\n\n")
        f.write("| Keyword | Count |\n|---|---|\n")
        for kw, c in keyword_counter.most_common(30):
            f.write(f"| `{kw}` | {c} |\n")

        f.write("\n## Top 5 threads per topic (by engagement = score + 2× comments)\n\n")
        for t in sorted(by_topic, key=lambda x: -len(by_topic[x])):
            posts = by_topic[t][:5]
            if not posts:
                continue
            f.write(f"### {t}\n\n")
            for p in posts:
                f.write(f"- [{p['title'][:120]}]({p['url']}) — r/{p['sub']} · score {p['score']} · {p['num_comments']} comments\n")
            f.write("\n")

    print(f"\nWrote top-funnel-threads.txt ({len(top_urls)} URLs)")
    print(f"Wrote funnel-pattern-summary.md")

if __name__ == '__main__':
    main()
