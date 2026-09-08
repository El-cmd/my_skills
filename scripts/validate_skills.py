#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys

from skill_utils import NAME_PATTERN, SkillFormatError, discover_skill_files, parse_skill


REPO_ROOT = Path(__file__).resolve().parent.parent
SCAFFOLD_MARKER = "scaffold:complete-me"


def validate() -> list[str]:
    errors: list[str] = []
    seen_names: dict[str, Path] = {}

    for path in discover_skill_files(REPO_ROOT):
        relative_path = path.relative_to(REPO_ROOT)
        try:
            skill = parse_skill(path)
        except (OSError, UnicodeError, SkillFormatError) as exc:
            errors.append(f"{relative_path}: {exc}")
            continue

        if not NAME_PATTERN.fullmatch(skill.name):
            errors.append(f"{relative_path}: name invalide : {skill.name!r}")
        if path.parent.name != skill.name:
            errors.append(
                f"{relative_path}: le name {skill.name!r} ne correspond pas au dossier {path.parent.name!r}"
            )
        if len(skill.name) > 63:
            errors.append(f"{relative_path}: le name doit contenir moins de 64 caractères")
        if len(skill.description) < 20:
            errors.append(f"{relative_path}: la description est trop courte")
        if not skill.body:
            errors.append(f"{relative_path}: les instructions sont vides")
        if SCAFFOLD_MARKER in skill.body:
            errors.append(f"{relative_path}: le brouillon n'a pas été complété")
        if "{{" in skill.description or "}}" in skill.description:
            errors.append(f"{relative_path}: la description contient un placeholder")

        previous_path = seen_names.get(skill.name)
        if previous_path:
            errors.append(
                f"{relative_path}: name déjà utilisé dans {previous_path.relative_to(REPO_ROOT)}"
            )
        else:
            seen_names[skill.name] = path

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation échouée :", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    count = len(discover_skill_files(REPO_ROOT))
    print(f"Validation réussie : {count} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

