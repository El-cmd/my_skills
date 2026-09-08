#!/usr/bin/env sh

set -eu

usage() {
  echo "Usage: $0 <nom-du-skill> <description> [famille]" >&2
}

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
  usage
  exit 2
fi

skill_name=$1
skill_description=$2
skill_family=${3:-frontend}

if [ -z "$skill_description" ]; then
  echo "Erreur : la description ne peut pas être vide." >&2
  exit 1
fi

case "$skill_name" in
  *[!a-z0-9-]*|'')
    echo "Erreur : le nom doit contenir uniquement a-z, 0-9 et des tirets." >&2
    exit 1
    ;;
esac

case "$skill_name" in
  -*|*-|*--*)
    echo "Erreur : le nom ne peut pas commencer/finir par un tiret ou contenir '--'." >&2
    exit 1
    ;;
esac

if [ "${#skill_name}" -gt 63 ]; then
  echo "Erreur : le nom doit contenir moins de 64 caractères." >&2
  exit 1
fi

case "$skill_family" in
  *[!a-z0-9-]*|''|-*|*-|*--*)
    echo "Erreur : la famille doit être un slug en minuscules." >&2
    exit 1
    ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(dirname -- "$script_dir")
target_dir="$repo_root/skills/$skill_family/$skill_name"
template="$repo_root/templates/SKILL.md.tpl"

if [ -e "$target_dir" ]; then
  echo "Erreur : $target_dir existe déjà." >&2
  exit 1
fi

if [ ! -f "$template" ]; then
  echo "Erreur : template introuvable : $template" >&2
  exit 1
fi

mkdir -p "$target_dir"

SKILL_NAME=$skill_name SKILL_DESCRIPTION=$skill_description \
  python3 - "$template" "$target_dir/SKILL.md" <<'PY'
import os
from pathlib import Path
import json
import sys

template_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
content = template_path.read_text(encoding="utf-8")
description = os.environ["SKILL_DESCRIPTION"].replace("\n", " ").strip()
if "{{" in description or "}}" in description:
    raise SystemExit("Erreur : la description contient un marqueur réservé.")
content = content.replace("{{NAME}}", os.environ["SKILL_NAME"])
content = content.replace("{{DESCRIPTION}}", json.dumps(description, ensure_ascii=False))
output_path.write_text(content, encoding="utf-8")
PY

python3 "$repo_root/scripts/build_catalog.py"

echo "Skill créé : $target_dir/SKILL.md"
echo "Complète les instructions et retire le marqueur scaffold:complete-me."
