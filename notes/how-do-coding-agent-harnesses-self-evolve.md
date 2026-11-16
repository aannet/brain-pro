---
title: "How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation"
url: https://arxiv.org/pdf/2610.34938
type: paper
authors: [Christoph Treude, Sebastian Baltes]
published: 2026-10-26
added: 2026-11-16
tags: [claude-code, evals, context-engineering, agents]
status: read
rating: null
tldr: "Un harness d'agent peut s'améliorer après coup, mais chaque modification doit prouver qu'elle réduit la récurrence du problème, sinon elle n'ajoute que du bruit."
related: [how-claude-code-works-in-large-codebases, when-to-fold-subagents-into-main-agent-loop, the-ai-native-sdlc-playbook]
tools: []
---

## En bref

Les auteurs étudient `/retro`, une compétence qui relit une session terminée de Claude Code et propose des modifications du harness : logiciels, configuration, instructions. Leur conclusion : un harness qui s'auto-améliore a besoin de moyens pour vérifier qu'une modification aide, et pour la réviser ou la retirer si elle n'aide pas. L'échantillon reste petit (30 issues SWE-bench Verified, 12 modifications testées, 5 sessions par harness), donc l'étude sert surtout de méthode.

## Points clés

- Sur 125 propositions codées, 101 partent d'un événement observé dans la session, 19 d'une pratique générale, 5 sont jugées faibles. Les vérifications exécutables dominent (38).
- Sur 13 événements de transfert, 7 sont informatifs. Deux modifications suppriment l'action ciblée (SymPy : 5/5 à 0/5, Astropy : 3/5 à 0/5), une la réduit (Astropy : 5/5 à 2/5), quatre ne changent rien.
- Une modification a fait travailler l'agent sur une issue non liée (Sphinx, 0/5 à 4/5 de comparaisons de référence).
- Le taux de réussite diffère au plus d'une session entre les deux harness. Une ligne de CLAUDE.md a fait passer la durée médiane de 88 à 156 secondes, parce qu'elle demandait aussi de lancer la CI.
- Évaluer une modification revient à trois questions : le problème s'est-il reproduit, l'agent a-t-il consulté la modification, ses actions ont-elles changé ? Les auteurs recommandent de réévaluer les modifications conservées et de réviser celles qui vieillissent.

## À ne pas faire

- Recommander une pratique (lint, hook pre-commit, CI) sans événement observé → une règle ajoutée sans preuve de gain. 18 des 43 propositions liées au lint sont dans ce cas.
- Regrouper plusieurs instructions dans une même modification → impossible de savoir laquelle a produit l'effet.
- Un fichier de tests connus qui traite tout échec absent de sa liste comme causé par ses propres modifications → vérifications inutiles ajoutées sur une issue de contrôle.
- Une liste de tests échoués trop liée à un environnement → les échecs rencontrés plus tard ne sont pas couverts.

## Ce que j'en retiens

Proposition, à valider : avant d'ajouter une règle à CLAUDE.md, noter l'événement qui la justifie, puis la tester sur une autre tâche du même dépôt. Une règle qui ne réduit pas la récurrence sort du fichier. Chaque ligne a aussi un coût en durée de session, à surveiller sur les tâches courantes.

## Pour aller plus loin

- Artefact de l'étude : DOI 10.5281/zenodo.23653700 (licence non indiquée dans la source).
- Compétence `/retro` du dépôt mattpocock/skills, commit b0618bc.
