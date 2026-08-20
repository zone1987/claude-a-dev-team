# shadcn-vue Line Charts — Vollstaendiger Quellcode

Alle 4 Line-Chart-Varianten. Alle nutzen `VisLine + VisAxis` aus `@unovis/vue`,
`CurveType` aus `@unovis/ts`.

---

## Contents

- [ChartLineDefault.vue — Natuerliche Kurve (CurveType.Natural)](#chartlinedefaultvue-natuerliche-kurve-curvetypenatural)
- [ChartLineLinear.vue — Gerade Linie (CurveType.Linear)](#chartlinelinearvue-gerade-linie-curvetypelinear)
- [ChartLineStep.vue — Treppenlinie (CurveType.Step)](#chartlinestepvue-treppenlinie-curvetypestep)
- [ChartLineInteractive.vue — Interaktiver Line Chart (aktive Linie per Button-Toggle)](#chartlineinteractivevue-interaktiver-line-chart-aktive-linie-per-button-toggle)
- [CurveType-Referenz](#curvetype-referenz)

## ChartLineDefault.vue — Natuerliche Kurve (CurveType.Natural)

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { CurveType } from "@unovis/ts"
import { VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
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
      <CardTitle>Line Chart</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent>
      <ChartContainer :config="chartConfig">
        <VisXYContainer :data="chartData" :margin="{ left: -24 }" :y-domain="[0, undefined]">
          <VisLine
            :x="(d: Data) => d.date"
            :y="(d: Data) => d.desktop"
            :color="chartConfig.desktop.color"
            :curve-type="CurveType.Natural"
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
            :color="chartConfig.desktop.color"
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

## ChartLineLinear.vue — Gerade Linie (CurveType.Linear)

Identisch mit ChartLineDefault, nur `CurveType.Linear` statt `CurveType.Natural`.

```vue
<!-- Nur der abweichende Teil: -->
<VisLine
  :x="(d: Data) => d.date"
  :y="(d: Data) => d.desktop"
  :color="chartConfig.desktop.color"
  :curve-type="CurveType.Linear"
/>
```

Vollstaendiger Code: exakt wie ChartLineDefault, Titel "Line Chart - Linear".

---

## ChartLineStep.vue — Treppenlinie (CurveType.Step)

Identisch mit ChartLineDefault, nur `CurveType.Step`.

```vue
<!-- Nur der abweichende Teil: -->
<VisLine
  :x="(d: Data) => d.date"
  :y="(d: Data) => d.desktop"
  :color="chartConfig.desktop.color"
  :curve-type="CurveType.Step"
/>
```

Vollstaendiger Code: exakt wie ChartLineDefault, Titel "Line Chart - Step".

---

## ChartLineInteractive.vue — Interaktiver Line Chart (aktive Linie per Button-Toggle)

Unterschied zu den anderen: 2 Serien (desktop + mobile), Button-Toggle im Header,
`ref(activeChart)`, `computed(total)`, `labelFormatter`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartCrosshair, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

// 90 Datenpunkte 2024-04-01 bis 2024-06-30
const chartData = [
  { date: new Date("2024-04-01"), desktop: 222, mobile: 150 },
  // ...
]

type Data = typeof chartData[number]

const chartConfig = {
  views: { label: "Page Views", color: undefined },
  desktop: { label: "Desktop", color: "var(--chart-1)" },
  mobile: { label: "Mobile", color: "var(--chart-2)" },
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
      <div class="flex flex-1 flex-col justify-center gap-1 px-6 pb-3 sm:pb-0">
        <CardTitle>Line Chart - Interactive</CardTitle>
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
          <VisLine
            :x="(d: Data) => d.date"
            :y="(d: Data) => d[activeChart as keyof typeof d]"
            :color="chartConfig[activeChart as keyof typeof chartConfig].color"
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
            :color="chartConfig.desktop.color"
          />
        </VisXYContainer>
      </ChartContainer>
    </CardContent>
  </Card>
</template>
```

## CurveType-Referenz

| Wert                  | Beschreibung          |
|-----------------------|-----------------------|
| `CurveType.Natural`   | Weiche Splines        |
| `CurveType.Linear`    | Gerade Verbindungen   |
| `CurveType.Step`      | Treppenfunktion       |
| `CurveType.StepAfter` | Stufe nach dem Punkt  |
| `CurveType.Basis`     | B-Spline              |
| `CurveType.Cardinal`  | Cardinal-Spline       |
