---
name: "Brand Context Protocol (BCP)"
url: "https://hellotacit-ai.pages.dev/docs"
repo: null
tags: [brand, context-engineering, agents, agent-readiness]
radar: assess
pricing: open-source
added: 2026-11-19
updated: null
pitch: "Spécification de fichiers markdown + YAML publiés sous /.well-known/brand/ pour donner aux agents IA la voix, les valeurs, les limites et les claims d'une marque."
alternatives: ["AdCP brand.json", "brand.md (thebrand.md)", "Intentful Brand MCP"]
seen_in: [brand-harness]
---

## Ce que c'est

Un format ouvert publié par Tacit (v0.1, spec en CC BY 4.0, code de référence en MIT), sans SDK ni serveur. Une racine `brand.md` obligatoire et des fichiers complémentaires (voice, values, boundaries, claims, representation) que chaque agent charge selon sa tâche : rédaction → voice, achat média → boundaries + claims, agent tiers → representation.

## Pourquoi ça m'intéresse

Proposition : s'en servir comme structure de départ pour le Brand Code d'un brand harness, versionné dans Git, plutôt que d'inventer un schéma maison. Le découpage par fichier colle au chargement de contexte à la demande.

## À vérifier avant d'essayer

- Maturité : v0.1, validateur officiel annoncé mais pas encore livré. Les changements cassants sont promis avec un préavis de 90 jours avant la v1.0.
- Collision de nom : un autre « Brand Context Protocol » existe (craft.wild.as), fermé ou non, à distinguer.
- Exposition publique sous `/.well-known/` : quels fichiers peuvent être publics (representation) et lesquels doivent rester internes (claims en cours de revue juridique, boundaries) ?
- Adoption réelle par des agents tiers : aucun consommateur identifié en dehors des exemples de la spec.
- Le fichier visual.md montré dans certaines présentations ne figure pas dans la spec v0.1.

## Retour d'essai

Seulement en trial, adopt ou hold : ce qui a marché, ce qui a coincé, la raison du choix.
