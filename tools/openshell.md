---
name: OpenShell
url: https://github.com/NVIDIA/OpenShell
repo: https://github.com/NVIDIA/OpenShell
tags: [agents, security, sandboxing, governance]
radar: assess
pricing: open-source
added: 2026-11-03
updated: null
pitch: "Runtime NVIDIA qui exécute des agents IA autonomes dans des sandboxes isolées, avec une politique déclarative sur fichiers, réseau, processus et credentials."
alternatives: []
seen_in: []
---

## Ce que c'est

Un runtime open-source (Apache 2.0, v0.1.6) qui fait tourner chaque agent dans une sandbox. L'opérateur déclare dans une policy YAML ce que l'agent peut lire, appeler et exécuter, et OpenShell l'applique au niveau noyau : Landlock pour le système de fichiers, seccomp et identité non privilégiée pour les processus, sortie réseau refusée par défaut sauf destinations approuvées. L'agent ne voit jamais les vrais secrets : il manipule des placeholders, résolus seulement vers les endpoints autorisés par le profil du provider.

Les couches n'ont pas le même cycle de vie. Fichiers et processus sont figés à la création de la sandbox ; réseau et credentials se modifient à chaud (rotation, révocation), sauf une nouvelle variable d'environnement qui impose un nouveau processus.

L'architecture tient en trois briques : une gateway (control plane : sandboxes, policies, accès), un supervisor, et les sandboxes (images, runtimes, support GPU). Les changements de policy passent par un « advisor » et un « prover » : la vérification formelle signale les nouveaux accès risqués (nouvel hôte avec credentials, nouvelle méthode d'API) et les met en attente de revue humaine. Tourne sur Docker, Podman ou virtualisation hôte, en local ou sur Kubernetes via Helm. SDK Python, TypeScript, Go et Rust. Agents cités par la doc : Claude Code, OpenCode, Codex et GitHub Copilot CLI. Image par défaut Ubuntu minimale, ou conteneur maison.

## Pourquoi ça m'intéresse

À valider : une couche d'exécution gouvernée pour laisser des agents de code ou d'ops travailler en autonomie sans leur donner les clés du SI. Le modèle « policy déclarative + credentials injectés hors de portée de l'agent + revue humaine sur l'élargissement des droits » répond directement à la question de sécurité qui bloque le passage d'un agent du poste de dev à un usage partagé. Utile aussi comme référence de design, même sans l'adopter.

## À vérifier avant d'essayer

- Maturité : v0.1.6, pas de date de release visible, environ 380 issues ouvertes. Stabilité des APIs entre versions mineures (le README recommande d'aligner SDK et gateway).
- Claude Code est annoncé comme supporté : vérifier le profil provider à écrire pour l'API Anthropic, et le comportement avec un agent qui touche beaucoup d'hôtes différents (MCP, registres de paquets).
- Policies versionnées en Git : tester si le cycle « policy en YAML, revue en PR, prover sur le diff » tient pour une équipe, ou si l'advisor devient indispensable.
- Coût opérationnel de la gateway en self-hosting, et prérequis Kubernetes (CNI qui applique les NetworkPolicy).
- Expressivité réelle des policies : granularité sur les méthodes d'API, effort pour écrire et maintenir une policy par agent.
- Télémétrie anonyme activée par défaut : à désactiver (`OPENSHELL_TELEMETRY_ENABLED=false`) pour un usage en entreprise.
- Windows/WSL 2 encore expérimental.
- Lock-in : dépendance éventuelle à des services NVIDIA (Brev n'est cité qu'en option cloud) à confirmer sur la doc d'architecture.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
