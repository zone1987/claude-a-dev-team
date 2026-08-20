# Pagination — Beispiele

## Contents

- [Beispiel 1: Basic Pagination (PaginationBasic.vue)](#beispiel-1-basic-pagination-paginationbasicvue)
- [Beispiel 2: Simple Pagination (PaginationSimple.vue)](#beispiel-2-simple-pagination-paginationsimplevue)
- [Beispiel 3: Pagination with Select (PaginationWithSelect.vue)](#beispiel-3-pagination-with-select-paginationwithselectvue)
- [Quellen](#quellen)

## Beispiel 1: Basic Pagination (PaginationBasic.vue)

Pagination mit Previous/Next, Seitennummern und Ellipsis.

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

## Beispiel 2: Simple Pagination (PaginationSimple.vue)

Nur Seitennummern ohne Previous/Next-Buttons.

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

## Beispiel 3: Pagination with Select (PaginationWithSelect.vue)

Kombination mit einem Rows-per-Page-Select.

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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationSimple.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationWithSelect.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pagination/PaginationExample.vue`
