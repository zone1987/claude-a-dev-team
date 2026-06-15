# shadcn-vue Chart — Installation & Theming

## CLI-Installation

```bash
npx shadcn-vue@latest add chart
```

Installiert `@unovis/vue` und `@unovis/ts` als Abhaengigkeiten und legt
`components/ui/chart/` an.

## Manuelle Installation

```bash
npm install @unovis/vue @unovis/ts
```

Dann die Dateien aus `components/ui/chart/` anlegen (siehe `ui-chart-source.md`).

## CSS-Farb-Variablen (--chart-1 bis --chart-5)

In der globalen CSS-Datei muessen die Chart-Farben definiert sein:

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

## ChartConfig und CSS-Variablen

`ChartStyle.vue` injiziert `--color-<key>` CSS-Variablen basierend auf `ChartConfig`:

```ts
// Statische Farbe
const chartConfig = {
  desktop: { label: "Desktop", color: "var(--chart-1)" }
}
// Theme-spezifische Farbe (light/dark)
const chartConfig = {
  desktop: {
    label: "Desktop",
    theme: { light: "#3b82f6", dark: "#60a5fa" }
  }
}
```

Die Variablen sind dann im SVG als `var(--color-desktop)` verfuegbar.

## unovis CSS-Reset (empfohlen)

`ChartContainer.vue` setzt folgende CSS-Custom-Properties fuer unovis:

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
