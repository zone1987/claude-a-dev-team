# Source Code

## Spinner.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { Loader2Icon } from "@lucide/vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <Loader2Icon
    role="status"
    aria-label="Loading"
    :class="cn('size-4 animate-spin', props.class)"
  />
</template>
```

## index.ts

```ts
export { default as Spinner } from "./Spinner.vue"
```

Sources:
- `registry/new-york-v4/ui/spinner/Spinner.vue`
- `registry/new-york-v4/ui/spinner/index.ts`
