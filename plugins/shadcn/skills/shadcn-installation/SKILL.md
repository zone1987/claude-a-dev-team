---
name: shadcn-installation
description: >
  shadcn/ui installation — all framework guides (Next.js, Vite, Astro, Remix,
  Laravel, Gatsby, React Router, TanStack Start, TanStack Router, manual).
  Use when asked about installing shadcn/ui, shadcn init, framework setup,
  adding components, shadcn/create, existing project setup.
---

# shadcn/ui — Installation

Three paths for every new project:

1. **shadcn/create** — visual builder at https://ui.shadcn.com/create —
   generates a framework-specific init command with preset code.
2. **CLI scaffold** — `npx shadcn@latest init -t [framework]`
3. **Existing project** — add to an already-created app.

## Quick start by framework

```bash
# Next.js
npx shadcn@latest init -t next

# Vite
npx shadcn@latest init -t vite

# TanStack Start
npx shadcn@latest init -t start

# React Router
npx shadcn@latest init -t react-router

# Astro
npx shadcn@latest init -t astro

# Laravel (create app first)
laravel new my-app && cd my-app && npx shadcn@latest init

# Remix
npx create-remix@latest my-app && cd my-app && npx shadcn@latest init

# Gatsby
npm init gatsby && npx shadcn@latest init

# TanStack Router
npx create-tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn

# Manual (any framework)
npm install shadcn class-variance-authority clsx tailwind-merge lucide-react tw-animate-css
npx shadcn@latest init
```

## Add components

```bash
npx shadcn@latest add button
npx shadcn@latest add card dialog select
```

## Reference files

- [references/next.md](references/next.md)
- [references/vite.md](references/vite.md)
- [references/astro.md](references/astro.md)
- [references/remix.md](references/remix.md)
- [references/laravel.md](references/laravel.md)
- [references/gatsby.md](references/gatsby.md)
- [references/react-router.md](references/react-router.md)
- [references/tanstack.md](references/tanstack.md)
- [references/tanstack-router.md](references/tanstack-router.md)
- [references/manual.md](references/manual.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/`
