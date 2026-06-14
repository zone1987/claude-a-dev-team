---
name: shadcn-charts-radar
description: >
  shadcn/ui Radar Charts – alle 14 Varianten mit komplettem Code.
  Trigger: "shadcn radar chart", "radar chart shadcn", "recharts radar shadcn",
  "RadarChart shadcn", "spinnennetz diagramm shadcn", "radar chart grid",
  "radar chart multiple", "radar chart icons", "radar chart legend",
  "radar chart dots", "radar chart lines only".
---

# shadcn/ui Radar Charts

All 14 radar chart variants from the shadcn registry. Each uses
`ChartContainer` + Recharts `RadarChart` with `PolarGrid`, `PolarAngleAxis`,
and one or more `Radar` series.

See:
- `references/radar-charts-1.md` — charts 1–5
- `references/radar-charts-2.md` — charts 6–10
- `references/radar-charts-3.md` — charts 11–14

## Variants Overview

| File | Description |
|---|---|
| `chart-radar-default` | Basic radar with polygon grid |
| `chart-radar-dots` | Radar with `dot={{ r: 4 }}` on data points |
| `chart-radar-grid-circle-fill` | Circle grid with `className` fill tint |
| `chart-radar-grid-circle-no-lines` | Circle grid, `radialLines={false}` |
| `chart-radar-grid-circle` | Circle grid with dots |
| `chart-radar-grid-custom` | Single-ring grid via `polarRadius={[90]}` |
| `chart-radar-grid-fill` | Polygon grid with opacity tint fill |
| `chart-radar-grid-none` | No `<PolarGrid>` at all |
| `chart-radar-icons` | Two series + `ChartLegend` using lucide icons in config |
| `chart-radar-label-custom` | Custom `tick` render on `PolarAngleAxis` |
| `chart-radar-legend` | Two series + `ChartLegend` |
| `chart-radar-lines-only` | Two series, `fillOpacity={0}` + explicit `stroke` |
| `chart-radar-multiple` | Two series overlapping with default fill |
| `chart-radar-radius` | Adds `PolarRadiusAxis` with custom `angle` |

---

Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/charts/chart-radar-*.tsx`
