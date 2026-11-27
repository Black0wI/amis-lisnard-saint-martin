// Affiche l'agenda officiel de Nouvelle Énergie pour les Antilles françaises.
// Source : https://www.unenouvelleenergie.fr/agenda.json (réutilisation autorisée,
// voir https://www.unenouvelleenergie.fr/agenda/reprendre/). Aucune inscription n'est recueillie ici.
(function () {
  var box = document.getElementById('agenda-liste');
  if (!box) return;
  var URL_AGENDA = 'https://www.unenouvelleenergie.fr/agenda.json?978,971,972,977';
  var TZ = 'America/Marigot';
  var EN = document.documentElement.lang === 'en';
  var T = EN ? {
    none: 'No events are announced for now in Saint-Martin, Guadeloupe, Martinique or Saint-Barthélemy in the official calendar.',
    sheet: 'Official page', signup: 'Sign up on the official website',
    fail: 'The official calendar could not be loaded. ', see: 'See the calendar on the official website'
  } : {
    none: "Aucun événement n'est annoncé pour le moment à Saint-Martin, en Guadeloupe, en Martinique ni à Saint-Barthélemy dans l'agenda officiel.",
    sheet: 'Fiche officielle', signup: "S'inscrire sur le site officiel",
    fail: "L'agenda officiel n'a pas pu être chargé. ", see: "Voir l'agenda sur le site officiel"
  };

  function fmtDate(ev) {
    var d = new Date(ev.date);
    if (isNaN(d)) return ev.date;
    var opts = { timeZone: TZ, weekday: 'short', day: 'numeric', month: 'short' };
    if (ev.horaireConfirme) { opts.hour = '2-digit'; opts.minute = '2-digit'; }
    return d.toLocaleString(EN ? 'en-GB' : 'fr-FR', opts);
  }
  function el(tag, text, cls) {
    var e = document.createElement(tag);
    if (text) e.textContent = text;
    if (cls) e.className = cls;
    return e;
  }
  function link(href, text) {
    var a = el('a', text);
    a.href = href; a.rel = 'noopener';
    return a;
  }

  fetch(URL_AGENDA)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) {
      var evs = (data && data.evenements) || [];
      box.textContent = '';
      if (!evs.length) {
        box.appendChild(el('p', T.none));
        return;
      }
      var ul = el('ul');
      evs.slice(0, 8).forEach(function (ev) {
        var li = el('li');
        li.appendChild(el('span', fmtDate(ev), 'date'));
        var body = el('div');
        body.appendChild(el('b', ev.titre));
        if (ev.lieu || ev.ville) body.appendChild(el('p', ev.lieu || ev.ville));
        var p = el('p');
        if (ev.url) p.appendChild(link(ev.url, T.sheet));
        if (ev.inscription) { p.appendChild(document.createTextNode(' · ')); p.appendChild(link(ev.inscription, T.signup)); }
        body.appendChild(p);
        li.appendChild(body);
        ul.appendChild(li);
      });
      box.appendChild(ul);
    })
    .catch(function () {
      box.textContent = '';
      var p = el('p', T.fail);
      p.appendChild(link('https://www.unenouvelleenergie.fr/agenda/', T.see));
      box.appendChild(p);
    });
})();
