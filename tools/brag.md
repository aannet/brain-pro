---
name: brag
url: https://github.com/latent-spaces/brag
repo: https://github.com/latent-spaces/brag
tags: [claude-code, agents, skills, video]
radar: assess
pricing: open-source
added: 2026-11-22
updated: null
pitch: "Skill d'agent MIT qui transforme le projet qu'on vient de coder en courte vidéo de lancement (musique, animations, texte de partage), rendue via Hyperframes."
alternatives: []
seen_in: []
---

## Ce que c'est

Skill `/brag` pour agents compatibles Agent Skills (Claude Code, Codex, opencode…), lancée depuis un répertoire de projet. Elle produit dans `brag-output/` un plan, un brief de composition, un texte de partage et un `brag.mp4`, avec options `--tone` et `--voice` (narration Kokoro). Une variante `/brag-slim` sans Hyperframes est prévue pour Opus 5.5. Un service web séparé, letsbrag.app, génère une vidéo de 20 secondes à partir d'un lien de site.

## Pourquoi ça m'intéresse

Proposition : tester sur un projet perso en page unique (démo GitHub Pages) pour obtenir un clip de présentation sans montage manuel. C'est aussi un exemple concret de skill qui pilote un moteur de rendu externe en ligne de commande.

## À vérifier avant d'essayer

- Licence : code MIT, mais la musique est sous CC BY 4.0 (attribution à reprendre si la vidéo est publiée) et les effets sonores viennent de Kenney.
- Dépendances : Node.js 22+, FFmpeg dans le `PATH`, Hyperframes CLI (`npx hyperframes doctor`), Kokoro pour la voix. Le coût éventuel d'Hyperframes n'est pas précisé par le README.
- letsbrag.app : annoncé sans abonnement, mais aucun tarif ni limite d'usage n'est indiqué. Ne pas y envoyer de projet non public.
- Maturité : environ 21k étoiles et version 0.4.0, mais seulement 58 commits. Date du dernier commit non vérifiée.
- Comportement sur Opus 5.5 : bascule automatique sur `/brag-slim`, `--full` pour garder le workflow Hyperframes. Comparer le rendu des deux modes.
- Le README présente un faux lancement Série A comme exemple de ton : vérifier que le rendu reste sobre pour un usage pro.

## Retour d'essai

_À compléter après un essai réel._
