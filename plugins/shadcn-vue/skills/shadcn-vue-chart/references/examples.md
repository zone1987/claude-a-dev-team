# Chart — Examples

Source: `registry/bases/reka/examples/chart/`

---

## Area Chart

`ChartAreaExample.vue` — Single-series area chart with crosshair tooltip
using `VisArea` + `VisLine` + `VisAxis`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/bases/reka/ui/chart"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Example } from "@/registry/bases/reka/components/example"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  ChartContainer,
  ChartCrosshair,
  ChartTooltip,
  ChartTooltipContent,
  componentToString,
} from "@/registry/bases/reka/ui/chart"

const areaChartData = [
  { month: 1, monthLabel: "January", desktop: 186 },
  { month: 2, monthLabel: "February", desktop: 305 },
  { month: 3, monthLabel: "March", desktop: 237 },
  { month: 4, monthLabel: "April", desktop: 73 },
  { month: 5, monthLabel: "May", desktop: 209 },
  { month: 6, monthLabel: "June", desktop: 214 },
]

type Data = typeof areaChartData[number]

const areaChartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
} satisfies ChartConfig
</script>

<template>
  <Example title="Area Chart">
    <Card class="w-full">
      <CardHeader>
        <CardTitle>Area Chart</CardTitle>
        <CardDescription>
          Showing total visitors for the last 6 months
        </CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer :config="areaChartConfig">
          <VisXYContainer
            :data="areaChartData"
            :margin="{ left: 12, right: 12 }"
          >
            <VisArea
              :x="(d: Data) => d.month"
              :y="(d: Data) => d.desktop"
              :color="areaChartConfig.desktop.color"
              :opacity="0.4"
            />
            <VisLine
              :x="(d: Data) => d.month"
              :y="(d: Data) => d.desktop"
              :color="areaChartConfig.desktop.color"
              :line-width="1"
            />
            <VisAxis
              type="x"
              :x="(d: Data) => d.month"
              :tick-line="false"
              :domain-line="false"
              :grid-line="false"
              :num-ticks="6"
              :tick-format="
                (_d: number, index: number) =>
                  areaChartData[index]?.monthLabel.slice(0, 3) ?? ''
              "
            />
            <ChartTooltip />
            <ChartCrosshair
              :template="
                componentToString(areaChartConfig, ChartTooltipContent, {
                  indicator: 'line',
                  labelKey: 'monthLabel',
                })!
              "
              :color="areaChartConfig.desktop.color"
            />
          </VisXYContainer>
        </ChartContainer>
      </CardContent>
      <CardFooter>
        <div class="flex w-full items-start gap-2">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month
            </div>
            <div class="flex items-center gap-2 leading-none text-muted-foreground">
              January - June 2024
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>
  </Example>
</template>
```

---

## Bar Chart (Multiple Series)

`ChartBarExample.vue` — Grouped bar chart with two series (desktop +
mobile) using `VisGroupedBar` + dashed crosshair tooltip.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/bases/reka/ui/chart"
import { VisAxis, VisGroupedBar, VisXYContainer } from "@unovis/vue"
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Example } from "@/registry/bases/reka/components/example"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  ChartContainer,
  ChartCrosshair,
  ChartTooltip,
  ChartTooltipContent,
  componentToString,
} from "@/registry/bases/reka/ui/chart"

const barChartData = [
  { month: 1, monthLabel: "January", desktop: 186, mobile: 80 },
  { month: 2, monthLabel: "February", desktop: 305, mobile: 200 },
  { month: 3, monthLabel: "March", desktop: 237, mobile: 120 },
  { month: 4, monthLabel: "April", desktop: 73, mobile: 190 },
  { month: 5, monthLabel: "May", desktop: 209, mobile: 130 },
  { month: 6, monthLabel: "June", desktop: 214, mobile: 140 },
]

type Data = typeof barChartData[number]

const barChartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
</script>

<template>
  <Example title="Bar Chart">
    <Card class="w-full">
      <CardHeader>
        <CardTitle>Bar Chart - Multiple</CardTitle>
        <CardDescription>January - June 2024</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer :config="barChartConfig">
          <VisXYContainer :data="barChartData">
            <VisGroupedBar
              :x="(d: Data) => d.month"
              :y="[(d: Data) => d.desktop, (d: Data) => d.mobile]"
              :color="[barChartConfig.desktop.color, barChartConfig.mobile.color]"
              :rounded-corners="4"
              bar-padding="0.15"
              group-padding="0"
            />
            <VisAxis
              type="x"
              :x="(d: Data) => d.month"
              :tick-line="false"
              :domain-line="false"
              :grid-line="false"
              :num-ticks="6"
              :tick-format="
                (_d: number, index: number) =>
                  barChartData[index]?.monthLabel.slice(0, 3) ?? ''
              "
            />
            <VisAxis
              type="y"
              :num-ticks="3"
              :tick-line="false"
              :domain-line="false"
            />
            <ChartTooltip />
            <ChartCrosshair
              :template="
                componentToString(barChartConfig, ChartTooltipContent, {
                  indicator: 'dashed',
                  hideLabel: true,
                })!
              "
              color="#0000"
            />
          </VisXYContainer>
        </ChartContainer>
      </CardContent>
      <CardFooter class="flex-col items-start gap-2">
        <div class="flex gap-2 font-medium leading-none">
          Trending up by 5.2% this month
        </div>
        <div class="leading-none text-muted-foreground">
          Showing total visitors for the last 6 months
        </div>
      </CardFooter>
    </Card>
  </Example>
</template>
```

---

## Line Chart (Multiple Series)

`ChartLineExample.vue` — Multi-series line chart with `CurveType.MonotoneX`
smooth curves and per-series crosshair color.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/bases/reka/ui/chart"
import { CurveType } from "@unovis/ts"
import { VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Example } from "@/registry/bases/reka/components/example"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  ChartContainer,
  ChartCrosshair,
  ChartTooltip,
  ChartTooltipContent,
  componentToString,
} from "@/registry/bases/reka/ui/chart"

const lineChartData = [
  { month: 1, monthLabel: "January", desktop: 186, mobile: 80 },
  { month: 2, monthLabel: "February", desktop: 305, mobile: 200 },
  { month: 3, monthLabel: "March", desktop: 237, mobile: 120 },
  { month: 4, monthLabel: "April", desktop: 73, mobile: 190 },
  { month: 5, monthLabel: "May", desktop: 209, mobile: 130 },
  { month: 6, monthLabel: "June", desktop: 214, mobile: 140 },
]

type Data = typeof lineChartData[number]

const lineChartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
</script>

<template>
  <Example title="Line Chart">
    <Card class="w-full">
      <CardHeader>
        <CardTitle>Line Chart - Multiple</CardTitle>
        <CardDescription>January - June 2024</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer :config="lineChartConfig">
          <VisXYContainer
            :data="lineChartData"
            :margin="{ left: 12, right: 12 }"
          >
            <VisLine
              :x="(d: Data) => d.month"
              :y="[(d: Data) => d.desktop, (d: Data) => d.mobile]"
              :color="[lineChartConfig.desktop.color, lineChartConfig.mobile.color]"
              :curve-type="CurveType.MonotoneX"
              :line-width="2"
            />
            <VisAxis
              type="x"
              :x="(d: Data) => d.month"
              :tick-line="false"
              :domain-line="false"
              :grid-line="false"
              :num-ticks="6"
              :tick-format="
                (_d: number, index: number) =>
                  lineChartData[index]?.monthLabel.slice(0, 3) ?? ''
              "
            />
            <ChartTooltip />
            <ChartCrosshair
              :template="
                componentToString(lineChartConfig, ChartTooltipContent, {
                  labelKey: 'monthLabel',
                })!
              "
              :color="
                (d: Data, i: number) =>
                  [lineChartConfig.desktop.color,
                   lineChartConfig.mobile.color][i % 2]
              "
            />
          </VisXYContainer>
        </ChartContainer>
      </CardContent>
      <CardFooter>
        <div class="flex w-full items-start gap-2">
          <div class="grid gap-2">
            <div class="flex items-center gap-2 font-medium leading-none">
              Trending up by 5.2% this month
            </div>
            <div class="flex items-center gap-2 leading-none text-muted-foreground">
              January - June 2024
            </div>
          </div>
        </div>
      </CardFooter>
    </Card>
  </Example>
</template>
```

---

## Radial Chart (Donut)

`ChartRadialExample.vue` — Single-value donut chart with central label
using `VisDonut` + `VisSingleContainer`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/bases/reka/ui/chart"
import { Donut } from "@unovis/ts"
import { VisDonut, VisSingleContainer } from "@unovis/vue"
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Example } from "@/registry/bases/reka/components/example"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  componentToString,
} from "@/registry/bases/reka/ui/chart"

const radialChartData = [
  { browser: "safari", visitors: 1260 },
]

type Data = typeof radialChartData[number]

const radialChartConfig = {
  visitors: {
    label: "Visitors",
  },
  safari: {
    label: "Safari",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
</script>

<template>
  <Example title="Radial Chart">
    <Card class="w-full">
      <CardHeader>
        <CardTitle>Radial Chart - Shape</CardTitle>
        <CardDescription>January - June 2024</CardDescription>
      </CardHeader>
      <CardContent class="flex-1 pb-0">
        <ChartContainer
          :config="radialChartConfig"
          class="mx-auto aspect-square max-h-[210px]"
          :style="{
            '--vis-donut-central-label-font-size': 'var(--text-3xl)',
            '--vis-donut-central-label-font-weight':
              'var(--font-weight-bold)',
            '--vis-donut-central-label-text-color': 'var(--foreground)',
            '--vis-donut-central-sub-label-text-color':
              'var(--muted-foreground)',
          }"
        >
          <VisSingleContainer
            :data="radialChartData"
            :margin="{ top: 30, bottom: 30 }"
          >
            <VisDonut
              :value="(d: Data) => d.visitors"
              :color="radialChartConfig.safari.color"
              :arc-width="30"
              :central-label="
                radialChartData[0]?.visitors.toLocaleString()
              "
              central-sub-label="Visitors"
            />
            <ChartTooltip
              :triggers="{
                [Donut.selectors.segment]: componentToString(
                  radialChartConfig,
                  ChartTooltipContent,
                  { hideLabel: true },
                )!,
              }"
            />
          </VisSingleContainer>
        </ChartContainer>
      </CardContent>
      <CardFooter class="flex-col gap-2">
        <div class="flex items-center gap-2 font-medium leading-none">
          Trending up by 5.2% this month
        </div>
        <div class="leading-none text-muted-foreground">
          Showing total visitors for the last 6 months
        </div>
      </CardFooter>
    </Card>
  </Example>
</template>
```

---

## Sources

- `registry/bases/reka/examples/chart/ChartAreaExample.vue`
- `registry/bases/reka/examples/chart/ChartBarExample.vue`
- `registry/bases/reka/examples/chart/ChartLineExample.vue`
- `registry/bases/reka/examples/chart/ChartRadialExample.vue`
- `registry/new-york-v4/ui/chart/` (all source files)
- `apps/v4/content/docs/components/chart.md`
