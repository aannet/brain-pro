---
name: retro (mattpocock/skills)
url: https://github.com/mattpocock/skills
repo: https://github.com/mattpocock/skills
tags: [claude-code, context-engineering, evals, agents]
radar: assess
pricing: open-source
added: 2026-11-16
updated: null
pitch: "Skill MIT de Matt Pocock : relit une session terminée et propose, par gravité, des améliorations de l'environnement de l'agent, sans rien modifier seul."
alternatives: []
seen_in: [how-do-coding-agent-harnesses-self-evolve]
---

## Ce que c'est

Skill `/retro` du dépôt mattpocock/skills (licence MIT), à invoquer à la main. Elle relit une session (la courante par défaut, ou une ancienne via les logs) et propose des changements de l'environnement de l'agent : pointeurs de navigation, checks automatiques, règles pour le reviewer, consignes à alléger, outillage, accès à l'information.

## Pourquoi ça m'intéresse

Proposition : la lancer sur une session difficile, puis confronter ses propositions à la grille de l'article. Une modification doit renvoyer à un moment précis de la session et se tester sur une autre tâche avant de rester. C'est aussi le cas pratique le plus proche de ce qu'on veut sur nos harness.

## À vérifier avant d'essayer

- Le chemin a changé depuis la version citée dans l'article (commit b0618bc, `skills/in-progress/retro`) : la skill est désormais dans `skills/engineering/retro`. Vérifier la version installée.
- Elle ne fait que proposer, sans mode simulation. Tester chaque check proposé avant de le laisser bloquer des merges.
- Elle ne voit qu'une session : elle peut surpondérer ce qui s'y est passé et ne réévalue pas les checks qu'elle a fait ajouter. Le nettoyage reste manuel.
- Sa propre documentation relaie le risque de conseils génériques inventés pour remplir ses catégories : écarter toute proposition qu'on ne peut pas rattacher à un moment précis.
- Elle s'appuie sur des conventions d'équipe (`CODING_STANDARDS.md`, reviewer dédié, skill `writing-for-agents`) qui n'existent pas forcément chez nous.
- Elle préfère les checks aux lignes de `CLAUDE.md` : à confronter à notre usage actuel.

## Retour d'essai

_À compléter après un essai réel._
