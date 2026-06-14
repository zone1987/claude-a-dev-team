# Accordion — API Reference

reka-ui API: https://reka-ui.com/docs/components/accordion#api-reference

## Anatomy

```vue
<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Title</AccordionTrigger>
    <AccordionContent>Content</AccordionContent>
  </AccordionItem>
</Accordion>
```

## Accordion (Root)

Forwards all props/emits to `AccordionRoot` from reka-ui.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `"single" \| "multiple"` | — | Whether one or multiple items can be open |
| `collapsible` | `boolean` | `false` | Allow closing open item (single mode only) |
| `defaultValue` | `string \| string[]` | — | Default open item(s) |
| `modelValue` / `v-model` | `string \| string[]` | — | Controlled open state |
| `disabled` | `boolean` | `false` | Disable entire accordion |
| `dir` | `"ltr" \| "rtl"` | `"ltr"` | Reading direction |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` | Orientation |

**Emits:** `update:modelValue`

**Slots:** default (receives `{ modelValue }`)

## AccordionItem

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | — | **Required.** Unique identifier |
| `disabled` | `boolean` | `false` | Disable this item |
| `class` | `string` | — | Additional CSS classes |

**Slots:** default (receives `{ open: boolean }`)

## AccordionTrigger

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |
| `asChild` | `boolean` | `false` | Render as child element |

**Named Slots:**
- `default` — Trigger label content
- `#icon` — Override the default ChevronDown icon

## AccordionContent

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Applied to inner `<div>` |
| `asChild` | `boolean` | `false` | Render as child element |
| `forceMount` | `boolean` | `false` | Force mount even when closed |

---
Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/accordion.md`, `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/accordion/`
