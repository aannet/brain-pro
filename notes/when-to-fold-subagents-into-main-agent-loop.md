---
title: "Building agents: When to fold subagents into your main agent loop"
url: https://claude.com/fr/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
type: blog
authors: [Diane Sarkis]
published: 2026-10-22
added: 2026-11-01
tags: [agents, orchestration, context-engineering, tool-design, evals]
status: read
rating: null
tldr: "En entreprise, une seule boucle agentique qui charge skills et tools à la demande bat souvent l'architecture multi-sous-agents : migrer un sous-agent à la fois, evals à l'appui."
related: [building-effective-agents, how-claude-code-works-in-large-codebases]
tools: [single-agent-loop-kit]
---

## En bref

Les sous-agents restent utiles (vérification, travail parallèle, cloisonnement des permissions), mais les déploiements entreprise en abusent. Routeurs, planificateurs et agents par domaine finissent par recopier l'organigramme et dégrader l'information à chaque passage de relais. La thèse : une seule boucle, un seul contexte, avec divulgation progressive des skills et des tools, gagne souvent sur la qualité, le coût et la latence. La migration se fait par étapes, mesurée par des evals.

## Points clés

- Garder des sous-agents quand c'est mesuré : dégradation réelle due au gonflement du contexte, tâches parallèles à contexte jetable, ou agent unique qui choisit mal ses tools / prompt aux consignes contradictoires.
- Découper par contexte, pas par type de problème : un sous-agent reçoit un travail qui dépend peu du reste et rend un résultat compact.
- Design cible : un modèle, une fenêtre de contexte, une boucle de tools ouverte. Le harness fixe les limites (budget de tours et de coût, gates d'écriture) et exécute en parallèle les lots de tool calls. Le modèle planifie tôt et révise ; planificateur et exécutant ne font qu'un.
- Répartition : la procédure métier et l'ordonnancement vont dans des skills, les limites dures et les lookups en cours de conversation dans des tools, le chargement trivial et toujours pertinent reste dans du code.
- Contexte partagé : un agent qui a vu toutes les étapes relie mieux les faits que des résumés renvoyés par des sous-agents. Anthropic aurait réduit le system prompt de Claude Code de plus de 80 % pour les modèles récents.
- Un client a mesuré une exécution environ deux fois plus rapide en passant d'un harness multi-agent à une boucle unique.
- Migration en quatre temps : (1) evals d'abord, un jeu end-to-end central (10 cas suffisent pour démarrer) plus des evals livrées avec chaque skill ; (2) fusionner les spécialistes fortement couplés ; (3) appeler les sous-agents comme des tools, schéma de réponse commun, l'agent principal garde la conversation ; (4) replier un sous-agent à la fois (prompt → skill, API → tool MCP) et comparer tâche par tâche.
- Exemple : un repli a fait gagner en latence mais cassé un cas (l'agent répondait depuis le lookup de commande sans demander la date de livraison au spécialiste). La casse n'apparaissait qu'une fois sur deux, d'où l'intérêt de lancer chaque tâche d'eval plusieurs fois.
- Contribution multi-équipes : tools MCP pour les actions et données live, regroupés par intention utilisateur ; skills pour la façon de travailler d'une équipe, avec un DRI et des evals ; bases de connaissance servies via des tools de recherche ou des fichiers de référence dans une skill.
- Gouvernance : une petite équipe centrale possède la qualité end-to-end et le system prompt, et valide chaque nouveau tool et eval.
- Principe final : mesurer, changer une chose à la fois, garder ce qui tient. Un sous-agent ne reste sous-agent que si sa version repliée score moins bien.

## À ne pas faire

- Un sous-agent par équipe ou par type de problème → l'architecture copie l'organigramme (Conway) et chaque relais perd de l'information.
- Laisser proliférer les sous-agents → des centaines d'agents redondants, sans propriétaire ni standard.
- Le « Frankenprompt » où chaque équipe ajoute sa phrase → règles contradictoires, pas de voix cohérente.
- Des evals locales par équipe sans propriétaire global → la direction arbitre sur des scores dilués.
- Classifieurs d'intention et pipelines multi-étapes figés → de la structure qui fait ce que le modèle sait désormais faire seul.
- Empiler un orchestrateur multi-agent sur tout → latence ajoutée (environ x2 dans une comparaison).
- Enchaîner les handoffs façon téléphone arabe → la fidélité baisse à chaque passage.
- Faire un handoff complet sans nécessité → coût inutile ; réserver au cas où le sous-agent doit parler à l'utilisateur.
- Du code qui colle de la connaissance dans le prompt → contexte gonflé ; préférer un tool de lookup ou un fichier de référence de skill.
- Trop de définitions de tools dans un même prompt → le choix de tool se dégrade au-delà de 30 à 50.
- Replier des sous-agents sans evals → les régressions se cachent dans un run unique ou dans le score agrégé.
- Garder des consignes écrites pour d'anciens modèles → agent ralenti ou rigide.

## Ce que j'en retiens

Proposition : utiliser la grille « découper par contexte, pas par organigramme » comme critère de revue pour toute factory agentique en brownfield, avant de créer un agent par domaine applicatif. La séquence evals → subagent-as-tool → repli un par un se transpose telle quelle à n'importe quel système multi-agent déjà en place. Le seuil 30-50 tools est un garde-fou concret pour les serveurs MCP d'intégration.

## Pour aller plus loin

- Kit de migration : https://github.com/anthropics/single-agent-loop-kit
- Skills associées citées : `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`, `/skill-creator`, `/skill-doctor`
- [[building-effective-agents]] pour le socle « commencer simple »
