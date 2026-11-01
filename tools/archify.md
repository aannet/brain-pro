---
name: Archify
url: https://github.com/tt-a1i/archify
repo: https://github.com/tt-a1i/archify
tags: [claude-code, architecture, diagrams, codebase-mapping]
radar: assess
pricing: open-source
added: 2026-11-01
updated: null
pitch: "Skill d'agent qui transforme une idée, un plan ou un repo en diagramme interactif dans un fichier HTML autonome, validé avant livraison."
alternatives: [floorplan, understand-anything, graphify]
seen_in: []
---

## Ce que c'est

Un skill (Claude Code, Codex, Cursor, opencode, Claude.ai) : l'agent produit une représentation intermédiaire JSON typée, des validateurs et contrôles de layout l'acceptent ou la rejettent avec des codes de règle, puis un HTML autonome est généré. Dix types de diagrammes (architecture, séquence, data flow, ERD, classes, timeline…), un mode « Architecture Delta » avant/après, des pages explicatives d'une page, exports PNG, PDF et cartes de partage.

Ce n'est ni un éditeur de dessin ni un thème Mermaid : pas d'import Mermaid, pas d'édition WYSIWYG, pas d'hébergement des diagrammes.

## Pourquoi ça m'intéresse

À valider : produire vite des schémas d'architecture propres et cohérents (cible, avant/après d'une migration) pour une revue ou un comité, sans passer par un outil de dessin. Le diff validé entre deux états est le point le plus intéressant pour documenter une trajectoire.

## À vérifier avant d'essayer

- Fidélité en mode repo : le diagramme reflète-t-il le code ou ce que l'agent en déduit ? Quelle part est vérifiée par les validateurs ?
- Maintenabilité : un HTML généré se modifie-t-il autrement qu'en regénérant ? Peut-on versionner l'IR JSON comme source ?
- Popularité très rapide (environ 87k étoiles annoncées, classement trending auto-déclaré) : signal de qualité ou d'effet de mode ?
- Dépendances : appel réseau de vérification de mise à jour (désactivable), sponsors tiers mis en avant dans le README.
- Coût en tokens d'un diagramme d'un gros repo.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
