/* ==========================================================================
   DATA — single source of truth for ward records, sources and records the
   campaign publishes. Percentages are ALWAYS computed from `voters`.
   Add verified items to the arrays at the bottom; leave them empty until then.
   Last full review of this file: 9 October 2026.
   ========================================================================== */
(function () {
  var VERIFIED_ON = '2026-10-09';

  /* ---- Sources. status: 'original' = checked against the original document;
          'official-site' = official public web page; 'reported' = news report,
          not an official record; 'awaiting' = not yet located or checked. ---- */
  var SOURCES = [
    { id: 'iebc-ward', status: 'original', publisher: 'IEBC',
      title: 'Registered Voters per County Assembly Ward for the 2022 General Election',
      url: 'https://www.iebc.or.ke/docs/rov_per_caw.pdf',
      supports: 'The four Ikolomani ward figures (Idakho South 10,404; Idakho East 15,195; Idakho North 13,605; Idakho Central 17,095).',
      period: '2022 General Election register', verified: VERIFIED_ON },
    { id: 'iebc-const', status: 'original', publisher: 'IEBC',
      title: 'Registered Voters per Constituency for the 2022 General Election',
      url: 'https://www.iebc.or.ke/docs/rov_per_constituency.pdf',
      supports: 'Ikolomani constituency total of 56,299 registered voters (constituency code 210).',
      period: '2022 General Election register', verified: VERIFIED_ON },
    { id: 'ngcdf-about', status: 'official-site', publisher: 'NG-CDF Ikolomani',
      title: 'About Us — Ikolomani Constituency',
      url: 'https://ikolomani.ngcdf.go.ke/about-us/',
      supports: 'Four county assembly wards; population of 111,743 (2019 census); area of 146.2 sq. km; small-scale farming as the main economic activity; artisanal miners dominating mining activity.',
      period: 'Page undated; 2019 census figures', verified: VERIFIED_ON },
    { id: 'ngcdf-home', status: 'official-site', publisher: 'NG-CDF Ikolomani',
      title: 'NG-CDF Ikolomani home page (news items)',
      url: 'https://ikolomani.ngcdf.go.ke/',
      supports: 'Describes the name “Ikolomani” as a corruption of “Gold Mines”; lists a 31 March 2022 item on NHIF enrolment of vulnerable residents and a Shichinji Secondary School hall handover. Historical items, not the latest record.',
      period: 'Items dated 2022', verified: VERIFIED_ON },
    { id: 'capital-fm', status: 'reported', publisher: 'Capital FM',
      title: 'State to earn Sh607mn in royalties after UK firm finds Sh680bn gold in Kakamega',
      url: 'https://www.capitalfm.co.ke/business/2025/11/state-to-earn-sh607mn-in-royalties-after-uk-firm-finds-sh680bn-gold-in-kakamega/',
      supports: 'Reporting on an Environmental Impact Assessment for the Isulu–Bushiangala underground mining project, said to affect parts of Idakho North and Idakho Central wards.',
      period: 'Published 12 November 2025', verified: VERIFIED_ON },
    { id: 'the-star', status: 'reported', publisher: 'The Star',
      title: 'Kakamega leaders fault proposed plan by investor to extract gold in Ikolomani',
      url: 'https://www.the-star.co.ke/counties/western/2025-11-17-leaders-raise-concerns-over-proposed-gold-mining-in-ikolomani',
      supports: 'Reported estimate of about 337 acres, mostly privately owned, and about 800 households that could be affected; concerns raised by local leaders and artisanal miners.',
      period: 'Published 17 November 2025', verified: VERIFIED_ON },
    { id: 'kna', status: 'reported', publisher: 'Kenya News Agency',
      title: 'Government promises a win-win outcome for Ikolomani gold mine residents',
      url: 'https://www.kenyanews.go.ke/government-promises-a-win-win-outcome-for-ikolomani-gold-mine-residents/',
      supports: 'Government commitment to comprehensive public engagement before mining; a shaft collapse that killed three miners and the county closure of an artisanal site; the 70/20/10 royalty sharing described under the Mining Act.',
      period: 'Published 10 December 2025', verified: VERIFIED_ON },
    { id: 'bhrrc', status: 'reported', publisher: 'Business & Human Rights Resource Centre',
      title: 'Kakamega leaders urge calm as Ikolomani gold tensions escalate over lack of sufficient consultations',
      url: 'https://www.business-humanrights.org/en/latest-news/kenya-kakamega-leaders-urge-calm-as-ikolomani-gold-tensions-escalate-over-lack-of-sufficient-consultations/',
      supports: 'Summary of the December 2025 tensions around public participation forums; reports of deaths and injuries (figures vary between reports).',
      period: 'Reported 12 December 2025', verified: VERIFIED_ON },
    { id: 'nation-senate', status: 'reported', publisher: 'Nation',
      title: 'Golden curse? Senate intervenes in Kakamega gold mining dispute',
      url: 'https://nation.africa/kenya/news/golden-curse-senate-intervenes-in-kakamega-gold-mining-dispute-5500982',
      supports: 'Reported mining licence application under review following a Kenya Gazette notice dated 4 March 2026; Senate scrutiny; questions about availability of EIA annexures.',
      period: 'Published mid-2026 (exact date to be confirmed)', verified: VERIFIED_ON },
    { id: 'standard-senate', status: 'reported', publisher: 'The Standard',
      title: 'Shanta gold project faces fresh scrutiny over land rights, public participation',
      url: 'https://www.standardmedia.co.ke/western/article/2001551875/sh683b-gold-project-faces-senate-scrutiny-over-land-dispute',
      supports: 'Senate committee public hearing at Bushiangala; the Mining Principal Secretary stating that the company held a prospecting licence and could not start mining before signing a Community Development Agreement.',
      period: 'Published mid-2026 (exact date to be confirmed)', verified: VERIFIED_ON },
    { id: 'cidp', status: 'awaiting', publisher: 'County Government of Kakamega',
      title: 'County Integrated Development Plan (CIDP) and current county project records',
      url: '', supports: 'Documented water, road, school and health projects by ward. Not yet located and checked.',
      period: 'Awaiting verification', verified: '' },
    { id: 'ngcdf-projects', status: 'awaiting', publisher: 'NG-CDF Ikolomani',
      title: 'NG-CDF public project lists by ward',
      url: '', supports: 'Project names, locations and status by ward. Not yet located and checked.',
      period: 'Awaiting verification', verified: '' },
    { id: 'nema-eia', status: 'awaiting', publisher: 'NEMA',
      title: 'Environmental Impact Assessment report for the Isulu–Bushiangala project (primary document)',
      url: '', supports: 'Primary text behind the news reports above. The campaign should read the original and its annexures.',
      period: 'Awaiting verification', verified: '' },
    { id: 'gazette', status: 'awaiting', publisher: 'Kenya Gazette',
      title: 'Gazette notice dated 4 March 2026 on the mining licence application (primary document)',
      url: '', supports: 'Primary text for the licence application status. Not yet located and checked.',
      period: 'Awaiting verification', verified: '' },
    { id: 'mining-act', status: 'awaiting', publisher: 'Republic of Kenya',
      title: 'Mining Act, 2016 and Constitution of Kenya, 2010 (Article 95) — primary texts',
      url: '', supports: 'Royalty sharing and the legislative, oversight and representative roles of Members of the National Assembly. Link to the official texts to be added.',
      period: 'Awaiting verification', verified: '' }
  ];

  /* ---- Reported constituency total (IEBC). The site also checks that the
          four ward figures add up to this number. ---- */
  var IEBC_CONSTITUENCY_TOTAL = 56299;

  /* ---- Ward records. `research` items are PRIORITIES TO INVESTIGATE, not
          findings. `documented` items are dated, sourced facts only. ---- */
  var WARDS = [
    { id: 'idakho-central', name: 'Idakho Central', voters: 17095, iebcCode: '1050', source: 'iebc-ward',
      research: [
        { t: 'Gold-mining safety and land-related concerns, where applicable', s: 'research' },
        { t: 'Water availability and quality', s: 'research' },
        { t: 'Roads and transport access', s: 'research' },
        { t: 'Agriculture and local livelihoods', s: 'research' },
        { t: 'Status and coverage of documented water projects', s: 'awaiting' }
      ],
      documented: [
        { t: 'An Environmental Impact Assessment for a proposed underground gold project at Isulu–Bushiangala was reported to cover parts of Idakho North and Idakho Central wards.', src: 'capital-fm', date: '12 Nov 2025' }
      ],
      category: 'gold' },
    { id: 'idakho-east', name: 'Idakho East', voters: 15195, iebcCode: '1048', source: 'iebc-ward',
      research: [
        { t: 'Land and mining-related concerns in affected locations', s: 'research' },
        { t: 'Water access', s: 'research' },
        { t: 'Road conditions and transport costs', s: 'research' },
        { t: 'Agricultural livelihoods', s: 'research' },
        { t: 'Youth employment and vocational opportunities', s: 'research' }
      ],
      documented: [],
      category: 'land' },
    { id: 'idakho-north', name: 'Idakho North', voters: 13605, iebcCode: '1049', source: 'iebc-ward',
      research: [
        { t: 'Road conditions and access to public services', s: 'research' },
        { t: 'School infrastructure and early-childhood education', s: 'research' },
        { t: 'Water availability', s: 'research' },
        { t: 'Agriculture and rural livelihoods', s: 'research' },
        { t: 'Current condition and coverage of documented county projects', s: 'awaiting' }
      ],
      documented: [
        { t: 'The same Environmental Impact Assessment was reported to cover parts of Idakho North ward as well as Idakho Central.', src: 'capital-fm', date: '12 Nov 2025' }
      ],
      category: 'roads' },
    { id: 'idakho-south', name: 'Idakho South', voters: 10404, iebcCode: '1047', source: 'iebc-ward',
      research: [
        { t: 'Road accessibility', s: 'research' },
        { t: 'Water supply', s: 'research' },
        { t: 'Agricultural opportunities', s: 'research' },
        { t: 'Access to healthcare', s: 'research' },
        { t: 'Youth employment and local enterprise opportunities', s: 'research' }
      ],
      documented: [],
      category: 'health' }
  ];

  /* ---- Concern categories used by the ward-specific participation form ---- */
  var CATEGORIES = [
    { id: 'gold', label: 'Gold mining and miner safety' },
    { id: 'land', label: 'Land rights and compensation' },
    { id: 'roads', label: 'Roads and transport' },
    { id: 'water', label: 'Water and environment' },
    { id: 'education', label: 'Education' },
    { id: 'health', label: 'Healthcare' },
    { id: 'agriculture', label: 'Agriculture and livelihoods' },
    { id: 'youth', label: 'Youth opportunities' },
    { id: 'other', label: 'Other' }
  ];

  var STATUS = {
    original: { label: 'Checked against original', icon: 'fa-circle-check' },
    'official-site': { label: 'Official public page', icon: 'fa-building-columns' },
    reported: { label: 'News report, not an official record', icon: 'fa-newspaper' },
    awaiting: { label: 'Awaiting verification', icon: 'fa-hourglass-half' },
    research: { label: 'Research priority', icon: 'fa-magnifying-glass' }
  };

  /* ---- Records the campaign will publish. LEAVE EMPTY until verified. ----
     COMMITMENTS: { priority, commitment, status, updated:'YYYY-MM-DD', source, url }
     CONSULTATIONS: { date:'YYYY-MM-DD', place, ward, summary, reportUrl }
     CONCERN_SUMMARIES: { period, ward, category, count, note }  (aggregated only)
     STATEMENTS: { date:'YYYY-MM-DD', title, url }
     UPDATES: { date:'YYYY-MM-DD', category, title, excerpt, url, image, alt }
     EVENTS: { date:'YYYY-MM-DD', time, title, place, ward, url }              */
  var COMMITMENTS = [];
  var CONSULTATIONS = [];
  var CONCERN_SUMMARIES = [];
  var STATEMENTS = [];
  var UPDATES = [];
  var EVENTS = [];

  window.CAMPAIGN_DATA = {
    verifiedOn: VERIFIED_ON, sources: SOURCES, wards: WARDS, categories: CATEGORIES, status: STATUS,
    iebcTotal: IEBC_CONSTITUENCY_TOTAL,
    commitments: COMMITMENTS, consultations: CONSULTATIONS, concernSummaries: CONCERN_SUMMARIES,
    statements: STATEMENTS, updates: UPDATES, events: EVENTS
  };
})();
