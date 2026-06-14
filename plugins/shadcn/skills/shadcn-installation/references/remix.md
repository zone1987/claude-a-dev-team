# shadcn/ui — Remix Installation

> Note: For React Router v7+, see [react-router.md](react-router.md).

## Steps

### Step 1 — Create project
```bash
npx create-remix@latest my-app
```

### Step 2 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 3 — Add components
```bash
npx shadcn@latest add button
```

Import (uses `~` alias by Remix convention):
```tsx
import { Button } from "~/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/remix.mdx`
