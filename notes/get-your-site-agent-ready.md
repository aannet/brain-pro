---
title: "Get your site agent-ready"
url: https://debbie.codes/blog/get-your-site-agent-ready
type: blog
authors: [Debbie O'Brien]
published: 2026-11-13
added: 2026-11-16
tags: [context-engineering, mcp, llms-txt, agent-readiness]
status: read
rating: null
tldr: "Exposer aux agents une carte courte (llms.txt), un index complet et des copies markdown de chaque page, tous générés au build, coûte peu et évite de leur faire décoder du HTML."
related: [modern-web-guidance]
tools: []
---

## En bref

L'autrice rend son site lisible par les agents IA avec des fichiers texte simples plutôt que du HTML à décoder. Trois couches : une carte courte (`/llms.txt`), un catalogue complet (`/llms-full.txt`) et une copie markdown de chaque article. Elle reconnaît que les grands crawlers n'exploitent pas encore ces fichiers, et défend le geste quand même : il est peu coûteux et sert déjà les agents de code et les outils qui vont chercher une page.

## Points clés

- Le gain de bruit est mesuré : une page HTML de 54 791 octets contient environ 3 121 octets de texte d'article, et sa version markdown pèse 4 023 octets. Les quatre pages de tags MCP du site font environ 257 Ko de HTML pour environ 12 Ko de contenu utile.
- `/llms.txt` (5 273 octets ici) suit la proposition de Jeremy Howard : titre, résumé en blockquote, sections de liens `- [nom](url): notes`, section `## Optional` facultative.
- `/llms-full.txt` (environ 151 Ko) est une liste annotée de tout le contenu, sans le corps des articles. Ce n'est pas dans la proposition officielle, mais c'est un ajout courant.
- `/blog/<slug>.md` : une copie markdown propre par article, avec titre, date, description, tags et une ligne Canonical.
- Un seul script de build (`generate-content-index.mjs`) produit llms.txt, llms-full.txt et l'index JSON consommé par les outils WebMCP, à partir du même catalogue.
- Les liens vont de préférence vers les `.md`. Dans le `<head>`, des `rel="alternate" type="text/markdown"` et un `rel="describedby"` vers llms.txt rendent le tout découvrable. Un commentaire dans `robots.txt` complète, sans remplacer.
- Les `.md` sont servis en `text/markdown`, avec `Link rel=canonical` et `X-Robots-Tag: noindex` pour que le HTML reste l'original aux yeux des moteurs.
- Vérification avec `curl` et l'onglet Network des DevTools.
- Contexte de position : John Mueller (Google) juge llms.txt « purely speculative for now ». Il se montre plus favorable à WebMCP, étape suivante où la page expose des outils appelables par l'agent.

## À ne pas faire

- Maintenir à la main un gros fichier d'index → il dérive du contenu réel ; le générer au build.
- Publier un llms.txt pour gagner en classement dans la recherche ou dans les résultats IA de Google → aucun effet démontré, et Google ne le reconnaît pas.
- S'en tenir au commentaire `robots.txt` → les agents ne découvrent pas les copies markdown ; il faut aussi les liens dans les pages.
- Laisser des brouillons dans les fichiers générés ou accessibles via leur URL `.md` → fuite de contenu non publié ; ils doivent renvoyer une 404.
- Attendre plus de fraîcheur que le dernier build → les fichiers reflètent le contenu au moment du déploiement, pas avant.

## Ce que j'en retiens

La recette est transposable à tout site à contenu éditorial : un script de build, une source unique de catalogue, trois sorties. Le point à vérifier avant d'investir est l'usage réel : l'autrice admet elle-même qu'il est faible côté crawlers, donc la valeur vient surtout des agents de code et des assistants qui récupèrent une page à la demande. Pour un parc multi-sites avec un CMS, la génération au build pose surtout la question de l'exclusion des brouillons et de la canonicalisation.

## Pour aller plus loin

- Proposition llms.txt (Jeremy Howard) : https://www.answer.ai/posts/2024-09-03-llmstxt.html
- Spécification : https://llmstxt.org/
- Exemples réels : https://docs.anthropic.com/llms.txt et https://developers.cloudflare.com/llms.txt
- Position de Google, via Search Engine Journal : https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/
- MCP : https://modelcontextprotocol.io/introduction
