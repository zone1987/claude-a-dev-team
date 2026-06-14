# Spinner — Installation

## CLI (recommended)

```bash
npx shadcn@latest add spinner
```

## Manual

Copy component to `components/ui/spinner.tsx`. No external dependencies beyond `lucide-react`.

## Usage

```tsx
import { Spinner } from "@/components/ui/spinner"
```

```tsx
<Spinner />
```

## In a button (loading state)

```tsx
<Button disabled>
  <Spinner />
  Loading...
</Button>
```

## Custom spinner icon

Replace `Loader2Icon` with any icon from lucide-react:

```tsx title="components/ui/spinner.tsx"
import { LoaderIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <LoaderIcon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }
```

## Source files

- `content/docs/components/base/spinner.mdx`
