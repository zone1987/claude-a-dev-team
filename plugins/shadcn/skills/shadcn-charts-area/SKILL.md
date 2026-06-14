---
name: shadcn-charts-area
description: >
  shadcn/ui Area Charts – alle 10 Varianten mit komplettem Code.
  Trigger: "shadcn area chart", "area chart shadcn", "recharts area shadcn",
  "AreaChart shadcn", "flaechendiagramm shadcn", "area chart stacked",
  "area chart gradient", "area chart interactive", "area chart linear",
  "area chart step", "area chart legend".
---

# shadcn/ui Area Charts

All 10 area chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `AreaChart`.

See `references/area-charts-1.md` for charts 1–5 and `references/area-charts-2.md` for charts 6–10.

## Variants Overview

| File | Description |
|---|---|
| `chart-area-default` | Simple single-series area chart |
| `chart-area-axes` | Two-series stacked with visible Y-axis |
| `chart-area-gradient` | SVG `linearGradient` fill per series |
| `chart-area-icons` | ChartConfig entries with `icon` field, renders legend icons |
| `chart-area-interactive` | Time-range picker (90d/30d/7d) filtering 90-day dataset |
| `chart-area-legend` | Two-series stacked with `ChartLegend` |
| `chart-area-linear` | `type="linear"` interpolation instead of `"natural"` |
| `chart-area-stacked` | Two stacked series, dot indicator in tooltip |
| `chart-area-stacked-expand` | Three series with `stackOffset="expand"` (percentage) |
| `chart-area-step` | `type="step"` interpolation |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-area-*.tsx`
