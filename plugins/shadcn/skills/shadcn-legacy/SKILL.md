---
name: shadcn-legacy
description: >
  shadcn/ui legacy docs — Tailwind v3 documentation. Use when asked about
  shadcn Tailwind v3, legacy shadcn, old shadcn docs, v3.shadcn.com,
  shadcn v3, old documentation.
---

# shadcn/ui — Legacy Docs (Tailwind v3)

The current documentation covers shadcn/ui with Tailwind v4.

For Tailwind v3 documentation, see:

**Legacy docs:** https://v3.shadcn.com

Key differences in v3:
- Uses HSL color format instead of OKLCH
- `tailwind.config.js` is required (not blank)
- `tailwindcss-animate` instead of `tw-animate-css`
- Components use `React.forwardRef` pattern
- No `data-slot` attributes
- `default` style available (now deprecated)
- CSS variables use `hsl()` wrapper: `hsl(var(--primary))`

When using Tailwind v3, set `tailwind.config` in `components.json`:
```json
{
  "tailwind": {
    "config": "tailwind.config.js"
  }
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/legacy.mdx`
