---
name: Yogurt
url: https://yogurt.so
repo: https://github.com/FrigadeHQ/yogurt
tags: [meeting-notes, local-ai, privacy, mcp]
radar: assess
pricing: open-source
added: 2026-11-19
updated: null
pitch: "App de bureau open source (MIT) qui enregistre, transcrit et résume des réunions avec des modèles d'IA exécutés en local, sans bot dans l'appel."
alternatives: []
seen_in: []
---

## Ce que c'est

Application de bureau pour Mac, Windows et Linux, éditée par Frigade. Elle capte le micro et le son de l'ordinateur, produit une transcription (whisper.cpp) puis un résumé avec un modèle open-weight exécuté localement (llama.cpp), et accepte des notes personnelles pendant l'appel.

## Pourquoi ça m'intéresse

Réunions où la transcription ne doit pas partir dans un cloud tiers : pas de compte, pas de bot visible, pas de télémétrie selon la page produit. Le serveur MCP local permet aussi de donner accès aux notes à un autre assistant, ce qui touche directement aux contraintes de données.

## À vérifier avant d'essayer

- Plateformes : macOS 14.4+ sur Apple silicon, Windows 10 (2004)+ 64 bits, Ubuntu 22.04+ 64 bits, 8 Go de RAM minimum. Vérifier la compatibilité de la machine cible avant tout.
- Téléchargement initial des modèles : l'app se connecte à internet pour les modèles et la vérification de mises à jour. Vérifier ce qui transite exactement, et quand.
- Serveur MCP local : contrôler à quel assistant il donne accès, et quand l'accès est activé.
- Qualité de la transcription et du résumé sur du français technique et des réunions multilingues (la page annonce 99 langues, sans métriques).
- Maturité : sortie récente (novembre 2026), version 0.3.x au moment de la recherche. Suivre les releases avant une adoption.
- Modèle économique : gratuit et MIT, pas d'offre payante annoncée. Le financement de Frigade et une éventuelle évolution vers du payant sont inconnus.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
