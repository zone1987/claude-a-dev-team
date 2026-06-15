# shadcn-vue: Theming Reference

shadcn-vue uses CSS variables for theming by default. Set `tailwind.cssVariables: true`
in `components.json` (this is the default).

```vue
<div class="bg-background text-foreground" />
```

Tailwind maps tokens to utilities: `bg-background`, `text-foreground`, `border-border`,
`ring-ring`.

Dark mode overrides the same tokens inside a `.dark` selector:

```css
@custom-variant dark (&:is(.dark *));
```

## Token Convention

Semantic background/foreground pairs. The base token controls the surface color;
the `-foreground` token controls text and icon color on that surface.
The `background` suffix is omitted for the surface token.
Example: `primary` pairs with `primary-foreground`.

```css
--primary: oklch(0.205 0 0);
--primary-foreground: oklch(0.985 0 0);
```

```vue
<div class="bg-primary text-primary-foreground">Hello</div>
```

## All Theme Tokens

| Token | What it controls | Used by |
|---|---|---|
| `background` / `foreground` | Default app background and text color | Page shell, sections, default text |
| `card` / `card-foreground` | Elevated surfaces and content inside them | Card, dashboard panels, settings panels |
| `popover` / `popover-foreground` | Floating surfaces and content inside them | Popover, DropdownMenu, ContextMenu, overlays |
| `primary` / `primary-foreground` | High-emphasis actions and brand surfaces | Default Button, selected states, badges, active accents |
| `secondary` / `secondary-foreground` | Lower-emphasis filled actions and supporting surfaces | Secondary buttons, secondary badges, supporting UI |
| `muted` / `muted-foreground` | Subtle surfaces and lower-emphasis content | Descriptions, placeholders, empty states, helper text |
| `accent` / `accent-foreground` | Interactive hover, focus, and active surfaces | Ghost buttons, menu highlight states, hovered rows |
| `destructive` | Destructive actions and error emphasis | Destructive buttons, invalid states, destructive menu items |
| `border` | Default borders and separators | Cards, menus, tables, separators, layout dividers |
| `input` | Form control borders and input surface treatment | Input, Textarea, Select, outline-style controls |
| `ring` | Focus rings and outlines | Buttons, inputs, checkboxes, menus, focusable controls |
| `chart-1` ... `chart-5` | Default chart palette | Charts and chart-driven dashboard blocks |
| `sidebar` / `sidebar-foreground` | Base sidebar surface and default sidebar text | Sidebar container and default content |
| `sidebar-primary` / `sidebar-primary-foreground` | High-emphasis sidebar actions | Active items, icon tiles, badges, sidebar CTAs |
| `sidebar-accent` / `sidebar-accent-foreground` | Sidebar hover and selected states | Sidebar menu hover, open items, interactive rows |
| `sidebar-border` | Sidebar-specific borders and separators | Sidebar headers, groups, internal dividers |
| `sidebar-ring` | Sidebar-specific focus rings | Focused controls inside the sidebar |
| `radius` | Base corner radius scale | Cards, inputs, buttons, popovers, derived radius-* tokens |

## Radius Scale

`--radius` is the base radius token. A scale is derived from it:

```css
@theme inline {
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) * 1.4);
  --radius-2xl: calc(var(--radius) * 1.8);
  --radius-3xl: calc(var(--radius) * 2.2);
  --radius-4xl: calc(var(--radius) * 2.6);
}
```

- `radius-lg` is the base value
- Changing `--radius` updates the entire radius scale

## Adding New Tokens

Define under `:root` and `.dark`, then expose to Tailwind with `@theme inline`:

```css
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}

.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}

@theme inline {
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
}
```

Usage: `bg-warning` and `text-warning-foreground`.

## Base Colors

`tailwind.baseColor` controls default token values at `init`.
Available: **Neutral**, **Gray**, **Zinc**, **Stone**, **Slate**.

## Full Default Neutral Theme CSS

```css
@import "tailwindcss";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) * 1.4);
  --radius-2xl: calc(var(--radius) * 1.8);
  --radius-3xl: calc(var(--radius) * 2.2);
  --radius-4xl: calc(var(--radius) * 2.6);
}

:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }

  body {
    @apply bg-background text-foreground;
  }
}
```

## Without CSS Variables

```bash
npx shadcn-vue@latest init --no-css-variables
```

Sets `tailwind.cssVariables: false`. Components use inline Tailwind color utilities:

```vue
<div class="bg-zinc-950 text-zinc-50 dark:bg-white dark:text-zinc-950" />
```

This is an installation-time choice. To switch an existing project, delete and
re-install all components.

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/04.theming.md`
