# shadcn/ui — React Router Installation

## Option A: Use shadcn/create
```bash
npx shadcn@latest init --preset [CODE] --template react-router
```

## Option B: CLI scaffold
```bash
npx shadcn@latest init -t react-router

# Monorepo
npx shadcn@latest init -t react-router --monorepo
```

## Option C: Existing project

### Step 1 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 2 — Add components
```bash
npx shadcn@latest add card
```

```tsx
// app/routes/home.tsx
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card"

export default function Home() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your React Router app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/react-router.mdx`
