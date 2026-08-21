# Source Code

## Contents

- [Table.vue](#tablevue)
- [TableBody.vue](#tablebodyvue)
- [TableCaption.vue](#tablecaptionvue)
- [TableCell.vue](#tablecellvue)
- [TableEmpty.vue](#tableemptyvue)
- [TableFooter.vue](#tablefootervue)
- [TableHead.vue](#tableheadvue)
- [TableHeader.vue](#tableheadervue)
- [TableRow.vue](#tablerowvue)
- [utils.ts](#utilsts)
- [index.ts](#indexts)

## Table.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div data-slot="table-container" class="relative w-full overflow-auto">
    <table data-slot="table" :class="cn('w-full caption-bottom text-sm', props.class)">
      <slot />
    </table>
  </div>
</template>
```

## TableBody.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <tbody
    data-slot="table-body"
    :class="cn('[&_tr:last-child]:border-0', props.class)"
  >
    <slot />
  </tbody>
</template>
```

## TableCaption.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <caption
    data-slot="table-caption"
    :class="cn('text-muted-foreground mt-4 text-sm', props.class)"
  >
    <slot />
  </caption>
</template>
```

## TableCell.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <td
    data-slot="table-cell"
    :class="
      cn(
        'p-2 align-middle whitespace-nowrap [&:has([role=checkbox])]:pr-0 *:[[role=checkbox]]:translate-y-0.5',
        props.class,
      )
    "
  >
    <slot />
  </td>
</template>
```

## TableEmpty.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { cn } from "@/lib/utils"
import TableCell from "./TableCell.vue"
import TableRow from "./TableRow.vue"

const props = withDefaults(defineProps<{
  class?: HTMLAttributes["class"]
  colspan?: number
}>(), {
  colspan: 1,
})

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <TableRow>
    <TableCell
      :class="
        cn(
          'p-4 whitespace-nowrap align-middle text-sm text-foreground',
          props.class,
        )
      "
      v-bind="delegatedProps"
    >
      <div class="flex items-center justify-center py-10">
        <slot />
      </div>
    </TableCell>
  </TableRow>
</template>
```

## TableFooter.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <tfoot
    data-slot="table-footer"
    :class="cn('bg-muted/50 border-t font-medium [&>tr]:last:border-b-0', props.class)"
  >
    <slot />
  </tfoot>
</template>
```

## TableHead.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <th
    data-slot="table-head"
    :class="cn('text-foreground h-10 px-2 text-left align-middle font-medium whitespace-nowrap [&:has([role=checkbox])]:pr-0 *:[[role=checkbox]]:translate-y-0.5', props.class)"
  >
    <slot />
  </th>
</template>
```

## TableHeader.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <thead
    data-slot="table-header"
    :class="cn('[&_tr]:border-b', props.class)"
  >
    <slot />
  </thead>
</template>
```

## TableRow.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <tr
    data-slot="table-row"
    :class="cn('hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors', props.class)"
  >
    <slot />
  </tr>
</template>
```

## utils.ts

```ts
import type { Updater } from "@tanstack/vue-table"

import type { Ref } from "vue"
import { isFunction } from "@tanstack/vue-table"

export function valueUpdater<T>(updaterOrValue: Updater<T>, ref: Ref<T>) {
  ref.value = isFunction(updaterOrValue)
    ? updaterOrValue(ref.value)
    : updaterOrValue
}
```

## index.ts

```ts
export { default as Table } from "./Table.vue"
export { default as TableBody } from "./TableBody.vue"
export { default as TableCaption } from "./TableCaption.vue"
export { default as TableCell } from "./TableCell.vue"
export { default as TableEmpty } from "./TableEmpty.vue"
export { default as TableFooter } from "./TableFooter.vue"
export { default as TableHead } from "./TableHead.vue"
export { default as TableHeader } from "./TableHeader.vue"
export { default as TableRow } from "./TableRow.vue"
```

Sources:
- `registry/new-york-v4/ui/table/Table.vue`
- `registry/new-york-v4/ui/table/TableBody.vue`
- `registry/new-york-v4/ui/table/TableCaption.vue`
- `registry/new-york-v4/ui/table/TableCell.vue`
- `registry/new-york-v4/ui/table/TableEmpty.vue`
- `registry/new-york-v4/ui/table/TableFooter.vue`
- `registry/new-york-v4/ui/table/TableHead.vue`
- `registry/new-york-v4/ui/table/TableHeader.vue`
- `registry/new-york-v4/ui/table/TableRow.vue`
- `registry/new-york-v4/ui/table/utils.ts`
- `registry/new-york-v4/ui/table/index.ts`
