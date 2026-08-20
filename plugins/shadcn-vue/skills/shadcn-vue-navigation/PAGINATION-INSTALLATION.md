# Pagination — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add pagination
```

## Manual

1. Install dependencies:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. The `Button` component must be present (Pagination uses `buttonVariants`):

```bash
npx shadcn-vue@latest add button
```

3. Copy the following files to `src/components/ui/pagination/`:
   - `Pagination.vue`
   - `PaginationContent.vue`
   - `PaginationEllipsis.vue`
   - `PaginationFirst.vue`
   - `PaginationItem.vue`
   - `PaginationLast.vue`
   - `PaginationNext.vue`
   - `PaginationPrevious.vue`
   - `index.ts`

## Imports

```ts
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationFirst,
  PaginationItem,
  PaginationLast,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/pagination/index.ts`
