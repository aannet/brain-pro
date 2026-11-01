---
name: Shunt
url: https://github.com/spotify/portal-ai-plugins/tree/main/plugins/shunt
repo: https://github.com/spotify/portal-ai-plugins
tags: [claude-code, context-engineering, token-optimization, model-routing]
radar: assess
pricing: open-source
added: 2026-11-01
updated: null
pitch: "Plugin Claude Code de Spotify qui délègue la lecture de gros fichiers et la génération de boilerplate à un modèle moins cher, via Spotify Portal."
alternatives: []
seen_in: []
---

## Ce que c'est

Un plugin Claude Code (Apache 2.0, v0.2.0) qui sort les tâches gourmandes en I/O du contexte de l'agent principal. Des hooks `PreToolUse` bloquent la lecture complète des fichiers de plus de 350 lignes (`Read`, ou `cat`/`head`/`tail` en Bash) et renvoient vers deux skills : `bulk-reader`, qui pose une question sur un lot de fichiers, et `code-writer`, qui génère du code à partir d'une spec et d'un fichier de référence. Le travail part vers des « modes » AiKA (l'assistant IA de Spotify Portal) qui tournent sur des modèles moins chers. Seule la réponse revient dans le contexte de Claude.

Le design est en trois couches : le hook comme garde-fou dur, un script aux arguments nommés pour que Claude n'assemble pas de pipeline bash, et la skill qui dit quand l'appeler. Le README liste explicitement ce qui n'est pas délégué : débogage, édition, petits fichiers, décisions d'architecture. Benchmarks de l'auteur sur un monorepo Java de 162 000 lignes : 82 à 94 % de tokens économisés en lecture, 90 % en moyenne. Le repo inclut 51 evals sur les hooks et le transport.

## Pourquoi ça m'intéresse

À valider : surtout comme pattern, moins comme outil. Le couple « hook qui bloque + skill qui redirige vers un worker moins cher » se transpose sans Portal (sous-agent Haiku, appel API direct) pour réduire la conso de tokens sur les gros fichiers d'un brownfield. La liste de ce qu'il ne faut pas déléguer et les evals de hooks sont réutilisables telles quelles.

## À vérifier avant d'essayer

- Dépendance forte : le plugin ne marche qu'avec une instance Spotify Portal où AiKA est activé, plus le plugin `portal` et le Portal CLI. Le plugin est open-source, la plateforme ne l'est pas : vérifier le modèle de prix de Portal.
- Effort pour reproduire le pattern sans Portal : remplacer `scripts/lib/aika.sh` par un appel à un autre modèle semble être le point d'entrée unique.
- Qualité des réponses du worker : la skill demande de revérifier numéros de ligne et valeurs exactes avant toute édition. Quel taux d'erreur en pratique ?
- Taille des requêtes : l'entrée passe par la ligne de commande, plafond de 120 Ko par défaut sous Linux. Sur de gros lots, il faut découper.
- `code-writer` n'a pas de hook : son usage dépend du bon déclenchement de la skill.
- Maturité : v0.2.0, Claude Code uniquement pour l'instant.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
