# shadcn/ui Radial Charts

All 6 radial chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `RadialBarChart` with `RadialBar`.

See `CHARTS-RADIAL-RADIAL-CHARTS.md` for all 6 variants.

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
