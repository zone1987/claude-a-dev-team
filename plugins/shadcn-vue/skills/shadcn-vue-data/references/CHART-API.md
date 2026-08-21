# Chart — API Reference

Reka-ui API: https://reka-ui.com/docs/components/chart#api-reference

---

## Contents

- [ChartConfig type](#chartconfig-type)
- [Exports from `@/components/ui/chart`](#exports-from-componentsuichart)
- [ChartContainer Props](#chartcontainer-props)
- [ChartLegendContent Props](#chartlegendcontent-props)
- [ChartTooltipContent Props](#charttooltipcontent-props)
- [componentToString](#componenttostring)
- [Unovis components used in examples](#unovis-components-used-in-examples)

## ChartConfig type

```ts
type ChartConfig = {
  [k in string]: {
    label?: string | Component
    icon?: string | Component
  } & (
    | { color?: string; theme?: never }
    | { color?: never; theme: Record<"light" | "dark", string> }
  )
}
```

Each key maps to a data series. `color` accepts any CSS color value
(hex, hsl, oklch, `var(--chart-1)`). Use `theme` instead of `color`
to specify different values per light/dark mode.

---

## Exports from `@/components/ui/chart`

| Export               | Type            | Description                                    |
| :------------------- | :-------------- | :--------------------------------------------- |
| `ChartContainer`     | Vue component   | Wrapper div; provides chart context + style    |
| `ChartLegendContent` | Vue component   | Horizontal legend row for all series           |
| `ChartTooltipContent`| Vue component   | Tooltip card with indicator, label, value      |
| `ChartTooltip`       | re-export       | `VisTooltip` from `@unovis/vue`               |
| `ChartCrosshair`     | re-export       | `VisCrosshair` from `@unovis/vue`             |
| `componentToString`  | function        | Renders a Vue component to HTML string for     |
|                      |                 | Unovis tooltip `template` prop                 |
| `ChartConfig`        | TypeScript type | Config shape for labels, icons, colors         |
| `THEMES`             | const           | `{ light: "", dark: ".dark" }`                 |
| `useChart`           | composable      | Access chart context (id + config) from child  |
| `provideChartContext` | function       | Provide chart context (used in ChartContainer) |

---

## ChartContainer Props

| Prop      | Type             | Default | Description                           |
| :-------- | :--------------- | :------ | :------------------------------------ |
| `config`  | `ChartConfig`    | —       | Required. Series labels, icons, colors|
| `id`      | `string`         | auto    | Optional custom id (prefixed chart-)  |
| `class`   | `string`         | —       | Additional CSS classes                |
| `cursor`  | `boolean`        | false   | Show crosshair cursor line            |

Slot: `default` — receives `{ id: string, config: ChartConfig }`.

---

## ChartLegendContent Props

| Prop            | Type               | Default    | Description                        |
| :-------------- | :----------------- | :--------- | :--------------------------------- |
| `verticalAlign` | `"top" \| "bottom"` | `"bottom"` | Legend placement                   |
| `nameKey`       | `string`           | —          | Override series name key           |
| `hideIcon`      | `boolean`          | false      | Hide icon from legend items        |
| `class`         | `string`           | —          | Additional CSS classes             |

---

## ChartTooltipContent Props

| Prop              | Type                            | Default | Description                         |
| :---------------- | :------------------------------ | :------ | :---------------------------------- |
| `payload`         | `Record<string, any>`           | `{}`    | Data for current hover point        |
| `config`          | `ChartConfig`                   | `{}`    | Chart config for label/color lookup |
| `indicator`       | `"dot" \| "line" \| "dashed"`   | `"dot"` | Indicator shape next to value       |
| `hideLabel`       | `boolean`                       | false   | Hide the tooltip label              |
| `hideIndicator`   | `boolean`                       | false   | Hide the color indicator            |
| `labelKey`        | `string`                        | —       | Config/data key to use for label    |
| `nameKey`         | `string`                        | —       | Config/data key to use for name     |
| `labelFormatter`  | `(d: number \| Date) => string` | —       | Custom label formatter function     |
| `x`               | `number \| Date`                | —       | Current x value (for labelFormatter)|
| `color`           | `string`                        | —       | Override color                      |
| `class`           | `string`                        | —       | Additional CSS classes              |

Slot: `default` — override entire tooltip content.

---

## componentToString

```ts
function componentToString<P>(
  config: ChartConfig,
  component: Constructor<P>,
  props?: P,
): ((data: any, x: number | Date) => string) | undefined
```

Call this at the top level of `<script setup>` (uses `useId()`
internally). Returns `undefined` on the server (SSR guard via
`isClient`). Pass the return value as the `template` prop of
`ChartCrosshair`:

```vue
<ChartCrosshair
  :template="componentToString(chartConfig, ChartTooltipContent, {
    indicator: 'line',
    labelKey: 'monthLabel',
  })"
  :color="chartConfig.desktop.color"
/>
```

Results are cached per data point (serialized key).

---

## Unovis components used in examples

| Component           | Purpose                                    |
| :------------------ | :----------------------------------------- |
| `VisXYContainer`    | XY chart container (cartesian charts)      |
| `VisSingleContainer`| Single-vis container (donut/radial)        |
| `VisGroupedBar`     | Grouped bar chart                          |
| `VisLine`           | Line series                                |
| `VisArea`           | Area series (filled below line)            |
| `VisAxis`           | X or Y axis with ticks                     |
| `VisDonut`          | Donut / radial chart                       |
| `VisCrosshair`      | Hover crosshair (re-exported as            |
|                     | `ChartCrosshair`)                          |
| `VisTooltip`        | Unovis tooltip container (re-exported as   |
|                     | `ChartTooltip`)                            |

Full Unovis API: https://unovis.dev/docs
