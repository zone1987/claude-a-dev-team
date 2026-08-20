# shadcn-vue Chart Tooltips — Complete source code

All 7 tooltip variants. All use `VisStackedBar + VisAxis` from `@unovis/vue` as
the host chart. Tooltip via `ChartCrosshair :template + componentToString`.

---

## Contents

- [Structure shared by all tooltip examples](#structure-shared-by-all-tooltip-examples)
- [ChartTooltipDefault.vue — Default tooltip with labelFormatter](#charttooltipdefaultvue--default-tooltip-with-labelformatter)
- [ChartTooltipIcons.vue — Tooltip with icons](#charttooltipiconsvue--tooltip-with-icons)
- [ChartTooltipIndicatorLine.vue — Line indicator instead of dot](#charttooltipindicatorlinevue--line-indicator-instead-of-dot)
- [ChartTooltipIndicatorNone.vue — No indicator](#charttooltipindicatornonevue--no-indicator)
- [ChartTooltipLabelCustom.vue — Custom label from ChartConfig](#charttooltiplabelcustomvue--custom-label-from-chartconfig)
- [ChartTooltipLabelFormatter.vue — Label formatter (long date)](#charttooltiplabelformattervue--label-formatter-long-date)
- [ChartTooltipLabelNone.vue — No label, no indicator](#charttooltiplabelnonevue--no-label-no-indicator)
- [ChartTooltipContent props — overview](#charttooltipcontent-props--overview)
- [componentToString — signature](#componenttostring--signature)

## Structure shared by all tooltip examples

```vue
<!-- Same data set in all 7 examples -->
const chartData = [
  { date: new Date("2024-07-15"), running: 450, swimming: 300 },
  { date: new Date("2024-07-16"), running: 380, swimming: 420 },
  { date: new Date("2024-07-17"), running: 520, swimming: 120 },
  { date: new Date("2024-07-18"), running: 140, swimming: 550 },
  { date: new Date("2024-07-19"), running: 600, swimming: 350 },
  { date: new Date("2024-07-20"), running: 480, swimming: 400 },
]

<!-- Shared VisXYContainer template -->
<VisXYContainer :data="chartData" :padding="{ top: 10, bottom: 10, left: 10, right: 10 }">
  <VisStackedBar
    :x="(d: Data) => d.date"
    :y="[(d: Data) => d.running, (d: Data) => d.swimming]"
    :color="[chartConfig.running.color, chartConfig.swimming.color]"
    :rounded-corners="4"
    :bar-padding="0.1"
  />
  <VisAxis
    type="x" :x="(d: Data) => d.date"
    :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
    :tick-format="(d: number) => new Date(d).toLocaleDateString('en-US', { weekday: 'short' })"
    :tick-values="chartData.map(d => d.date)"
  />
  <ChartTooltip />
  <ChartCrosshair
    :template="/* VARIES per example */"
    color="#0000"
  />
</VisXYContainer>
```

---

## ChartTooltipDefault.vue — Default tooltip with labelFormatter

`indicator: "dot"` (default), date as label via `labelFormatter`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { VisAxis, VisStackedBar, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { date: new Date("2024-07-15"), running: 450, swimming: 300 },
  { date: new Date("2024-07-16"), running: 380, swimming: 420 },
  { date: new Date("2024-07-17"), running: 520, swimming: 120 },
  { date: new Date("2024-07-18"), running: 140, swimming: 550 },
  { date: new Date("2024-07-19"), running: 600, swimming: 350 },
  { date: new Date("2024-07-20"), running: 480, swimming: 400 },
]
type Data = typeof chartData[number]

const chartConfig = {
  running: { label: "Running", color: "var(--chart-1)" },
  swimming: { label: "Swimming", color: "var(--chart-2)" },
} satisfies ChartConfig
</script>

<template>
  <!-- ... card wrapper ... -->
  <ChartCrosshair
    :template="componentToString(chartConfig, ChartTooltipContent, {
      labelFormatter(d) {
        const date = new Date(d)
        return date.toLocaleDateString('sv-SE')
      } })"
    color="#0000"
  />
</template>
```

---

## ChartTooltipIcons.vue — Tooltip with icons

ChartConfig has `icon: Footprints` / `icon: Waves`. `hideLabel: true` hides the date.

```vue
import { Footprints, Waves } from "@lucide/vue"

const chartConfig = {
  running: { label: "Running", color: "var(--chart-1)", icon: Footprints },
  swimming: { label: "Swimming", color: "var(--chart-2)", icon: Waves },
} satisfies ChartConfig

<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })"
  color="#0000"
/>
```

---

## ChartTooltipIndicatorLine.vue — Line indicator instead of dot

`indicator: 'line'` shows a vertical color stripe instead of the dot.

```vue
<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    indicator: 'line',
    labelFormatter(d) {
      return new Date(d).toLocaleDateString('sv-SE')
    } })"
  color="#0000"
/>
```

---

## ChartTooltipIndicatorNone.vue — No indicator

`hideIndicator: true` hides the color indicator entirely.

```vue
<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    hideIndicator: true,
    labelFormatter(d) {
      return new Date(d).toLocaleDateString('sv-SE')
    } })"
  color="#0000"
/>
```

---

## ChartTooltipLabelCustom.vue — Custom label from ChartConfig

`labelKey: 'activities'` reads the label from `chartConfig.activities.label`.

```vue
const chartConfig = {
  activities: { label: "Activities" },  // <-- used as the tooltip label
  running: { label: "Running", color: "var(--chart-1)" },
  swimming: { label: "Swimming", color: "var(--chart-2)" },
} satisfies ChartConfig

<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    indicator: 'line',
    labelKey: 'activities',
  })"
  color="#0000"
/>
```

---

## ChartTooltipLabelFormatter.vue — Label formatter (long date)

Formatted as "15 July 2024".

```vue
<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    labelFormatter(d) {
      const date = new Date(d)
      return date.toLocaleDateString('en-US', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      })
    } })"
  color="#0000"
/>
```

---

## ChartTooltipLabelNone.vue — No label, no indicator

`hideLabel: true` + `hideIndicator: true` = just the values, no decoration.

```vue
<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    hideLabel: true,
    hideIndicator: true,
    labelFormatter(d) {
      return new Date(d).toLocaleDateString('sv-SE')
    },
  })"
  color="#0000"
/>
```

---

## ChartTooltipContent props — overview

| Prop             | Type                             | Default  | Effect                                       |
|------------------|----------------------------------|----------|----------------------------------------------|
| `hideLabel`      | `boolean`                        | `false`  | Hide the top label row                       |
| `hideIndicator`  | `boolean`                        | `false`  | Hide the color indicator (dot/line)          |
| `indicator`      | `"line" \| "dot" \| "dashed"`    | `"dot"`  | Shape of the color indicator                 |
| `labelKey`       | `string`                         | –        | ChartConfig key whose `.label` is shown      |
| `labelFormatter` | `(d: number \| Date) => string`  | –        | Formatter for the X label                   |
| `nameKey`        | `string`                         | –        | Key for the row names                        |
| `payload`        | `Record<string, any>`            | `{}`     | Data point (automatic from componentToString) |
| `config`         | `ChartConfig`                    | `{}`     | Chart configuration                          |
| `x`              | `number \| Date`                 | –        | X value for labelFormatter                  |

## componentToString — signature

```ts
componentToString(
  config: ChartConfig,
  component: Constructor,     // ChartTooltipContent
  props?: Partial<ChartTooltipContentProps>
): ((_data: any, x: number | Date) => string) | undefined
```

Returns a callback function of the kind `ChartCrosshair :template` expects.
Renders the Vue component to an HTML string (with caching).
