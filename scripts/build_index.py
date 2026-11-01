#!/usr/bin/env python3
"""Valide le front matter des fiches (notes/) et des outils (tools/), puis génère INDEX.md.

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
RADAR_ORDER = ["adopt", "trial", "assess", "hold"]
RADAR_LABEL = {"adopt": "Adopt", "trial": "Trial", "assess": "Assess", "hold": "Hold"}


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


def load(folder: str, schema_file: str, errors: list) -> dict:
    validator = Draft202012Validator(
        json.loads((ROOT / "schema" / schema_file).read_text(encoding="utf-8"))
    )
    items = {}
    for path in sorted((ROOT / folder).glob("*.md")):
        label = f"{folder}/{path.name}"
        try:
            fm = read_front_matter(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{label}: {exc}")
            continue
        for err in validator.iter_errors(fm):
            loc = ".".join(str(p) for p in err.path) or "(racine)"
            errors.append(f"{label}: {loc}: {err.message}")
        items[path.stem] = fm
    return items


def esc(value) -> str:
    return str(value or "").replace("|", "\\|")


def main() -> int:
    check_only = "--check" in sys.argv
    errors: list[str] = []
    notes = load("notes", "note.schema.json", errors)
    tools = load("tools", "tool.schema.json", errors)

    for slug, fm in notes.items():
        for rel in fm.get("related") or []:
            if rel not in notes:
                errors.append(f"notes/{slug}.md: related -> '{rel}' introuvable")
        for t in fm.get("tools") or []:
            if t not in tools:
                errors.append(f"notes/{slug}.md: tools -> '{t}' introuvable dans tools/")
            elif slug not in (tools[t].get("seen_in") or []):
                errors.append(f"tools/{t}.md: seen_in doit contenir '{slug}' (lien réciproque)")
    for slug, fm in tools.items():
        for n in fm.get("seen_in") or []:
            if n not in notes:
                errors.append(f"tools/{slug}.md: seen_in -> '{n}' introuvable dans notes/")
            elif slug not in (notes[n].get("tools") or []):
                errors.append(f"notes/{n}.md: tools doit contenir '{slug}' (lien réciproque)")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{len(notes)} fiche(s), {len(tools)} outil(s) valides")
    if check_only:
        return 0

    lines = [
        "# Index",
        "",
        "Fichier généré par `scripts/build_index.py`, ne pas modifier à la main.",
        "",
        f"## Fiches de lecture ({len(notes)})",
        "",
        "| Ajout | Fiche | Type | Tags | Statut | TL;DR |",
        "|---|---|---|---|---|---|",
    ]
    for slug, fm in sorted(notes.items(), key=lambda kv: kv[1].get("added", ""), reverse=True):
        tags = " ".join(f"`{t}`" for t in fm.get("tags", []))
        lines.append(
            f"| {fm.get('added', '')} | [{esc(fm.get('title', slug))}](notes/{slug}.md) "
            f"| {fm.get('type', '')} | {tags} | {fm.get('status', '')} | {esc(fm.get('tldr'))} |"
        )

    lines += ["", f"## Outils ({len(tools)})", ""]
    if not tools:
        lines.append("Aucun outil référencé pour l'instant.")
    else:
        lines += [
            "Radar : `adopt` utilisé, `trial` essayé, `assess` repéré non testé, `hold` écarté.",
            "",
            "| Radar | Outil | Tags | Prix | Pitch |",
            "|---|---|---|---|---|",
        ]
        ordered = sorted(
            tools.items(),
            key=lambda kv: (RADAR_ORDER.index(kv[1].get("radar", "assess")), kv[1].get("name", "").lower()),
        )
        for slug, fm in ordered:
            tags = " ".join(f"`{t}`" for t in fm.get("tags", []))
            lines.append(
                f"| {RADAR_LABEL.get(fm.get('radar'), '')} | [{esc(fm.get('name', slug))}](tools/{slug}.md) "
                f"| {tags} | {fm.get('pricing', '')} | {esc(fm.get('pitch'))} |"
            )

    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
