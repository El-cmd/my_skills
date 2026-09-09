from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Skill:
    path: Path
    name: str
    description: str
    body: str


class SkillFormatError(ValueError):
    pass


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise SkillFormatError(f"chaîne YAML invalide : {value!r}") from exc
        if not isinstance(parsed, str):
            raise SkillFormatError(f"valeur texte attendue : {value!r}")
        return parsed
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def discover_skill_files(root: Path) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.exists():
        return []
    return sorted(skills_root.glob("**/SKILL.md"))


def parse_skill(path: Path) -> Skill:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        raise SkillFormatError("le fichier doit commencer par un frontmatter YAML")

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise SkillFormatError("le frontmatter YAML n'est pas fermé") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise SkillFormatError(f"ligne de frontmatter invalide : {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = parse_scalar(value)

    missing = [key for key in ("name", "description") if not fields.get(key)]
    if missing:
        raise SkillFormatError(f"champ(s) obligatoire(s) manquant(s) : {', '.join(missing)}")

    return Skill(
        path=path,
        name=fields["name"],
        description=fields["description"],
        body="\n".join(lines[end + 1 :]).strip(),
    )
