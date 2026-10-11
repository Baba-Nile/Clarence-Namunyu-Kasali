#!/usr/bin/env python3
"""Generate the static site. Usage:  SITE_URL=https://your-domain.ke python3 tools/build.py
Output: .html files, sitemap.xml, robots.txt, site.webmanifest in the project root."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
import shell
from pages_home import build_index
from pages_inner import *
from pages_data import *
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = {'index.html': build_index, 'about.html': build_about, 'manifesto.html': build_manifesto,
         'gold-land-mining.html': build_gold, 'projects.html': build_projects, 'wards.html': build_wards,
         'dashboard.html': build_dashboard, 'community.html': build_community, 'updates.html': build_updates,
         'volunteer.html': build_volunteer, 'donate.html': build_donate, 'contact.html': build_contact,
         'privacy.html': build_privacy, '404.html': build_404}
for name, fn in pages.items():
    open(os.path.join(root, name), 'w', encoding='utf-8').write(fn())
indexed = [p for p in pages if p != '404.html']
open(os.path.join(root, 'sitemap.xml'), 'w').write(shell.sitemap(indexed))
open(os.path.join(root, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {shell.SITE_URL}/sitemap.xml\n')
open(os.path.join(root, 'site.webmanifest'), 'w').write(json.dumps({
    "name": "Hon. Clarence Namunyu Kasali, Ikolomani 2027", "short_name": "Clarence 2027", "start_url": "./index.html",
    "display": "standalone", "theme_color": "#ffffff", "background_color": "#ffffff",
    "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
print('built', len(pages), 'pages for', shell.SITE_URL)
