---
name: Understand Anything
url: https://github.com/Egonex-AI/Understand-Anything
repo: https://github.com/Egonex-AI/Understand-Anything
tags: [claude-code, codebase-mapping, knowledge-graph, architecture, onboarding]
radar: assess
pricing: open-source
added: 2026-11-01
updated: null
pitch: "Plugin Claude Code (et 16 autres plateformes) qui construit un graphe de connaissance d'un codebase ou d'un wiki, avec dashboard, visites guidées et vue par domaine métier."
alternatives: [floorplan, graphify, archify]
seen_in: []
---

## Ce que c'est

Approche hybride : Tree-sitter extrait la structure de façon déterministe (imports, définitions, appels), un pipeline de cinq agents LLM ajoute résumés, tags, couches (API, service, data, UI) et visites guidées. Le graphe est stocké en JSON dans `.ua/`, versionnable, avec mises à jour incrémentales et un viewer en lecture seule sans appel LLM.

Commandes au-delà de la carte : chat sur le graphe, analyse d'impact d'un diff, onboarding, vue domaine (code rattaché aux domaines, flux et étapes métier), et analyse de wikis au format LLM wiki de Karpathy.

## Pourquoi ça m'intéresse

À valider : la vue domaine colle à une lecture d'architecture par domaines métier, et l'analyse d'impact d'un diff servirait en revue de code sur un brownfield. Le graphe commité dans le repo pourrait aussi servir de contexte durable pour les agents de code.

## À vérifier avant d'essayer

- Langages couverts : le README ne liste pas les grammaires Tree-sitter utilisées. Quid d'Apex, PHP ou C# ?
- Coût du premier `/understand` sur un gros repo, explicitement signalé comme élevé ; qualité avec un modèle local (Ollama).
- Qualité de la vue domaine : déduction pertinente ou découpage technique rebaptisé ?
- Taille du graphe commité (git-lfs recommandé au-delà de 10 Mo) et bruit dans les PR.
- Gouvernance : porté par une entreprise (Egonex / Infinite Universe), modèle économique non affiché.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
