# shadcn/ui Chart Tooltips

All 9 tooltip variants from the shadcn registry. All examples use stacked
`BarChart` as the host chart and demonstrate different `ChartTooltipContent`
props.

See:
- `CHARTS-TOOLTIP-TOOLTIP-CHARTS-1.md` — charts 1–5
- `CHARTS-TOOLTIP-TOOLTIP-CHARTS-2.md` — charts 6–9

## Variants Overview

| File | Description |
|---|---|
| `chart-tooltip-default` | Default `ChartTooltipContent` with no props |
| `chart-tooltip-advanced` | Custom `formatter` prop showing total row after last item |
| `chart-tooltip-formatter` | Custom `formatter` showing kcal unit inline |
| `chart-tooltip-icons` | `ChartConfig` with `icon` field (lucide icons in tooltip) |
| `chart-tooltip-indicator-line` | `indicator="line"` on `ChartTooltipContent` |
| `chart-tooltip-indicator-none` | `hideIndicator` prop removes the color indicator |
| `chart-tooltip-label-custom` | `labelKey="activities"` resolves label from `ChartConfig` |
| `chart-tooltip-label-formatter` | `labelFormatter` renders formatted date string |
| `chart-tooltip-label-none` | `hideIndicator` + `hideLabel` – minimal tooltip |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-tooltip-*.tsx`
