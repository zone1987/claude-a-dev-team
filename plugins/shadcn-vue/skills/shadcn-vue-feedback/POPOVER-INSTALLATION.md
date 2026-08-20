# Popover — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add popover
```

## Manual

1. Install the dependencies:

```bash
npm install reka-ui @vueuse/core
```

2. Copy the following files into `src/components/ui/popover/`:
   - `Popover.vue`
   - `PopoverAnchor.vue`
   - `PopoverContent.vue`
   - `PopoverTrigger.vue`
   - `index.ts`

## Imports

```ts
import {
  Popover,
  PopoverAnchor,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
```

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/popover/index.ts`
