# shadcn-vue Chart — Installation & Theming

## CLI installation

```bash
npx shadcn-vue@latest add chart
```

Installs `@unovis/vue` and `@unovis/ts` as dependencies and creates
`components/ui/chart/`.

## Manual installation

```bash
npm install @unovis/vue @unovis/ts
```

Then create the files in `components/ui/chart/` (see `ui-chart-source.md`).

## CSS color variables (--chart-1 to --chart-5)

The chart colors must be defined in the global CSS file:

```css
:root {
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.714);
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
```

## ChartConfig and CSS variables

`ChartStyle.vue` injects `--color-<key>` CSS variables based on `ChartConfig`:

```ts
// Static color
const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" }
}
// Theme-specific color (light/dark)
const chartConfig = {
  desktop: {
    label: "Desktop",
    theme: { light: "#3b82f6", dark: "#60a5fa" }
  }
}
```

The variables are then available in the SVG as `var(--color-desktop)`.

## unovis CSS reset (recommended)

`ChartContainer.vue` sets the following CSS custom properties for unovis:

```ts
'--vis-tooltip-padding': '0px',
'--vis-tooltip-background-color': 'transparent',
'--vis-tooltip-border-color': 'transparent',
'--vis-tooltip-text-color': 'none',
'--vis-tooltip-shadow-color': 'none',
'--vis-tooltip-backdrop-filter': 'none',
'--vis-crosshair-circle-stroke-color': '#0000',
'--vis-crosshair-line-stroke-width': cursor ? '1px' : '0px',
'--vis-font-family': 'var(--font-sans)',
```
