# shadcn/ui Tailwind v4 Changelog

## March 19, 2025 — Deprecate tailwindcss-animate

`tailwindcss-animate` is deprecated in favour of `tw-animate-css`.

New projects have `tw-animate-css` by default.

To migrate existing projects:

1. Remove `tailwindcss-animate` from dependencies.
2. Remove `@plugin 'tailwindcss-animate'` from globals.css.
3. Install `tw-animate-css` as dev dependency.
4. Add `@import "tw-animate-css"` to globals.css.

```diff
- @plugin 'tailwindcss-animate';
+ @import "tw-animate-css";
```

## March 12, 2025 — New Dark Mode Colors

Revisited dark mode colors for improved accessibility.

**Applies only to new Tailwind v4 projects (not upgraded ones).**

To update:

1. Commit your changes first (CLI will overwrite components)
2. Re-add all components:
   ```bash
   npx shadcn@latest add --all --overwrite
   ```
3. Update dark mode colors in `globals.css` to new OKLCH values.
4. Review and re-apply any customizations.

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/tailwind-v4.mdx`
