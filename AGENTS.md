# Instructions pour les agents

Ce dépôt catalogue des skills, principalement frontend.

- Place les nouveaux skills frontend dans `skills/frontend/<nom>/`.
- Chaque skill doit avoir un `SKILL.md` avec un frontmatter contenant `name` et
  `description`.
- Le champ `name` doit correspondre au nom du dossier et utiliser uniquement des
  lettres minuscules, des chiffres et des tirets.
- Préserve l'intention de l'utilisateur et les conventions déjà présentes.
- N'ajoute des scripts, références ou assets que s'ils sont réellement utilisés.
- Après toute création, suppression ou modification de frontmatter, exécute
  `python3 scripts/build_catalog.py` et `python3 scripts/validate_skills.py`.
- Ne modifie pas `CATALOG.md` manuellement.

