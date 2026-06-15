# shadcn-vue Chart Tooltips — Vollstaendiger Quellcode

Alle 7 Tooltip-Varianten. Alle nutzen `VisStackedBar + VisAxis` aus `@unovis/vue`
als Traeger-Chart. Tooltip via `ChartCrosshair :template + componentToString`.

---

## Gemeinsame Struktur aller Tooltip-Beispiele

```vue
<!-- Gleiche Datenbasis in allen 7 Beispielen -->
const chartData = [
  { date: new Date("2024-07-15"), running: 450, swimming: 300 },
  { date: new Date("2024-07-16"), running: 380, swimming: 420 },
  { date: new Date("2024-07-17"), running: 520, swimming: 120 },
  { date: new Date("2024-07-18"), running: 140, swimming: 550 },
  { date: new Date("2024-07-19"), running: 600, swimming: 350 },
  { date: new Date("2024-07-20"), running: 480, swimming: 400 },
]

<!-- Gemeinsames VisXYContainer-Template -->
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
    :template="/* VARIIERT je nach Beispiel */"
    color="#0000"
  />
</VisXYContainer>
```

---

## ChartTooltipDefault.vue — Standard-Tooltip mit labelFormatter

`indicator: "dot"` (Standard), Datum als Label via `labelFormatter`.

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
  <!-- ... Card-Wrapper ... -->
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

## ChartTooltipIcons.vue — Tooltip mit Icons

ChartConfig hat `icon: Footprints` / `icon: Waves`. `hideLabel: true` blendet das Datum aus.

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

## ChartTooltipIndicatorLine.vue — Linien-Indikator statt Punkt

`indicator: 'line'` zeigt einen vertikalen Farbstreifen statt des Punktes.

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

## ChartTooltipIndicatorNone.vue — Kein Indikator

`hideIndicator: true` blendet den Farbindikator komplett aus.

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

## ChartTooltipLabelCustom.vue — Benutzerdefiniertes Label aus ChartConfig

`labelKey: 'activities'` liest das Label aus `chartConfig.activities.label`.

```vue
const chartConfig = {
  activities: { label: "Activities" },  // <-- wird als Tooltip-Label verwendet
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

## ChartTooltipLabelFormatter.vue — Label-Formatter (langes Datum)

Formattierung als "15. July 2024".

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

## ChartTooltipLabelNone.vue — Kein Label, kein Indikator

`hideLabel: true` + `hideIndicator: true` = nur die Werte ohne Dekoration.

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

## ChartTooltipContent Props — Uebersicht

| Prop             | Typ                              | Standard | Wirkung                                      |
|------------------|----------------------------------|----------|----------------------------------------------|
| `hideLabel`      | `boolean`                        | `false`  | Obere Label-Zeile ausblenden                 |
| `hideIndicator`  | `boolean`                        | `false`  | Farbindikator (Punkt/Linie) ausblenden       |
| `indicator`      | `"line" \| "dot" \| "dashed"`    | `"dot"`  | Form des Farbindikators                      |
| `labelKey`       | `string`                         | –        | ChartConfig-Key dessen `.label` angezeigt    |
| `labelFormatter` | `(d: number \| Date) => string`  | –        | Formatter fuer das X-Label                  |
| `nameKey`        | `string`                         | –        | Key fuer Zeilennamen                         |
| `payload`        | `Record<string, any>`            | `{}`     | Datenpunkt (automatisch von componentToString)|
| `config`         | `ChartConfig`                    | `{}`     | Chart-Konfiguration                          |
| `x`              | `number \| Date`                 | –        | X-Wert fuer labelFormatter                  |

## componentToString — Signatur

```ts
componentToString(
  config: ChartConfig,
  component: Constructor,     // ChartTooltipContent
  props?: Partial<ChartTooltipContentProps>
): ((_data: any, x: number | Date) => string) | undefined
```

Gibt eine Callback-Funktion zurueck, die `ChartCrosshair :template` erwartet.
Rendert die Vue-Komponente zu HTML-String (mit Caching).
