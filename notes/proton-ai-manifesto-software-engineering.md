---
title: "Manifeste de Proton pour l'IA en ingénierie logicielle"
url: https://proton.me/fr/blog/ai-manifesto
type: blog
authors: [Bart Butler]
published: 2026-11-03
added: 2026-11-17
tags: [sdlc, adoption, agents, governance]
status: read
rating: null
tldr: "Le CTO de Proton juge que l'entreprise est restée à « utiliser les LLM pour accélérer l'existant » et qu'il faut repenser tout le cycle de vie, l'ingénieur devenant celui qui encadre et améliore les agents."
related: [the-ai-native-sdlc-playbook, two-years-of-ai-in-software-development, what-makes-a-good-software-factory]
tools: []
---

## En bref

Note interne rendue publique par le CTO de Proton, publiée avec une introduction sur les licenciements dans la tech. Thèse : le génie logiciel a changé de façon irréversible, et Proton prend du retard, ce qu'il qualifie de menace existentielle pour la mission de l'entreprise. Le diagnostic : tout le monde utilise déjà des LLM, mais la productivité n'a pas bondi, parce que l'entreprise est restée à une « phase 1 » (accélérer des tâches dans des workflows inchangés) au lieu de passer à une « phase 2 » qui refond les processus. Le texte dit lui-même qu'il n'est pas un document d'ingénierie : rien sur la sécurité, la fiabilité ou l'infrastructure.

## Points clés

- Le métier a changé : l'ingénieur n'écrit plus le code, il aide le LLM à mieux et plus vite l'écrire. Chaque ingénieur devient chef d'équipe, ses collaborateurs directs étant les modèles et les agents. Un binôme permanent avec l'IA n'est pas une équipe : elle doit travailler en autonomie continue, avec de moins en moins de supervision.
- Améliorer la façon dont l'agent travaille est une responsabilité collective : fichiers de contexte au niveau du dépôt, compétences et prompts partagés, analyse et correction déclenchées par les échecs répétés.
- Trois causes du retard : culture et mentalité d'ingénierie, enfermement en phase 1, problème d'action collective (optimiser un process pour toute une équipe demande des moyens que l'entreprise n'a pas encore investis).
- Supprimer un goulot en fait apparaître un autre : vitesse de l'intégration continue, conception, validation, spécifications, revue de code. L'auteur assume que la majeure partie de la revue de code humaine doit prendre fin.
- L'expertise ne meurt pas : le LLM est rapide, l'humain apporte jugement, expérience et responsabilité. Les bonnes pratiques (architecture, documentation, tests) restent, mais leurs seuils bougent avec les coûts : des tests peu chers déplacent la frontière du « trop de tests », surtout en bout en bout.
- Engagements : l'ingénieur est responsable de la manière dont le travail est fait, pas seulement de sa livraison, automatise au maximum, partage ses améliorations et remonte celles qu'il ne peut pas porter. L'entreprise organise et finance la bascule en phase 2.
- Conclusion de l'auteur : « La "programmation" est morte », l'ingénierie non. L'expérimentation continue, mais le moment d'agir est venu.

## À ne pas faire

- Utiliser les LLM seulement pour accélérer les tâches dans les workflows existants → on reste en phase 1, sans gain structurel de productivité.
- Optimiser une étape sans examiner les processus de façon holistique → le goulot se déplace (CI, conception, validation, revue) au lieu de disparaître.
- Ne pas investir dans les outils qui identifient les goulots → l'organisation ne sait pas où elle perd du temps, et la transformation d'ensemble ne démarre pas.
- Mener des campagnes IA superficielles et cosmétiques, faites pour paraître innovantes → de l'agitation sans effet sur le fond, y compris chez les concurrents.

## Ce que j'en retiens

C'est un cadrage d'adoption, pas une méthode : le diagnostic phase 1 / phase 2 est net, mais le texte ne donne ni mesure, ni critère pour savoir qu'on est passé en phase 2. Les engagements d'ingénieurs rejoignent l'idée d'un harness qu'on améliore en continu. La position sur la fin de la revue humaine est la plus discutable : elle n'est tenable que si des garde-fous déterministes et des évaluations la remplacent, et l'auteur renvoie ces sujets hors du périmètre de la note.

## Pour aller plus loin

- PDF du manifeste, lié depuis l'article.
- the-ai-native-sdlc-playbook (fiche) : version outillée du même constat, avec boucle d'artefacts, hooks et portes humaines.
