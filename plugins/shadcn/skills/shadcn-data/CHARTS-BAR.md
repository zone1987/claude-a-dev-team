# shadcn/ui Bar Charts

All 10 bar chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `BarChart`.

See `CHARTS-BAR-BAR-CHARTS-1.md` for charts 1–5 and `CHARTS-BAR-BAR-CHARTS-2.md` for charts 6–10.

## Variants Overview

| File | Description |
|---|---|
| `chart-bar-default` | Simple single-series vertical bar chart |
| `chart-bar-active` | Custom `shape` prop renders active bar with dashed stroke |
| `chart-bar-horizontal` | `layout="vertical"` for horizontal bars |
| `chart-bar-interactive` | Toggle between desktop/mobile series via header buttons |
| `chart-bar-label` | `LabelList` rendering value above each bar |
| `chart-bar-label-custom` | Custom label content with `LabelList` |
| `chart-bar-mixed` | Per-bar fill color via `fill` field in data |
| `chart-bar-multiple` | Two grouped series side-by-side |
| `chart-bar-negative` | Negative values with conditional fill colors |
| `chart-bar-stacked` | Two stacked series |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-bar-*.tsx`
