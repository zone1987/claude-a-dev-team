# Toast — Deprecation and Migration

## Status

The `toast` component is deprecated as of shadcn/ui v4.
Use the `sonner` component instead.

## Migration Steps

1. Remove the old toast component:
   - Delete `components/ui/toast.tsx`, `components/ui/toaster.tsx`, `components/ui/use-toast.ts`
   - Remove `<Toaster />` from root layout (if it was the old toast variant)

2. Install sonner:

```bash
npx shadcn@latest add sonner
```

3. Add `<Toaster />` from sonner to root layout:

```tsx title="app/layout.tsx"
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Toaster />
      </body>
    </html>
  )
}
```

4. Replace toast calls:

```tsx
// Before (old toast)
import { useToast } from "@/hooks/use-toast"
const { toast } = useToast()
toast({ title: "Success", description: "Done" })

// After (sonner)
import { toast } from "sonner"
toast("Success", { description: "Done" })
```

## Why Sonner?

- Simpler API — just `import { toast } from "sonner"`
- No hook required
- Built-in types: success, error, info, warning, promise, loading
- Better animations and accessibility
- Active maintenance by emilkowalski

Sources: content/docs/components/radix/toast.mdx, content/docs/components/base/toast.mdx
