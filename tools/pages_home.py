from shell import *


def privacy_consent(label_extra=''):
    return f'''<div class="field"><label class="check-i" for="f-consent"><input type="checkbox" id="f-consent" name="consent" value="yes" required data-err="Tick the box to confirm you have read the privacy notice.">
<span>I have read the <a href="privacy.html">privacy notice</a> and I agree that the campaign team may use these details to respond and to plan its priorities.{label_extra}</span></label></div>'''


def honeypot():
    return '<div class="hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>'


BANNER = '''<div class="banner" data-form-banner hidden role="status">
<p><strong>This form is not connected to a delivery service yet.</strong> Nothing you send here will reach the campaign until the team finishes setup. You can still try the form; it will tell you clearly that nothing was sent.</p></div>'''

NOSCRIPT = '<noscript><p class="note">This form needs JavaScript to check and send your message. Please turn it on, or use the contact options on the <a href="contact.html">contact page</a>.</p></noscript>'


def community_form(idp='c'):
    return f'''<div class="form-wrap">{BANNER}
<div class="summary" hidden></div>
<form class="form" id="form" data-form="community" novalidate aria-labelledby="form-h">
<div class="field"><label for="{idp}-ward">Your ward <span class="req" aria-hidden="true">*</span></label>
<select id="{idp}-ward" name="ward" required data-err="Choose the ward your concern is about." data-options="wards"><option value="">Choose a ward</option></select></div>
<div class="field"><label for="{idp}-cat">What is your concern about? <span class="req" aria-hidden="true">*</span></label>
<select id="{idp}-cat" name="category" required data-err="Choose the topic that fits best." data-options="categories"><option value="">Choose a topic</option></select></div>
<div class="field"><label for="{idp}-msg">Your message <span class="req" aria-hidden="true">*</span></label>
<p class="hint" id="{idp}-msg-h">Describe what is happening, where, and what you would like done. Please do not include other people&rsquo;s names or personal details.</p>
<textarea id="{idp}-msg" name="message" required minlength="10" maxlength="1500" aria-describedby="{idp}-msg-h" data-err="Write your message so we can understand your concern." data-minmsg="Please write at least 10 characters so we can understand your concern."></textarea><p class="cnt" aria-hidden="true"></p></div>
<div class="field"><label for="{idp}-name">Your name (optional)</label><input id="{idp}-name" name="name" type="text" autocomplete="name" maxlength="80"></div>
<div class="field"><label for="{idp}-phone">Phone number (optional)</label><p class="hint" id="{idp}-contact-h">Only give a phone number or email if you would like a reply. You can send a concern anonymously.</p>
<input id="{idp}-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" maxlength="30" aria-describedby="{idp}-contact-h"></div>
<div class="field"><label for="{idp}-email">Email address (optional)</label><input id="{idp}-email" name="email" type="email" autocomplete="email" maxlength="120"></div>
{honeypot()}{privacy_consent()}
<div><button class="btn" type="submit">Send my concern</button></div>
<p class="privacy-line">We ask only for what we need. Individual messages are not published.</p>
</form>{NOSCRIPT}<div class="status" hidden role="status"></div></div>'''


def build_index():
    hero_img = picture('clarence-hero', [480, 800, 1086], '(min-width:900px) 460px, 400px',
                       'Hon. Clarence Namunyu Kasali, aspiring Member of Parliament for Ikolomani, in a light blue shirt and patterned maroon tie', 1086, 1448, fetch=True)
    blazer_img = picture('clarence-blazer', [480, 800, 1053], '(min-width:900px) 440px, 90vw', 'Hon. Clarence Namunyu Kasali in a maroon blazer and cream shirt, resting his arms on a table', 1053, 1493)
    path_full = '<img src="img/community-path-1280.webp" alt="" width="1280" height="759" loading="eager">'
    grp = picture('community-group', [640, 1011], '(min-width:900px) 58vw, 100vw', 'A group of women and one man standing together in a garden among tall grasses and trees', 1011, 670)
    gath = picture('community-gathering', [480, 660], '(min-width:900px) 40vw, 100vw', 'Residents gathered outdoors under trees, listening to a speaker holding a microphone', 660, 860)
    cards = [('Land and community interests', 'Fair process and clear information for families affected by land decisions.', 'land'),
             ('Miner safety and dignity', 'Safer working conditions and respect for lawful artisanal miners.', 'miners'),
             ('Responsible mining', 'Protect water, rehabilitate land and deal with unsafe shafts.', 'environment'),
             ('Youth and enterprise', 'Practical routes into skills, business and employment.', 'youth'),
             ('Education', 'Safe, equipped schools and early-childhood learning within reach.', 'education-healthcare'),
             ('Healthcare', 'Closer, better-run care for every ward.', 'education-healthcare'),
             ('Roads and services', 'Roads, water and services families can rely on.', 'infrastructure'),
             ('Accountability', 'Open forums, public reporting and a record residents can read.', 'transparency')]
    cl = ''.join(f'<a class="card" href="manifesto.html#{a}"><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p><span class="go">Read the chapter</span></a>' for i, (t, d, a) in enumerate(cards))
    body = f'''<section class="hero" aria-labelledby="hero-h"><div class="wrap hero-g">
<div class="hero-copy"><p class="kicker" data-in style="--i:0">Ikolomani Constituency &middot; 2027</p>
<h1 id="hero-h" data-in style="--i:1"><span class="l1">Hon. Clarence</span> <span class="l2">Namunyu Kasali</span></h1>
<p class="slogan" data-in style="--i:2">&ldquo;Sovereign Power Belongs to the People.&rdquo;</p>
<p class="support" data-in style="--i:3">Aspiring Member of Parliament, campaigning to protect Ikolomani&rsquo;s land, make mining safer for artisanal miners and deliver accountable representation.</p>
<div class="actions" data-in style="--i:4"><a class="btn" href="manifesto.html">Explore the Manifesto</a><a class="btn btn--ghost" href="about.html">Meet Clarence</a></div></div>
<div class="hero-art">{hero_img}<p class="hero-plate"><b>Aspiring Member of Parliament</b><span>Ikolomani, Kakamega County</span></p></div></div></section>

<section class="stats" aria-label="Ikolomani at a glance"><div class="wrap"><div class="stats-card">
<div class="stat"><b data-bind="ward-count">4</b><span>Electoral wards</span></div>
<div class="stat"><b data-bind="total">56,299</b><span>Registered voters, 2022 (IEBC)</span></div>
<div class="stat"><b>146.2</b><span>Square kilometres (NG-CDF)</span></div>
<div class="stat"><b>111,743</b><span>People, 2019 census (NG-CDF)</span></div></div>
<p class="stats-note">The 2022 voter figure is historical and does not describe the 2027 electorate. <a href="dashboard.html#sources">Sources</a></p></div></section>

<section class="sec"><div class="wrap"><div class="msg"><p class="kicker">Our message</p><h2>A representative should answer first to the people who live with the decisions.</h2>
<p>On land, on mining and on the services every ward depends on, the campaign&rsquo;s priorities are proposals, set out openly and open to change as residents respond.</p><a class="link" href="manifesto.html">Read the manifesto</a></div></div></section>

<section class="feature" id="gold" aria-labelledby="gold-h">{path_full}<div class="wrap feature-g">
<div><p class="kicker">Signature issue</p><h2 id="gold-h">Our Gold.<span>Our Land. Our Future.</span></h2>
<p class="lead">Gold is part of Ikolomani&rsquo;s identity, and families here live with both its promise and its risks. The campaign puts land, miner safety and fair process at the centre.</p>
<div class="actions"><a class="btn" href="gold-land-mining.html">Gold &amp; Land</a><a class="btn btn--ghost" href="community.html?category=gold#form">Share a concern</a></div><p class="fine">Proposed priorities, not confirmed promises.</p></div>
<ul class="feature-list"><li><b>Protect land and community interests</b><span>Households informed, consulted and treated fairly.</span></li><li><b>Make artisanal mining safer</b><span>Safer shafts, training and recognition for miners.</span></li><li><b>Mine responsibly</b><span>Protect water and rehabilitate damaged land.</span></li><li><b>Open, accountable decisions</b><span>Licences and agreements that residents can see.</span></li></ul></div></section>

<section class="sec sec--warm" id="priorities"><div class="wrap"><div class="sec-title"><p class="kicker">Our priorities</p><h2>What the campaign will work on</h2><p>Eight areas, each set out in the manifesto with the concern, the proposal and what an MP can lawfully do.</p></div>
<div class="cards">{cl}</div></div></section>

<section class="sec"><div class="wrap meet"><figure>{blazer_img}</figure><div><p class="kicker">The candidate</p><h2>Meet Clarence</h2><p class="lead">Hon. Clarence Namunyu Kasali is an aspiring Member of Parliament for Ikolomani Constituency, seeking election in 2027.</p><p>His campaign is built on land, the safety and dignity of artisanal miners, and representation that answers to residents in every ward.</p><div class="actions"><a class="btn btn--green" href="about.html">About Clarence</a></div></div></div></section>

<section class="sec sec--warm" id="wards" aria-labelledby="wards-h"><div class="wrap wards-home"><div><p class="kicker">Know your ward</p><h2 id="wards-h">Ikolomani&rsquo;s four wards</h2>
<p>Idakho Central, East, North and South. The 2022 register is a historical reference, not the 2027 electorate, and it measures the size of an electorate rather than the severity of a ward&rsquo;s challenges.</p>
<div class="actions"><a class="btn btn--ghost btn--sm" href="wards.html">Know your ward</a><a class="link" href="dashboard.html">Dashboard</a></div></div>
<div class="chart-card"><ol class="bars" data-chart="wards" aria-label="Registered voters by ward, 2022"></ol>
<noscript><table class="tbl"><caption>Registered voters by ward, 2022 (IEBC)</caption><tbody><tr><th>Idakho Central</th><td>17,095</td></tr><tr><th>Idakho East</th><td>15,195</td></tr><tr><th>Idakho North</th><td>13,605</td></tr><tr><th>Idakho South</th><td>10,404</td></tr><tr><th>Total</th><td>56,299</td></tr></tbody></table></noscript>
<p class="chart-note">Source: IEBC, registered voters per county assembly ward, 2022 general election.</p></div></div></section>

<section class="sec"><div class="wrap"><div class="sec-title"><p class="kicker">Ikolomani</p><h2>The people the campaign is for</h2><p>Small-scale farming and artisanal mining shape daily life across much of Ikolomani, according to NG-CDF Ikolomani.</p></div>
<div class="photos"><figure>{grp}</figure><figure>{gath}</figure></div></div></section>

<section class="cta-band"><div class="wrap cta-g"><div><h2>Join the campaign for Ikolomani.</h2><p>Volunteer in your ward, share a concern, or get in touch with the team.</p></div>
<div class="actions"><a class="btn" href="volunteer.html">Join the Campaign</a><a class="btn btn--ghost" href="community.html#form">Share a concern</a></div></div></section>
'''
    return page('index.html', f'{NAME} | Aspiring MP for Ikolomani, 2027',
                'Hon. Clarence Namunyu Kasali is an aspiring Member of Parliament for Ikolomani, Kakamega County. Sovereign power belongs to the people: land, mining safety and accountable representation.',
                body, active='index.html', body_class='home')
