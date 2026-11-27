# Les amis de David Lisnard à Saint-Martin

Site statique de soutien indépendant à David Lisnard et Nouvelle Énergie, animé par des habitants de Saint-Martin (Antilles).

> Initiative indépendante de soutien à David Lisnard et Nouvelle Énergie : non gérée ni validée par le mouvement.

Adresse : https://davidlisnard978.fr/ (domaine Route 53 ; ancienne adresse : https://black0wi.github.io/amis-lisnard-saint-martin/)

## Règles suivies

Le site applique la [charte de partage et de création](https://www.unenouvelleenergie.fr/charte-de-partage/) de Nouvelle Énergie (version du 23 novembre 2026) :

- bandeau « site non officiel » sur toutes les pages ;
- ni logo, ni portrait, ni visuel officiel ; nom et adresse distincts des sites officiels ;
- aucune collecte de données, aucun formulaire, aucun cookie, aucune publicité payante, aucune dépense ;
- chaque citation et chaque mesure du programme renvoient à leur page officielle ; chaque chiffre à sa source ;
- les propositions locales sont présentées comme des pistes du collectif, pas comme des engagements du candidat ;
- aucun nouveau contenu de propagande à partir de zéro heure la veille d'un scrutin.

Couleurs et typographie : relevées sur unenouvelleenergie.fr (Montserrat, marine #1D257A, or sable #B0AD85).

## Modifier le contenu

Les pages HTML sont générées par `outils/build.py`. Modifier le texte dans ce fichier, puis :

```
python3 outils/build.py
```

L'agenda de la page Agir est lu en direct depuis `https://www.unenouvelleenergie.fr/agenda.json?978,971,972,977` (`assets/agenda.js`).

## À faire avant d'annoncer le site

- [x] Responsable de la publication : Jean-Baptiste Monin.
- [ ] Déclarer le site à Nouvelle Énergie via leur [formulaire de signalement](https://adherent.unenouvelleenergie.fr/contact/signaler-contenu).
- [ ] Faire relire les propositions locales par le référent local.
