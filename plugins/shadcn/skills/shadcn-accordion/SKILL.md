---
name: shadcn-accordion
description: >
  shadcn/ui Accordion component — vertically stacked interactive headings
  that reveal content sections. Use when asked about Accordion, Akkordeon,
  aufklappbare Inhalte, shadcn accordion, collapsible sections, shadcn/ui
  Accordion, AccordionItem, AccordionTrigger, AccordionContent.
---

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

- `references/installation.md` — CLI and manual install steps
- `references/source.md` — full component source (Radix + Base)
- `references/api.md` — props, anatomy, composition tree
- `references/examples.md` — all examples with full code
- `references/base-vs-radix.md` — differences between Base UI and Radix UI
