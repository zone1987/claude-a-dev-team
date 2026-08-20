# Pagination — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add pagination
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Die `Button`-Komponente muss vorhanden sein (Pagination nutzt `buttonVariants`):

```bash
npx shadcn-vue@latest add button
```

3. Folgende Dateien nach `src/components/ui/pagination/` kopieren:
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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/pagination/index.ts`
