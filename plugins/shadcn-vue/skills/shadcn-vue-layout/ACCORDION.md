# shadcn-vue: Accordion

Vertically stacked interactive headings that each reveal a section of content.
Built on top of reka-ui AccordionRoot. Supports `single` and `multiple` open modes,
collapsible mode, and disabled items.

## Sub-Components

- `Accordion` — Root container (wraps reka-ui AccordionRoot)
- `AccordionItem` — Individual collapsible item (requires unique `value`)
- `AccordionTrigger` — Clickable header that toggles the item; includes animated ChevronDown icon
- `AccordionContent` — Content panel with open/close animation

## Key Features

- Animated expand/collapse via `data-[state=open/closed]` Tailwind classes
- Disabled items via `:disabled="true"` on `AccordionItem`
- Custom icon slot on `AccordionTrigger` via `#icon`
- Fully accessible (WAI-ARIA)

## Reference Files

- `ACCORDION-INSTALLATION.md` — CLI and manual installation steps
- `ACCORDION-SOURCE.md` — Complete Vue source code for all component files
- `ACCORDION-API.md` — Props, slots, reka-ui API link
- `ACCORDION-EXAMPLES.md` — All demo examples with full code
