---
name: shadcn-chart
description: Creates a shadcn/ui chart (Recharts) — picks the chart type and variant, takes the complete example code from the shadcn-data skill, and adapts ChartConfig, the data and the --chart colour tokens.
argument-hint: <type> area|bar|line|pie|radar|radial [--variant e.g. stacked|interactive|donut] [--data "description"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-chart

Build a chart. Skills: `shadcn-data` for the chart code, `shadcn-theming` for the colour tokens.

## Steps
1. Chart type and variant from `$ARGUMENTS`.
2. From `shadcn-data`: take the complete example for that type and variant.
3. Adapt `ChartConfig` (the series keys, labels and colours) to the actual data.
4. Colours come from the `--chart-1` to `--chart-5` tokens, so the chart follows the theme in light
   and dark (`shadcn-theming`).
5. `--data` shapes the example data to what is described.

Use the documented ChartConfig fields and Recharts props only (source: `shadcn-data`).
