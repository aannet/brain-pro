---
title: "Computer Use Agents in practice: Automating UI testing"
url: https://www.ml6.eu/en/blog/computer-use-agents-in-practice-automating-ui-testing
type: blog
authors: [Violetta Nguyen]
published: 2026-07-22
added: 2026-11-26
tags: [agents, computer-use, ui-testing, playwright, evals]
status: read
rating: null
tldr: "ML6 utilise des agents de computer use pour tester une UI : trois pipelines (découverte de parcours, chasse aux bugs, génération de tests Playwright) qui déplacent l'effort vers la qualité des descriptions d'entrée et la relecture humaine."
related: [what-makes-a-good-software-factory, when-to-fold-subagents-into-main-agent-loop]
tools: []
---

## En bref

Les outils de test UI existent depuis longtemps, le goulot est le temps d'écriture et de maintenance des tests. ML6 a construit une CLI, `cua-uat`, où un agent de computer use (CUA) pilote un navigateur à partir de descriptions en langage naturel. Elle expose trois pipelines : cartographier les parcours d'une app, trouver des bugs depuis des scénarios Gherkin, produire des tests Playwright. Le CUA ne remplace ni la conception de tests ni le jugement QA.

## Points clés

- Un CUA tourne en boucle : capture d'écran, appel d'outil structuré renvoyé par le modèle (clic, frappe, scroll), exécution par le code du développeur, nouvelle capture. Le modèle décide, il n'agit pas.
- Environnement : conteneur Debian avec navigateur, xdotool pour les entrées, ImageMagick pour les captures. Pour le web, passer le DOM plutôt que des captures réduit les tokens et tend à améliorer la fiabilité sur les apps bien structurées.
- Benchmark de modèles (petits échantillons, 10 à 30 tâches) : Claude Sonnet 4.6 le plus précis (70 %, environ 1,44 € par tâche), GPT-5.4 le plus rapide et le moins cher à précision comparable aux Gemini (43 %). ML6 retient GPT-5.4 avec un effort de raisonnement élevé, qui améliore nettement ses résultats.
- User Flow Generator : un agent Browser Use explore l'app en ligne, puis un agent Claude (Agent SDK) lit le code pour ajouter erreurs, droits et composants conditionnels. Déduplication sémantique en fin de run. Plus de 25 minutes et 3 à 7 € par exécution.
- Bug Finder : scénarios Gherkin exécutés sur le site live, GIF avant/après sur échec. Sur une app avec bugs implantés : 27 bugs fonctionnels sur 28 et 6 bugs visuels sur 8.
- Playwright Writer : Codegen enregistre les actions du CUA (brouillon fragile), puis trois agents proposeurs indépendants (OpenAI Agents SDK) réécrivent le test en parallèle, et un agent « compilateur » fusionne et itère jusqu'à ce que le test passe. Raison : un agent seul applique avec confiance une même hypothèse fausse. Sur un projet de production : 14 tests pour 10 fonctionnalités, relus par un développeur avant PR.
- Playwright Planner/Generator/Healer (v1.56) passent par l'arbre d'accessibilité. Les CUA travaillent au niveau pixel et OS, donc mieux adaptés aux interactions « humaines » (upload, UI mal exposée dans l'arbre).
- Latence plancher : chaque action coûte un aller-retour complet, certains runs du Bug Finder atteignent 30 minutes par scénario. Le parallélisme entre scénarios aide, pas la latence par action.

## À ne pas faire

- Décrire les parcours de façon vague → l'agent fait des hypothèses qui s'accumulent dans la boucle, runs plus lents, plus chers, tests moins fiables (une dizaine de minutes passées à resserrer les étapes ont rapporté plus qu'un budget d'étapes plus long).
- Lancer les agents sans état d'authentification préparé → ils démarrent sur la page de login et gaspillent des étapes (ML6 écrit un fichier de credentials réutilisable, monté dans chaque conteneur).
- Brancher le User Flow Generator sur chaque commit → trop lent et coûteux, il vise un run par projet ou par grande zone fonctionnelle.
- Merger un test généré sans relecture → la qualité du test reste un jugement humain, le Playwright Writer déplace l'effort sans le supprimer.

## Ce que j'en retiens

- Proposition : le motif « trois proposeurs indépendants puis un compilateur qui exécute » se réutilise hors test UI, partout où une erreur confiante et cohérente d'un agent unique coûte cher.
- Le benchmark repose sur 10 à 30 tâches par modèle et un astérisque non expliqué sur Gemini-3-Flash : à lire comme un ordre de grandeur, pas comme un classement.
- Le vrai produit est le test Playwright déterministe en CI, pas l'agent pixel. Le CUA sert de scribe coûteux, une fois.
- Cas d'usage probable : couvrir des UI de SaaS ou de plateformes tierces où l'on ne maîtrise pas les sélecteurs, avec le Bug Finder en recette avant release.

## Pour aller plus loin

- Documentation Playwright : Codegen et agents Planner/Generator/Healer (v1.56)
- Browser Use, Claude Agent SDK, OpenAI Agents SDK
