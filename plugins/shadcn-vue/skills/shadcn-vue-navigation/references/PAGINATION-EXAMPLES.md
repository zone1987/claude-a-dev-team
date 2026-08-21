# Pagination — Examples

## Contents

- [Example 1: Basic Pagination (PaginationBasic.vue)](#example-1-basic-pagination-paginationbasicvue)
- [Example 2: Simple Pagination (PaginationSimple.vue)](#example-2-simple-pagination-paginationsimplevue)
- [Example 3: Pagination with Select (PaginationWithSelect.vue)](#example-3-pagination-with-select-paginationwithselectvue)
- [Sources](#sources)

## Example 1: Basic Pagination (PaginationBasic.vue)

Pagination with Previous/Next, page numbers and ellipsis.

```vue
<script setup lang="ts">
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
</script>

<template>
  <Pagination>
    <PaginationContent>
      <PaginationItem>
        <PaginationPrevious href="#" />
      </PaginationItem>
      <PaginationItem :value="1">
        1
      </PaginationItem>
      <PaginationItem :value="2" :is-active="true">
        2
      </PaginationItem>
      <PaginationItem :value="3">
        3
      </PaginationItem>
      <PaginationEllipsis :index="0" />
      <PaginationItem>
        <PaginationNext href="#" />
      </PaginationItem>
    </PaginationContent>
  </Pagination>
</template>
```

---

## Example 2: Simple Pagination (PaginationSimple.vue)

Page numbers only, without Previous/Next buttons.

```vue
<script setup lang="ts">
import {
  Pagination,
  PaginationContent,
  PaginationItem,
} from "@/components/ui/pagination"
</script>

<template>
  <Pagination>
    <PaginationContent>
      <PaginationItem :value="1">1</PaginationItem>
      <PaginationItem :value="2" :is-active="true">2</PaginationItem>
      <PaginationItem :value="3">3</PaginationItem>
      <PaginationItem :value="4">4</PaginationItem>
      <PaginationItem :value="5">5</PaginationItem>
    </PaginationContent>
  </Pagination>
</template>
```

---

## Example 3: Pagination with Select (PaginationWithSelect.vue)

Combined with a rows-per-page select.

```vue
<script setup lang="ts">
import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
</script>

<template>
  <div class="flex items-center justify-between gap-4">
    <div class="flex items-center gap-2">
      <label for="select-rows-per-page" class="text-sm">Rows per page</label>
      <Select default-value="25">
        <SelectTrigger id="select-rows-per-page" class="w-20">
          <SelectValue />
        </SelectTrigger>
        <SelectContent align="start">
          <SelectGroup>
            <SelectItem value="10">10</SelectItem>
            <SelectItem value="25">25</SelectItem>
            <SelectItem value="50">50</SelectItem>
            <SelectItem value="100">100</SelectItem>
          </SelectGroup>
        </SelectContent>
      </Select>
    </div>
    <Pagination class="mx-0 w-auto">
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious href="#" />
        </PaginationItem>
        <PaginationItem>
          <PaginationNext href="#" />
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  </div>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationSimple.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationWithSelect.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationExample.vue`
