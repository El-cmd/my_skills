# Ajouter ou modifier un skill

1. Crée le skill avec `./scripts/new-skill.sh <nom> <description> [famille]`.
2. Remplace le contenu de brouillon par des instructions utiles et ciblées.
3. Ajoute uniquement les ressources réellement nécessaires au workflow.
4. Lance `python3 scripts/validate_skills.py`.
5. Régénère le catalogue avec `python3 scripts/build_catalog.py`.

## Principes de rédaction

- Utilise un nom en minuscules avec des tirets, identique au nom du dossier.
- Décris précisément dans le frontmatter ce que fait le skill et quand il
  s'applique.
- Garde `SKILL.md` concis et place les détails conditionnels dans `references/`.
- Documente surtout les décisions non évidentes, les contraintes réelles et le
  résultat attendu.
- Ne crée `scripts/`, `references/` ou `assets/` que lorsqu'ils apportent une
  valeur concrète.
- Ne mets jamais de token, clé API ou donnée sensible dans un skill.

Le format minimal est :

```markdown
---
name: nom-du-skill
description: Explique la capacité et les situations dans lesquelles l'utiliser.
---

# Instructions

Décris ici le résultat attendu, les contraintes et les choix importants.
```

