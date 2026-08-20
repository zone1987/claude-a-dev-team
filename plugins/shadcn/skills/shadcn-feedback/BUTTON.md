# shadcn/ui — Button

Displays a button or a component that looks like a button. Built on Radix UI
Slot (Radix version) or Base UI Button primitive (Base version).

## Variants

`default`, `outline`, `secondary`, `ghost`, `destructive`, `link`

## Sizes

`default`, `xs`, `sm`, `lg`, `icon`, `icon-xs`, `icon-sm`, `icon-lg`

## Key notes

- Radix: `asChild` prop renders children as the button
- Base: uses `ButtonPrimitive` from `@base-ui/react/button`; always applies
  `role="button"` — do NOT use for links, use `buttonVariants` + `<a>` instead
- `buttonVariants` helper exported for applying styles without `<Button>`

## Reference files

- `BUTTON-INSTALLATION.md` — CLI and manual install
- `BUTTON-SOURCE.md` — full component source (Radix + Base)
- `BUTTON-API.md` — variants, sizes, props table
- `BUTTON-EXAMPLES.md` — all examples with full code
- `BUTTON-BASE-VS-RADIX.md` — asChild vs render prop, link caveat
