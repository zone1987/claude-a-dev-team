# shadcn/ui Pie Charts

All 11 pie chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `PieChart`.

See `CHARTS-PIE-PIE-CHARTS-1.md` for charts 1–6 and `CHARTS-PIE-PIE-CHARTS-2.md` for charts 7–11.

## Variants Overview

| File | Description |
|---|---|
| `chart-pie-simple` | Basic pie chart, per-segment fill from data |
| `chart-pie-donut` | Donut with `innerRadius={60}` |
| `chart-pie-donut-active` | Donut with active sector expanded via custom `shape` |
| `chart-pie-donut-text` | Donut with centered total text via `<Label>` |
| `chart-pie-interactive` | Donut with `<Select>` to highlight active month; uses `ChartStyle` directly |
| `chart-pie-stacked` | Two concentric `<Pie>` rings (desktop outer, mobile inner) |
| `chart-pie-label` | Built-in Recharts labels (percentage) |
| `chart-pie-label-custom` | Custom label render prop showing raw visitor count |
| `chart-pie-label-list` | `<LabelList>` inside pie showing browser name |
| `chart-pie-legend` | Pie with `ChartLegend` |
| `chart-pie-separator-none` | Pie with `stroke="0"` removing segment borders |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-pie-*.tsx`
