---
title: "Modern Web Guidance"
url: https://developer.chrome.com/docs/modern-web-guidance
type: doc
authors: [Chrome for Developers]
published: null
added: 2026-11-17
tags: [claude-code, context-engineering, agents, web-platform]
status: read
rating: null
tldr: "Chrome publie une CLI et des skills qui donnent à l'agent de codage des guides web à jour (Baseline) et un scanner de code legacy, pour qu'il arrête de produire du web d'il y a dix ans."
related: [get-your-site-agent-ready]
tools: [modern-web-guidance]
---

## En bref

Modern Web Guidance est un ensemble de skills édité par Chrome for Developers. Une CLI renvoie à l'agent des guides courts, choisis par des experts, avec les données de compatibilité Baseline. Le but : éviter que l'agent code avec les patterns que ses données d'entraînement ont le plus vus (modales maison, tooltips JS, animations à coups de `max-height`).

Le dépôt source (Apache-2.0) est maintenu avec Edge, Firefox et MDN. Les guides sont optimisés en tokens, et les évaluations servent à retirer ce que les modèles savent déjà. Lecture : page d'accueil, index des guides, workflow de modernisation, README du dépôt. Le contenu détaillé de chaque guide n'a pas été lu.

## Points clés

- Trois commandes : `search` (trouver un guide), `retrieve` (récupérer un guide par identifiant), `legacy-scan` (repérer des patterns obsolètes dans le code). Installation par `npx modern-web-guidance@latest install`, ou plugin Claude Code, Copilot CLI, Antigravity.
- Le catalogue annonce environ 190 guides sur la page d'index (le README parle de 250 fonctionnalités et 203 cas d'usage). Catégories : visual design, composants UI, comportements, formulaires, CSS, JavaScript (Temporal), performance (24 guides), accessibilité, sécurité (passkeys, Trusted Types, SRI), PWA, IA intégrée, WebMCP.
- Workflow de modernisation en quatre étapes : scan, vérification contextuelle (règles `keepWhen` / `dropWhen` pour écarter les faux positifs), rapport, puis récupération du guide, refactoring et tests.
- Pas de `--fix` volontairement : une modernisation touche souvent JS, HTML, CSS et dépendances, avec des effets de bord possibles. L'humain valide le plan.
- `legacy-scan` ne couvre qu'une partie des guides.
- Intégration avec Chrome DevTools for agents (audits perf, arbre d'accessibilité, logs console) et codelab d'introduction.
- Activité du dépôt à la capture : environ 6,5 k étoiles, 305 issues ouvertes, 1 612 commits.

## À ne pas faire

Anti-patterns détectés par le workflow de modernisation, avec leur remplacement :

- Auto-redimensionner un `<textarea>` via `scrollHeight` → remplacer par `field-sizing: content`.
- Envoyer un formulaire sur `keydown` Entrée sans garde IME → vérifier `e.isComposing` et `keyCode === 229`.
- Styler `:invalid` dès le chargement → utiliser `:user-invalid` et `:user-valid`.
- Omettre `autocomplete` sur les formulaires d'authentification et de paiement → valeurs standardisées.
- Écouteurs `e.target === dialog` pour fermer une modale → `<dialog closedby="any">`.
- `addEventListener` pour ouvrir des overlays → attributs `popover` et `popovertarget`.
- Accordéon animé avec `max-height: 9999px` → `interpolate-size: allow-keywords` et `calc-size()`.
- Bascule de classes du parent en JS selon l'état des enfants → sélecteur `:has()`.
- Blocs `@media (prefers-color-scheme: dark)` dupliqués → fonction `light-dark()`.
- Scripts CDN sans Subresource Integrity → `integrity` et `crossorigin="anonymous"`.

## Ce que j'en retiens

- Même logique que la fiche sur l'agent-readiness, côté producteur de code : on outille l'agent avec une référence à jour plutôt que de compter sur ses connaissances figées.
- Le couple `legacy-scan` + guides est applicable à un chantier de migration sur un grand parc de sites. Le scan donne une liste chiffrée, les guides donnent le remplacement.
- Gratuit (Apache-2.0). Le vrai coût est le temps de revue des refactorings proposés.
- Points ouverts : couverture réelle de `legacy-scan` (partielle), fraîcheur face à l'évolution de Baseline, biais Chrome malgré la gouvernance multi-navigateurs. Aucun retour d'essai à ce stade.

## Pour aller plus loin

- [Index des guides](https://developer.chrome.com/docs/modern-web-guidance/guides)
- [Workflow de modernisation](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow)
- [Dépôt source](https://github.com/GoogleChrome/modern-web-guidance-src)
- Codelab « Intro to Modern Web Guidance »
