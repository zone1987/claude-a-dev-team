---
name: shadcn-button
description: >
  shadcn/ui Button component — versatile button with variants and sizes.
  Use when asked about Button, Schaltflaeche, shadcn button, buttonVariants,
  asChild button, icon button, loading button, shadcn/ui button component,
  outline ghost destructive secondary link button.
---

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

- `references/installation.md` — CLI and manual install
- `references/source.md` — full component source (Radix + Base)
- `references/api.md` — variants, sizes, props table
- `references/examples.md` — all examples with full code
- `references/base-vs-radix.md` — asChild vs render prop, link caveat
