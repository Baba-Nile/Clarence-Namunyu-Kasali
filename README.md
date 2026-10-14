# Hon. Clarence Namunyu Kasali — Ikolomani 2027 campaign website

Static HTML, CSS and vanilla JavaScript. No framework, no database. Deploys to ordinary shared hosting / cPanel.

## Design basis
White-dominant editorial system sampled from the official logo (`assets/images/brand/`): deep olive (#3A5A1E / wordmark #2E4818), antique gold (#C9961C fills, #8A6410 for gold text), charcoal #202820, off-white #F7F8F5, hairlines #E5E8E1. Source Serif 4 (headlines) + Inter (UI and body), self-hosted variable woff2 in `fonts/`. Gold is used for the main CTA, fine rules and small markers; olive for links, active navigation and bars. The only dark area is the Gold & Land feature on the home page. No Google Fonts request; icons still load Font Awesome from cdnjs. `css/main.css` is a single stylesheet.

## Brand assets
`assets/images/brand/`: `logo-full.png` (transparent, full size), `logo-full-900.webp` (footer, 404), `logo-mark-160/320.webp` (navbar, 1x/2x), `favicon.svg` (embeds the official mark as raster, not a hand-traced vector). Root: `favicon.ico`, `favicon-32.png`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`, `img/og-image.jpg` (logo + portrait share image). The navbar uses the mark plus live text for CLARENCE / NAMUNYU KASALI so it stays legible at small sizes. Logo/favicons were cut from the supplied 1536x1024 PNG; supply an SVG or vector original if one exists for a truly crisp favicon.

## Hero redesign (11 Oct 2026)
Homepage hero rebuilt as an asymmetric editorial composition (`tools/pages_home.py`, `css/main.css` "hero" block): the transparent portrait cutout (unaltered) stands on a pale-sage panel sized to the photo, the head rising above it, with a small caption plate and gold corner rule. Headline reduced to `clamp(2.1rem,3.8vw,3.4rem)`; only the surname line is olive. Palette tokens in `:root` now follow the brief (#354B27, #20251F, #C69A32, #F0F2E9, #686D66; `--gold-ink` #8A6410 stays for gold *text* so it passes AA). Motion: CSS-only staggered hero entrance (150-900 ms) and a below-the-fold scroll reveal in `js/main.js`; both are disabled under `prefers-reduced-motion` and the page is fully visible without JavaScript. Layout: two columns from 700 px up, stacked on phones.
Tested (headless Chromium): 14 pages x 390/820/1440 px: no overflow, JS errors or missing local assets; reduced-motion and no-JS states; hero CTAs; mobile menu open/Esc. Not tested: real devices, screen readers, Safari/Firefox.

## Run locally
```
cd <this folder>
python3 -m http.server 8000      # then open http://localhost:8000
```
(The forms need PHP to actually send. Locally they will correctly say "nothing was sent".)

## Deploy to cPanel
1. Set the final domain (see below) and rebuild, or search-and-replace `https://CAMPAIGN-DOMAIN.example` in all files.
2. cPanel → File Manager → `public_html` → upload everything in this folder (except `tools/`, `docs/`, `README.md`, which are optional) — or upload the zip and Extract. `.htaccess` must come along (enable "Show hidden files").
3. Turn on form delivery: in `api/`, copy `config.sample.php` to `config.php`; set `recipient` (campaign inbox) and `from` (an address on your own domain, e.g. website@your-domain.ke). Test by sending a message; the red/amber banner above forms disappears when the endpoint reports it is configured.
4. Fill in `js/config.js` (WhatsApp, phone, email, office, social links, manifesto PDF, donation instructions) — only verified values.
5. Submit `sitemap.xml` in Google Search Console.

## Setting the domain
`SITE_URL=https://your-domain.ke python3 tools/build.py` regenerates all pages, canonical/Open Graph URLs, `sitemap.xml` and `robots.txt`. (Pages are generated from `tools/*.py`; edit text there, then rebuild. Or edit the `.html` files directly if you prefer.)

## Publishing content
Everything publishable lives in `js/data.js`: `UPDATES`, `EVENTS`, `CONSULTATIONS`, `CONCERN_SUMMARIES`, `COMMITMENTS`, `STATEMENTS`. They are empty on purpose; add only confirmed items. Ward figures and sources are in the same file; percentages and totals are computed, and the dashboard checks the four wards against the IEBC constituency total.

## Language readiness
`js/i18n.js` + `languages` in `js/config.js`. Kiswahili is NOT enabled. Enable only after approved wording exists.

## Still needed before launch (nothing below was invented)
- Verified biography, qualifications, history (About + home "Meet Clarence"); captions/date/place/consent for the supplied community photos.
- Verified WhatsApp, phone, email, office, social accounts; approved manifesto PDF; approved donation channels and any legally required disclosures.
- Campaign legal review: manifesto "within an MP's role" wording, the roles table on the gold/land/mining page, and the privacy notice (data controller details, retention, Data Protection Act obligations).
- Final domain; mail `recipient`/`from` in `api/config.php`.
- Primary documents still to be located and linked (shown as "awaiting verification" on the dashboard): NEMA EIA report, Gazette notice of 4 March 2026, Mining Act 2016 and Constitution texts, Kakamega CIDP and county project records, NG-CDF project lists. News items on the mining timeline are reports, not official records; exact dates of the Nation and Standard Senate articles should be added.
- Font Awesome loads from cdnjs. For privacy or reliability you may self-host it.
- Unused supplied photos: the tent/funeral photo (not suitable for campaign use) and a low-resolution vertical group photo.

## Tests performed (9 Oct 2026, headless Chromium, offline CDNs)
All 14 pages at 390 / 820 / 1440 px (rechecked after the redesign, nav also checked at 1350, 1366 and 1920 px): no console or JS errors, no horizontal overflow, no missing local assets or broken internal links/anchors, no duplicate ids, balanced HTML. Verified: mobile menu (open/close/Esc/aria), ward filter and deep links, ward figures 17,095 + 15,195 + 13,605 + 10,404 = 56,299 matching IEBC, computed shares 30.4 / 27.0 / 24.2 / 18.5 %, form validation summaries and per-field errors, ward/category pre-selection from links, volunteer "choose at least one" rule, and that forms report "nothing was sent" when no delivery service answers. No trace of the previous campaign's names, slogan, number or domain remains.
Not tested: real email delivery (`api/submit.php` was written but PHP was not available here), rendering of the Montserrat/Font Awesome CDN assets, real devices, screen readers.
