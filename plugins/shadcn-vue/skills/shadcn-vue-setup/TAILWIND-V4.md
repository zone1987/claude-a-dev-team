# shadcn-vue: Tailwind v4

Tailwind v4 is fully supported. New projects start with v4 automatically.
Existing v3 projects keep working without changes.

## Key changes

- CLI initializes projects with Tailwind v4
- Full support for `@theme` and `@theme inline`
- All components updated for Tailwind v4
- Every primitive has a `data-slot` attribute (for CSS targeting)
- `toast` component deprecated in favor of `sonner`
- Buttons use the default cursor (no more `cursor-pointer` by default)
- `default` style deprecated, new projects use `new-york`
- HSL colors converted to OKLCH

Demo: https://v4.shadcn-vue.com

## Reference Files

- `TAILWIND-V4-DETAIL.md` — Complete What's New list, framework links,
  step-by-step upgrade: Tailwind upgrade guide + codemod, migrating CSS variables
  from HSL to OKLCH with @theme inline, using the size-* utility,
  updating dependencies (tw-animate-css, reka-ui, @lucide/vue, tailwind-merge, clsx)
