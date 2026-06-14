---
name: shadcn-typography
description: >
  shadcn/ui Typography — heading h1 h2 h3 h4 paragraph blockquote list table
  inline-code lead large small muted text styles, Typografie, Textgestaltung,
  shadcn typography, Tailwind text styles, prose styles
---

# shadcn/ui Typography

Utility class patterns for styling headings, paragraphs, lists, blockquotes, tables, and
other text elements. No component file — apply Tailwind classes directly to HTML elements.

> shadcn/ui does not ship typography styles by default. Use these utility class patterns
> to style your text.

## Quick Reference

No installation needed — these are plain Tailwind classes.

| Element | Key classes |
|---------|-------------|
| `h1` | `scroll-m-20 text-4xl font-extrabold tracking-tight text-balance` |
| `h2` | `scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0` |
| `h3` | `scroll-m-20 text-2xl font-semibold tracking-tight` |
| `h4` | `scroll-m-20 text-xl font-semibold tracking-tight` |
| `p` | `leading-7 [&:not(:first-child)]:mt-6` |
| `blockquote` | `mt-6 border-l-2 pl-6 italic` |
| `code` | `relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold` |
| `lead` | `text-xl text-muted-foreground` |
| `large` | `text-lg font-semibold` |
| `small` | `text-sm leading-none font-medium` |
| `muted` | `text-sm text-muted-foreground` |

## Reference files

- [classes.md](references/classes.md) — All element classes with full documentation
- [examples.md](references/examples.md) — All individual examples + full demo
