# shadcn/ui — Accordion

A vertically stacked set of interactive headings that each reveal a section
of content. Built on Radix UI (default) or Base UI primitives.

## Sub-components

- `Accordion` — root container
- `AccordionItem` — single panel with `value` prop
- `AccordionTrigger` — clickable header; chevron rotates when open
- `AccordionContent` — animated body; wraps children in a padding div

## Key props

- `type="single"` (one open at a time) or `type="multiple"` (many)
- `collapsible` — allow closing the active item (single mode)
- `defaultValue` — initially open item value(s)
- `disabled` on `AccordionItem` — disables that panel

## Reference files

- `ACCORDION-INSTALLATION.md` — CLI and manual install steps
- `ACCORDION-SOURCE.md` — full component source (Radix + Base)
- `ACCORDION-API.md` — props, anatomy, composition tree
- `ACCORDION-EXAMPLES.md` — all examples with full code
- `ACCORDION-BASE-VS-RADIX.md` — differences between Base UI and Radix UI
