# brain-pro

Fiches de lecture sur l'AI engineering : agents, evals, RAG, context engineering, outillage.

- [`INDEX.md`](INDEX.md) : toutes les fiches, une ligne chacune
- [`notes/`](notes/) : une fiche par source, en Markdown avec front matter
- [`CLAUDE.md`](CLAUDE.md) : conventions et procédure d'ajout

Chaque fiche paraphrase la source et renvoie vers elle. Les droits sur les contenus cités restent à leurs auteurs.

## Ajouter une fiche

Coller le lien dans une conversation Claude avec le skill `reading-note`, ou à la main :

```bash
cp _templates/note.md notes/my-slug.md   # remplir
pip install pyyaml jsonschema
python3 scripts/build_index.py
```

La CI valide le front matter et régénère `INDEX.md` à chaque push sur `main`.
