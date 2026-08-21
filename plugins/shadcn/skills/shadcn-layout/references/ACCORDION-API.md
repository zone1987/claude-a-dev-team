# Accordion — API Reference

## Composition

```
Accordion
├── AccordionItem
│   ├── AccordionTrigger
│   └── AccordionContent
└── AccordionItem
    ├── AccordionTrigger
    └── AccordionContent
```

## Accordion (Root)

| Prop | Type | Default | Notes |
|------|------|---------|-------|
| `type` | `"single" \| "multiple"` | required | Single or multiple panels |
| `collapsible` | `boolean` | `false` | Allow closing in single mode |
| `defaultValue` | `string \| string[]` | — | Initially open value(s) |
| `value` | `string \| string[]` | — | Controlled value |
| `onValueChange` | `function` | — | Change handler |

## AccordionItem

| Prop | Type | Default |
|------|------|---------|
| `value` | `string` | required |
| `disabled` | `boolean` | `false` |
| `className` | `string` | — |

## AccordionTrigger

Extends `button` element. Renders chevron icon automatically.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |
| `children` | `ReactNode` | — |

## AccordionContent

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |
| `children` | `ReactNode` | — |

## data-slot values

- `data-slot="accordion"` — root
- `data-slot="accordion-item"` — item
- `data-slot="accordion-trigger"` — trigger button
- `data-slot="accordion-content"` — content panel

## External API docs

- Radix UI: https://www.radix-ui.com/primitives/docs/components/accordion#api-reference
- Base UI: https://base-ui.com/react/components/accordion#api-reference

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/accordion.mdx`
