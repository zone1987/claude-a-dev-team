# shadcn/ui — TanStack Router Installation

TanStack Router has built-in shadcn/ui support via `create-tsrouter-app`.

## Create new project with shadcn/ui included

```bash
npx create-tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn
```

## Add components
```bash
npx shadcn@latest add button
```

```tsx
// src/routes/index.tsx
import { createFileRoute } from "@tanstack/react-router"
import { Button } from "@/components/ui/button"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/tanstack-router.mdx`
