---
title: "How to build a knowledge factory for AI agents"
url: "https://www.langchain.com/blog/knowledge-factory"
type: blog
authors: ["Harrison Chase"]
published: 2026-11-21
added: 2026-11-22
tags: [agents, context-engineering, knowledge-management, skills]
status: read
rating: null
tldr: "Ce qui manque aux agents en entreprise, c'est de la connaissance maintenue, pas du contexte : une factory où les agents signalent les lacunes et un agent curateur met à jour skills et savoir métier en tâche de fond."
related: [how-do-coding-agent-harnesses-self-evolve, what-makes-a-good-software-factory, when-to-fold-subagents-into-main-agent-loop]
tools: [okf]
---

## En bref

Pour Harrison Chase, l'IA en entreprise bute moins sur la qualité du modèle ou la taille du contexte que sur l'absence de bonnes connaissances : comment l'entreprise travaille, ses standards, où vivent les données. Le contexte, c'est ce que l'agent a sous la main pendant une tâche. La connaissance, c'est la compréhension réutilisable qui lui permet de bien la faire, souvent implicite et jamais écrite. La « knowledge factory » est le système qui collecte, organise et maintient cette connaissance pour les agents, comme une software factory le fait pour le code.

## Points clés

- Trois types de connaissances : les skills (comment faire le travail : procédures, scripts, consignes maison), le savoir métier (définitions, politiques, faits sur produits, clients, organisation) et le guidage d'accès aux données (quelles sources, où, comment les interroger).
- Pour les données à jour, ne pas recopier une source de vérité fiable : documenter comment y accéder.
- Deux mécanismes alimentent la factory : un outil de signalement que l'agent appelle quand une information est manquante ou fausse (avec correction suggérée en option), et un agent curateur qui tourne en arrière-plan à cadence fixe.
- Le curateur lit les sources brutes (Notion, Slack), les traces d'agents et les signalements, puis met à jour la base de connaissances.
- Le stockage est le composant le moins critique (skills dans GitHub, fichier Notion, format OKF dans Context Hub, graphe Neo4j). Il suffit que le curateur sache le manipuler.
- Mémoire : les skills sont devenus le standard de la mémoire procédurale, rien de stabilisé pour la mémoire sémantique. Ne pas sur-spécifier le format.
- Exemple de bout en bout (rapport de revenus) : l'agent repère une colonne renommée dans BigQuery, s'adapte et le signale. Le responsable finance corrige la mise en forme. La nuit suivante, le curateur lit signalement et trace, puis met à jour deux skills.
- Méthode de démarrage : un workflow récurrent, observer où les agents échouent, boucler la boucle. Pas de documentation exhaustive préalable.

## À ne pas faire

- Maintenir la connaissance à la main → effort décrit comme herculéen, qui ne tient pas dans la durée.
- Laisser les agents utilisateurs écrire eux-mêmes dans la base → contenu désordonné et contradictoire, chaque agent étant centré sur son propre objectif.
- Dupliquer des données qui ont déjà une source de vérité → copies qui dérivent, au lieu d'un accès documenté.
- Tout documenter avant de lancer les agents → on retarde le démarrage alors que le travail réel révèle les lacunes.
- Figer tôt un format de stockage rigide → verrouillage sur un standard qui n'est pas encore stabilisé.
- Prendre la documentation existante pour complète → elle est souvent lacunaire, voire fausse.

## Ce que j'en retiens

L'idée utile est la séparation des rôles : les agents qui travaillent signalent, un seul agent curateur écrit. Ça règle le problème de la connaissance qui se pollue quand tout le monde a les droits d'écriture. À tester : un curateur nocturne sur un domaine restreint, avec revue humaine des mises à jour de skills au début, puis relâchement progressif. Le lien avec les notes sur l'auto-évolution des harness est direct : le signalement et la trace sont la matière première de l'adaptation rétrospective. L'article ne donne aucun chiffre de résultat, les gains restent à mesurer.

## Pour aller plus loin

- Context engineering for agents (blog LangChain)
- Introduction à Context Hub (blog LangChain) et dépôt GitHub du format OKF
- Documentation des skills deepagents et des planifications d'agents managés
- « From tasks to goals » et « Goal Engineering: How to Design Goals » (blog LangChain, nov. 2026)
