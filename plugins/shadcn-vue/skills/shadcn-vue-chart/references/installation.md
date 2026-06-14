# Chart — Installation

## CLI

```bash
npx shadcn-vue@latest add chart
```

## Manual

### 1. Install dependencies

```bash
npm install @unovis/ts @unovis/vue
```

### 2. Copy source files

Copy all files from
[GitHub: registry/new-york-v4/ui/chart](https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/chart)
into your project (e.g. `src/components/ui/chart/`).

### 3. Update import paths

Replace `@/registry/bases/reka/ui/chart` with `@/components/ui/chart`
throughout your project.

### 4. Add CSS color variables

Add the following to your global CSS file:

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

## Dependencies overview

| Package        | Purpose                                   |
| :------------- | :---------------------------------------- |
| `@unovis/ts`   | Unovis core (selectors, types, CurveType) |
| `@unovis/vue`  | Vue 3 Unovis components (VisXYContainer,  |
|                | VisGroupedBar, VisLine, VisArea, VisAxis,  |
|                | VisDonut, VisSingleContainer,             |
|                | VisCrosshair, VisTooltip)                 |
| `reka-ui`      | useId, Primitive, createContext           |
| `@vueuse/core` | isClient (SSR guard in utils.ts)          |

## Source location

`/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/chart/`
