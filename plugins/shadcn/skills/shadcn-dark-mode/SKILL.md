---
name: shadcn-dark-mode
description: >
  shadcn/ui dark mode — framework-specific setup for Next.js, Vite, Astro,
  Remix, TanStack Start. next-themes, ThemeProvider, mode toggle component,
  FOUC prevention, .dark class, localStorage. Use when asked about dark mode,
  theme toggle, next-themes, ThemeProvider, light/dark mode shadcn.
---

# shadcn/ui — Dark Mode

Dark mode works by toggling the `.dark` class on the `<html>` element.
The `.dark` selector overrides the same CSS variable tokens.

```css
@custom-variant dark (&:is(.dark *));
```

## Framework setup

| Framework | Approach |
|-----------|---------|
| Next.js | `next-themes` package + ThemeProvider |
| Vite | Custom ThemeProvider with localStorage |
| Astro | Inline script in page head |
| Remix | `remix-themes` + server-side session cookie |
| TanStack Start | Custom ThemeProvider with ScriptOnce (FOUC prevention) |

## Reference files

- [references/next.md](references/next.md)
- [references/vite.md](references/vite.md)
- [references/astro.md](references/astro.md)
- [references/remix.md](references/remix.md)
- [references/tanstack-start.md](references/tanstack-start.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/dark-mode/`
