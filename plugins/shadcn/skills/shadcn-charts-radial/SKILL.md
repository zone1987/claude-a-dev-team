---
name: shadcn-charts-radial
description: >
  shadcn/ui Radial Charts – alle 6 Varianten mit komplettem Code.
  Trigger: "shadcn radial chart", "radial chart shadcn", "recharts radial bar",
  "RadialBarChart shadcn", "radiales balkendiagramm shadcn",
  "radial chart label", "radial chart stacked", "radial chart text",
  "radial chart grid", "radial chart shape".
---

# shadcn/ui Radial Charts

All 6 radial chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `RadialBarChart` with `RadialBar`.

See `references/radial-charts.md` for all 6 variants.

## Variants Overview

| File | Description |
|---|---|
| `chart-radial-simple` | Basic radial bar chart with `background` track |
| `chart-radial-grid` | Radial with `PolarGrid gridType="circle"` |
| `chart-radial-label` | Radial with `LabelList position="insideStart"` |
| `chart-radial-shape` | Single-bar arc with `PolarGrid polarRadius` + center `Label` |
| `chart-radial-stacked` | Two stacked bars `stackId="a"` with center label, `endAngle=180` |
| `chart-radial-text` | Single bar with `PolarGrid` rings, center text label |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-radial-*.tsx`
