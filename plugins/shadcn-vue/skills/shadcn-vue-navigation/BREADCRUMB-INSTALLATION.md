# Breadcrumb — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add breadcrumb
```

This installs all 7 component files into `src/components/ui/breadcrumb/`.

## Manual

### 1. Install dependencies

Most sub-components only require `@lucide/vue` and the `cn()` utility.
`BreadcrumbLink` additionally uses `Primitive` from `reka-ui`:

```bash
npm install reka-ui @lucide/vue
```

### 2. Copy source files

Copy all files from the `ui/breadcrumb/` directory into your project
(e.g. `src/components/ui/breadcrumb/`).
See `references/source.md` for the complete source code.

### 3. Update import paths

Replace the registry import path with your actual component path:

```ts
// Before (registry path)
import { Breadcrumb, BreadcrumbList } from "@/registry/new-york-v4/ui/breadcrumb"

// After (your project)
import { Breadcrumb, BreadcrumbList } from "@/components/ui/breadcrumb"
```

### 4. Ensure `cn()` utility exists

The components use `cn()` from `@/lib/utils`. If it doesn't exist yet:

```bash
npm install clsx tailwind-merge
```

```ts
// src/lib/utils.ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

## Dependencies

| Package | Used by | Purpose |
|---------|---------|---------|
| `reka-ui` | `BreadcrumbLink` | `Primitive` component for polymorphic rendering / `asChild` |
| `@lucide/vue` | `BreadcrumbSeparator`, `BreadcrumbEllipsis` | `ChevronRight`, `MoreHorizontal` default icons |
| `clsx` + `tailwind-merge` | All components (via `cn()`) | Class merging utility |

> **Note:** Only `BreadcrumbLink` requires `reka-ui`. The other six components are plain Vue SFCs
> with no headless-UI dependency. If you use a dropdown inside `BreadcrumbItem`, you will also
> need the `DropdownMenu` component (which itself depends on reka-ui).

---
Source: shadcn-vue breadcrumb component
