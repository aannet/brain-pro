---
title: "Building effective agents"
url: https://www.anthropic.com/engineering/building-effective-agents
type: blog
authors: [Erik Schluntz, Barry Zhang]
published: 2024-12-19
added: 2026-11-01
tags: [agents, workflows, orchestration, tool-design]
status: read
rating: 5
tldr: "Commencer par l'appel LLM le plus simple, monter vers des workflows composables, et ne passer à un agent autonome que si la tâche l'exige."
related: [how-claude-code-works-in-large-codebases]
---

## En bref

Anthropic tire les leçons de ses déploiements clients : les systèmes qui marchent reposent sur des patterns simples et composables, pas sur des frameworks lourds. L'article distingue les workflows, où le code orchestre des appels LLM selon un chemin prédéfini, des agents, où le modèle pilote lui-même son processus et ses outils. La complexité ne s'ajoute que si elle améliore un résultat mesuré.

## Points clés

- Brique de base : un LLM augmenté (retrieval, outils, mémoire).
- Cinq workflows : prompt chaining (étapes séquentielles avec contrôles), routing (classifier puis aiguiller), parallélisation (sectioning ou vote), orchestrator-workers (un LLM découpe et délègue dynamiquement), evaluator-optimizer (boucle génération/critique).
- Un agent est un LLM qui utilise des outils en boucle à partir du feedback de l'environnement. Pertinent quand le nombre d'étapes est imprévisible ; le prix est la latence, le coût et les erreurs qui se cumulent.
- Les frameworks aident à démarrer mais masquent prompts et réponses ; il vaut mieux comprendre le code sous-jacent.
- Investir dans l'interface agent-outil (ACI) autant que dans une interface humaine : documentation des outils, formats proches de ce que le modèle voit naturellement, paramètres qui empêchent les erreurs.

## À ne pas faire

- Ajouter des couches agentiques sans mesure qui le justifie → latence et coût en hausse sans gain prouvé.
- Adopter un framework sans comprendre le code qu'il génère → prompts et réponses masqués, débogage difficile.
- Lâcher un agent autonome sans environnement de test ni garde-fous → les erreurs s'enchaînent sur plusieurs étapes.

## Ce que j'en retiens

La grille workflow vs agent sert d'abord à justifier le choix le plus simple. Dans un brownfield, la plupart des cas d'usage tiennent dans du chaining ou du routing, avec des points de contrôle déterministes ; l'agent autonome se réserve aux tâches ouvertes avec un environnement de test (le code, typiquement).

## Pour aller plus loin

- Cookbook d'Anthropic avec les implémentations des patterns
