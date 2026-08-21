# shadcn/ui — Gatsby Installation

> Note: This guide is for Gatsby with Tailwind CSS v3. For new projects,
> prefer Next.js or Vite which support Tailwind CSS v4.

## Steps

### Step 1 — Create project
```bash
npm init gatsby
```
When prompted:
- TypeScript: Yes
- Styling: Tailwind CSS

### Step 2 — Edit tsconfig.json
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

### Step 3 — Create gatsby-node.ts
```typescript
import * as path from "path"

export const onCreateWebpackConfig = ({ actions }) => {
  actions.setWebpackConfig({
    resolve: {
      alias: {
        "@/components": path.resolve(__dirname, "src/components"),
        "@/lib/utils": path.resolve(__dirname, "src/lib/utils"),
      },
    },
  })
}
```

### Step 4 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 5 — Add components
```bash
npx shadcn@latest add button
```
```tsx
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/gatsby.mdx`
