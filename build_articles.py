#!/usr/bin/env python3
"""Genera los 3 artículos SEO estáticos a partir de ARTICLES. Sin dependencias externas."""
import json
import re

SITE = "https://iflorit.github.io"
APP_ID = "6738656243"

SHELL_HEAD = """<!DOCTYPE html>
<html lang="en" data-lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="app-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{site}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{site}/og-image.png">
<meta name="apple-itunes-app" content="app-id={app_id}">
<script type="application/ld+json">
{schema}
</script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#08090c; --bg2:#0b0d12; --card:#101218; --line:rgba(255,255,255,.08);
  --green:#30D158; --blue:#0A84FF; --ink:#f5f5f7; --mut:#8b8b94; --mut2:#6a6a72;
  --max:760px;
}}
html{{scroll-behavior:smooth;background:var(--bg)}}
a:focus-visible{{outline:2px solid var(--green);outline-offset:3px;border-radius:6px}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;line-height:1.6}}
a{{color:var(--green);text-decoration:none}}
a:hover{{text-decoration:underline}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 24px}}
header{{position:sticky;top:0;z-index:50;backdrop-filter:blur(18px);
  background:rgba(8,9,12,.72);border-bottom:1px solid var(--line)}}
.nav{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:var(--max);margin:0 auto;padding:0 24px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;letter-spacing:-.01em;color:var(--ink)}}
.brand img{{width:28px;height:28px;border-radius:7px}}
.btn-cta{{color:var(--ink);border:1px solid rgba(255,255,255,.18);padding:8px 16px;border-radius:980px;
  font-size:13px;font-weight:600}}
.btn-cta:hover{{background:rgba(255,255,255,.08);text-decoration:none}}
main{{padding:56px 0 80px}}
.kicker{{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--green);margin-bottom:16px}}
h1{{font-size:clamp(28px,4.4vw,42px);line-height:1.12;font-weight:800;letter-spacing:-.03em;max-width:680px}}
.dek{{margin-top:18px;font-size:18px;color:var(--mut);line-height:1.55}}
article h2{{font-size:clamp(22px,2.6vw,28px);font-weight:800;letter-spacing:-.02em;margin:44px 0 14px}}
article h3{{font-size:18px;font-weight:700;margin:26px 0 10px}}
article p{{font-size:16.5px;color:#d6d6dc;margin:14px 0}}
article ul,article ol{{margin:14px 0 14px 22px;color:#d6d6dc}}
article li{{margin:8px 0;font-size:16.5px;line-height:1.55}}
article strong{{color:var(--ink)}}
.callout{{margin:32px 0;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px}}
.callout p{{margin:0;font-size:15.5px;color:var(--mut)}}
.cta-box{{margin:48px 0 8px;background:var(--card);border:1px solid rgba(48,209,88,.3);border-radius:18px;padding:28px 26px;text-align:center}}
.cta-box h3{{margin-top:0;font-size:20px}}
.cta-box p{{color:var(--mut);font-size:15px;margin:8px 0 18px}}
.badge{{height:50px}}
.faq dt{{font-weight:700;font-size:16.5px;margin-top:22px;color:var(--ink)}}
.faq dd{{margin:8px 0 0;color:var(--mut);font-size:15.5px;line-height:1.55}}
.related{{margin-top:56px;padding-top:32px;border-top:1px solid var(--line)}}
.related h2{{margin-top:0}}
.related ul{{list-style:none;margin:0;padding:0}}
.related li{{margin:10px 0}}
footer{{border-top:1px solid var(--line);background:var(--bg2)}}
.foot{{display:flex;align-items:center;justify-content:space-between;padding:28px 24px;flex-wrap:wrap;gap:14px;max-width:var(--max);margin:0 auto}}
.foot-links{{display:flex;gap:22px;color:var(--mut);font-size:14px}}
.foot-links a{{color:var(--mut)}}
.foot-links a:hover{{color:var(--ink)}}
.copy{{color:var(--mut);font-size:13px}}
</style>
</head>
<body>
<header><div class="nav">
  <a class="brand" href="index.html"><img src="app-icon-128.png" width="28" height="28" alt="Call to Meet">Call to Meet</a>
  <a class="btn-cta" href="index.html">Home</a>
</div></header>
<main><div class="wrap">
<article>
<div class="kicker">{kicker}</div>
<h1>{h1}</h1>
<p class="dek">{dek}</p>
{body}
</article>
{related}
</div></main>
<footer><div class="wrap foot">
  <a class="brand" href="index.html"><img src="app-icon-128.png" width="26" height="26" alt="" loading="lazy">Call to Meet</a>
  <div class="foot-links">
    <a href="privacy.html">Privacy</a>
    <a href="terms.html">Terms</a>
    <a href="support.html">Support</a>
  </div>
  <div class="copy">© 2026 Call to Meet</div>
</div></footer>
</body>
</html>
"""

def faq_schema(canonical, qa_pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qa_pairs
        ],
    }

def howto_schema(name, description, steps):
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": [
            {"@type": "HowToStep", "name": s["name"], "text": s["text"]}
            for s in steps
        ],
    }

def render_faq_html(qa_pairs):
    out = ['<h2>Frequently asked questions</h2>', '<dl class="faq">']
    for q, a in qa_pairs:
        out.append(f"<dt>{q}</dt><dd>{a}</dd>")
    out.append("</dl>")
    return "\n".join(out)

def render_related(current_slug, all_slugs_titles):
    items = "".join(
        f'<li><a href="{slug}.html">{title}</a></li>'
        for slug, title in all_slugs_titles if slug != current_slug
    )
    return f'<div class="related"><h2>Related reading</h2><ul>{items}</ul></div>'

def cta(slug, label="Get Call to Meet"):
    return f'''<div class="cta-box">
<h3>{label}</h3>
<p>Free on the App Store. Real alarms for your meetings, even on silent.</p>
<a href="https://apps.apple.com/app/id{APP_ID}?ct=seo-{slug}&mt=8"><img class="badge" src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" width="150" height="50" alt="Download on the App Store"></a>
</div>'''

def build(article, all_slugs_titles):
    slug = article["slug"]
    canonical = f"{SITE}/{slug}.html"
    combined_schema = article["schemas"]
    schema_json = "\n".join(json.dumps(s, ensure_ascii=False, indent=2) for s in combined_schema) if len(combined_schema) == 1 else json.dumps(combined_schema, ensure_ascii=False, indent=2)
    html = SHELL_HEAD.format(
        title=article["title"],
        description=article["description"],
        canonical=canonical,
        site=SITE,
        app_id=APP_ID,
        schema=schema_json,
        kicker=article["kicker"],
        h1=article["h1"],
        dek=article["dek"],
        body=article["body_html"],
        related=render_related(slug, all_slugs_titles),
    )
    with open(f"/tmp/landing-seo/{slug}.html", "w") as f:
        f.write(html)
    return slug
