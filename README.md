# brain-pro

Fiches de lecture sur l'AI engineering : agents, evals, RAG, context engineering, outillage.

- [`INDEX.md`](INDEX.md) : toutes les fiches, une ligne chacune
- [`notes/`](notes/) : une fiche par source, en Markdown avec front matter
- [`CLAUDE.md`](CLAUDE.md) : conventions et procédure d'ajout
- Site de lecture : https://aannet.github.io/brain-pro/ (Astro, dans `site/`)

Chaque fiche paraphrase la source et renvoie vers elle. Les droits sur les contenus cités restent à leurs auteurs.

## Ajouter une fiche

Coller le lien dans une conversation Claude avec le skill `/aa-reading-note-to-brain-pro`, ou à la main :

```bash
cp _templates/note.md notes/my-slug.md   # remplir
pip install pyyaml jsonschema
python3 scripts/build_index.py
```

La CI valide le front matter et régénère `INDEX.md` à chaque push sur `main`.

## Site

`site/` est un site Astro qui lit `notes/` sans les déplacer : index filtrable, pages par tag, page « À ne pas faire » qui agrège les anti-patterns de toutes les fiches, et recherche plein texte (Pagefind).

```bash
cd site && npm install
npm run dev     # aperçu local (sans la recherche)
npm run build   # site + index de recherche dans site/dist
```

Déployé sur GitHub Pages par `.github/workflows/deploy-site.yml` à chaque push qui touche `notes/` ou `site/`.
