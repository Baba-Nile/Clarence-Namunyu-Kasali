/* ==========================================================================
   CAMPAIGN CONFIGURATION — the one file to edit before launch.
   Nothing here is invented: every value is empty until the campaign team
   supplies a verified one. Empty values are shown honestly as "not yet
   published" on the site; they never fall back to placeholder numbers.
   ========================================================================== */
window.CAMPAIGN_CONFIG = {

  /* Final public domain. Canonical/OG URLs in the HTML are set by
     tools/build.py (see README, "Setting the domain"). */
  siteUrl: '',

  /* Election date shown nowhere by default. Add a verified IEBC date here
     only if you want to use it in your own components. */
  electionDate: '',

  /* Verified contact channels. Leave '' until confirmed by the campaign team.
     whatsapp: international digits only, e.g. '2547XXXXXXXX' (no + or spaces).
     Never copy a number from another campaign. */
  contact: {
    whatsapp: '',
    phone: '',
    email: '',
    office: ''           // verified office / address text
  },

  /* Verified social channels (full https:// URLs). '' = not yet published. */
  social: {
    facebook: '',
    x: '',
    instagram: '',
    youtube: '',
    tiktok: ''
  },

  /* Form delivery. The forms post to a real endpoint and only show a success
     state when the server answers {"ok":true}. The bundled cPanel/PHP endpoint
     is api/submit.php (see README). If it is not configured, forms say so. */
  formEndpoint: 'api/submit.php',

  /* Approved manifesto document. '' = no download is shown. */
  manifestoPdf: '',

  /* Donations: verified payment instructions only. '' = page says support
     channels are not open yet. */
  donation: {
    instructions: ''     // plain text, e.g. verified paybill/till details
  },

  /* Language readiness. Add 'sw' to `enabled` ONLY when approved Kiswahili
     text exists in js/i18n.js (approved:true). Machine translation must not
     be published as campaign wording. */
  languages: {
    default: 'en',
    enabled: ['en'],
    labels: { en: 'English', sw: 'Kiswahili' }
  }
};
