# shadcn-vue Pie / Donut Charts — Complete source code

All 4 variants. They use `VisDonut + VisSingleContainer` from `@unovis/vue` and
`Donut` from `@unovis/ts`. Tooltip via `ChartTooltip :triggers` (no ChartCrosshair!).

---

## Contents

- [ChartPieSimple.vue — Simple pie chart (arc-width=0)](#chartpiesimplevue--simple-pie-chart-arc-width0)
- [ChartPieDonut.vue — Donut chart (arc-width=30)](#chartpiedonutvue--donut-chart-arc-width30)
- [ChartPieDonutText.vue — Donut with a number in the center](#chartpiedonuttextvue--donut-with-a-number-in-the-center)
- [ChartPieStacked.vue — Stacked donuts (2 concentric rings)](#chartpiestackedvue--stacked-donuts-2-concentric-rings)
- [Important VisDonut props](#important-visdonut-props)

## ChartPieSimple.vue — Simple pie chart (arc-width=0)

`arc-width: 0` = full circle (no donut hole).

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { Donut } from "@unovis/ts"
import { VisDonut, VisSingleContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
  { browser: "firefox", visitors: 187, fill: "var(--color-firefox)" },
  { browser: "edge", visitors: 173, fill: "var(--color-edge)" },
  { browser: "other", visitors: 90, fill: "var(--color-other)" },
]
type Data = typeof chartData[number]

const chartConfig = {
  visitors: { label: "Visitors", color: undefined },
  chrome: { label: "Chrome", color: "var(--chart-1)" },
  safari: { label: "Safari", color: "var(--chart-2)" },
  firefox: { label: "Firefox", color: "var(--chart-3)" },
  edge: { label: "Edge", color: "var(--chart-4)" },
  other: { label: "Other", color: "var(--chart-5)" },
} satisfies ChartConfig
</script>

<template>
  <Card class="flex flex-col">
    <CardHeader class="items-center pb-0">
      <CardTitle>Pie Chart</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent class="flex-1 pb-0">
      <ChartContainer :config="chartConfig" class="mx-auto aspect-square max-h-[250px]">
        <VisSingleContainer :data="chartData" :margin="{ top: 30, bottom: 30 }">
          <VisDonut
            :value="(d: Data) => d.visitors"
            :color="(d: Data) => chartConfig[d.browser as keyof typeof chartConfig].color"
            :arc-width="0"
          />
          <ChartTooltip
            :triggers="{
              [Donut.selectors.segment]: componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })!,
            }"
          />
        </VisSingleContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col gap-2 text-sm">
      <div class="flex items-center gap-2 font-medium leading-none">
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

## ChartPieDonut.vue — Donut chart (arc-width=30)

Identical to ChartPieSimple, only `arc-width: 30` instead of `0`.

```vue
<VisDonut
  :value="(d: Data) => d.visitors"
  :color="(d: Data) => chartConfig[d.browser as keyof typeof chartConfig].color"
  :arc-width="30"
/>
```

---

## ChartPieDonutText.vue — Donut with a number in the center

Difference: `computed(totalVisitors)`, CSS vars for font size/color of the center caption,
`central-label` and `central-sub-label` props on `VisDonut`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { Donut } from "@unovis/ts"
import { VisDonut, VisSingleContainer } from "@unovis/vue"
import { computed } from "vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
  { browser: "firefox", visitors: 287, fill: "var(--color-firefox)" },
  { browser: "edge", visitors: 173, fill: "var(--color-edge)" },
  { browser: "other", visitors: 190, fill: "var(--color-other)" },
]
type Data = typeof chartData[number]

const chartConfig = {
  visitors: { label: "Visitors", color: undefined },
  chrome: { label: "Chrome", color: "var(--chart-1)" },
  safari: { label: "Safari", color: "var(--chart-2)" },
  firefox: { label: "Firefox", color: "var(--chart-3)" },
  edge: { label: "Edge", color: "var(--chart-4)" },
  other: { label: "Other", color: "var(--chart-5)" },
} satisfies ChartConfig

const totalVisitors = computed(() => chartData.reduce((acc, curr) => acc + curr.visitors, 0))
</script>

<template>
  <Card class="flex flex-col">
    <CardHeader class="items-center pb-0">
      <CardTitle>Pie Chart</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent class="flex-1 pb-0">
      <ChartContainer
        :config="chartConfig"
        class="mx-auto aspect-square max-h-[250px]"
        :style="{
          '--vis-donut-central-label-font-size': 'var(--text-3xl)',
          '--vis-donut-central-label-font-weight': 'var(--font-weight-bold)',
          '--vis-donut-central-label-text-color': 'var(--foreground)',
          '--vis-donut-central-sub-label-text-color': 'var(--muted-foreground)',
        }"
      >
        <VisSingleContainer :data="chartData" :margin="{ top: 30, bottom: 30 }">
          <VisDonut
            :value="(d: Data) => d.visitors"
            :color="(d: Data) => chartConfig[d.browser as keyof typeof chartConfig].color"
            :arc-width="30"
            :central-label-offset-y="10"
            :central-label="totalVisitors.toLocaleString()"
            central-sub-label="Visitors"
          />
          <ChartTooltip
            :triggers="{
              [Donut.selectors.segment]: componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })!,
            }"
          />
        </VisSingleContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col gap-2 text-sm">
      <div class="flex items-center gap-2 font-medium leading-none">
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

## ChartPieStacked.vue — Stacked donuts (2 concentric rings)

Difference: 2 separate data sets (desktopData, mobileData), 2 `VisSingleContainer`
stacked via `position: absolute`. Inner ring: `arc-width: 0` + `radius: 50`.

```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"
import { TrendingUp } from "@lucide/vue"
import { Donut } from "@unovis/ts"
import { VisDonut, VisSingleContainer } from "@unovis/vue"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/registry/new-york-v4/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent, componentToString } from "@/registry/new-york-v4/ui/chart"

const desktopData = [
  { month: "january", desktop: 186, fill: "var(--color-january)" },
  { month: "february", desktop: 305, fill: "var(--color-february)" },
  { month: "march", desktop: 237, fill: "var(--color-march)" },
  { month: "april", desktop: 173, fill: "var(--color-april)" },
  { month: "may", desktop: 209, fill: "var(--color-may)" },
]
const mobileData = [
  { month: "january", mobile: 80, fill: "var(--color-january)" },
  { month: "february", mobile: 200, fill: "var(--color-february)" },
  { month: "march", mobile: 120, fill: "var(--color-march)" },
  { month: "april", mobile: 190, fill: "var(--color-april)" },
  { month: "may", mobile: 130, fill: "var(--color-may)" },
]

type DesktopData = typeof desktopData[number]
type MobileData = typeof mobileData[number]

const chartConfig = {
  visitors: { label: "Visitors", color: undefined },
  desktop: { label: "Desktop", color: undefined },
  mobile: { label: "Mobile", color: undefined },
  january: { label: "January", color: "var(--chart-1)" },
  february: { label: "February", color: "var(--chart-2)" },
  march: { label: "March", color: "var(--chart-3)" },
  april: { label: "April", color: "var(--chart-4)" },
  may: { label: "May", color: "var(--chart-5)" },
} satisfies ChartConfig
</script>

<template>
  <Card class="flex flex-col">
    <CardHeader class="items-center pb-0">
      <CardTitle>Pie Chart</CardTitle>
      <CardDescription>January - June 2024</CardDescription>
    </CardHeader>
    <CardContent class="flex-1 pb-0">
      <ChartContainer
        :config="chartConfig"
        class="relative mx-auto aspect-square max-h-[250px] [&_[data-vis-single-container]]:!absolute"
      >
        <!-- Outer ring: donut (mobile) -->
        <VisSingleContainer :margin="{ top: 30, bottom: 30 }">
          <VisDonut
            :data="mobileData"
            :value="(d: MobileData) => d.mobile"
            :color="(d: MobileData) => chartConfig[d.month as keyof typeof chartConfig].color"
            :arc-width="25"
          />
          <ChartTooltip
            :triggers="{
              [Donut.selectors.segment]: componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })!,
            }"
          />
        </VisSingleContainer>
        <!-- Inner circle: pie (desktop, radius=50) -->
        <VisSingleContainer :margin="{ top: 30, bottom: 30 }">
          <VisDonut
            :data="desktopData"
            :value="(d: DesktopData) => d.desktop"
            :color="(d: DesktopData) => chartConfig[d.month as keyof typeof chartConfig].color"
            :arc-width="0"
            :radius="50"
          />
          <ChartTooltip
            :triggers="{
              [Donut.selectors.segment]: componentToString(chartConfig, ChartTooltipContent, { hideLabel: true })!,
            }"
          />
        </VisSingleContainer>
      </ChartContainer>
    </CardContent>
    <CardFooter class="flex-col gap-2 text-sm">
      <div class="flex items-center gap-2 font-medium leading-none">
        Trending up by 5.2% this month <TrendingUp class="h-4 w-4" />
      </div>
      <div class="leading-none text-muted-foreground">
        Showing total visitors for the last 6 months
      </div>
    </CardFooter>
  </Card>
</template>
```

## Important VisDonut props

| Prop                   | Description                                   |
|------------------------|-----------------------------------------------|
| `value`                | Function: data point -> numeric value         |
| `color`                | Function or string for the segment color      |
| `arc-width`            | 0 = full pie, >0 = donut ring width           |
| `radius`               | Outer radius in pixels (for stacked)          |
| `central-label`        | Text in the center of the donut               |
| `central-sub-label`    | Subtext in the center                         |
| `central-label-offset-y` | Y offset of the central label              |
