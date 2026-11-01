---
name: Floorplan
url: https://github.com/haydenschmitty/floorplan
repo: https://github.com/haydenschmitty/floorplan
tags: [claude-code, codebase-mapping, architecture, security]
radar: assess
pricing: open-source
added: 2026-11-01
updated: null
pitch: "Plugin Claude Code et Codex qui génère une carte interactive d'un codebase, avec health check sécurité et suivi des changements de l'agent."
alternatives: [archify, understand-anything]
seen_in: []
---

## Ce que c'est

Un plugin (Claude Code et Codex) qui scanne un ou plusieurs repos, fait nommer et décrire chaque partie, fichier et endpoint par l'agent, puis ouvre une carte HTML locale zoomable. Les scripts Node font le travail mécanique (imports, routes, appels front vers back, y compris entre repos), le modèle fait le nommage en langage clair.

En plus de la carte : un health check des erreurs typiques des apps générées par IA (secrets dans le code, tables Supabase ou règles Firebase ouvertes, webhooks Stripe non vérifiés, endpoints sans authentification), une vue « Recent work » des cartes touchées par le dernier passage de l'agent, une barre de questions sur la carte, et un mode blueprint qui dessine la carte cible à partir d'un PRD. Mises à jour incrémentales, tout tourne en local, rien n'est commité.

## Pourquoi ça m'intéresse

À valider : obtenir en quelques minutes une carte d'un brownfield multi-repos pour l'onboarding ou un audit de premier niveau, et visualiser ce qu'un agent de code vient de modifier. Le mode blueprint depuis un PRD pourrait aussi servir de support de revue d'architecture avant développement.

## À vérifier avant d'essayer

- Couverture des langages : TS/JS, Python, Go, Rust, Java, Kotlin, Scala annoncés ; ni PHP, ni C#, ni Apex dans la liste. Que donne le support « plus léger » sur ces stacks ?
- Maturité : première version le 2026-10-27, une quinzaine de releases en une semaine, un seul auteur. Stabilité et pérennité à surveiller.
- Coût en tokens d'une première carte sur un gros repo (chaque fichier et endpoint est décrit).
- Public visé : des builders qui ne lisent pas le code. La vue développeur suffit-elle pour un usage d'architecte ?
- Modèle économique : une offre « Floorplan Cloud » est annoncée (liste d'attente). Risque de bascule de fonctionnalités vers une version payante.
- Fiabilité du health check : l'auteur le présente comme une vérification, pas un audit.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
