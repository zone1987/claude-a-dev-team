# shadcn/ui — Monorepo

The CLI understands monorepo structure and installs components, dependencies,
and registry dependencies to the correct paths while handling imports.

## Create a new monorepo project

```bash
npx shadcn@latest init --monorepo
# Select template: Next.js | Vite | TanStack Start | React Router | Astro
```

Creates two workspaces: `web` (app) and `ui` (shared components),
with Turborepo as the build system.

## Add components (run from app directory)

```bash
cd apps/web
npx shadcn@latest add button
# or from repo root:
npx shadcn@latest add button -c apps/web
```

The CLI detects the component type:
- UI primitives → `packages/ui/src/components/`
- App-specific blocks → `apps/web/components/`

## Import components

```tsx
import { Button } from "@workspace/ui/components/button"
import { useTheme } from "@workspace/ui/hooks/use-theme"
import { cn } from "@workspace/ui/lib/utils"
```

## Reference files

- [MONOREPO-DETAIL.md](MONOREPO-DETAIL.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/monorepo.mdx`
