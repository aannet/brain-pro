---
name: Graphify
url: https://github.com/Graphify-Labs/graphify
repo: https://github.com/Graphify-Labs/graphify
tags: [codebase-mapping, knowledge-graph, context-engineering, claude-code, mcp]
radar: assess
pricing: freemium
added: 2026-11-01
updated: null
pitch: "CLI et skill qui transforme code, docs, schémas SQL, PDF et médias en graphe de connaissance interrogeable, sans embeddings, exposé aux agents via MCP."
alternatives: [understand-anything, floorplan, archify]
seen_in: []
---

## Ce que c'est

Le code est parsé localement par Tree-sitter (une quarantaine de langages, sans LLM). Docs, PDF, images et audio/vidéo passent par une passe sémantique (modèle de l'assistant ou backend configuré, dont Azure OpenAI, Bedrock, Ollama). Chaque arête est marquée extraite ou inférée, les communautés sont détectées par l'algorithme de Leiden.

Sorties : `graph.html` navigable, `GRAPH_REPORT.md` (nœuds centraux, communautés, questions suggérées), `graph.json`. Interrogation par CLI (`query`, `path`, `explain`) ou serveur MCP. Graphify Cloud, payant avec essai de 14 jours, ajoute multi-repos, revue de code et connecteurs Sentry et Jira.

## Pourquoi ça m'intéresse

À valider : un contexte structuré pour les agents de code sur un brownfield, moins coûteux en tokens que la lecture de fichiers, et qui mélange code, schémas SQL, configs et documentation. La distinction extrait/inféré est utile pour savoir à quoi se fier.

## À vérifier avant d'essayer

- Benchmarks auto-déclarés (LOCOMO, LongMemEval, ERPNext) : à reproduire sur un repo connu avant d'y croire.
- Frontière open source / Cloud : multi-repos et connecteurs sont dans l'offre payante, prix non publiés.
- Double licence Apache-2.0 et MIT présente dans le repo : laquelle s'applique à quoi ?
- Confidentialité de la passe sémantique : quels contenus partent vers le backend LLM configuré.
- Maturité réelle derrière les chiffres (environ 140k étoiles, plus de 700 issues ouvertes) et stabilité du format `graph.json`.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
