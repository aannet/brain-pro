#!/usr/bin/env python3
"""Valide le front matter des fiches et génère INDEX.md.

Usage :
  python3 scripts/build_index.py          # valide puis écrit INDEX.md
  python3 scripts/build_index.py --check  # valide seulement (CI)
Dépendances : pyyaml, jsonschema
"""
import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
SCHEMA = json.loads((ROOT / "schema" / "note.schema.json").read_text(encoding="utf-8"))


def normalize(value):
    """YAML transforme 2026-11-01 en date ; le schéma attend une chaîne."""
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()[:10]
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    return value


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("front matter absent")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("front matter non fermé")
    return normalize(yaml.safe_load(text[4:end]) or {})


def main() -> int:
    check_only = "--check" in sys.argv
    validator = Draft202012Validator(SCHEMA)
    notes, errors = [], []

    for path in sorted(NOTES.glob("*.md")):
        try:
            fm = read_front_matter(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.name}: {exc}")
            continue
        for err in validator.iter_errors(fm):
            loc = ".".join(str(p) for p in err.path) or "(racine)"
            errors.append(f"{path.name}: {loc}: {err.message}")
        notes.append((path.stem, fm))

    slugs = {s for s, _ in notes}
    for slug, fm in notes:
        for rel in fm.get("related") or []:
            if rel not in slugs:
                errors.append(f"{slug}.md: related -> '{rel}' introuvable")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{len(notes)} fiche(s) valide(s)")
    if check_only:
        return 0

    notes.sort(key=lambda f: f[1].get("added", ""), reverse=True)
    lines = [
        "# Index des fiches",
        "",
        "Fichier généré par `scripts/build_index.py`, ne pas modifier à la main.",
        "",
        "| Ajout | Fiche | Type | Tags | Statut | TL;DR |",
        "|---|---|---|---|---|---|",
    ]
    for slug, fm in notes:
        tags = " ".join(f"`{t}`" for t in fm.get("tags", []))
        tldr = str(fm.get("tldr", "")).replace("|", "\\|")
        title = str(fm.get("title", slug)).replace("|", "\\|")
        lines.append(
            f"| {fm.get('added', '')} | [{title}](notes/{slug}.md) | {fm.get('type', '')} "
            f"| {tags} | {fm.get('status', '')} | {tldr} |"
        )
    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
