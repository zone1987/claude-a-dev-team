# Chart — Source Code

All files from `registry/new-york-v4/ui/chart/`.

---

## Contents

- [index.ts](#indexts)
- [ChartContainer.vue](#chartcontainervue)
- [ChartStyle.vue](#chartstylevue)
- [ChartLegendContent.vue](#chartlegendcontentvue)
- [ChartTooltipContent.vue](#charttooltipcontentvue)
- [utils.ts](#utilsts)

## index.ts

```ts
import type { Component, Ref } from "vue"
import { createContext } from "reka-ui"

export { default as ChartContainer } from "./ChartContainer.vue"
export { default as ChartLegendContent } from "./ChartLegendContent.vue"
export { default as ChartTooltipContent } from "./ChartTooltipContent.vue"
export { componentToString } from "./utils"

// Format: { THEME_NAME: CSS_SELECTOR }
export const THEMES = { light: "", dark: ".dark" } as const

export type ChartConfig = {
  [k in string]: {
    label?: string | Component
    icon?: string | Component
  } & (
    | { color?: string, theme?: never }
    | { color?: never, theme: Record<keyof typeof THEMES, string> }
  )
}

interface ChartContextProps {
  id: string
  config: Ref<ChartConfig>
}

export const [useChart, provideChartContext] =
  createContext<ChartContextProps>("Chart")

export { VisCrosshair as ChartCrosshair, VisTooltip as ChartTooltip }
  from "@unovis/vue"
```

---

## ChartContainer.vue

```vue
<script lang="ts">
import type { HTMLAttributes } from "vue"
import type { ChartConfig } from "."
import { useId } from "reka-ui"
import { computed, toRefs } from "vue"
import { cn } from "@/lib/utils"
import { provideChartContext } from "."
import ChartStyle from "./ChartStyle.vue"
</script>

<script setup lang="ts">
const props = defineProps<{
  id?: HTMLAttributes["id"]
  class?: HTMLAttributes["class"]
  config: ChartConfig
  cursor?: boolean
}>()

defineSlots<{
  default: {
    id: string
    config: ChartConfig
  }
}>()

const { config } = toRefs(props)
const uniqueId = useId()
const chartId = computed(() =>
  `chart-${props.id || uniqueId.replace(/:/g, "")}`)

provideChartContext({
  id: uniqueId,
  config,
})
</script>

<template>
  <div
    data-slot="chart"
    :data-chart="chartId"
    :class="cn(
      `[&_.tick_text]:!fill-muted-foreground [&_.tick_line]:!stroke-border/50
       [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border
       [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border
       [&_.recharts-radial-bar-background-sector]:fill-muted
       [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted
       [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border
       flex flex-col aspect-video justify-center text-xs
       [&_.recharts-dot[stroke='#fff']]:stroke-transparent
       [&_.recharts-layer]:outline-hidden [&_.recharts-sector]:outline-hidden
       [&_.recharts-sector[stroke='#fff']]:stroke-transparent
       [&_.recharts-surface]:outline-hidden
       [&_[data-vis-xy-container]]:h-full
       [&_[data-vis-single-container]]:h-full h-full
       [&_[data-vis-xy-container]]:w-full
       [&_[data-vis-single-container]]:w-full w-full `,
      props.class,
    )"
    :style="{
      '--vis-tooltip-padding': '0px',
      '--vis-tooltip-background-color': 'transparent',
      '--vis-tooltip-border-color': 'transparent',
      '--vis-tooltip-text-color': 'none',
      '--vis-tooltip-shadow-color': 'none',
      '--vis-tooltip-backdrop-filter': 'none',
      '--vis-crosshair-circle-stroke-color': '#0000',
      '--vis-crosshair-line-stroke-width': cursor ? '1px' : '0px',
      '--vis-font-family': 'var(--font-sans)',
    }"
  >
    <slot :id="uniqueId" :config="config" />
    <ChartStyle :id="chartId" />
  </div>
</template>
```

---

## ChartStyle.vue

Injects per-chart CSS variables for colors into a `<style>` tag using
the `Primitive` component from reka-ui.

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { Primitive } from "reka-ui"
import { computed } from "vue"
import { THEMES, useChart } from "."

defineProps<{
  id?: HTMLAttributes["id"]
}>()

const { config } = useChart()

const colorConfig = computed(() => {
  return Object.entries(config.value).filter(
    ([, config]) => config.theme || config.color,
  )
})
</script>

<template>
  <Primitive
    v-if="colorConfig.length"
    as="style"
  >
    {{ Object.entries(THEMES)
      .map(
        ([theme, prefix]) => `
${prefix} [data-chart=${id}] {
${colorConfig
  .map(([key, itemConfig]) => {
    const color
      = itemConfig.theme?.[theme as keyof typeof itemConfig.theme]
      || itemConfig.color
    return color ? `  --color-${key}: ${color};` : null
  })
        .join("\n")}
}
`,
      )
      .join("\n") }}
  </Primitive>
</template>
```

---

## ChartLegendContent.vue

Renders a legend row listing all series from the `ChartConfig`.

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { computed, onMounted, ref } from "vue"
import { cn } from "@/lib/utils"
import { useChart } from "."

const props = withDefaults(defineProps<{
  hideIcon?: boolean
  nameKey?: string
  verticalAlign?: "bottom" | "top"
  class?: HTMLAttributes["class"]
}>(), {
  verticalAlign: "bottom",
})

const { id, config } = useChart()

const payload = computed(() =>
  Object.entries(config.value).map(([key, value]) => ({
    key: props.nameKey || key,
    itemConfig: value,
  }))
)

const containerSelector = ref("")
onMounted(() => {
  containerSelector.value =
    `[data-chart="chart-${id}"]>[data-vis-xy-container]`
})
</script>

<template>
  <div
    v-if="containerSelector"
    :class="cn(
      'flex items-center justify-center gap-4',
      verticalAlign === 'top' ? 'pb-3' : 'pt-3',
      props.class,
    )"
  >
    <div
      v-for="{ key, itemConfig } in payload"
      :key="key"
      :class="cn(
        '[&>svg]:text-muted-foreground flex items-center gap-1.5' +
        ' [&>svg]:h-3 [&>svg]:w-3',
      )"
    >
      <component :is="itemConfig.icon" v-if="itemConfig.icon" />
      <div
        v-else
        class="h-2 w-2 shrink-0 rounded-xs"
        :style="{ backgroundColor: itemConfig?.color }"
      />
      {{ itemConfig.label }}
    </div>
  </div>
</template>
```

---

## ChartTooltipContent.vue

Renders a tooltip card with indicator, label and value for each series.

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { ChartConfig } from "."
import { computed } from "vue"
import { cn } from "@/lib/utils"

const props = withDefaults(defineProps<{
  hideLabel?: boolean
  hideIndicator?: boolean
  indicator?: "line" | "dot" | "dashed"
  nameKey?: string
  labelKey?: string
  labelFormatter?: (d: number | Date) => string
  payload?: Record<string, any>
  config?: ChartConfig
  class?: HTMLAttributes["class"]
  color?: string
  x?: number | Date
}>(), {
  payload: () => ({}),
  config: () => ({}),
  indicator: "dot",
})

const payload = computed(() => {
  return Object.entries(props.payload).map(([key, value]) => {
    const itemConfig = props.config[key]
    const indicatorColor =
      props.config[key]?.color ?? props.payload.fill
    return { key, value, itemConfig, indicatorColor }
  }).filter(i => i.itemConfig)
})

const nestLabel = computed(() =>
  Object.keys(props.payload).length === 1 && props.indicator !== "dot"
)

const tooltipLabel = computed(() => {
  if (props.hideLabel) return null
  if (props.labelFormatter && props.x !== undefined) {
    return props.labelFormatter(props.x)
  }
  return props.labelKey
    ? props.config[props.labelKey]?.label || props.payload[props.labelKey]
    : props.x
})
</script>

<template>
  <div
    :class="cn(
      'border-border/50 bg-background grid min-w-[8rem] items-start' +
      ' gap-1.5 rounded-lg border px-2.5 py-1.5 text-xs shadow-xl',
      props.class,
    )"
  >
    <slot>
      <div v-if="!nestLabel && tooltipLabel" class="font-medium">
        {{ tooltipLabel }}
      </div>
      <div class="grid gap-1.5">
        <div
          v-for="{ value, itemConfig, indicatorColor, key } in payload"
          :key="key"
          :class="cn(
            '[&>svg]:text-muted-foreground flex w-full flex-wrap' +
            ' items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5',
            indicator === 'dot' && 'items-center',
          )"
        >
          <component :is="itemConfig.icon" v-if="itemConfig?.icon" />
          <template v-else-if="!hideIndicator">
            <div
              :class="cn(
                'shrink-0 rounded-xs border-(--color-border)' +
                ' bg-(--color-bg)',
                {
                  'h-2.5 w-2.5': indicator === 'dot',
                  'w-1': indicator === 'line',
                  'w-0 border-[1.5px] border-dashed bg-transparent':
                    indicator === 'dashed',
                  'my-0.5': nestLabel && indicator === 'dashed',
                },
              )"
              :style="{
                '--color-bg': indicatorColor,
                '--color-border': indicatorColor,
              }"
            />
          </template>

          <div
            :class="cn(
              'flex flex-1 justify-between leading-none',
              nestLabel ? 'items-end' : 'items-center',
            )"
          >
            <div class="grid gap-1.5">
              <div v-if="nestLabel" class="font-medium">
                {{ tooltipLabel }}
              </div>
              <span class="text-muted-foreground">
                {{ itemConfig?.label || value }}
              </span>
            </div>
            <span
              v-if="value"
              class="text-foreground font-mono font-medium tabular-nums"
            >
              {{ value.toLocaleString() }}
            </span>
          </div>
        </div>
      </div>
    </slot>
  </div>
</template>
```

---

## utils.ts

`componentToString` — renders a Vue component to an HTML string for use
as the Unovis tooltip/crosshair `template` prop.

```ts
import type { ChartConfig } from "."
import { isClient } from "@vueuse/core"
import { useId } from "reka-ui"
import { h, render } from "vue"

// Simple cache using a Map to store serialized object keys
const cache = new Map<string, string>()

// Convert object to a consistent string key
function serializeKey(key: Record<string, any>): string {
  return JSON.stringify(key, Object.keys(key).sort())
}

interface Constructor<P = any> {
  __isFragment?: never
  __isTeleport?: never
  __isSuspense?: never
  new (...args: any[]): {
    $props: P
  }
}

export function componentToString<P>(
  config: ChartConfig,
  component: Constructor<P>,
  props?: P,
) {
  if (!isClient) return

  // This function will be called once during mount lifecycle
  const id = useId()

  // https://unovis.dev/docs/auxiliary/Crosshair#component-props
  return (_data: any, x: number | Date) => {
    const data = "data" in _data ? _data.data : _data
    const serializedKey = `${id}-${serializeKey(data)}`
    const cachedContent = cache.get(serializedKey)
    if (cachedContent) return cachedContent

    const vnode = h<unknown>(component, {
      ...props,
      payload: data,
      config,
      x,
    })
    const div = document.createElement("div")
    render(vnode, div)
    cache.set(serializedKey, div.innerHTML)
    return div.innerHTML
  }
}
```
