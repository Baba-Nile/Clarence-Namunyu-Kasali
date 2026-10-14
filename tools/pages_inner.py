from shell import *
from pages_home import privacy_consent, honeypot, BANNER, NOSCRIPT, community_form


def form_shell(form_html_inner, ftype, fid='form', labelled='form-h'):
    return f'''<div class="form-wrap">{BANNER}<div class="summary" hidden></div>
<form class="form" id="{fid}" data-form="{ftype}" novalidate aria-labelledby="{labelled}">{form_html_inner}</form>{NOSCRIPT}<div class="status" hidden role="status"></div></div>'''


def build_about():
    blazer = picture('clarence-blazer', [480, 800, 1053], '(min-width:900px) 340px, 240px',
                     'Hon. Clarence Namunyu Kasali in a maroon blazer and cream shirt, resting his arms on a table', 1053, 1493, fetch=True)
    suit = picture('clarence-suit', [480, 800, 1200], '(min-width:900px) 34vw, 340px', 'Portrait of Hon. Clarence Namunyu Kasali in a dark blazer and light blue shirt', 1254, 1254)
    body = page_hero('', 'About Clarence', 'Educationist, community leader and aspiring Member of Parliament for Ikolomani Constituency, Kakamega County.', ['About'], fig=blazer) + f'''
<section class="sec"><div class="wrap bio-g"><aside class="bio-side"><figure>{suit}</figure>
<div class="glance"><h2>At a glance</h2><dl>
<div><dt>Born</dt><dd>1981, Luhakayu Village, Malinya Sublocation, Idakho Central Ward, Shirumba Location</dd></div>
<div><dt>Constituency</dt><dd>Ikolomani, Kakamega County</dd></div>
<div><dt>Profession</dt><dd>Educationist; Founder and Director, The Holyway Junior School</dd></div>
<div><dt>Service</dt><dd>Member, Rotary Club of Gachie</dd></div></dl></div></aside>
<div class="bio"><p class="kicker">Biography</p><h2>Educationist, community leader and social impact advocate</h2>
<p class="bio-lead">Born in 1981 in Luhakayu Village, Malinya Sublocation, Idakho Central Ward, Shirumba Location, in Ikolomani Constituency, Kakamega County, Western Kenya, he is a passionate educationist, community leader, and social impact advocate committed to transforming lives and creating meaningful change in society.</p>
<p>He began his education at Malinya Primary School before joining Our Lady of Assumption Mixed Secondary School in Shitoli, where he was among the pioneer students. Driven by a strong commitment to education, he pursued a Certificate in Early Childhood Education at Professional ECE College in Limuru, followed by a Diploma in Education at St. Mary&rsquo;s Teacher College in Nakuru.</p>
<ol class="tline" aria-label="Education and service">
<li><b>Malinya Primary School</b><span>Primary education</span></li>
<li><b>Our Lady of Assumption Mixed Secondary School, Shitoli</b><span>Among the pioneer students</span></li>
<li><b>Professional ECE College, Limuru</b><span>Certificate in Early Childhood Education</span></li>
<li><b>St. Mary&rsquo;s Teacher College, Nakuru</b><span>Diploma in Education</span></li>
<li><b>The Holyway Junior School</b><span>Founder and Director</span></li>
<li><b>Rotary Club of Gachie</b><span>Active member</span></li></ol>
<p>As the Founder and Director of The Holyway Junior School, he is dedicated to nurturing young minds, promoting quality education, and creating opportunities for future generations. Beyond education, he is an active member of the Rotary Club of Gachie, where he embraces the spirit of service, fellowship, and community development.</p>
<p>His life and work are guided by a deep passion for empowering people, uplifting communities, and making a lasting positive impact on society. Through education, leadership, and service, he continues to champion meaningful change and inspire others to contribute to the greater good.</p></div></div></section>
<section class="sec sec--warm"><div class="wrap about-intro"><p class="big">His campaign rests on one idea: sovereign power belongs to the people, and a representative exists to serve them.</p>
<div><p>The message echoes the opening principle of Kenya&rsquo;s Constitution (Article 1). For Ikolomani, it means residents are never bystanders when decisions are made about their land, their work and their public services.</p>
<div class="actions"><a class="btn" href="manifesto.html">Read the manifesto</a><a class="link" href="gold-land-mining.html">Gold &amp; Land</a></div></div></div></section>
<section class="sec"><div class="wrap values-head"><div><h2>What the campaign stands for</h2></div>
<ul class="values"><li><b>Accountability</b><span>A public record of what residents raise and what is done about it.</span></li>
<li><b>Protection of land</b><span>Land and livelihoods treated as matters of rights, information and fair process.</span></li>
<li><b>Dignity of work</b><span>Safe, lawful and respected work for miners, farmers, traders and young people.</span></li>
<li><b>Participation</b><span>Priorities shaped ward by ward, with residents, and published for scrutiny.</span></li>
<li><b>Honesty about limits</b><span>No promises beyond what an MP can lawfully deliver.</span></li></ul></div></section>
<section class="sec sec--warm sec--tight"><div class="wrap close"><h2>Help shape the priorities.</h2><div><a class="btn" href="community.html#form">Share a concern</a><ul><li><a class="link" href="volunteer.html">Volunteer in your ward</a></li></ul></div></div></section>'''
    return page('about.html', f'About Clarence | {NAME}, Ikolomani 2027',
                'Biography of Hon. Clarence Namunyu Kasali, educationist, community leader and aspiring Member of Parliament for Ikolomani: his education, The Holyway Junior School, Rotary service and 2027 campaign.', body)


def two_col(form_html, side_html, h):
    return f'''<section class="sec"><div class="wrap formpage"><div><h2 id="form-h" style="font-size:1.6rem;margin-bottom:1.25rem">{h}</h2>{form_html}</div><aside class="side">{side_html}</aside></div></section>'''


def build_contact():
    f = '''<div class="field"><label for="k-name">Your name <span class="req" aria-hidden="true">*</span></label><input id="k-name" name="name" type="text" autocomplete="name" required maxlength="80" data-err="Enter your name."></div>
<div class="field"><label for="k-email">Email address <span class="req" aria-hidden="true">*</span></label><input id="k-email" name="email" type="email" autocomplete="email" required maxlength="120" data-err="Enter your email address so the team can reply."></div>
<div class="field"><label for="k-phone">Phone number (optional)</label><input id="k-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" maxlength="30"></div>
<div class="field"><label for="k-subj">What is your message about? <span class="req" aria-hidden="true">*</span></label><select id="k-subj" name="subject" required data-err="Choose what your message is about.">
<option value="">Choose a subject</option><option value="information">Request campaign information</option><option value="general">General question</option><option value="media">Media enquiry</option><option value="updates">Receive campaign updates</option><option value="other">Something else</option></select></div>
<div class="field"><label for="k-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="k-msg" name="message" required minlength="10" maxlength="1500" data-err="Write your message." data-minmsg="Please write at least 10 characters."></textarea><p class="cnt" aria-hidden="true"></p></div>''' + honeypot() + privacy_consent() + '<div><button class="btn" type="submit">Send message</button></div><p class="privacy-line">Your details are used only to reply. See the <a href="privacy.html">privacy notice</a>.</p>'
    side = '<h2>Other ways to reach us</h2><ul class="channels" data-channels></ul><p class="fine" style="margin-top:1rem"><a href="volunteer.html">Volunteer</a> or <a href="community.html#form">share a ward concern</a>.</p>'
    body = page_hero('', 'Contact the campaign', 'Send a message to the campaign team.', ['Contact']) + two_col(form_shell(f, 'contact'), side, 'Send a message')
    return page('contact.html', f'Contact | {NAME}, Ikolomani 2027',
                'Contact the Hon. Clarence Namunyu Kasali campaign for Ikolomani. Send a message or request campaign information.', body)


def build_volunteer():
    areas = ['Community mobilisation in my ward', 'Ward forums and public meetings', 'Research and data collection', 'Communications and social media', 'Transport and logistics', 'Youth outreach', 'Other']
    chk = ''.join(f'<label class="check-i" for="v-a{i}"><input type="checkbox" id="v-a{i}" name="areas[]" value="{a}"><span>{a}</span></label>' for i, a in enumerate(areas))
    f = f'''<div class="field"><label for="v-name">Full name <span class="req" aria-hidden="true">*</span></label><input id="v-name" name="name" type="text" autocomplete="name" required maxlength="80" data-err="Enter your full name."></div>
<div class="field"><label for="v-phone">Phone number <span class="req" aria-hidden="true">*</span></label><p class="hint" id="v-ph">So the campaign team can reach you about volunteering.</p><input id="v-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required maxlength="30" aria-describedby="v-ph" data-err="Enter a phone number so the team can reach you."></div>
<div class="field"><label for="v-email">Email address (optional)</label><input id="v-email" name="email" type="email" autocomplete="email" maxlength="120"></div>
<div class="field"><label for="v-ward">Your ward <span class="req" aria-hidden="true">*</span></label><select id="v-ward" name="ward" required data-err="Choose your ward, or the last option if you are not sure." data-options="wards"><option value="">Choose a ward</option></select></div>
<fieldset class="field" data-require-one="Choose at least one way you would like to help."><legend>How would you like to help? <span class="req" aria-hidden="true">*</span></legend><div class="checks">{chk}</div></fieldset>
<div class="field"><label for="v-note">Anything else we should know? (optional)</label><textarea id="v-note" name="message" maxlength="1000" style="min-height:6rem"></textarea><p class="cnt" aria-hidden="true"></p></div>''' + honeypot() + privacy_consent() + '<div><button class="btn" type="submit">Register to volunteer</button></div><p class="privacy-line">Registering is not a commitment. See the <a href="privacy.html">privacy notice</a>.</p>'
    side = '<h2>What volunteers do</h2><ul><li>Help organise ward forums and listening sessions.</li><li>Collect concerns from neighbours, with their consent.</li><li>Share verified campaign information.</li><li>The campaign never asks volunteers to pay to take part.</li></ul>'
    body = page_hero('', 'Volunteer with the campaign', 'Tell the team where you live and how you would like to help.', ['Volunteer']) + two_col(form_shell(f, 'volunteer'), side, 'Volunteer registration')
    return page('volunteer.html', f'Volunteer | {NAME}, Ikolomani 2027',
                'Register to volunteer with the Hon. Clarence Namunyu Kasali campaign in Ikolomani. Choose your ward and how you would like to help.', body)


def build_donate():
    body = page_hero('', 'Support the campaign', 'Ways to help today, and how to avoid anyone using the campaign&rsquo;s name to ask for money.', ['Support']) + '''
<section class="sec"><div class="wrap formpage"><div><ol class="clist"><li><div><b>Give your time</b><span>Register as a volunteer in your ward. <a class="link" href="volunteer.html">Volunteer</a></span></div></li>
<li><div><b>Share verified information</b><span>Share pages from this website with people you know.</span><div class="share" data-share="Hon. Clarence Namunyu Kasali, Ikolomani 2027" style="margin-top:.7rem"></div></div></li>
<li><div><b>Share your concerns and ideas</b><span>Tell the campaign what matters in your ward. <a class="link" href="community.html#form">Share a concern</a></span></div></li></ol>
<h2 style="font-size:1.4rem;margin-top:2.5rem">Financial contributions</h2>
<div data-donation-none><p>Financial contributions are not open yet. When they are, the official payment details will be published on this page and nowhere else.</p></div><p data-donation hidden></p></div>
<aside class="side"><h2>Beware of impersonation</h2><ul><li>If anyone asks for money in the campaign&rsquo;s name through a number, account or link that is not published on this page, do not pay.</li><li>Report it on the <a href="contact.html">contact page</a>.</li></ul></aside></div></section>'''
    return page('donate.html', f'Support the Campaign | {NAME}, Ikolomani 2027',
                'How to support the Hon. Clarence Namunyu Kasali campaign in Ikolomani. Volunteering is open now; payment details will be published here only once official.', body)


def build_privacy():
    body = page_hero('', 'Privacy notice', 'What this website collects when you use a form, why, and what your choices are.', ['Privacy']) + '''
<section class="sec"><div class="wrap"><div style="max-width:var(--prose)">
<h2 style="font-size:1.3rem">Who we are</h2><p>This website is run by the campaign of Hon. Clarence Namunyu Kasali, aspiring Member of Parliament for Ikolomani. You can reach the campaign through the <a href="contact.html">contact page</a>.</p>
<h2 style="font-size:1.3rem;margin-top:2rem">What we collect</h2><ul style="padding-left:1.2rem;margin-bottom:1em"><li><strong>Community concern form:</strong> ward, topic and message. Name, phone and email are optional.</li><li><strong>Volunteer form:</strong> name, phone, ward and areas of interest. Email and notes are optional.</li><li><strong>Contact form:</strong> name, email, subject and message. Phone is optional.</li></ul>
<p>We do not ask for ID numbers, voter card numbers, party membership, ethnicity, religion or other sensitive details. Please do not include them in free-text boxes.</p>
<h2 style="font-size:1.3rem;margin-top:2rem">Why we use it</h2><p>To respond to your message, organise volunteers and understand which issues matter in each ward. Individual messages are not published. Where concerns are summarised publicly, they are anonymised and combined.</p>
<h2 style="font-size:1.3rem;margin-top:2rem">How it is handled</h2><p>Your submission is emailed from the website to the campaign inbox. The website does not keep submissions in a database. Messages are kept only as long as needed to respond and to plan, and are then deleted.</p>
<h2 style="font-size:1.3rem;margin-top:2rem">Third-party resources</h2><p>This site loads icons from cdnjs; those providers can see your IP address. This site sets no advertising or analytics cookies.</p>
<h2 style="font-size:1.3rem;margin-top:2rem">Your rights</h2><p>Under Kenya&rsquo;s Data Protection Act, 2019 you can ask to see, correct or delete personal data held about you, and object to its use. Use the <a href="contact.html">contact page</a>. You may also complain to the Office of the Data Protection Commissioner.</p></div></div></section>'''
    return page('privacy.html', f'Privacy Notice | {NAME}, Ikolomani 2027',
                'Privacy notice for the Hon. Clarence Namunyu Kasali campaign website: what the forms collect, why, who sees it and your rights.', body)


def build_community():
    gath = picture('community-gathering', [480, 660], '(min-width:1000px) 28vw, 80vw', 'Residents gathered outdoors under trees, listening to a speaker holding a microphone', 660, 860)
    side = f'''<h2>What happens to your message</h2><ul><li>The campaign team reads it. It is not published.</li><li>Concerns are grouped by ward and topic to decide what is researched first.</li><li>A reply is possible only if you share a phone number or email.</li><li>This form is not for emergencies. For urgent safety problems, contact the emergency services or the responsible authority.</li>
<li><a class="link" data-whatsapp="Hello, I have a community concern for the Clarence Namunyu Kasali campaign." href="#" hidden>Message on WhatsApp</a></li></ul><figure style="margin-top:1.75rem">{gath}</figure>'''
    body = page_hero('', 'Share a concern. Shape a priority.', 'Tell the campaign what matters in your ward. Concerns help decide which priorities are researched first.', ['Ikolomani', 'Community Engagement']) + two_col(community_form('c'), side, 'Ward concern form')
    return page('community.html', f'Community Engagement | {NAME}, Ikolomani 2027',
                'Share a community concern with the Hon. Clarence Namunyu Kasali campaign. Choose your Ikolomani ward and topic: land, mining safety, roads, water, education, health.', body)


def build_updates():
    body = page_hero('', 'News and updates', 'Announcements, public meetings and community reports from the campaign.', ['News']) + '''
<section class="sec"><div class="wrap" style="max-width:860px;margin-inline:0 auto"><div data-feed="updates"><div class="empty" data-empty><h2>Nothing has been announced yet</h2><p>The first announcements and meeting dates will appear here as soon as they are confirmed. To hear about them directly, send the campaign a message.</p><a class="btn btn--ghost btn--sm" href="contact.html?subject=updates#form">Request campaign information</a></div></div>
<div data-feed="events" id="events" style="margin-top:2rem"></div>
<div class="share" data-share="News and updates from the Clarence Namunyu Kasali campaign" style="margin-top:2.5rem"></div></div></section>'''
    return page('updates.html', f'News & Updates | {NAME}, Ikolomani 2027',
                'Announcements, public meetings and community reports from the Hon. Clarence Namunyu Kasali campaign for Ikolomani.', body)


def build_404():
    body = page_hero('', 'We could not find that page', 'The link may be old or mistyped. Try one of these pages.', None) + '''
<section class="sec"><div class="wrap"><img class="err-logo" src="assets/images/brand/logo-full-900.webp" width="900" height="580" alt="Clarence Namunyu Kasali logo"><div class="issues" style="max-width:36rem"><a class="issue" href="index.html" style="grid-template-columns:1fr 1.5rem"><h3>Home</h3></a><a class="issue" href="manifesto.html" style="grid-template-columns:1fr 1.5rem"><h3>The Manifesto</h3></a><a class="issue" href="wards.html" style="grid-template-columns:1fr 1.5rem"><h3>Know Your Ward</h3></a><a class="issue" href="contact.html" style="grid-template-columns:1fr 1.5rem"><h3>Contact</h3></a></div></div></section>'''
    return page('404.html', f'Page not found | {NAME}', 'Page not found.', body, noindex=True)
