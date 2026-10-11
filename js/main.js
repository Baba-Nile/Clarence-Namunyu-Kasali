/* Clarence Namunyu Kasali campaign site — vanilla JS, no dependencies.
   Modules: menu, language readiness, data binding, charts, ward directory, dashboard,
   honest forms, manifesto navigation, sharing, config-driven contact channels, publishable feeds. */
(function () {
  'use strict';
  var d = document, C = window.CAMPAIGN_CONFIG || {}, D = window.CAMPAIGN_DATA || { wards: [], sources: [], categories: [], status: {} };
  var root = d.documentElement; root.classList.add('js');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var loadedAt = Date.now();

  function $(s, r) { return (r || d).querySelector(s); }
  function $$(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(n) { return Number(n).toLocaleString('en-GB'); }
  function longDate(iso) { var t = new Date(iso + 'T00:00:00'); return isNaN(t) ? iso : t.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); }
  function safeUrl(u) { return /^https?:\/\//i.test(u) ? u : ''; }

  /* ---------- Derived figures: computed from the ward records, never typed in ---------- */
  var wards = D.wards || [];
  var total = wards.reduce(function (s, w) { return s + w.voters; }, 0);
  function share(v) { return total ? (v / total * 100).toFixed(1) : '0.0'; }
  var maxV = wards.reduce(function (m, w) { return Math.max(m, w.voters); }, 0);

  /* ---------- Data binding ---------- */
  $$('[data-bind]').forEach(function (el) {
    var k = el.getAttribute('data-bind');
    if (k === 'total') el.textContent = fmt(total);
    else if (k === 'ward-count') el.textContent = wards.length;
    else if (k === 'verified-date' && D.verifiedOn) el.textContent = longDate(D.verifiedOn);
  });

  /* ---------- Menu and Ikolomani dropdown ---------- */
  var btn = $('.menu-btn'), navWrap = $('#site-nav');
  var subLi = $('.has-sub'), subBtn = subLi && $('.sub-btn', subLi);
  function setSub(open) { if (!subLi) return; subLi.classList.toggle('open', open); subBtn.setAttribute('aria-expanded', open ? 'true' : 'false'); }
  if (subBtn) {
    subBtn.addEventListener('click', function (e) { e.stopPropagation(); setSub(!subLi.classList.contains('open')); });
    d.addEventListener('click', function (e) { if (!subLi.contains(e.target) && !e.target.closest('.menu-btn')) setSub(false); });
    subLi.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setSub(false); subBtn.focus(); } });
    subLi.addEventListener('focusout', function (e) { if (!subLi.contains(e.relatedTarget)) setSub(false); });
    subLi.addEventListener('mouseenter', function () { if (matchMedia('(min-width:1000px)').matches) subBtn.setAttribute('aria-expanded', 'true'); });
    subLi.addEventListener('mouseleave', function () { if (!subLi.classList.contains('open')) subBtn.setAttribute('aria-expanded', 'false'); });
    if ($('.sub-btn.cur')) setSub(false);
  }
  if (btn && navWrap) {
    var setMenu = function (open) {
      navWrap.classList.toggle('open', open);
      d.body.classList.toggle('menu-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      var ic = btn.querySelector('i'); if (ic) ic.className = open ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
      var tx = btn.querySelector('span'); if (tx) tx.textContent = open ? 'Close' : 'Menu';
      if (open && subLi && window.innerWidth < 1000) setSub(true);
    };
    btn.addEventListener('click', function () { setMenu(!navWrap.classList.contains('open')); });
    navWrap.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    d.addEventListener('keydown', function (e) {
      if (!navWrap.classList.contains('open')) return;
      if (e.key === 'Escape') { setMenu(false); btn.focus(); return; }
      if (e.key === 'Tab') {
        var f = [btn].concat($$('a,button', navWrap)).filter(function (x) { return x.offsetParent !== null; });
        var i = f.indexOf(d.activeElement);
        if (e.shiftKey && (i <= 0)) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
      }
    });
    matchMedia('(min-width:1000px)').addEventListener('change', function (m) { if (m.matches) { setMenu(false); setSub(false); } });
  }

  /* ---------- Language readiness ---------- */
  (function () {
    var L = C.languages || { default: 'en', enabled: ['en'] }, I = window.CAMPAIGN_I18N || {};
    var cur = L.default;
    try { var s = localStorage.getItem('lang'); if (s && L.enabled.indexOf(s) > -1) cur = s; } catch (e) { }
    function apply(lang) {
      var pack = I[lang];
      if (lang !== L.default && !(pack && pack.approved)) return; // never show unapproved wording
      root.setAttribute('lang', lang);
      $$('[data-i18n]').forEach(function (el) {
        var v = pack && pack.strings && pack.strings[el.getAttribute('data-i18n')];
        if (v) el.textContent = v;
      });
    }
    if (L.enabled.length > 1) {
      var slot = $('#site-nav'); if (slot) {
        var box = d.createElement('li'); box.className = 'lang'; box.setAttribute('role', 'group'); box.setAttribute('aria-label', 'Language');
        L.enabled.forEach(function (code) {
          var b = d.createElement('button'); b.type = 'button'; b.textContent = (L.labels || {})[code] || code; b.setAttribute('lang', code);
          b.setAttribute('aria-pressed', code === cur ? 'true' : 'false');
          b.addEventListener('click', function () { try { localStorage.setItem('lang', code); } catch (e) { } $$('button', box).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); apply(code); });
          box.appendChild(b);
        });
        slot.insertBefore(box, slot.lastChild);
      }
    }
    if (cur !== L.default) apply(cur);
  })();

  /* ---------- Charts ---------- */
  function sortedWards(by) {
    var a = wards.slice();
    if (by === 'name') a.sort(function (x, y) { return x.name.localeCompare(y.name); });
    else a.sort(function (x, y) { return y.voters - x.voters; });
    return a;
  }
  function renderBars(ol, by) {
    if (!ol || !wards.length) return;
    var link = ol.getAttribute('data-link') !== 'off';
    ol.classList.remove('in');
    ol.innerHTML = sortedWards(by).map(function (w) {
      var nm = link ? '<a href="wards.html#' + w.id + '">' + esc(w.name) + '</a>' : esc(w.name);
      return '<li><span class="nm">' + nm + '</span>' +
        '<span class="tr" aria-hidden="true"><span class="fl" style="--w:' + (w.voters / maxV * 100).toFixed(2) + '%"></span></span>' +
        '<span class="vl"><b>' + fmt(w.voters) + '</b> registered voters, ' + share(w.voters) + '% of the constituency</span></li>';
    }).join('');
    ol.classList.add('in');
  }
  $$('ol.bars[data-chart]').forEach(function (ol) { renderBars(ol, 'size'); });

  /* ---------- Status chips ---------- */
  function chip(kind) {
    var s = (D.status || {})[kind] || { label: kind };
    var cls = { original: 'pill--ok', 'official-site': 'pill--ok', reported: 'pill--rep', awaiting: 'pill--wait', research: 'pill--res' }[kind] || '';
    return '<span class="pill ' + cls + '">' + esc(s.label) + '</span>';
  }
  function srcById(id) { return (D.sources || []).filter(function (s) { return s.id === id; })[0]; }
  function srcLink(id) { var s = srcById(id); if (!s) return ''; return s.url ? '<a href="' + esc(s.url) + '" rel="noopener">' + esc(s.publisher) + '</a>' : esc(s.publisher); }

  /* ---------- Ward directory ---------- */
  var dir = $('#ward-directory');
  if (dir && wards.length) {
    var cats = D.categories || [];
    var html = wards.map(function (w) {
      var seg = wards.map(function (o) { return '<span class="' + (o.id === w.id ? 'me' : '') + '" style="--w:' + share(o.voters) + '%"></span>'; }).join('');
      var documented = w.documented.length
        ? '<h3>Documented</h3><ul class="rlist">' + w.documented.map(function (x) { return '<li>' + chip('reported') + '<span>' + esc(x.t) + '</span><span class="src">' + srcLink(x.src) + ', ' + esc(x.date) + '. A news report, not an official record.</span></li>'; }).join('') + '</ul>'
        : '';
      var research = '<ul class="rlist">' + w.research.map(function (r) { return '<li>' + chip(r.s) + '<span>' + esc(r.t) + '</span></li>'; }).join('') + '</ul>';
      return '<article class="ward" id="' + w.id + '" data-ward="' + w.id + '" aria-labelledby="h-' + w.id + '">' +
        '<div class="ward-top"><h2 id="h-' + w.id + '">' + esc(w.name) + '</h2>' +
        '<div><p class="vote">' + fmt(w.voters) + '<small>registered voters in 2022 (IEBC), ' + share(w.voters) + '% of the reported constituency electorate</small></p>' +
        '<div class="seg" role="img" aria-label="' + esc(w.name) + ' is ' + share(w.voters) + ' percent of the constituency electorate of ' + fmt(total) + '">' + seg + '</div></div></div>' +
        '<div class="ward-body"><div class="ward-actions" style="margin-top:0;flex-direction:column;align-items:flex-start"><button class="btn btn--sm" type="button" aria-expanded="false" aria-controls="p-' + w.id + '" data-toggle="p-' + w.id + '">Development priorities</button>' +
        '<a class="btn btn--ghost btn--sm" href="community.html?ward=' + w.id + '&amp;category=' + w.category + '#form">Share a concern</a></div>' +
        '<div>' + documented + '<div class="disclose" id="p-' + w.id + '" hidden><h3>Topics to research with residents</h3><p class="fine">Proposed for investigation. These are not findings and have not been verified for this ward.</p>' + research + '</div></div></div></article>';
    }).join('');
    dir.innerHTML = html;

    dir.addEventListener('click', function (e) {
      var t = e.target.closest('[data-toggle]'); if (!t) return;
      var p = d.getElementById(t.getAttribute('data-toggle')), open = t.getAttribute('aria-expanded') === 'true';
      t.setAttribute('aria-expanded', open ? 'false' : 'true'); p.hidden = open;
    });

    var fbar = $('#ward-filter');
    var applyFilter = function (id, scroll) {
      var valid = wards.some(function (w) { return w.id === id; }); if (!valid) id = 'all';
      $$('.ward', dir).forEach(function (a) {
        var show = id === 'all' || a.id === id; a.hidden = !show;
        var tg = $('[data-toggle]', a), pn = $('.disclose', a);
        if (id !== 'all' && show && tg && pn.hidden) tg.click();
      });
      if (fbar) $$('button', fbar).forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-ward') === id ? 'true' : 'false'); });
      var live = $('#ward-live'); if (live) live.textContent = id === 'all' ? 'Showing all four wards.' : 'Showing ' + (wards.filter(function (w) { return w.id === id; })[0] || {}).name + ' only.';
      if (scroll && id !== 'all') { var el = d.getElementById(id); if (el) el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }
    };
    if (fbar) {
      fbar.innerHTML = '<button type="button" data-ward="all" aria-pressed="true">All wards</button>' + wards.map(function (w) { return '<button type="button" data-ward="' + w.id + '" aria-pressed="false">' + esc(w.name) + '</button>'; }).join('');
      fbar.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return; var id = b.getAttribute('data-ward');
        applyFilter(id, false);
        try { history.replaceState(null, '', id === 'all' ? location.pathname : '#' + id); } catch (er) { }
      });
    }
    var fromHash = function () { var h = location.hash.slice(1); applyFilter(h || 'all', !!h); };
    addEventListener('hashchange', fromHash); fromHash();
  }

  /* ---------- Dashboard ---------- */
  var dchart = $('#dash-chart');
  if (dchart) {
    renderBars(dchart, 'size');
    $$('[data-sort]').forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-sort]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        renderBars(dchart, b.getAttribute('data-sort')); buildTable(b.getAttribute('data-sort'));
      });
    });
  }
  var tb = $('#dash-table tbody');
  function buildTable(by) {
    if (!tb) return;
    var summaries = D.concernSummaries || [];
    tb.innerHTML = sortedWards(by || 'size').map(function (w) {
      return '<tr><th scope="row"><a href="wards.html#' + w.id + '">' + esc(w.name) + '</a></th><td class="num">' + fmt(w.voters) + '</td><td class="num">' + share(w.voters) + '%</td>' +
        '<td><ul>' + w.research.filter(function (r) { return r.s === 'research'; }).map(function (r) { return '<li>' + esc(r.t) + '</li>'; }).join('') + '</ul></td></tr>';
    }).join('');
    var tf = $('#dash-table tfoot td.t-total'); if (tf) tf.textContent = fmt(total);
  }
  buildTable('size');
  var chk = $('#sum-check');
  if (chk) {
    var ok = total === D.iebcTotal;
    chk.className = 'check' + (ok ? '' : ' bad');
    chk.innerHTML = '<i class="fa-solid ' + (ok ? 'fa-circle-check' : 'fa-triangle-exclamation') + '" aria-hidden="true"></i><span>' +
      (ok ? 'Check passed: the four ward figures add up to ' + fmt(total) + ', which equals the IEBC constituency total of ' + fmt(D.iebcTotal) + '.'
        : 'Check failed: the ward figures add up to ' + fmt(total) + ' but the IEBC constituency total is ' + fmt(D.iebcTotal) + '. Do not publish until this is resolved.') + '</span>';
  }
  var st = $('#sources-table tbody');
  if (st) {
    st.innerHTML = (D.sources || []).filter(function (s) { return s.status !== 'awaiting'; }).map(function (s) {
      return '<tr><th scope="row">' + esc(s.publisher) + '<br><span style="font-weight:500">' + esc(s.title) + '</span></th><td>' + esc(s.supports) + '</td><td>' + esc(s.period) + '</td><td>' + (s.verified ? esc(longDate(s.verified)) : 'Not yet') + '</td><td>' + chip(s.status) + '</td><td>' +
        (s.url ? '<a href="' + esc(s.url) + '" rel="noopener">Open source</a>' : 'Link to be added') + '</td></tr>';
    }).join('');
  }

  /* ---------- Config-driven contact channels (nothing invented) ---------- */
  var ct = C.contact || {}, so = C.social || {};
  function waLink(msg) { return ct.whatsapp ? 'https://wa.me/' + ct.whatsapp.replace(/\D/g, '') + (msg ? '?text=' + encodeURIComponent(msg) : '') : ''; }
  $$('[data-whatsapp]').forEach(function (el) { if (ct.whatsapp) { el.href = waLink(el.getAttribute('data-whatsapp')); el.hidden = false; } else el.hidden = true; });
  $$('[data-whatsapp-fallback]').forEach(function (el) { el.hidden = !!ct.whatsapp; });
  var chanBox = $('[data-channels]');
  if (chanBox) {
    var rows = [
      ['fa-brands fa-whatsapp', 'WhatsApp', ct.whatsapp, ct.whatsapp && waLink('Hello, I am writing from the Clarence Namunyu Kasali campaign website.'), 'Message the campaign on WhatsApp'],
      ['fa-solid fa-phone', 'Phone', ct.phone, ct.phone && 'tel:' + ct.phone.replace(/[^\d+]/g, ''), ct.phone],
      ['fa-solid fa-envelope', 'Email', ct.email, ct.email && 'mailto:' + ct.email, ct.email],
      ['fa-solid fa-location-dot', 'Campaign office', ct.office, '', ct.office],
      ['fa-brands fa-facebook-f', 'Facebook', so.facebook, so.facebook, 'Campaign Facebook page'],
      ['fa-brands fa-x-twitter', 'X', so.x, so.x, 'Campaign account on X'],
      ['fa-brands fa-instagram', 'Instagram', so.instagram, so.instagram, 'Campaign Instagram'],
      ['fa-brands fa-youtube', 'YouTube', so.youtube, so.youtube, 'Campaign YouTube channel'],
      ['fa-brands fa-tiktok', 'TikTok', so.tiktok, so.tiktok, 'Campaign TikTok']
    ];
    var have = rows.filter(function (r) { return !!r[2]; });
    chanBox.innerHTML = have.length ? have.map(function (r) {
      var body = r[3] ? '<a href="' + esc(r[3]) + '"' + (/^https?/.test(r[3]) ? ' rel="noopener" target="_blank"' : '') + '>' + esc(r[4]) + '</a>' : '<span>' + esc(r[4]) + '</span>';
      return '<li><strong>' + r[1] + '</strong>' + body + '</li>';
    }).join('') : '<li>Use the form to reach the campaign team.</li>';
  }
  var ftc = $('[data-footer-contact]');
  if (ftc) {
    var li = [];
    if (ct.phone) li.push('<li><a href="tel:' + esc(ct.phone.replace(/[^\d+]/g, '')) + '">' + esc(ct.phone) + '</a></li>');
    if (ct.email) li.push('<li><a href="mailto:' + esc(ct.email) + '">' + esc(ct.email) + '</a></li>');
    if (ct.office) li.push('<li>' + esc(ct.office) + '</li>');
    ftc.innerHTML = li.join('');
  }
  var fts = $('[data-footer-social]');
  if (fts) {
    var ic = { facebook: 'fa-facebook-f', x: 'fa-x-twitter', instagram: 'fa-instagram', youtube: 'fa-youtube', tiktok: 'fa-tiktok' }, out = [];
    Object.keys(ic).forEach(function (k) { if (so[k]) out.push('<a href="' + esc(so[k]) + '" rel="noopener" target="_blank" aria-label="Campaign on ' + k + '"><i class="fa-brands ' + ic[k] + '" aria-hidden="true"></i></a>'); });
    fts.innerHTML = out.join('');
  }
  var pdf = $('[data-manifesto-pdf]');
  if (pdf) { if (C.manifestoPdf) { var a = $('a', pdf); a.href = C.manifestoPdf; pdf.querySelector('[data-pdf-yes]').hidden = false; pdf.querySelector('[data-pdf-no]').hidden = true; } }
  var don = $('[data-donation]');
  if (don && C.donation && C.donation.instructions) { don.textContent = C.donation.instructions; $('[data-donation-none]') && ($('[data-donation-none]').hidden = true); don.hidden = false; }

  /* ---------- Forms: validate, then really send, or say plainly that nothing was sent ---------- */
  var qs = new URLSearchParams(location.search);
  $$('select[data-options]').forEach(function (sel) {
    var list = sel.getAttribute('data-options') === 'wards' ? wards.map(function (w) { return { id: w.id, label: w.name }; }) : (D.categories || []);
    sel.insertAdjacentHTML('beforeend', list.map(function (o) { return '<option value="' + esc(o.id) + '">' + esc(o.label) + '</option>'; }).join(''));
    var pre = qs.get(sel.name); if (pre && list.some(function (o) { return o.id === pre; })) sel.value = pre;
  });

  function fieldWrap(el) { return el.closest('.field') || el.parentNode; }
  function validate(form) {
    var errs = [];
    $$('.err', form).forEach(function (x) { x.remove(); });
    $$('[aria-invalid]', form).forEach(function (x) { x.removeAttribute('aria-invalid'); if (x.dataset.desc !== undefined) x.setAttribute('aria-describedby', x.dataset.desc); else x.removeAttribute('aria-describedby'); });
    function fail(el, msg) {
      var id = 'err-' + (el.id || el.name), p = d.createElement('p'); p.className = 'err'; p.id = id; p.textContent = msg;
      (el.closest('fieldset') || fieldWrap(el)).appendChild(p);
      el.setAttribute('aria-invalid', 'true');
      el.setAttribute('aria-describedby', ((el.dataset.desc || '') + ' ' + id).trim());
      errs.push({ el: el, msg: msg });
    }
    $$('input,select,textarea', form).forEach(function (el) {
      if (el.type === 'hidden' || el.closest('.hp') || el.type === 'submit') return;
      if (el.dataset.desc === undefined) el.dataset.desc = el.getAttribute('aria-describedby') || '';
    });
    $$('input,select,textarea', form).forEach(function (el) {
      if (el.type === 'hidden' || el.closest('.hp') || el.type === 'submit' || el.type === 'checkbox' && el.closest('[data-require-one]')) return;
      var v = (el.value || '').trim(), req = el.required, em = el.getAttribute('data-err') || 'This field is required.';
      if (el.type === 'checkbox') { if (req && !el.checked) fail(el, em); return; }
      if (req && !v) { fail(el, em); return; }
      if (v && el.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) fail(el, 'Enter an email address in the form name@example.com.');
      else if (v && el.type === 'tel' && (v.replace(/\D/g, '').length < 9 || !/^[+\d][\d\s()-]+$/.test(v))) fail(el, 'Enter a phone number with at least 9 digits, for example 0712 345 678.');
      else if (v && el.minLength > 0 && v.length < el.minLength) fail(el, el.getAttribute('data-minmsg') || 'Please write at least ' + el.minLength + ' characters.');
    });
    $$('[data-require-one]', form).forEach(function (fs) {
      if (!$$('input:checked', fs).length) fail($('input', fs), fs.getAttribute('data-require-one'));
    });
    return errs;
  }

  $$('form[data-form]').forEach(function (form) {
    var type = form.getAttribute('data-form'), summary = $('.summary', form.parentNode), status = $('.status', form.parentNode), banner = $('[data-form-banner]', form.parentNode);
    var sb = $('button[type=submit]', form), sbText = sb ? sb.innerHTML : '';
    var msg = $('textarea[maxlength]', form), cnt = $('.cnt', form);
    if (msg && cnt) { var upd = function () { cnt.textContent = msg.value.length + ' of ' + msg.maxLength + ' characters'; }; msg.addEventListener('input', upd); upd(); }

    // Tell visitors up front whether submissions can currently be delivered.
    if (banner) {
      var showBanner = function () { banner.hidden = false; };
      if (!C.formEndpoint) showBanner();
      else fetch(C.formEndpoint + '?status=1', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (j) { if (!j || j.configured !== true) showBanner(); }).catch(showBanner);
    }

    function showStatus(kind, title, body, extra) {
      if (!status) return;
      status.className = 'status' + (kind === 'ok' ? '' : kind === 'warn' ? ' status--warn' : ' status--err');
      status.innerHTML = '<h3>' + esc(title) + '</h3><p>' + esc(body) + '</p>' + (extra || '');
      status.hidden = false; status.setAttribute('tabindex', '-1'); status.focus();
    }
    function copyText() {
      var lines = []; new FormData(form).forEach(function (v, k) { if (v && k !== 'website' && k !== 'consent') { var l = form.querySelector('[name="' + k + '"]'); var lab = l && fieldWrap(l).querySelector('label,legend'); lines.push((lab ? lab.textContent.replace('*', '').replace(/\s+/g, ' ').trim() : k) + ': ' + v); } });
      return lines.join('\n');
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (status) status.hidden = true;
      var errs = validate(form);
      if (summary) {
        if (errs.length) {
          summary.innerHTML = '<h3>Please fix ' + errs.length + (errs.length === 1 ? ' problem' : ' problems') + ' before sending</h3><ul>' + errs.map(function (x) { return '<li><a href="#' + (x.el.id || '') + '">' + esc(x.msg) + '</a></li>'; }).join('') + '</ul>';
          summary.hidden = false; summary.setAttribute('tabindex', '-1'); summary.focus();
          $$('a', summary).forEach(function (a, i) { a.addEventListener('click', function (ev) { ev.preventDefault(); errs[i].el.focus(); }); });
        } else summary.hidden = true;
      }
      if (errs.length) { if (!summary) errs[0].el.focus(); return; }

      var fd = new FormData(form); fd.append('type', type); fd.append('elapsed', String(Date.now() - loadedAt));
      if (sb) { sb.setAttribute('aria-disabled', 'true'); sb.disabled = true; sb.textContent = 'Sending…'; }
      var ctl = ('AbortController' in window) ? new AbortController() : null, to = ctl && setTimeout(function () { ctl.abort(); }, 15000);
      var done = function () { if (to) clearTimeout(to); if (sb) { sb.disabled = false; sb.removeAttribute('aria-disabled'); sb.innerHTML = sbText; } };
      var copyBtn = '<button type="button" class="btn btn-line btn-sm" data-copy>Copy my message</button>';
      var bindCopy = function () { var b = $('[data-copy]', status); if (b) b.addEventListener('click', function () { var t = copyText(); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { b.textContent = 'Copied'; }, function () { b.textContent = 'Copy failed. Select the text in the form instead.'; }); }); };
      if (!C.formEndpoint) { done(); showStatus('warn', 'Your message has not been sent', 'This form is not connected to a delivery service yet, so nothing was sent. The campaign team needs to finish setting it up before launch.', copyBtn); bindCopy(); return; }
      fetch(C.formEndpoint, { method: 'POST', body: fd, signal: ctl ? ctl.signal : undefined, headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.json().catch(function () { return null; }).then(function (j) { return { ok: r.ok, j: j, code: r.status }; }); })
        .then(function (res) {
          done();
          if (res.ok && res.j && res.j.ok === true) {
            form.reset(); if (cnt) cnt.textContent = '0 of ' + (msg ? msg.maxLength : '') + ' characters';
            showStatus('ok', 'Message received', 'The website server accepted your message and passed it to the campaign team’s inbox. The team can only reply if you gave a phone number or email address. Do not use this form for emergencies or urgent safety reports.');
          } else if (res.j && res.j.error === 'too_fast') { showStatus('warn', 'Please try again', 'The form was submitted too quickly to be checked. Nothing was sent. Wait a few seconds and press Send again.'); }
          else if (res.code === 429) { showStatus('warn', 'Too many messages', 'Nothing was sent. Please wait a while before sending another message.'); }
          else if (res.code === 404 || res.code === 405 || res.code === 501 || res.code === 503 || (res.j && res.j.error === 'not_configured')) { showStatus('warn', 'Your message has not been sent', 'This form is not connected to a working delivery service yet, so nothing was sent. The campaign team needs to finish setting it up before launch.', copyBtn); bindCopy(); }
          else { showStatus('err', 'Your message has not been sent', 'The server could not accept your message. Nothing was sent. Please try again later.', copyBtn); bindCopy(); }
        })
        .catch(function () { done(); showStatus('err', 'Your message has not been sent', 'We could not reach the server, so nothing was sent. Check your connection and try again.', copyBtn); bindCopy(); });
    });
  });

  /* ---------- Manifesto navigation: scroll-spy + reading progress ---------- */
  var body = $('#manifesto-body');
  if (body) {
    var links = $$('.toc a, .m-mobile-toc a'), targets = {};
    links.forEach(function (a) { var id = a.getAttribute('href').slice(1); targets[id] = d.getElementById(id); });
    var ids = Object.keys(targets).filter(function (k) { return targets[k]; });
    var bar = $('.progress');
    var onScroll = function () {
      var cur = ids[0];
      ids.forEach(function (id) { if (targets[id].getBoundingClientRect().top < 190) cur = id; });
      links.forEach(function (a) { var on = a.getAttribute('href') === '#' + cur && scrollY > 120; if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
      var m = $('.toc ol'), act = m && $('a[aria-current]', m);
      if (act && m.scrollWidth > m.clientWidth) m.scrollTo({ left: act.offsetLeft - 24, behavior: reduce ? 'auto' : 'smooth' });
      if (bar) { var r = body.getBoundingClientRect(), h = r.height - innerHeight * .6, p = Math.min(1, Math.max(0, -r.top / (h > 0 ? h : 1))); bar.style.transform = 'scaleX(' + p.toFixed(3) + ')'; }
    };
    onScroll(); addEventListener('scroll', onScroll, { passive: true }); addEventListener('resize', onScroll);
  }

  /* ---------- Social sharing ---------- */
  $$('[data-share]').forEach(function (box) {
    var can = $('link[rel=canonical]'), url = can && can.href && can.href.indexOf('CAMPAIGN-DOMAIN') === -1 ? can.href : location.href.split('#')[0];
    var title = box.getAttribute('data-share') || d.title, u = encodeURIComponent(url), t = encodeURIComponent(title);
    box.innerHTML = '<span class="lbl">Share</span>' +
      '<a href="https://wa.me/?text=' + t + '%20' + u + '" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i>WhatsApp</a>' +
      '<a href="https://www.facebook.com/sharer/sharer.php?u=' + u + '" target="_blank" rel="noopener"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i>Facebook</a>' +
      '<a href="https://twitter.com/intent/tweet?text=' + t + '&url=' + u + '" target="_blank" rel="noopener"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i>X</a>' +
      '<button type="button" data-copylink><i class="fa-solid fa-link" aria-hidden="true"></i>Copy link</button>';
    $('[data-copylink]', box).addEventListener('click', function (e) {
      var b = e.currentTarget; (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { b.lastChild.textContent = 'Copied'; }, function () { b.lastChild.textContent = url; });
    });
  });

  /* ---------- Publishable feeds: render only what the campaign has verified and added to data.js ---------- */
  function feed(name, items, tpl) {
    $$('[data-feed="' + name + '"]').forEach(function (box) {
      if (!items || !items.length) return;
      var em = $('[data-empty]', box); if (em) em.hidden = true;
      var ul = d.createElement('ul'); ul.className = 'feed-list';
      items.slice().sort(function (a, b) { return (b.date || '').localeCompare(a.date || ''); }).forEach(function (it) { ul.insertAdjacentHTML('beforeend', '<li>' + tpl(it) + '</li>'); });
      box.appendChild(ul);
    });
  }
  function ln(u, t) { var s = safeUrl(u || ''); return s ? '<a class="tlink" href="' + esc(s) + '">' + esc(t) + '</a>' : ''; }
  feed('updates', D.updates, function (u) { return '<time datetime="' + esc(u.date) + '">' + esc(longDate(u.date)) + (u.category ? ' · ' + esc(u.category) : '') + '</time><h4>' + esc(u.title) + '</h4><p>' + esc(u.excerpt || '') + '</p>' + ln(u.url, 'Read more'); });
  feed('events', D.events, function (e) { return '<time datetime="' + esc(e.date) + '">' + esc(longDate(e.date)) + (e.time ? ', ' + esc(e.time) : '') + '</time><h4>' + esc(e.title) + '</h4><p>' + esc([e.place, e.ward].filter(Boolean).join(', ')) + '</p>' + ln(e.url, 'Details'); });
  feed('consultations', D.consultations, function (c) { return '<time datetime="' + esc(c.date) + '">' + esc(longDate(c.date)) + '</time><h4>' + esc([c.place, c.ward].filter(Boolean).join(', ')) + '</h4><p>' + esc(c.summary || '') + '</p>' + ln(c.reportUrl, 'Read the report'); });
  feed('statements', D.statements, function (s) { return '<time datetime="' + esc(s.date) + '">' + esc(longDate(s.date)) + '</time><h4>' + esc(s.title) + '</h4>' + ln(s.url, 'Read the statement'); });
  feed('concerns', D.concernSummaries, function (c) { return '<time>' + esc(c.period || '') + '</time><h4>' + esc([c.ward, c.category].filter(Boolean).join(', ')) + '</h4><p>' + esc(String(c.count)) + ' concerns received. ' + esc(c.note || '') + '</p>'; });
  var cbody = $('#commit-body');
  if (cbody && (D.commitments || []).length) {
    cbody.innerHTML = D.commitments.map(function (c) { return '<tr><th scope="row">' + esc(c.priority) + '</th><td>' + esc(c.commitment) + '</td><td>' + esc(c.status) + '</td><td>' + esc(longDate(c.updated)) + '</td><td>' + (safeUrl(c.url || '') ? '<a href="' + esc(c.url) + '">' + esc(c.source || 'Source') + '</a>' : esc(c.source || '')) + '</td></tr>'; }).join('');
    $$('[data-feed="commitments"] [data-empty]').forEach(function (x) { x.hidden = true; });
  }
})();

/* back to top: shown after scrolling on long pages */
(function () {
  var b = document.querySelector('.totop'); if (!b) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function upd() { var long = document.documentElement.scrollHeight > window.innerHeight * 2.5; b.hidden = !long; b.classList.toggle('show', long && window.scrollY > 700); }
  window.addEventListener('scroll', upd, { passive: true }); window.addEventListener('resize', upd); upd();
  b.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); var m = document.getElementById('main'); if (m) { m.setAttribute('tabindex', '-1'); m.focus({ preventScroll: true }); } });
})();

/* subtle scroll reveal for below-the-fold sections. Progressive enhancement: skipped entirely with reduced motion
   or without IntersectionObserver, and anything already on screen at load is left alone (no flash, no layout shift). */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var sel = '.sec-title, .msg, .cards .card, .meet > *, .wards-home > *, .photos figure, .cta-g, .feature-g > *';
  var vh = window.innerHeight, els = [];
  document.querySelectorAll(sel).forEach(function (el) { if (el.getBoundingClientRect().top > vh) els.push(el); });
  if (!els.length) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  els.forEach(function (el) { el.classList.add('js-rv'); io.observe(el); });
})();
