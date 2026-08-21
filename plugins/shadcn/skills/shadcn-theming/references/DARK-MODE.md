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

- [DARK-MODE-NEXT.md](DARK-MODE-NEXT.md)
- [DARK-MODE-VITE.md](DARK-MODE-VITE.md)
- [DARK-MODE-ASTRO.md](DARK-MODE-ASTRO.md)
- [DARK-MODE-REMIX.md](DARK-MODE-REMIX.md)
- [DARK-MODE-TANSTACK-START.md](DARK-MODE-TANSTACK-START.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/dark-mode/`
