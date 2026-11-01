# brain-pro — base de connaissance AI engineering

Deux collections :
- `notes/` : fiches de lecture (article, paper, talk…), une par source.
- `tools/` : fiches outils, testés ou non, positionnés sur un radar.

## Conventions

Noms de fichiers, dossiers, clés et valeurs du front matter, tags, branches et préfixes de commit : **en anglais**.
Contenu (titres de sections, texte, tldr, pitch) : **en français**.

Fichiers nommés `<slug>.md` : kebab-case ASCII, en anglais, sans date. Tags partagés entre les deux collections.

## Fiche de lecture (`notes/`)

Schéma `schema/note.schema.json`, modèle `_templates/note.md`.
`status` : `inbox` (pas encore lu en entier), `read`, `deep-dive`.

1. Lire la source en entier (WebFetch). Si elle est inaccessible, s'arrêter et le dire.
2. Doublons : `grep -rl "<url>" notes/`. Si la fiche existe, proposer de la compléter.
3. Front matter. `tags` : réutiliser en priorité les tags existants (`grep -h "^tags:" notes/*.md tools/*.md`).
4. Corps en français, paraphrasé, une citation de moins de 15 mots maximum.
   Section « À ne pas faire » : seulement si la source formule des anti-patterns explicites, au format « anti-pattern → conséquence ». Sinon, l'omettre. Ne jamais inverser des bonnes pratiques pour la remplir. Les mises en garde personnelles vont dans « Ce que j'en retiens ».
5. `related` : slugs des fiches qui partagent des tags. `tools` : slugs des fiches outils citées.

## Fiche outil (`tools/`)

Schéma `schema/tool.schema.json`, modèle `_templates/tool.md`.
`radar` : `assess` (repéré, pas testé : valeur par défaut), `trial` (essayé), `adopt` (utilisé), `hold` (écarté).

1. Lire la page produit et, s'il existe, le README du repo. Ne rien affirmer sur les fonctionnalités ou la licence sans l'avoir lu.
2. Doublons : `grep -rli "<nom>" tools/`.
3. `pitch` : une phrase factuelle. `pricing` d'après la page de prix ou la licence.
4. « À vérifier avant d'essayer » : les questions ouvertes (licence, self-hosting, maturité, lock-in, coût).
5. « Retour d'essai » : laisser le placeholder tant que `radar: assess`. Ne jamais rédiger un retour d'essai que l'utilisateur n'a pas donné.
6. Changement d'anneau : mettre à jour `radar` et `updated`, compléter « Retour d'essai ».

## Liens entre collections

Une fiche de lecture qui cite un outil : `tools: [slug]` dans la fiche, et `seen_in: [slug-fiche]` dans l'outil. Le script refuse un lien non réciproque.

## Valider et publier

`python3 scripts/build_index.py --check && python3 scripts/build_index.py`
Commit `note: <title>` ou `tool: <name>`, push sur `main`.

## Interroger la base

Lire `INDEX.md` d'abord (fiches puis outils, une ligne chacun). Ouvrir les fichiers seulement si le détail est nécessaire.
Filtrer : `grep -l "tags:.*evals" notes/*.md tools/*.md`, `grep -l "status: inbox" notes/*.md`, `grep -l "radar: assess" tools/*.md`.
Tous les anti-patterns : `grep -A10 "^## À ne pas faire" notes/*.md`.

## Règles

- Le repo est public : pas de reproduction de contenu, pas d'information interne à un employeur.
- `INDEX.md` est généré, ne jamais le modifier à la main.
