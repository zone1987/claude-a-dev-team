# Tabs — Installation

## CLI (recommended)

```bash
npx shadcn@latest add tabs
```

## Manual

Install dependency:

```bash
npm install radix-ui
```

Copy `components/ui/tabs.tsx` (see source.md).
Update import paths to match your project.

## Usage

```tsx
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

```tsx
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">Make changes to your account here.</TabsContent>
  <TabsContent value="password">Change your password here.</TabsContent>
</Tabs>
```

Sources: content/docs/components/radix/tabs.mdx
