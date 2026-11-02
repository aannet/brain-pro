---
title: "The AI-native SDLC playbook"
url: https://claude.com/fr/resources/articles/the-ai-native-sdlc-playbook
type: blog
authors: [Louis Claxton]
published: 2026-08-21
added: 2026-11-02
tags: [sdlc, claude-code, governance, evals, security, adoption]
status: read
rating: null
tldr: "Le code n'est plus le goulot : le SDLC devient une boucle d'artefacts versionnés (intent, spec, plan, diff, revue, incident), les règles critiques passent par des hooks déterministes et l'humain juge aux portes."
related: [how-claude-code-works-in-large-codebases]
tools: []
---

## En bref

Anthropic part d'un constat : l'écriture du code est devenue rapide, mais planification, revue, tests, déploiement et gouvernance tournent encore à vitesse humaine. Le goulot s'est déplacé. L'article propose de repenser tout le cycle comme une boucle où chaque étape produit un artefact versionné lu par la suivante, la chaîne de commits servant de piste d'audit. L'humain reste propriétaire des décisions de jugement et concentre son attention sur les points de contrôle, là où l'agent a signalé quelque chose.

## Points clés

- Six étapes, six artefacts : `intent.md` (Plan), `spec.md` (Design), `plan.md` puis diff et tests (Build, Test), revue de PR (Deploy), dossier d'incident réinjecté comme nouvel intent (Maintain).
- Plan : l'idée est capturée une fois, dans les mots de son auteur (problème, résultat, utilisateurs, contraintes, questions ouvertes), puis validée par le product owner. Indicateurs : délai discussion → fichier commité, taux d'acceptation.
- Design : la spec est dérivée de l'intent en appliquant les skills de l'organisation (marque, sécurité, conformité, UX) ; les points sensibles remontent au propriétaire de la politique concernée.
- Build : plan mode obligatoire avant tout code, auto mode seulement quand les garde-fous sont mûrs. `CLAUDE.md` versionné et court. Une skill est un contrôle consultatif ; une règle qui doit toujours s'appliquer exige un hook déterministe.
- Chaque artefact a un système de référence désigné : le dépôt, l'outil historique (Jira, ServiceNow), ou au minimum un lien entre les deux.
- Test : donner à l'agent sa propre boucle de feedback (tests, build, capture) avant tout regard humain. Bug fix = test qui échoue d'abord, protégé par un hook. Evals en CI à chaque changement de configuration ; chaque incident de prod devient une eval.
- Deploy : revue de PR assistée cadrée par un `REVIEW.md` (passes, sévérités, seuils), approbation humaine via protection de branche. Les hooks servent de portes d'approbation. L'agent agit jusqu'à la porte de prod, sans pouvoir la franchir.
- Configuration gérée pour environnement réglementé : lecture des secrets refusée, allowlist réseau, sandbox, marketplace approuvée, version minimale imposée.
- Maintain : monitoring déterministe à seuils en écarts-types ; l'intervention de l'agent est graduée selon le niveau (log, diagnostic read-only, PR proposée, runbook pré-approuvé). Scans de sécurité planifiés, pas ponctuels.
- Indicateurs par étape plutôt que chiffres de gain : taux de passage au premier essai, taux de réussite des evals, temps avant la première PR d'un arrivant, métriques DORA.

## À ne pas faire

- Relire chaque ligne générée à la main → impossible à tenir au volume des agents ; la revue doit se déplacer vers l'intention et le risque.
- Faire passer les exceptions par des comités hebdomadaires ou mensuels → la gouvernance devient le goulot.
- Faire respecter une règle critique par une skill seule → ce n'est qu'une recommandation, l'agent peut l'ignorer.
- Laisser l'agent auteur approuver sa propre modification ou réécrire les tests pour faire passer un fix → le contrôle s'auto-valide.
- Laisser `CLAUDE.md` vieillir ou grossir → le contexte transmis aux agents devient faux ou bruité.
- Donner à l'agent des credentials de prod ou un réseau non filtré → surface d'attaque et de dégât sans borne.
- Multiplier les sessions parallèles sans capacité de revue → la production dépasse la capacité de contrôle.
- Traiter un scan de sécurité comme un événement ponctuel → la couverture se dégrade entre deux scans.
- Insérer des demandes d'approbation à chaque étape de build → l'humain revient sur le chemin critique.

## Ce que j'en retiens

La chaîne `intent.md` → `spec.md` → `plan.md` recoupe une séparation Intent / Spec / Implementation ; la proposition à tester est d'en faire des fichiers versionnés dans le dépôt plutôt que des documents vivant à côté. La distinction skill (consultatif) / hook (déterministe) donne une grille simple pour classer chaque règle de gouvernance. Angle mort : l'article ne parle ni du coût de maintenance des artefacts produits (tests, evals, specs), ni du brownfield où l'intent d'origine n'existe plus.

## Pour aller plus loin

- [How Claude Code works in large codebases](how-claude-code-works-in-large-codebases.md) : le harness (CLAUDE.md, hooks, skills) côté préparation du codebase.
