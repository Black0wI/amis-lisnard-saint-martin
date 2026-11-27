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
    "cs-hopital": ("http://www.soualigapost.com/fr/actualite/44322/sant%C3%A9/h%C3%B4pital-le-conseil-de-surveillance-adopte-un-budget-de-52-millions-deuros-pour", "Soualiga Post, conseil de surveillance de l'hôpital (mai 2023)"),
    "police-com": ("https://www.com-saint-martin.fr/thematiques/securite-et-tranquilite-publique/police-territoriale/role-de-la-police-territoriale", "Collectivité de Saint-Martin, rôle de la police territoriale"),
    "ofast": ("https://outremers360.com/bassin-atlantique-appli/lutte-antidrogue-lofast-renforce-sa-presence-et-ses-moyens-aux-antilles", "Outremers360, l'OFAST renforce sa présence aux Antilles (novembre 2025)"),
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


SRC_EN = {
    "iedom": "IEDOM annual report 2025, summarised by Outremers360 (19/10/2026, in French)",
    "rup": "European Commission, Saint-Martin regional fact sheet (outermost regions)",
    "senat": "French Senate, report L25-514 on Saint-Martin and Sint Maarten (April 2026, in French)",
    "cs-hopital": "Soualiga Post, hospital supervisory board (May 2023, in French)",
    "police-com": "Collectivité de Saint-Martin, role of the territorial police (in French)",
    "ofast": "Outremers360, OFAST steps up its presence in the French Caribbean (November 2025, in French)",
    "hopital": "French Senate, topical question 0937G (June 2026, in French)",
    "voeux": "Collectivité de Saint-Martin, President's 2026 New Year address",
    "axe1": "Programme, pillar 1 “Taking charge of our destiny” (in French)",
    "axe2": "Programme, pillar 2 “Achieving a new French ambition” (in French)",
    "axe3": "Programme, pillar 3 “Sparking a civic renewal” (in French)",
    "securite": "Programme, Security page (in French)",
    "immigration": "Programme, Immigration page (in French)",
    "sante": "Programme, Health page (in French)",
    "education": "Programme, Education page (in French)",
    "programme": "Nouvelle Énergie programme (in French)",
}


def s(key, label=None, lang="fr"):
    url, title = SRC[key]
    if lang == "en":
        title = SRC_EN[key]
    return f'<a href="{url}" rel="noopener">{label or title}</a>'


def e(key, label=None):
    """Lien source pour les pages anglaises."""
    return s(key, label, "en")


NAV = [
    ("index.html", "Accueil"),
    ("saint-martin.html", "Saint-Martin d'abord"),
    ("regalien.html", "La France qui tient"),
    ("chiffres.html", "L'île en chiffres"),
    ("agir.html", "Agir"),
]

NAV_EN = [
    ("index.html", "Home"),
    ("saint-martin.html", "Saint-Martin first"),
    ("regalien.html", "A France that stands firm"),
    ("chiffres.html", "The island in figures"),
    ("agir.html", "Get involved"),
]

BANNER_FR = "Initiative indépendante de soutien à David Lisnard et Nouvelle Énergie : non gérée ni validée par le mouvement."

UI = {
    "fr": dict(skip="Aller au contenu", unofficial="Site non officiel", banner=BANNER_FR,
               official="Site officiel de Nouvelle Énergie", navlabel="Navigation principale", join="Adhérer",
               brand_sub="à Saint-Martin", switch=("EN", "en", "Read this page in English"),
               f_h1="Initiative indépendante",
               f_p1=f'{BANNER_FR} Ce site suit la <a href="{NE}/charte-de-partage/" rel="noopener">charte de partage et de création</a> publiée par Nouvelle Énergie (version du 23 novembre 2026).',
               f_p2=f"Aucun cookie, aucune mesure d'audience, aucun formulaire, aucune publicité payante. Mise à jour : {MAJ}.",
               f_h2="Informations", f_legal="Mentions légales et données personnelles", f_prog="Programme officiel"),
    "en": dict(skip="Skip to content", unofficial="Unofficial site",
               banner="Independent initiative supporting David Lisnard and Nouvelle Énergie: not run or approved by the movement.",
               official="Official Nouvelle Énergie website", navlabel="Main navigation", join="Join",
               brand_sub="à Saint-Martin", switch=("FR", "fr", "Lire cette page en français"),
               f_h1="Independent initiative",
               f_p1=f'Independent initiative supporting David Lisnard and Nouvelle Énergie: not run or approved by the movement (<span lang="fr">« {BANNER_FR} »</span>). This site follows the <a href="{NE}/charte-de-partage/" rel="noopener">sharing and creation charter</a> (in French) published by Nouvelle Énergie (version of 23 November 2026).',
               f_p2="No cookies, no audience tracking, no forms, no paid advertising. Last updated: 27 November 2026.",
               f_h2="Information", f_legal="Legal notice and personal data", f_prog="Official programme (in French)"),
}



CSS_V = hashlib.sha1((ROOT / "assets/style.css").read_bytes()).hexdigest()[:8]
JS_V = hashlib.sha1((ROOT / "assets/agenda.js").read_bytes()).hexdigest()[:8]


SITE = "https://davidlisnard978.fr/"


def page(fname, title, description, body, lang="fr", scripts="", fixed_base=None):
    u = UI[lang]
    base = fixed_base or ("../" if lang == "en" else "")
    nav = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == fname else ""}>{label}</a></li>'
        for href, label in (NAV_EN if lang == "en" else NAV)
    )
    sw_label, sw_lang, sw_title = u["switch"]
    sw_href = (f"en/{fname}" if lang == "fr" else f"../{fname}") if not fixed_base else ("en/" if lang == "fr" else "./")
    fr_url, en_url = SITE + ("" if fname == "index.html" else fname), SITE + "en/" + ("" if fname == "index.html" else fname)
    full_title = "Les amis de David Lisnard à Saint-Martin" if fname == "index.html" else f"{title} · Les amis de David Lisnard à Saint-Martin"
    base_tag = f'<base href="{fixed_base}">\n' if fixed_base else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{base_tag}<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta name="theme-color" content="#1D257A">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@500;600;700&display=swap">
<link rel="stylesheet" href="{"" if fixed_base else base}assets/style.css?v={CSS_V}">
</head>
<body>
<a class="skip" href="#contenu">{u["skip"]}</a>
<div class="flag" role="note">
  <div class="wrap">
    <span><strong>{u["unofficial"]}</strong> · {u["banner"]}</span>
    <a href="{NE}/" rel="noopener">{u["official"]}</a>
  </div>
</div>
<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="dot" aria-hidden="true"></span><span class="bt"><b>Les amis de David Lisnard</b><span>{u["brand_sub"]}</span></span></a>
    <nav aria-label="{u["navlabel"]}"><ul>
{nav}
    </ul></nav>
    <a class="lang" href="{sw_href}" hreflang="{sw_lang}" lang="{sw_lang}" title="{sw_title}">{sw_label}</a>
    <a class="pill" href="{ADHESION}" rel="noopener">{u["join"]}</a>
  </div>
</header>
<main id="contenu">
{body}
</main>
<footer>
  <div class="wrap">
    <div>
      <h3>{u["f_h1"]}</h3>
      <p>{u["f_p1"]}</p>
      <p>{u["f_p2"]}</p>
    </div>
    <div>
      <h3>{u["f_h2"]}</h3>
      <p><a href="mentions-legales.html">{u["f_legal"]}</a></p>
      <p><a href="{NE}/notre-programme/" rel="noopener">{u["f_prog"]}</a> · <a href="{ADHESION}" rel="noopener">{u["join"]}</a></p>
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
         constat=f"L'eau potable coûtait 5,51 €/m³ en 2022, contre 2,11 €/m³ en moyenne nationale en 2021. Ces deux prix moyens portent sur l'eau potable seule : l'assainissement, l'abonnement et la tranche haute (au-delà de 30 m³ par trimestre) s'y ajoutent sur la facture. Environ 30 % de l'eau se perd dans les fuites du réseau. {s('rup', 'Fiche RUP')}",
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
    dict(n="Sécurité", titre="Renforcer l'action de l'OFAST sur l'île",
         court="L'Office anti-stupéfiants a déjà un détachement à Saint-Martin : la « task force dédiée » du programme doit venir le renforcer.",
         constat=f"Le Sénat décrit une frontière ouverte avec Sint Maarten, au cadre juridique lacunaire, avec des enjeux de sécurité. {s('senat', 'Sénat, 2026')} L'OFAST dispose d'un détachement à Saint-Martin, renforcé en 2025 avec des policiers spécialisés. {s('ofast', 'Outremers360, 2025')}",
         programme=f"Contre le narcotrafic : « cellules locales anti-stups sous autorité du préfet », « coopération internationale renforcée, task forces dédiées en outre-mer ». {s('securite')}",
         piste="Ne pas créer une structure de plus : renforcer durablement le détachement de l'OFAST déjà présent sur l'île, l'inscrire dans la cellule locale prévue sous l'autorité du préfet, et renforcer la coopération avec la police de Sint Maarten.",
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
         piste=f"Saint-Martin n'a pas de maire : c'est le président de la Collectivité qui exerce ce rôle. Il préside déjà le conseil de surveillance de l'hôpital (c'était le cas en 2023, {s('cs-hopital', 'Soualiga Post')}). L'apport de la mesure serait donc ailleurs : transférer à ce conseil et au préfet les décisions aujourd'hui prises par l'ARS de Guadeloupe, et ouvrir des stages d'internes sur l'île.",
         qui="L'État (loi), puis la Collectivité et le préfet."),
    dict(n="École", titre="Deux collèges pilotes de l'autonomie",
         court="Les deux collèges neufs ouverts en 2026 pourraient tester l'autonomie prévue par le programme.",
         constat=f"La Collectivité ouvre deux collèges en 2026, pour 1 500 places. {s('voeux', 'Vœux 2026 de la Collectivité')}",
         programme=f"Autonomie des chefs d'établissement pour « recruter leurs équipes pédagogiques, appliquer leurs méthodes, gérer leur budget », et 20 % d'augmentation de la rémunération des enseignants. {s('education')}",
         piste="En faire des établissements pilotes de l'autonomie, avec un projet bilingue français-anglais adapté à l'île.",
         qui="L'État (Éducation nationale), avec la Collectivité propriétaire des bâtiments."),
]


def cards(props=None, who="Qui décide"):
    out = []
    for i, p in enumerate(props or PROPS, 1):
        out.append(f"""<a class="prop" href="saint-martin.html#p{i}"><span class="num">{i}</span><span class="tag">{p['n']}</span><h3>{p['titre']}</h3><p>{p['court']}</p><span class="who">{who} · {p['qui']}</span></a>""")
    return "\n".join(out)


def fiches(props=None, labels=("Le constat", "Ce que dit le programme", "Notre piste pour Saint-Martin", "Qui décide")):
    out = []
    for i, p in enumerate(props or PROPS, 1):
        out.append(f"""<article class="fiche" id="p{i}">
  <div><span class="num">{i}</span><span class="tag">{p['n']}</span><h2>{p['titre']}</h2></div>
  <dl>
    <div><dt>{labels[0]}</dt><dd>{p['constat']}</dd></div>
    <div><dt>{labels[1]}</dt><dd>{p['programme']}</dd></div>
    <div><dt>{labels[2]}</dt><dd>{p['piste']}</dd></div>
    <div><dt>{labels[3]}</dt><dd>{p['qui']}</dd></div>
  </dl>
</article>""")
    return "\n".join(out)


THEMES = [
    ("Sécurité", "securite", [
        "Donner aux préfets les moyens de commander réellement, avec des marges d'action locales sur les effectifs et les équipements.",
        "Ramener les forces de sécurité sur le terrain : 50 % de présence minimum, contre 37 % aujourd'hui.",
        ("Permettre aux communes volontaires d'armer leur police municipale.", f"À Saint-Martin, sans commune, ce rôle revient à la police territoriale de la Collectivité. {s('police-com', 'Source')}"),
        ("Cellules locales anti-stups sous l'autorité du préfet et task forces dédiées en outre-mer.", f"À Saint-Martin, il s'agit de renforcer le détachement de l'OFAST déjà présent sur l'île. {s('ofast', 'Source')}"),
    ]),
    ("Immigration", "immigration", [
        "Mettre fin à l'automaticité du droit du sol.",
        "Expulser systématiquement les étrangers condamnés pour délits graves et les fichés S étrangers.",
        "Conditionner les prestations sociales non contributives à cinq ans de résidence régulière.",
        "Supprimer l'AME et la remplacer par une aide d'urgence.",
    ]),
    ("Santé", "sante", [
        "Supprimer les ARS et transférer leurs responsabilités aux préfets et aux élus.",
        ("Redonner aux maires la présidence des conseils d'administration des hôpitaux.", f"À Saint-Martin, sans maire, c'est le président de la Collectivité : il préside déjà le conseil de surveillance de l'hôpital Louis-Constant-Fleming (2023). {s('cs-hopital', 'Source')}"),
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


def themes(limit=None, data=None, more=lambda name: f"Page {name.lower()} du programme →"):
    out = []
    for name, key, items in (data or THEMES):
        li = "".join(f'<li>{x[0]}<span class="here">{x[1]}</span></li>' if isinstance(x, tuple) else f"<li>{x}</li>" for x in items[:limit] if x)
        out.append(f"""<div class="theme"><h3>{name}</h3><ul>{li}</ul><a class="more" href="{SRC[key][0]}" rel="noopener">{more(name)}</a></div>""")
    return "\n".join(out)


CHIFFRES = [
    ("Population", "32 489", "Habitants sur 53 km², la plus petite région ultrapériphérique française", "rup"),
    ("Emploi", "27 %", "Taux de chômage au recensement de 2023", "iedom"),
    ("Emploi", "−11,8 %", "Baisse de la population active entre 2013 et 2023", "iedom"),
    ("Emploi", "8 119", "Salariés fin 2025, un record (+5,3 % sur un an)", "iedom"),
    ("Tourisme", "2,6 millions", "Visiteurs sur l'ensemble de l'île en 2025 (+15,7 %)", "iedom"),
    ("Tourisme", "95,5 %", "Part de ces visiteurs accueillis côté néerlandais", "iedom"),
    ("Eau potable", "5,51 €/m³", "Prix moyen de l'eau potable seule en 2022, hors assainissement et abonnement, contre 2,11 €/m³ en moyenne nationale en 2021", "rup"),
    ("Eau", "≈ 30 %", "Part de l'eau perdue dans les fuites du réseau en 2022", "rup"),
    ("Logement", "28,3 %", "Ménages propriétaires en 2020, contre 63,6 % en moyenne nationale", "rup"),
    ("Logement", "13,9 %", "Logements vacants en 2018", "rup"),
    ("Précarité", "60 %", "Part de la population éligible à une aide de la CAF (47 % des ménages dans l'Hexagone)", "rup"),
    ("Irma", "95 %", "Bâtiments endommagés par l'ouragan de septembre 2017", "rup"),
]


def table(rows, heads=("Sujet", "Chiffre", "Ce qu'il mesure", "Source"), rup="Fiche RUP"):
    tr = "\n".join(
        f'<tr><td>{a}</td><td class="fig">{b}</td><td>{c}</td><td>{s(k, "IEDOM" if k == "iedom" else rup)}</td></tr>'
        for a, b, c, k in rows
    )
    return f"""<div class="tablebox"><table>
<thead><tr>{"".join(f"<th>{h}</th>" for h in heads)}</tr></thead>
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
      <p class="lead">Nous vivons et travaillons à Saint-Martin, de Marigot à Grand-Case, de Quartier-d'Orléans à Sandy Ground. Nous soutenons David Lisnard parce que ses priorités rejoignent celles des familles de l'île : la vie chère, du travail pour nos jeunes, un toit après Irma, la sécurité dans nos quartiers.</p>
      <p class="lead-en" lang="en">We live here, we work here, and we want a France that delivers for Saint-Martin. <a href="en/index.html" hreflang="en">Read it in English →</a></p>
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
      <p>Le programme national n'a pas de volet consacré à l'outre-mer. Nous sommes donc partis de ce que vivent les familles d'ici : le prix de l'eau, le chômage, le logement, la sécurité. Ces pistes sont celles de notre collectif : chacune part d'un constat sourcé, s'appuie sur une mesure du programme et dit qui décide. <span class="status">Pistes du collectif, pas des engagements du candidat</span></p>
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
      <div><b>5,51 €</b><span>le mètre cube d'eau potable en 2022, hors assainissement, plus de deux fois la moyenne nationale</span></div>
      <div><b>28,3 %</b><span>de ménages propriétaires en 2020, contre 63,6 % en moyenne nationale</span></div>
      <div><b>95 %</b><span>des bâtiments de l'île endommagés par l'ouragan Irma en septembre 2017</span></div>
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
      <p>À Saint-Martin, chaque voix compte, et tout commence par l'inscription sur les listes électorales. Ce site ne collecte aucune donnée : chaque lien mène au service officiel concerné.</p>
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
    "Erreur 404", "Cette page n'existe pas", "Le lien est peut-être ancien. <span lang=\"en\">This page does not exist: the link may be out of date.</span>") + """
<section><div class="wrap"><p><a href="index.html">Revenir à l'accueil</a> · <a href="en/index.html" lang="en">Back to the English home page</a></p></div></section>
""")


# ---------------------------------------------------------------------------
# Version anglaise : mêmes pages, mêmes sources. Les citations du programme
# sont notre traduction et renvoient à la page officielle (en français).
# ---------------------------------------------------------------------------
PROPS_EN = [
    dict(n="Local freedom", titre="A right to adapt national rules to the island",
         court="The Territorial Council could ask for a national rule to be adapted, and get a quick answer from the State.",
         constat=f"Saint-Martin already has its own powers, such as taxation and town planning, but many national rules are still designed for mainland France, on a 53 km² island shared with Sint Maarten. {e('rup', 'EU fact sheet')}",
         programme=f"A “massive transfer of powers” to local governments and “autonomy of local regulatory power”, to “adapt public policies to concrete and specific local needs”. {e('axe3')}",
         piste="Give the Collectivité a right to adapt national rules, at the request of the Territorial Council, with a short deadline for the State to reply.",
         qui="The State, through a revision of the organic law on the island's status."),
    dict(n="Water", titre="Drinking water, a top priority",
         court="Drinking water costs more than twice the national average, and nearly a third is lost in the network.",
         constat=f"Drinking water cost €5.51/m³ in 2022, against a national average of €2.11/m³ in 2021. Both are average prices for drinking water alone: sanitation, the fixed charge and the higher band (above 30 m³ per quarter) come on top of the bill. About 30% of the water is lost through leaks in the network. {e('rup', 'EU fact sheet')}",
         programme=f"The national programme has no specific measure on water. This proposal builds on the decentralisation and lighter regulation it stands for. {e('axe3')}",
         piste="Make the network and desalination a top priority, with a public target for cutting losses and a progress report published every year.",
         qui="The Collectivité and its water authority, with support from the State."),
    dict(n="Jobs", titre="Make Saint-Martin a priority hiring zone",
         court="Apply here first the negative employer contributions planned for hiring people on the RSA (minimum income).",
         constat=f"The 2023 census counts 27% unemployment, and the working population fell by 11.8% between 2013 and 2023. Yet salaried employment reached a record 8,119 employees at the end of 2025. {e('iedom', 'IEDOM')}",
         programme=f"“A system of negative employer contributions will be created for hiring people who have been on the RSA for more than 2 years.” {e('axe2')}",
         piste="Roll out this measure first in Saint-Martin, with training for jobs in tourism and construction.",
         qui="The State (social contributions). How it fits with the Collectivité's own taxes remains to be studied."),
    dict(n="Housing", titre="Owning your own home",
         court="Fewer than one household in three owns its home, against nearly two in three nationally.",
         constat=f"28.3% of households owned their home in 2020, against a national average of 63.6%, and 13.9% of homes stood empty in 2018. {e('rup', 'EU fact sheet')}",
         programme=f"The programme would let people “release a capitalised share” of their retirement savings “to buy their main home”, and takes housing policy beyond “social housing alone”. {e('axe2')}",
         piste="Help resident families become homeowners and bring empty homes back onto the market, in line with the Local Housing Programme 2025-2030.",
         qui="The Collectivité (planning, housing) and the State (savings, grants)."),
    dict(n="Security", titre="Step up OFAST's work on the island",
         court="The national anti-drug office already has a unit in Saint-Martin: the programme's “dedicated task forces” should reinforce it.",
         constat=f"The French Senate describes an open border with Sint Maarten, with gaps in the legal framework and real security issues. {e('senat', 'Senate, 2026')} OFAST, the national anti-drug office, has a unit in Saint-Martin, reinforced in 2025 with specialist officers. {e('ofast', 'Outremers360, 2025')}",
         programme=f"Against drug trafficking: “local anti-drug units under the authority of the prefect”, “stronger international cooperation, dedicated task forces in the overseas territories”. {e('securite')}",
         piste="Rather than adding another structure, durably reinforce the OFAST unit already on the island, make it part of the local unit the programme places under the prefect, and step up cooperation with the Sint Maarten police.",
         qui="The State, with the Netherlands for cooperation."),
    dict(n="Border", titre="Firm on immigration, with discernment",
         court="Priority to removing foreign nationals convicted of crimes and to enforcing the conditions for access to benefits.",
         constat=f"Movements between the two sides of the island are not checked. {e('senat', 'Senate, 2026')}",
         programme=f"“Systematically expel foreign nationals convicted of serious offences” and make non-contributory benefits conditional on “at least five years” of legal residence. {e('immigration')}",
         piste="Focus the State's action in Saint-Martin on these two measures, on an island where many families have roots all over the Caribbean.",
         qui="The State."),
    dict(n="Health", titre="A hospital run closer to home",
         court="Without the regional health agency (ARS), the Marigot hospital would be run closer to the island.",
         constat=f"The Louis-Constant-Fleming hospital went on strike in June 2026 and struggles to attract health workers. {e('hopital', 'Senate, June 2026')}",
         programme=f"“Abolish the ARS, transfer responsibilities to prefects and elected officials, give mayors back the chairmanship of hospital boards”, and “double the number of medical students by 2030”. {e('sante')}",
         piste=f"Saint-Martin has no mayor: the President of the Collectivité plays that role, and already chairs the hospital's supervisory board (as was the case in 2023, {e('cs-hopital', 'Soualiga Post')}). The measure's real benefit lies elsewhere: transferring to this board and to the prefect the decisions now taken by the ARS of Guadeloupe, and opening placements for medical interns on the island.",
         qui="The State (by law), then the Collectivité and the prefect."),
    dict(n="Schools", titre="Two pilot schools for autonomy",
         court="The two new secondary schools opening in 2026 could try out the autonomy set out in the programme.",
         constat=f"The Collectivité is opening two secondary schools (collèges) in 2026, with 1,500 places. {e('voeux', 'Collectivité, 2026 address')}",
         programme=f"Autonomy for head teachers to “recruit their teaching teams, apply their methods, manage their budget”, and a 20% pay rise for teachers. {e('education')}",
         piste="Make them pilot schools for autonomy, with a French-English bilingual project suited to the island.",
         qui="The State (national education), with the Collectivité as owner of the buildings."),
]

THEMES_EN = [
    ("Security", "securite", [
        "Give prefects real command, with local room to manoeuvre on staff and equipment.",
        "Put security forces back on the ground: at least 50% of their time, against 37% today.",
        ("Allow willing municipalities to arm their municipal police.", f"In Saint-Martin, which has no municipalities, this role falls to the Collectivité's territorial police. {e('police-com', 'Source')}"),
        ("Local anti-drug units under the prefect's authority and dedicated task forces in the overseas territories.", f"In Saint-Martin, this means reinforcing the OFAST unit already on the island. {e('ofast', 'Source')}"),
    ]),
    ("Immigration", "immigration", [
        "End automatic citizenship by birth on French soil.",
        "Systematically expel foreign nationals convicted of serious offences and foreign nationals on the security watch list (fiche S).",
        "Make non-contributory social benefits conditional on five years of legal residence.",
        "Abolish State Medical Aid (AME) and replace it with emergency aid.",
    ]),
    ("Health", "sante", [
        "Abolish the regional health agencies (ARS) and transfer their responsibilities to prefects and elected officials.",
        ("Give mayors back the chairmanship of hospital boards.", f"In Saint-Martin, which has no mayor, this means the President of the Collectivité, who already chairs the supervisory board of the Louis-Constant-Fleming hospital (2023). {e('cs-hopital', 'Source')}"),
        "Better reimbursement of care in under-served areas.",
        "Double the number of medical students by 2030.",
    ]),
    ("Schools", "education", [
        "Abolish school catchment areas and gradually introduce an education voucher.",
        "Give head teachers the freedom to recruit, choose their methods and manage their budget.",
        "Create an end-of-primary-school certificate required to enter secondary school.",
        "Raise teachers' pay by 20%.",
    ]),
]
MORE_EN = lambda name: f"{name} page of the programme (in French) →"

CHIFFRES_EN = [
    ("Population", "32,489", "Residents on 53 km², the smallest French outermost region", "rup"),
    ("Jobs", "27%", "Unemployment rate in the 2023 census", "iedom"),
    ("Jobs", "−11.8%", "Fall in the working population between 2013 and 2023", "iedom"),
    ("Jobs", "8,119", "Employees at the end of 2025, a record (+5.3% in a year)", "iedom"),
    ("Tourism", "2.6 million", "Visitors to the whole island in 2025 (+15.7%)", "iedom"),
    ("Tourism", "95.5%", "Share of these visitors welcomed on the Dutch side", "iedom"),
    ("Drinking water", "€5.51/m³", "Average price of drinking water alone in 2022, excluding sanitation and fixed charges, against €2.11/m³ nationally in 2021", "rup"),
    ("Water", "≈ 30%", "Share of water lost through leaks in the network in 2022", "rup"),
    ("Housing", "28.3%", "Households owning their home in 2020, against a national average of 63.6%", "rup"),
    ("Housing", "13.9%", "Empty homes in 2018", "rup"),
    ("Hardship", "60%", "Share of the population eligible for family allowance (CAF) support (47% of households in mainland France)", "rup"),
    ("Irma", "95%", "Buildings damaged by the hurricane in September 2017", "rup"),
]

ACT_EN = f"""<div class="act">
  <a class="tile" href="{ADHESION}" rel="noopener"><b>Join</b><span>€20, €35 for couples, €10 for under-25s.</span><i>Official website →</i></a>
  <a class="tile" href="https://www.service-public.gouv.fr/particuliers/vosdroits/R16396" rel="noopener"><b>Register to vote</b><span>Online, with ID and proof of address.</span><i>service-public.gouv.fr →</i></a>
  <a class="tile" href="https://www.maprocuration.gouv.fr/" rel="noopener"><b>Set up a proxy vote</b><span>For people from Saint-Martin studying or working elsewhere.</span><i>maprocuration.gouv.fr →</i></a>
  <a class="tile" href="{NE}/devenir-benevole/" rel="noopener"><b>Volunteer</b><span>Leafleting, public meetings, door-to-door with the movement's local contacts.</span><i>Official website →</i></a>
</div>"""

CARD_WHO_EN = "Who decides"
FICHE_LABELS_EN = ("The facts", "What the programme says (our translation)", "Our proposal for Saint-Martin", "Who decides")

PAGES_EN = {}

PAGES_EN["index.html"] = ("Home", "Independent supporters' site for David Lisnard and Nouvelle Énergie, run by residents of Saint-Martin (French Caribbean).", f"""
<div class="hero hero-photo">
  <div class="hero-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/David_Lisnard_en_2026.jpg/960px-David_Lisnard_en_2026.jpg" width="960" height="1280" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-text">
      <p class="eyebrow">2027 presidential election · France, in Saint-Martin</p>
      <h1>Saint-Martin <em>stands with David Lisnard.</em></h1>
      <p class="lead">We live and work in Saint-Martin, from Marigot to Grand-Case, from Quartier-d'Orléans to Sandy Ground. We support David Lisnard because his priorities meet those of the island's families: the cost of living, work for our young people, a roof over our heads since Irma, safety in our neighbourhoods.</p>
      <p class="lead-en" lang="fr">Nous vivons ici, nous travaillons ici, et nous voulons une France à la hauteur pour Saint-Martin. <a href="../index.html" hreflang="fr">Lire en français →</a></p>
      <div class="cta">
        <a class="btn btn-primary" href="{ADHESION}" rel="noopener">Join Nouvelle Énergie</a>
        <a class="btn btn-line" href="saint-martin.html">Our proposals for the island</a>
      </div>
      <p class="fine">Membership on the official website (in French) · €20, €10 for under-25s</p>
    </div>
  </div>
  <p class="credit">Photo of David Lisnard: Grégor Sauvagère, <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" rel="noopener">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:David_Lisnard_en_2026.jpg" rel="noopener">Wikimedia Commons</a></p>
</div>

<div class="quote-band"><div class="wrap">
  <figure class="quote">
    <p class="qlabel">What he stands for</p>
    <blockquote>A revolution of freedom for a strong, fair and influential France. Our country needs a jolt.</blockquote>
    <figcaption>David Lisnard · <a href="{NE}/notre-programme/" rel="noopener">Nouvelle Énergie programme</a> (our translation)</figcaption>
  </figure>
</div></div>

<section id="pourquoi">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Why David Lisnard</p>
      <h2>Liberty, Order, Dignity</h2>
      <p>Nouvelle Énergie's three founding words, summarised from the {e('programme', 'official programme page')} (in French).</p>
    </div>
    <div class="tri">
      <div><h3>Liberty</h3><p>Less tax and regulatory control by the State: free choice of school, funded pensions, self-government for local authorities.</p></div>
      <div><h3>Order</h3><p>“In the streets as in the public accounts”: a State refocused on education, security, justice, diplomacy and health.</p></div>
      <div><h3>Dignity</h3><p>Respect for every French citizen as an individual, made possible by liberty and order.</p></div>
    </div>
  </div>
</section>

<section class="alt island">
  <div class="island-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Panorama_depuis_Bellevue.jpg/1280px-Panorama_depuis_Bellevue.jpg" width="1280" height="853" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Saint-Martin first</p>
      <h2>Eight proposals for the island</h2>
      <p>The national programme has no chapter on the overseas territories. So we started from what families here live with: the price of water, unemployment, housing, safety. These proposals come from our local group: each starts from a sourced fact, builds on a measure in the programme and says who decides. <span class="status">Proposals from our group, not commitments from the candidate</span></p>
    </div>
    <div class="props">
{cards(PROPS_EN, CARD_WHO_EN)}
    </div>
    <p class="more-link"><a href="saint-martin.html">Read the detailed proposals and their sources →</a></p>
  </div>
  <p class="credit">View of Marigot from Bellevue: Thierry Pierrard, <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" rel="noopener">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:Panorama_depuis_Bellevue.jpg" rel="noopener">Wikimedia Commons</a> (blurred and tinted)</p>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">A France that stands firm</p>
      <h2>Law and order and the big national issues</h2>
      <p>Measures taken from the programme's topic pages, translated from French.</p>
    </div>
    <div class="themes">
{themes(3, THEMES_EN, MORE_EN)}
    </div>
    <p class="more-link"><a href="regalien.html">See all measures →</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">The island in figures</p>
      <h2>Key figures</h2>
    </div>
    <div class="keys">
      <div><b>27%</b><span>unemployment in the 2023 census</span></div>
      <div><b>€5.51</b><span>per cubic metre of drinking water in 2022, excluding sanitation, more than twice the national average</span></div>
      <div><b>28.3%</b><span>of households owned their home in 2020, against 63.6% nationally</span></div>
      <div><b>95%</b><span>of the island's buildings damaged by Hurricane Irma in September 2017</span></div>
    </div>
    <p class="more-link"><a href="chiffres.html">All figures and their sources →</a></p>
  </div>
</section>

<section class="alt island">
  <div class="island-bg" aria-hidden="true"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Fort_Louis_Marigot_View_%286546074117%29.jpg/1280px-Fort_Louis_Marigot_View_%286546074117%29.jpg" width="1280" height="960" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Get involved</p>
      <h2>Four useful steps before 2027</h2>
      <p>In Saint-Martin, every vote counts, and it all starts with registering to vote. This site collects no data: each link takes you to the official service.</p>
    </div>
{ACT_EN}
    <p class="more-link"><a href="agir.html">See the Caribbean events calendar →</a></p>
  </div>
  <p class="credit">Marigot marina seen from Fort Louis: Richie Diesterheft, <a href="https://creativecommons.org/licenses/by-sa/2.0/deed.en" rel="noopener">CC BY-SA 2.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:Fort_Louis_Marigot_View_(6546074117).jpg" rel="noopener">Wikimedia Commons</a> (blurred and tinted)</p>
</section>
""")

PAGES_EN["saint-martin.html"] = ("Saint-Martin first", "Eight proposals from our group for Saint-Martin, each based on a sourced fact and a measure from Nouvelle Énergie's programme.", hero_page(
    "Saint-Martin first", "Eight proposals for the island",
    "Nouvelle Énergie's national programme has no chapter on the overseas territories. Here are our group's proposals. They come from local supporters, are open for discussion, and are not commitments from the candidate.") + f"""
<section><div class="wrap">
{fiches(PROPS_EN, FICHE_LABELS_EN)}
<p class="note">Sources checked on 27 November 2026. Quotes from the programme are our own translation from French; each links to the original official page.</p>
</div></section>
""")

PAGES_EN["regalien.html"] = ("A France that stands firm", "Nouvelle Énergie's measures on security, immigration, health and schools, taken from the official programme.", hero_page(
    "A France that stands firm", "Law and order and the big national issues",
    "Security, immigration, health, schools: the measures below come from the topic pages of Nouvelle Énergie's official programme, translated from French. Each block links to the original page.") + f"""
<section><div class="wrap">
  <div class="themes wide">
{themes(None, THEMES_EN, MORE_EN)}
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="head">
    <p class="eyebrow">The programme's three pillars</p>
    <h2>A rebuild in three stages</h2>
  </div>
  <div class="tri">
    <div><h3>Taking charge of our destiny</h3><p>Respond to the risks of financial bankruptcy, weakening democracy, an inefficient State and a stalled Europe. {e('axe1', 'Read pillar 1 (in French)')}</p></div>
    <div><h3>Achieving a new French ambition</h3><p>A more prosperous economy, a fairer society, stronger national cohesion. {e('axe2', 'Read pillar 2 (in French)')}</p></div>
    <div><h3>Sparking a civic renewal</h3><p>A revolution in schools, radical decentralisation and the ecological transformation. {e('axe3', 'Read pillar 3 (in French)')}</p></div>
  </div>
</div></section>
""")

PAGES_EN["chiffres.html"] = ("The island in figures", "Saint-Martin's main economic and social figures, with their public sources.", hero_page(
    "The island in figures", "What people in Saint-Martin live with",
    "Jobs, water, housing, tourism: each figure links to its public source and gives its reference year.") + f"""
<section><div class="wrap">
{table(CHIFFRES_EN, ("Topic", "Figure", "What it measures", "Source"), "EU fact sheet")}
<p class="note">Sources: {e('iedom')}; {e('rup')}. Checked on 27 November 2026.</p>
</div></section>
""")

PAGES_EN["agir.html"] = ("Get involved", "Register to vote, set up a proxy vote, join and follow Nouvelle Énergie's events in the French Caribbean.", hero_page(
    "Get involved", "Get involved in Saint-Martin",
    "This site collects no data. To join, register or attend an event, each link takes you to the official service.") + f"""
<section><div class="wrap">
{ACT_EN}
  <div class="agenda" aria-live="polite">
    <b>Caribbean calendar</b>
    <div id="agenda-liste"><p>Loading the official calendar…</p></div>
    <p class="note">Events published by Nouvelle Énergie for Saint-Martin, Guadeloupe, Martinique and Saint-Barthélemy, taken automatically from the <a href="{NE}/agenda/" rel="noopener">official calendar</a> (in French). Times shown in Saint-Martin time.</p>
  </div>
</div></section>
<section class="alt"><div class="wrap narrow">
  <div class="prose">
    <h2>In Saint-Martin, we vote on Saturday</h2>
    <p>As in the other French Caribbean territories, voting takes place the day before mainland France. Keep this in mind if you are setting up a proxy vote, or if you live on the Sint Maarten side while being registered on the French side.</p>
    <h2>The rules we follow</h2>
    <ul>
      <li>No paid advertising, no “boosted” posts on social media.</li>
      <li>No donations or contact details collected on this site.</li>
      <li>No new campaign messages from midnight on the eve of the vote.</li>
    </ul>
    <p>These rules come from Nouvelle Énergie's <a href="{NE}/charte-de-partage/" rel="noopener">sharing charter</a> (in French) and the French electoral code.</p>
  </div>
</div></section>
""")

PAGES_EN["mentions-legales.html"] = ("Legal notice", "Legal notice, hosting and personal data.", hero_page(
    "Information", "Legal notice", "Publisher, hosting and personal data. The French version is the reference text.") + f"""
<section><div class="wrap narrow"><div class="prose">
  <h2>About this site</h2>
  <p>Independent initiative supporting David Lisnard and Nouvelle Énergie: not run or approved by the movement. The site is published on a voluntary, non-professional basis by residents of Saint-Martin. It does not use Nouvelle Énergie's official logo or visuals.</p>
  <h2>Publisher</h2>
  <p>Jean-Baptiste Monin, Saint-Martin.</p>
  <h2>Hosting</h2>
  <p>GitHub Pages, a service of GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States.</p>
  <h2>Personal data</h2>
  <p>This site sets no cookies, uses no audience measurement tools and contains no forms. It collects no personal data.</p>
  <p>Three third-party services are called when you visit: Google Fonts for typefaces, Wikimedia Commons for the photos, and Nouvelle Énergie's public calendar file on the Get involved page. Like any web server, they receive the visitor's IP address. GitHub, the host, may keep technical connection logs.</p>
  <h2>Sources and rights</h2>
  <p>Quotes and measures from Nouvelle Énergie's programme each link to their original page; on the English pages they are our own translation. Figures on Saint-Martin come from IEDOM and the European Commission. The photo of David Lisnard on the home page is by Grégor Sauvagère (October 2026), published under a CC BY-SA 4.0 licence on Wikimedia Commons. The view of Marigot from Bellevue is by Thierry Pierrard, under the same licence, and the view of the marina from Fort Louis is by Richie Diesterheft (CC BY-SA 2.0); both are blurred and tinted for use as backgrounds. Texts written by our group may be freely reused with credit to the site.</p>
  <h2>Election rules</h2>
  <p>The site incurs no expenses and uses no paid advertising. No new campaign content is published from midnight on the eve of a vote.</p>
</div></div></section>
""")

REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Les amis de David Lisnard à Saint-Martin</title>
<meta http-equiv="refresh" content="0; url=en/index.html"><link rel="canonical" href="https://davidlisnard978.fr/en/">
</head><body><p><a href="en/index.html">English version</a></p></body></html>
"""


# Pause : en attente de validation par l'équipe de campagne (27/11/2026).
# Pour remettre le site complet en ligne : PAUSE = False, puis python3 outils/build.py
# (le site complet est aussi conservé sur la branche site-complet).
PAUSE = True

PAUSE_BODY = f"""<div class="intro"><div class="wrap narrow">
  <p class="eyebrow">Présidentielle 2027 · Saint-Martin</p>
  <h1>Site en pause</h1>
  <p class="lead">Ce site de soutien est en cours de relecture par l'équipe de campagne de Nouvelle Énergie. Il sera remis en ligne après sa validation.</p>
  <p class="lead" lang="en">This supporters' site is being reviewed by the Nouvelle Énergie campaign team. It will be back online once approved.</p>
  <p><a class="btn btn-primary" href="{NE}/" rel="noopener">Site officiel de Nouvelle Énergie</a></p>
  <p class="fine">Responsable de la publication : Jean-Baptiste Monin, Saint-Martin. Hébergement : GitHub Pages (GitHub, Inc., San Francisco, États-Unis). Aucun cookie, aucune donnée collectée.</p>
</div></div>"""


def pause_page():
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<base href="/">
<title>Les amis de David Lisnard à Saint-Martin</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#1D257A">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@500;600;700&display=swap">
<link rel="stylesheet" href="assets/style.css?v={CSS_V}">
</head>
<body>
<div class="flag" role="note"><div class="wrap"><span><strong>Site non officiel</strong> · {BANNER_FR}</span></div></div>
<header class="site"><div class="wrap"><span class="brand"><span class="dot" aria-hidden="true"></span><span class="bt"><b>Les amis de David Lisnard</b><span>à Saint-Martin</span></span></span></div></header>
<main id="contenu">
{PAUSE_BODY}
</main>
</body>
</html>
"""


def main_pause():
    html = pause_page()
    for d in (ROOT, ROOT / "en"):
        for f in d.glob("*.html"):
            f.unlink()
    (ROOT / "en").mkdir(exist_ok=True)
    for f in (ROOT / "index.html", ROOT / "404.html", ROOT / "en" / "index.html"):
        f.write_text(html, encoding="utf-8")
        print("pause :", f.relative_to(ROOT))


def main():
    if PAUSE:
        return main_pause()
    (ROOT / "en").mkdir(exist_ok=True)
    for lang, pages, outdir in (("fr", PAGES, ROOT), ("en", PAGES_EN, ROOT / "en")):
        for fname, (title, desc, body, *rest) in pages.items():
            base = "../" if lang == "en" else ""
            scripts = f'<script src="{base}assets/agenda.js?v={JS_V}" defer></script>' if fname == "agir.html" else ""
            fixed = "/" if fname == "404.html" else None
            (outdir / fname).write_text(page(fname, title, desc, body, lang, scripts, fixed), encoding="utf-8")
            print("écrit", ("en/" if lang == "en" else "") + fname)
    (ROOT / "english.html").write_text(REDIRECT, encoding="utf-8")
    print("écrit english.html (redirection)")


if __name__ == "__main__":
    main()
