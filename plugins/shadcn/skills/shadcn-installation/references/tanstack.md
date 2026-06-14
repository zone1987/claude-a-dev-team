# shadcn/ui — TanStack Start Installation

## Option A: Use shadcn/create
```bash
npx shadcn@latest init --preset [CODE] --template start
```

## Option B: CLI scaffold
```bash
npx shadcn@latest init -t start

# Monorepo
npx shadcn@latest init -t start --monorepo
```

## Option C: Existing TanStack Start project

### Run the CLI
```bash
npx shadcn@latest init
```

### Add components
```bash
npx shadcn@latest add card
```

```tsx
// src/routes/index.tsx
import { createFileRoute } from "@tanstack/react-router"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your TanStack Start app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/tanstack.mdx`
