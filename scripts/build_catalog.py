#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from skill_utils import SkillFormatError, discover_skill_files, parse_skill


REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "CATALOG.md"


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_catalog() -> str:
    skills = []
    for path in discover_skill_files(REPO_ROOT):
        try:
            skills.append(parse_skill(path))
        except (OSError, UnicodeError, SkillFormatError) as exc:
            relative_path = path.relative_to(REPO_ROOT)
            raise SkillFormatError(f"{relative_path}: {exc}") from exc

    lines = [
        "# Catalogue des skills",
        "",
        "> Ce fichier est généré par `python3 scripts/build_catalog.py`.",
        "",
    ]

    if not skills:
        lines.extend(["_Aucun skill référencé pour le moment._", ""])
        return "\n".join(lines)

    lines.extend(
        [
            "| Famille | Skill | Description |",
            "| --- | --- | --- |",
        ]
    )
    for skill in sorted(skills, key=lambda item: (item.path.parent.parent.name, item.name)):
        family = skill.path.parent.parent.name
        link = skill.path.relative_to(REPO_ROOT).as_posix()
        lines.append(
            f"| {markdown_cell(family)} | [{markdown_cell(skill.name)}]({link}) | "
            f"{markdown_cell(skill.description)} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Génère le catalogue des skills.")
    parser.add_argument("--check", action="store_true", help="vérifie sans modifier le fichier")
    args = parser.parse_args()

    try:
        expected = render_catalog()
    except SkillFormatError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        return 1

    current = CATALOG_PATH.read_text(encoding="utf-8") if CATALOG_PATH.exists() else ""
    if args.check:
        if current != expected:
            print("CATALOG.md n'est pas à jour. Lance scripts/build_catalog.py.", file=sys.stderr)
            return 1
        print("CATALOG.md est à jour.")
        return 0

    if current != expected:
        CATALOG_PATH.write_text(expected, encoding="utf-8")
        print("CATALOG.md mis à jour.")
    else:
        print("CATALOG.md est déjà à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

