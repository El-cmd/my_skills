# My Skills

Ce dépôt centralise des skills réutilisables, principalement orientés frontend.
Chaque skill vit dans son propre dossier et possède un fichier `SKILL.md` comme
point d'entrée.

## Organisation

```text
skills/
└── frontend/
    └── nom-du-skill/
        ├── SKILL.md          # obligatoire
        ├── scripts/          # optionnel : automatisations déterministes
        ├── references/       # optionnel : documentation ciblée
        └── assets/           # optionnel : templates et fichiers à réutiliser
```

Les autres familles peuvent être ajoutées au même niveau que `frontend`, par
exemple `backend`, `tooling` ou `design`.

## Créer un skill

```bash
./scripts/new-skill.sh build-react-component \
  "Crée ou adapte un composant React accessible dans un projet existant."
```

Le troisième argument permet de choisir une autre famille :

```bash
./scripts/new-skill.sh audit-api \
  "Analyse une API et signale les problèmes de conception." backend
```

Le générateur crée le dossier et actualise [CATALOG.md](CATALOG.md). Le fichier
produit contient un marqueur de brouillon : complète ses instructions, puis
retire ce marqueur avant validation.

## Vérifier et indexer

```bash
python3 scripts/validate_skills.py
python3 scripts/build_catalog.py
```

Avant un commit, vérifie aussi que le catalogue est à jour :

```bash
python3 scripts/build_catalog.py --check
```

## Utiliser un skill localement

Un dossier de skill finalisé peut être copié ou lié dans le dossier de skills de
Codex :

```bash
ln -s "$(pwd)/skills/frontend/build-react-component" \
  "${CODEX_HOME:-$HOME/.codex}/skills/build-react-component"
```

Évite de versionner des secrets, des dépendances générées ou des sorties de
build dans ce dépôt.
