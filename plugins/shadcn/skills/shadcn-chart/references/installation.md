# Chart — Installation

## CLI (recommended)

```bash
npx shadcn@latest add chart
```

## Manual

1. Install dependencies:

```bash
npm install recharts
```

2. Copy the source from `references/source.md` into `components/ui/chart.tsx`.
3. Add the following colors to your CSS file:

```css
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
    --chart-3: oklch(0.398 0.07 227.392);
    --chart-4: oklch(0.828 0.189 84.429);
    --chart-5: oklch(0.769 0.188 70.08);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
    --chart-3: oklch(0.769 0.188 70.08);
    --chart-4: oklch(0.627 0.265 303.9);
    --chart-5: oklch(0.645 0.246 16.439);
  }
}
```

4. Update the import paths to match your project setup.

## Recharts v3 Migration Notes

If upgrading older chart code to Recharts v3:
- Use `var(--chart-1)` instead of `hsl(var(--chart-1))` when referencing CSS variables.
- Use `ChartTooltip.defaultIndex` for initial tooltip state only. Keep persistent active shapes in your own chart state.
- Remove `layout` from `<Bar>` when the parent `<BarChart>` already defines it.
- Keep a height, `min-h-*`, or `aspect-*` on `ChartContainer` so `ResponsiveContainer` can measure on first render.

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/chart.mdx`_
