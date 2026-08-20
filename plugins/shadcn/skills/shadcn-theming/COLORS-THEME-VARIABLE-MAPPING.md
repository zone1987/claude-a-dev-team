# shadcn/ui — Theme Variable to Tailwind Class Mapping

## How token mapping works

shadcn/ui CSS tokens are exposed to Tailwind via `@theme inline`:

```css
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  /* ... */
}
```

Tailwind generates utility classes from these:
- `--color-background` → `bg-background`, `text-background`, `border-background`
- `--color-primary` → `bg-primary`, `text-primary`, `border-primary`

## Complete token → utility class mapping

| CSS Variable | Background class | Text class | Border class |
|-------------|-----------------|-----------|-------------|
| `--background` | `bg-background` | `text-background` | `border-background` |
| `--foreground` | `bg-foreground` | `text-foreground` | `border-foreground` |
| `--card` | `bg-card` | `text-card` | `border-card` |
| `--card-foreground` | `bg-card-foreground` | `text-card-foreground` | |
| `--popover` | `bg-popover` | `text-popover` | `border-popover` |
| `--popover-foreground` | `bg-popover-foreground` | `text-popover-foreground` | |
| `--primary` | `bg-primary` | `text-primary` | `border-primary` |
| `--primary-foreground` | `bg-primary-foreground` | `text-primary-foreground` | |
| `--secondary` | `bg-secondary` | `text-secondary` | `border-secondary` |
| `--secondary-foreground` | `bg-secondary-foreground` | `text-secondary-foreground` | |
| `--muted` | `bg-muted` | `text-muted` | `border-muted` |
| `--muted-foreground` | `bg-muted-foreground` | `text-muted-foreground` | |
| `--accent` | `bg-accent` | `text-accent` | `border-accent` |
| `--accent-foreground` | `bg-accent-foreground` | `text-accent-foreground` | |
| `--destructive` | `bg-destructive` | `text-destructive` | `border-destructive` |
| `--border` | `bg-border` | `text-border` | `border-border` |
| `--input` | `bg-input` | `text-input` | `border-input` |
| `--ring` | | | `outline-ring` / `ring-ring` |
| `--chart-1` ... `--chart-5` | `bg-chart-1` | `text-chart-1` | |
| `--sidebar` | `bg-sidebar` | `text-sidebar` | `border-sidebar` |
| `--sidebar-foreground` | | `text-sidebar-foreground` | |
| `--sidebar-primary` | `bg-sidebar-primary` | `text-sidebar-primary` | |
| `--sidebar-primary-foreground` | | `text-sidebar-primary-foreground` | |
| `--sidebar-accent` | `bg-sidebar-accent` | `text-sidebar-accent` | |
| `--sidebar-accent-foreground` | | `text-sidebar-accent-foreground` | |
| `--sidebar-border` | | | `border-sidebar-border` |
| `--sidebar-ring` | | | `ring-sidebar-ring` |

## Radius classes

| CSS Variable | Tailwind class |
|-------------|---------------|
| `--radius-sm` | `rounded-sm` |
| `--radius-md` | `rounded-md` |
| `--radius-lg` | `rounded-lg` |
| `--radius-xl` | `rounded-xl` |
| `--radius-2xl` | `rounded-2xl` |
| `--radius-3xl` | `rounded-3xl` |
| `--radius-4xl` | `rounded-4xl` |

## OKLCH format

New shadcn/ui v4 projects use OKLCH: `oklch(lightness chroma hue)`

- Lightness: 0 (black) to 1 (white)
- Chroma: 0 (grey) to ~0.4 (vivid)
- Hue: 0-360 degrees

Benefits over HSL:
- Perceptually uniform (equal steps look equally different)
- Wider gamut for display-p3 screens
- More predictable contrast ratios

Source: `https://ui.shadcn.com/r/colors/index.json` + theming docs
