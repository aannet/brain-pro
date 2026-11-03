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

Un runtime open-source (Apache 2.0, v0.1.x) qui fait tourner chaque agent dans une sandbox. L'opérateur déclare dans une policy ce que l'agent peut lire, appeler et exécuter, et OpenShell l'applique au niveau noyau : accès fichiers et appels système filtrés, chaque connexion réseau vérifiée avant de sortir. L'agent ne voit jamais les vrais secrets : ils sont injectés seulement sur les requêtes vers des endpoints autorisés.

L'architecture tient en trois briques : une gateway (control plane : sandboxes, policies, accès), un supervisor, et les sandboxes (images, runtimes, support GPU). Les changements de policy passent par un « advisor » et un « prover » : la vérification formelle signale les nouveaux accès risqués (nouvel hôte avec credentials, nouvelle méthode d'API) et les met en attente de revue humaine. Tourne sur Docker, Podman ou virtualisation hôte, en local ou sur Kubernetes via Helm. SDK Python, TypeScript, Go et Rust. L'image par défaut est un Ubuntu minimal sans agent ; le tutoriel installe OpenCode.

## Pourquoi ça m'intéresse

À valider : une couche d'exécution gouvernée pour laisser des agents de code ou d'ops travailler en autonomie sans leur donner les clés du SI. Le modèle « policy déclarative + credentials injectés hors de portée de l'agent + revue humaine sur l'élargissement des droits » répond directement à la question de sécurité qui bloque le passage d'un agent du poste de dev à un usage partagé. Utile aussi comme référence de design, même sans l'adopter.

## À vérifier avant d'essayer

- Maturité : v0.1.x, pas de date de release visible, environ 380 issues ouvertes. Stabilité des APIs entre versions mineures (le README recommande d'aligner SDK et gateway).
- Agents supportés : seul OpenCode est cité. Faisabilité de faire tourner Claude Code ou un agent maison dans une sandbox, et comportement avec un agent qui a besoin de beaucoup d'hôtes différents.
- Coût opérationnel de la gateway en self-hosting, et prérequis Kubernetes (CNI qui applique les NetworkPolicy).
- Expressivité réelle des policies : granularité sur les méthodes d'API, effort pour écrire et maintenir une policy par agent.
- Télémétrie anonyme activée par défaut : à désactiver (`OPENSHELL_TELEMETRY_ENABLED=false`) pour un usage en entreprise.
- Windows/WSL 2 encore expérimental.
- Lock-in : dépendance éventuelle à des services NVIDIA (Brev n'est cité qu'en option cloud) à confirmer sur la doc d'architecture.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
