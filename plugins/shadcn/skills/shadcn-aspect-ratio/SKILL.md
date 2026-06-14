---
name: shadcn-aspect-ratio
description: >
  shadcn/ui AspectRatio component — displays content within a desired ratio.
  Use when asked about AspectRatio, Seitenverhaeltnis, shadcn aspect ratio,
  16/9 Bild, responsive image ratio, shadcn/ui aspect-ratio.
---

# shadcn/ui — Aspect Ratio

Displays content within a desired ratio. Wrapper around Radix UI
AspectRatio.Root (Radix version) or a pure CSS solution (Base version).

## Props

- `ratio` — number, e.g. `16/9`, `1/1`, `9/16` (required)
- `className` — custom classes

## Typical usage

Wrap an `<Image>` or video element. The Base version uses a CSS
`aspect-(--ratio)` custom property; the Radix version uses a padding-top
trick internally.

## Reference files

- `references/installation.md` — CLI and manual install
- `references/source.md` — full component source (Radix + Base)
- `references/api.md` — props table
- `references/examples.md` — demo, square, portrait examples
- `references/base-vs-radix.md` — implementation differences
