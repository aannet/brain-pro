# Index

Fichier généré par `scripts/build_index.py`, ne pas modifier à la main.

## Fiches de lecture (4)

| Ajout | Fiche | Type | Tags | Statut | TL;DR |
|---|---|---|---|---|---|
| 2026-11-02 | [The AI-native SDLC playbook](notes/the-ai-native-sdlc-playbook.md) | blog | `sdlc` `claude-code` `governance` `evals` `security` `adoption` | read | Le code n'est plus le goulot : le SDLC devient une boucle d'artefacts versionnés (intent, spec, plan, diff, revue, incident), les règles critiques passent par des hooks déterministes et l'humain juge aux portes. |
| 2026-11-01 | [Building effective agents](notes/building-effective-agents.md) | blog | `agents` `workflows` `orchestration` `tool-design` | read | Commencer par l'appel LLM le plus simple, monter vers des workflows composables, et ne passer à un agent autonome que si la tâche l'exige. |
| 2026-11-01 | [How Claude Code works in large codebases: Best practices and where to start](notes/how-claude-code-works-in-large-codebases.md) | blog | `claude-code` `context-engineering` `agents` `tool-design` `adoption` | read | Sur un gros codebase, le harness (CLAUDE.md, hooks, skills, LSP, sous-agents) pèse plus que le modèle : rendre le code navigable et nommer un responsable avant d'ouvrir l'accès. |
| 2026-11-01 | [Building agents: When to fold subagents into your main agent loop](notes/when-to-fold-subagents-into-main-agent-loop.md) | blog | `agents` `orchestration` `context-engineering` `tool-design` `evals` | read | En entreprise, une seule boucle agentique qui charge skills et tools à la demande bat souvent l'architecture multi-sous-agents : migrer un sous-agent à la fois, evals à l'appui. |

## Outils (7)

Radar : `adopt` utilisé, `trial` essayé, `assess` repéré non testé, `hold` écarté.

| Radar | Outil | Tags | Prix | Pitch |
|---|---|---|---|---|
| Assess | [Archify](tools/archify.md) | `claude-code` `architecture` `diagrams` `codebase-mapping` | open-source | Skill d'agent qui transforme une idée, un plan ou un repo en diagramme interactif dans un fichier HTML autonome, validé avant livraison. |
| Assess | [Floorplan](tools/floorplan.md) | `claude-code` `codebase-mapping` `architecture` `security` | open-source | Plugin Claude Code et Codex qui génère une carte interactive d'un codebase, avec health check sécurité et suivi des changements de l'agent. |
| Assess | [Graphify](tools/graphify.md) | `codebase-mapping` `knowledge-graph` `context-engineering` `claude-code` `mcp` | freemium | CLI et skill qui transforme code, docs, schémas SQL, PDF et médias en graphe de connaissance interrogeable, sans embeddings, exposé aux agents via MCP. |
| Assess | [OpenShell](tools/openshell.md) | `agents` `security` `sandboxing` `governance` | open-source | Runtime NVIDIA qui exécute des agents IA autonomes dans des sandboxes isolées, avec une politique déclarative sur fichiers, réseau, processus et credentials. |
| Assess | [Shunt](tools/shunt.md) | `claude-code` `context-engineering` `token-optimization` `model-routing` | open-source | Plugin Claude Code de Spotify qui délègue la lecture de gros fichiers et la génération de boilerplate à un modèle moins cher, via Spotify Portal. |
| Assess | [Single Agent Loop Kit](tools/single-agent-loop-kit.md) | `agents` `orchestration` `evals` `claude-code` | open-source | Skill Claude Code et scripts Python d'Anthropic pour migrer un système routeur + sous-agents vers une boucle unique, chaque changement étant mesuré sur une eval. |
| Assess | [Understand Anything](tools/understand-anything.md) | `claude-code` `codebase-mapping` `knowledge-graph` `architecture` `onboarding` | open-source | Plugin Claude Code (et 16 autres plateformes) qui construit un graphe de connaissance d'un codebase ou d'un wiki, avec dashboard, visites guidées et vue par domaine métier. |
