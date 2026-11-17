---
name: Modern Web Guidance
url: https://developer.chrome.com/docs/modern-web-guidance
repo: https://github.com/GoogleChrome/modern-web-guidance-src
tags: [claude-code, context-engineering, agents, web-platform]
radar: assess
pricing: open-source
added: 2026-11-17
updated: null
pitch: "CLI et skills qui fournissent à l'agent de codage des guides web à jour (Baseline) et un scanner de patterns legacy, installables en plugin Claude Code."
alternatives: []
seen_in: [modern-web-guidance]
---

## Ce que c'est

Une CLI (`npx modern-web-guidance`) avec trois commandes : `search`, `retrieve` et `legacy-scan`. Elle renvoie dans le contexte de l'agent des guides courts et des listes de vérification issues de la plateforme web et des données Baseline.

Licence Apache-2.0, maintenu par Chrome, Edge, Firefox et MDN. Plugin disponible pour Claude Code, Copilot CLI et Antigravity.

## Pourquoi ça m'intéresse

Cadrer un agent qui modernise du code front legacy (modales, formulaires, CSS, sécurité des scripts tiers) sur un parc de sites, avec un scan qui produit la liste des écarts avant toute modification.

## À vérifier avant d'essayer

- Couverture de `legacy-scan` : le workflow indique lui-même qu'il ne couvre qu'une partie des guides.
- Taux de faux positifs sur un vrai code (les règles `keepWhen` / `dropWhen` sont appliquées par l'agent, pas par l'outil).
- Biais Chrome malgré la gouvernance multi-navigateurs : vérifier les cibles Baseline retenues.
- Coût en tokens des guides récupérés sur un gros repo.
- Pas de `--fix` : prévoir le temps de revue des refactorings.

## Retour d'essai

Pas encore essayé.
