---
title: "How Claude Code works in large codebases: Best practices and where to start"
url: https://claude.com/fr/resources/articles/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
type: blog
authors: [Anthropic]
published: 2026-05-14
added: 2026-11-01
tags: [claude-code, context-engineering, agents, tool-design, adoption]
status: read
rating: null
tldr: "Sur un gros codebase, le harness (CLAUDE.md, hooks, skills, LSP, sous-agents) pèse plus que le modèle : rendre le code navigable et nommer un responsable avant d'ouvrir l'accès."
related: [building-effective-agents]
---

## En bref

Premier article de la série « Claude Code at scale ». Anthropic synthétise ce qui distingue les déploiements réussis sur des monorepos de plusieurs millions de lignes, du legacy et des organisations de milliers de développeurs. La thèse : la performance dépend davantage de l'outillage autour du modèle et de la préparation du codebase que du modèle lui-même. L'article couvre aussi des langages qu'on croit mal servis (C, C++, C#, Java, PHP).

## Points clés

- Navigation agentique plutôt que RAG : Claude Code parcourt l'arborescence, lit, grep et suit les références en local, sans index à maintenir. Avantage : pas de résultats périmés quand le code bouge vite. Limite : une recherche floue sur un très gros repo peut saturer la fenêtre de contexte, d'où l'intérêt de lui indiquer où chercher.
- Les briques du harness, chacune avec son rôle :
  - CLAUDE.md hiérarchiques : vue d'ensemble à la racine, conventions locales dans les sous-dossiers, chargés automatiquement en remontant l'arborescence.
  - Hooks : contrôles déterministes (lint, format) et boucle d'amélioration (un hook de fin de session propose des mises à jour du CLAUDE.md).
  - Skills : expertise chargée à la demande, éventuellement limitée à un chemin du repo.
  - Plugins : empaquettent skills, hooks et MCP pour diffuser les pratiques via une marketplace interne.
  - LSP : navigation par symbole (définition, références) au lieu de la recherche textuelle.
  - MCP : accès aux outils et données internes.
  - Sous-agents : contexte isolé, par exemple un explorateur en lecture seule qui cartographie un sous-système avant toute modification.
- Rendre le code navigable : lancer Claude dans le sous-dossier de travail plutôt qu'à la racine, limiter tests et lint au périmètre, exclure le code généré et les dépendances tierces via `permissions.deny` dans un `.claude/settings.json` versionné, ajouter une carte du codebase si l'arborescence ne parle pas d'elle-même.
- Entretenir la configuration : une consigne utile à un ancien modèle peut brider le suivant, et un hook de contournement devient inutile quand l'outil intègre la fonction. Revue tous les 3 à 6 mois ou après chaque sortie majeure de modèle.
- Organisation : les déploiements les plus rapides ont construit l'infrastructure avant d'ouvrir l'accès. Il faut un responsable unique (DRI, ou un rôle hybride d'« agent manager »), un jeu restreint de skills validées, la revue de code obligatoire et un groupe de travail transverse ingénierie, sécurité et gouvernance.
- Ordre de construction suggéré : CLAUDE.md, puis hooks, skills, plugins, LSP, et MCP en dernier. Brancher des MCP avant que les bases tiennent figure parmi les erreurs fréquentes.
- Exemples clients sans métriques : un plugin d'accès à une plateforme analytique interne publié avant le déploiement, et LSP généralisé en amont pour fiabiliser la navigation en C/C++.
- Hors périmètre, annoncé pour des articles suivants : les repos à millions de fichiers, les VCS non Git (Perforce) et les contributeurs non ingénieurs.

## Ce que j'en retiens

À valider : dans un SI hétérogène multi-stack, le levier le moins cher reste la lisibilité (CLAUDE.md par domaine métier, exclusions du code généré), bien avant les MCP. L'ordre de construction proposé donne une roadmap d'adoption utilisable telle quelle : harness minimal, DRI nommé, skills validées, puis ouverture progressive. La revue de configuration à chaque nouveau modèle ressemble à de la dette d'outillage, il faut la planifier comme telle.

## Pour aller plus loin

- Suites annoncées de la série « Claude Code at scale » (très grands repos, VCS non Git)
- Article d'Anthropic sur la modernisation de code COBOL avec Claude Code
- [[building-effective-agents]] pour la grille workflow vs agent et la conception d'outils
