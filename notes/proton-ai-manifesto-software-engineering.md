---
title: "Manifeste de Proton pour l'IA en ingénierie logicielle"
url: https://proton.me/fr/blog/ai-manifesto
type: blog
authors: [Bart Butler]
published: 2026-11-03
added: 2026-11-17
tags: [sdlc, adoption, agents, governance]
status: inbox
rating: null
tldr: "Le CTO de Proton juge que l'entreprise est restée à « utiliser les LLM pour accélérer l'existant » et qu'il faut repenser tout le cycle de vie, l'ingénieur devenant celui qui encadre et améliore les agents."
related: [the-ai-native-sdlc-playbook, two-years-of-ai-in-software-development, what-makes-a-good-software-factory]
tools: []
---

## En bref

Note interne rendue publique par le CTO de Proton. Thèse : le génie logiciel a changé de façon irréversible, et Proton est en retard, bloqué à une « phase 1 » (les LLM accélèrent des tâches dans des workflows inchangés) alors qu'il faut une « phase 2 » qui refond les processus. L'auteur y voit une menace existentielle pour la mission de l'entreprise. Le texte précise qu'il ne détaille ni sécurité, ni fiabilité, ni infrastructure.

Fiche écrite à partir d'un résumé structuré de la page, pas du texte intégral (le PDF complet n'était pas accessible) : statut `inbox`.

## Points clés

- Trois causes du retard : la culture d'ingénierie (le métier devient guider les agents, corriger leurs erreurs et améliorer durablement leur façon de travailler : fichiers de contexte, compétences partagées, analyse des échecs répétés), l'enfermement en phase 1, et l'absence d'action collective.
- Supprimer un goulot en révèle un autre (conception, validation, spécifications, revue de code) : il faut optimiser le cycle entier, pas la seule production de code.
- L'entreprise ignore souvent où sont ses goulots, faute d'outils de mesure pour les identifier.
- L'expertise humaine reste centrale (expérience, jugement, responsabilité). Les pratiques d'ingénierie (architecture, documentation, tests) restent valables, mais leurs seuils bougent quand les coûts changent : des tests bon marché déplacent la frontière entre trop et trop peu de tests.
- Position tranchée : la revue de code humaine doit, à terme, largement disparaître.
- Engagements des ingénieurs : être responsables de la manière dont le travail est fait et pas seulement de sa livraison, automatiser au maximum, partager les améliorations, remonter celles qu'ils ne peuvent pas porter seuls. Engagement de l'entreprise : organiser et financer la bascule en phase 2.

## À ne pas faire

- Utiliser les LLM seulement pour accélérer les tâches existantes → on reste en phase 1, sans gain structurel.
- Optimiser une étape sans regarder le processus entier → le goulot se déplace (spécification, validation, revue) au lieu de disparaître.
- Accepter des échecs répétés sans analyse ni correction → le harness n'apprend pas et les mêmes erreurs reviennent.

## Ce que j'en retiens

Le texte est un cadrage d'adoption, pas une méthode : il donne le diagnostic (phase 1 contre phase 2) mais ni mesures, ni critères pour savoir qu'on est passé en phase 2. Les engagements d'ingénieurs rejoignent l'idée d'un harness qu'on améliore en continu. La position sur la fin de la revue humaine est la plus discutable : elle n'a de sens que si des garde-fous déterministes et des évaluations la remplacent, ce que cette note n'aborde pas.

## Pour aller plus loin

- PDF complet du manifeste, lié depuis l'article (à lire pour passer la fiche en `read`).
- the-ai-native-sdlc-playbook (fiche) : version outillée du même constat (boucle d'artefacts, hooks, portes humaines).
