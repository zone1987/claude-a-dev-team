# shadcn-vue: Tailwind v4

Tailwind v4 is fully supported. New projects start with v4 by default.
Existing v3 projects continue to work unchanged.

Demo: https://v4.shadcn-vue.com

## What's New in shadcn-vue for Tailwind v4

- The CLI initializes projects with Tailwind v4
- Full support for the new `@theme` directive and `@theme inline` option
- All components updated for Tailwind v4
- Every primitive has a `data-slot` attribute for CSS targeting
- `toast` component deprecated in favor of `sonner`
- Buttons now use the default cursor (no `cursor-pointer` by default)
- `default` style deprecated; new projects use `new-york`
- HSL colors converted to OKLCH

**Non-breaking:** Existing Tailwind v3 apps still work. New components will be v3
until you upgrade. Only new projects start with v4.

## Getting Started (New Projects)

See framework-specific guides:
- Vite: `/docs/installation/vite`
- Nuxt: `/docs/installation/nuxt`
- Astro: `/docs/installation/astro`
- Laravel: `/docs/installation/laravel`

## Upgrading Existing Projects

**Important:** Read the Tailwind v4 Compatibility Docs first:
https://tailwindcss.com/docs/compatibility

Tailwind v4 uses bleeding-edge browser features and is designed for modern browsers.

### Step 1: Follow the Tailwind v4 Upgrade Guide

```bash
# Official upgrade guide: https://tailwindcss.com/docs/upgrade-guide
# Use the codemod to remove deprecated utilities and update tailwind config:
npx @tailwindcss/upgrade@next
```

### Step 2: Update CSS Variables

The codemod migrates CSS variables as references under `@theme`:

```css
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

To use `@theme inline` (recommended):

1. Move `:root` and `.dark` out of `@layer base`
2. Wrap the color values in `hsl()`
3. Change `@theme` to `@theme inline`
4. Remove the `hsl()` wrappers from `@theme`

```css
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

This makes color values accessible both in utility classes and in JavaScript.

### Step 3: Use size-* utility

Replace `w-* h-*` pairs with the new `size-*` utility (supported by tailwind-merge):

```diff
- w-4 h-4
+ size-4
```

### Step 4: Update dependencies

```bash
pnpm i tw-animate-css
pnpm up reka-ui @lucide/vue tailwind-merge clsx --latest
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/.tailwind-v4.md`
