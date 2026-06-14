# shadcn/ui — Tailwind v4 Upgrade Guide

> Before upgrading: read https://tailwindcss.com/docs/compatibility
> Tailwind v4 uses bleeding-edge browser features (modern browsers only).

## Step 1 — Follow the Tailwind v4 Upgrade Guide

```bash
# Use the official codemod to remove deprecated utilities and update config
npx @tailwindcss/upgrade@next
```

Full guide: https://tailwindcss.com/docs/upgrade-guide

## Step 2 — Update CSS variables

The codemod migrates CSS variables under the `@theme` directive:

```css
/* After codemod — works but not optimal */
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
  }
}

@theme {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
}
```

**Manual improvement — switch to `@theme inline`:**

1. Move `:root` and `.dark` out of `@layer base`
2. Wrap color values in `hsl()`
3. Change `@theme` to `@theme inline`
4. Remove `hsl()` wrappers from `@theme`

```css
/* Final result — recommended */
:root {
  --background: hsl(0 0% 100%);
  --foreground: hsl(0 0% 3.9%);
}

.dark {
  --background: hsl(0 0% 3.9%);
  --foreground: hsl(0 0% 98%);
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
}
```

This makes theme variables accessible both in utility classes and in JavaScript
(e.g. `var(--background)` directly, no `hsl()` wrapper needed).

New projects use OKLCH directly (no hsl wrapper needed at all):
```css
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
}
```

## Step 3 — Update chart colors

With `hsl()` baked into the CSS variable, remove the wrapper from `chartConfig`:

```diff
const chartConfig = {
  desktop: {
    label: "Desktop",
-   color: "hsl(var(--chart-1))",
+   color: "var(--chart-1)",
  },
}
```

## Step 4 — Use new size-* utility

```diff
- w-4 h-4
+ size-4
```

## Step 5 — Update dependencies

```bash
pnpm up "@radix-ui/*" cmdk lucide-react recharts tailwind-merge clsx --latest
```

## Step 6 — Remove forwardRef

### Option A: Codemod
```bash
# https://github.com/reactjs/react-codemod#remove-forward-ref
npx codemod remove-forward-ref
```

### Option B: Manual

Replace `React.forwardRef<...>` with `React.ComponentProps<...>`, remove `ref={ref}`,
add `data-slot` attribute.

Before:
```tsx
const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item
    ref={ref}
    className={cn("border-b last:border-b-0", className)}
    {...props}
  />
))
AccordionItem.displayName = "AccordionItem"
```

After:
```tsx
function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/tailwind-v4.mdx`
