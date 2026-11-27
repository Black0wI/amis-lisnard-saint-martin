#!/usr/bin/env python3
"""Génère les pages HTML du site à partir du gabarit commun.

Usage : python3 outils/build.py   (depuis la racine du dépôt)
Les pages sont écrites à la racine du dépôt. Modifier le contenu ici, puis relancer.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent.parent
MAJ = "27 novembre 2026"
NE = "https://www.unenouvelleenergie.fr"
ADHESION = "https://soutenir.unenouvelleenergie.fr/adhesion"

SRC = {
    "iedom": ("https://outremers360.com/bassin-atlantique-appli/saint-martin-un-tourisme-en-progression-mais-dimportants-defis-structurels-a-relever-selon-le-rapport-annuel-de-liedom",
              "IEDOM, rapport annuel 2025, résumé par Outremers360 (19/10/2026)"),
    "rup": ("https://ec.europa.eu/regional_policy/sources/policy/themes/outermost-regions/rup_2024/regional_fiche_saint_martin.pdf",
            "Commission européenne, fiche régionale Saint-Martin (régions ultrapériphériques)"),
    "senat": ("https://www.senat.fr/rap/l25-514/l25-514-syn.pdf", "Sénat, rapport L25-514 sur Saint-Martin et Sint Maarten (avril 2026)"),
    "hopital": ("https://www.senat.fr/questions/base/2026/qSEQ26060937G.html", "Sénat, question d'actualité 0937G (juin 2026)"),
    "voeux": ("https://www.com-saint-martin.fr/en/actualites/les-voeux-2026-du-president-louis-mussington", "Collectivité de Saint-Martin, vœux 2026 du président"),
    "axe1": (NE + "/notre-programme/etre-maitre-de-notre-destin/", "Programme, axe 1 « Être maître de notre destin »"),
    "axe2": (NE + "/notre-programme/reussir-une-nouvelle-ambition-francaise/", "Programme, axe 2 « Réussir une nouvelle ambition française »"),
    "axe3": (NE + "/notre-programme/generer-un-renouveau-civique/", "Programme, axe 3 « Générer un renouveau civique »"),
    "securite": (NE + "/notre-programme/securite/", "Programme, page Sécurité"),
    "immigration": (NE + "/notre-programme/immigration/", "Programme, page Immigration"),
    "sante": (NE + "/notre-programme/sante/", "Programme, page Santé"),
    "education": (NE + "/notre-programme/education/", "Programme, page Éducation"),
    "programme": (NE + "/notre-programme/", "Programme de Nouvelle Énergie"),
}


def s(key, label=None):
    url, title = SRC[key]
    return f'<a href="{url}" rel="noopener">{label or title}</a>'


NAV = [
    ("index.html", "Accueil"),
    ("saint-martin.html", "Saint-Martin d'abord"),
    ("regalien.html", "La France qui tient"),
    ("chiffres.html", "L'île en chiffres"),
    ("agir.html", "Agir"),
    ("english.html", "English"),
]


CSS_V = hashlib.sha1((ROOT / "assets/style.css").read_bytes()).hexdigest()[:8]
JS_V = hashlib.sha1((ROOT / "assets/agenda.js").read_bytes()).hexdigest()[:8]


def page(fname, title, description, body, lang="fr", scripts=""):
    nav = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == fname else ""}{" lang=\"en\"" if href == "english.html" else ""}>{label}</a></li>'
        for href, label in NAV
    )
    full_title = "Les amis de David Lisnard à Saint-Martin" if fname == "index.html" else f"{title} · Les amis de David Lisnard à Saint-Martin"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta name="theme-color" content="#1D257A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@500;600;700&display=swap">
<link rel="stylesheet" href="assets/style.css?v={CSS_V}">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="flag" role="note">
  <div class="wrap">
    <span><strong>Site non officiel</strong> · Initiative indépendante de soutien à David Lisnard et Nouvelle Énergie : non gérée ni validée par le mouvement.</span>
    <a href="{NE}/" rel="noopener">Site officiel de Nouvelle Énergie</a>
  </div>
</div>
<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="dot" aria-hidden="true"></span><span class="bt"><b>Les amis de David Lisnard</b><span>à Saint-Martin</span></span></a>
    <nav aria-label="Navigation principale"><ul>
{nav}
    </ul></nav>
    <a class="pill" href="{ADHESION}" rel="noopener">Adhérer</a>
  </div>
</header>
<main id="contenu">
{body}
</main>
<footer>
  <div class="wrap">
    <div>
      <h3>Initiative indépendante</h3>
      <p>Initiative indépendante de soutien à David Lisnard et Nouvelle Énergie : non gérée ni validée par le mouvement. Ce site suit la <a href="{NE}/charte-de-partage/" rel="noopener">charte de partage et de création</a> publiée par Nouvelle Énergie (version du 23 novembre 2026).</p>
      <p>Aucun cookie, aucune mesure d'audience, aucun formulaire, aucune publicité payante. Mise à jour : {MAJ}.</p>
    </div>
    <div>
      <h3>Informations</h3>
      <p><a href="mentions-legales.html">Mentions légales et données personnelles</a></p>
      <p><a href="{NE}/notre-programme/" rel="noopener">Programme officiel</a> · <a href="{ADHESION}" rel="noopener">Adhérer</a></p>
    </div>
  </div>
</footer>
{scripts}
</body>
</html>
"""


def hero_page(eyebrow, h1, lead):
    return f"""<div class="intro"><div class="wrap">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
</div></div>"""


# ---------------------------------------------------------------------------
# Propositions locales : constat sourcé, mesure du programme vérifiée, piste du collectif
# ---------------------------------------------------------------------------
PROPS = [
    dict(n="Libertés locales", titre="Un droit d'adapter les normes nationales à l'île",
         court="Le conseil territorial pourrait demander l'adaptation d'une règle nationale, avec une réponse rapide de l'État.",
         constat=f"Saint-Martin exerce déjà des compétences propres, comme la fiscalité et l'urbanisme, mais beaucoup de règles nationales restent pensées pour l'Hexagone, sur une île de 53 km² partagée avec Sint Maarten. {s('rup', 'Fiche RUP')}",
         programme=f"Un « transfert massif de compétences » aux collectivités et « l'autonomie du pouvoir réglementaire local », pour « adapter les politiques publiques aux besoins concrets et particuliers locaux ». {s('axe3')}",
         piste="Ouvrir à la Collectivité un droit d'adaptation des normes nationales, sur demande du conseil territorial, avec un délai de réponse court pour l'État.",
         qui="L'État, par une révision de la loi organique statutaire."),
    dict(n="Eau", titre="L'eau potable, chantier prioritaire",
         court="L'eau coûte plus de deux fois la moyenne nationale et près d'un tiers se perd dans le réseau.",
         constat=f"L'eau coûtait 5,51 €/m³ en 2022, contre 2,11 €/m³ en moyenne nationale en 2021, et environ 30 % se perd dans les fuites du réseau. {s('rup', 'Fiche RUP')}",
         programme=f"Le programme national ne contient pas de mesure dédiée à l'eau. La piste s'appuie sur la décentralisation et l'allègement normatif qu'il défend. {s('axe3')}",
         piste="Faire du réseau et du dessalement un chantier prioritaire, avec un objectif public de réduction des pertes et un suivi publié chaque année.",
         qui="La Collectivité et son établissement des eaux, avec le soutien de l'État."),
    dict(n="Emploi", titre="Faire de Saint-Martin une zone d'embauche prioritaire",
         court="Appliquer en priorité ici les charges patronales négatives prévues pour l'embauche d'allocataires du RSA.",
         constat=f"Le recensement de 2023 compte 27 % de chômage, et la population active a baissé de 11,8 % entre 2013 et 2023. L'emploi salarié atteint pourtant un record de 8 119 salariés fin 2025. {s('iedom', 'IEDOM')}",
         programme=f"« Un système de charges patronales négatives pour les embauches de personnes au RSA depuis plus de 2 ans sera créé. » {s('axe2')}",
         piste="Déployer cette mesure en priorité à Saint-Martin, avec des formations aux métiers du tourisme et du BTP.",
         qui="L'État (cotisations sociales). L'articulation avec la fiscalité propre de la Collectivité reste à étudier."),
    dict(n="Logement", titre="Devenir propriétaire de sa résidence principale",
         court="Moins d'un ménage sur trois est propriétaire, contre près de deux sur trois au niveau national.",
         constat=f"28,3 % de propriétaires en 2020, contre 63,6 % en moyenne nationale, et 13,9 % de logements vacants en 2018. {s('rup', 'Fiche RUP')}",
         programme=f"Le programme prévoit de pouvoir « débloquer une part capitalisée » de l'épargne retraite « pour l'achat de la résidence principale », et sort la politique du logement du « seul logement social ». {s('axe2')}",
         piste="Accompagner les familles résidentes vers la propriété et remettre sur le marché les logements vacants, en lien avec le Programme local de l'habitat 2025-2030.",
         qui="La Collectivité (urbanisme, habitat) et l'État (épargne, aides)."),
    dict(n="Sécurité", titre="Une task force anti-stups implantée sur l'île",
         court="Le programme prévoit des « task forces dédiées en outre-mer » : nous demandons qu'une soit basée à Saint-Martin.",
         constat=f"Le Sénat décrit une frontière ouverte avec Sint Maarten, au cadre juridique lacunaire, avec des enjeux de sécurité. {s('senat', 'Sénat, 2026')}",
         programme=f"Contre le narcotrafic : « cellules locales anti-stups sous autorité du préfet », « coopération internationale renforcée, task forces dédiées en outre-mer ». {s('securite')}",
         piste="Implanter à Saint-Martin une cellule anti-stups permanente et renforcer la coopération avec la police de Sint Maarten.",
         qui="L'État, avec les Pays-Bas pour la coopération."),
    dict(n="Frontière", titre="Appliquer la fermeté migratoire avec discernement",
         court="Priorité à l'éloignement des étrangers condamnés et au respect des conditions d'accès aux prestations.",
         constat=f"Les déplacements entre les deux parties de l'île ne sont pas contrôlés. {s('senat', 'Sénat, 2026')}",
         programme=f"« Expulser systématiquement les étrangers condamnés pour délits graves » et conditionner les prestations non contributives à « au moins cinq ans » de résidence régulière. {s('immigration')}",
         piste="Concentrer l'action de l'État sur ces deux mesures à Saint-Martin, dans une île où beaucoup de familles ont des origines dans toute la Caraïbe.",
         qui="L'État."),
    dict(n="Santé", titre="Un hôpital gouverné au plus près",
         court="Sans ARS, l'hôpital de Marigot serait piloté au plus près du territoire.",
         constat=f"L'hôpital Louis-Constant-Fleming a connu une grève en juin 2026 et peine à attirer des soignants. {s('hopital', 'Sénat, juin 2026')}",
         programme=f"« Supprimer les ARS, transférer les responsabilités aux préfets et aux élus, redonner aux maires la présidence des conseils d'administration des hôpitaux », et « doubler le nombre d'étudiants en médecine d'ici 2030 ». {s('sante')}",
         piste="Confier la présidence du conseil d'administration de l'hôpital à un élu de la Collectivité et ouvrir des stages d'internes sur l'île.",
         qui="L'État."),
    dict(n="École", titre="Deux collèges pilotes de l'autonomie",
         court="Les deux collèges neufs ouverts en 2026 pourraient tester l'autonomie prévue par le programme.",
         constat=f"La Collectivité ouvre deux collèges en 2026, pour 1 500 places. {s('voeux', 'Vœux 2026 de la Collectivité')}",
         programme=f"Autonomie des chefs d'établissement pour « recruter leurs équipes pédagogiques, appliquer leurs méthodes, gérer leur budget », et 20 % d'augmentation de la rémunération des enseignants. {s('education')}",
         piste="En faire des établissements pilotes de l'autonomie, avec un projet bilingue français-anglais adapté à l'île.",
         qui="L'État (Éducation nationale), avec la Collectivité propriétaire des bâtiments."),
]


def cards():
    out = []
    for i, p in enumerate(PROPS, 1):
        out.append(f"""<a class="prop" href="saint-martin.html#p{i}"><span class="num">{i}</span><span class="tag">{p['n']}</span><h3>{p['titre']}</h3><p>{p['court']}</p><span class="who">Qui décide · {p['qui']}</span></a>""")
    return "\n".join(out)


def fiches():
    out = []
    for i, p in enumerate(PROPS, 1):
        out.append(f"""<article class="fiche" id="p{i}">
  <div><span class="num">{i}</span><span class="tag">{p['n']}</span><h2>{p['titre']}</h2></div>
  <dl>
    <div><dt>Le constat</dt><dd>{p['constat']}</dd></div>
    <div><dt>Ce que dit le programme</dt><dd>{p['programme']}</dd></div>
    <div><dt>Notre piste pour Saint-Martin</dt><dd>{p['piste']}</dd></div>
    <div><dt>Qui décide</dt><dd>{p['qui']}</dd></div>
  </dl>
</article>""")
    return "\n".join(out)


THEMES = [
    ("Sécurité", "securite", [
        "Donner aux préfets les moyens de commander réellement, avec des marges d'action locales sur les effectifs et les équipements.",
        "Ramener les forces de sécurité sur le terrain : 50 % de présence minimum, contre 37 % aujourd'hui.",
        "Permettre aux communes volontaires d'armer leur police municipale.",
        "Cellules locales anti-stups sous l'autorité du préfet et task forces dédiées en outre-mer.",
    ]),
    ("Immigration", "immigration", [
        "Mettre fin à l'automaticité du droit du sol.",
        "Expulser systématiquement les étrangers condamnés pour délits graves et les fichés S étrangers.",
        "Conditionner les prestations sociales non contributives à cinq ans de résidence régulière.",
        "Supprimer l'AME et la remplacer par une aide d'urgence.",
    ]),
    ("Santé", "sante", [
        "Supprimer les ARS et transférer leurs responsabilités aux préfets et aux élus.",
        "Redonner aux maires la présidence des conseils d'administration des hôpitaux.",
        "Mieux rembourser les actes dans les zones sous-dotées.",
        "Doubler le nombre d'étudiants en médecine d'ici 2030.",
    ]),
    ("École", "education", [
        "Abroger la carte scolaire et instaurer progressivement un chèque-éducation.",
        "Donner aux chefs d'établissement la liberté de recruter, de choisir leurs méthodes et de gérer leur budget.",
        "Créer un certificat de fin de primaire conditionnant l'entrée au collège.",
        "Augmenter de 20 % la rémunération des enseignants.",
    ]),
]


def themes(limit=None):
    out = []
    for name, key, items in THEMES:
        li = "".join(f"<li>{x}</li>" for x in items[:limit] if x)
        out.append(f"""<div class="theme"><h3>{name}</h3><ul>{li}</ul><a class="more" href="{SRC[key][0]}" rel="noopener">Page {name.lower()} du programme →</a></div>""")
    return "\n".join(out)


CHIFFRES = [
    ("Population", "32 489", "Habitants sur 53 km², la plus petite région ultrapériphérique française", "rup"),
    ("Emploi", "27 %", "Taux de chômage au recensement de 2023", "iedom"),
    ("Emploi", "−11,8 %", "Baisse de la population active entre 2013 et 2023", "iedom"),
    ("Emploi", "8 119", "Salariés fin 2025, un record (+5,3 % sur un an)", "iedom"),
    ("Tourisme", "2,6 millions", "Visiteurs sur l'ensemble de l'île en 2025 (+15,7 %)", "iedom"),
    ("Tourisme", "95,5 %", "Part de ces visiteurs accueillis côté néerlandais", "iedom"),
    ("Eau", "5,51 €/m³", "Prix de l'eau en 2022, contre 2,11 €/m³ en moyenne nationale en 2021", "rup"),
    ("Eau", "≈ 30 %", "Part de l'eau perdue dans les fuites du réseau en 2022", "rup"),
    ("Logement", "28,3 %", "Ménages propriétaires en 2020, contre 63,6 % en moyenne nationale", "rup"),
    ("Logement", "13,9 %", "Logements vacants en 2018", "rup"),
    ("Précarité", "60 %", "Part de la population éligible à une aide de la CAF (47 % des ménages dans l'Hexagone)", "rup"),
    ("Irma", "95 %", "Bâtiments endommagés par l'ouragan de septembre 2017", "rup"),
]


def table(rows):
    tr = "\n".join(
        f'<tr><td>{a}</td><td class="fig">{b}</td><td>{c}</td><td>{s(k, "IEDOM" if k == "iedom" else "Fiche RUP")}</td></tr>'
        for a, b, c, k in rows
    )
    return f"""<div class="tablebox"><table>
<thead><tr><th>Sujet</th><th>Chiffre</th><th>Ce qu'il mesure</th><th>Source</th></tr></thead>
<tbody>
{tr}
</tbody></table></div>"""


ACT = f"""<div class="act">
  <a class="tile" href="{ADHESION}" rel="noopener"><b>Adhérer</b><span>20 €, 35 € en couple, 10 € pour les moins de 25 ans.</span><i>Site officiel →</i></a>
  <a class="tile" href="https://www.service-public.gouv.fr/particuliers/vosdroits/R16396" rel="noopener"><b>S'inscrire sur les listes</b><span>En ligne, avec une pièce d'identité et un justificatif de domicile.</span><i>service-public.gouv.fr →</i></a>
  <a class="tile" href="https://www.maprocuration.gouv.fr/" rel="noopener"><b>Préparer une procuration</b><span>Pour les Saint-Martinois qui étudient ou travaillent ailleurs.</span><i>maprocuration.gouv.fr →</i></a>
  <a class="tile" href="{NE}/devenir-benevole/" rel="noopener"><b>Devenir bénévole</b><span>Tractage, réunions publiques, porte-à-porte avec les relais du mouvement.</span><i>Site officiel →</i></a>
</div>"""

# ---------------------------------------------------------------------------
PAGES = {}

PAGES["index.html"] = ("Accueil", "Site indépendant de soutien à David Lisnard et Nouvelle Énergie, animé par des habitants de Saint-Martin (Antilles).", f"""
<div class="hero hero-photo">
  <div class="hero-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/David_Lisnard_en_2026.jpg/960px-David_Lisnard_en_2026.jpg" width="960" height="1280" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-text">
      <p class="eyebrow">Présidentielle 2027 · La France, à Saint-Martin</p>
      <h1>Saint-Martin <em>soutient David Lisnard.</em></h1>
      <p class="lead">Nous sommes des habitants de la partie française de l'île. Nous portons ici le projet de Nouvelle Énergie, sur les sujets nationaux comme sur ceux qui comptent pour Saint-Martin : l'eau, l'emploi, le logement et la sécurité à la frontière.</p>
      <div class="cta">
        <a class="btn btn-primary" href="{ADHESION}" rel="noopener">Adhérer à Nouvelle Énergie</a>
        <a class="btn btn-line" href="saint-martin.html">Nos propositions pour l'île</a>
      </div>
      <p class="fine">Adhésion sur le site officiel · 20 €, 10 € pour les moins de 25 ans</p>
    </div>
  </div>
  <p class="credit">Photo de David Lisnard : Grégor Sauvagère, <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" rel="noopener">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:David_Lisnard_en_2026.jpg" rel="noopener">Wikimedia Commons</a></p>
</div>

<div class="quote-band"><div class="wrap">
  <figure class="quote">
    <p class="qlabel">Ce qu'il défend</p>
    <blockquote>Une révolution de la liberté pour une France forte, juste et rayonnante. Notre pays a besoin d’un sursaut.</blockquote>
    <figcaption>David Lisnard · <a href="{NE}/notre-programme/" rel="noopener">programme de Nouvelle Énergie</a></figcaption>
  </figure>
</div></div>

<section id="pourquoi">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Pourquoi David Lisnard</p>
      <h2>Liberté, Ordre, Dignité</h2>
      <p>Le triptyque de Nouvelle Énergie, résumé d'après la {s('programme', 'page programme officielle')}.</p>
    </div>
    <div class="tri">
      <div><h3>Liberté</h3><p>Moins de tutelle fiscale et réglementaire de l'État : libre choix de l'école, capitalisation pour la retraite, libre administration des collectivités.</p></div>
      <div><h3>Ordre</h3><p>« Dans la rue comme dans les comptes » : un État recentré sur l'instruction, la sécurité, la justice, la diplomatie et la santé.</p></div>
      <div><h3>Dignité</h3><p>Le respect de chaque Français comme individu, que la liberté et l'ordre rendent possible.</p></div>
    </div>
  </div>
</section>

<section class="alt island">
  <div class="island-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Panorama_depuis_Bellevue.jpg/1280px-Panorama_depuis_Bellevue.jpg" width="1280" height="853" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Saint-Martin d'abord</p>
      <h2>Huit propositions pour l'île</h2>
      <p>Le programme national n'a pas de volet consacré à l'outre-mer. Ces pistes sont celles de notre collectif : chacune part d'un constat sourcé, s'appuie sur une mesure du programme et dit qui décide. <span class="status">Pistes du collectif, pas des engagements du candidat</span></p>
    </div>
    <div class="props">
{cards()}
    </div>
    <p class="more-link"><a href="saint-martin.html">Lire les fiches détaillées et leurs sources →</a></p>
  </div>
  <p class="credit">Vue de Marigot depuis Bellevue : Thierry Pierrard, <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" rel="noopener">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:Panorama_depuis_Bellevue.jpg" rel="noopener">Wikimedia Commons</a> (floutée et teintée)</p>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">La France qui tient</p>
      <h2>Le régalien et les grands sujets nationaux</h2>
      <p>Mesures reprises des pages thématiques du programme officiel.</p>
    </div>
    <div class="themes">
{themes(3)}
    </div>
    <p class="more-link"><a href="regalien.html">Voir toutes les mesures →</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">L'île en chiffres</p>
      <h2>Chiffres clés</h2>
    </div>
    <div class="keys">
      <div><b>27 %</b><span>de chômage au recensement de 2023</span></div>
      <div><b>5,51 €</b><span>le mètre cube d'eau en 2022, plus de deux fois la moyenne nationale</span></div>
      <div><b>28,3 %</b><span>de ménages propriétaires en 2020, contre 63,6 % en moyenne nationale</span></div>
      <div><b>95,5 %</b><span>des 2,6 millions de visiteurs de l'île accueillis côté néerlandais en 2025</span></div>
    </div>
    <p class="more-link"><a href="chiffres.html">Tous les chiffres et leurs sources →</a></p>
  </div>
</section>

<section class="alt island">
  <div class="island-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Fort_Louis_Marigot_View_%286546074117%29.jpg/1280px-Fort_Louis_Marigot_View_%286546074117%29.jpg" width="1280" height="960" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Agir</p>
      <h2>Quatre gestes utiles avant 2027</h2>
      <p>Ce site ne collecte aucune donnée : chaque lien mène au service officiel concerné.</p>
    </div>
{ACT}
    <p class="more-link"><a href="agir.html">Voir l'agenda des Antilles →</a></p>
  </div>
  <p class="credit">La marina de Marigot vue du fort Louis : Richie Diesterheft, <a href="https://creativecommons.org/licenses/by-sa/2.0/deed.fr" rel="noopener">CC BY-SA 2.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:Fort_Louis_Marigot_View_(6546074117).jpg" rel="noopener">Wikimedia Commons</a> (floutée et teintée)</p>
</section>
""")

PAGES["saint-martin.html"] = ("Saint-Martin d'abord", "Huit pistes du collectif pour Saint-Martin, chacune appuyée sur un constat sourcé et une mesure du programme de Nouvelle Énergie.", hero_page(
    "Saint-Martin d'abord", "Huit propositions pour l'île",
    "Le programme national de Nouvelle Énergie n'a pas de volet consacré à l'outre-mer. Voici les pistes de notre collectif. Ce sont des propositions de soutiens locaux, en discussion, et non des engagements du candidat.") + f"""
<section><div class="wrap">
{fiches()}
<p class="note">Sources consultées le {MAJ}. Les citations du programme sont reprises mot pour mot des pages officielles liées.</p>
</div></section>
""")

PAGES["regalien.html"] = ("La France qui tient", "Les mesures de Nouvelle Énergie sur la sécurité, l'immigration, la santé et l'école, reprises du programme officiel.", hero_page(
    "La France qui tient", "Le régalien et les grands sujets nationaux",
    "Sécurité, immigration, santé, école : les mesures ci-dessous sont reprises des pages thématiques du programme officiel de Nouvelle Énergie. Chaque bloc renvoie à la page d'origine.") + f"""
<section><div class="wrap">
  <div class="themes wide">
{themes()}
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="head">
    <p class="eyebrow">Les trois axes du programme</p>
    <h2>Une refondation en trois temps</h2>
  </div>
  <div class="tri">
    <div><h3>Être maître de notre destin</h3><p>Répondre aux risques de faillite financière, d'affaiblissement démocratique, d'inefficacité de l'État et d'enlisement européen. {s('axe1', 'Lire l\'axe 1')}</p></div>
    <div><h3>Réussir une nouvelle ambition française</h3><p>Une économie plus prospère, une société plus équitable, une cohésion nationale plus forte. {s('axe2', 'Lire l\'axe 2')}</p></div>
    <div><h3>Générer un renouveau civique</h3><p>La révolution de l'école, la décentralisation radicale et la transformation écologique. {s('axe3', 'Lire l\'axe 3')}</p></div>
  </div>
</div></section>
""")

PAGES["chiffres.html"] = ("L'île en chiffres", "Les principaux chiffres économiques et sociaux de Saint-Martin, avec leurs sources publiques.", hero_page(
    "L'île en chiffres", "Ce que vivent les Saint-Martinois",
    "Emploi, eau, logement, tourisme : chaque chiffre renvoie à sa source publique et précise son année de référence.") + f"""
<section><div class="wrap">
{table(CHIFFRES)}
<p class="note">Sources : {s('iedom')} ; {s('rup')}. Vérifié le {MAJ}.</p>
</div></section>
""")

PAGES["agir.html"] = ("Agir", "S'inscrire sur les listes électorales, préparer une procuration, adhérer et suivre l'agenda de Nouvelle Énergie aux Antilles.", hero_page(
    "Agir", "Agir à Saint-Martin",
    "Ce site ne recueille aucune donnée. Pour adhérer, s'inscrire ou participer à un événement, chaque lien mène au service officiel concerné.") + f"""
<section><div class="wrap">
{ACT}
  <div class="agenda" aria-live="polite">
    <b>Agenda Antilles</b>
    <div id="agenda-liste"><p>Chargement de l'agenda officiel…</p></div>
    <p class="note">Événements publiés par Nouvelle Énergie pour Saint-Martin, la Guadeloupe, la Martinique et Saint-Barthélemy, repris automatiquement de l'<a href="{NE}/agenda/" rel="noopener">agenda officiel</a>. Heures affichées à l'heure de Saint-Martin.</p>
  </div>
</div></section>
<section class="alt"><div class="wrap narrow">
  <div class="prose">
    <h2>À Saint-Martin, on vote le samedi</h2>
    <p>Comme dans les autres collectivités des Antilles, le vote a lieu la veille de l'Hexagone. Pensez-y si vous préparez une procuration ou si vous vivez côté Sint Maarten tout en étant inscrit côté français.</p>
    <h2>Les règles que nous suivons</h2>
    <ul>
      <li>Aucune publicité payante, aucun « boost » sur les réseaux.</li>
      <li>Aucune collecte de dons ni de coordonnées sur ce site.</li>
      <li>Aucun nouveau message de campagne à partir de zéro heure la veille du scrutin.</li>
    </ul>
    <p>Ces règles viennent de la <a href="{NE}/charte-de-partage/" rel="noopener">charte de partage</a> de Nouvelle Énergie et du code électoral.</p>
  </div>
</div></section>
""", )

PAGES["english.html"] = ("English", "Independent supporters' site for David Lisnard, run by residents of French Saint-Martin.", hero_page(
    "English", "Saint-Martin supports David Lisnard",
    "We are residents of the French side of the island, supporting David Lisnard and his party Nouvelle Énergie for the 2027 French presidential election.") + f"""
<section><div class="wrap en">
  <div class="prose">
    <h2>Who we are</h2>
    <p>This is an independent supporters' initiative. It is not run, approved or funded by Nouvelle Énergie. The party's official website is <a href="{NE}/" rel="noopener">unenouvelleenergie.fr</a>.</p>
    <p>David Lisnard is the mayor of Cannes. His programme rests on three words: liberty, order and dignity. It calls for a state focused on security, justice, education, diplomacy and health, and for a radical transfer of powers to local governments.</p>
  </div>
  <div class="prose">
    <h2>What we ask for Saint-Martin</h2>
    <ul>
      <li>The right for the Collectivité to adapt national rules to the island.</li>
      <li>Water as a priority: it costs more than twice the national average.</li>
      <li>A priority hiring zone, with 27% unemployment in 2023.</li>
      <li>A permanent anti-drug task force based on the island.</li>
    </ul>
    <p>These are proposals from our local group, not commitments from the candidate. <a href="saint-martin.html" lang="fr">Read them in French</a>.</p>
    <p><b>Make sure you are registered to vote</b> on <a href="https://www.service-public.gouv.fr/particuliers/vosdroits/R16396" rel="noopener">service-public.gouv.fr</a>.</p>
  </div>
</div></section>
""", "en")

PAGES["mentions-legales.html"] = ("Mentions légales", "Mentions légales, hébergement et données personnelles du site.", hero_page(
    "Informations", "Mentions légales", "Éditeur, hébergement et données personnelles.") + f"""
<section><div class="wrap narrow"><div class="prose">
  <h2>Nature du site</h2>
  <p>Initiative indépendante de soutien à David Lisnard et Nouvelle Énergie : non gérée ni validée par le mouvement. Le site est édité à titre bénévole et non professionnel par des habitants de Saint-Martin. Il n'utilise ni le logo ni les visuels officiels de Nouvelle Énergie.</p>
  <h2>Responsable de la publication</h2>
  <p>Jean-Baptiste Monin, Saint-Martin.</p>
  <h2>Hébergement</h2>
  <p>GitHub Pages, service de GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
  <h2>Données personnelles</h2>
  <p>Ce site ne dépose aucun cookie, n'utilise aucun outil de mesure d'audience et ne contient aucun formulaire. Il ne recueille aucune donnée personnelle.</p>
  <p>Trois services tiers sont appelés lors de la consultation : Google Fonts, pour les polices, Wikimedia Commons, pour les photos de l'accueil, et le fichier public de l'agenda de Nouvelle Énergie sur la page Agir. Comme tout serveur web, ils reçoivent l'adresse IP du visiteur. L'hébergeur GitHub peut conserver des journaux techniques de connexion.</p>
  <h2>Sources et droits</h2>
  <p>Les citations et mesures reprises du programme de Nouvelle Énergie renvoient chacune à leur page d'origine. Les chiffres sur Saint-Martin proviennent de l'IEDOM et de la Commission européenne. La photo de David Lisnard en page d'accueil est de Grégor Sauvagère (octobre 2026), publiée sous licence CC BY-SA 4.0 sur Wikimedia Commons. La vue de Marigot depuis Bellevue est de Thierry Pierrard, sous la même licence, floutée et teintée pour servir de fond, de même que la vue de la marina depuis le fort Louis, de Richie Diesterheft (licence CC BY-SA 2.0). Les textes propres au collectif peuvent être repris librement en citant le site.</p>
  <h2>Règles électorales</h2>
  <p>Le site n'engage aucune dépense et ne recourt à aucune publicité payante. Aucun nouveau contenu de propagande n'y est publié à partir de zéro heure la veille d'un scrutin.</p>
</div></div></section>
""")

# 404
PAGES["404.html"] = ("Page introuvable", "Cette page n'existe pas.", hero_page(
    "Erreur 404", "Cette page n'existe pas", "Le lien est peut-être ancien.") + """
<section><div class="wrap"><p><a href="index.html">Revenir à l'accueil</a></p></div></section>
""")


def main():
    for fname, (title, desc, body, *rest) in PAGES.items():
        lang = rest[0] if rest else "fr"
        scripts = f'<script src="assets/agenda.js?v={JS_V}" defer></script>' if fname == "agir.html" else ""
        (ROOT / fname).write_text(page(fname, title, desc, body, lang, scripts), encoding="utf-8")
        print("écrit", fname)


if __name__ == "__main__":
    main()
