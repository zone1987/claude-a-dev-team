# Source

## ResizableHandle.vue

```vue
<script setup lang="ts">
import type { SplitterResizeHandleEmits, SplitterResizeHandleProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { GripVertical } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { SplitterResizeHandle, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<SplitterResizeHandleProps & { class?: HTMLAttributes["class"], withHandle?: boolean }>()
const emits = defineEmits<SplitterResizeHandleEmits>()

const delegatedProps = reactiveOmit(props, "class", "withHandle")
const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <SplitterResizeHandle
    data-slot="resizable-handle"
    v-bind="forwarded"
    :class="cn('bg-border focus-visible:ring-ring relative flex w-px items-center justify-center after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:ring-1 focus-visible:ring-offset-1 focus-visible:outline-hidden data-[orientation=vertical]:h-px data-[orientation=vertical]:w-full data-[orientation=vertical]:after:left-0 data-[orientation=vertical]:after:h-1 data-[orientation=vertical]:after:w-full data-[orientation=vertical]:after:-translate-y-1/2 data-[orientation=vertical]:after:translate-x-0 [&[data-orientation=vertical]>div]:rotate-90', props.class)"
  >
    <template v-if="props.withHandle">
      <div class="bg-border z-10 flex h-4 w-3 items-center justify-center rounded-xs border">
        <slot>
          <GripVertical class="size-2.5" />
        </slot>
      </div>
    </template>
  </SplitterResizeHandle>
</template>
```

## ResizablePanel.vue

```vue
<script setup lang="ts">
import type { SplitterPanelEmits, SplitterPanelProps } from "reka-ui"
import { SplitterPanel, useForwardExpose, useForwardPropsEmits } from "reka-ui"

const props = defineProps<SplitterPanelProps>()
const emits = defineEmits<SplitterPanelEmits>()

const forwarded = useForwardPropsEmits(props, emits)
const { forwardRef } = useForwardExpose()
</script>

<template>
  <SplitterPanel
    :ref="forwardRef"
    v-slot="slotProps"
    data-slot="resizable-panel"
    v-bind="forwarded"
  >
    <slot v-bind="slotProps" />
  </SplitterPanel>
</template>
```

## ResizablePanelGroup.vue

```vue
<script setup lang="ts">
import type { SplitterGroupEmits, SplitterGroupProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { SplitterGroup, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<SplitterGroupProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<SplitterGroupEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <SplitterGroup
    v-slot="slotProps"
    data-slot="resizable-panel-group"
    v-bind="forwarded"
    :class="cn('flex h-full w-full data-[orientation=vertical]:flex-col', props.class)"
  >
    <slot v-bind="slotProps" />
  </SplitterGroup>
</template>
```

## index.ts

```ts
export { default as ResizableHandle } from "./ResizableHandle.vue"
export { default as ResizablePanel } from "./ResizablePanel.vue"
export { default as ResizablePanelGroup } from "./ResizablePanelGroup.vue"
```
