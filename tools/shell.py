"""Shared page shell for the Clarence Namunyu Kasali campaign site.
Static output only: the generated .html files are what gets uploaded to cPanel."""
import json, os, html

# The final domain is NOT assumed. Replace via:  SITE_URL=https://example.ke python3 tools/build.py
SITE_URL = os.environ.get('SITE_URL', 'https://CAMPAIGN-DOMAIN.example').rstrip('/')
NAME = 'Hon. Clarence Namunyu Kasali'
SHORT = 'Clarence Namunyu Kasali'
TAGLINE = 'Aspiring Member of Parliament, Ikolomani Constituency, 2027'
SLOGAN = 'Sovereign Power Belongs to the People.'
LASTMOD = '2026-10-09'

NAV = [
    ('index.html', 'nav.home', 'Home', True),
    ('about.html', 'nav.about', 'About Clarence', False),
    ('manifesto.html', 'nav.manifesto', 'The Manifesto', False),
    ('gold-land-mining.html', 'nav.gold', 'Gold, Land &amp; Mining', False),
    ('projects.html', 'nav.priorities', 'Our Priorities', False),
    ('wards.html', 'nav.wards', 'Wards', False),
    ('community.html', 'nav.community', 'Community Engagement', False),
    ('updates.html', 'nav.news', 'News &amp; Updates', False),
    ('contact.html', 'nav.contact', 'Contact', False),
]

BRAND_DIR = 'assets/images/brand'
# Official logo: compact mark + live wordmark for the navbar; full lockup in the footer and 404.
LOGO = (f'<img class="brand-mark" src="{BRAND_DIR}/logo-mark-160.webp" srcset="{BRAND_DIR}/logo-mark-160.webp 1x, {BRAND_DIR}/logo-mark-320.webp 2x" '
        'width="160" height="151" alt="" decoding="async">')
LOGO_FULL = (f'<img src="{BRAND_DIR}/logo-full-900.webp" width="900" height="{round(900*750/1165)}" '
             'alt="Clarence Namunyu Kasali official logo: a raised fist over a map of Kenya in the national colours" loading="lazy" decoding="async">')


def head(title, desc, path, og_image='img/og-image.jpg', ld=None, noindex=False):
    url = f'{SITE_URL}/{path}' if path != 'index.html' else f'{SITE_URL}/'
    img = f'{SITE_URL}/{og_image}'
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    base_ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": f"{NAME} for Ikolomani", "url": f"{SITE_URL}/",
                "inLanguage": "en"}]
    if path == 'index.html' or path == 'about.html':
        base_ld.append({"@context": "https://schema.org", "@type": "Person", "name": SHORT, "honorificPrefix": "Hon.",
                        "url": f"{SITE_URL}/", "image": f"{SITE_URL}/img/clarence-suit-800.webp",
                        "description": "Aspiring Member of Parliament for Ikolomani Constituency, Kakamega County, Kenya (2027 general election)."})
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in base_ld + (ld or []))
    robots = 'noindex, follow' if noindex else 'index, follow'
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}"><meta name="robots" content="{robots}"><meta name="theme-color" content="#FFFFFF">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME} for Ikolomani"><meta property="og:locale" content="en_KE"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{NAME}, aspiring Member of Parliament for Ikolomani, 2027. {SLOGAN}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{img}">
<link rel="icon" href="assets/images/brand/favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.ico" sizes="48x48"><link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32"><link rel="icon" href="icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<link rel="preload" href="fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/source-serif-4-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">
<link rel="stylesheet" href="css/main.css?v=4">{ld_html}</head>
'''


SUB = [('wards.html', 'Know Your Ward'), ('dashboard.html', 'Development Dashboard'), ('community.html', 'Community Engagement')]


def header(active, body_class=''):
    def cur(h):
        return ' aria-current="page"' if h == active else ''
    sub_cur = ' cur' if active in [h for h, _ in SUB] else ''
    sub = ''.join(f'<li><a href="{h}"{cur(h)}>{t}</a></li>' for h, t in SUB)
    bc = f' class="{body_class}"' if body_class else ''
    return f'''<body{bc}><a class="skip" href="#main">Skip to main content</a><div class="progress" aria-hidden="true"></div>
<header class="site-header"><div class="wrap hd">
<a class="brand" href="index.html" aria-label="Clarence Namunyu Kasali, Ikolomani MP campaign. Home">{LOGO}<span class="brand-t"><strong>Clarence</strong><small>Namunyu Kasali</small></span></a>
<nav class="nav" id="site-nav" aria-label="Main"><ul>
<li><a href="about.html"{cur('about.html')}>About</a></li>
<li><a href="manifesto.html"{cur('manifesto.html')}>Manifesto</a></li>
<li><a href="gold-land-mining.html"{cur('gold-land-mining.html')}>Gold &amp; Land</a></li>
<li><a href="projects.html"{cur('projects.html')}>Our Priorities</a></li>
<li class="has-sub"><button class="sub-btn{sub_cur}" type="button" aria-expanded="false" aria-controls="sub-ik">Ikolomani <svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></button><ul class="sub" id="sub-ik">{sub}</ul></li>
<li><a href="updates.html"{cur('updates.html')}>News</a></li></ul>
<a class="btn" href="volunteer.html">Join the Campaign</a></nav>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><svg class="b" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 4h14M2 9h14M2 14h14" stroke="currentColor" stroke-width="2" fill="none"/></svg><svg class="x" viewBox="0 0 18 18" aria-hidden="true"><path d="M3 3l12 12M15 3L3 15" stroke="currentColor" stroke-width="2" fill="none"/></svg><span>Menu</span></button>
</div></header>
<main id="main">
'''


def footer():
    return f'''</main>
<footer class="site-footer"><div class="wrap"><div class="ft">
<div><a class="ft-logo" href="index.html" aria-label="Clarence Namunyu Kasali, home">{LOGO_FULL}</a><p>Aspiring Member of Parliament for Ikolomani Constituency, Kakamega County.</p><div class="ft-social" data-footer-social></div></div>
<nav aria-label="Footer"><h3>Explore</h3><ul><li><a href="about.html">About</a></li><li><a href="manifesto.html">Manifesto</a></li><li><a href="gold-land-mining.html">Gold &amp; Land</a></li><li><a href="projects.html">Our Priorities</a></li><li><a href="wards.html">Know Your Ward</a></li><li><a href="updates.html">News</a></li></ul></nav>
<div><h3>Take part</h3><ul><li><a href="volunteer.html">Volunteer</a></li><li><a href="community.html">Share a concern</a></li><li><a href="contact.html">Contact</a></li><li><a href="donate.html">Support</a></li><li><a href="privacy.html">Privacy</a></li></ul><ul data-footer-contact style="margin-top:.75rem"></ul></div>
</div><div class="ft-base"><span>&copy; 2026 {NAME}</span><span>Ward data from IEBC, checked <span data-bind="verified-date">9 October 2026</span>. <a href="dashboard.html#sources">Sources</a></span></div></div></footer>
<button class="totop" type="button" aria-label="Back to top" hidden><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 10l5-5 5 5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></button>
<script src="js/config.js" defer></script><script src="js/data.js" defer></script><script src="js/i18n.js" defer></script><script src="js/main.js" defer></script>
</body></html>
'''


def page(path, title, desc, body, active=None, **kw):
    bc = kw.get('body_class', '')
    return head(title, desc, path, og_image=kw.get('og', 'img/og-image.jpg'), ld=kw.get('ld'), noindex=kw.get('noindex', False)) + header(active or path, bc) + body + footer()


def picture(base, widths, sizes, alt, w, h, cls='', lazy=False, ext='webp', fetch=False, extra=''):
    ss = ', '.join(f'img/{base}-{x}.{ext} {x}w' for x in widths)
    big = widths[-1]
    load = 'fetchpriority="high"' if fetch else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="img/{base}-{big}.{ext}" srcset="{ss}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt, quote=True)}" {load} {extra}>'


def page_hero(title_unused, h1, sub, crumbs=None, fig=None):
    cr = ('<p class="crumbs"><a href="index.html">Home</a> / ' + ' / '.join(crumbs) + '</p>') if crumbs else ''
    if fig:
        return (f'<section class="phead phead--split"><div class="wrap phead-g"><div class="copy">{cr}<h1>{h1}</h1><p class="lead">{sub}</p></div><figure class="phead-fig">{fig}</figure></div></section>')
    return f'<section class="phead"><div class="wrap phead-g"><div>{cr}<h1>{h1}</h1><p class="lead">{sub}</p></div></div></section>'


def sitemap(pages):
    rows = ''.join(f'<url><loc>{SITE_URL}/{"" if p == "index.html" else p}</loc><lastmod>{LASTMOD}</lastmod></url>\n' for p in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'
