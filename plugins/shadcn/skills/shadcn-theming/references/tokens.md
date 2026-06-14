# shadcn/ui — Theme Token Details

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

`radius-lg` is the base. Change `--radius` once to update the entire scale.

## Adding New Custom Tokens

Define in `:root` and `.dark`, then expose to Tailwind with `@theme inline`:

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

Usage:
```tsx
<div className="bg-warning text-warning-foreground" />
```

## CSS Variables vs Utility Classes

### With CSS variables (default)
```tsx
<div className="bg-background text-foreground" />
```

### Without CSS variables
```bash
npx shadcn@latest init --no-css-variables
```
```tsx
<div className="bg-zinc-950 text-zinc-50 dark:bg-white dark:text-zinc-950" />
```

This is an installation-time choice. To switch, delete and re-install all
components.

## Base Colors

`tailwind.baseColor` in `components.json` controls which default token values
are generated.

Available: `neutral`, `stone`, `zinc`, `mauve`, `olive`, `mist`, `taupe`

## Dark Mode

Dark mode works by overriding tokens inside `.dark` selector.

```css
@custom-variant dark (&:is(.dark *));
```

The `.dark` class is added to the `<html>` element by your theme provider.
See the shadcn-dark-mode skill for framework-specific setup.

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/theming.mdx`
