# shadcn/ui — Next.js Installation

## Option A: Use shadcn/create

1. Open https://ui.shadcn.com/create?template=next
2. Build preset visually (style, colors, fonts, icons).
3. Click "Create Project", copy the generated command:
   ```bash
   npx shadcn@latest init --preset [CODE] --template next
   ```
4. Add components:
   ```bash
   npx shadcn@latest add card
   ```

## Option B: CLI scaffold

```bash
npx shadcn@latest init -t next

# Monorepo
npx shadcn@latest init -t next --monorepo
```

Add component from monorepo root:
```bash
npx shadcn@latest add card -c apps/web
```

## Option C: Existing Next.js project

### Step 1 — Create project (if needed)
```bash
npx create-next-app@latest
# or with src/ directory
npx create-next-app@latest --src-dir
```
Choose recommended defaults: Tailwind CSS, App Router, `@/*` import alias.

### Step 2 — Ensure tsconfig.json alias
```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```
For `--src-dir`: `"@/*": ["./src/*"]`

### Step 3 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 4 — Add components
```bash
npx shadcn@latest add button
```

Import:
```tsx
import { Button } from "@/components/ui/button"
```

## Monorepo imports
```tsx
import { Button } from "@workspace/ui/components/button"
import { cn } from "@workspace/ui/lib/utils"
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/next.mdx`
