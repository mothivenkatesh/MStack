"""
Deep analysis of scraped funnel threads + comments.
Produces a structured intelligence report mining REAL Reddit signal:
- Total conversation count (posts + comments)
- Top funnel-template patterns observed
- Real quoted insights with permalinks
- ClickFunnels-specific complaints/praise
- Anti-patterns mentioned by practitioners
"""
import json
import glob
import os
import re
from collections import Counter, defaultdict

# Funnel templates as observable patterns in the discourse
TEMPLATE_PATTERNS = {
    'tripwire_low_ticket': ['tripwire', 'low-ticket', 'low ticket', 'order bump', '$7 offer', '$27 offer', '$17 offer'],
    'vsl_application_call': ['vsl', 'video sales letter', 'sales call', 'discovery call', 'application funnel', 'strategy session'],
    'webinar_funnel': ['webinar', 'masterclass', 'evergreen webinar', 'live training'],
    'plg_free_trial': ['free trial', 'product-led', 'product led', 'plg', 'self-serve', 'self serve', 'activation'],
    'freemium': ['freemium', 'free tier', 'free plan', 'free forever'],
    'lead_magnet_nurture': ['lead magnet', 'opt-in', 'opt in', 'email capture', 'email list', 'nurture sequence', 'drip'],
    'challenge_funnel': ['challenge funnel', '5-day challenge', '7-day challenge', 'bootcamp funnel'],
    'book_funnel': ['book funnel', 'free + shipping', 'free plus shipping', '$7 book'],
    'high_ticket_app': ['high ticket', 'high-ticket', 'application form', 'qualifying call', 'sales close'],
    'ecom_pdp_checkout': ['shopify', 'product page', 'pdp', 'add to cart', 'cart abandonment', 'abandoned cart'],
    'affiliate_bridge': ['affiliate', 'bridge page', 'clickbank', 'commission', 'affiliate link'],
    'marketplace_2sided': ['marketplace', 'two-sided', 'two sided', 'supply side', 'demand side', 'liquidity'],
}

ANTI_PATTERNS = {
    'fake_urgency': ['fake urgency', 'fake scarcity', 'reset timer', 'fake countdown', 'manufactured urgency'],
    'too_many_upsells': ['too many upsells', 'upsell overload', 'aggressive upsell', 'upsell stack'],
    'message_mismatch': ['message mismatch', 'ad to landing', 'landing page mismatch', 'inconsistent messaging'],
    'no_followup': ['no follow up', 'no follow-up', 'one email', 'single email', 'follow up sequence'],
    'vanity_metrics': ['vanity metrics', 'open rate', 'meaningless metrics'],
    'cold_to_high_ticket': ['cold to high ticket', 'cold traffic high ticket', 'no warming'],
    'guru_scam': ['guru', 'scam', 'rug pull', 'snake oil', 'overpriced', 'ripoff', 'rip off'],
}

PLATFORM_MENTIONS = {
    'clickfunnels': ['clickfunnels', 'click funnels'],
    'gohighlevel': ['gohighlevel', 'go high level', 'ghl'],
    'kajabi': ['kajabi'],
    'systeme': ['systeme', 'systeme.io'],
    'kartra': ['kartra'],
    'leadpages': ['leadpages'],
    'unbounce': ['unbounce'],
    'shopify': ['shopify'],
    'klaviyo': ['klaviyo'],
}

GURU_MENTIONS = {
    'brunson': ['russell brunson', 'brunson', 'dotcom secrets', 'expert secrets'],
    'hormozi': ['hormozi', '$100m offers', '100m offers', 'acquisition.com'],
    'ovens': ['sam ovens', 'consulting.com'],
    'gadzhi': ['gadzhi', 'iag media', 'agency navigator'],
    'gordon': ['cole gordon', 'closers.io'],
    'tai_lopez': ['tai lopez'],
    'grant_cardone': ['grant cardone'],
    'neil_patel': ['neil patel'],
}


def collect():
    threads = sorted(glob.glob('reddit-scrape/data/thread_*.json'))
    return threads


def main():
    thread_files = collect()
    total_comments = 0
    template_hits = defaultdict(list)  # template -> list of (score, text, permalink, sub)
    anti_hits = defaultdict(list)
    platform_hits = defaultdict(list)
    guru_hits = defaultdict(list)
    all_comment_count = 0
    all_post_count = 0

    for tf in thread_files:
        try:
            d = json.load(open(tf))
        except Exception:
            continue
        post = d.get('post', {})
        comments = d.get('comments', [])
        all_post_count += 1
        all_comment_count += len(comments)

        sub = post.get('subreddit', '?')
        thread_url = f"https://www.reddit.com{post.get('permalink','')}"
        thread_title = post.get('title', '')[:120]

        # Process post body
        post_text = (post.get('title','') + ' ' + (post.get('selftext','') or '')).lower()
        post_score = post.get('score', 0) or 0

        for tmpl, kws in TEMPLATE_PATTERNS.items():
            if any(kw in post_text for kw in kws):
                template_hits[tmpl].append({
                    'score': post_score, 'sub': sub, 'title': thread_title,
                    'url': thread_url, 'is_post': True,
                    'snippet': post.get('selftext','')[:300]
                })

        for ap, kws in ANTI_PATTERNS.items():
            if any(kw in post_text for kw in kws):
                anti_hits[ap].append({
                    'score': post_score, 'sub': sub, 'title': thread_title,
                    'url': thread_url, 'is_post': True,
                    'snippet': post.get('selftext','')[:300]
                })

        for plat, kws in PLATFORM_MENTIONS.items():
            if any(kw in post_text for kw in kws):
                platform_hits[plat].append({
                    'score': post_score, 'sub': sub, 'title': thread_title,
                    'url': thread_url, 'snippet': post.get('selftext','')[:200]
                })

        for guru, kws in GURU_MENTIONS.items():
            if any(kw in post_text for kw in kws):
                guru_hits[guru].append({
                    'score': post_score, 'sub': sub, 'title': thread_title,
                    'url': thread_url, 'snippet': post.get('selftext','')[:200]
                })

        # Process comments
        for c in comments:
            body = (c.get('body') or '').lower()
            if not body or len(body) < 30:
                continue
            cscore = c.get('score', 0) or 0
            if cscore < 5:  # Only meaningful comments
                continue
            cperma = f"https://www.reddit.com{c.get('permalink','')}" if c.get('permalink') else thread_url

            for tmpl, kws in TEMPLATE_PATTERNS.items():
                if any(kw in body for kw in kws):
                    template_hits[tmpl].append({
                        'score': cscore, 'sub': sub, 'title': thread_title,
                        'url': cperma, 'is_post': False,
                        'snippet': c.get('body','')[:400]
                    })

            for ap, kws in ANTI_PATTERNS.items():
                if any(kw in body for kw in kws):
                    anti_hits[ap].append({
                        'score': cscore, 'sub': sub, 'title': thread_title,
                        'url': cperma, 'is_post': False,
                        'snippet': c.get('body','')[:400]
                    })

            for plat, kws in PLATFORM_MENTIONS.items():
                if any(kw in body for kw in kws):
                    platform_hits[plat].append({
                        'score': cscore, 'sub': sub, 'title': thread_title,
                        'url': cperma, 'snippet': c.get('body','')[:300]
                    })

            for guru, kws in GURU_MENTIONS.items():
                if any(kw in body for kw in kws):
                    guru_hits[guru].append({
                        'score': cscore, 'sub': sub, 'title': thread_title,
                        'url': cperma, 'snippet': c.get('body','')[:300]
                    })

    # Sort each by score
    for d in (template_hits, anti_hits, platform_hits, guru_hits):
        for k in d:
            d[k].sort(key=lambda x: -x['score'])

    print(f"Threads analyzed: {all_post_count}")
    print(f"Total comments: {all_comment_count:,}")
    print(f"Total conversations (posts + comments): {all_post_count + all_comment_count:,}")
    print()
    print("Template mentions (posts + meaningful comments, score>=5):")
    for t in sorted(template_hits, key=lambda x: -len(template_hits[x])):
        print(f"  {t:<25} {len(template_hits[t]):>5}")
    print()
    print("Anti-pattern mentions:")
    for t in sorted(anti_hits, key=lambda x: -len(anti_hits[x])):
        print(f"  {t:<25} {len(anti_hits[t]):>5}")
    print()
    print("Platform mentions:")
    for t in sorted(platform_hits, key=lambda x: -len(platform_hits[x])):
        print(f"  {t:<25} {len(platform_hits[t]):>5}")
    print()
    print("Guru/influencer mentions:")
    for t in sorted(guru_hits, key=lambda x: -len(guru_hits[x])):
        print(f"  {t:<25} {len(guru_hits[t]):>5}")

    # Write structured output
    out = {
        'meta': {
            'threads_analyzed': all_post_count,
            'total_comments': all_comment_count,
            'total_conversations': all_post_count + all_comment_count,
        },
        'templates': {t: hits[:10] for t, hits in template_hits.items()},
        'anti_patterns': {t: hits[:10] for t, hits in anti_hits.items()},
        'platforms': {t: hits[:10] for t, hits in platform_hits.items()},
        'gurus': {t: hits[:10] for t, hits in guru_hits.items()},
    }
    with open('deep-analysis.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote deep-analysis.json")

if __name__ == '__main__':
    main()
