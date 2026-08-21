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

- `ASPECT-RATIO-INSTALLATION.md` — CLI and manual install
- `ASPECT-RATIO-SOURCE.md` — full component source (Radix + Base)
- `ASPECT-RATIO-API.md` — props table
- `ASPECT-RATIO-EXAMPLES.md` — demo, square, portrait examples
- `ASPECT-RATIO-BASE-VS-RADIX.md` — implementation differences
