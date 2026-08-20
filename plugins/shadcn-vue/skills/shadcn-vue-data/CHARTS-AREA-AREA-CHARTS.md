# shadcn-vue Area Charts — Vollstaendiger Quellcode

Alle 4 Area-Chart-Varianten. Alle nutzen `VisXYContainer + VisArea + VisLine + VisAxis`
aus `@unovis/vue`.

---

## Contents

- [ChartAreaAxes.vue — Area mit X- und Y-Achsen](#chartareaaxesvue-area-mit-x--und-y-achsen)
- [ChartAreaGradient.vue — Area mit SVG-Gradient-Fuellung](#chartareagradientvue-area-mit-svg-gradient-fuellung)
- [ChartAreaIcons.vue — Area mit Icons in der Legende](#chartareaiconsvue-area-mit-icons-in-der-legende)
- [ChartAreaInteractive.vue — Area mit Zeitfilter (Select)](#chartareainteractivevue-area-mit-zeitfilter-select)

## ChartAreaAxes.vue — Area mit X- und Y-Achsen

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { month: 1, monthLabel: "January", desktop: 186, mobile: 80 },
  { month: 2, monthLabel: "February", desktop: 305, mobile: 200 },
  { month: 3, monthLabel: "March", desktop: 237, mobile: 120 },
  { month: 4, monthLabel: "April", desktop: 73, mobile: 190 },
  { month: 5, monthLabel: "May", desktop: 209, mobile: 130 },
  { month: 6, monthLabel: "June", desktop: 214, mobile: 140 },
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
      <CardTitle>Area Chart - Axes</CardTitle>
      <CardDescription>Showing total visitors for the last 6 months</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData">
          <VisArea
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :opacity="0.4"
          />
          <VisLine
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.mobile + d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :line-width="1"
          />
          <VisAxis
            type="x"
            :x="(d: Data) => d.month"
            :tick-line="false"
            :domain-line="false"
            :grid-line="false"
            :num-ticks="6"
            :tick-format="(d: number, index: number) => chartData[index]?.monthLabel.slice(0, 3) ?? ''"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { labelKey: 'monthLabel' })"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i % 2]"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter>
      <div class="flex w-full items-start gap-2 text-sm">
        <div class="grid gap-2">
          <div class="flex items-center gap-2 leading-none font-medium">
            Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
          </div>
          <div class="text-muted-foreground flex items-center gap-2 leading-none">
            January - June 2024
          </div>
        </div>
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartAreaGradient.vue — Area mit SVG-Gradient-Fuellung

Unterschied: `svgDefs` mit `<linearGradient>` Definitionen + `url(#fillDesktop)` als Farbe.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { month: 1, monthLabel: "January", desktop: 186, mobile: 80 },
  { month: 2, monthLabel: "February", desktop: 305, mobile: 200 },
  { month: 3, monthLabel: "March", desktop: 237, mobile: 120 },
  { month: 4, monthLabel: "April", desktop: 73, mobile: 190 },
  { month: 5, monthLabel: "May", desktop: 209, mobile: 130 },
  { month: 6, monthLabel: "June", desktop: 214, mobile: 140 },
]

type Data = typeof chartData[number]

const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" },
  mobile: { label: "Mobile", color: "var(--chart-2)" },
} satisfies ChartConfig

const svgDefs = `
  <linearGradient id="fillDesktop" x1="0" y1="0" x2="0" y2="1">
    <stop offset="5%" stop-color="var(--color-desktop)" stop-opacity="0.8" />
    <stop offset="95%" stop-color="var(--color-desktop)" stop-opacity="0.1" />
  </linearGradient>
  <linearGradient id="fillMobile" x1="0" y1="0" x2="0" y2="1">
    <stop offset="5%" stop-color="var(--color-mobile)" stop-opacity="0.8" />
    <stop offset="95%" stop-color="var(--color-mobile)" stop-opacity="0.1" />
  </linearGradient>
`
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Area Chart - Gradient</CardTitle>
      <CardDescription>Showing total visitors for the last 6 months</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData" :svg-defs="svgDefs">
          <VisArea
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.desktop]"
            :color="(d: Data, i: number) => ['url(#fillMobile)', 'url(#fillDesktop)'][i]"
            :opacity="0.4"
          />
          <VisLine
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.mobile + d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :line-width="1"
          />
          <VisAxis
            type="x"
            :x="(d: Data) => d.month"
            :tick-line="false" :domain-line="false" :grid-line="false"
            :num-ticks="6"
            :tick-format="(d: number, index: number) => chartData[index]?.monthLabel.slice(0, 3) ?? ''"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false"
            :tick-format="(d: number, index: number) => ''" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { labelKey: 'monthLabel' })"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i % 2]"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter>
      <div class="flex w-full items-start gap-2 text-sm">
        <div class="grid gap-2">
          <div class="flex items-center gap-2 leading-none font-medium">
            Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
          </div>
          <div class="text-muted-foreground flex items-center gap-2 leading-none">
            January - June 2024
          </div>
        </div>
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartAreaIcons.vue — Area mit Icons in der Legende

Unterschied: ChartConfig enthaelt `icon: TrendingUp` / `icon: TrendingDown` + `ChartLegendContent`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingDown, TrendingUp } from "@lucide/vue"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartLegendContent, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { month: 1, monthLabel: "January", desktop: 186, mobile: 80 },
  { month: 2, monthLabel: "February", desktop: 305, mobile: 200 },
  { month: 3, monthLabel: "March", desktop: 237, mobile: 120 },
  { month: 4, monthLabel: "April", desktop: 73, mobile: 190 },
  { month: 5, monthLabel: "May", desktop: 209, mobile: 130 },
  { month: 6, monthLabel: "June", desktop: 214, mobile: 140 },
]

type Data = typeof chartData[number]

const chartConfig = {
  mobile: { label: "Mobile", color: "var(--chart-2)", icon: TrendingUp },
  desktop: { label: "Desktop", color: "var(--chart-1)", icon: TrendingDown },
} satisfies ChartConfig
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Area Chart - Icons</CardTitle>
      <CardDescription>Showing total visitors for the last 6 months</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData" :margin="{ top: 10, bottom: 10 }">
          <VisArea
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :opacity="0.4"
          />
          <VisLine
            :x="(d: Data) => d.month"
            :y="[(d: Data) => d.mobile, (d: Data) => d.mobile + d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :line-width="1"
          />
          <VisAxis
            type="x" :x="(d: Data) => d.month"
            :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
            :tick-format="(d: number, index: number) => chartData[index]?.monthLabel.slice(0, 3) ?? ''"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false"
            :tick-format="(d: number, index: number) => ''" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, { labelKey: 'monthLabel', indicator: 'line' })"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i % 2]"
          />
        </VisXYContainer>

        <ChartLegendContent />
      </ChartContainer>
    </CardContent>
    <CardFooter>
      <div class="flex w-full items-start gap-2 text-sm">
        <div class="grid gap-2">
          <div class="flex items-center gap-2 leading-none font-medium">
            Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
          </div>
          <div class="text-muted-foreground flex items-center gap-2 leading-none">
            January - June 2024
          </div>
        </div>
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## ChartAreaInteractive.vue — Area mit Zeitfilter (Select)

Unterschied: 90 Datenpunkte (Date-Objekte), `ref(timeRange)`, `computed(filterRange)`,
`Select`-Dropdown, `labelFormatter` im Tooltip, Gradient-Fuellung.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartLegendContent, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/registry/new-york-v4/ui/select"

const chartData = [
  { date: new Date("2024-04-01"), desktop: 222, mobile: 150 },
  { date: new Date("2024-04-02"), desktop: 97, mobile: 180 },
  // ... 90 Datenpunkte bis 2024-06-30
]

type Data = typeof chartData[number]

const chartConfig = {
  mobile: { label: "Mobile", color: "var(--chart-2)" },
  desktop: { label: "Desktop", color: "var(--chart-1)" },
} satisfies ChartConfig

const svgDefs = `
  <linearGradient id="fillDesktop" x1="0" y1="0" x2="0" y2="1">
    <stop offset="5%" stop-color="var(--color-desktop)" stop-opacity="0.8" />
    <stop offset="95%" stop-color="var(--color-desktop)" stop-opacity="0.1" />
  </linearGradient>
  <linearGradient id="fillMobile" x1="0" y1="0" x2="0" y2="1">
    <stop offset="5%" stop-color="var(--color-mobile)" stop-opacity="0.8" />
    <stop offset="95%" stop-color="var(--color-mobile)" stop-opacity="0.1" />
  </linearGradient>
`

const timeRange = ref("90d")
const filterRange = computed(() => {
  return chartData.filter((item) => {
    const date = new Date(item.date)
    const referenceDate = new Date("2024-06-30")
    let daysToSubtract = 90
    if (timeRange.value === "30d") daysToSubtract = 30
    else if (timeRange.value === "7d") daysToSubtract = 7
    const startDate = new Date(referenceDate)
    startDate.setDate(startDate.getDate() - daysToSubtract)
    return date >= startDate
  })
})
</script>

<template>
  <Card class="pt-0">
    <CardHeader class="flex items-center gap-2 space-y-0 border-b py-5 sm:flex-row">
      <div class="grid flex-1 gap-1">
        <CardTitle>Area Chart - Interactive</CardTitle>
        <CardDescription>Showing total visitors for the last 3 months</CardDescription>
      </div>
      <Select v-model="timeRange">
        <SelectTrigger class="hidden w-[160px] rounded-lg sm:ml-auto sm:flex" aria-label="Select a value">
          <SelectValue placeholder="Last 3 months" />
        </SelectTrigger>
        <SelectContent class="rounded-xl">
          <SelectItem value="90d" class="rounded-lg">Last 3 months</SelectItem>
          <SelectItem value="30d" class="rounded-lg">Last 30 days</SelectItem>
          <SelectItem value="7d" class="rounded-lg">Last 7 days</SelectItem>
        </SelectContent>
      </Select>
    </CardHeader>
    <CardContent class="px-2 pt-4 sm:px-6 sm:pt-6 pb-4">
      <ChartContainer :config="chartConfig" class="aspect-auto h-[250px] w-full" :cursor="false">
        <VisXYContainer :data="filterRange" :svg-defs="svgDefs" :margin="{ left: -40 }" :y-domain="[0, 1200]">
          <VisArea
            :x="(d: Data) => d.date"
            :y="[(d: Data) => d.mobile, (d: Data) => d.desktop]"
            :color="(d: Data, i: number) => ['url(#fillMobile)', 'url(#fillDesktop)'][i]"
            :opacity="0.6"
          />
          <VisLine
            :x="(d: Data) => d.date"
            :y="[(d: Data) => d.mobile, (d: Data) => d.mobile + d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :line-width="1"
          />
          <VisAxis
            type="x" :x="(d: Data) => d.date"
            :tick-line="false" :domain-line="false" :grid-line="false" :num-ticks="6"
            :tick-format="(d: number, index: number) => {
              const date = new Date(d)
              return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
            }"
          />
          <VisAxis type="y" :num-ticks="3" :tick-line="false" :domain-line="false" />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, {
              labelFormatter: (d) => new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
            })"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i % 2]"
          />
        </VisXYContainer>

        <ChartLegendContent />
      </ChartContainer>
    </CardContent>
  </Card>
</template>
```
