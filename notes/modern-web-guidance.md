---
title: "Modern Web Guidance"
url: https://developer.chrome.com/docs/modern-web-guidance
type: doc
authors: [Chrome for Developers]
published: null
added: 2026-11-17
tags: [claude-code, context-engineering, agents, web-platform]
status: read
rating: null
tldr: "Chrome publie des skills pour agents de codage qui embarquent bonnes pratiques de la plateforme web et données Baseline, pour éviter que l'agent produise du code web legacy."
related: [get-your-site-agent-ready]
tools: []
---

## En bref

Page d'entrée de Modern Web Guidance, un ensemble de skills édité par Chrome for Developers. L'idée : injecter dans l'agent de codage l'expertise de la plateforme web, les bonnes pratiques et la compatibilité navigateurs (Baseline), pour qu'il privilégie les standards récents plutôt que les patterns que ses données d'entraînement ont le plus vus.

La page est un hub : installation, exemples de prompts, codelab, liens vers des sous-pages. Elle ne formule pas de principes détaillés. Les sous-pages (get started, modernization workflow, guides, troubleshooting) n'ont pas été lues.

## Points clés

- Installation recommandée par CLI (`npx modern-web-guidance@latest install`). Autres voies : `npx skills`, plugin via marketplace pour Claude Code et Copilot CLI, commande dédiée pour Antigravity.
- Les exemples de prompts sont rangés en quatre familles : construire de nouvelles expériences (accordéon animé, onglets avec highlight via CSS Anchor Positioning, container queries), moderniser le legacy (modales vers `<dialog>`, tooltips vers Popover API), sécurité (passkeys, CSP de départ, audit), performance (préchargement au survol, INP, LCP).
- Un codelab guide l'audit d'une application legacy : cibles Baseline, puis optimisation des Core Web Vitals.
- Couplage annoncé avec Chrome DevTools for agents : audits de performance, arbre d'accessibilité, logs console, corrections automatiques.
- Les sources sont ouvertes (dépôt GoogleChrome/modern-web-guidance-src) et les contributions sont acceptées.

## Ce que j'en retiens

- Même logique que la fiche sur l'agent-readiness, côté producteur de code cette fois : on outille l'agent avec du contexte de référence plutôt que de compter sur ses connaissances figées.
- Intérêt direct pour les chantiers web à grand parc (migration de sites legacy) : le workflow de modernisation et les cibles Baseline sont les deux pièces à lire en priorité.
- À vérifier avant de s'y fier : fraîcheur des skills face à l'évolution de Baseline, et comportement sur du code non-Chrome-centric. Aucun retour d'essai à ce stade.
- Candidat à une fiche outil (`assess`) si on veut l'essayer. Je ne l'ai pas créée.

## Pour aller plus loin

- Sous-pages : get-started, modernization-workflow, guides, troubleshoot
- Codelab « Intro to Modern Web Guidance »
- Dépôt GoogleChrome/modern-web-guidance-src
