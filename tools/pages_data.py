from shell import *

SRC = {  # label -> url (all seen and checked on 9 Oct 2026; news = reported, not official)
    'capital-fm': ('Capital FM, 12 Nov 2025', 'https://www.capitalfm.co.ke/business/2025/11/state-to-earn-sh607mn-in-royalties-after-uk-firm-finds-sh680bn-gold-in-kakamega/'),
    'star': ('The Star, 17 Nov 2025', 'https://www.the-star.co.ke/counties/western/2025-11-17-leaders-raise-concerns-over-proposed-gold-mining-in-ikolomani'),
    'kna': ('Kenya News Agency, 10 Dec 2025', 'https://www.kenyanews.go.ke/government-promises-a-win-win-outcome-for-ikolomani-gold-mine-residents/'),
    'bhrrc': ('Business &amp; Human Rights Resource Centre, 12 Dec 2025', 'https://www.business-humanrights.org/en/latest-news/kenya-kakamega-leaders-urge-calm-as-ikolomani-gold-tensions-escalate-over-lack-of-sufficient-consultations/'),
    'nation': ('Nation, 2026', 'https://nation.africa/kenya/news/golden-curse-senate-intervenes-in-kakamega-gold-mining-dispute-5500982'),
    'standard': ('The Standard, 2026', 'https://www.standardmedia.co.ke/western/article/2001551875/sh683b-gold-project-faces-senate-scrutiny-over-land-dispute'),
    'ngcdf': ('NG-CDF Ikolomani', 'https://ikolomani.ngcdf.go.ke/about-us/'),
}


def srcs(*keys):
    return '<p class="srcs">Sources (news reports, not official records): ' + '; '.join(f'<a href="{SRC[k][1]}" rel="noopener">{SRC[k][0]}</a>' for k in keys) + '.</p>'


def chapter(cid, title, concern, priority, actions, limit, cat, tag='h2', small=False):
    acts = ''.join(f'<li>{a}</li>' for a in actions)
    return f'''<section id="{cid}" aria-labelledby="{cid}-h"><div class="wrap chapter"><{tag} class="ch-t" id="{cid}-h">{title}</{tag}>
<div class="ch-body">
<div><h4>The community concern</h4>{concern}</div>
<div><h4>The proposed priority</h4>{priority}</div>
<div><h4>Possible actions within an MP&rsquo;s role</h4><ul>{acts}</ul><p class="limit">{limit}</p></div>
<div><h4>How you can contribute</h4><p>Tell the campaign what you see in your ward; it helps decide what is researched first.</p><a class="btn btn--sm" href="community.html?category={cat}#form">Share feedback on this chapter</a></div>
</div></div></section>'''


def build_manifesto():
    mp_limit = 'An MP can make and amend laws, scrutinise ministries and agencies, and represent residents. Decisions on licences, approvals and land acquisition rest with the relevant national and county authorities, not with an individual MP.'
    land = chapter('land', 'Protecting community land interests',
        '<p>Families in parts of Ikolomani have faced uncertainty about land, relocation and compensation linked to a proposed large-scale underground gold project. Public reporting since late 2025 describes an Environmental Impact Assessment said to cover parts of Idakho North and Idakho Central, community protests, and questions about public participation and access to documents.</p>' + srcs('capital-fm', 'star', 'nation'),
        '<p>Households and landowners should be fully informed, genuinely consulted and treated fairly and lawfully before any decision that affects their land.</p>',
        ['<strong>Legislation:</strong> support proposals that strengthen consultation, information and compensation protections for communities affected by mining and land acquisition.',
         '<strong>Oversight:</strong> ask questions of the responsible ministries and agencies, and request publication of documents and agreements in the public interest.',
         '<strong>Representation:</strong> convene residents with officials, carry petitions, and keep a public record of what was raised and the answers given.'],
        mp_limit, 'land', tag='h3', small=True)
    miners = chapter('miners', 'Artisanal miner safety and welfare',
        '<p>Artisanal miners dominate mining activity in the constituency, according to NG-CDF Ikolomani. Reporting in December 2025 described a shaft collapse that killed three miners, after which the county government closed an artisanal site.</p>' + srcs('ngcdf', 'kna'),
        '<p>Lawful artisanal mining should be safer and more dignified, with miners treated as workers whose livelihoods matter.</p>',
        ['<strong>Oversight:</strong> press the responsible authorities on safety inspection, enforcement and emergency response.',
         '<strong>Representation:</strong> bring miners&rsquo; associations and officials together, and help miners understand lawful permits and how to organise.',
         '<strong>Legislation and budget:</strong> support measures and funding for safety training and equipment through the national process, without promising amounts in advance.'],
        'Safety regulation and permits are the responsibility of the national ministry responsible for mining and, where applicable, county authorities. No budget or delivery date is promised here.', 'gold', tag='h3', small=True)
    env = chapter('environment', 'Responsible mining and environmental stewardship',
        '<p>Unsafe or abandoned shafts, land damage and risks to water sources are recognised risks of gold mining. The campaign does not yet have verified ward-level evidence of where they occur, and proposes to gather it from residents.</p>',
        '<p>Mining should protect water and land, and damaged land should be rehabilitated. Unsafe shafts should be identified and dealt with.</p>',
        ['<strong>Oversight:</strong> scrutinise how environmental conditions are monitored and enforced, and raise residents&rsquo; reports with the regulators.',
         '<strong>Representation:</strong> help communities document concerns about water and land so that they reach the right authority.',
         '<strong>Legislation:</strong> support clear rehabilitation and closure obligations for mining operations.'],
        'Environmental approvals and enforcement belong to regulators such as NEMA and water authorities, working with county government.', 'water', tag='h3', small=True)
    youth = chapter('youth', 'Youth economic opportunities',
        '<p>Youth employment and vocational opportunities are proposed research topics in Idakho East and Idakho South. The campaign has no verified local employment data yet and will gather it with residents.</p>',
        '<p>Practical routes for young people into skills, enterprise and decent work, including in farming and lawful, responsible mining.</p>',
        ['<strong>Representation:</strong> link young people with training institutions, national programmes and county opportunities.',
         '<strong>Oversight:</strong> ask how national youth and enterprise programmes reach Ikolomani.',
         '<strong>Constituency funds:</strong> advocate, within the NG-CDF law and through public participation, for skills and bursary priorities.'],
        'Jobs and programmes depend on national and county budgets and on private employers. No job numbers are promised.', 'youth')
    edu = chapter('education-healthcare', 'Education and healthcare',
        '<p>School infrastructure and early-childhood education are proposed research topics in Idakho North, and access to healthcare in Idakho South. NG-CDF Ikolomani&rsquo;s site lists historical items such as a school hall handover and health-insurance enrolment support from 2022, which show what constituency funds have been used for, not the current situation.</p>' + srcs('ngcdf'),
        '<p>Schools that are safe and equipped, and health services that are close, staffed and affordable.</p>',
        ['<strong>Constituency funds:</strong> advocate for transparent, community-chosen priorities in school infrastructure and bursaries under the NG-CDF framework.',
         '<strong>Oversight:</strong> follow national education and health funding that reaches the constituency.',
         '<strong>Representation:</strong> take specific facility problems raised by residents to the County Government of Kakamega, which runs county health services.'],
        'County government is responsible for county health services. No facilities, staffing levels or budgets are promised here.', 'education')
    infra = chapter('infrastructure', 'Infrastructure and local development',
        '<p>Road conditions, transport costs and water supply are proposed research topics in all four wards. The campaign has not yet verified road or water project status by ward and will publish it once sourced.</p>',
        '<p>Roads, water and essential services that families and farmers can rely on, with progress that residents can check.</p>',
        ['<strong>Oversight:</strong> track road and water projects in the constituency and publish what is documented.',
         '<strong>Representation:</strong> carry ward-level priorities to the relevant road agencies and county departments.',
         '<strong>Constituency funds:</strong> advocate for community-identified local projects within NG-CDF rules.'],
        'Road and water responsibilities are shared between national agencies and the county government. No roads, kilometres or dates are promised.', 'roads')
    trans = chapter('transparency', 'Transparent representation and accountability',
        '<p>Residents should be able to see what their representative has been told, what was done, and what happened next.</p>',
        '<p>A regular, public record of the campaign&rsquo;s work and, if elected, of the MP&rsquo;s.</p>',
        ['Hold regular open forums in every ward and publish a short report after each.',
         'Publish anonymised summaries of concerns received, by ward and topic.',
         'Publish each commitment with a date and its status, and update it with evidence.',
         'Report back to residents on how constituency funds are used, as far as public information allows.'],
        'This chapter is largely within the campaign&rsquo;s and an MP&rsquo;s own control, so it is the first one the campaign can start doing.', 'other')

    toc = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in [('gold-land-people', 'Gold, land and people'), ('land', 'Land'), ('miners', 'Miners'), ('environment', 'Environment'), ('youth', 'Youth'), ('education-healthcare', 'Education and health'), ('infrastructure', 'Infrastructure'), ('transparency', 'Accountability')])
    body = page_hero('', 'The Manifesto', 'Proposed priorities in seven chapters. Each separates the concern, the proposal, what an MP can do, and how you can contribute.', ['Manifesto']) + f'''
<nav class="toc" aria-label="Manifesto chapters"><div class="wrap"><ol>{toc}</ol></div></nav>
<div id="manifesto-body" class="wrap" style="padding-top:clamp(2rem,4vw,3rem);padding-bottom:clamp(2rem,4vw,3rem)">
<p class="note" style="margin-bottom:2rem">These are proposed priorities, not confirmed commitments. No budgets, dates or outcomes are promised, and statements about documented events are sourced.</p>
<div class="flag" id="gold-land-people" role="region" aria-labelledby="glp-h"><h2 id="glp-h">Protecting Our Gold, Our Land and Our People</h2>
<p>Gold is part of Ikolomani&rsquo;s identity. This chapter sets out how the campaign proposes to protect land, make mining safer for the people who do the work, and make decisions about natural resources open and fair, in three linked parts.</p><a class="link" href="gold-land-mining.html">Read the gold and land hub</a></div>
{land}{miners}{env}{youth}{edu}{infra}{trans}
<div style="border-top:1px solid var(--line-dk);padding-top:2.5rem"><h2 style="font-size:1.5rem">From proposal to commitment</h2>
<ol class="process"><li><strong>Proposed</strong><span>A priority is published here, clearly marked as proposed.</span></li><li><strong>Reviewed</strong><span>Residents and the campaign comment. Legal limits are checked.</span></li><li><strong>Committed</strong><span>Only then is it published as a dated, public commitment.</span></li></ol>
<div class="share" data-share="The manifesto of Hon. Clarence Namunyu Kasali, Ikolomani 2027" style="margin-top:2rem"></div></div></div>'''
    return page('manifesto.html', f'The Manifesto | {NAME}, Ikolomani 2027',
                'Proposed priorities of Hon. Clarence Namunyu Kasali for Ikolomani: protecting gold, land and people, miner safety, youth, education, health, infrastructure and accountability.', body)


def build_gold():
    path = picture('community-path', [640, 1000, 1280], '(min-width:900px) 40vw, 92vw', 'Residents walking together along a shaded village path between farms and trees', 1280, 759, lazy=False)
    tl = [
        ('November 2025', 'An Environmental Impact Assessment for an underground gold project at Isulu–Bushiangala was reported to have been submitted to NEMA. It was reported to affect parts of Idakho North and Idakho Central, with land acquisition and compensation to follow Kenyan law and international resettlement standards.', ['capital-fm']),
        ('November 2025', 'Reports estimated that about 337 acres, mostly privately owned, would be needed and that about 800 households could be affected. Local leaders and artisanal miners raised concerns, including about coexistence with artisanal mining.', ['star']),
        ('4 December 2025', 'A public participation meeting convened at Isulu met protests. Reports describe confrontations, deaths and injuries; figures differ between reports and are not repeated here.', ['bhrrc']),
        ('December 2025', 'Kakamega County government was reported to have closed an artisanal mining site after a shaft collapse killed three miners.', ['kna']),
        ('10 December 2025', 'Government leaders were reported to have committed to comprehensive public engagement of all stakeholders before any mining begins.', ['kna']),
        ('4 March 2026', 'A Kenya Gazette notice of this date was reported in connection with a mining licence application, said to be under review by the responsible ministry.', ['nation']),
        ('2026 (date to be confirmed)', 'A Senate committee held a public hearing at Bushiangala. The Mining Principal Secretary was reported to say the company held only a prospecting licence and could not start mining until a Community Development Agreement was signed.', ['standard', 'nation']),
    ]
    tl_html = ''.join(f'<li><time>{d}</time><p>{t}</p>{srcs(*s)}</li>' for d, t, s in tl)
    prios = [
        ('Protecting community land interests', 'Scrutinise land and mining policy; raise residents&rsquo; concerns in Parliament; ask for documents to be published.', 'National Land Commission and the ministry responsible for lands; County Government of Kakamega (planning); the courts for disputes.'),
        ('Meaningful public participation in mining decisions', 'Insist, through oversight and representation, on adequate notice, accessible documents and local-language participation; convene community meetings.', 'NEMA (environmental public participation); the ministry responsible for mining; county government; the licence applicant.'),
        ('Fair, transparent and lawful compensation where applicable', 'Advocate for clear compensation rules and for information on how valuations are done; point residents to independent legal advice.', 'The acquiring entity and valuers; the National Land Commission where applicable; the courts; the responsible ministry.'),
        ('Artisanal miner safety and working conditions', 'Press for safety enforcement and emergency response; support safety funding through the national budget process.', 'Ministry responsible for mining (inspection); county government; miners&rsquo; associations; health and rescue services.'),
        ('Responsible mining and environmental rehabilitation', 'Scrutinise environmental monitoring and enforcement; support clear rehabilitation duties in law.', 'NEMA; county environment officers; licence holders.'),
        ('Protecting water sources and addressing unsafe or abandoned shafts', 'Raise documented cases with regulators; press for closure and rehabilitation plans.', 'NEMA; Water Resources Authority; county government; ministry responsible for mining.'),
        ('Lawful livelihood opportunities for mining communities', 'Advocate for skills, cooperatives and local inclusion in opportunities linked to mining.', 'Ministry responsible for mining; county government; licence holders; training institutions.'),
        ('Transparency and accountability in natural-resource decisions', 'Ask parliamentary questions; push for publication of licences and community agreements; publish what the MP learns.', 'The ministry responsible for mining; parliamentary committees; regulators.'),
    ]
    rows = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td></tr>' for a, b, c in prios)
    clist = ''.join(f'<li><div><b>{a}</b></div></li>' for a, b, c in prios)
    body = page_hero('', 'Protect Our Gold. Protect Our Land. Protect Our People.', 'The campaign&rsquo;s proposed priorities, what is documented, what an MP can and cannot do, and how residents can take part.', ['Gold &amp; Land']) + f'''
<div class="wrap banner-img">{path}</div>
<section class="sec"><div class="wrap split"><div><h2>What is documented</h2><p>Items below come from news reports and public statements, checked on <span data-bind="verified-date">9 October 2026</span>. They are not official records, accounts differ in places, and later developments may be missing.</p></div>
<div><ol class="tl">{tl_html}</ol>
<p class="note">Under the Mining Act, royalties are reported to be shared 70% to the national government, 20% to the county and 10% to the community where mining occurs.</p>{srcs('kna')}
<p class="fine" style="margin-top:1rem">Primary documents are not linked here because they have not yet been located and checked. See <a href="dashboard.html#sources">sources</a>.</p></div></div></section>
<section class="sec sec--warm"><div class="wrap split"><div><h2>Eight proposed priorities</h2><p>Proposals for review, not confirmed promises. No incidents, household counts, compensation outcomes or statistics are claimed beyond the sourced timeline.</p></div>
<ol class="clist">{clist}</ol></div></section>
<section class="sec"><div class="wrap"><h2>What an MP can do, and who else must act</h2>
<p class="lead" style="margin-bottom:1.75rem">A Member of the National Assembly makes laws, oversees state organs and represents constituents. Many decisions on mining, land and the environment belong to other bodies, and the campaign will not promise what it has no power to deliver.</p>
<div class="tbl-wrap"><table class="tbl"><caption>Priorities, an MP&rsquo;s legislative, oversight and representative role, and required collaboration</caption><thead><tr><th scope="col">Priority</th><th scope="col">Within an MP&rsquo;s role</th><th scope="col">Requires collaboration with</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="actions"><a class="btn" href="community.html?category=gold#form">Share a gold or land concern</a><a class="link" href="manifesto.html#gold-land-people">Read the manifesto chapter</a></div>
<div class="share" data-share="Protect Our Gold. Protect Our Land. Protect Our People. Hon. Clarence Namunyu Kasali, Ikolomani 2027" style="margin-top:2rem"></div></div></section>'''
    return page('gold-land-mining.html', f'Gold & Land | {NAME}, Ikolomani 2027',
                'Protect Our Gold. Protect Our Land. Protect Our People. Sourced timeline, proposed priorities and the limits of an MP’s role on mining and land in Ikolomani.', body)


def build_projects():
    pr = [('Land protection and community interests', 'land', 'Fair process and clear information for families affected by land decisions.'),
          ('Artisanal miner safety and dignity', 'miners', 'Safer working conditions and respect for lawful miners.'),
          ('Responsible mining and environmental stewardship', 'environment', 'Protect water, rehabilitate land, address unsafe shafts.'),
          ('Youth skills, enterprise and employment', 'youth', 'Practical routes into skills, business and jobs.'),
          ('Education and access to opportunity', 'education-healthcare', 'Schools that are safe, equipped and within reach.'),
          ('Healthcare and community wellbeing', 'education-healthcare', 'Closer, better-run care for every ward.'),
          ('Roads, infrastructure and essential services', 'infrastructure', 'Roads, water and services families can rely on.'),
          ('Transparent representation and accountability', 'transparency', 'Regular public reporting and an open record.')]
    li = ''.join(f'<a class="issue" href="manifesto.html#{a}"><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p></a>' for i, (t, a, d) in enumerate(pr))
    body = page_hero('', 'Our Priorities', 'Eight proposed priorities for Ikolomani. Each links to a manifesto chapter that explains the concern, the proposal and the limits of an MP&rsquo;s role.', ['Our Priorities']) + f'''
<section class="sec"><div class="wrap"><div class="issues">{li}</div></div></section>
<section class="sec sec--warm" id="accountability"><div class="wrap split"><div><h2>Your Voice, Our Accountability</h2><p>How the campaign proposes to report back.</p></div>
<ol class="clist"><li><div><b>Concerns received</b><span>Anonymised summaries by ward and topic, published once real submissions have been collected and reviewed.</span></div></li>
<li><div><b>Consultations held</b><span>The date, place and ward of each public meeting, with a short report.</span></div></li>
<li><div><b>Public commitments</b><span>A priority becomes a commitment only once it is approved and dated. Its status is then updated with evidence.</span></div></li>
<li><div><b>Statements and progress</b><span>Official statements published in full, with dates.</span></div></li></ol></div></section>
<section class="sec sec--tight"><div class="wrap"><div class="actions" style="margin-top:0"><a class="btn" href="community.html#form">Share a concern</a><a class="link" href="manifesto.html">Read the manifesto</a></div></div></section>'''
    return page('projects.html', f'Our Priorities | {NAME}, Ikolomani 2027',
                'Eight proposed priorities for Ikolomani and how the campaign proposes to report back: land, miner safety, mining, youth, education, health, infrastructure and accountability.', body)


def build_wards():
    body = page_hero('', 'Know Your Ward', 'Ikolomani has four electoral wards. See each ward&rsquo;s reported 2022 electorate and the topics the campaign proposes to research with residents.', ['Ikolomani', 'Know Your Ward']) + '''
<section class="sec" style="padding-top:2rem"><div class="wrap">
<p class="note">Figures are IEBC&rsquo;s registered voters for the 2022 general election, checked <span data-bind="verified-date">9 October 2026</span>. They are historical, not the 2027 electorate, and show the size of an electorate rather than how severe a ward&rsquo;s challenges are. Research priorities are topics to investigate, not findings. County and NG-CDF project records have not yet been verified, so none are shown. <a href="dashboard.html">Dashboard</a></p>
<div id="ward-filter" class="wfilter" role="group" aria-label="Filter wards"></div><p class="vh" id="ward-live" role="status" aria-live="polite"></p>
<div id="ward-directory"><noscript><table class="tbl"><caption>Registered voters by ward, 2022 (IEBC)</caption><tbody><tr><th>Idakho Central</th><td>17,095</td></tr><tr><th>Idakho East</th><td>15,195</td></tr><tr><th>Idakho North</th><td>13,605</td></tr><tr><th>Idakho South</th><td>10,404</td></tr><tr><th>Total</th><td>56,299</td></tr></tbody></table></noscript></div>
</div></section>'''
    return page('wards.html', f'Know Your Ward | {NAME}, Ikolomani 2027',
                'Explore Ikolomani’s four wards: Idakho Central, East, North and South. Reported 2022 voters, research priorities and a way to share ward concerns.', body)


def build_dashboard():
    body = page_hero('', 'Ikolomani Development Dashboard', 'The reported 2022 electorate by ward, the topics the campaign will research, and the sources behind every figure.', ['Ikolomani', 'Dashboard']) + '''
<section class="sec"><div class="wrap split">
<div><h2>Registered voters, 2022</h2><p style="font:500 clamp(2.4rem,4vw,3.2rem)/1 var(--serif);color:var(--forest);margin:0 0 .4rem" data-bind="total">56,299</p><p class="fine">Total reported registered voters in Ikolomani (IEBC, 2022 register). Historical reference data, not the 2027 electorate.</p><div id="sum-check" class="check" role="status"></div></div>
<div><div class="wfilter" role="group" aria-label="Sort wards" style="margin-top:0"><button type="button" data-sort="size" aria-pressed="true">Largest first</button><button type="button" data-sort="name" aria-pressed="false">A to Z</button></div>
<ol class="bars" id="dash-chart" aria-label="Registered voters by ward, 2022" data-link="on"></ol><p class="chart-note">Bar length compares each ward with the largest. Shares are calculated from the ward figures and rounded to one decimal place, so they can add up to 100.1%.</p></div></div></section>
<section class="sec sec--warm"><div class="wrap"><h2>Wards side by side</h2><p class="lead" style="margin-bottom:1.5rem">Verified project and county-plan data are not yet published for any ward, so none is shown. No development scores or support levels exist.</p>
<div class="tbl-wrap"><table class="tbl" id="dash-table"><caption>Ikolomani wards: 2022 electorate and research priorities</caption><thead><tr><th scope="col">Ward</th><th scope="col" class="num">Registered voters</th><th scope="col" class="num">Share</th><th scope="col">Research priorities (not findings)</th></tr></thead><tbody></tbody>
<tfoot><tr><th scope="row">Total</th><td class="num t-total">56,299</td><td class="num">100.0%</td><td>Sum of the four wards</td></tr></tfoot></table></div></div></section>
<section class="sec" id="sources"><div class="wrap"><h2>Data sources and methodology</h2><p class="lead" style="margin-bottom:1.5rem">Every figure has a source, a reference period and a date it was last checked. News reports are labelled as reports, not official records.</p>
<div class="tbl-wrap"><table class="tbl" id="sources-table"><caption>Sources used on this website</caption><thead><tr><th scope="col">Source</th><th scope="col">What it supports</th><th scope="col">Reference period</th><th scope="col">Last checked</th><th scope="col">Status</th><th scope="col">Link</th></tr></thead><tbody></tbody></table></div>
<ol class="clist" style="max-width:var(--prose);margin-top:2rem"><li><div><b>Ward share</b><span>Ward voters divided by the sum of the four wards, times 100, to one decimal place.</span></div></li><li><div><b>Consistency check</b><span>The four ward figures are added and compared with IEBC&rsquo;s separate constituency total.</span></div></li><li><div><b>Order of sources</b><span>IEBC records first, then county and NG-CDF records, credible news reporting and official mining and environmental authorities.</span></div></li></ol></div></section>'''
    return page('dashboard.html', f'Development Dashboard | {NAME}, Ikolomani 2027',
                'Ikolomani Development Dashboard: reported 2022 registered voters by ward, research priorities and sources, with figures checked against IEBC records.', body)
