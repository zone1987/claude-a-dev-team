# shadcn-vue Installation: Astro

## Step 1: Create project

```bash
npx create-astro@latest astro-app --template with-tailwindcss --install --add vue --git
```

## Step 2: Edit tsconfig.json

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

## Step 3: Run the CLI

```bash
npx shadcn-vue@latest init
```

## Step 4: Add Components

```bash
npx shadcn-vue@latest add button
```

Usage in `.astro` files:

```astro
---
import { Button } from "@/components/ui/button"
---

<html lang="en">
  <head>
    <title>Astro</title>
  </head>
  <body>
    <Button>Hello World</Button>
  </body>
</html>
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/installation/03.astro.md`
