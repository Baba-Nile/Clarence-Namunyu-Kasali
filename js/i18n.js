/* Language-ready content structure (English / Kiswahili).
   Elements with data-i18n="key" are replaced with strings from the ACTIVE language pack,
   but only if that pack has approved:true. Kiswahili is deliberately NOT approved:
   do not paste machine-translated text here. Have the campaign team (or a qualified translator)
   write and sign off each string, set approved:true, then add 'sw' to
   CAMPAIGN_CONFIG.languages.enabled in js/config.js. Long-form pages (manifesto, ward profiles)
   should be translated as separate approved pages, e.g. /sw/manifesto.html, with hreflang links. */
window.CAMPAIGN_I18N = {
  en: { approved: true, strings: {
    'nav.home': 'Home', 'nav.about': 'About Clarence', 'nav.manifesto': 'The Manifesto',
    'nav.gold': 'Gold, Land & Mining', 'nav.priorities': 'Our Priorities', 'nav.wards': 'Wards',
    'nav.community': 'Community Engagement', 'nav.news': 'News & Updates', 'nav.contact': 'Contact',
    'cta.join': 'Join the Campaign'
  } },
  sw: { approved: false, strings: {} }
};
