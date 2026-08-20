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

- [INSTALLATION-NEXT.md](INSTALLATION-NEXT.md)
- [INSTALLATION-VITE.md](INSTALLATION-VITE.md)
- [INSTALLATION-ASTRO.md](INSTALLATION-ASTRO.md)
- [INSTALLATION-REMIX.md](INSTALLATION-REMIX.md)
- [INSTALLATION-LARAVEL.md](INSTALLATION-LARAVEL.md)
- [INSTALLATION-GATSBY.md](INSTALLATION-GATSBY.md)
- [INSTALLATION-REACT-ROUTER.md](INSTALLATION-REACT-ROUTER.md)
- [INSTALLATION-TANSTACK.md](INSTALLATION-TANSTACK.md)
- [INSTALLATION-TANSTACK-ROUTER.md](INSTALLATION-TANSTACK-ROUTER.md)
- [INSTALLATION-MANUAL.md](INSTALLATION-MANUAL.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/`
