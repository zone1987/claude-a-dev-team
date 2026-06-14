# Chart — API Reference

## Design Philosophy

Charts use composition with Recharts. You build charts using Recharts components and bring in custom components (`ChartTooltip`, `ChartLegend`) only when needed. The chart is NOT wrapped — you can follow Recharts upgrade paths directly.

## ChartConfig Type

```ts
type ChartConfig = Record<
  string,
  {
    label?: React.ReactNode
    icon?: React.ComponentType
  } & (
    | { color?: string; theme?: never }
    | { color?: never; theme: Record<"light" | "dark", string> }
  )
>
```

Usage:

```tsx
import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
    // OR use CSS variable:
    // color: "var(--chart-1)",
    // OR use theme object for light/dark:
    // theme: { light: "#2563eb", dark: "#dc2626" },
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig
```

## ChartContainer

The root wrapper. Provides a `ChartContext` with the config, injects CSS color variables, and wraps children in `ResponsiveContainer`.

| Prop               | Type                                   | Default              | Description                                    |
| ------------------ | -------------------------------------- | -------------------- | ---------------------------------------------- |
| `config`           | `ChartConfig`                          | required             | Chart configuration object                     |
| `children`         | `React.ReactNode`                      | required             | Recharts chart component(s)                    |
| `id`               | `string`                               | auto-generated       | Unique chart ID for CSS scoping                |
| `initialDimension` | `{ width: number; height: number }`    | `{ width: 320, height: 200 }` | Initial dimension for ResponsiveContainer |
| `className`        | `string`                               | -                    | Applied to the wrapper div                     |

**Important:** Always set a `min-h-[VALUE]`, height, or `aspect-*` class on `ChartContainer`.

## ChartTooltip

Re-export of `RechartsPrimitive.Tooltip`. Use with `content={<ChartTooltipContent />}`.

```tsx
<ChartTooltip content={<ChartTooltipContent />} />
```

## ChartTooltipContent

| Prop            | Type                      | Default | Description                                   |
| --------------- | ------------------------- | ------- | --------------------------------------------- |
| `indicator`     | `"dot" \| "line" \| "dashed"` | `"dot"` | Visual indicator style                       |
| `hideLabel`     | `boolean`                 | `false` | Hide the tooltip label                        |
| `hideIndicator` | `boolean`                 | `false` | Hide the color indicator                      |
| `labelKey`      | `string`                  | -       | Config/data key to use for the label          |
| `nameKey`       | `string`                  | -       | Config/data key to use for the item name      |
| `labelFormatter`| `function`                | -       | Custom label formatter                        |
| `formatter`     | `function`                | -       | Custom value formatter                        |
| `color`         | `string`                  | -       | Override indicator color                      |

## ChartLegend

Re-export of `RechartsPrimitive.Legend`. Use with `content={<ChartLegendContent />}`.

```tsx
<ChartLegend content={<ChartLegendContent />} />
```

## ChartLegendContent

| Prop           | Type      | Default    | Description                              |
| -------------- | --------- | ---------- | ---------------------------------------- |
| `hideIcon`     | `boolean` | `false`    | Hide the icon/color swatch               |
| `nameKey`      | `string`  | -          | Config/data key to use for legend names  |
| `verticalAlign`| `string`  | `"bottom"` | Position: `"top"` or `"bottom"`         |

## Using Colors

Reference chart config colors in components:

```tsx
// Recharts component fill
<Bar dataKey="desktop" fill="var(--color-desktop)" />

// Chart data (pie/donut)
const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
]

// Tailwind class
<LabelList className="fill-(--color-desktop)" />
```

## Accessibility

```tsx
<LineChart accessibilityLayer />
```

The `accessibilityLayer` prop adds keyboard access and screen reader support.

## Building a Chart Step-by-Step

```tsx
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
import {
  ChartContainer,
  ChartLegend,
  ChartLegendContent,
  ChartTooltip,
  ChartTooltipContent,
  type ChartConfig,
} from "@/components/ui/chart"

const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
]

const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" },
  mobile: { label: "Mobile", color: "var(--chart-2)" },
} satisfies ChartConfig

export function MyChart() {
  return (
    <ChartContainer config={chartConfig} className="min-h-[200px] w-full">
      <BarChart accessibilityLayer data={chartData}>
        <CartesianGrid vertical={false} />
        <XAxis
          dataKey="month"
          tickLine={false}
          tickMargin={10}
          axisLine={false}
          tickFormatter={(value) => value.slice(0, 3)}
        />
        <ChartTooltip content={<ChartTooltipContent />} />
        <ChartLegend content={<ChartLegendContent />} />
        <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
        <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
      </BarChart>
    </ChartContainer>
  )
}
```

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/chart.mdx`_
