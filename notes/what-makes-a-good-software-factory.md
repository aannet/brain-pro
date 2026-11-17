---
title: "What makes a good software factory"
url: https://www.robert-glaser.de/what-makes-a-good-software-factory/
type: blog
authors: [Robert Glaser]
published: 2026-11-12
added: 2026-11-13
tags: [sdlc, governance, evals, agents, adoption]
status: read
rating: null
tldr: "Donner des agents de code à cent développeurs ne fait pas une usine : il faut une ligne partagée, une trace par changement, des contrôles indépendants et le produit associé dès la conception."
related: [the-ai-native-sdlc-playbook, two-years-of-ai-in-software-development, when-to-fold-subagents-into-main-agent-loop, proton-ai-manifesto-software-engineering]
tools: []
---

## En bref

Équiper cent développeurs d'agents produit beaucoup plus de code, pas forcément de meilleurs produits ni de meilleures livraisons. Une usine logicielle doit transformer l'intention produit en système de livraison partiellement autonome. L'auteur donne douze propriétés, regroupées en deux blocs : ce qui distingue une usine de cent laptops, et ce qui l'empêche de rester un simple outil d'ingénierie. Sa thèse : celui qui construit l'usine décide de ce qu'elle contrôle, donc le produit et le métier doivent être là dès le départ.

## Points clés

- Une ligne partagée plutôt qu'un AGENTS.md copié partout : un point unique pour corriger tout le monde, avec la raison de chaque règle et la preuve qu'elle a aidé.
- Autonomie intégrée : des contrôles déterministes et agentiques nourrissent l'agent en retour, les humains décident de l'affectation et de la livraison. Le goulot se déplace vers l'intégration (un build de 45 min sur trois machines, environ quatre changements par heure) puis vers la clarté de l'intention.
- Une trace par changement, de la demande produit à la mise en production, avec les raisons de chaque décision, pour corriger une fois la cause d'un défaut récurrent.
- Variantes produit prototypées vite et choisies par ceux qui connaissent le produit ; les variantes écartées sont gardées avec leurs raisons.
- Escalade de l'intention vers le ticket : l'agent cherche d'abord seul, pose les questions restantes dans le ticket, avance sur ce qui n'en dépend pas, signale qui doit trancher.
- Approbation selon la classe de risque, pas selon l'auteur. Tout ce qui est irréversible est à risque maximal ; bascules de fonctionnalités et déploiement progressif réduisent le risque.
- Contrôle dans un contexte neuf, idéalement par des relecteurs adverses (parfois d'un autre fournisseur de modèle) et des cas de test secrets. Le « slop » demande des contrôles produit et métier.
- Une personne possède chaque changement, même déployé automatiquement. Le niveau de contrôle baisse tant que retours arrière et incidents restent bas, et remonte dès qu'ils augmentent.
- Arrêter la ligne, à la manière de Toyota : remonter à la source du défaut, corriger l'usine, prouver que la correction attrape l'erreur initiale. Les problèmes lents passent par des revues périodiques.
- Métrique principale : le délai entre détection d'un échec et correction prouvée. Le coût par résultat validé se suit sans le cibler.
- L'équipe doit pouvoir modifier l'usine sans prestataire. Chaque règle dit si elle compense une faiblesse actuelle des modèles, auquel cas elle disparaît quand les preuves le permettent ; permissions et évaluations restent.

## À ne pas faire

- Un AGENTS.md commun comme seule mutualisation → il n'explique pas pourquoi une règle existe ni si elle a aidé, et chaque équipe dérive de son côté.
- Deviner l'intention quand elle manque → l'agent livre du code qui passe les tests sans répondre au besoin.
- Faire relire le travail par l'agent qui l'a produit → le contrôle partage ses angles morts.
- Approuver ce qu'on ne comprend pas parce que les tests passent → l'équipe perd la compréhension de son propre système, ce que l'auteur assimile à de la triche.
- Compter les pull requests par semaine → l'indicateur ne mesure rien.
- Cibler le coût par résultat validé → les problèmes plus durs coûtent plus cher, on pénalise les bons cas.
- Laisser les seuls ingénieurs concevoir l'usine → le jugement produit et métier n'entre jamais dans les contrôles.

## Ce que j'en retiens

Pour choisir un premier cas d'usage d'usine agentique, la trace par changement et l'escalade d'intention vers le ticket sont probablement les plus faciles à brancher sur un outillage existant. La classe de risque et le propriétaire unique par changement se transposent sans refonte. Le texte reste normatif : aucun retour chiffré d'une usine en production, les douze propriétés valent comme cahier des charges, pas comme preuve.

## Pour aller plus loin

- John Cutler, « TBM 448 » : https://cutlefish.substack.com/p/tbm-448-the-software-factory-as-identity
- Du même auteur, « Approach the software factory as a product team » : https://www.robert-glaser.de/approach-the-software-factory-as-a-product-team/
- Du même auteur, « When everyone has AI and the company still learns nothing » : https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/
- Livre « Loop engineering » : https://elastic-loop.robert-glaser.de/
