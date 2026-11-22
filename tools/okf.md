---
name: Open Knowledge Format (OKF)
url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
repo: https://github.com/GoogleCloudPlatform/open-knowledge-format
tags: [knowledge-management, context-engineering, agents, knowledge-graph]
radar: assess
pricing: open-source
added: 2026-11-22
updated: null
pitch: "Spécification ouverte (Apache-2.0) de Google Cloud : un bundle de connaissances est un dossier de fichiers markdown à front matter YAML, reliés entre eux par des liens, lisible par des agents."
alternatives: []
seen_in: [how-to-build-a-knowledge-factory]
---

## Ce que c'est

Format publié par Google Cloud le 12 juin 2026, qui formalise le pattern « LLM wiki » : un répertoire de fichiers markdown, un concept par fichier (table, métrique, runbook, API), avec un front matter YAML et des liens markdown qui forment un graphe. Aucun SDK, compte ou cloud n'est requis pour le produire ou le lire. Le repo fournit aussi un agent de référence (génération de bundles depuis BigQuery) et un visualiseur HTML autonome.

## Pourquoi ça m'intéresse

C'est le format de stockage de connaissances cité par l'article LangChain sur la knowledge factory (via LangSmith Context Hub). Il est assez simple pour qu'un agent curateur le lise et l'écrive, et il se versionne dans Git comme les autres fiches de ce repo. Candidat pour structurer une base de connaissances destinée à des agents.

## À vérifier avant d'essayer

- Maturité de la spec : l'annonce parle de v0.1 « point de départ, pas standard finalisé », le repo de v0.2. Repo récent (6 commits, aucune release ni package visibles au moment de la lecture).
- Champs requis : l'annonce dit que seul `type` l'est. Le repo cite aussi `status`, `sources`, `verified`, `stale_after` en exemple. Lire SPEC.md pour savoir ce qui est obligatoire en v0.2.
- Outillage : aucun validateur ni convertisseur mentionné sur la page du repo. Le dossier `connectors/` n'est pas décrit.
- Dépendances de l'agent de référence : le mode BigQuery demande gcloud et un projet de facturation, l'agent demande Gemini (clé AI Studio ou Vertex AI). Le format lui-même n'en dépend pas, l'agent oui.
- Repo canonique : l'annonce renvoie vers `GoogleCloudPlatform/knowledge-catalog` (dossier `okf`), la page lue est `GoogleCloudPlatform/open-knowledge-format`. Confirmer lequel fait foi.
- Adoption hors Google : la prise en charge par LangSmith Context Hub vient de l'article LangChain, pas d'un test. Vérifier ce que les autres outils lisent réellement.
- Fit avec un contenu non data : les exemples sont orientés données (tables BigQuery, datasets). Voir si le modèle de concept tient pour des skills et des procédures.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
