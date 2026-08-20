# shadcn-vue Bar Charts — Vollstaendiger Quellcode

Alle 4 Bar-Chart-Varianten. Alle nutzen `VisGroupedBar + VisAxis` aus `@unovis/vue`.

---

## Contents

- [ChartBarDefault.vue — Einfacher Bar Chart](#chartbardefaultvue-einfacher-bar-chart)
- [ChartBarHorizontal.vue — Horizontaler Bar Chart](#chartbarhorizontalvue-horizontaler-bar-chart)
- [ChartBarMultiple.vue — Gruppierter Bar Chart (mehrere Serien)](#chartbarmultiplevue-gruppierter-bar-chart-mehrere-serien)
- [ChartBarInteractive.vue — Interaktiver Bar Chart (aktive Spalte per Button)](#chartbarinteractivevue-interaktiver-bar-chart-aktive-spalte-per-button)

## ChartBarDefault.vue — Einfacher Bar Chart

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { VisAxis, VisGroupedBar, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { date: new Date("2024-01-01"), desktop: 186 },
  { date: new Date("2024-02-01"), desktop: 305 },
  { date: new Date("2024-03-01"), desktop: 237 },
  { date: new Date("2024-04-01"), desktop: 73 },
  { date: new Date("2024-05-01"), desktop: 209 },
  { date: new Date("2024-06-01"), desktop: 214 },
]

type Data = typeof chartData[number]

const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" },
} satisfies ChartConfig
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Bar Chart</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData" :margin="{ left: -24 }" :y-domain="[0, undefined]">
          <VisGroupedBar
            :x="(d: Data) => d.date"
            :y="(d: Data) => d.desktop"
            :color="chartConfig.desktop.color"
            :rounded-corners="10"
          />
          <VisAxis
            type="x" :x="(d: Data) => d.date"
            :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
            :tick-format="(d: number) => new Date(d).toLocaleDateString('en-US', { month: 'short' })"
            :tick-values="chartData.map(d => d.date)"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })"
            color="#0000"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col items-start gap-2 text-sm">
      <div class="flex gap-2 font-medium leading-none">
        Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
      </div>
      <div class="leading-none text-muted-foreground">
        Showing total visitors for the last 6 months
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartBarHorizontal.vue — Horizontaler Bar Chart

Unterschied: `Orientation.Horizontal` aus `@unovis/ts`, X-Achse wird zur Y-Achse.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { Orientation } from "@unovis/ts"
import { VisAxis, VisGroupedBar, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { date: new Date("2024-01-01"), desktop: 186 },
  { date: new Date("2024-02-01"), desktop: 305 },
  { date: new Date("2024-03-01"), desktop: 237 },
  { date: new Date("2024-04-01"), desktop: 73 },
  { date: new Date("2024-05-01"), desktop: 209 },
  { date: new Date("2024-06-01"), desktop: 214 },
]

type Data = typeof chartData[number]

const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" },
} satisfies ChartConfig
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Bar Chart - Horizontal</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData">
          <VisGroupedBar
            :x="(d: Data) => d.date"
            :y="(d: Data) => d.desktop"
            :color="chartConfig.desktop.color"
            :rounded-corners="5"
            :orientation="Orientation.Horizontal"
          />
          <VisAxis
            type="y"
            :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
            :tick-format="(d: number) => new Date(d).toLocaleDateString('en-US', { month: 'short' })"
            :tick-values="chartData.map(d => d.date)"
          />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })"
            color="#0000"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col items-start gap-2 text-sm">
      <div class="flex gap-2 font-medium leading-none">
        Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
      </div>
      <div class="leading-none text-muted-foreground">
        Showing total visitors for the last 6 months
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartBarMultiple.vue — Gruppierter Bar Chart (mehrere Serien)

Unterschied: `:y` als Array, `:color` als Array, `bar-padding`, `group-padding`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { VisAxis, VisGroupedBar, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { date: new Date("2024-01-01"), desktop: 186, mobile: 80 },
  { date: new Date("2024-02-01"), desktop: 305, mobile: 200 },
  { date: new Date("2024-03-01"), desktop: 237, mobile: 120 },
  { date: new Date("2024-04-01"), desktop: 73, mobile: 190 },
  { date: new Date("2024-05-01"), desktop: 209, mobile: 130 },
  { date: new Date("2024-06-01"), desktop: 214, mobile: 140 },
]

type Data = typeof chartData[number]

const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" },
  mobile: { label: "Mobile", color: "var(--chart-2)" },
} satisfies ChartConfig
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Bar Chart - Multiple</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData">
          <VisGroupedBar
            :x="(d: Data) => d.date"
            :y="[(d: Data) => d.desktop, (d: Data) => d.mobile]"
            :color="[chartConfig.desktop.color, chartConfig.mobile.color]"
            :rounded-corners="4"
            bar-padding="0.15"
            group-padding="0"
          />
          <VisAxis
            type="x" :x="(d: Data) => d.date"
            :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
            :tick-format="(d: number) => new Date(d).toLocaleDateString('en-US', { month: 'short' })"
            :tick-values="chartData.map(d => d.date)"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { indicator: 'dashed', hideLabel: true })"
            color="#0000"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col items-start gap-2 text-sm">
      <div class="flex gap-2 font-medium leading-none">
        Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
      </div>
      <div class="leading-none text-muted-foreground">
        Showing total visitors for the last 6 months
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartBarInteractive.vue — Interaktiver Bar Chart (aktive Spalte per Button)

Unterschied: `ref(activeChart)`, `computed(total)`, Button-Toggle im Card-Header,
`labelFormatter` im Tooltip.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { VisAxis, VisGroupedBar, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

// 90 Datenpunkte von 2024-04-01 bis 2024-06-30
const chartData = [
  { date: new Date("2024-04-01"), desktop: 222, mobile: 150 },
  // ...
]

type Data = typeof chartData[number]

const chartConfig = {
  views: { label: "Page Views", color: undefined },
  desktop: { label: "Desktop", color: "var(--chart-2)" },
  mobile: { label: "Mobile", color: "var(--chart-1)" },
} satisfies ChartConfig

const activeChart = ref("desktop")
const total = computed(() => ({
  desktop: chartData.reduce((acc, curr) => acc + curr.desktop, 0),
  mobile: chartData.reduce((acc, curr) => acc + curr.mobile, 0),
}))
</script>

<template>
  <Card class="py-4 sm:py-0">
    <CardHeader class="flex flex-col items-stretch border-b !p-0 sm:flex-row">
      <div class="flex flex-1 flex-col justify-center gap-1 px-6 py-5 sm:py-6">
        <CardTitle>Bar Chart - Interactive</CardTitle>
        <CardDescription>Showing total visitors for the last 3 months</CardDescription>
      </div>
      <div class="flex">
        <button
          v-for="chart in ['desktop', 'mobile'] as (keyof typeof chartConfig)[]"
          :key="chart"
          :data-active="activeChart === chart"
          class="data-[active=true]:bg-muted/50 flex flex-1 flex-col justify-center gap-1 border-t px-6 py-4 text-left even:border-l sm:border-t-0 sm:border-l sm:px-8 sm:py-6"
          @click="activeChart = chart"
        >
          <span class="text-muted-foreground text-xs">{{ chartConfig[chart].label }}</span>
          <span class="text-lg leading-none font-bold sm:text-3xl">
            {{ total[chart as keyof typeof total].toLocaleString() }}
          </span>
        </button>
      </div>
    </CardHeader>
    <CardContent class="px-2 sm:p-6">
      <ChartContainer :config="chartConfig" class="aspect-auto h-[250px] w-full" cursor>
        <VisXYContainer :data="chartData" :margin="{ left: -24 }" :y-domain="[0, undefined]">
          <VisGroupedBar
            :x="(d: Data) => d.date"
            :y="(d: Data) => d[activeChart as keyof typeof d]"
            :color="chartConfig[activeChart as keyof typeof chartConfig].color"
            :bar-padding="0.1"
            :rounded-corners="false"
          />
          <VisAxis
            type="x" :x="(d: Data) => d.date"
            :tick-line="false" :domain-line="false" :grid-line="false"
            :tick-format="(d: number) => new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, {
              labelFormatter(d) {
                return new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
              },
            })"
            color="#0000"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
  </Card>
</template>
```
