---
name: gsap-awwwards-website
description: SPYLT product landing with GSAP scroll animations, React 19, and Tailwind CSS 4.
---

# GSAP Awwwards Website

A stunning product landing page with GSAP scroll animations, modern React 19 architecture, and Tailwind CSS 4 styling.

## Tech Stack

- **Framework**: React 19
- **Build Tool**: Vite
- **Animation**: GSAP
- **Styling**: Tailwind CSS 4
- **Package Manager**: npm
- **Output**: `dist` directory
- **Dev Port**: 5173

## Setup

### 1. Clone the Template

Clone the template into a new, empty directory. Do not move or delete files from
an existing workspace to make room for it.

```bash
git clone --depth 1 https://github.com/Eng0AI/gsap-awwwards-website-template.git my-gsap-site
cd my-gsap-site
```

Preserve the cloned Git history by default. If the user explicitly wants a new
repository, create it in a separate empty directory instead of deleting an
existing `.git` directory.

### 3. Install Dependencies

```bash
npm install
```

## Build

```bash
npm run build
```

Creates a production build in the `dist/` directory.

## Deploy

> **CRITICAL**: For Vercel, you MUST use `vercel build --prod` then `vercel deploy --prebuilt --prod`. Never use `vercel --prod` directly.

### Vercel (Recommended)

Read `VERCEL_TOKEN` from the environment or a secret manager. Never print or
commit its value.

```bash
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN
```

### Netlify

```bash
netlify deploy --prod --dir=dist
```

## Development

```bash
npm run dev
```

Opens at http://localhost:5173

## Notes

- Static React site - no environment variables needed
- Never run `npm run dev` in VM environment
