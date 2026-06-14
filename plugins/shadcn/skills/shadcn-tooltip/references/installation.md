# Tooltip — Installation

## CLI (recommended)

```bash
npx shadcn@latest add tooltip
```

Add `TooltipProvider` to the root of your app:

```tsx title="app/layout.tsx"
import { TooltipProvider } from "@/components/ui/tooltip"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  )
}
```

## Manual

Install dependency:

```bash
npm install radix-ui
```

Copy `components/ui/tooltip.tsx` (see source.md).
Update import paths to match your project.
Add `<TooltipProvider>` to root layout as shown above.

## Usage

```tsx
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

```tsx
<Tooltip>
  <TooltipTrigger>Hover</TooltipTrigger>
  <TooltipContent>
    <p>Add to library</p>
  </TooltipContent>
</Tooltip>
```

Sources: content/docs/components/radix/tooltip.mdx
