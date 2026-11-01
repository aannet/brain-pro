# Index

Fichier généré par `scripts/build_index.py`, ne pas modifier à la main.

## Fiches de lecture (2)

| Ajout | Fiche | Type | Tags | Statut | TL;DR |
|---|---|---|---|---|---|
| 2026-11-01 | [Building effective agents](notes/building-effective-agents.md) | blog | `agents` `workflows` `orchestration` `tool-design` | read | Commencer par l'appel LLM le plus simple, monter vers des workflows composables, et ne passer à un agent autonome que si la tâche l'exige. |
| 2026-11-01 | [How Claude Code works in large codebases: Best practices and where to start](notes/how-claude-code-works-in-large-codebases.md) | blog | `claude-code` `context-engineering` `agents` `tool-design` `adoption` | read | Sur un gros codebase, le harness (CLAUDE.md, hooks, skills, LSP, sous-agents) pèse plus que le modèle : rendre le code navigable et nommer un responsable avant d'ouvrir l'accès. |

## Outils (5)

Radar : `adopt` utilisé, `trial` essayé, `assess` repéré non testé, `hold` écarté.

| Radar | Outil | Tags | Prix | Pitch |
|---|---|---|---|---|
| Assess | [Archify](tools/archify.md) | `claude-code` `architecture` `diagrams` `codebase-mapping` | open-source | Skill d'agent qui transforme une idée, un plan ou un repo en diagramme interactif dans un fichier HTML autonome, validé avant livraison. |
| Assess | [Floorplan](tools/floorplan.md) | `claude-code` `codebase-mapping` `architecture` `security` | open-source | Plugin Claude Code et Codex qui génère une carte interactive d'un codebase, avec health check sécurité et suivi des changements de l'agent. |
| Assess | [Graphify](tools/graphify.md) | `codebase-mapping` `knowledge-graph` `context-engineering` `claude-code` `mcp` | freemium | CLI et skill qui transforme code, docs, schémas SQL, PDF et médias en graphe de connaissance interrogeable, sans embeddings, exposé aux agents via MCP. |
| Assess | [Shunt](tools/shunt.md) | `claude-code` `context-engineering` `token-optimization` `model-routing` | open-source | Plugin Claude Code de Spotify qui délègue la lecture de gros fichiers et la génération de boilerplate à un modèle moins cher, via Spotify Portal. |
| Assess | [Understand Anything](tools/understand-anything.md) | `claude-code` `codebase-mapping` `knowledge-graph` `architecture` `onboarding` | open-source | Plugin Claude Code (et 16 autres plateformes) qui construit un graphe de connaissance d'un codebase ou d'un wiki, avec dashboard, visites guidées et vue par domaine métier. |
