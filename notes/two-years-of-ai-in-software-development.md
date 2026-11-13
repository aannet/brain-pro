---
title: "Deux ans d'IA en développement logiciel : ce qui a tenu, ce qui a changé"
url: https://www.mirego.com/fr/perspectives/deux-ans-d-ia-en-developpement-logiciel-ce-qui-a-tenu-ce-qui-a-change
type: blog
authors: [Rémi Prévost]
published: 2026-11-04
added: 2026-11-10
tags: [model-routing, token-optimization, sdlc, governance, adoption]
status: read
rating: null
tldr: "Le vrai coût de l'IA en dev est celui d'une tâche (itérations, planification, revue, dette de compréhension), pas du token : router le modèle selon la tâche et nommer un humain responsable de chaque changement livré."
related: [the-ai-native-sdlc-playbook, what-makes-a-good-software-factory]
tools: []
---

## En bref

Mirego relit ses prises de position de 2024 et 2025. L'IA amplifie toujours les équipes sans les remplacer, mais la règle « chaque ligne est soumise par un développeur » ne suffit plus : la question devient qui répond du changement. Le débat se déplace aussi vers l'économie (coût par tâche, choix du modèle) et vers la capacité humaine à comprendre et relire ce que les agents produisent. Pas de certitudes sur l'avenir du métier, une ligne d'expérimentation sur de vrais projets.

## Points clés

- Le coût d'un token compte peu, celui d'une tâche compte. Il inclut les itérations ratées, le temps de planification, le temps de revue et de correction, et la dette de compréhension.
- Exemple de 2025 : environ 6 h de planification ont produit l'équivalent de 15 jours de dev, suivis d'environ 10 jours de corrections à la main. Les tokens étaient négligeables, le coût réel non.
- Illustration : un modèle deux fois moins cher qui demande trois itérations et une heure de revue revient plus cher qu'un modèle haut de gamme qui réussit du premier coup.
- Model routing : modèles de pointe pour planification, architecture et analyse complexe ; modèles rapides et moins chers pour les tâches bien cadrées (implémenter un plan, tests à partir d'exemples, migrations, refactors mécaniques) ; modèles locaux quand la souveraineté des données l'exige.
- Le choix du modèle et du harnais qui l'entoure pèse désormais plus que l'éditeur ou l'agent utilisé.
- Software factories (spécification → pull request, voire déploiement, avec peu d'humain) : efficaces sur le code standardisé, les migrations répétitives, les mises à jour de dépendances, la couverture de tests. Questions ouvertes pour le reste.
- Dette de compréhension : du code qui passe les tests mais que personne ne comprend est un risque à long terme, surtout côté architecture.
- Revue de code : la validation humaine devient le goulot. Relire 2000 lignes générées en quelques minutes n'est pas relire 200 lignes écrites avec intention ; Mirego revoit ses principes de revue.
- Les outils déterministes (analyse statique, scan de vulnérabilités, tests automatisés) restent le socle du SDLC.
- Engagement 2026 : chaque changement livré a un responsable humain. L'humain peut sortir de certaines étapes d'exécution, pas de l'architecture, de la sécurité ni des décisions produit.
- Question de relève ouverte : comment un débutant forge-t-il son jugement s'il écrit et lit de moins en moins de code ?
- Évolution de position : le modèle « chirurgien » reste, mais les agents deviennent des membres de l'équipe autour du chirurgien.

## Ce que j'en retiens

- Proposition : mesurer le coût par tâche (tokens + heures de planification et de revue + reprises) avant de comparer des modèles ou des abonnements, plutôt que le prix au token.
- Proposition : formaliser une grille de routing simple (pointe pour plan et architecture, modèle léger pour exécution cadrée) et la tester sur quelques tâches types.
- Proposition : dans une approche factory, nommer un responsable humain par changement et fixer une taille de diff relisable, sinon la revue devient la contrainte.
- Le texte nomme peu d'anti-patterns explicites ; ce sont des positions d'équipe, pas des retours chiffrés (un seul exemple de 2025).

## Pour aller plus loin

- [The AI-native SDLC playbook](the-ai-native-sdlc-playbook.md) : SDLC par artefacts versionnés, hooks déterministes et humain aux portes de validation.
- Modèles à poids ouverts cités pour le local : GLM (Z.ai), DeepSeek, Qwen, Kimi.
- Modèles « System One » cités : Jev (Typesafe), Clef et Clairic (Cloudflare).
