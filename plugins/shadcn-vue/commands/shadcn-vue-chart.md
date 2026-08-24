---
name: shadcn-vue-chart
description: Creates a shadcn-vue chart — picks the chart type and variant, takes the complete example Vue code from the shadcn-vue-data skill, and adapts the chart config, the data and the --chart colour tokens.
argument-hint: <type> area|bar|line|pie [--variant e.g. stacked|donut] [--data "description"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-chart

Build a chart. Skills: `shadcn-vue-data` for the chart code, `shadcn-vue-theming` for the tokens.

## Steps
1. Chart type and variant from `$ARGUMENTS`.
2. From `shadcn-vue-data`: take the complete example for that type and variant, including
   `ChartContainer` and the tooltip and legend components.
3. Adapt the chart config (series keys, labels, colours) to the actual data.
4. Colours come from the `--chart-1` to `--chart-5` tokens, so the chart follows the theme in light
   and dark (`shadcn-vue-theming`).
5. `--data` shapes the example data to what is described.

Use the documented config fields and component props only (source: `shadcn-vue-data`).
