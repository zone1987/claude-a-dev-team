# AspectRatio — Source Files

## `src/components/ui/aspect-ratio/AspectRatio.vue`

```vue
<script setup lang="ts">
import type { AspectRatioProps } from "reka-ui"
import { AspectRatio } from "reka-ui"

const props = defineProps<AspectRatioProps>()
</script>

<template>
  <AspectRatio
    v-slot="slotProps"
    data-slot="aspect-ratio"
    v-bind="props"
  >
    <slot v-bind="slotProps" />
  </AspectRatio>
</template>
```

## `src/components/ui/aspect-ratio/index.ts`

```ts
export { default as AspectRatio } from "./AspectRatio.vue"
```
