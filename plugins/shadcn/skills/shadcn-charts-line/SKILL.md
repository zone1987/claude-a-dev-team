---
name: shadcn-charts-line
description: >
  shadcn/ui Line Charts – alle 10 Varianten mit komplettem Code.
  Trigger: "shadcn line chart", "line chart shadcn", "recharts line shadcn",
  "LineChart shadcn", "liniendiagramm shadcn", "line chart dots",
  "line chart multiple", "line chart interactive", "line chart label",
  "line chart linear", "line chart step".
---

# shadcn/ui Line Charts

All 10 line chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `LineChart`.

See `references/line-charts-1.md` for charts 1–5 and `references/line-charts-2.md` for charts 6–10.

## Variants Overview

| File | Description |
|---|---|
| `chart-line-default` | Simple single-series line, `type="natural"`, no dots |
| `chart-line-dots` | Single series with dot markers on each data point |
| `chart-line-dots-colors` | Per-dot custom fill via data `fill` field and `<Dot>` render prop |
| `chart-line-dots-custom` | Custom SVG icon as dot via render prop |
| `chart-line-interactive` | Toggle between desktop/mobile series via header buttons |
| `chart-line-label` | `LabelList` renders value above each data point |
| `chart-line-label-custom` | Custom label from ChartConfig via `LabelList formatter` |
| `chart-line-linear` | `type="linear"` straight-line interpolation |
| `chart-line-multiple` | Two series with `type="monotone"` |
| `chart-line-step` | `type="step"` staircase interpolation |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-line-*.tsx`
