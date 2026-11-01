---
name: Single Agent Loop Kit
url: https://github.com/anthropics/single-agent-loop-kit
repo: https://github.com/anthropics/single-agent-loop-kit
tags: [agents, orchestration, evals, claude-code]
radar: assess
pricing: open-source
added: 2026-11-01
updated: null
pitch: "Skill Claude Code et scripts Python d'Anthropic pour migrer un système routeur + sous-agents vers une boucle unique, chaque changement étant mesuré sur une eval."
alternatives: []
seen_in: [when-to-fold-subagents-into-main-agent-loop]
---

## Ce que c'est

Kit de référence (Apache-2.0) livré avec l'article sur le repli des sous-agents. Une skill à copier dans `.claude/skills/` enchaîne audit (verdict par sous-agent : replier, fusionner, appeler comme tool, garder), baseline d'eval, fusion, repli un par un et maintenance, avec des points d'arrêt avant chaque run payant.

Scripts fournis : `coupling_map.py` (qui appelle qui, d'après les traces), `compare.py` (complétion, latence, tokens, coût entre deux runs), `chain_coverage.py`, `estimate.py`. Une boucle de référence minimale (`reference_loop/loop.py`) et une démo support-desk (routeur + 6 sous-agents, versions avant/après) tournent hors ligne sans clé API.

## Pourquoi ça m'intéresse

Proposition : s'en servir comme grille d'audit d'une architecture multi-agent existante, ou comme squelette de boucle unique pour un nouvel agent, plutôt que comme outil de migration clé en main. Le `coupling_map.py` sur des traces réelles donne vite un premier diagnostic.

## À vérifier avant d'essayer

- Maintenance : le README le déclare non maintenu, sans suivi des issues ni des PR. Prévoir un fork.
- Maturité : résultats issus de deux runs, une personne, un modèle. Les étapes merge et upkeep, et le démarrage sans eval, n'ont pas encore tourné sur un vrai modèle.
- Prérequis réels : un moyen d'exécuter son système hors prod sur une requête de test, et quelqu'un capable de définir le résultat attendu.
- Format des traces attendu par `coupling_map.py` : compatible avec ce qu'on exporte déjà ?
- Coût : chaque run d'eval appelle le modèle par tâche, répétition et variante (point de départ suggéré : 10 tâches, 2 à 3 répétitions).
- Dépendance aux commandes `/claude-api` et `/skill-doctor` vers lesquelles les étapes renvoient.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
