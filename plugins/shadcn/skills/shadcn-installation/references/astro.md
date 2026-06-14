# shadcn/ui — Astro Installation

## Option A: Use shadcn/create
```bash
npx shadcn@latest init --preset [CODE] --template astro
```

## Option B: CLI scaffold
```bash
npx shadcn@latest init -t astro

# Monorepo
npx shadcn@latest init -t astro --monorepo
```

## Option C: Existing Astro project

### Step 1 — Add React integration (if not present)
```bash
npx astro add react
```

### Step 2 — Add Tailwind CSS
```bash
npx astro add tailwind
```

### Step 3 — Configure import alias in tsconfig.json
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

### Step 4 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 5 — Add components and use in Astro pages
```bash
npx shadcn@latest add card
```

```astro
---
import Layout from "@/layouts/main.astro"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
---

<Layout>
  <Card className="max-w-sm">
    <CardHeader>
      <CardTitle>Project Overview</CardTitle>
      <CardDescription>
        Track progress and recent activity.
      </CardDescription>
    </CardHeader>
    <CardContent>Your design system is ready.</CardContent>
  </Card>
</Layout>
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/astro.mdx`
