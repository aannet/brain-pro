# brain-pro — base de fiches de lecture AI engineering

## Conventions

Noms de fichiers, dossiers, clés et valeurs du front matter, tags, branches et préfixes de commit : **en anglais**.
Contenu des fiches (titres de sections, texte, tldr) : **en français**.

Une fiche = un fichier Markdown dans `notes/`, nommé `<slug>.md` : kebab-case ASCII, en anglais, sans date (ex. `building-effective-agents.md`).
Le front matter respecte `schema/note.schema.json`. Le modèle est `_templates/note.md`.
Valeurs de `status` : `inbox` (pas encore lu en entier), `read`, `deep-dive`.

## Créer une fiche à partir d'un lien

1. Lire la source en entier (WebFetch). Si elle est inaccessible, s'arrêter et le dire.
2. Vérifier les doublons : `grep -rl "<url>" notes/`. Si la fiche existe, proposer de la compléter.
3. Remplir le front matter. `tags` : réutiliser en priorité les tags existants (`grep -h "^tags:" notes/*.md`).
4. Rédiger le corps en français, paraphrasé. Une citation de moins de 15 mots maximum par fiche.
5. Remplir `related` avec les slugs des fiches qui partagent des tags.
6. Valider puis régénérer l'index : `python3 scripts/build_index.py --check && python3 scripts/build_index.py`.
7. Commit `note: <title>`, push sur `main`.

## Interroger la base

Lire `INDEX.md` d'abord (une ligne par fiche). Ouvrir les fiches seulement si le détail est nécessaire.
Filtrer : `grep -l "tags:.*evals" notes/*.md`, `grep -l "status: inbox" notes/*.md`.

## Règles

- Le repo est public : pas de reproduction de contenu, pas d'information interne à un employeur.
- `INDEX.md` est généré, ne jamais le modifier à la main.
