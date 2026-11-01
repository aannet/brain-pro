# brain-pro

Base de connaissance sur l'AI engineering : agents, evals, RAG, context engineering, outillage.

- [`INDEX.md`](INDEX.md) : toutes les fiches et tous les outils, une ligne chacun
- [`notes/`](notes/) : fiches de lecture, une par source
- [`tools/`](tools/) : outils repérés, essayés, adoptés ou écartés (radar `assess` / `trial` / `adopt` / `hold`)
- [`CLAUDE.md`](CLAUDE.md) : conventions et procédures d'ajout

Chaque fiche paraphrase la source et renvoie vers elle. Les droits sur les contenus cités restent à leurs auteurs. Un outil en `assess` n'a pas été testé.

## Ajouter une fiche ou un outil

Coller le lien dans une conversation Claude avec le skill `/aa-brain-pro`, ou à la main :

```bash
cp _templates/note.md notes/my-slug.md   # ou _templates/tool.md vers tools/
pip install pyyaml jsonschema
python3 scripts/build_index.py
```

La CI valide le front matter et régénère `INDEX.md` à chaque push sur `main`.
